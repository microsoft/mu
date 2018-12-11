# @file DocBuildTest.py
# Python Unit Tests for DocBuild
#
# Add simple unit tests for DocBuild to make sure behavior works
# as desired.   Much of DocBuild changes filesystem and/or global state
# These simple unit tests focus on the easy to test parts.
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
import unittest
from DocBuild import NavTree


class NavTreeTest(unittest.TestCase):

    def test_MakeFriendly_CamelCase(self):
        a = NavTree()
        self.assertEqual("Test Camel Case", a.MakeFriendly("TestCamelCase"))

    def test_MakeFriendly_SnakeCase(self):
        a = NavTree()
        self.assertEqual("Test Snake Case", a.MakeFriendly("Test_Snake_Case"))

    def test_MakeFriendly_MixedCase(self):
        a = NavTree()
        self.assertEqual("Test Mixed Case", a.MakeFriendly("TestMixed_Case"))

    def test_MakeFriendly_AllCaps(self):
        a = NavTree()
        self.assertEqual("TESTALLCAPS", a.MakeFriendly("TESTALLCAPS"))

    def test_MakeFriendly_MultipleUpper(self):
        a = NavTree()
        self.assertEqual("TEst MULtiple UPPEr CASEINAROW",
                         a.MakeFriendly("TEstMULtipleUPPErCASEINAROW"))

    def test_MakeFriendly_DuplicateSpaces(self):
        a = NavTree()
        self.assertEqual("test extra spaces",
                         a.MakeFriendly("test    extra   spaces"))

    def test_MakeFriendly_StartEndSpaces(self):
        a = NavTree()
        self.assertEqual("test start end spaces",
                         a.MakeFriendly("  test start end spaces   "))


if __name__ == '__main__':
    unittest.main()
