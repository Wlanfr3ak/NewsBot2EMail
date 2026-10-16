# Changelog: Memtest86+

Quelle: https://api.github.com/repos/memtest86plus/memtest86plus/releases?per_page=100
Stand: 16.10.2026 01:13

---

## 9.00 – 2026-10-15

**Memtest86+ v9.00**

Memtest86+ v9.00 is our biggest release since the v6 rewrite! It adds support for a brand new architecture (ARM64), a new feature to Save Report to USB Drive, redesigned test algorithms, and many more!

TL;DR changelog:

- Support AArch64 (ARM64) - Tested on Snapdragon X and Raspberry Pi 4/5
- Save Report to USB Drive (FAT32 formatted only)
- Resigned Test Suite for better efficiency (Better Time to First Fault)
- Add 128 & 256-bit vector SIMD tests (SSE2/AVX2/NEON/LASX)
- Add a new Bus Stress Test (especially for DDR5, but useful for all RAMs) 
- Add a new RowHammer Test (Test 11, disabled by default)
- Improved Bit Fade Test (adjacent cells)
- Corrupted SPD detection Test 
- Better Automation (Serial)
- Better RAM information (DMI fallback if SPD unavailable)
- 100+ new DRAM brands detected
- Support for new platforms (Wildcat Lake)
- Signed for Secure Boot by our own CA (hopefully by Microsoft soon)
- Many (many) Bug fixes


## What's Changed
* Fix double handling of key input by @mibe in https://github.com/memtest86plus/memtest86plus/pull/610
* Add ECC polling option  by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/615
* Add temperature quirks for AMD EPYCs by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/616
* Add .osrel section to the binary by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/617
* Expand and modernise the test suite for V9 by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/628
* Hardened AP Stack Management by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/631
* Display memory info from DMI when SPD is unavailable by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/629
* Add support for USB Mass Storage Devices by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/607
* Add support for aarch64 (ARM64) architecture by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/626
* Fix EPYC Temperature reporting by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/633
* la64: Add LASX Test (instead of the scalar fallback path) by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/634
* Add a machine-parseable serial log ("log" boot option) by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/640
* Add SPD Checksum/CRC check at startup by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/641
* Minor fixes for Memtest86+ v9 (bugs found during betatesting) by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/642

**Full Changelog**: https://github.com/memtest86plus/memtest86plus/compare/v8.10...v9.00

## 8.10 – 2026-05-16

**Memtest86+ v8.10**

This release include some significant internal updates, adds CLang/LLD support, and now ships as a single binary for both UEFI and legacy boot.

**TL;DR changelog:**

* Add support for x2APIC
* Better support for Intel Lunar/Panther Lake
* Better Bandwidth measurement for caches and RAM
* Enable SIMD (SSE2) on x86_64 build
* Fix timings on LPDDR5
* Fix AMI BIOS boot issues due to unannounced W^X policy change
* Fix older GRUB boot issues
* Fix SecureBoot code & binary structure for future shim review
* LA64-specific improvements
* Bug fixes
 
## What's Changed (Complete Changelog)
* Bump actions/checkout from 5 to 6 by @dependabot[bot] in https://github.com/memtest86plus/memtest86plus/pull/564
* Avoid glitch in runtime hours display when time is reset by @tormodvolden in https://github.com/memtest86plus/memtest86plus/pull/561
* debug_memtest.sh: Extract offsets (also BSS) from code and binary by @tormodvolden in https://github.com/memtest86plus/memtest86plus/pull/562
* Specify tests to run in boot options by @gmongaras in https://github.com/memtest86plus/memtest86plus/pull/570
* Work-arounds for issues with Fedora GRUB EFI "linux" command by @martinwhitaker in https://github.com/memtest86plus/memtest86plus/pull/572
* system: loongarch: cpuinfo: Unroll memspeed copy loop by @ziyao233 in https://github.com/memtest86plus/memtest86plus/pull/578
* hwquirks: Detect cache on VIA VP/VPX by @jonathan-teh in https://github.com/memtest86plus/memtest86plus/pull/576
* system/loongarch: Fixes display issues for 2K3000/3B6000M by @MarsDoge in https://github.com/memtest86plus/memtest86plus/pull/589
* Add support for x2APIC by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/583
* Fix Secureboot to allow shim loading by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/595
* Fix PE/COFF W^X violation & set NX flag to fix recent AMI UEFI refusing to load Memtest86+ by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/604
* system/loongarch: Correcting temperature overflow by @MarsDoge in https://github.com/memtest86plus/memtest86plus/pull/593
* Better Cache & DRAM Bandwidth measurement (+Enable SSE2 on x86_64) by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/587
* Fix LA64-only linker RWX warnings by @x86fr in https://github.com/memtest86plus/memtest86plus/pull/609

**Full Changelog**: https://github.com/memtest86plus/memtest86plus/compare/v8.00...v8.10

## 8.00 – 2025-11-23

**Memtest86+ v8.00**

This release include some significant internal updates, adds CLang/LLD support, and now ships as a single binary for both UEFI and legacy boot.

Complete changelog:

- Add support for latest Intel CPUs
- Add support for latest AMD CPUs
- Faster detection for many-cores CPUs
- Added Temperature reporting on DDR5
- Added optional Dark Mode
- Fix DDR5 XMP 3.0 issue
- Better BadRAM support and reporting
- Better SPD detection on early ICHs
- Better support for VTxxx serial console
- Various refinements for Loongson µarch
- Bug fixes & optimizations

## 7.20 – 2024-11-11

**Memtest86+ v7.20**

This release add support for Loongson LoongArch (LA664) CPUs, the first non-x86 architecture supported by Memtest86+. It also add support for latest CPUs, up to Intel's Arrow Lake (Core Ultra Series 2) and Ryzen 9000 series (Zen5-based).

Complete changelog:

- Add support for Loongson LA64 arch
- Add support for latest Intel CPUs
- Add support for latest AMD CPUs
- Preliminary support for NUMA
- Bug fixes & optimizations

## 7.00 – 2024-01-07

**v7.00**

This release adds support for IMC (Integrated Memory Controller) polling to get live RAM settings on Intel Core 1st to 14th Gen and AMD Ryzen CPUs, and preliminary ECC polling support for selected AMD Ryzen CPUs.

Complete changelog:

- IMC polling for live DRAM settings
- Preliminary support for ECC polling
- Add support for MMIO UART 
- Add debugging options
- Bug fixes & optimizations

## 6.20 – 2023-05-07

**v6.20**

This release adds support for older systems and fix some issues with newer platforms (especially embedded/mobile).

Complete changelog:

- Add support for Alder Lake-N CPUs
- Add support for VIA VT8233(A)/VT8237
- Add support for nVidia nForce 3
- Add temperature reporting on AMD K8
- Add support for ALi M1533/1543(C)/1535
- Add some JEDEC Manufacturers
- Better handling of SPD reading on Mobile CPUs
- Fix APIC Timer fail on some mobile platforms
- Fix older CPU (P5/P6-class) detection

## 6.10 – 2023-02-03

**v6.10**

This release mainly add support for Secure Boot Signing

Complete changelog:
- Add support for Secure Boot Signing
- Add support for Headless EFI system 
- Add various command line options
- Add support for legacy ATI SB400
- Fix an issue related to BadRAM pattern
- Fix disabling SMP using F2 at startup
- Fix crash on SuperMicro X10SDV
- Various bug fixes and optimizations

## 6.01 – 2023-01-03

**v6.01**

This is a bug fix release. It fixes the following issues:

- False positives in test 9 [Modulo 20, random pattern] (issue #216)
- Failing to remove the big PASS/FAIL status banner (issue #130 and #173)
