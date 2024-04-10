# Features

## Summary

Project Mu features will generally be found in a "MU" sub-module, for example, "Common/MU" or "Silicon/Intel/MU".
What major features does Project Mu bring to the table above/beyond EDK2?

### Feature List

* Pluggable, cross-device, performance-optimized BDS
* Device Firmware Configuration Interface (DFCI) - enables practical MDM management
* PBKDF2-based BIOS password example
* Support for EKU-based trust anchors during signature validation
* Microsoft unit test framework
* Audit, function, & performance tests for platform features
* Scalable Python build environment
* Build plug in: override tracking tool
* Build plug in: flash descriptor analysis
* Binary package management via NuGet
* Capsule signing via signtool.exe
* Up-to-date Visual Studio compiler support
* Base64 encode for binary objects
* XML Support Package
* Rust support
  * [Rust build documentation](../CodeDevelopment/rust_build.md)
  * [Rust convention documentation](../CodeDevelopment/rust_documentation_conventions.md)
  * [Rust motivation documentation:](../WhatAndWhy/rust.md)
* [Enhanced Memory Protection:](../WhatAndWhy/rust.md)
l
### Features Coming Soon

* Modern BIOS menu example (Surface inspired)
* On screen keyboard (OSK) with mouse, touch support
* Graphical end-to-end boot performance analysis library and tool
* Infineon TPM firmware update via Capsule
* On screen notifications: color bars to inform users that a device is not in a production configuration

### Features integrated into Tiano

* Safe Integer library
* Heap Guard
* ESRT DXE driver
* Scalable device FMP framework
* Progress bar for Capsule Updates
* TCG FV pre hashing optimization
* NVME shutdown
