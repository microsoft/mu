# @file DocBuild.py
# This tool supports doc collection for a code tree.  This is a prep step before using
# mkdocs
#
##
# Copyright (c) 2018, Microsoft Corporation
#
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
##
###

import os
import sys
import argparse
import logging
import shutil
import datetime
import time
import subprocess
from Utf8Test import EncodingCheck
import yaml


SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))
VERSION = "0.8.0"

#
# Class with basic git support.  Allow data collection from git repo
#


class GitSupport(object):

    def get_url(self, path):
        cmd = "git config --get remote.origin.url"
        pipe = subprocess.Popen(cmd, shell=True, cwd=path,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out, error) = pipe.communicate()
        pipe.wait()
        return out.decode().strip()

    def get_branch(self, path):
        cmd = "git rev-parse --abbrev-ref HEAD"
        pipe = subprocess.Popen(cmd, shell=True, cwd=path,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out, error) = pipe.communicate()
        pipe.wait()
        return out.decode().strip()

    def get_commit(self, path):
        cmd = "git rev-parse HEAD"
        pipe = subprocess.Popen(cmd, shell=True, cwd=path,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out, error) = pipe.communicate()
        pipe.wait()
        return out.decode().strip()

    def get_date(self, path, commit):
        cmd = "git show -s --format=%ci " + commit
        pipe = subprocess.Popen(cmd, shell=True, cwd=path,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out, error) = pipe.communicate()
        pipe.wait()
        return out.decode().strip()

    def make_commit_url(self, commit, url):
        cl = url
        if(url.endswith(".git")):  # github address scheme
            cl = url[:-4]
        return cl + "/commit/" + commit


#
# Simple Tree object for collecting navigation
# and outputing in YML format.
#
class NavTree(object):

    SPECIAL_KEY_FIND_PKG_DOCS = "Docs"  # this is the name of folder at package root with Package Docs
    SPECIAL_KEY_REPLACE_WITH = "Package Overview"  # this will be in the TOC as container for package Docs
    SPECIAL_KEY_PACKAGE_MODULES = "Modules"  # this will be in the TOC as container for all docs found with code

    def __init__(self, Leaf=None):
        self.Leaf = Leaf
        self.Children = {}

    def __str__(self):
        if(self.Leaf is not None):
            return "(Leaf: " + self.Leaf + ")"
        else:
            st = "(Children:"
            for (k, v) in self.Children.items():
                st += "[" + k + ":" + str(v) + "]" + "\n"
            return st

    #
    # to support node iteration create function
    # to return the node.  The returned node could
    # be a new node or an existing node.
    #
    # name is node name
    # leaf is md path.  None if intermediate node
    #
    def GetOrMakeChildNode(self, name, leaf=None):
        if name in self.Children.keys():
            if leaf is not None:
                raise Exception(
                    "Can't make child with same name {}".format(name))
            else:
                return self.Children[name]

        # This is the Make Path
        t = NavTree(leaf)
        self.Children[name] = t
        return t

    #
    # Make Tree nodes for a given path
    #
    def AddToTree(self, path, leafvalue):
        if(path is None):
            return
        p = path.partition("/")  # p[0] = name p[2] = remaining
        if(len(p[2]) > 0):
            rem = p[2]
            # Dev Note: it was decided that a "Docs" folder found at the root of a Edk2 Package
            #           should be treated special and that all markdown files found with the code (in modules)
            #           should lowered one level in TOC by adding a "Module" node.
            if p[0].endswith("Pkg") and not p[2].startswith(NavTree.SPECIAL_KEY_FIND_PKG_DOCS):
                rem = NavTree.SPECIAL_KEY_PACKAGE_MODULES + "/" + p[2]
            self.GetOrMakeChildNode(p[0]).AddToTree(rem, leafvalue)
        else:
            self.GetOrMakeChildNode(p[0], leafvalue)
        return

    #
    # Output yaml for the tree
    #
    def GetNavYml(self, string, prefix):
        if self.Leaf is not None:
            return string + ' "' + self.Leaf + '"'
        string2 = ""

        # Dev Note: it was decided that a "Docs" folder found at the root of a Edk2 Package
        #           should be treated special and put first in the TOC within the Package.  It also
        #           should be renamed to something more descriptive than docs
        #
        if(NavTree.SPECIAL_KEY_FIND_PKG_DOCS in self.Children.keys()):
            string1 = "\n" + prefix + "- " + self.MakeFriendly(NavTree.SPECIAL_KEY_REPLACE_WITH) + ":"
            string2 += self.Children[NavTree.SPECIAL_KEY_FIND_PKG_DOCS].GetNavYml(string1, prefix + "  ")

        for (name, cnode) in self.Children.items():
            if name == NavTree.SPECIAL_KEY_FIND_PKG_DOCS:
                # already inserted above
                continue
            string1 = "\n" + prefix + "- " + self.MakeFriendly(name) + ":"
            string2 += cnode.GetNavYml(string1, prefix + "  ")
        return string + string2

    #
    # When generating the nav convert visible names
    # to something more human readable
    #
    # Currently support changing snake_case and CamelCase
    #
    def MakeFriendly(self, string):
        string = string.replace("_", " ").strip()  # strip snake case
        string = ' '.join(string.split())  # strip duplicate spaces

        # Handle camel case
        newstring = ""
        prev_char_lowercase = False
        for i in string:
            if(not prev_char_lowercase):
                newstring += i
            else:
                if(i.isupper()):
                    newstring += " " + i
                else:
                    newstring += i
            prev_char_lowercase = i.islower()

        return newstring

    #
    # Collapse when there is only a single node with a leaf
    #
    def Collapse(self):
        if self.Leaf is not None:
            return self

        if(len(self.Children) == 1):
            for (name, cnode) in self.Children.items():
                leaf = cnode.Collapse()
                if(leaf is not None):
                    self.Leaf = leaf.Leaf
                    self.Children = {}
        else:
            for (name, cnode) in self.Children.items():
                cnode.Collapse()
        return


#
# Main class which runs Documentation build work
# This helps find all markdown files in source trees
# and copys them to the mkdocs project
#
# This also collects repo information and adds to yml
# file so markdown pages can use the data for display
#
# Finally it must create the complex nav structure
# required for mkdocs
#
#
class DocBuild(object):
    DYNFOLDER = "dyn"
    #
    # constructor that creates the DocBuild object
    #

    def __init__(self, RootDir, OutputDir, YmlFile):

        self.RootDirectory = None
        self.YmlFilePathBase = None
        self.YmlFilePathOut = None
        self.OutputDirectory = None
        self.MdFiles = list()
        self.Repos = dict()
        self.EncodingChecker = EncodingCheck()
        self.ExtraContents = dict()

        # Convert RootDir to abs and confirm valid
        if(RootDir is not None):
            if(os.path.isabs(RootDir)):
                self.RootDirectory = RootDir
            else:
                self.RootDirectory = os.path.join(
                    os.path.abspath(os.getcwd()), RootDir)
            self.RootDirectory = os.path.realpath(self.RootDirectory)
            if(not os.path.isdir(self.RootDirectory)):
                raise Exception(
                    "Invalid Path for RootDir: {0}".format(self.RootDirectory))

        # Convert YmlFile to abs and confirm valid
        if(YmlFile is not None):
            if(os.path.isabs(YmlFile)):
                self.YmlFilePathBase = YmlFile
            else:
                self.YmlFilePathBase = os.path.join(
                    os.path.abspath(os.getcwd()), YmlFile)
            self.YmlFilePathBase = os.path.realpath(self.YmlFilePathBase)
            if(not os.path.isfile(self.YmlFilePathBase)):
                raise Exception(
                    "Invalid Path for YmlFile: {0}".format(self.YmlFilePathBase))

            self.YmlFilePathOut = os.path.join(
                os.path.dirname(self.YmlFilePathBase), "mkdocs.yml")

        # Convert OutputDir to abs and then mkdir if necessary
        if(OutputDir is not None):
            if(os.path.isabs(OutputDir)):
                self.OutputDirectory = OutputDir
            else:
                self.OutputDirectory = os.path.join(
                    os.path.abspath(os.getcwd()), OutputDir)
            self.OutputDirectory = os.path.realpath(self.OutputDirectory)

            if(os.path.basename(self.OutputDirectory) != "docs"):
                raise Exception(
                    "For mkdocs we only support output dir of docs. OutputDir: %s" % self.OutputDirectory)
            # set output to the dynamic folder
            self.OutputDirectory = os.path.join(OutputDir, DocBuild.DYNFOLDER)
            if(not os.path.isdir(self.OutputDirectory)):
                logging.debug("Output directory doesn't exist.  Making... {0}".format(
                    self.OutputDirectory))
                os.makedirs(self.OutputDirectory)

        # add all variables and functions here
        self.ExtraContents["version"] = VERSION
        self.ExtraContents["buildtime"] = str(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.ExtraContents["social"] = [
            {"type": 'github', "link": 'https://github.com/microsoft/mu'}]

    #
    # delete the outputdirectory
    #
    def Clean(self):
        retry = 1  # hack to make rmtree more successful
        while True:
            try:
                if(self.OutputDirectory is not None and os.path.isdir(self.OutputDirectory)):
                    shutil.rmtree(self.OutputDirectory)
            except OSError:
                if not retry:
                    # If we're out of retries, bail.
                    raise Exception(
                        "Failed to Clean dir {0}".format(self.OutputDirectory))
                time.sleep(2)
                retry -= 1
                continue
            break

        if(os.path.isfile(self.YmlFilePathOut)):
            os.remove(self.YmlFilePathOut)

    ###########################################################################################
    # Process functions - Start
    ###########################################################################################

    #
    # Process md files.  Make folders in output and copy
    #
    # @apath - absolute path to md file
    #

    def _ProcessMarkdownFile(self, apath):
        # Add relative path to list of md files
        rpath = os.path.relpath(apath, self.RootDirectory)
        self.MdFiles.append(rpath)
        logging.debug("md file found: {0}".format(rpath))

        # Copy to output dir
        s = apath
        d = os.path.join(self.OutputDirectory, rpath)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        shutil.copy2(s, d)

    #
    # Process Dec files.  Collect info add add to list
    #
    # @apath - absolute path to dec file
    #
    def _ProcessEdk2DecFile(self, apath):
        pass

    def _ProcessImageFile(self, apath):
        rpath = os.path.relpath(apath, self.RootDirectory)
        logging.debug("image file found: {0}".format(rpath))
        # Copy to output dir
        s = apath
        d = os.path.join(self.OutputDirectory, rpath)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        shutil.copy2(s, d)

    #
    # Process git repo.  Collect git stats
    #
    # dirpath - absolute path for root of git directory
    #

    def _ProcessGitRepo(self, dirpath):
        name = os.path.basename(dirpath)
        u = GitSupport().get_url(dirpath)
        b = GitSupport().get_branch(dirpath)
        c = GitSupport().get_commit(dirpath)
        d = GitSupport().get_date(dirpath, c)
        cl = GitSupport().make_commit_url(c, u)
        obj = {"url": u, "branch": b, "commit": c, "date": d, "commitlink": cl}
        self.Repos[name] = obj

    ###########################################################################################
    # Process functions - End
    ###########################################################################################

    #
    # walk the RootDirectory looking for md files
    #  #Copy the md files to OutputDirectory
    #
    # Also look for git repository roots
    #  #Collect more data about repos
    #
    #

    def ProcessRootDir(self):
        if(self.RootDirectory is None):
            logging.debug("ProcessRootDir: No RootDirectory set.")
            return

        if self.OutputDirectory is None:
            logging.debug("ProcessRootDir: No OutputDirectory set.")
            return

        for top, dirs, files in os.walk(self.RootDirectory):
            for f in files:
                if f.lower().endswith(".md"):
                    if(not self.EncodingChecker.TestMdEncodingOk(os.path.join(top, f), "utf-8")):
                        logging.error("Ignore Invalid markdown file: {0}".format(
                            os.path.join(top, f)))
                    else:
                        self._ProcessMarkdownFile(os.path.join(top, f))

                elif f.lower().endswith(".dec"):
                    self._ProcessEdk2DecFile(os.path.join(top, f))

                elif f.lower().endswith(("_mu.gif", "_mu.png", "_mu.jpg")):
                    self._ProcessImageFile(os.path.join(top, f))

            if(".git" in dirs):
                # root of git repo
                self._ProcessGitRepo(top)
        return 0

    def MakeYml(self):
        f = open(self.YmlFilePathBase, "r")
        f2 = open(self.YmlFilePathOut, 'w')
        for l in f:
            f2.write(l)

        # now parse as yaml
        f.seek(0)
        # yaml.load(f)
        # IMPORTANT NOTE: This call to "unsafe_load()" is only acceptable because we control the yml file being loaded.
        #                   Unsafe load is required to support some configuration options for pymdownx.
        if "extra" in yaml.unsafe_load(f):
            raise Exception(
                "extra: member not allowed in mkdocs_base.yml.  Please add the contents to DocBuild constructor instead.  ")
        f.close()
        self.Yml = f2

    def CloseYml(self):
        if self.Yml is not None:
            self.Yml.close()

        with open(self.YmlFilePathOut, 'r') as a:
            logging.debug("FINAL YML file")
            logging.debug(a.read())

    #
    # Make yml nav output for the dynamic content
    # Write it to the yml file
    #
    def MakeNav(self):

        if self.YmlFilePathBase is None:
            logging.debug("MakeNav: No YmlFilePathBase set.")
            return

        if self.RootDirectory is None:
            logging.debug("MakeNav: No RootDirectory set.")
            return

        if self.OutputDirectory is None:
            logging.debug("MakeNav: No OutputDirectory set.")
            return

        root = self._MakeNavTree()
        root.Collapse()
        navstring = root.GetNavYml("", "    ")

        self.Yml.write("\n  - Code Repositories:")
        self.Yml.write(navstring)

    #
    # Make yml config data for each repo
    # Write it to the yml file
    #
    def MakeRepoInfo(self):

        if self.Yml is None:
            logging.debug("MakeRepoInfo: No open Yml file.")
            return

        if self.RootDirectory is None:
            logging.debug("MakeRepoInfo: No RootDirectory set.")
            return

        if self.OutputDirectory is None:
            logging.debug("MakeRepoInfo: No OutputDirectory set.")
            return

        logging.debug(str(self.Repos))
        self.ExtraContents.update(self.Repos)

    def WriteExtra(self):
        if self.Yml is None:
            logging.debug("WriteExtra: No open Yml file.")
            return
        self.Yml.write("\n#AutoGenerated based on ExtraContents in DocBuild\n")
        yaml.dump({"extra": self.ExtraContents},
                  self.Yml, default_flow_style=False)

    #
    # Internal function
    def _MakeNavTree(self):
        root = NavTree()
        for a in self.MdFiles:
            string1 = a.replace(os.sep, "/")
            string2 = string1.rpartition(".")[0]  # remove the md extension
            # this is intentionally not os.sep
            root.AddToTree(string2, DocBuild.DYNFOLDER + "/" + string1)
        logging.debug(root)
        return root


####################################################################################################################################
### GLOBAL ###
####################################################################################################################################

def GatherArguments():
    # Arg Parse
    parser = argparse.ArgumentParser(description='DocBuild ')
    parser.add_argument("--Build", "--build", dest="Build",
                        action="store_true", help="Build", default=False)
    parser.add_argument("--Clean", "--clean", dest="Clean", action="store_true",
                        help="Delete Dynamic Output Directory and Clean Yml", default=False)
    parser.add_argument('--OutputDir', "--outputdir", "--Outputdir",
                        dest="OutputDir", help="Path to output folder. The mkdocs docs directory.")
    parser.add_argument('--yml', dest="YmlFilePath",
                        help="<Required>Path to yml base file", required=True)
    parser.add_argument('--RootDir', '--rootdir', '--Rootdir', dest="RootDir",
                        help="Path to Root Directory to search for repos and md files.  Only set for dynamic content builds")
    parser.add_argument('-o', "--OutputLog", '--outputlog',
                        dest="OutputLog", help="Create an output log file")
    return parser.parse_args()


def main():
    args = GatherArguments()

    # setup file based logging if outputReport specified
    if(args.OutputLog):
        if(len(args.OutputLog) < 2):
            logging.critical("the output log file parameter is invalid")
            return -2

        # setup file based logging
        filelogger = logging.FileHandler(filename=args.OutputLog, mode='w')
        filelogger.setLevel(logging.DEBUG)
        filelogger.setFormatter(formatter)
        logging.getLogger('').addHandler(filelogger)

    logging.info("Log Started: " + datetime.datetime.strftime(
        datetime.datetime.now(), "%A, %B %d, %Y %I:%M%p"))

    # logging.debug("Script Path is %s" % SCRIPT_PATH)
    Build = DocBuild(args.RootDir, args.OutputDir, args.YmlFilePath)
    logging.info("Root Directory For Doc Scanning: {0}".format(
        Build.RootDirectory))
    logging.info("Output Directory For Docs: {0}".format(
        Build.OutputDirectory))

    if(args.Clean):
        logging.critical("Clean")
        Build.Clean()

    if(not args.Build):
        return 0

    logging.critical("Build")

    Build.MakeYml()
    if(args.OutputDir is not None):
        Build.ProcessRootDir()
        Build.MakeNav()
        Build.MakeRepoInfo()
    Build.WriteExtra()
    Build.CloseYml()

    return 0


if __name__ == '__main__':
    # setup main console as logger
    logger = logging.getLogger('')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    console = logging.StreamHandler()
    console.setLevel(logging.CRITICAL)
    console.setFormatter(formatter)
    logger.addHandler(console)

    # call main worker function
    retcode = main()

    if retcode != 0:
        logging.critical("Failed.  Return Code: %d" % retcode)
    else:
        logging.critical("Success!")
    # end logging
    logging.shutdown()
    sys.exit(retcode)
