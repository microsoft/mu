# Rust Documentation Conventions

This document lays out the standards of practice for inline rust documentation for generating rust
docs. It also provides templates that should be followed when creating documentation for these
items. The templates will be immediately provided, however if this is your first time seeing this
document, please read it in it's entirety.

## Table of Contents

- [Rust Documentation Conventions](#rust-documentation-conventions)
  - [Table of Contents](#table-of-contents)
  - [Templates](#templates)
    - [Crate Template](#crate-template)
    - [Module Template](#module-template)
    - [Type Template](#type-template)
    - [Function Template](#function-template)
  - [Quick Reference](#quick-reference)
  - [Common Sections](#common-sections)
    - [Examples](#examples)
    - [Errors](#errors)
    - [Safety](#safety)
    - [Panics](#panics)
    - [Lifetimes](#lifetimes)
  - [Style Guides](#style-guides)
    - [Crate Style Guide](#crate-style-guide)
    - [Module Style Guide](#module-style-guide)
    - [Type Style Guide](#type-style-guide)
    - [Function Style Guide](#function-style-guide)

## Templates

### Crate Template

Example [Here](#crate-style-guide).

``` rust
//! Summary Line -> what this is
//!
//! Longer description and use of the crate
//!
//! ## Getting Started
//!
//! <any non-code requirements for this library to work (installations, etc.)>
//!
//! ## Examples and Usage
//!
//! <Short examples of using this library or links to where examples can be found>
//! <can use links [`String`](std::string::String) to other places in the library>
//!
//! ## Features
//!
//! <Add this section if this library defines features that can be enabled / disabled>
//!
//! ## <Custom sections>
//!
//! <Common additional sections are described in the Common Sections section or other custom
//! sections>
//!
//! ## License
//!
//! <Add the license type here>
//!
```

### Module Template

Example [Here](#module-style-guide).

``` rust
//! Summary Line -> what this is
//!
//! Longer description and use of the module.
//!
//! ## <Custom sections>
//!
//! <Common additional sections are described in the Common Sections section or other custom
//! sections>
//!
```

### Type Template

Example [Here](#type-style-guide).

``` rust
/// Summary line -> what this is
///
/// <Optional> longer description and semantics regarding the type. (e.g. how to construct and deconstruct)
///
/// ## <Custom sections>
///
/// <Common additional sections are described in the Common Sections section or other custom
/// sections>
///
/// <for each attribute in the type>
/// A short description of the attribute
///
```

### Function Template

Example [Here](#function-style-guide)

``` rust
/// Summary line -> what this is
///
/// <Optional> longer description of what is returned
///
/// # Errors
///
/// <list of possible raised errors and why. Use doc links>
/// Returns [`NoOptionalHeader`](Pe32Error::NoOptionalHeader) if the optional header is missing
/// in the PE32 image.
///
/// # Examples
///
/// ```
/// <some-rust-code></some-rust-code>
/// ```
///
/// <Common additional sections are described in the Common Sections section or other custom
/// sections>
///
```

## Quick Reference

- `///` Documents the item following the comment whereas `//!` documents the parent item.
- `#[doc(html_playground_url = "https://playground.example.com/")]` to add a Run button to examples
  - Warning: Be cognizant of using the playground run button with confidential code.
- `#[doc(hidden)]` to hide items
- `#[doc(alias = "alias")]` to make items easier to find via the search index
- `[Bar]`, `[bar](Bar)`, is supported for linking items (i.e. `[String](std::string::String)`)
- markdown is supported including sections (`#`), footnotes (`[^note]`), tables, tasks, punctuation
- Keep documentation lines to 100 characters
- codeblock attributes (\`\`\`[attribute]) options: `should_panic`, `no_run`, `compile_fail`

## Common Sections

All sections are described as `## <section_name>` inside the doc comments.

### Examples

Examples can optionally contain descriptions of each example, but must contain code blocks.
Code blocks can contain one of the following attributes: `ignore`, `should_panic`, `no_run`, or
`compile_fail`.

``` rust
/// # Examples
///
/// optional description
///
/// ``` <attribute>
/// <code></code>
/// ```
```

Code snippets should show how to use what is being documented.

Including `#[doc(html_playground_url = "https://playground.example.com/")]` will allow examples to be runnable in the documentation.

### Errors

Errors can optionally contain an overall description, but should contain the error type as a
linked reference and the reason why the error would be returned

``` rust
/// # Errors
///
/// Returns [ErrorName1](crate::module::ErrorEnum::Error1) when <this> happens
/// Returns [ErrorName2](crate::module::ErrorEnum::Error2) when <this> happens
///
```

### Safety

Provide general description and comments on unsafe calls, what makes the call unsafe, and any
undefined behavior that may happen. If being used at the module or crate level, use a general
description and then use a reference link to the function. The function should contain a detailed
Safety section.

### Panics

Provide general description and comments on any functions that use `.unwrap()`, `debug_assert!`,
etc. that would result in a panic. Typically only used when describing functions.

### Lifetimes

Provide a general description and comments on any types that have lifetimes more complex than a
single lifetime (explicit or implicit). Assume that the developer understands lifetimes; focus on
why the lifetime was modeled a certain way rather than describing why it was needed to make the
compiler happy! Typically only used when describing types.

## Style Guides

The goal is to create documentation that provides developers with a clear and concise description
on how to use a crate, module, type, or function while keeping it clean when auto-generating
documentation with `cargo doc`. As alluded to, it is the responsibility of the developer to ensure
that each library crate, public module, public type, and public function is well documented. Below
are the expectations for each.

If a common section is not applicable to the documented item, do not include it.

### Crate Style Guide

Crate documentation should be located at the top of the lib.rs or main.rs file. The intent is to
describe the purpose of the crate, providing any setup instructions and examples. This is also the
place to describe any common misconceptions or "gotchas". Doc comments here use `//!` specifying
we are documenting the *parent* item (the crate).

``` rust
//! PE32 Management
//!
//! This library provides high-level functionality for operating on and representing PE32 images.
//!
//! ## Examples and Usage
//!
//! ```
//! let file: File = File::open(test_collateral!("test_image.pe32"))
//!   .expect("failed to open test file.");
//!
//! let mut buffer: Vec<u8> = Vec::new();
//! file.read_to_end(&mut buffer).expect("Failed to read test file");
//!
//! let image_info: Pe32ImageInfo = pe32_get_image_info(buffer).unwrap();
//!
//! let mut loaded_image: Vec<u8> = vec![0; image_info.size_of_image as usize];
//! pe32_load_image(&image, &mut loaded_image).unwrap();
//! ```
//!
//! ## License
//!
//! Copyright (C) Microsoft Corporation. All rights reserved.
//!
//! SPDX-License-Identifier: BSD-2-Clause-Patent
//!
```

### Module Style Guide

Module documentation should be placed at the top of a module, whether that be a mod.rs file or the
module itself if contained to a single file. If a crate only consists of a single module, the crate
style guide should be used.Submodules should be avoided if possible, as they cause confusion. The
goal is to describe the types found in this module and their interactions with the rest of the
crate. Doc comments here use `//!` specifying we are documenting the *parent* item (the module).

``` rust
//! PE32 Management
//!
//! This module provides high-level functionality for operating on and representing PE32 images.
//!
//! ## License
//!
//! Copyright (C) Microsoft Corporation. All rights reserved.
//!
//! SPDX-License-Identifier: BSD-2-Clause-Patent
//!
```

### Type Style Guide

Type documentation should be available for all public public types such as enums, structs, etc. The
focus should be on the construction of the type (when / how), Destruction of the type if a custom
Drop trait is implemented, and any performance concerns. Doc comments here use `///` specifying we
are documenting the item directly below it (the type or member of the type).

**Document traits, not trait implementations!**

``` rust
/// Type for describing errors that result from working with PE32 images.
#[derive(Debug)]
pub enum Pe32Error {
    /// Goblin failed to parse the PE32 image.
    ///
    /// See the enclosed goblin error for a reason why the parsing failed.
    ParseError(goblin::error::Error),
    /// The parsed PE32 image does not contain an Optional Header.
    NoOptionalHeader,
    /// Failed to load the PE32 image into the provided memory buffer.
    LoadError,
    /// Failed to relocate the loaded image to the destination.
    RelocationError,
}

/// Type containing information about a PE32 image.
#[derive(PartialEq, Debug)]
pub struct Pe32ImageInfo {
    /// The offset of the entry point relative to the start address of the PE32 image.
    pub entry_point_offset: usize,
    /// The subsystem type (IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER [0xB], etc.).
    pub image_type: u16,
    /// The total length of the image.
    pub size_of_image: u32,
    /// The size of an individual section in a power of 2 (4K [0x1000], etc.).
    pub section_alignment: u32,
    /// The ascii string representation of a file (<filenname>.efi).
    pub filename: Option<String>,
}
```

### Function Style Guide

Function documentation should be available for functions of a public type (associated functions),
and any public functions. At least one example is required for each function in addition to the
other sections mentioned below.

Do not provide an arguments section, the name and type of the argument should make it self-evident

Do not provide a Returns section, this should be captured in the longer description and the return
type makes the possible return value self-evident.

``` rust

/// Attempts to parse a PE32 image and return information about the image.
///
/// Parses the bytes buffer containing a PE32 image and generates a [Pe32ImageInfo] struct
/// containing general information about the image otherwise an error.
///
/// ## Errors
///
/// Returns [`ParseError`](Pe32Error::ParseError) if parsing the PE32 image failed. Contains the
/// exact parsing [`Error`](goblin::error::Error).
///
/// Returns [`NoOptionalHeader`](Pe32Error::NoOptionalHeader) if the parsed PE32 image does not
/// contain the OptionalHeader necessary to provide information about the image.
///
/// ## Examples
///
/// ```
/// extern crate std;
///
/// use std::{fs::File, io::Read};
/// use uefi_pe32_lib::pe32_get_image_info;
///
/// let mut file: File = File::open(concat!(env!("CARGO_MANIFEST_DIR"), "/resources/test/","test_image.pe32"))
///   .expect("failed to open test file.");
///
/// let mut buffer: Vec<u8> = Vec::new();
/// file.read_to_end(&mut buffer).expect("Failed to read test file");
///
/// let image_info = pe32_get_image_info(&buffer).unwrap();
/// ```
///
pub fn pe32_get_image_info(image: &[u8]) -> Result<Pe32ImageInfo, Pe32Error> {
  ...
}
```
