## @file DocBuild.py
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

from __future__ import print_function  #support Python3 and 2 for print
import os
import sys
import argparse
import logging
import shutil
import datetime
import time
import subprocess


SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

#
# Class with basic git support.  Allow data collection from git repo
#
class GitSupport(object):

    def get_url(self, path):
        cmd = "git config --get remote.origin.url"
        pipe = subprocess.Popen(cmd, shell=True, cwd=path,stdout = subprocess.PIPE,stderr = subprocess.PIPE )
        (out, error) = pipe.communicate()
        pipe.wait()
        return out.decode().strip()

    def get_branch(self, path):        
        cmd = "git rev-parse --abbrev-ref HEAD"
        pipe = subprocess.Popen(cmd, shell=True, cwd=path,stdout = subprocess.PIPE,stderr = subprocess.PIPE )
        (out, error) = pipe.communicate()
        pipe.wait()
        return out.decode().strip()
    
    def get_commit(self, path):        
        cmd = "git rev-parse HEAD"
        pipe = subprocess.Popen(cmd, shell=True, cwd=path,stdout = subprocess.PIPE,stderr = subprocess.PIPE )
        (out, error) = pipe.communicate()
        pipe.wait()
        return out.decode().strip()

    def get_date(self, path, commit):
        cmd = "git show -s --format=%ci " + commit
        d = "????"
        pipe = subprocess.Popen(cmd, shell=True, cwd=path,stdout = subprocess.PIPE,stderr = subprocess.PIPE )
        (out, error) = pipe.communicate()
        pipe.wait()
        return out.decode().strip()

    def make_commit_url(self, commit, url):
        cl = url
        if(url.endswith(".git")): #github address scheme
            cl = url[:-4]
        return cl + "/commit/" + commit


#
# Simple Tree object for collecting navigation
# and outputing in YML format.
#
class NavTree(object):

    def __init__(self, Leaf=None):
        self.Leaf = Leaf
        self.Children = {}

    def __str__(self):
        if(self.Leaf is not None):
            return "(Leaf: " + self.Leaf + ")"
        else:
            st = "(Children:"
            for (k,v) in self.Children.items(): 
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
                raise Exception("Can't make child with same name {}".format(name))
            else:
                return self.Children[name]

        #This is the Make Path
        t = NavTree(leaf)
        self.Children[name] = t
        return t

    #
    # Make Tree nodes for a given path
    #
    def AddToTree(self, path, leafvalue):
        if(path == None):
            return
        p = path.partition("/")  # p[0] = name p[2] = remaining
        if( len(p[2]) > 0):
            self.GetOrMakeChildNode(p[0]).AddToTree(p[2], leafvalue)
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
        for (name, cnode) in self.Children.items():
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
        string = string.replace("_", " ").strip()

        newstring = ""
        for i in string:
            #don't mess with first char
            if(newstring == ""):
                newstring += i
            elif(i.isupper()):
                newstring += " " + i
            else:
                newstring += i

        return newstring

    #
    # Collapse when there is only a single node with a leaf
    #
    def Collapse(self):
        if self.Leaf is not None:
            return self

        if(len(self.Children) == 1):
            for (name, cnode) in self.Children.items():
                l = cnode.Collapse()
                if(l is not None):
                    self.Leaf = l.Leaf
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

        #Convert RootDir to abs and confirm valid
        if(RootDir is not None):
            if(os.path.isabs(RootDir)):
                self.RootDirectory = RootDir
            else:
                self.RootDirectory = os.path.join(os.path.abspath(os.getcwd()), RootDir)
            self.RootDirectory = os.path.realpath(self.RootDirectory)
            if(not os.path.isdir(self.RootDirectory)):
                raise Exception("Invalid Path for RootDir: {0}".format(self.RootDirectory))

        #Convert YmlFile to abs and confirm valid
        if(YmlFile is not None):
            if(os.path.isabs(YmlFile)):
                self.YmlFilePathBase = YmlFile
            else:
                self.YmlFilePathBase = os.path.join(os.path.abspath(os.getcwd()), YmlFile)
            self.YmlFilePathBase = os.path.realpath(self.YmlFilePathBase)
            if(not os.path.isfile(self.YmlFilePathBase)):
                raise Exception("Invalid Path for YmlFile: {0}".format(self.YmlFilePathBase))
            
            self.YmlFilePathOut = os.path.join(os.path.dirname(self.YmlFilePathBase), "mkdocs.yml")

        #Convert OutputDir to abs and then mkdir if necessary
        if(OutputDir is not None):        
            if(os.path.isabs(OutputDir)):
                self.OutputDirectory = OutputDir
            else:
                self.OutputDirectory = os.path.join(os.path.abspath(os.getcwd()), OutputDir)
            self.OutputDirectory = os.path.realpath(self.OutputDirectory)

            if(os.path.basename(self.OutputDirectory) != "docs"):
                raise Exception("For mkdocs we only support output dir of docs. OutputDir: %s" % self.OutputDirectory)
            self.OutputDirectory = os.path.join(OutputDir, DocBuild.DYNFOLDER) #set output to the dynamic folder
            if(not os.path.isdir(self.OutputDirectory)):
                logging.debug("Output directory doesn't exist.  Making... {0}".format(self.OutputDirectory))
                os.makedirs(self.OutputDirectory)

    #
    # delete the outputdirectory
    #
    def Clean(self):
        retry = 1  #hack to make rmtree more successful
        while True:
            try:
                if(self.OutputDirectory is not None and os.path.isdir(self.OutputDirectory)):
                    shutil.rmtree(self.OutputDirectory)
            except OSError:
                if not retry:
                    # If we're out of retries, bail.
                    raise Exception("Failed to Clean dir {0}".format(self.OutputDirectory))
                time.sleep(2)
                retry -= 1
                continue
            break

        if(os.path.isfile(self.YmlFilePathOut)):
            os.remove(self.YmlFilePathOut)
        
    
    ###########################################################################################
    ## Process functions - Start
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

        #Copy to output dir
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
        cl= GitSupport().make_commit_url(c,u)
        obj = { "url": u, "branch": b, "commit": c, "date": d, "commitlink": cl}
        self.Repos[name] = obj

    ###########################################################################################
    ## Process functions - End
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
            return

        for top, dirs, files in os.walk(self.RootDirectory):
            for f in files:
                if f.lower().endswith(".md"):
                    self._ProcessMarkdownFile(os.path.join(top, f))
                elif f.lower().endswith(".dec"):
                    self._ProcessEdk2DecFile(os.path.join(top, f))
            
            if(".git" in dirs):
                #root of git repo
                self._ProcessGitRepo(top)
        return 0

    def MakeYml(self):
        f = open(self.YmlFilePathBase, "r")
        f2 = open(self.YmlFilePathOut, 'w')
        for l in f:
            f2.write(l)
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
            return

        #navstring = self.__MakeNavTree().GetNavYml("", "    ")
        #logging.debug("NavString: " + navstring)
        root = self._MakeNavTree()
        root.Collapse()
        navstring = root.GetNavYml("", "    ")
        #logging.debug("NavString: " + navstring)

        self.Yml.write("\n  - Code Repositories:")
        self.Yml.write(navstring)

    #
    # Make yml config data for each repo
    # Write it to the yml file
    #
    def MakeRepoInfo(self):

        self.Yml.write("\nextra:\n")

        for (k,v) in self.Repos.items():
            logging.debug(k + str(v))
            self.Yml.write("  " + k + ":\n")
            self.Yml.write("    url: " + v["url"] + "\n")
            self.Yml.write("    commit: " + v["commit"] + "\n")
            self.Yml.write("    branch: " + v["branch"] + "\n")
            self.Yml.write("    commitlink: " + v["commitlink"] + "\n")
            self.Yml.write("    date: " + v["date"] + "\n")

    #
    # Internal function 
    def _MakeNavTree(self):
        root = NavTree()
        for a in self.MdFiles:
            string1 = a.replace(os.sep, "/")
            string2 = string1.partition(".")[0]
            root.AddToTree(string2, DocBuild.DYNFOLDER+ "/"+ string1)
        logging.debug(root)
        return root


####################################################################################################################################
### GLOBAL ###
####################################################################################################################################

def GatherArguments():
  #Arg Parse
  parser = argparse.ArgumentParser(description='DocBuild ')
  parser.add_argument("--Build", "--build", dest="Build", action="store_true", help="Build", default=False)
  parser.add_argument("--Clean", "--clean", dest="Clean", action="store_true", help="Delete Dynamic Output Directory and Clean Yml", default=False)
  parser.add_argument('--OutputDir', "--outputdir", "--Outputdir", dest="OutputDir", help="Path to output folder. The mkdocs docs directory.")
  parser.add_argument('--yml', dest="YmlFilePath", help="<Required>Path to yml base file", required=True)
  parser.add_argument('--RootDir', '--rootdir', '--Rootdir', dest="RootDir", help="Path to Root Directory to search for repos and md files.  Only set for dynamic content builds")
  parser.add_argument('-o', "--OutputLog", '--outputlog', dest="OutputLog", help="Create an output log file")
  return parser.parse_args()


def main():
    args = GatherArguments()
    ret = 0

    #setup file based logging if outputReport specified
    if(args.OutputLog):
        if(len(args.OutputLog) < 2):
            logging.critical("the output log file parameter is invalid")
            return -2

        #setup file based logging
        filelogger = logging.FileHandler(filename=args.OutputLog, mode='w')
        filelogger.setLevel(logging.DEBUG)
        filelogger.setFormatter(formatter)
        logging.getLogger('').addHandler(filelogger)

    logging.info("Log Started: " + datetime.datetime.strftime(datetime.datetime.now(), "%A, %B %d, %Y %I:%M%p" ))

    #logging.debug("Script Path is %s" % SCRIPT_PATH)
    Build = DocBuild(args.RootDir, args.OutputDir, args.YmlFilePath)
    logging.info("Root Directory For Doc Scanning: {0}".format(Build.RootDirectory))
    logging.info("Output Directory For Docs: {0}".format(Build.OutputDirectory))

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
    Build.CloseYml()

    return 0

if __name__ == '__main__':
    #setup main console as logger
    logger = logging.getLogger('')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    console = logging.StreamHandler()
    console.setLevel(logging.CRITICAL)
    console.setFormatter(formatter)
    logger.addHandler(console)

    #call main worker function
    retcode = main()

    if retcode != 0:
        logging.critical("Failed.  Return Code: %d" % retcode)
    else:
        logging.critical("Success!")
    #end logging
    logging.shutdown()
    sys.exit(retcode)
    