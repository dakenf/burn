# Burn Core

This crate should be used with [burn](https://github.com/burn-rs/burn).

[![Current Crates.io Version](https://img.shields.io/crates/v/burn-core.svg)](https://crates.io/crates/burn-core)
[![license](https://shields.io/badge/license-MIT%2FApache--2.0-blue)](https://github.com/burn-rs/burn-core/blob/master/README.md)


## Feature Flags

This crate can be used without the standard library (`#![no_std]`) with `alloc` by disabling
the default `std` feature.

* `std` - enables the standard library. Enabled by default.
* `experimental-named-tensor` - enables experimental named tensor.
