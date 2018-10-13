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

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

class MyTree(object):

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

    def GetOrMakeChildNode(self, name, leaf=None):
        if name in self.Children.keys():
            if leaf is not None:
                raise Exception("Can't make child with same name {}".format(name))
            else:
                return self.Children[name]

        #This is the Make Path
        t = MyTree(leaf)
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
            string1 = "\n" + prefix + "- " + name + ":"
            string2 += cnode.GetNavYml(string1, prefix + "  ")
        return string + string2

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
        

class DocBuild(object):
    #
    # constructor that creates the DocBuild object 
    #
    def __init__(self, RootDir, OutputDir, YmlFile):

        #Convert RootDir to abs and confirm valid
        if(os.path.isabs(RootDir)):
            self.RootDirectory = RootDir
        else:
            self.RootDirectory = os.path.join(os.path.abspath(os.getcwd()), RootDir)
        self.RootDirectory = os.path.realpath(self.RootDirectory)
        if(not os.path.isdir(self.RootDirectory)):
            raise Exception("Invalid Path for RootDir: {0}".format(self.RootDirectory))

        #Convert YmlFile to abs and confirm valid
        if(os.path.isabs(YmlFile)):
            self.YmlFilePath = YmlFile
        else:
            self.YmlFilePath = os.path.join(os.path.abspath(os.getcwd()), YmlFile)
        self.YmlFilePath = os.path.realpath(self.YmlFilePath)
        if(not os.path.isfile(self.YmlFilePath)):
            raise Exception("Invalid Path for YmlFile: {0}".format(self.YmlFilePath))

        #Convert OutputDir to abs and then mkdir if necessary
        if(os.path.isabs(OutputDir)):
            self.OutputDirectory = RootDir
        else:
            self.OutputDirectory = os.path.join(os.path.abspath(os.getcwd()), OutputDir)
        self.OutputDirectory = os.path.realpath(self.OutputDirectory)
        if(not os.path.isdir(self.OutputDirectory)):
            logging.debug("Output directory doesn't exist.  Making... {0}".format(self.OutputDirectory))
            os.makedirs(self.OutputDirectory)
        
        self.MdFiles = list()


    def Clean(self):
        retry = 1  #hack to make rmtree more successful
        while True:
            try:
                shutil.rmtree(self.OutputDirectory)
            except OSError:
                if not retry:
                    # If we're out of retries, bail.
                    raise Exception("Failed to Clean dir {0}".format(self.OutputDirectory))
                time.sleep(2)
                retry -= 1
                continue
            break

    def CollectDocs(self):
        for top, dirs, files in os.walk(self.RootDirectory):
            dirs = dirs # just for pylint
            for f in files:
                if f.lower().endswith(".md"):
                    rpath = os.path.relpath(os.path.join(top, f), self.RootDirectory)
                    self.MdFiles.append(rpath)
                    logging.debug("md file found: {0}".format(rpath))

        #Copy Markdown files
        for a in self.MdFiles:
            s = os.path.join(self.RootDirectory, a)
            p = os.path.join(self.OutputDirectory, a)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            shutil.copy2(s, p) 
        return 0

    def MakeNav(self):
        navstring = self.__MakeNavTree().GetNavYml("", "    ")
        logging.debug("NavString: " + navstring)
        root = self.__MakeNavTree()
        root.Collapse()
        navstring = root.GetNavYml("", "    ")
        logging.debug("NavString: " + navstring)

        f = open(self.YmlFilePath, "r")
        ypath = os.path.join(os.path.dirname(self.YmlFilePath), "mkdocs.yml")
        f2 = open(ypath, 'w')
        for l in f:
            f2.write(l)
        f.close()
        f2.write("\n  - Code Repositories:")

        f2.write(navstring)
        f2.close()

    def __MakeNavTree(self):

        root = MyTree()
        for a in self.MdFiles:
            string1 = a.replace(os.sep, "/")
            string2 = string1.partition(".")[0]
            root.AddToTree(string2, "dyn/"+ string1)
        logging.debug(root)


        return root

def GatherArguments():
  #Arg Parse
  parser = argparse.ArgumentParser(description='DocBuild ')
  parser.add_argument("--Clean", "--clean", dest="Clean", action="store_true", help="Delete Output Directory", default=False)
  parser.add_argument('--OutputDir', dest="OutputDir", help="<Required>Path to output folder for all docs", required=True)
  parser.add_argument('--yml', dest="YmlFilePath", help="<Required>Path to yml base file", required=True)
  parser.add_argument('--RootDir', dest="RootDir", help="<Required>Path to Root Directory to search for doc files", required=True)
  parser.add_argument("--OutputLog", dest="OutputLog", help="Create an output log file")
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
        logging.debug("Clean Called.  Deleting all Output Files")
        Build.Clean()

    ret = Build.CollectDocs()
    if(ret != 0):
        logging.critical("Failed to collect docs.  Return Code: {0x%x}".format(ret))

    Build.MakeNav()
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
    