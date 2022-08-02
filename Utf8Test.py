# @file Utf8Test.py
# This tool supports checking markdown files for encoding issues.  All
# markdown files must be valid utf-8
#
# Tool is callable as a cmdline tool and the EncodingCheck class is importable
# to leverage the same functionality in a DocBuild
#
##
# Copyright (c), Microsoft Corporation
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
import logging
import argparse
import datetime


class EncodingCheck(object):
    def TestMdEncodingOk(self, apath, encoding):
        try:
            with open(apath, "rb") as fobj:
                fobj.read().decode(encoding)
        except Exception as exp:
            logging.error("Encoding failure {1}: {0}".format(apath, encoding))
            logging.debug("EXCEPTION: while processing {1} - {0}".format(exp, apath))
            return False

        return True


def Valid_Dir(string):
    ab = string
    if (not os.path.isabs(ab)):
        ab = os.path.join(os.getcwd(), ab)
    ab = os.path.realpath(ab)
    if not os.path.isdir(ab):
        raise argparse.ArgumentTypeError("{0} is not a valid directory".format(string))
    return ab


def main():
    # Arg Parse
    parser = argparse.ArgumentParser(description='Utf8Test.py ')
    parser.add_argument('--RootDir', '--rootdir', '--Rootdir', dest="RootDir", help="Path to Root Directory to search md files to test.", required=True, type=Valid_Dir)
    parser.add_argument('-o', "--OutputLog", '--outputlog', dest="OutputLog", help="Create an output log file")
    parser.add_argument("--debug", dest="debug", help="Output all debug messages to console", action="store_true", default=False)
    args = parser.parse_args()

    if (args.debug):
        logging.getLogger().handlers[0].setLevel(logging.DEBUG)

    # setup file based logging if outputReport specified
    if (args.OutputLog):
        if (len(args.OutputLog) < 2):
            logging.critical("the output log file parameter is invalid")
            return -2

        # setup file based logging
        filelogger = logging.FileHandler(filename=args.OutputLog, mode='w')
        filelogger.setLevel(logging.DEBUG)
        filelogger.setFormatter(formatter)
        logging.getLogger('').addHandler(filelogger)

    logging.info("Log Started: " + datetime.datetime.strftime(datetime.datetime.now(), "%A, %B %d, %Y %I:%M%p"))

    error = 0
    count = 0
    EC = EncodingCheck()
    for root, dirs, files in os.walk(args.RootDir):
        for f in files:
            if f.lower().endswith(".md"):
                count += 1
                p = os.path.join(root, f)
                logging.info("Checking File: {%s}" % p)
                if not EC.TestMdEncodingOk(p, "utf-8"):
                    error += 1
    logging.info("Finished Processing {0} md files.  Found {1} files with errors.".format(count, error))
    return error


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
