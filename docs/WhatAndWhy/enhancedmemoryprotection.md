# Enhanced Memory Protection

## Summary
While considerable attention has been devoted to hardware trust anchors and operating system 
security, attackers have discovered that UEFI firmware lacks basic memory protection that has 
been present in other system software for over a decade. Coupled with the inconsistency of 
security capabilities inherent to vendor firmware implementations, UEFI firmware has become an 
increasingly attractive system attack vector

In response to these security concerns, Microsoft has defined a set of paging protections
which UEFI vendors should implement in order to provide a more secure firmware environment.
Project Mu provides a reference implementation for Enhanced Memory Protections as well as
Compatibility Mode which is a reduced security state automatically entered when
legacy Option ROMs are loaded.

For the full specification, see the
[Microsoft Enhanced Memory Protection Specification](../pdf/enhanced_uefi_memory_protection_spec.pdf)
document.
