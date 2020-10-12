# Tests

Testing firmware is critical and should be done so much more than it is today. So please, start writing tests. A lot
of work has been done to make it easier.

## Static Code Tests (analysis)

*stuart_ci_build* provides a framework for running static tests on the code base.  More details of the ever changing
tests can be found here. <https://github.com/microsoft/mu_basecore/tree/release/202002/.pytool/Plugin>

## UEFI Unit Tests - C code

It now exists!! There is a framework available in Tianocore and Project Mu basecore.
Simple API here. <https://github.com/microsoft/mu_basecore/blob/release/202002/MdePkg/Include/Library/UnitTestLib.h>
Implementation details here. <https://github.com/microsoft/mu_basecore/tree/release/202002/UnitTestFrameworkPkg>

### Host Based - console app

Host based allow you to run your tests on the same machine in which you are compiling your code.  These tests will run
as applications within the operating system host environment.  This is the preferred route when possible as these
tests will automatically roll into the CI process and are much faster and easier to run.  Obviously this means you
will need to write your code and tests with limited UEFI dependencies.  Any dependency your code has will need to be
mocked or faked for the unit test scenario.  The host test does leverage **cmocka** so lightweight mocking is possible.

### Target Based (UEFI Firmware on a device)

Some testing just doesn't make sense to run as a host test.  Tests that rely on system hardware and system state might
only work as target tests.  The unit test framework supports this and the implementation works for both.  This can
also include features that require reboots and saving state before the reboot so that tests can resume upon
continued execution.

## UEFI Shell Based Functional Tests

These can also leverage the UEFI target based tests.

## UEFI Shell Based Audit Tests

These tests are often one off UEFI shell applications that collect system data and then compare that data against known
good values for a system.  This is because these types of tests have no right or wrong answer.  Often we have a python
script/component to the test to compare expected result to actual result.  If the actual result doesn't match then this
type of test should fail.

## Testing Automation for physical hardware

The Project Mu team has done a lot of work with the open source project "robot framework".  This framework provides a
great logging and execution environment but at this time it is out of scope for Project Mu docs.  If you want to know
more, contact us as we are definitely willing to partner/share/engage.

## Testing Python

* Create pytest and/or python unit-test compatible tests.
* Make sure the python code passes the `flake8` "linter"
