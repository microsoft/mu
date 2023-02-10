# Features

## Summary

Project Mu features will generally be found in a "MU" sub-module, for example, "Common/MU" or "Silicon/Intel/MU".
What major features does Project Mu bring to the table above/beyond EDK2?

### Feature List

* Pluggable, cross-device, performance-optimized BDS
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

### Stand alone Mu Features with separate code repositories

These Project Mu features may be included as submodules or as external git dependency repositories.
See each code repository for more details

* Device Firmware Configuration Interface (DFCI) - enables practical MDM management [mu_feature_dfci](https://github.com/microsoft/mu_feature_dfci)
* Manamgement Module Supervisor (protections in Management Mode) - [mu_feature_mm_supv](https://github.com/microsoft/mu_feature_mm_supv)
* Platform Configuration Support - [mu_feature_config](https://github.com/microsoft/mu_feature_config)
* Uefi Variable Store (In design phase) - [mu_feature_uefi_variable](https://github.com/microsoft/mu_feature_uefi_variable)