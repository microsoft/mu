# Announcements

## 2018/11/05

* Docs
  * Announcement page created to give high level view of Project Mu activity
  * Added Docs for code development (prereqs, compile, test)
  * Added support for images in Multi-Repo documentation

* Mu BaseCore
  * New TianoCore integration from Aug 2018 stable point. 
  * _release/201808_ branch created.
  * Basetools and UefiBuild moved to Mu Build repo
  * Work in progress to finish integration and validation. 

* Mu Build
  * Repository created to isolate build tools from UEFI source code
  * MuBuild plugin added to test for invalid character encoding
  * Python 3.7 Version supported. No more python binaries.  

* Mu Plus
  * MsGraphicsPkg open sourced adding features like:
    * Graphical Setup Browser
    * UI Toolkit for widgets
    * Rectangle and Circle libraries (Circular progress bar)
    * On screen keyboard
  * PcBdsPkg open sourced adding BDS functionality targeted at PC class systems
  * Add DeviceStateLib to support tracking device state
  * Add mathlib to MsCorePkg to support limited floating point math operations like `sqrt`, `cos`, and `sine`

* Mu Oem Sample
  * Repository created to open source assets generally customized by the OEM. 
  * These sample assets include BDS policy/behavior, logo, version
  * This repository will be updated to add more sample assets as needed

___

