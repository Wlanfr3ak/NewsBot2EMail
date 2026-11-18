# Changelog: VeraCrypt

Quelle: https://github.com/veracrypt/VeraCrypt/releases
Stand: 05.11.2026 12:44

---

## 1.26.31 – 2026-11-02

**Downloads:** [Jump directly to installers, packages, source archives, checksums and signatures](#user-content-downloads)

### Changes between 1.26.30 and 1.26.31 (2 November 2026):

* **All OSes:**

  * Update translations and documentation.

* **Windows:**

  * Fix upgrades from VeraCrypt 1.26.30 that could fail while replacing the system service executable. Wait for the service process to exit, retry locked files and defer replacement until Windows restarts when necessary.
  * Fix MSI upgrades on systems with an encrypted system drive, including migration of original bootloader backups, bootloader updates and Secure Boot compatibility checks.
  * Report Windows feature-update configuration, recovery-backup migration and system-service update failures as warnings identifying the affected file or registry value, allowing installation, uninstallation and system-encryption operations to finish. Retry feature-update configuration when the system service starts.
  * Warn when a new Rescue Disk would reuse a Windows Boot Manager backup signed by Microsoft Windows Production PCA 2011 during migration to Windows UEFI CA 2023. Recreating the Rescue Disk does not update this stored backup.
  * Improve protection and cleanup of the legacy system encryption support directory under ProgramData, including read-only files and redirected paths. Preserve recovery backups and retain old driver files until Windows Setup registration changes are verified.
  * Avoid repeated warnings caused by unrelated incompatible language packs. When no compatible pack is available for the selected language, display a single warning and fall back to English while preserving the language preference.

* **Linux, macOS and BSD:**

  * Security: Prevent programs launched by VeraCrypt from inheriting the pipes between its interface and service, which could let them use an active administrator session. This extends the protection added in version 1.26.30.

    * Reported by [aorakko](https://github.com/aorakko).

  * Security: Prevent programs launched by VeraCrypt from inheriting its open files, devices and internal pipes.
  * Fix cases where VeraCrypt could hang while waiting for system tools used to mount volumes or open them in a file manager. Improve timeout handling for these tools.
  * Document that permission to run VeraCrypt or its core service as root through `sudo` or `doas` grants full root authority. See the [security model](https://veracrypt.jp/en/Security%20Model.html#sudo-and-doas).
  * Fix mount-point validation for directories that do not yet exist, including paths containing `..` or symbolic links. (GH #1973)

    * Reported by [aorakko](https://github.com/aorakko).

  * Restore compatibility with GCC 4.4 for Unix GUI and console builds.
  * Improve password dialog titles for long volume paths, preserving the volume file name where possible and adapting to window resizing.

* **Linux and BSD:**

  * Only default mount-point names, consisting of the configured prefix followed by a slot number from 1 to 64, receive automatic directory creation, ownership changes and removal. Custom mount points such as `/media/veracrypt-backup` or `/media/veracrypt1/photos` must already exist with suitable permissions; sharing the default prefix no longer makes them automatically managed.

* **Linux:**

  * Add optional Ayatana AppIndicator support to RPM and Arch Linux package builds for system tray integration, including on KDE Wayland. (GH #1339)

## Merged Pull Requests
* Common: make derived key buffer alignment explicit in CreateVolumeHeaderInMemory by @bernardladenthin in https://github.com/veracrypt/VeraCrypt/pull/1843
* Complete and refine the Swedish translation by @NickWick13 in https://github.com/veracrypt/VeraCrypt/pull/1951
* Update Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1975
* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1976


**Full Changelog**: https://github.com/veracrypt/VeraCrypt/compare/VeraCrypt_1.26.30...VeraCrypt_1.26.31

## Downloads

Detached GPG signatures are provided as `sig` links next to each download.

- **Windows**
  - Installer: [VeraCrypt.Setup.1.26.31.exe](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt.Setup.1.26.31.exe) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt.Setup.1.26.31.exe.sig))
  - MSI installer (x64): [VeraCrypt_Setup_x64_1.26.31.msi](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_Setup_x64_1.26.31.msi) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_Setup_x64_1.26.31.msi.sig))
  - MSI installer (ARM64): [VeraCrypt_Setup_arm64_1.26.31.msi](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_Setup_arm64_1.26.31.msi) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_Setup_arm64_1.26.31.msi.sig))
  - Portable version: [VeraCrypt.Portable.1.26.31.exe](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt.Portable.1.26.31.exe) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt.Portable.1.26.31.exe.sig))
  - Debugging symbols: [VeraCrypt_1.26.31_Windows_Symbols.zip](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_1.26.31_Windows_Symbols.zip) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_1.26.31_Windows_Symbols.zip.sig))

- **macOS**
  - Standard package: [VeraCrypt_1.26.31.dmg](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_1.26.31.dmg) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_1.26.31.dmg.sig))
  - FUSE-T package: [VeraCrypt_FUSE-T_1.26.31.dmg](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_FUSE-T_1.26.31.dmg) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_FUSE-T_1.26.31.dmg.sig))

- **Linux**
  - AppImage x64: [VeraCrypt-1.26.31-x86_64.AppImage](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt-1.26.31-x86_64.AppImage) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt-1.26.31-x86_64.AppImage.sig))
  - AppImage ARM64: [VeraCrypt-1.26.31-aarch64.AppImage](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt-1.26.31-aarch64.AppImage) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt-1.26.31-aarch64.AppImage.sig))
  - Legacy GTK2 AppImage: [VeraCrypt-1.26.31-gtk2-legacy-i686.AppImage](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt-1.26.31-gtk2-legacy-i686.AppImage) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt-1.26.31-gtk2-legacy-i686.AppImage.sig)); [VeraCrypt-1.26.31-gtk2-legacy-x86_64.AppImage](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt-1.26.31-gtk2-legacy-x86_64.AppImage) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt-1.26.31-gtk2-legacy-x86_64.AppImage.sig))
  - Generic installer: [veracrypt-1.26.31-setup.tar.bz2](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-setup.tar.bz2) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-setup.tar.bz2.sig))
  - Legacy installer for 32-bit CPU with no SSE2: [veracrypt-1.26.31-x86-legacy-setup.tar.bz2](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-x86-legacy-setup.tar.bz2) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-x86-legacy-setup.tar.bz2.sig))

<details>
<summary>Linux Debian/Ubuntu packages</summary>

- Debian 13: GUI [veracrypt-1.26.31-Debian-13-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Debian-13-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Debian-13-amd64.deb.sig)), [veracrypt-1.26.31-Debian-13-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Debian-13-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Debian-13-arm64.deb.sig)); Console [veracrypt-console-1.26.31-Debian-13-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Debian-13-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Debian-13-amd64.deb.sig)), [veracrypt-console-1.26.31-Debian-13-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Debian-13-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Debian-13-arm64.deb.sig))
- Debian 12: GUI [veracrypt-1.26.31-Debian-12-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Debian-12-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Debian-12-amd64.deb.sig)), [veracrypt-1.26.31-Debian-12-i386.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Debian-12-i386.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Debian-12-i386.deb.sig)); Console [veracrypt-console-1.26.31-Debian-12-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Debian-12-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Debian-12-amd64.deb.sig)), [veracrypt-console-1.26.31-Debian-12-i386.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Debian-12-i386.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Debian-12-i386.deb.sig))
- Ubuntu 26.10: GUI [veracrypt-1.26.31-Ubuntu-26.10-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Ubuntu-26.10-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Ubuntu-26.10-amd64.deb.sig)); Console [veracrypt-console-1.26.31-Ubuntu-26.10-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Ubuntu-26.10-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Ubuntu-26.10-amd64.deb.sig))
- Ubuntu 26.04: GUI [veracrypt-1.26.31-Ubuntu-26.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Ubuntu-26.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Ubuntu-26.04-amd64.deb.sig)), [veracrypt-1.26.31-Ubuntu-26.04-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Ubuntu-26.04-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Ubuntu-26.04-arm64.deb.sig)); Console [veracrypt-console-1.26.31-Ubuntu-26.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Ubuntu-26.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Ubuntu-26.04-amd64.deb.sig)), [veracrypt-console-1.26.31-Ubuntu-26.04-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Ubuntu-26.04-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Ubuntu-26.04-arm64.deb.sig))
- Ubuntu 24.04: GUI [veracrypt-1.26.31-Ubuntu-24.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Ubuntu-24.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Ubuntu-24.04-amd64.deb.sig)), [veracrypt-1.26.31-Ubuntu-24.04-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Ubuntu-24.04-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Ubuntu-24.04-arm64.deb.sig)); Console [veracrypt-console-1.26.31-Ubuntu-24.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Ubuntu-24.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Ubuntu-24.04-amd64.deb.sig)), [veracrypt-console-1.26.31-Ubuntu-24.04-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Ubuntu-24.04-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Ubuntu-24.04-arm64.deb.sig))
- Ubuntu 22.04: GUI [veracrypt-1.26.31-Ubuntu-22.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Ubuntu-22.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Ubuntu-22.04-amd64.deb.sig)); Console [veracrypt-console-1.26.31-Ubuntu-22.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Ubuntu-22.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Ubuntu-22.04-amd64.deb.sig))

</details>

<details>
<summary>Linux RPM packages</summary>

- Fedora 44: GUI [veracrypt-1.26.31-Fedora-44-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Fedora-44-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Fedora-44-x86_64.rpm.sig)); Console [veracrypt-console-1.26.31-Fedora-44-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Fedora-44-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Fedora-44-x86_64.rpm.sig))
- Fedora 43: GUI [veracrypt-1.26.31-Fedora-43-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Fedora-43-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-Fedora-43-x86_64.rpm.sig)); Console [veracrypt-console-1.26.31-Fedora-43-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Fedora-43-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-Fedora-43-x86_64.rpm.sig))
- openSUSE 15: GUI [veracrypt-1.26.31-openSUSE-15-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-openSUSE-15-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-openSUSE-15-x86_64.rpm.sig)); Console [veracrypt-console-1.26.31-openSUSE-15-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-openSUSE-15-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-openSUSE-15-x86_64.rpm.sig))
- CentOS 8: GUI [veracrypt-1.26.31-CentOS-8-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-CentOS-8-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-CentOS-8-x86_64.rpm.sig)); Console [veracrypt-console-1.26.31-CentOS-8-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-CentOS-8-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-CentOS-8-x86_64.rpm.sig))
- CentOS 7: GUI [veracrypt-1.26.31-CentOS-7-i686.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-CentOS-7-i686.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-CentOS-7-i686.rpm.sig)), [veracrypt-1.26.31-CentOS-7-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-CentOS-7-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-CentOS-7-x86_64.rpm.sig)); Console [veracrypt-console-1.26.31-CentOS-7-i686.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-CentOS-7-i686.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-CentOS-7-i686.rpm.sig)), [veracrypt-console-1.26.31-CentOS-7-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-CentOS-7-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-CentOS-7-x86_64.rpm.sig))
- CentOS 6: GUI [veracrypt-1.26.31-CentOS-6-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-CentOS-6-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-CentOS-6-x86_64.rpm.sig)), [veracrypt-1.26.31-CentOS-6-i686.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-CentOS-6-i686.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-CentOS-6-i686.rpm.sig)); Console [veracrypt-console-1.26.31-CentOS-6-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-CentOS-6-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-CentOS-6-x86_64.rpm.sig)), [veracrypt-console-1.26.31-CentOS-6-i686.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-CentOS-6-i686.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-console-1.26.31-CentOS-6-i686.rpm.sig))

</details>

- **Source code**
  - [VeraCrypt_1.26.31_Source.tar.bz2](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_1.26.31_Source.tar.bz2) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_1.26.31_Source.tar.bz2.sig))
  - [VeraCrypt_1.26.31_Source.zip](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_1.26.31_Source.zip) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_1.26.31_Source.zip.sig))
  - [VeraCrypt-DCS-EFI-LGPL_1.26.31_Source.zip](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt-DCS-EFI-LGPL_1.26.31_Source.zip) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt-DCS-EFI-LGPL_1.26.31_Source.zip.sig))

- **Documentation and verification**
  - Full list of changes: [README.TXT](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/README.TXT) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/README.TXT.sig))
  - Checksums: [veracrypt-1.26.31-sha256sum.txt](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-sha256sum.txt) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-sha256sum.txt.sig)); [veracrypt-1.26.31-sha512sum.txt](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-sha512sum.txt) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/veracrypt-1.26.31-sha512sum.txt.sig))
  - User Guide CHM (English): [VeraCrypt.User.Guide.chm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt.User.Guide.chm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt.User.Guide.chm.sig))
  - User Guide CHM (Russian): [VeraCrypt.User.Guide.ru.chm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt.User.Guide.ru.chm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt.User.Guide.ru.chm.sig))
  - User Guide CHM (Simplified Chinese): [VeraCrypt.User.Guide.zh-cn.chm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt.User.Guide.zh-cn.chm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt.User.Guide.zh-cn.chm.sig))
  - Bundle containing all release files: [VeraCrypt_1.26.31_Bundle.7z](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_1.26.31_Bundle.7z) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_1.26.31_Bundle.7z.sig)); [VeraCrypt_1.26.31_Bundle.7z.checksums](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_1.26.31_Bundle.7z.checksums) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.31/VeraCrypt_1.26.31_Bundle.7z.checksums.sig))

## 1.26.30 – 2026-10-24

**Downloads:** [Jump directly to installers, packages, source archives, checksums and signatures](#user-content-downloads)



### Changes between 1.26.29 and 1.26.30 (24 October 2026):



* **All OSes:**



  * Security: Improve erasure of security token data and limit smart card responses to prevent hangs or excessive memory use.

  * Fix unintended reuse of the current PIM when switching KDFs in the password-change and header-KDF dialogs. The selected KDF's default PIM is now used unless a new PIM is explicitly specified.

  * Fix cryptographic errors on processors using big endian byte order. Prevent alignment crashes on affected processors, including 32 bit ARM. (GH #1899, GH #1908, GH #1909)

  * Fix ChaCha output when processing successive partial blocks.

  * Improve encryption worker error handling and wait for active work to finish before shutdown.

  * Update translations and correct missing entries, formatting placeholders and escaped punctuation.

  * Expand documentation for EFI Secure Boot certificate migration, KDF selection, supported operating systems and Windows builds.



* **Windows:**



  * Security: Fix [GHSA-w98h-pqh6-wfjj](https://github.com/veracrypt/VeraCrypt/security/advisories/GHSA-w98h-pqh6-wfjj): insufficient protection of system encryption support files could enable local privilege escalation during a qualifying Windows feature update or tampering with the BIOS loader during restoration. Protect setup scripts, driver packages and recovery backups, and reject untrusted legacy backups and driver sources.



    * Reported by [Kaarssteun](https://github.com/Kaarssteun).



  * Security: Fix [GHSA-9mgv-w2fw-3m78](https://github.com/veracrypt/VeraCrypt/security/advisories/GHSA-9mgv-w2fw-3m78): prevent local disclosure of limited disk metadata.



    * Reported by [artemy-ccrsky](https://github.com/artemy-ccrsky).

    * CVE-2026-77572



  * Fix driver stability regressions reported with VeraCrypt 1.26.29 and improve cleanup during mounting and dismounting. Restore the previous I/O completion behavior and disable ordered flush barriers by default.

  * Handle processor state-save failures safely during key derivation and fix KDF worker completion and startup cleanup.

  * Improve system encryption setup and upgrade failure handling. Retain recovery backups during uninstall, warn when an encrypted system's original loader backup is unavailable, and keep Windows Setup configuration failures independent of boot-loader repair.

  * Prevent incompatible EFI bootloader installation when Secure Boot is enabled. Refresh the Windows Boot Manager copy from compatible Windows files.

  * Warn when installed boot components need CA migration and prompt users to recreate the Rescue Disk after bootloader certificate changes.

  * Correct dismount status reporting and drive removal notifications, including command line dismounts. (GH #1852)

  * Prevent repeated errors when a favorite set to mount on device arrival has a drive letter already occupied by another device.

  * Update stored favorite volume PIM/KDF metadata after password or header KDF changes.

  * Fix `Argon2` and `Argon2id` command line aliases, and accept `n` to disable `/protectScreen` and `/protectMemory`.

  * Fix windows and dialogs appearing off screen or on the wrong monitor. (GH #1858, GH #1865, GH #1912)

  * Fix favorite labels containing XML characters and prevent label text from changing saved mount options. (GH #1946)

  * Preserve Unicode paths and literal XML entity text in saved settings. Prevent extra carriage returns from accumulating when configuration files are rewritten.

  * Fix partially translated interfaces and untranslated menu items and benchmark controls. (GH #1587, GH #1929, GH #1930)

  * Update bundled zlib to 1.3.2 and LZMA SDK to 26.02.

  * **Favorite labels when downgrading:** Back up your ordinary and system favorite volume configuration files before downgrading. Older versions can display XML escapes in labels and keep that text when saving, even after you upgrade again. Restore your backups or correct the labels after returning to this version.

  * **Upgrade note for system encryption:** Install the updated VeraCrypt before preparing a Windows feature update, and resolve any Windows update support or original loader backup warning. If Windows Setup has already staged support files, restart feature-update preparation so it stages the updated files; installing VeraCrypt does not replace a previously staged script. Preserve existing recovery backups and a known trustworthy VeraCrypt Rescue Disk. Changing an old backup's ownership or permissions does not establish that its contents are safe.



* **Linux, macOS and BSD:**



  * Security: Fix [GHSA-4j3p-7hp7-xw73](https://github.com/veracrypt/VeraCrypt/security/advisories/GHSA-4j3p-7hp7-xw73): prevent a heap buffer overflow, out-of-bounds reads and excessive memory allocations when deserializing requests in the privileged service.



    * Reported by [damianrickard](https://github.com/damianrickard).

    * CVE-2026-77372



  * Security: Prevent privileged-service communication and authentication file descriptors from leaking into child processes.

  * Detect CPU features before starting core services so mounted volumes use available hardware acceleration. Correct failed instruction probes on older processors. (GH #1939)

  * Preserve forced read-only protection when mounting partially encrypted system volumes through FUSE.

  * Make unattended unmount commands return a nonzero exit status when a busy volume can't be unmounted.

  * Support `doas` when `sudo` isn't available, including `opendoas` on FreeBSD. Avoid repeated password prompts after successful authentication.

  * Preserve hidden volume protection when mounting favorites, including during credential retries. Keep each favorite's mount options separate.

  * Cache the credentials actually used to mount a volume and preserve cancellation and other non-credential errors during automatic backup-header retries.

  * Reject missing, oversized or incorrectly encoded `--stdin` passwords instead of silently using an empty or truncated password. Decode the complete first line using the current locale. (GH #1935)

  * Require confirmation before replacing an existing container file during command line creation. Use `--force` to allow replacement without a prompt. (GH #1861)

  * Honor `--no-size-check` during command line container creation. (GH #1756)

  * Expose BLAKE2b-512 in random-pool, keyfile-generation and hash-benchmark dialogs, including when using Argon2id.

  * Preserve paths containing XML special characters and literal XML entity text in favorites, volume history and settings. (GH #1943)

  * Fall back to English when a language file is unusable, and fix password-length warnings and busy-volume dismount confirmation messages. (GH #1944)



* **Linux and FreeBSD:**



  * Security: Fix [GHSA-wf3r-pjv3-fcxx](https://github.com/veracrypt/VeraCrypt/security/advisories/GHSA-wf3r-pjv3-fcxx): a generic installer vulnerability could let a separate local user replace the embedded package and gain root privileges. Distribution packages and AppImage builds aren't affected.

  * Improve volume-file and tray icons, and make desktop cache updates optional when the required utilities aren't installed.



* **Linux:**



  * Enforce read-only protection on loop devices, all device-mapper layers and filesystems. Automatically mount volumes as read only when the backing block device reports write protection, even if it permits an open request with write access.

  * Forward sync requests for volumes mounted through FUSE to the backing file or device and report flush failures. Previously, a successful sync could leave data in the host cache.

  * Check that devices belong to the selected volume before dismount or filesystem checks. Leave externally supplied host devices attached and refuse normal dismount while a decrypted loop device remains in use.

  * Support writable volume files on shares that restrict root access, including GVfs and NFS with `root_squash`. (GH #23) Keep the share mounted and the user session active until dismount.

  * Improve mounting on minimal systems, including FAT and exFAT detection. Use FUSE automatically when `dmsetup` isn't installed. (GH #1898)

  * Support NixOS helper locations and report when launcher restrictions block administrator authentication. (GH #1911)

  * Rewrite `mount.veracrypt` in POSIX shell, honor read-only options and supported `mount(8)` flags, reject invalid options, and fix argument quoting. (GH #1895, GH #1928)

  * Fix installation on systems with a merged `/usr` layout. (GH #1764)



* **macOS:**



  * Security: Fix [GHSA-f3px-f8h2-fm4c](https://github.com/veracrypt/VeraCrypt/security/advisories/GHSA-f3px-f8h2-fm4c): correct FUSE-T cleanup that could leave decrypted volumes accessible after dismount. Protect auxiliary mounts and report when service shutdown can't be confirmed.



    * Reported by [morin-andrew](https://github.com/morin-andrew) and [techfoxactual](https://github.com/techfoxactual).

    * Remediation contributed by [mimoex](https://github.com/mimoex), with analysis by [theophieln](https://github.com/theophieln).

    * CVE-2026-108982



  * Security: Validate disk device ownership changes and prefer trusted system utilities when running privileged operations. (GH #1758, GH #1790)

  * Fix mounting and dismounting crashes with macFUSE 5.3.3 and later. (GH #1887)

  * Fix Check Filesystem and Repair Filesystem so they operate on the selected volume and show their results in Terminal. (GH #1791)

  * Add a preference to disable screen protection, which remains enabled by default.

  * Improve disk-image discovery and avoid detaching unrelated disks when device numbers are reused after an external eject. Keep volume status updates responsive.

  * **Upgrade note for FUSE-T users:** When upgrading from VeraCrypt 1.26.29, dismount your volumes and restart macOS before using the updated build. Replacing the application doesn't end services that are already running.



* **FreeBSD:**



  * Detect ARM64 AES and SHA-256 hardware acceleration while retaining software fallbacks.



* **OpenBSD:**



  * Add FFS volume creation in the wizard and on the command line.



* **Building and packaging:**



  * Fix builds with `NOASM` or `NOSSE2`, and Argon2 builds targeting x86-64-v3/v4 or XOP. (GH #1891, GH #1896, GH #1906)

  * Fix FreeBSD ARM builds and local Apple Silicon builds. (GH #1678, GH #1934) Restore Linux builds with GCC 4.4 and fix `INDICATOR=1` tray-menu builds. (GH #1823)

  * Let wxWidgets builds follow the parent make's parallel job settings, including OpenWrt builds. (GH #1903)

  * Remove OpenWrt's Bash dependency and preserve SDK package selections. (GH #1932)

  * Improve macOS signing and notarization validation, and refresh app bundles before packaging.

  * Remove the MFC dependency from Windows driver resource compilation.

## Merged Pull Requests

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1762

* macOS: validate target of privileged SetFileOwner (restrict to disk device nodes) by @damianrickard in https://github.com/veracrypt/VeraCrypt/pull/1758

* Honor --no-size-check in CLI volume creation by @damianrickard in https://github.com/veracrypt/VeraCrypt/pull/1756

* Update Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1770

* Update Language.de.xml by @Mr-Update in https://github.com/veracrypt/VeraCrypt/pull/1771

* Some formatting changes to README.md by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1777

* macOS: parse hdiutil -plist output via CoreFoundation instead of string scanning by @damianrickard in https://github.com/veracrypt/VeraCrypt/pull/1776

* Update Corsican translation on 2026-06 by @Patriccollu in https://github.com/veracrypt/VeraCrypt/pull/1774

* Translate English entries to Chinese in XML by @nkh0472 in https://github.com/veracrypt/VeraCrypt/pull/1769

* Update Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1782

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1781

* Update Corsican translation on 2026-06 (2nd) by @Patriccollu in https://github.com/veracrypt/VeraCrypt/pull/1784

* Use HTML entities in translation files by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1787

* macOS: search system directories before /usr/local/bin for binaries by @damianrickard in https://github.com/veracrypt/VeraCrypt/pull/1790

* Typo fix in Spanish translation by @borj404 in https://github.com/veracrypt/VeraCrypt/pull/1794

* macOS: honor the CheckFilesystem repair flag by @damianrickard in https://github.com/veracrypt/VeraCrypt/pull/1791

* Update Corsican translation on 2026-06 (3rd) by @Patriccollu in https://github.com/veracrypt/VeraCrypt/pull/1795

* Update Language.nl.xml by @RockyTDR in https://github.com/veracrypt/VeraCrypt/pull/1796

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1797

* Update Swedish translation by @NickWick13 in https://github.com/veracrypt/VeraCrypt/pull/1798

* Update Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1799

* Update Language.ro.xml by @TigerxWood in https://github.com/veracrypt/VeraCrypt/pull/1800

* Update Language.ro.xml by @TigerxWood in https://github.com/veracrypt/VeraCrypt/pull/1802

* Update Swedish translation by @NickWick13 in https://github.com/veracrypt/VeraCrypt/pull/1805

* Update Language.zh-cn.xml by @nkh0472 in https://github.com/veracrypt/VeraCrypt/pull/1813

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1814

* Linux: fix tray icon menu build with INDICATOR=1 by @ElCruncharino in https://github.com/veracrypt/VeraCrypt/pull/1823

* Update Swedish translation by @NickWick13 in https://github.com/veracrypt/VeraCrypt/pull/1825

* macOS: initialize PC/SC lazily to keep fork() children clean by @heinz-goetz in https://github.com/veracrypt/VeraCrypt/pull/1887

* macOS/FUSE-T: Terminate auxiliary FUSE service on dismount by @mimoex in https://github.com/veracrypt/VeraCrypt/pull/1866

* Linux: make mount.veracrypt POSIX sh by @flatstik in https://github.com/veracrypt/VeraCrypt/pull/1895

* Crypto: fix NOASM link failures on x86 by @flatstik in https://github.com/veracrypt/VeraCrypt/pull/1896

* Crypto: use VC_INLINE for the ARM CPU_Query helpers by @flatstik in https://github.com/veracrypt/VeraCrypt/pull/1886

* Linux: fall back to FUSE when dmsetup is not installed by @flatstik in https://github.com/veracrypt/VeraCrypt/pull/1898

* Crypto: fix portable C code on big-endian CPUs by @flatstik in https://github.com/veracrypt/VeraCrypt/pull/1899

* Update Language.nl.xml by @RockyTDR in https://github.com/veracrypt/VeraCrypt/pull/1893

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1902

* Argon2: fix build with -march=x86-64-v3/v4 and XOP targets by @flatstik in https://github.com/veracrypt/VeraCrypt/pull/1906

* Unix: require confirmation before overwriting containers by @felix314159 in https://github.com/veracrypt/VeraCrypt/pull/1861

* Update Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1904

* Crypto: no unaligned 64-bit accesses on 32-bit ARM by @flatstik in https://github.com/veracrypt/VeraCrypt/pull/1908

* Crypto: use alignment-safe loads and stores where unaligned access faults by @flatstik in https://github.com/veracrypt/VeraCrypt/pull/1909

* Show mount/wait dialog on the monitor of the main window by @amail80 in https://github.com/veracrypt/VeraCrypt/pull/1865

* CI: build and test on big-endian (s390x) and across byte orders by @flatstik in https://github.com/veracrypt/VeraCrypt/pull/1905

* Build: let a parent make control the wxWidgets build jobs by @flatstik in https://github.com/veracrypt/VeraCrypt/pull/1903

* Tests: read known data from the test volumes without mounting by @flatstik in https://github.com/veracrypt/VeraCrypt/pull/1907

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1918

* Show Secure Desktop dialogs on the monitor of their parent window by @amail80 in https://github.com/veracrypt/VeraCrypt/pull/1912

* Windows: bring the main window back on screen when its restore position is off screen by @amail80 in https://github.com/veracrypt/VeraCrypt/pull/1858

* Update Swedish translation by @NickWick13 in https://github.com/veracrypt/VeraCrypt/pull/1826

* Fix build with NOSSE2 by @puleglot in https://github.com/veracrypt/VeraCrypt/pull/1891

* Tests: verify that CRYPTOPP_ALIGN_DATA delivers the requested alignment by @bernardladenthin in https://github.com/veracrypt/VeraCrypt/pull/1844

* Crypto: document that CRYPTOPP_ALIGN_DATA can expand to nothing by @bernardladenthin in https://github.com/veracrypt/VeraCrypt/pull/1842

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1921

* Update Windows build guide: current NASM, simplified YASM setup, common-error reference by @0xDarkMatter in https://github.com/veracrypt/VeraCrypt/pull/1851

* Update Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1916

* Update Swedish translation and correct safety instructions by @NickWick13 in https://github.com/veracrypt/VeraCrypt/pull/1919

* Use direct burn in BufferPtr::Erase and guard token keyfile data by @damianrickard in https://github.com/veracrypt/VeraCrypt/pull/1816

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1924

* Update Language.zh-cn.xml by @nkh0472 in https://github.com/veracrypt/VeraCrypt/pull/1915

* Update Corsican translation on 2026-10 by @Patriccollu in https://github.com/veracrypt/VeraCrypt/pull/1860

* Windows: flush shell notifications when dismounting with /q by @amail80 in https://github.com/veracrypt/VeraCrypt/pull/1852

* Updated IT translation by @aldolat in https://github.com/veracrypt/VeraCrypt/pull/1925

* Update Norwegian Nynorsk translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1922

* Windows: fix untranslated Pre-Boot check box in Benchmark dialog by @amail80 in https://github.com/veracrypt/VeraCrypt/pull/1930

* Windows: fix untranslated Repair EFI Boot Loader menu item by @amail80 in https://github.com/veracrypt/VeraCrypt/pull/1929

* Update Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1927

* OpenWrt: drop the bash dependency by @flatstik in https://github.com/veracrypt/VeraCrypt/pull/1932

* Linux: mount.veracrypt: honour ro and the flags mount(8) passes by @flatstik in https://github.com/veracrypt/VeraCrypt/pull/1928

* Linux: --stdin: decode the whole password line, fail on bad input by @flatstik in https://github.com/veracrypt/VeraCrypt/pull/1935

* Uniform usage of a-/e-endings in Norwegian Nynorsk by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1936

* Update Language.nl.xml by @RockyTDR in https://github.com/veracrypt/VeraCrypt/pull/1937

* Update Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1940

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1938

* Update Language.zh-cn.xml by @nkh0472 in https://github.com/veracrypt/VeraCrypt/pull/1941

* Translations: write the normal font face "default" untranslated by @amail80 in https://github.com/veracrypt/VeraCrypt/pull/1948

* Translations: make format placeholders match the values passed by @amail80 in https://github.com/veracrypt/VeraCrypt/pull/1947

* Linux, macOS: show two messages that StringFormatter could not format by @amail80 in https://github.com/veracrypt/VeraCrypt/pull/1944

* Translations: show apostrophes and quotation marks as such by @amail80 in https://github.com/veracrypt/VeraCrypt/pull/1945

* Linux, macOS: escape '&' first when writing XML files by @amail80 in https://github.com/veracrypt/VeraCrypt/pull/1943

* Windows: escape the labels of favorite volumes in the favorites file by @amail80 in https://github.com/veracrypt/VeraCrypt/pull/1946

## New Contributors

* @damianrickard made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1758

* @borj404 made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1794

* @ElCruncharino made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1823

* @heinz-goetz made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1887

* @mimoex made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1866

* @flatstik made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1895

* @felix314159 made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1861

* @puleglot made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1891

* @0xDarkMatter made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1851

* @aldolat made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1925



**Full Changelog**: https://github.com/veracrypt/VeraCrypt/compare/VeraCrypt_1.26.29...VeraCrypt_1.26.30



<a id="downloads"></a>

## Downloads



Detached GPG signatures are provided as `sig` links next to each download.



- **Windows**

  - Installer: [VeraCrypt.Setup.1.26.30.exe](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt.Setup.1.26.30.exe) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt.Setup.1.26.30.exe.sig))

  - MSI installer (x64): [VeraCrypt_Setup_x64_1.26.30.msi](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_Setup_x64_1.26.30.msi) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_Setup_x64_1.26.30.msi.sig))

  - MSI installer (ARM64): [VeraCrypt_Setup_arm64_1.26.30.msi](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_Setup_arm64_1.26.30.msi) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_Setup_arm64_1.26.30.msi.sig))

  - Portable version: [VeraCrypt.Portable.1.26.30.exe](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt.Portable.1.26.30.exe) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt.Portable.1.26.30.exe.sig))

  - Debugging symbols: [VeraCrypt_1.26.30_Windows_Symbols.zip](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_1.26.30_Windows_Symbols.zip) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_1.26.30_Windows_Symbols.zip.sig))



- **macOS**

  - Standard package: [VeraCrypt_1.26.30.dmg](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_1.26.30.dmg) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_1.26.30.dmg.sig))

  - FUSE-T package: [VeraCrypt_FUSE-T_1.26.30.dmg](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_FUSE-T_1.26.30.dmg) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_FUSE-T_1.26.30.dmg.sig))



- **Linux**

  - AppImage x64: [VeraCrypt-1.26.30-x86_64.AppImage](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt-1.26.30-x86_64.AppImage) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt-1.26.30-x86_64.AppImage.sig))

  - AppImage ARM64: [VeraCrypt-1.26.30-aarch64.AppImage](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt-1.26.30-aarch64.AppImage) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt-1.26.30-aarch64.AppImage.sig))

  - Legacy GTK2 AppImage: [VeraCrypt-1.26.30-gtk2-legacy-i686.AppImage](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt-1.26.30-gtk2-legacy-i686.AppImage) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt-1.26.30-gtk2-legacy-i686.AppImage.sig)); [VeraCrypt-1.26.30-gtk2-legacy-x86_64.AppImage](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt-1.26.30-gtk2-legacy-x86_64.AppImage) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt-1.26.30-gtk2-legacy-x86_64.AppImage.sig))

  - Generic installer: [veracrypt-1.26.30-setup.tar.bz2](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-setup.tar.bz2) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-setup.tar.bz2.sig))

  - Legacy installer for 32-bit CPU with no SSE2: [veracrypt-1.26.30-x86-legacy-setup.tar.bz2](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-x86-legacy-setup.tar.bz2) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-x86-legacy-setup.tar.bz2.sig))



<details>

<summary>Linux Debian/Ubuntu packages</summary>



- Debian 13: GUI [veracrypt-1.26.30-Debian-13-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Debian-13-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Debian-13-amd64.deb.sig)), [veracrypt-1.26.30-Debian-13-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Debian-13-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Debian-13-arm64.deb.sig)); Console [veracrypt-console-1.26.30-Debian-13-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Debian-13-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Debian-13-amd64.deb.sig)), [veracrypt-console-1.26.30-Debian-13-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Debian-13-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Debian-13-arm64.deb.sig))

- Debian 12: GUI [veracrypt-1.26.30-Debian-12-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Debian-12-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Debian-12-amd64.deb.sig)), [veracrypt-1.26.30-Debian-12-i386.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Debian-12-i386.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Debian-12-i386.deb.sig)); Console [veracrypt-console-1.26.30-Debian-12-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Debian-12-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Debian-12-amd64.deb.sig)), [veracrypt-console-1.26.30-Debian-12-i386.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Debian-12-i386.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Debian-12-i386.deb.sig))

- Ubuntu 26.10: GUI [veracrypt-1.26.30-Ubuntu-26.10-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Ubuntu-26.10-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Ubuntu-26.10-amd64.deb.sig)); Console [veracrypt-console-1.26.30-Ubuntu-26.10-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Ubuntu-26.10-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Ubuntu-26.10-amd64.deb.sig))

- Ubuntu 26.04: GUI [veracrypt-1.26.30-Ubuntu-26.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Ubuntu-26.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Ubuntu-26.04-amd64.deb.sig)), [veracrypt-1.26.30-Ubuntu-26.04-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Ubuntu-26.04-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Ubuntu-26.04-arm64.deb.sig)); Console [veracrypt-console-1.26.30-Ubuntu-26.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Ubuntu-26.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Ubuntu-26.04-amd64.deb.sig)), [veracrypt-console-1.26.30-Ubuntu-26.04-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Ubuntu-26.04-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Ubuntu-26.04-arm64.deb.sig))

- Ubuntu 24.04: GUI [veracrypt-1.26.30-Ubuntu-24.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Ubuntu-24.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Ubuntu-24.04-amd64.deb.sig)), [veracrypt-1.26.30-Ubuntu-24.04-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Ubuntu-24.04-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Ubuntu-24.04-arm64.deb.sig)); Console [veracrypt-console-1.26.30-Ubuntu-24.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Ubuntu-24.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Ubuntu-24.04-amd64.deb.sig)), [veracrypt-console-1.26.30-Ubuntu-24.04-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Ubuntu-24.04-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Ubuntu-24.04-arm64.deb.sig))

- Ubuntu 22.04: GUI [veracrypt-1.26.30-Ubuntu-22.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Ubuntu-22.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Ubuntu-22.04-amd64.deb.sig)); Console [veracrypt-console-1.26.30-Ubuntu-22.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Ubuntu-22.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Ubuntu-22.04-amd64.deb.sig))



</details>



<details>

<summary>Linux RPM packages</summary>



- Fedora 44: GUI [veracrypt-1.26.30-Fedora-44-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Fedora-44-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Fedora-44-x86_64.rpm.sig)); Console [veracrypt-console-1.26.30-Fedora-44-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Fedora-44-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Fedora-44-x86_64.rpm.sig))

- Fedora 43: GUI [veracrypt-1.26.30-Fedora-43-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Fedora-43-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-Fedora-43-x86_64.rpm.sig)); Console [veracrypt-console-1.26.30-Fedora-43-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Fedora-43-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-Fedora-43-x86_64.rpm.sig))

- openSUSE 15: GUI [veracrypt-1.26.30-openSUSE-15-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-openSUSE-15-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-openSUSE-15-x86_64.rpm.sig)); Console [veracrypt-console-1.26.30-openSUSE-15-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-openSUSE-15-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-openSUSE-15-x86_64.rpm.sig))

- CentOS 8: GUI [veracrypt-1.26.30-CentOS-8-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-CentOS-8-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-CentOS-8-x86_64.rpm.sig)); Console [veracrypt-console-1.26.30-CentOS-8-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-CentOS-8-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-CentOS-8-x86_64.rpm.sig))

- CentOS 7: GUI [veracrypt-1.26.30-CentOS-7-i686.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-CentOS-7-i686.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-CentOS-7-i686.rpm.sig)), [veracrypt-1.26.30-CentOS-7-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-CentOS-7-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-CentOS-7-x86_64.rpm.sig)); Console [veracrypt-console-1.26.30-CentOS-7-i686.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-CentOS-7-i686.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-CentOS-7-i686.rpm.sig)), [veracrypt-console-1.26.30-CentOS-7-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-CentOS-7-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-CentOS-7-x86_64.rpm.sig))

- CentOS 6: GUI [veracrypt-1.26.30-CentOS-6-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-CentOS-6-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-CentOS-6-x86_64.rpm.sig)), [veracrypt-1.26.30-CentOS-6-i686.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-CentOS-6-i686.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-CentOS-6-i686.rpm.sig)); Console [veracrypt-console-1.26.30-CentOS-6-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-CentOS-6-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-CentOS-6-x86_64.rpm.sig)), [veracrypt-console-1.26.30-CentOS-6-i686.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-CentOS-6-i686.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-console-1.26.30-CentOS-6-i686.rpm.sig))



</details>



- **Source code**

  - [VeraCrypt_1.26.30_Source.tar.bz2](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_1.26.30_Source.tar.bz2) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_1.26.30_Source.tar.bz2.sig))

  - [VeraCrypt_1.26.30_Source.zip](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_1.26.30_Source.zip) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_1.26.30_Source.zip.sig))

  - [VeraCrypt-DCS-EFI-LGPL_1.26.30_Source.zip](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt-DCS-EFI-LGPL_1.26.30_Source.zip) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt-DCS-EFI-LGPL_1.26.30_Source.zip.sig))



- **Documentation and verification**

  - Full list of changes: [README.TXT](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/README.TXT) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/README.TXT.sig))

  - Checksums: [veracrypt-1.26.30-sha256sum.txt](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-sha256sum.txt) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-sha256sum.txt.sig)); [veracrypt-1.26.30-sha512sum.txt](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-sha512sum.txt) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/veracrypt-1.26.30-sha512sum.txt.sig))

  - User Guide CHM: [VeraCrypt.User.Guide.chm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt.User.Guide.chm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt.User.Guide.chm.sig))

  - Bundle containing all release files: [VeraCrypt_1.26.30_Bundle.7z](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_1.26.30_Bundle.7z) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_1.26.30_Bundle.7z.sig)); [VeraCrypt_1.26.30_Bundle.7z.checksums](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_1.26.30_Bundle.7z.checksums) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.30/VeraCrypt_1.26.30_Bundle.7z.checksums.sig))

## 1.26.29 – 2026-06-12

**Downloads:** [Jump directly to installers, packages, source archives, checksums and signatures](#user-content-downloads)



Binaries for supported operating systems are also available at [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.26.29/).



### Changes between 1.26.24 and 1.26.29 (9 June 2026):



* **All OSes:**

  * Add Argon2id as an alternative memory-hard KDF for non-system volumes.

  * Use "KDF" terminology in the user interface and documentation instead of "PKCS-5 PRF".

  * Update logo icons with simplified icons without extra label text.

  * Harden XML and TLV parsers against malformed input.

  * Security: Fix [GHSA-94c6-mgmv-mqc5](https://github.com/veracrypt/VeraCrypt/security/advisories/GHSA-94c6-mgmv-mqc5): non-default `WOLFCRYPT=1` builds now use wolfCrypt PBKDF2 instead of HKDF and honor VeraCrypt's PBKDF2 iteration count.

    * Reported by [vastblast](https://github.com/vastblast).

    * CVE-2026-53762

  * Fix CPU feature detection and crypto implementation edge cases, including AVX2/leaf 7 detection, BLAKE2s/Argon2 no-SSE2 x86 fallback paths, Camellia SSSE3 dispatch, Twofish x64 multiblock tail handling, and Whirlpool alignment.

  * Update documentation, including Argon2id/KDF information and split Windows/Unix command line usage pages.

  * Update translations.



* **Windows:**

  * Fix rare BSOD issue affecting the VeraCrypt driver.

  * Fix hibernation crash on fresh Windows 11 25H2 installations.

  * Security: Fix [GHSA-jjcr-75w7-58jp](https://github.com/veracrypt/VeraCrypt/security/advisories/GHSA-jjcr-75w7-58jp): hidden volume quick format no longer uses the file-container allocation shortcut that wrote plaintext zero sectors at 128 MiB intervals, preserving plausible deniability.

    * Reported by [vastblast](https://github.com/vastblast).

    * Regression introduced in 1.26.6.

    * CVE-2026-54073

  * Harden Windows driver input validation and crash dump filter handling. (GH PR #1590)

  * Improve driver I/O handling, including safer request completion, ordered volume flush barriers, and better VERIFY/TRIM validation.

  * Fix PBKDF XSTATE cleanup and add Win64 unwind metadata for AES assembly.

  * Speed up mounting when KDF autodetection is selected.

  * Allow selecting which KDF algorithms are included in the benchmark dialog.

  * Allow canceling long mount operations from the wait dialog and with the new `/cancelmount` CLI switch, including auto-mount scans.

  * Add support for new Microsoft UEFI CA 2023 signed EFI bootloaders while preserving Microsoft UEFI CA 2011 support.

  * Improve EFI system encryption repair and upgrade handling, including stuck decryption finalization, Post-OOBE repair, loader restoration verification, and clearer missing-loader reporting.

  * Fix EFI `DcsProp` rewrite handling.

  * Fix ghost drive letter after command line unmount. (GH #337, GH #1426)

  * Fix favorite volume mount race.

  * Validate PIM when changing only the KDF.

  * Fix elevated COM format drive validation and device path normalization. (GH #1670)

  * Fix ReFS formatting during volume creation.

  * Fix MSI traveler disk creation with WHQL-signed drivers, ARM64 MSI build, Start Menu folder upgrades, and discovery of newer SDK MSI tools.

  * Add CLI switch `/protectScreen` to allow disabling screen protection in portable mode.

  * Add argument to CLI switch `/protectMemory` to allow disabling memory protection in portable mode.

  * Add setting and CLI switch `/enableIME` to allow enabling Input Method Editor (IME) in Secure Desktop.

  * Use tab control for VeraCrypt preferences to reduce clutter and size of the dialog.

  * Provide [VeraCrypt C/C++ SDK](https://github.com/veracrypt/VeraCrypt-SDK) for creating volumes.

  * Update LZMA SDK to version 26.01.



* **Linux:**

  * Update Ubuntu 25.04 dependency to require `libwxgtk3.2-1t64`.

  * Add support for building against FUSE3.

  * Add in-kernel NTFS driver selection for NTFS mounts, including `--filesystem=kernel-ntfs` and `-m kernelntfs`.

    * `--filesystem=ntfs3` now pins the kernel ntfs3 driver and bypasses mount helpers such as `mount.ntfs3`.

  * Fix AppImage portability and language loading, bundle a matching FUSE library, and allow AppImage file name to start with "veracrypt" in any case.

  * Suppress redundant "already running" dialog and store the GUI instance lock under XDG paths.

  * Add emergency cleanup for stale unmounts.

  * Parallelize header KDF autodetection.

  * Honor `nokernelcrypto` during external formatting.

  * On WSL, open mounted volumes using Windows Explorer.

  * Add support for reproducible Linux builds, including SOURCE_DATE_EPOCH handling, DEB/RPM packages, and Arch package builds.

  * Add OpenWrt package build and QEMU test scripts.

  * Fix CMake 4 compatibility, CentOS 6 GCC 4.4 builds, and wxWidgets-related build issues.



* **Linux and macOS:**

  * Fix initial width of columns in main UI.

  * Enable Quick Format for normal file containers. The container is sized with `ftruncate()`, so the host filesystem may keep regions unwritten or sparse until data is written to them.

  * Fix hidden volume size estimation for exFAT outer volumes.

  * Fix hidden volume FAT size limit handling.

  * Fix erroneous 2 TiB limit for hidden file containers in GUI wizard.

  * Show volume creation finalization stages.

  * Collect mouse entropy from nested controls in the volume creation wizard.

  * Fix remaining wxWidgets sizer flags.



* **macOS:**

  * Use SMB backend for FUSE-T auxiliary mounts and improve FUSE-T SMB metadata handling and mount stability.

  * Recover mounted volume mount points.

  * Validate format wizard device targets and block partitioned whole-disk alias bypasses.

  * Run APFS formatter elevated when needed and prepare APFS formatter device aliases.

  * Force fresh exFAT layout when formatting volumes.

  * Fix `Command-A` in password fields.

  * Link against wxWidgets 3.2.10 and allow overriding the deployment target.



* **BSD:**

  * FreeBSD: link static wxWidgets builds with iconv.

  * OpenBSD: fix device-hosted volume sizing, honor doas user for mount ownership and FUSE access, and fix CLI build and PCSC exit handling.

## Merged Pull Requests

* Use “unmount” instead of “dismount” in scripts and in text shown to the user by @samhocevar in https://github.com/veracrypt/VeraCrypt/pull/1548

* All platforms: Update logo icons by @Jertzukka in https://github.com/veracrypt/VeraCrypt/pull/1546

* Documentation: Remove XHTML spec and fix errors by @Jertzukka in https://github.com/veracrypt/VeraCrypt/pull/1547

* Linux/FreeBSD/macOS: Column widths correct initially and on update by @Jertzukka in https://github.com/veracrypt/VeraCrypt/pull/1552

* Linux: Update Ubuntu 25.04 Plucky dependencies by @Jertzukka in https://github.com/veracrypt/VeraCrypt/pull/1556

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1564

* Update Corsican translation on 2025-06 by @Patriccollu in https://github.com/veracrypt/VeraCrypt/pull/1566

* Update Language.zh-cn.xml by @nkh0472 in https://github.com/veracrypt/VeraCrypt/pull/1565

* Fix IDC_MOUNTALL in German translation by @helmutbuhler in https://github.com/veracrypt/VeraCrypt/pull/1568

* Fix code compilation. by @uni-kod in https://github.com/veracrypt/VeraCrypt/pull/1583

* Update Corsican translation on 2025-08 by @Patriccollu in https://github.com/veracrypt/VeraCrypt/pull/1591

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1592

* Update Swedish translation by @NickWick13 in https://github.com/veracrypt/VeraCrypt/pull/1594

* Update Language.zh-cn.xml by @nkh0472 in https://github.com/veracrypt/VeraCrypt/pull/1597

* Update Language.de.xml by @Mr-Update in https://github.com/veracrypt/VeraCrypt/pull/1598

* Fix problems inside crash dump filter path by @Chuccle in https://github.com/veracrypt/VeraCrypt/pull/1590

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1606

* Update Language.zh-cn.xml by @nkh0472 in https://github.com/veracrypt/VeraCrypt/pull/1607

* Update Language.de.xml by @Mr-Update in https://github.com/veracrypt/VeraCrypt/pull/1608

* Update Corsican translation on 2025-09 by @Patriccollu in https://github.com/veracrypt/VeraCrypt/pull/1609

* Fix links to documentation in README.md by @codytubbs in https://github.com/veracrypt/VeraCrypt/pull/1617

* Fix: Incorrect tooltip on mouseover due to bad translation key (fix #1635) by @babastienne in https://github.com/veracrypt/VeraCrypt/pull/1637

* Fix ghost drive letter after CLI dismount (Silent mode) by @amail80 in https://github.com/veracrypt/VeraCrypt/pull/1658

* Fix erroneous 2 TiB limit for hidden file containers in GUI wizard by @Computeiful in https://github.com/veracrypt/VeraCrypt/pull/1672

* Update Language.ro.xml by @TigerxWood in https://github.com/veracrypt/VeraCrypt/pull/1636

* Fix hibernation crash on fresh Windows 11 25H2 (BSOD Event 41) by @audriusbuika in https://github.com/veracrypt/VeraCrypt/pull/1671

* Windows: Fix elevated COM format drive validation and device path normalization by @audriusbuika in https://github.com/veracrypt/VeraCrypt/pull/1670

* Added line break between AM Crypto and IDRIX by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1679

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1685

* Fix undefined behavior in StartElevated stderr read loop (#1550) by @curious-rabbit in https://github.com/veracrypt/VeraCrypt/pull/1687

* Update Swedish translation by @NickWick13 in https://github.com/veracrypt/VeraCrypt/pull/1688

* Update Dutch translations by @RockyTDR in https://github.com/veracrypt/VeraCrypt/pull/1691

* Update Language.de.xml by @Mr-Update in https://github.com/veracrypt/VeraCrypt/pull/1692

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1696

* Update Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1697

* Some minor fixes to Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1699

* Update Language.zh-cn.xml by @nkh0472 in https://github.com/veracrypt/VeraCrypt/pull/1694

* Linux: allow mounting NTFS volumes with ntfs3 by @mammothcoding in https://github.com/veracrypt/VeraCrypt/pull/1695

* Update Language.nb.xml by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1701

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1702

* New update to Language.nb.xml by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1703

* Increment version to 1.26.28 in Language.nl.xml by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1705

* Fix whitespace issues in translation files by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1707

* Update Corsican translation on 2026-05 by @Patriccollu in https://github.com/veracrypt/VeraCrypt/pull/1708

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1709

* New translations to Language.nb.xml by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1710

* Update Russian translation for ntfs3 preference by @mammothcoding in https://github.com/veracrypt/VeraCrypt/pull/1704

* Translate English entries to Chinese in XML by @nkh0472 in https://github.com/veracrypt/VeraCrypt/pull/1711

* Update Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1712

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1713

* Update Language.de.xml by @Mr-Update in https://github.com/veracrypt/VeraCrypt/pull/1715

* Update Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1716

* Update Language.nl.xml by @RockyTDR in https://github.com/veracrypt/VeraCrypt/pull/1718

* Update Corsican translation on 2026-05 (2nd) by @Patriccollu in https://github.com/veracrypt/VeraCrypt/pull/1720

* Fix Off-By-One Stack Buffer Overflows in XML Parser by @S4N-T0S in https://github.com/veracrypt/VeraCrypt/pull/1717

* Update Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1722

* Update Language.ro_1.26.28.xml by @TigerxWood in https://github.com/veracrypt/VeraCrypt/pull/1721

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1725

* Update Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1724

* Update Language.de.xml by @Mr-Update in https://github.com/veracrypt/VeraCrypt/pull/1727

* Update Corsican translation on 2026-05 (3rd) by @Patriccollu in https://github.com/veracrypt/VeraCrypt/pull/1728

* Update Language.nl.xml by @RockyTDR in https://github.com/veracrypt/VeraCrypt/pull/1730

* Update Language.zh-cn.xml by @nkh0472 in https://github.com/veracrypt/VeraCrypt/pull/1732

* Ensure reproducible builds on Linux by @curious-rabbit in https://github.com/veracrypt/VeraCrypt/pull/1731

* Update FUSE package version for Debian and Ubuntu by @thurask in https://github.com/veracrypt/VeraCrypt/pull/1736

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1737

* Update to Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1738

* Update Language.nl.xml by @RockyTDR in https://github.com/veracrypt/VeraCrypt/pull/1741

* Linux: add Arch package build support by @idrassi in https://github.com/veracrypt/VeraCrypt/pull/1740

* Update Language.de.xml by @Mr-Update in https://github.com/veracrypt/VeraCrypt/pull/1742

* Update Norwegian Bokmål translation by @sandakersmann in https://github.com/veracrypt/VeraCrypt/pull/1746

* Update Corsican translation on 2026-05 (4th) by @Patriccollu in https://github.com/veracrypt/VeraCrypt/pull/1747

* Update Language.zh-cn.xml by @nkh0472 in https://github.com/veracrypt/VeraCrypt/pull/1748

* Update Language.pl.xml by @Ganeron11 in https://github.com/veracrypt/VeraCrypt/pull/1750

## New Contributors

* @samhocevar made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1548

* @helmutbuhler made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1568

* @uni-kod made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1583

* @Chuccle made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1590

* @codytubbs made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1617

* @babastienne made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1637

* @amail80 made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1658

* @Computeiful made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1672

* @audriusbuika made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1671

* @curious-rabbit made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1687

* @mammothcoding made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1695

* @S4N-T0S made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1717

* @thurask made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1736

* @Ganeron11 made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1750



**Full Changelog**: https://github.com/veracrypt/VeraCrypt/compare/VeraCrypt_1.26.24...VeraCrypt_1.26.29



<a id="downloads"></a>

## Downloads



Detached GPG signatures are provided as `sig` links next to each download.



- **Windows**

  - Installer: [VeraCrypt.Setup.1.26.29.exe](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt.Setup.1.26.29.exe) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt.Setup.1.26.29.exe.sig))

  - MSI installer (x64): [VeraCrypt_Setup_x64_1.26.29.msi](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_Setup_x64_1.26.29.msi) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_Setup_x64_1.26.29.msi.sig))

  -  MSI installer (ARM64): [VeraCrypt_Setup_arm64_1.26.29.msi](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_Setup_arm64_1.26.29.msi) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_Setup_arm64_1.26.29.msi.sig))

  - Portable version: [VeraCrypt.Portable.1.26.29.exe](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt.Portable.1.26.29.exe) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt.Portable.1.26.29.exe.sig))

  - Debugging symbols: [VeraCrypt_1.26.29_Windows_Symbols.zip](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_1.26.29_Windows_Symbols.zip) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_1.26.29_Windows_Symbols.zip.sig))



- **macOS**

  - Standard package: [VeraCrypt_1.26.29.dmg](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_1.26.29.dmg) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_1.26.29.dmg.sig))

  - FUSE-T package: [VeraCrypt_FUSE-T_1.26.29.dmg](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_FUSE-T_1.26.29.dmg) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_FUSE-T_1.26.29.dmg.sig))



- **Linux**

  - AppImage x64: [VeraCrypt-1.26.29-x86_64.AppImage](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt-1.26.29-x86_64.AppImage) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt-1.26.29-x86_64.AppImage.sig))

  - AppImage ARM64: [VeraCrypt-1.26.29-aarch64.AppImage](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt-1.26.29-aarch64.AppImage) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt-1.26.29-aarch64.AppImage.sig))

  - Legacy GTK2 AppImage: [VeraCrypt-1.26.29-gtk2-legacy-i686.AppImage](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt-1.26.29-gtk2-legacy-i686.AppImage) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt-1.26.29-gtk2-legacy-i686.AppImage.sig)); [VeraCrypt-1.26.29-gtk2-legacy-x86_64.AppImage](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt-1.26.29-gtk2-legacy-x86_64.AppImage) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt-1.26.29-gtk2-legacy-x86_64.AppImage.sig))

  - Generic installer: [veracrypt-1.26.29-setup.tar.bz2](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-setup.tar.bz2) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-setup.tar.bz2.sig))

  - Legacy installer for 32-bit CPU with no SSE2: [veracrypt-1.26.29-x86-legacy-setup.tar.bz2](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-x86-legacy-setup.tar.bz2) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-x86-legacy-setup.tar.bz2.sig))



<details>

<summary>Linux Debian/Ubuntu packages</summary>



- Debian 13: GUI [veracrypt-1.26.29-Debian-13-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Debian-13-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Debian-13-amd64.deb.sig)), [veracrypt-1.26.29-Debian-13-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Debian-13-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Debian-13-arm64.deb.sig)); Console [veracrypt-console-1.26.29-Debian-13-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Debian-13-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Debian-13-amd64.deb.sig)), [veracrypt-console-1.26.29-Debian-13-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Debian-13-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Debian-13-arm64.deb.sig))

- Debian 12: GUI [veracrypt-1.26.29-Debian-12-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Debian-12-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Debian-12-amd64.deb.sig)), [veracrypt-1.26.29-Debian-12-i386.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Debian-12-i386.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Debian-12-i386.deb.sig)); Console [veracrypt-console-1.26.29-Debian-12-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Debian-12-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Debian-12-amd64.deb.sig)), [veracrypt-console-1.26.29-Debian-12-i386.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Debian-12-i386.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Debian-12-i386.deb.sig))

- Debian 11: GUI [veracrypt-1.26.29-Debian-11-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Debian-11-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Debian-11-amd64.deb.sig)), [veracrypt-1.26.29-Debian-11-i386.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Debian-11-i386.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Debian-11-i386.deb.sig)); Console [veracrypt-console-1.26.29-Debian-11-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Debian-11-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Debian-11-amd64.deb.sig)), [veracrypt-console-1.26.29-Debian-11-i386.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Debian-11-i386.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Debian-11-i386.deb.sig))

- Ubuntu 26.04: GUI [veracrypt-1.26.29-Ubuntu-26.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Ubuntu-26.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Ubuntu-26.04-amd64.deb.sig)), [veracrypt-1.26.29-Ubuntu-26.04-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Ubuntu-26.04-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Ubuntu-26.04-arm64.deb.sig)); Console [veracrypt-console-1.26.29-Ubuntu-26.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Ubuntu-26.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Ubuntu-26.04-amd64.deb.sig)), [veracrypt-console-1.26.29-Ubuntu-26.04-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Ubuntu-26.04-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Ubuntu-26.04-arm64.deb.sig))

- Ubuntu 25.10: GUI [veracrypt-1.26.29-Ubuntu-25.10-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Ubuntu-25.10-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Ubuntu-25.10-amd64.deb.sig)); Console [veracrypt-console-1.26.29-Ubuntu-25.10-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Ubuntu-25.10-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Ubuntu-25.10-amd64.deb.sig))

- Ubuntu 24.04: GUI [veracrypt-1.26.29-Ubuntu-24.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Ubuntu-24.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Ubuntu-24.04-amd64.deb.sig)), [veracrypt-1.26.29-Ubuntu-24.04-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Ubuntu-24.04-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Ubuntu-24.04-arm64.deb.sig)); Console [veracrypt-console-1.26.29-Ubuntu-24.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Ubuntu-24.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Ubuntu-24.04-amd64.deb.sig)), [veracrypt-console-1.26.29-Ubuntu-24.04-arm64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Ubuntu-24.04-arm64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Ubuntu-24.04-arm64.deb.sig))

- Ubuntu 22.04: GUI [veracrypt-1.26.29-Ubuntu-22.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Ubuntu-22.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Ubuntu-22.04-amd64.deb.sig)); Console [veracrypt-console-1.26.29-Ubuntu-22.04-amd64.deb](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Ubuntu-22.04-amd64.deb) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Ubuntu-22.04-amd64.deb.sig))



</details>



<details>

<summary>Linux RPM packages</summary>



- Fedora 44: GUI [veracrypt-1.26.29-Fedora-44-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Fedora-44-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Fedora-44-x86_64.rpm.sig)); Console [veracrypt-console-1.26.29-Fedora-44-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Fedora-44-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Fedora-44-x86_64.rpm.sig))

- Fedora 43: GUI [veracrypt-1.26.29-Fedora-43-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Fedora-43-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-Fedora-43-x86_64.rpm.sig)); Console [veracrypt-console-1.26.29-Fedora-43-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Fedora-43-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-Fedora-43-x86_64.rpm.sig))

- openSUSE 15: GUI [veracrypt-1.26.29-openSUSE-15-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-openSUSE-15-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-openSUSE-15-x86_64.rpm.sig)); Console [veracrypt-console-1.26.29-openSUSE-15-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-openSUSE-15-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-openSUSE-15-x86_64.rpm.sig))

- CentOS 8: GUI [veracrypt-1.26.29-CentOS-8-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-CentOS-8-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-CentOS-8-x86_64.rpm.sig)); Console [veracrypt-console-1.26.29-CentOS-8-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-CentOS-8-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-CentOS-8-x86_64.rpm.sig))

- CentOS 7: GUI [veracrypt-1.26.29-CentOS-7-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-CentOS-7-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-CentOS-7-x86_64.rpm.sig)), [veracrypt-1.26.29-CentOS-7-i686.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-CentOS-7-i686.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-CentOS-7-i686.rpm.sig)); Console [veracrypt-console-1.26.29-CentOS-7-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-CentOS-7-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-CentOS-7-x86_64.rpm.sig)), [veracrypt-console-1.26.29-CentOS-7-i686.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-CentOS-7-i686.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-CentOS-7-i686.rpm.sig))

- CentOS 6: GUI [veracrypt-1.26.29-CentOS-6-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-CentOS-6-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-CentOS-6-x86_64.rpm.sig)), [veracrypt-1.26.29-CentOS-6-i686.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-CentOS-6-i686.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-CentOS-6-i686.rpm.sig)); Console [veracrypt-console-1.26.29-CentOS-6-x86_64.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-CentOS-6-x86_64.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-CentOS-6-x86_64.rpm.sig)), [veracrypt-console-1.26.29-CentOS-6-i686.rpm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-CentOS-6-i686.rpm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-console-1.26.29-CentOS-6-i686.rpm.sig))



</details>



- **Source code**

  - [VeraCrypt_1.26.29_Source.tar.bz2](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_1.26.29_Source.tar.bz2) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_1.26.29_Source.tar.bz2.sig))

  - [VeraCrypt_1.26.29_Source.zip](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_1.26.29_Source.zip) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_1.26.29_Source.zip.sig))

  - [VeraCrypt-DCS-EFI-LGPL_1.26.29_Source.zip](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt-DCS-EFI-LGPL_1.26.29_Source.zip) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt-DCS-EFI-LGPL_1.26.29_Source.zip.sig))



- **Documentation and verification**

  - Full list of changes: [README.TXT](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/README.TXT) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/README.TXT.sig))

  - Checksums: [veracrypt-1.26.29-sha256sum.txt](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-sha256sum.txt) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-sha256sum.txt.sig)); [veracrypt-1.26.29-sha512sum.txt](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-sha512sum.txt) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/veracrypt-1.26.29-sha512sum.txt.sig))

  - User Guide CHM: [VeraCrypt.User.Guide.chm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt.User.Guide.chm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt.User.Guide.chm.sig)); [VeraCrypt.User.Guide.ru.chm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt.User.Guide.ru.chm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt.User.Guide.ru.chm.sig)); [VeraCrypt.User.Guide.zh-cn.chm](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt.User.Guide.zh-cn.chm) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt.User.Guide.zh-cn.chm.sig))

  - Bundle containing all release files: [VeraCrypt_1.26.29_Bundle.7z](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_1.26.29_Bundle.7z) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_1.26.29_Bundle.7z.sig)); [VeraCrypt_1.26.29_Bundle.7z.checksums](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_1.26.29_Bundle.7z.checksums) ([sig](https://github.com/veracrypt/VeraCrypt/releases/download/VeraCrypt_1.26.29/VeraCrypt_1.26.29_Bundle.7z.checksums.sig))

## 1.26.24 – 2025-05-31

Binaries for supported operating systems are also available at [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.26.24/).



### Changes between 1.26.20 and 1.26.24 (30 May 2025):



* **All OSes:**

  * Fix Whirlpool implementation for big-endian platforms. (GH #1529)

  * Rename "Dismount All" to "Unmount All" in UI, with ALT+u as the new accelerator key (previously ALT+s).

  * Add contributed Chinese and Russian CHM documentation.

  * Update translations.



* **Windows:**

  * Implement screen protection against screenshots and screen recording, enabled by default.

    * This feature can be disabled during installation or via Performance/Driver Configuration settings.

  * Add checkboxes in the MSI installer for controlling memory protection and screen protection features.

    * Introduce command-line options `DISABLEMEMORYPROTECTION` and `DISABLESCREENPROTECTION` for MSI installer configuration.

    * Both options accept values `0` (enabled) or `1` (disabled).

    * *Example:*

      ```

      msiexec /i VeraCrypt_Setup_x64_1.26.24.msi DISABLESCREENPROTECTION=1 /qn REBOOT=ReallySuppress MSIRESTARTMANAGERCONTROL=Disable ACCEPTLICENSE=YES

      ```

  * Fix race conditions when multiple instances of `veracrypt.exe` are launched simultaneously.

  * Update bundled libzip to version 1.11.3.



* **Linux:**

  * Add support for AppImage packaging and usage.

  * Fix absolute path usage for `true` command when checking sudo session status.

  * Fix failure to use Hungarian language translations.

  * Improve generic installer scripts. (GH #1514)

  * Add support for `/run/media/veracrypt` as default mount prefix when `/media` is not available. (GH #1524)

  * Remove `pcsclite` dependency from `.deb`/`.rpm` packages—now detected/loaded dynamically at runtime.



* **macOS:**

  * Fix absolute path usage for `true` command when checking sudo session status.

  * Create symlink for VeraCrypt in `/usr/local/bin` to allow CLI usage.

  * Fix failure to use Hungarian language translations.

## Merged Github Pull Requests

* Update Language.de.xml by @bugtracker2019 in https://github.com/veracrypt/VeraCrypt/pull/1489

* CI: Enable XML Validation Workflow by @Jertzukka in https://github.com/veracrypt/VeraCrypt/pull/1497

* Fix SetupDLL and ExpandVolume Error by @Feryquence in https://github.com/veracrypt/VeraCrypt/pull/1495

* Update Language.nl.xml by @RockyTDR in https://github.com/veracrypt/VeraCrypt/pull/1502

* Linux/FreeBSD: Improvements on installation scripts by @Jertzukka in https://github.com/veracrypt/VeraCrypt/pull/1514

* Refactor: Use symbolic constants for volume header magic numbers by @bernardladenthin in https://github.com/veracrypt/VeraCrypt/pull/1525

* Add alignment constants for derived key and KEY_INFO buffers to ensure SIMD compatibility. by @bernardladenthin in https://github.com/veracrypt/VeraCrypt/pull/1526

* User Guide with HTML by @fzxx in https://github.com/veracrypt/VeraCrypt/pull/1523

* Update Tradition Chinese (Hong Kong) by @harryytm in https://github.com/veracrypt/VeraCrypt/pull/1486

* Fix the whirlpool for big-endian platform by @pingwcy in https://github.com/veracrypt/VeraCrypt/pull/1529

* Fix a mistake by @fzxx in https://github.com/veracrypt/VeraCrypt/pull/1530

* modify unix default mounting point prefix (use /run/media/veracrypt t… by @stevenleeS0ht in https://github.com/veracrypt/VeraCrypt/pull/1524

* Update Polish translation by @Matthaiks in https://github.com/veracrypt/VeraCrypt/pull/1533

* Update Corsican translation on 2025-05 (1t4s) by @Patriccollu in https://github.com/veracrypt/VeraCrypt/pull/1535

* typo Readme.txt by @zaphodapriest in https://github.com/veracrypt/VeraCrypt/pull/1538

* Update Corsican translation on 2025-05 (2) by @Patriccollu in https://github.com/veracrypt/VeraCrypt/pull/1543

## New Contributors

* @bugtracker2019 made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1489

* @Feryquence made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1495

* @bernardladenthin made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1525

* @pingwcy made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1529

* @stevenleeS0ht made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1524

* @zaphodapriest made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1538



**Full Changelog**: https://github.com/veracrypt/VeraCrypt/compare/VeraCrypt_1.26.20...VeraCrypt_1.26.24

## 1.26.20 – 2025-02-05

Binaries for supported operating systems are also available at [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.26.20/).



### Changes between 1.26.18 and 1.26.20 (3 February 2025):



  - All OSes:  

     * Implement SHA-256 acceleration on ARM64 platforms using CPU instructions.

     * Update translations.

     * Replace "Dismount" with "Unmount" across the UI and documentation to align with IT standards (GH #1478)

  - Windows:

     * Fix regression in driver that always allowed defragmentation and caused other side effects.

     * Revert to the previous method of gathering system entropy due to stability issues reported by users.

  - Linux:

     * Fix a regression in Linux Mint affecting administrator password authentication. (GH #1473)

  - macOS:

     * Fix regression that blocked dismounting of volumes. (GH #1467)

     * Resolve a wxWidgets 3.2.6 assertion error related to the undefined switch `use-dummy-sudo-password`. (GH #1470)

## Merged Github Pull Requests

* Update Language.pl.xml by @p0k33m0n in https://github.com/veracrypt/VeraCrypt/pull/1471

* Enable AESNI only on x86 by @Xeonacid in https://github.com/veracrypt/VeraCrypt/pull/1479

* refactor: use the term unmount instead of dismount by @tessus in https://github.com/veracrypt/VeraCrypt/pull/1478

* Update Chinese (Hong Kong) translation by @harryytm in https://github.com/veracrypt/VeraCrypt/pull/1408

## New Contributors

* @p0k33m0n made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1471

* @Xeonacid made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1479

* @tessus made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1478



**Full Changelog**: https://github.com/veracrypt/VeraCrypt/compare/VeraCrypt_1.26.18...VeraCrypt_1.26.20

## 1.26.19 – 2025-01-23

Binaries for supported operating systems are also available at [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.26.19/).



#### Changes between 1.26.18 and 1.26.19 (22 January 2025):



  - macOS:

     * Fix regression that blocked dismounting of volumes. (GH #1467, GH #1469)



**Full Changelog**: https://github.com/veracrypt/VeraCrypt/compare/VeraCrypt_1.26.18...VeraCrypt_1.26.19

## 1.26.18 – 2025-01-22

Binaries for supported operating systems are also available at [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.26.18/).



##### Changes between 1.26.15 and 1.26.18 (20 January 2025):



  - All OSes:

     * Added support for SHA-256 x86 intrinsic to enhance the performance of PBKDF2-HMAC-SHA256.

     * Added support for AES hardware on ARM64 platforms (e.g. Windows ARM64, macOS on Apple Silicon Mx).

     * Updated translations

  - Windows:

     * Dropped support for Windows 32-bit.

     * Set Windows 10 October 2018 Update (version 1809) as the minimum supported version.

     * Reduce driver deadlock occurences under low-memory scenarios caused by re-entrant IRP completions.

     * Fixed failed EFI detection on some PCs where the BootOrder variable is not defined (proposed by @kriegste, GH #360).

     * Fixed "Access Denied" error when updating VeraCrypt using EXE setup following a Windows upgrade.

     * Fixed various issues affecting the EFI system encryption configuration editor.

     * Fixed regression in Traveler Disk creation (GH #886)

     * Replaced the deprecated CryptGenRandom with BCryptGenRandom for generating secure random bytes.

     * Use modern API to gather system entropy for random generation instead of obsolete ones.

     * Update LZMA SDK to version 24.09

     * Update libzip to version 1.11.2

  - Linux:

     * CVE-2024-54187: Added absolute paths when executing system binaries to prevent path hijacking (collaboration with SivertPL @__tfr)

     * CVE-2025-23021: Prevent mounting volumes on system directories and PATH (reported by SivertPL @__tfr)

     * Fixed an assertion issue with the wxWidgets library included in Ubuntu.

     * Improved directory-opening logic by prioritizing xdg-open and adding fallback mechanisms.

     * Ensure that volume exists before starting the mount operation.

     * Fix "Password too long" error message not expanded to include max length (GH #1456)

     * Simplify sudo session detection logic.

  - macOS:

     * CVE-2024-54187: Added absolute paths when executing system binaries to prevent path hijacking (collaboration with SivertPL @__tfr)

     * CVE-2025-23021: Prevent mounting volumes on system directories and PATH (reported by SivertPL @__tfr)

     * Disabled screen capture by default. Added the --allow-screencapture CLI switch to enable it if needed.

     * Ensure that volume exists before starting the mount operation.

     * Implement sudo session detection logic

## Contributors

* Update Language.sv.xml by @NickWick13 in https://github.com/veracrypt/VeraCrypt/pull/1416

* Add Option to Enable/Disable Screen Capture by @denizt in https://github.com/veracrypt/VeraCrypt/pull/1418

* Update Language.ro.xml by @TigerxWood in https://github.com/veracrypt/VeraCrypt/pull/1434





**Full Changelog**: https://github.com/veracrypt/VeraCrypt/compare/VeraCrypt_1.26.15...VeraCrypt_1.26.18

## 1.26.15 – 2024-09-03

Binaries for supported operating systems are also available at [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.26.15/).



##### Changes between 1.26.14 and 1.26.15 (2 September 2024):



- Windows:

  * Fix MSI install/uninstall issues:

    - Fixed error 1603 returned by MSI silent install when REBOOT=ReallySuppress is specified and a reboot is required.

    - Fixed missing documentation and language files from the MSI package.

    - Fixed MSI not installing new documentation and language files when upgrading from an EXE-based installation.

    - Fixed installation folder not being removed after MSI uninstall in some cases.

  * Fix regression during UEFI system decryption that caused the bootloader to persist.



**Full Changelog**: https://github.com/veracrypt/VeraCrypt/compare/VeraCrypt_1.26.14...VeraCrypt_1.26.15

## 1.26.14 – 2024-08-27

Binaries for supported operating systems are also available at [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.26.14/).



##### Changes between 1.26.7 and 1.26.14 (25 August 2024):



- All OSes:

  * Update translations and documentation.

  * Implement language selection settings in non-Windows versions.

  * Make codebase compatible with wxWidgets 3.3 in non-Windows versions.

  * Implement detection of volumes affected by XTS master key vulnerability and warn user about it.

  * Update mount failure error messages to mention removal of TrueCrypt support and old algorithms.



- Windows:

  * Better fix for Secure Desktop issues under Windows 11 22H2.

    - IME is now disabled in Secure Desktop because it is known to cause issues.

  * VeraCrypt Expander: Fix expansion of volumes on disks with a sector size different from 512 (by skl0n6).

  * Fix writing wrong EFI System Encryption Advanced Options to registry.

  * Don't close Setup when exiting VeraCrypt process through system tray Exit menu.

  * Fix failure to format some disks (e.g., VHDX) caused by virtual partition offset not 4K aligned.

  * Fallback to absolute positioning when accessing disks if relative positioning fails.

  * Update zlib to version 1.3.1.



- Linux:

  * Focus PIM field when selected (GH #1239).

  * Fix generic installation script on Konsole in Wayland (GH #1244).

  * Added the ability to build using wolfCrypt as the cryptographic backend. Disabled by default. (Contributed by wolfSSL, GH PR #1227).

  * Allows GUI to launch in a Wayland-only environment (GH #1264).

  * CLI: Don't initially re-ask PIM if it was already specified (GH #1288).

  * CLI: Fix incorrect max hidden volume size for file containers (GH #1338).

  * Enhance ASLR security of generic installer binaries by adding linked flag for old GCC version (reported by @morton-f on Sourceforge).



- macOS:

  * Fix corrupted disk icon in main UI (GH #1218).

  * Fix near zero width PIM input box and simplify wxTextValidator logic (GH #1274).

  * Use correct Disk Utility location when "check filesystem" is ran (GH #1273).

  * Add support for FUSE-T as an alternative to MacFUSE (GH #1055).



- FreeBSD:

  * Fix privilege escalation prompts not showing up (GH #1349).

  * Support automatic detection and mounting of ext2/3/4, exFAT, NTFS filesystems (GH #1350).

  * Use correct Disk Utility location when "check filesystem" is ran (GH #1273).

## New Contributors

* @Mattoje made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1226

* @udev2045 made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1230

* @MayanTigger made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1241

* @lealem47 made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1227

* @kayazeren made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1254

* @JonatanWick made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1270

* @pji2918 made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1291

* @RoboSchmied made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1324

* @nerun made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1306

* @Ozero4 made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1372

* @SebastienGeeraert made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1373

* @chatgptdev made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1386

* @lollolong made their first contribution in https://github.com/veracrypt/VeraCrypt/pull/1389



**Full Changelog**: https://github.com/veracrypt/VeraCrypt/compare/VeraCrypt_1.26.7...VeraCrypt_1.26.14

## 1.26.7 – 2023-10-01

Binaries for supported operating systems are also available at [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.26.7/).



##### Changes between 1.25.9 and 1.26.7 (1 October 2023) :

- All OSes:

   * Security: Ensure that XTS primary key is different from the secondary key when creating volumes

       * Issue unlikely to happen thanks to random generator properties but this check must be added to prevent attacks

       * Reference: CCSS,NSA comment at page 3: https://csrc.nist.gov/csrc/media/Projects/crypto-publication-review-project/documents/initial-comments/sp800-38e-initial-public-comments-2021.pdf

   * Remove TrueCrypt Mode support. Version 1.25.9 can be used to mount or [convert TrueCrypt volumes](https://veracrypt.fr/en/Converting%20TrueCrypt%20volumes%20and%20partitions.html).

   * Complete removal of RIPEMD160 and GOST89 algorithms. Legacy volumes using any of them cannot be mounted by VeraCrypt anymore.

   * Add support for BLAKE2s as new PRF algorithm for both system encryption and standard volumes.

   * Introducing support for EMV banking smart cards as keyfiles for non-system volumes.

       * No need for a separate PKCS#11 module configuration.

       * Card PIN isn't required.

       * Generates secure keyfile content from unique, encoded data present on the banking card.

       * Supports all EMV standard-compliant banking cards.

       * Can be enabled in settings (go to Settings->Security Tokens).

       * Developed by a team of students from the Institut national des sciences appliquées de Rennes.

       * More details about the team and the project are available at https://projets-info.insa-rennes.fr/projets/2022/VeraCrypt/index_en.html.

   * When overwriting an existing file container during volume creation, add its current size to the available free space

   * Add Corsican language support. Update several translations.

   * Update documentation

- Windows:

     * Officially, the minimum supported version is now <strong>Windows 10</strong>. VeraCrypt may still run on Windows 7 and Windows 8/8.1, but no active tests are done on these platforms.

     * EFI Bootloader:

         * Fix bug in PasswordTimeout value handling that caused it to be limited to 255 seconds.

         * Rescue Disk: enhance "Boot Original Windows Loader" by using embedded backup of original Windows loader if it is missing from disk

         * Addition of Blake2s and removal of RIPEMD160 & GOST89

     * Enable memory protection by default. Add option under Performance/Driver Configuration to disable it if needed.

         * Memory protection blocks non-admin processes from reading VeraCrypt memory

         * It may block Screen Readers (Accessibility support) from reading VeraCrypt UI, in which case it can be disabled

         * It can be disabled by setting registry value "VeraCryptEnableMemoryProtection" to 0 under <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\veracrypt</code>

     * Add process mitigation policy to prevent VeraCrypt from being injected by other processes

     * Minor enhancements to RAM Encryption implementation

     * Fix Secure Desktop issues under Windows 11 22H2

     * Implement support for mounting partially encrypted system partitions.

     * Fix false positive detection of new device insertion when Clear Encryption Keys option is enable (System Encryption case only)

     * Better implementation of Fast Create when creating file containers that uses UAC to request required privilege if not already held

     * Allow choosing Fast Create in Format Wizard UI when creating file containers

     * Fix formatting issues during volume creation on some machines.

     * Fix stall issue caused by Quick Format of large file containers

     * Add dropdown menu to Mount button to allow mounting without using the cache.

     * Possible workaround for logarithmic slowdown for Encrypt-In-Place on large volumes.

     * Make Expander first check file existence before proceeding further

     * Allow selecting size unit (KB/MB/GB) for generated keyfiles

     * Display full list of supported cluster sizes for NTFS, ReFS and exFAT filesystems when creating volumes

     * Support drag-n-drop of files and keyfiles in Expander.

     * Implement translation of Expander UI

     * Replace legacy file/dir selection APIs with modern IFileDialog interface for better Windows 11 compatibility

     * Enhancements to dependency dlls safe loading, including delay loading.

     * Remove recommendation of keyfiles files extensions and update documentation to mention risks of third-party file extensions.

     * Add support for more language in the setup installer

     * Update LZMA library to version 23.01

     * Update libzip to version 1.10.1 and zlib to version 1.3.

  - Linux:

     * Fix bug in Random generator on Linux when used with Blake2s that was triggering a self test failure.

     * Modify Random Generator on Linux to exactly match official documentation and the Windows implementation.

     * Fix compatibility issues with Ubuntu 23.04.

     * Fix assert messages displayed when using wxWidgets 3.1.6 and newer.

     * Fix issues launching fsck on Linux.

     * Fix privilege escalation prompts being ignored.

     * Fix wrong size for hidden volume when selecting the option to use all free space.

     * Fix failure to create hidden volume on a disk using CLI caused by wrong maximum size detection.

     * Fix various issues when running in Text mode:

         * Don't allow selecting exFAT/BTRFS filesytem if they are not present or not compatible with the created volume.

         * Fix wrong dismount message displayed when mounting a volume.

         * Hide PIM during entry and re-ask PIM when user entered a wrong value.

         * Fix printing error when checking free space during volume creation in path doesn't exist.

     * Use wxWidgets 3.2.2.1 for static builds (e.g. console only version)

     * Fix compatibility of generic installers with old Linux distros

     * Update help message to indicate that when cascading algorithms they must be separated by dash

     * Better compatibility with building under Alpine Linux and musl libc

  - macOS:

     * Fix issue of VeraCrypt window becoming unusable in use cases involving multiple monitors and change in resolution.

## 1.25.9 – 2022-02-20

Binaries for FreeBSD, Linux, macOS and Windows are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.25.9) and [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.25.9/).



##### Changes between 1.25.7 and 1.25.9 (19 February 2022) :

- All OSes:

  - Update translations (Chinese, Dutch, French, German, Turkish).



- Windows:

  - Make MSI installer compatible with system encryption (Issue #869).

  - Set minimum support for MSI installation to Windows 7.

  - Fix failure to create Traveler Disk when VeraCrypt is installed using MSI (Issue #886).

  - Don't cache the outer volume password when mounting with hidden volume protection if wrong hidden volume password was specified.

  - Reduce the size of EXE installers by almost 50% by using LZMA compression instead of DEFLATE.

  - Fix double-clicking mounted drive in VeraCrypt UI not working in some special Windows configurations (Issue #873).

  - Add registry key to fix BSOD during shutdown/reboot on some machines when using system encryption (Issue #871).

       - Under "`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\veracrypt`", create a REG_DWORD value named "`VeraCryptEraseKeysShutdown`".

       - Setting this registry value to 0 disables erasing system encryption keys which is the cause of BSOD during shutdown on some machines.



- Linux:

  - Fix hidden volume settings not correctly displayed when enabling hidden volume protection in mount options window.

  - Fix generic Linux installer overwriting /usr/sbin if it is a symlink (Issue #888).

  - Fix crash when building with _GLIBCXX_ASSERTIONS defined (Issue #896).

  - Enable building from source without AES-NI support (Issue #892).



- MacOSX:

  - Fix hidden volume settings not correctly displayed when enabling hidden volume protection in mount options window.

## 1.25.7 – 2022-01-08

Binaries for Windows and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.25.7) and [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.25.7/).



##### Changes between 1.25.4 and 1.25.7 (7 January 2022) :

- All OSes:

  - Update translations.

    

- Windows:

  - Restore support of Windows Vista, Windows 7 and Windows 8/8.1.

    - Windows 7 support requires that either **KB3033929** or **KB4474419** is installed.

    - Windows Vista support requires that either **KB4039648** or **KB4474419** is installed.

  - MSI installation only: Fix double-clicking .hc file container inserting %1 instead of volume name in path field.

  - Advanced users: Add registry settings to control driver internal encryption queue to allow tuning performance for SSD disks and having better stability under heavy load.

    - Under registry key `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\veracrypt`:

      - `VeraCryptEncryptionFragmentSize` (REG_DWORD): size of encryption data fragment in KiB. Default is 256. Maximum is 2048.

      - `VeraCryptEncryptionIoRequestCount` (REG_DWORD): maximum number of parallel I/O requests. Default is 16. Maximum is 8192.

      - `VeraCryptEncryptionItemCount` (REG_DWORD): maximum number of encryption queue items processed in parallel. Default as well as maximum is half of `VeraCryptEncryptionIoRequestCount`.

    - The triplet (FragmentSize=512, IoRequestCount=128, ItemCount=64) is an example of parameters that enhance sequential read speed on some SSD NVMe systems.

  - Fix truncate text in installer for some languages.



- MacOSX:

  - Fix resource files inside VeraCrypt application bundle (e.g. HTML documentation, languages XML files) being world-writable. (Reported by Niall O'Reilly)

## 1.25.4 – 2021-12-04

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.25.4) and [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.25.4/).



##### Changes between 1.24-Update8 and 1.25.4 (3 December 2021) :

- All OSes:

  - Speed optimization of Streebog.

  - Update translations.

    

- Windows:

  - Add support for Windows on ARM64 (e.g. Microsoft Surface Pro X) but system encryption not yet supported.

  - Add MSI installer for silent mode deployment (ACCEPTLICENSE=YES must be set in msiexec command line).

    - For now, MSI installer cannot be used if system partition is encrypted with VeraCrypt

    - MSI installer requires Windows 10 or newer

  - Drop support of Windows Vista, Windows 7, Windows 8 and Windows 8.1 because of new requirement for driver code signing.

  - Reduce time of mount when PRF auto-detection is selected.

  - Fix potential memory corruption in driver caused by integer overflow in IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES (reported by Ilja van Sprundel).

  - Replace insecure wcscpy/wcscat/strcpy runtime functions with secure equivalents.

  - Changes EFI Bootloader:

    - Fix memory leak in some cases caused by wrong check of pointer for calling MEM_FREE

    - Clear bootParams variable that may contain sensitive information when halting the system in case of fatal error

    - Add option "KeyboardInputDelay" in DcsProp to control the minimum delay supported between two key strokes

  - Try to workaround Windows Feature Updates issues with system encryption by fixing of bootloader and SetupConfig.ini when system resumes or when session is opened/unlocked

  - Fix failure to load local HTML documentation if application running with administrative privileges

  - Fix freeze when password dialog displayed in secure desktop and try to access token keyfiles protected by PIN

  - Fix failure to launch keyfile generator in secure desktop mode

  - Block Windows from resizing system partition if it is encrypted

  - Add keyboard shortcut to "TrueCrypt mode" in the mount dialog.



- MacOSX:

  - Native support of Apple Silicon M1.

  - Drop official support of Mac OS X 10.7 Lion and Mac OS X 10.8 Mountain Lion.

  - Add UI language support using installed XML files. Language is automatically detected using "LANG" environment variable.

  - Add CLI switch (`--size=max`) and UI option to give a file container all available free space on the disk where it is created.

  - Return error if unknown filesystem value specified in CLI --filesystem switch instead of silently skipping filesystem creation.



- Linux:

  - Add UI language support using installed XML files. Language is automatically detected using "LANG" environment variable

  - Compatiblity with with pam_tmpdir.

  - Display icon in notification area on Ubuntu 18.04 and newer (contibuted by https://unit193.net/).

  - Add CLI switch (`--size=max`) and UI option to give a file container all available free space on the disk where it is created.

  - Return error if unknown filesystem value specified in CLI --filesystem switch instead of silently skipping filesystem creation.



- FreeBSD:

  - Make system devices work under FreeBSD

  - Add CLI switch (`--size=max`) and UI option to give a file container all available free space on the disk where it is created.

  - Return error if unknown filesystem value specified in CLI --filesystem switch instead of silently skipping filesystem creation.



- OpenBSD:

  - Add basic support of OpenBSD

  - Add CLI switch (`--size=max`) and UI option to give a file container all available free space on the disk where it is created.

  - Return error if unknown filesystem value specified in CLI --filesystem switch instead of silently skipping filesystem creation.

## 1.24-Update8_MacOSX – 2020-11-29

Package for MacOSX is available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.24-update8) and [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.24-Update8/).



##### Changes between 1.24-Update7 and 1.24-Update8 (28 November 2020) :

- MacOSX:

  - Fix compatibility issues with macOS Big Sur, especially on Apple Silicon M1 with macFUSE 4.0.x (#699 )

## 1.24-Update7 – 2020-08-09

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.24-update7) and [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.24-Update7/).



##### Changes between 1.24-Update6 and 1.24-Update7 (7 August 2020) :

- Windows:

  - Fix regression in Expander and Format when RAM encryption is enable that was causing volume headers to be corrupted.





- All OSes:

  - Don't allow Hidden volume to have the same password, PIM and keyfiles as Outer volume

  - Fix random crash in 32-bit builds when using Streebog.

  - Enable FIPS mode in JitterEntropy random generator.

  - Update Beginner's Tutorial in documentation to use "MyVolume.hc" instead of "My Volume" for file container name in order to avoid confusion about nature of file nature.

  - Minor code cleanup

    

- Windows:

  - Fix wrong results in benchmark of encryption algorithms when RAM encryption is enabled

  - Fix issue when RAM encryption used, AES selected and AES-NI not supported by CPU that caused the free space of newly created volumes not filled with random data even if "quick format" is not selected.

  - Fix UI for blocking TRIM in system encryption not working in MBR boot mode.

  - Support password drag-n-drop from external applications (e.g. KeePass) to password UI fields which is more secure than using clipboard.

  - Implements compatibility with Windows 10 Modern Standby and Windows 8.1 Connected Standby power model. This makes detection of entering power saving mode more reliable.

  - Avoid displaying waiting dialog when /silent specified for "VeraCrypt Format" during creating of file container using /create switch and a filesystem other than FAT.

  - Use native Windows format program to perform formatting of volume since it is more reliable and only fallback to FormatEx function from fmifs.dll in case of issue.

  - Don't use API for Processor Groups support if there is only 1 CPU group in the system. This can fix slowness issue observed on some PCs with AMD CPUs.

  - Don't allow to encrypt the system drive if it is already encrypted by BitLocker.

  - Implement detection of Hibernate and Fast Startup and disable them if RAM encryption is activated.

  - Warn about Fast Startup if it is enabled during VeraCrypt installation/upgrade, when starting system encryption or when creating a volume, and propose to disable it.

  - Add UI options to control the behavior of automatic bootloader fixing when System Encryption used.

  - Don't allow a directory path to be entered for the file container to be created in Format wizard.

  - Don't try to use fix for CVE-2019-19501 if Windows Shell has been modified or is not running since there is no reliable way to fix it in such non standard configuation.

  - MBR bootloader: fix incorrect compressed data size passed to decompressor in boot sector.

  - Add warning message when typed password reaches maximum length during the system encryption wizard.

  - Fix wrong error message when UTF-8 encoding of entered password exceeds the maximum supported length.

  - Fix crash when using portable 32-bit "VeraCrypt Format.exe" to create hidden volume on a 64-bit machine where VeraCrypt is already installed.

  - Update libzip to latest version 1.7.3.

  - Update translations.



- Linux/MacOSX:

  - Force reading of at least 32 bytes from /dev/random before allowing it to fail gracefully

  - Allow choosing a filesystem other than FAT for Outer volume but display warning about risks of such choice. Implement an estimation of maximum possible size of hidden volume in this case.

  - Erase sensitive memory explicitly instead of relying on the compiler not optimizing calls to method Memory::Erase.

  - Add support for Btrfs filesystem when creating volumes (Linux Only).

  - Update wxWidgets for static builds to version 3.0.5.

## 1.24-Update6 – 2020-03-11

Binaries for Windows are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.24-update6), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.24-Update6/) and [Bitbucket](https://bitbucket.org/veracrypt/veracrypt/downloads/)



##### Changes between 1.24-Update5 and 1.24-Update6 (10 March 2020) :

- Windows:

  - Fix PIM label text truncation in password dialog

  - Fix wrong language used in installer if user selects a language other than English and then selects English before clicking OK on language selection dialog.

## 1.24-Update5 – 2020-03-11

Binaries for Windows are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.24-update5), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.24-Update5/) and [Bitbucket](https://bitbucket.org/veracrypt/veracrypt/downloads/)



##### Changes between 1.24-Update4 and 1.24-Update5 (9 March 2020) :

- Windows:

  - Optimize performance for CPUs that have more than 64 logical processors (contributed by Sachin Keswani from AMD)

  - Support specifying keyfiles (both in tokens and in filesystem) when creating file containers using command line (switches /keyfile, /tokenlib and /tokenpin supported in VeraCrypt Format)

  - Fix leak of keyfiles path and name after VeraCrypt process exits.

  - Add CLI switch /secureDesktop to VeraCrypt Format.

  - Update libzip to version 1.6.1

  - Minor UI fixes

## 1.24-Update4 – 2020-01-24

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.24-update4), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.24-Update4/) and [Bitbucket](https://bitbucket.org/veracrypt/veracrypt/downloads/)



##### Changes between 1.24-Update2 and 1.24-Update4 (23 January 2020) :

- Windows:

  - Fix regression in Expander and Format when RAM encryption is enable that was causing volume headers to be corrupted.

  - Fix failure of Screen Readers (Accessibility support) to read UI by disabling newly introduced memory protection by default and adding a CLI switch (/protectMemory) to enable it when needed.

  - Fix side effects related to the fix for CVE-2019-19501 which caused links in UI not to open.

  - Add switch /signalExit to support notifying [WAITFOR](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/waitfor) Windows command when VeraCrypt.exe exits if /q was specified in CLI (cf documentation for usage).

  - Don't display mount/dismount examples in help dialog for command line in Format and Expander.

  - Documentation and translation updates.



- Linux:

  - Fix console-only build to remove dependency on GTK that is not wanted on headless servers.

  - Fix regression that limited the size available for hidden volumes created on disk or partition.



- MacOSX:

  - Fix regression that limited the size available for hidden volumes created on disk or partition.

## 1.24-Update2 – 2019-12-17

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.24-update2), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.24-Update2/) and [Bitbucket](https://bitbucket.org/veracrypt/veracrypt/downloads/)



##### Changes between 1.24-Hotfix1 and 1.24-Update2 (16 Decembre 2019) :

- All OSs:

  - clear AES key from stack memory when using non-optimized implementation. Doesn't apply to VeraCrypt official build (Reported and fixed by Hanno Böck)

  - Update Jitterentropy RNG Library to version 2.2.0

  - Start following IEEE 1541 agreed naming of bytes (KiB, MiB, GiB, TiB, PiB).

  - Various documentation enhancements.

- Windows:

  - Fix possible local privilege escalation vulnerability during execution of VeraCrypt Expander (CVE-2019-19501)

  - MBR bootloader:

    - workaround for SSD disks that don't allow write operations in BIOS mode with buffers less than 4096 bytes.

    - Don't restore MBR to VeraCrypt value if it is coming from a loader different from us or different from Microsoft one.

  - EFI bootloader:

    - Fix "ActionFailed" not working and add "ActionCancelled" to customize handling of user hitting ESC on password prompt

    - Fix F5 showing previous password after failed authentication attempt. Ensure that even wrong password value are cleared from memory.

  - Fix multi-OS boot compatibility by only setting VeraCrypt as first bootloader of the system if the current first bootloader is Windows one.

  - Add new registry flags for SystemFavoritesService to control updating of EFI BIOS boot menu on shutdown.

  - Allow system encrypted drive to be mounted in WindowsPE even if changing keyboard layout fails (reported and fixed by Sven Strickroth)

  - Enhancements to the mechanism preserving file timestamps, especially for keyfiles.

  - Fix RDRAND instruction not detected on AMD CPUs.

  - Detect cases where RDRAND is flawed (e.g. AMD Ryzen) to avoid using it if enabled by user.

  - Don't write extra 0x00 byte at the end of DcsProp file when modifying it through UI

  - Reduce memory usage of IOCTL_DISK_VERIFY handler used in disk verification by Windows.

  - Add switch /FastCreateFile for VeraCrypt Format.exe to speedup creation of large file container if quick format is selected.

  - Fix the checkbox for skipping verification of Rescue Disk not reflecting the value of /noisocheck switch specified in VeraCrypt Format command line.

  - check "TrueCrypt Mode" in password dialog when mounting a file container with .tc extension

  - Update XML languages files.



- Linux:

  - Fix regression causing admin password to be requested too many times in some cases

  - Fix off by one buffer overflow in function Process::Execute (Reported and fixed by Hanno Böck)

  - Make sure password gets deleted in case of internal error when mounting volume (Reported and fixed by Hanno Böck)

  - Fix passwords using Unicode characters not recognized in text mode.

  - Fix failure to run VeraCrypt binary built for console mode on headless machines.

  - Add switch to force the use of legacy maximum password length (64 UTF8 bytes)

  - Add CLI switch (--use-dummy-sudo-password) to force use of old sudo behavior of sending a dummy password

  - During uninstall, output error message to STDERR instead of STDOUT for better compatibility with package managers.

  - Make sector size mismatch error when mounting disks more verbose.

  - Speedup SHA256 in 64-bit mode by using assembly code.

- MacOSX:

  - Add switch to force the use of legacy maximum password length (64 UTF8 bytes)

  - Fix off by one buffer overflow in function Process::Execute (Reported and fixed by Hanno Böck)

  - Fix passwords using Unicode characters not recognized in text mode.

  - Make sector size mismatch error when mounting disks more verbose.

  - Speedup SHA256 in 64-bit mode by using assembly code.

## 1.24-Hotfix1 – 2019-10-27

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.24-hotfix1), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.24-Hotfix1/) and [Bitbucket](https://bitbucket.org/veracrypt/veracrypt/downloads/)



##### Changes between 1.24 and 1.24-Hotfix1 (27 October 2019) :

- All OSs:

  - Fix 1.24 regression that caused system favorites not to mount at boot if VeraCrypt freshly installed.

  - Fix failure to encrypt system if the current Windows username contains a Unicode non-ASCII character.

  - Make VeraCrypt Expander able to resume expansion of volumes whose previous expansion was aborted before it finishes.

  - Add "Quick Expand" option to VeraCrypt Expander to accelarate the expansion of large file containers.

  - Add several robustness checks and validation in case of system encryption to better handle some corner cases.

  - Minor UI and documentation changes.



- Linux:

  - Workaround gcc 4.4.7 bug under CentOS 6 that caused VeraCrypt built under CentOS 6 to crash when Whirlpool hash is used.

  - Fix "incorrect password attempt" written to /var/log/auth.log when mounting volumes.

  - Fix dropping file in UI not showing its correct path , specifically under GTK-3.

  - Add missing JitterEntropy implementation/



- MacOSX:

  - Fix some devices and partitions not showing in the device selection dialog under OSX 10.13 and newer.

  - Fix keyboard tab navigation between password fields in "Volume Password" page of volume creation wizard.

  - Add missing JitterEntropy implementation/

  - Support APFS filesystem for creation volumes.

  - Support Dark Mode.

## 1.24 – 2019-10-07

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.24), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.24/) and [Bitbucket](https://bitbucket.org/veracrypt/veracrypt/downloads/)



##### Changes between 1.23-Hotfix-2 and 1.24 (6 October 2019) :

- All OSs:

  - Increase password maximum length to 128 bytes in UTF-8 encoding for non-system volumes.

   - Add option to use legacy maximum password length (64) instead of new one for compatibility reasons.

  - Use Hardware RNG based on CPU timing jitter "Jitterentropy" by Stephan Mueller as a good alternative to CPU RDRAND (http://www.chronox.de/jent.html)

  - Speed optimization of XTS mode on 64-bit machine using SSE2 (up to 10% faster).

  - Fix detection of CPU features AVX2/BMI2. Add detection of RDRAND/RDSEED CPU features. Detect Hygon CPU as AMD one.

- Windows:

  - Implement RAM encryption for keys and passwords using ChaCha12 cipher, t1ha non-cryptographic fast hash and ChaCha20 based CSPRNG.

    - Available only on 64-bit machines.

    - Disabled by default. Can be enabled using option in UI.

    - Less than 10% overhead on modern CPUs.

    - Side effect: Windows Hibernate is not possible if VeraCrypt System Encryption is also being used.

  - Mitigate some memory attacks by making VeraCrypt applications memory inaccessible to non-admin users (based on KeePassXC implementation)

  - New security features:

    - Erase system encryption keys from memory during shutdown/reboot to help mitigate some cold boot attacks

    - Add option when system encryption is used to erase all encryption keys from memory when a new device is connected to the system.

    - Add new driver entry point that can be called by applications to erase encryption keys from memory in case of emergency.

  - MBR Bootloader: dynamically determine boot loader memory segment instead of hardcoded values (proposed by neos6464)

  - MBR Bootloader: workaround for issue affecting creation of hidden OS on some SSD drives.

  - Fix issue related to Windows Update breaking VeraCrypt UEFI bootloader.

  - Several enhancements and fixes for EFI bootloader:

    - Implement timeout mechanism for password input. Set default timeout value to 3 minutes and default timeout action to "shutdown".

    - Implement new actions "shutdown" and "reboot" for EFI DcsProp config file.

    - Enhance Rescue Disk implementation of restoring VeraCrypt loader.

    - Fix ESC on password prompt during Pre-Test not starting Windows.

    - Add menu entry in Rescue Disk that enables starting original Windows loader.

    - Fix issue that was preventing Streebog hash from being selected manually during Pre-Boot authentication.

    - If "VeraCrypt" folder is missing from Rescue Disk, it will boot PC directly from bootloader stored on hard drive

      - This makes it easy to create a bootable disk for VeraCrypt from Rescue Disk just by removing/renaming its "VeraCrypt" folder.

  - Add option (disabled by default) to use CPU RDRAND or RDSEED as an additional entropy source for our random generator when available.

  - Add mount option (both UI and command line) that allows mounting a volume without attaching it to the specified drive letter.

  - Update libzip to version 1.5.2

  - Do not create uninstall shortcut in startmenu when installing VeraCrypt. (by Sven Strickroth)

  - Enable selection of Quick Format for file containers creation. Separate Quick Format and Dynamic Volume options in the wizard UI.

  - Fix editor of EFI system encryption configuration file not accepting ENTER key to add new lines.

  - Avoid simultaneous calls of favorites mounting, for example if corresponding hotkey is pressed multiple times.

  - Ensure that only one thread at a time can create a secure desktop.

  - Resize some dialogs in Format and Mount Options to fix some text truncation issues with non-English languages.

  - Fix high CPU usage when using favorites and add switch to disable periodic check on devices to reduce CPU load.

  - Minor UI changes.

  - Updates and corrections to translations and documentation.

- MacOSX:

  - Add check on size of file container during creation to ensure it's smaller than available free disk space. Add CLI switch --no-size-check to disable this check.

- Linux:

  - Make CLI switch --import-token-keyfiles compatible with Non-Interactive mode.

  - Add check on size of file container during creation to ensure it's smaller than available free disk space. Add CLI switch --no-size-check to disable this check.

## 1.23 – 2018-09-13

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.23), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.23/) and [Bitbucket](https://bitbucket.org/veracrypt/veracrypt/downloads/)



##### Changes between 1.22 and 1.23 (12 September 2018) :

- Windows:

  - VeraCrypt is now compatible with default EFI SecureBoot configuration for system encryption.

  - Fix EFI system encryption issues on some machines (e.g. HP, Acer).

  - Support EFI system encryption on Windows LTSB.

  - Add compatibility of system encryption with Windows 10 upgrade using ReflectDrivers mechanism

  - Make EFI Rescue Disk decrypt partition correctly when Windows Repair overwrites first partition sector.

  - Add Driver option in the UI to explicitly allow Windows 8.1 and Windows 10 defragmenter to see VeraCrypt encrypted disks.

  - Add internal verification of binaries embedded signature to protect against some types to tampering attacks.

  - Fix Secure Desktop not working for favorites set to mount at logon on Windows 10 under some circumstances.

  - when Secure Desktop is enabled, use it for Mount Options dialog if it is displayed before password dialog.

   - when extracting files in Setup or Portable mode, decompress zip files docs.zip and Languages.zip in order to have ready to use configuration.

   - Display a balloon tip warning message when text pasted to password field is longer than maximum length and so it will be truncated.

  - Implement language selection mechanism at the start of the installer to make easier for international users.

  - Add check on size of file container during creation to ensure it's smaller than available free disk space.

  - Fix buttons at the bottom not shown when user sets a large system font under Window 7.

  - Fix compatibility issues with some disk drivers that don't support IOCTL_DISK_GET_DRIVE_GEOMETRY_EX ioctl.

- MacOSX:

  - Support pasting values to password fields using keyboard (CMD+V and CMD+A now working properly).

  - Add CheckBox in mount option dialog to force the use of embedded backup header during mount.

  - When performing backup of volume header, automatically try to use embedded backup header if using the main header fails.

  - Implement benchmarking UI for Hash and PKCS-5 PRF algorithms.

- Linux:

  - Don't allow waiting dialog to be closed before the associated operation is finished. This fix a crash under Lubuntu 16.04.

  - Add CheckBox in mount option dialog to force the use of embedded backup header during mount.

  - When performing backup of volume header, automatically try to use embedded backup header if using the main header fails.

  - Implement benchmarking UI for Hash and PKCS-5 PRF algorithms.

  - Remove limitation of hidden volume protection on disk with sector size larger than 512 bytes.

## 1.22 – 2018-04-04

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.22), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.22/) and [Bitbucket](https://bitbucket.org/veracrypt/veracrypt/downloads/)



##### Changes between 1.21 and 1.22 (30 March 2018) :

- All OSs:

  - SIMD speed optimization for Kuznyechik cipher implementation (up to 2x speedup).

  - Add 5 new cascades of cipher algorithms: Camellia-Kuznyechik, Camellia-Serpent, Kuznyechik-AES, Kuznyechik-Serpent-Camellia and Kuznyechik-Twofish.



- Windows:

  - MBR Bootloader: Fix failure to boot hidden OS on some machines.

  - MBR Bootloader: Reduce CPU usage during password prompt.

  - Security enhancement: Add option to block TRIM command for system encryption on SSD drives.

  - Implement TRIM support for non-system SSD drives and add option to enable it (TRIM is disabled by default for non-system volumes).

  - Better fix for "Parameter Incorrect" issues during EFI system encryption in some machines.

  - Driver: remove unnecessary dependency to wcsstr which can cause issues on some machines.

  - Driver: Fix "Incorrect Parameter" error when mounting volumes on some machines.

  - Fix failure to mount system favorites during boot on some machines.

  - Fix current application losing focus when VeraCrypt is run in command line with /quit /silent switches.

  - Fix some cases of external applications freezing during mount/dismount.

  - Fix rare cases of secure desktop for password dialog not visible which caused UI to block.

  - Update libzip to version 1.5.0 that include fixes for some security issues.

  - Extend Secure Desktop feature to smart card PIN entry dialog.

  - Fix truncated license text in installer wizard.

  - Add portable package that allows extracting binaries without asking for admin privileges.

  - Simplify format of language XML files.

  - Workaround for cases where password dialog doesn't get keyboard focus if Secure Desktop is not enabled.



- Linux:

  - Fix failure to install GUI version under recent versions of KDE.

  - Fix wxWidgets assertion failed when backing up/restoring volume header.



- MacOSX:

  - Fix issue preventing some local help files from opening in the browser.

## 1.21 – 2018-01-03

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.21), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.21/) and [Bitbucket](https://bitbucket.org/veracrypt/veracrypt/downloads/)



##### Changes between 1.20 and 1.21 (9 July 2017) :

- All OSs:

  - Fix 1.20 regression crash when running on CPU not supporting extended features.

- Windows:

  - Fix 1.20 regression that caused PIM value stored in favorites to be ignored during mount.

  - Fix 1.20 regression that causes system favorites not to mount in some cases.

  - Fix some cases of "Parameter Incorrect" error during EFI system encryption wizard.

  - Install PDF documents related to EFI system encryption configuration for advanced users:

    - disk_encryption_v1_2.pdf related to EFI hidden OS and full fisk encryption

    - dcs_tpm_owner_02.pdf related to TPM configuration for EFI system encryption.

- FreeBSD:

  - Add support for building on FreeBSD.

## 1.20 – 2018-01-03

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.20), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.20/) and [Bitbucket](https://bitbucket.org/veracrypt/veracrypt/downloads/)



##### Changes between 1.19 and 1.20 (29 June 2017) :

- All OSs:

  - Use 64-bit optimized assembly implementation of Twofish and Camellia by Jussi Kivilinna. 

    - Camellia 2.5 faster when AES-NI supported by CPU. 30% faster without it.

  - Use optimized implementation for SHA-512/SHA256. 

    - 33% speedup on 64-bit systems.

  - Deploy local HTML documentation instead of User Guide PDF.

  - Change links in UI from ones on Codeplex to ones hosted at veracrypt.fr

  - Security: build binaries with support for Address Space Layout Randomization (ASLR).

- Windows:

  - Several fixes and modifications for EFI System Encryption: 

    - Fix bug in EFI system decryption using EFI Rescue Disk

    - Add support for TPM 1.2 and TPM 2.0 (experimental) through DCS low level configuration. 

      - https://dc5.sourceforge.io/docs/dcs_tpm_owner_02.pdf

    - Add Support for EFI full disk encryption and hidden OS using manual procedure (not exposed in UI). 

      - https://dc5.sourceforge.io/docs/disk_encryption_v1_2.pdf

  - Enable using Secure Desktop for password entry. Add preferences option and command line switch (/secureDesktop) to activate it.

  - Use default mount parameters when mounting multiple favorites with password caching.

  - Enable specifying PRF and TrueCryptMode for favorites.

  - Preliminary driver changes to support EFI hidden OS functionality.

  - Fix Streebog not recognized by /hash command line.

  - Add support for ReFS filesystem on Windows 10 when creating normal volumes

  - Fix high CPU usage when favorite configured to mount with VolumeID on arrival.

  - Use CHM file for User Guide instead of PDF.

  - Fix false warning in case of EFI system encryption about Windows not installed on boot drive.

  - Enhancements to driver handling of various disk IOCTL.

  - Enhancements to EFI bootloader. Add possibility to manually edit EFI configuration file.

  - Driver Security: Use enhanced protection of NX pool under Windows 8 and later.

  - Reduce performance impact of internal check for disconnected network drives.

  - Minor fixes.

- MacOSX:

  - OSX 10.7 or newer is required to run VeraCrypt.

  - Make VeraCrypt default handler of .hc & .tc files.

  - Add custom VeraCrypt icon to .hc and .tc files in Finder.

  - Check TrueCryptMode in password dialog when opening container file with .tc extension.

- Linux:

  - Check TrueCryptMode in password dialog when opening container file with .tc extension.

  - Fix executable stack in resulting binary which was caused by crypto assembly files missing the GNU-stack note.

## 1.19 – 2016-10-17

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.19), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.19/) and [Codeplex](https://veracrypt.codeplex.com/wikipage?title=Downloads)

##### Changes between 1.18 and 1.19 (17 October 2016) :
- All OSs:
  - Fix issues raised by Quarkslab audit.
    - Remove GOST89 encryption algorithm.
    - Make PBKDF2 and HMAC code clearer and easier to analyze.
    - Add test vectors for Kuznyechik.
    - Update documentation to warn about risks of using command line switch ”tokenpin”.
  - Use SSE2 optimized Serpent algorithm implementation from Botan project (2.5 times faster on 64-bit platforms).
- Windows:
  - Fix keyboard issues in EFI Boot Loader.
  - Fix crash on 32-bit machines when creating a volume that uses Streebog as PRF.
  - Fix false positive detection of Evil-Maid attacks in some cases (e.g. hidden OS creation)
  - Fix failure to access EFS data on VeraCrypt volumes under Windows 10.
  - Fix wrong password error in the process of copying hidden OS.
  - Fix issues raised by Quarkslab audit:
    - Fix leak of password length in MBR bootloader inherited from TrueCrypt.
    - EFI bootloader: Fix various leaks and erase keyboard buffer after password is typed.
    - Use libzip library for handling zip Rescue Disk file instead of vulnerable XUnzip library.
  - Support EFI system encryption for 32-bit Windows.
  - Perform shutdown instead of reboot during Pre-Test of EFI system encryption to detect incompatible motherboards.
  - Minor GUI and translations fixes.
- MacOSX:
  - Remove dependency to MacFUSE compatibility layer in OSXFuse.

## 1.18a – 2016-08-19

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.18a), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.18/) and [Codeplex](https://veracrypt.codeplex.com/wikipage?title=Downloads)

##### Changes between 1.17 and 1.18a (17 August 2016) :
- All OSs:
  - Support Japanese encryption standard Camellia, including for Windows system encryption (MBR & EFI).
  - Support Russian encryption and hash standards Kuznyechik, Magma and Streebog, including for Windows EFI system encryption.
- Windows:
  - Support EFI Windows system encryption (limitations: no hidden os, no boot custom message)
  - Fix TrueCrypt vulnerability allowing detection of hidden volumes presence(reported by Ivanov Aleksey Mikhailovich, alekc96 [at] mail dot ru)
  - Enhanced protection against dll hijacking attacks.
  - Fix boot issues on some machines by increasing required memory by 1 KiB
  - Add benchmarking of hash algorithms and PRF with PIM (including for pre-boot).
  - Move build system to Visual C++ 2010 for better stability.
  - Workaround for AES-NI support under Hyper-V on Windows Server 2008 R2.
  - Correctly remove driver file veracrypt.sys during uninstall on Windows 64-bit.
  - Implement passing smart card PIN as command line argument (/tokenpin) when explicitly mounting a volume.
  - When no drive letter specified, choose A: or B: only when no other free drive letter is available.
  - Reduce CPU usage caused by the option to disable use of disconnected network drives.
  - Add new volume ID mechanism to be used to identify disks/partitions instead of their device name.
  - Add option to avoid PIM prompt in pre-boot authentication by storing PIM value unencrypted in MBR.
  - Add option and command line switch to hide waiting dialog when performing operations.
  - Add checkbox in "VeraCrypt Format" wizard GUI to skip Rescue Disk verification during system encryption procedure.
  - Allow files drag-n-drop when VeraCrypt is running as elevated process.
  - Minor GUI and translations fixes.
- Linux:
  - Fix mount issue on Fedora 23.
  - Fix mount failure when compiling source code using gcc 5.x.
  - Adhere to XDG Desktop Specification by using XDG_CONFIG_HOME to determine location of configuration files. 
- MacOSX:
  - Solve compatibility issue with newer versions of OSXFuse.

## 1.18 – 2016-08-18

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.18a), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.18/) and [Codeplex](https://veracrypt.codeplex.com/wikipage?title=Downloads)

##### Changes between 1.17 and 1.18a (17 August 2016) :
- All OSs:
  - Support Japanese encryption standard Camellia, including for Windows system encryption (MBR & EFI).
  - Support Russian encryption and hash standards Kuznyechik, Magma and Streebog, including for Windows EFI system encryption.
- Windows:
  - Support EFI Windows system encryption (limitations: no hidden os, no boot custom message)
  - Fix TrueCrypt vulnerability allowing detection of hidden volumes presence(reported by Ivanov Aleksey Mikhailovich, alekc96 [at] mail dot ru)
  - Enhanced protection against dll hijacking attacks.
  - Fix boot issues on some machines by increasing required memory by 1 KiB
  - Add benchmarking of hash algorithms and PRF with PIM (including for pre-boot).
  - Move build system to Visual C++ 2010 for better stability.
  - Workaround for AES-NI support under Hyper-V on Windows Server 2008 R2.
  - Correctly remove driver file veracrypt.sys during uninstall on Windows 64-bit.
  - Implement passing smart card PIN as command line argument (/tokenpin) when explicitly mounting a volume.
  - When no drive letter specified, choose A: or B: only when no other free drive letter is available.
  - Reduce CPU usage caused by the option to disable use of disconnected network drives.
  - Add new volume ID mechanism to be used to identify disks/partitions instead of their device name.
  - Add option to avoid PIM prompt in pre-boot authentication by storing PIM value unencrypted in MBR.
  - Add option and command line switch to hide waiting dialog when performing operations.
  - Add checkbox in "VeraCrypt Format" wizard GUI to skip Rescue Disk verification during system encryption procedure.
  - Allow files drag-n-drop when VeraCrypt is running as elevated process.
  - Minor GUI and translations fixes.
- Linux:
  - Fix mount issue on Fedora 23.
  - Fix mount failure when compiling source code using gcc 5.x.
  - Adhere to XDG Desktop Specification by using XDG_CONFIG_HOME to determine location of configuration files. 
- MacOSX:
  - Solve compatibility issue with newer versions of OSXFuse.

## 1.17 – 2016-02-14

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.17), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.17/) and [Codeplex](https://veracrypt.codeplex.com/wikipage?title=Downloads)

##### Changes between 1.16 and 1.17 (13 February 2016) :
- All OSs:
  - Support UNICODE passwords: all characters are now accepted in passwords (except Windows system encryption)
  - Cut mount/boot time by half thanks to a clever optimization of key derivation (found by [Xavier de Carné de Carnavalet](https://madiba.encs.concordia.ca/~x_decarn/))
  - Optimize Whirlpool code by using assembly (25% speed gain compared to previous code).
  - Add support for creating exFAT volumes.
  - Add GUI indicator for the amount of randomness gathered using mouse movement.
  - Include new icons and graphics contributed by [Andreas Becker](http://www.andreasbecker.de)
- Windows:
  - Fix dll hijacking issue affecting installer that allows code execution with elevation of privilege ([CVE-2016-1281](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-1281)). Reported by [Stefan Kanthak](http://home.arcor.de/skanthak/)
  - Sign binaries using both SHA-1 and SHA-256 to follow new Microsoft recommendations.
  - Solve issues under Comodo/Kaspersky when running an application from a VeraCrypt volume (Reported and fixed by Robert Geisler)
  - Bootloader: Protect password/PIM length by filling the fields to maximum length with '*' after ENTER
  - Solve issue with system favorites not being able to be mounted to drive A:
  - Solve lost focus issues for after displaying the waiting dialog
  - Solve rare issue where some partitions where associated with wrong disk the "Select Device" dialog. 
  - Implement PIM caching, for both system encryption and normal volumes. Add options to activate it.
  - Don't try mounting using cached passwords if password and/or keyfile are specified in the command line.
  - Internal rewrite to make VeraCrypt native UNICODE application.
  - Workaround to avoid false positive detection by some anti-virus software.  
  - Hide disconnected network drives in the list of available drives. Add option to make them available for mounting.
  - Solve issue that caused in some cases configuration and history XML files to be updated even when not needed.
  - Fix leak of path of selected keyfiles in RAM.
  - Fix TB unit can't be deselected in VeraCryptExpander.
  - Add Alt+i keyboard shortcut for "Use PIM" checkbox.
  - Minor GUI and translations fixes.
- Linux/MacOSX:
  - Fix issue of --stdin option not handling correctly passwords that contain a space character (reported and fixed by Codeplex user horsley1953).
  - Fix issue creating volumes using command line with a filesystem other than FAT.
  - Support K/M/G/T suffixes for --size switch to indicate unit to use for size value.

## 1.16 – 2015-10-10

Binaries for Windows, Linux and MacOSX are available at [Launchpad](https://launchpad.net/veracrypt/trunk/1.16), [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.16/) and [Codeplex](https://veracrypt.codeplex.com/releases/view/616110)

##### Changes between 1.15 and 1.16 (7 October 2015) :
- Windows:
  - Modify patch for CVE-2015-7358 vulnerability to solve side effects on Windows while still making it very hard to abuse drive letter handling.
  - Fix failure to restore volume header from an external file in some configurations.
  - Add option to disable “Evil Maid” attack detection for those encountering false positive cases (e.g. FLEXnet/Adobe issue).
  - By default, don’t try to mount using empty password when default keyfile configured or keyfile specified in command line. Add option to restore the old behavior.
    - If mounting using empty password is needed, explicitly specify so in the command line using: /p ""

## 1.15 – 2015-10-10

##### Changes between 1.14 and 1.15 (26 September 2015) :
- Windows:
  - Fix two TrueCrypt vulnerabilities reported by James Forshaw (Google Project Zero)
    - [CVE-2015-7358](https://code.google.com/p/google-security-research/issues/detail?id=538) (critical): Local Elevation of Privilege on Windows by abusing drive letter handling.
    - [CVE-2015-7359](https://code.google.com/p/google-security-research/issues/detail?id=537): Local Elevation of Privilege on Windows caused by incorrect Impersonation Token Handling.
  - Fix regression in mounting of favorite volumes at user logon.
  - Fix display of some Unicode languages (e.g. Chinese) in formatting wizard.
  - Set keyboard focus to PIM field when "Use PIM" is checked.
  - Allow Application key to open context menu on drive letters list
  - Support specifying volumes size in TB in the GUI (command line already supports this)

## 1.14 – 2015-09-19

##### Changes between 1.13 and 1.14 (16 September 2015) :
- All OSs:
  - Mask and unmask PIM value in GUI and bootloader like the password.
- Windows:
  - Solve Rescue Disk damaged error when using cascade ciphers and SHA256 for system encryption.
  - Solve option "Cache password in drive memory" always disabled even if checked in preferences.
  - Solve UI language change not taken into account for new install unless a preference is changed.
  - Implement creating file containers using command line.
  - Driver: disable support of `IOCTL_STORAGE_QUERY_PROPERTY` by default and add option to enable it.
  - Driver: Support returning StorageDeviceProperty if `IOCTL_STORAGE_QUERY_PROPERTY` is supported.
  - Support setting volume label in Explorer through mount option or favorite label value.
  - Fix for Hot Keys assignment dialog issue where OEM-233 is always displayed and can't be changed.
  - Always copy both 32-bit and 64-bit executable binaries during install and in Traveler Disk Setup.
  - Traveler Disk will again use 32-bit exe by default while also offering 64-bit exe.
  - On Windows 64-bit, 32-bit exe files are now available(e.g. if needed to use 32-bit PKCS#11 dll)
  - Include Volume Expander in Traveler Disk Setup.
  - Don't offer creating a restore point if it is disabled in Windows.
  - Add possibility to verify a Rescue Disk ISO image file.
  - Minors fixes in the installer, GUI and driver.
- Linux:
  - Support supplying password using stdin in non interactive mode (contributed by [LouisTakePILLz](https://github.com/LouisTakePILLz])
  - Example: `veracrypt -t ${IMAGE_PATH} ${MOUNT_PATH} --mount --non-interactive --stdin <<< "$PWD"`

## 1.13 – 2015-08-09

Binaries for Windows, Linux and MacOSX are available at [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.13/)

##### Changes between 1.12 and 1.13 (9 August 2015) :
- Windows:
  - Solve TOR crashing when run from a VeraCrypt volume.

##### Changes between 1.0f-2 and 1.12 (5 August 2015) :
- All OSs:
  - Implement "Dynamic Mode" by supporting a Personal Iterations Multiplier (PIM). See documentation for more information.
- Windows:
  - Detect Boot Loader tampering ("Evil Maid" attacks) for system encryption and propose recovery options.
  - Fix buffer overrun issue and other memory related bugs when parsing language XML files.  
  - Fix wrongly reported bad sectors by chkdsk caused by a bug in {"IOCTL_DISK_VERIFY"} handling.
  - Fix privacy issue caused by configuration and history files being updated whenever VeraCrypt is used (reported by Liran Elharar)
  - Fix system favorites not always mounting after cold start.
  - Solve installer error when updating VeraCrypt on Windows 10.
  - Implement decryption of non-system partition/drive.
  - Include 64-bit exe files in the installer and deploy them on 64-bit machines for better performances.
  - Allow using drive letters A: and B: for mounting volumes
  - Make command line argument parsing more strict and robust (e.g. /lz rejected, must be /l z)
  - Add possibility to show system encryption password in Windows GUI and bootloader
  - Solve "Class Already exists" error that was happening for some users.
  - Solve some menu items and GUI fields not translatable
  - Make volumes correctly report Physical Sector size to Windows.
  - Correctly detect switch user/RDP disconnect operations for autodismount on session locked.
  - Add manual selection of partition when resuming in-place encryption.
  - Add command line option (/cache f) to temporarily cache password during favorites mounting.
  - Add waiting dialog for Auto-Mount Devices operations to avoid freezing GUI.
  - Add extra information to displayed error message in order to help analyze reported issues.
  - Disable menu entry for changing system encryption PRF since it's not yet implemented.
  - Fix failure to change password when UAC required (inherited from TrueCrypt)
  - Minor fixes and changes (see Git history for more details)
- Linux:
  - Solve installer issue under KDE when xterm not available
  - Fix warnings on about/LegalNotice dialogs when wxWidgets linked dynamically (N/A for official binary)
  - Support hash names with '-' in command line (sha-256, sha-512 and ripemd-160)
  - Remove "--current-hash" switch and add "--new-hash" to be more coherent with existing switches.
  - When only keyfile specified in command line, don't try to mount using empty password.
    - If mounting using empty password is needed, explicitly specify so using: -p ""

## 1.12 – 2015-08-07

There is compatibility issue between this version and Tor Browser. Subsequent version 1.13 corrects this and it should be used instead.

##### Changes between 1.0f-2 and 1.12 (5 August 2015) :
- All OSs:
  - Implement "Dynamic Mode" by supporting a Personal Iterations Multiplier (PIM). See documentation for more information.
- Windows:
  - Detect Boot Loader tampering ("Evil Maid" attacks) for system encryption and propose recovery options.
  - Fix buffer overrun issue and other memory related bugs when parsing language XML files.  
  - Fix wrongly reported bad sectors by chkdsk caused by a bug in {"IOCTL_DISK_VERIFY"} handling.
  - Fix privacy issue caused by configuration and history files being updated whenever VeraCrypt is used (reported by Liran Elharar)
  - Fix system favorites not always mounting after cold start.
  - Solve installer error when updating VeraCrypt on Windows 10.
  - Implement decryption of non-system partition/drive.
  - Include 64-bit exe files in the installer and deploy them on 64-bit machines for better performances.
  - Allow using drive letters A: and B: for mounting volumes
  - Make command line argument parsing more strict and robust (e.g. /lz rejected, must be /l z)
  - Add possibility to show system encryption password in Windows GUI and bootloader
  - Solve "Class Already exists" error that was happening for some users.
  - Solve some menu items and GUI fields not translatable
  - Make volumes correctly report Physical Sector size to Windows.
  - Correctly detect switch user/RDP disconnect operations for autodismount on session locked.
  - Add manual selection of partition when resuming in-place encryption.
  - Add command line option (/cache f) to temporarily cache password during favorites mounting.
  - Add waiting dialog for Auto-Mount Devices operations to avoid freezing GUI.
  - Add extra information to displayed error message in order to help analyze reported issues.
  - Disable menu entry for changing system encryption PRF since it's not yet implemented.
  - Fix failure to change password when UAC required (inherited from TrueCrypt)
  - Minor fixes and changes (see Git history for more details)
- Linux:
  - Solve installer issue under KDE when xterm not available
  - Fix warnings on about/LegalNotice dialogs when wxWidgets linked dynamically (N/A for official binary)
  - Support hash names with '-' in command line (sha-256, sha-512 and ripemd-160)
  - Remove "--current-hash" switch and add "--new-hash" to be more coherent with existing switches.
  - When only keyfile specified in command line, don't try to mount using empty password.
    - If mounting using empty password is needed, explicitly specify so using: -p ""

## 1.0f-2 – 2015-04-07

Binaries for Windows, Linux and MacOSX are available at [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.0f-2/) and [Codeplex](https://veracrypt.codeplex.com/releases/view/565079)

##### Changes between 1.0f-1 and 1.0f-2 (5 April 2015) :
- All OSs:
  - Mounting speed improvement, up to 20% quicker on 64-bit (contributed by Nils Maier)
  - Add option to set default hash/TrueCryptMode used for mounting volumes.
  - Use TrueCryptMode/Hash specified in command line in password dialog.
- Windows:
  - Solve CryptAcquireContext vulnerability reported by Open Crypto Audit Phase II.
  - Proper handling of random generator failures. Inform user in such cases.
  - TrueCrypt Mode related changes:
  - Support mounting TrueCrypt system partition (no conversion yet)
  - Support TrueCrypt volumes as System Favorites.
  - Correct displaying wrong TrueCrypt mode in volume properties when SHA-256 is used. 
  - Solve PIN BLOCKED issue with smart cards in a special case.
  - Correctly handle file access errors when mounting containers.
  - Solve several issues reported by the Static Code Analysis too Coverity.
  - Bootloader: Add "Verifying Password..." message.
  - When UAC prompt fails (for example timeout), offer the user to retry the operation.
  - Uninstall link now open the standard "Add/Remove Programs" window.
  - On uninstall, remove all VeraCrypt references from registry and disk.
  - Included VeraCryptExpander in the Setup.
  - Add option to temporary cache password when mounting multiple favorites.
  - Minor fixes and enhancements (see git history for more information) 
- MacOSX:
  - Solve issue volumes not auto-dismounting when quitting VeraCrypt.
  - Solve issue VeraCrypt window not reopening by clicking dock icon
- Linux/MacOSX: 
  - Solve preferences dialog not closing when clicking on the 'X' icon.
  - Solve read-only issue when mounting non-FAT volumes in some cases.
  - Support opening/exploring mounted volumes on desktops other than Gnome/KDE.
  - Solve various installer issues when running on less common configurations
  - Minor fixes (see git history for more information)

## 1.0f-1 – 2015-01-06

Binaries for Windows, Linux and MacOSX are available at [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.0f-1/)

##### Changes between 1.0f and 1.0f-1 (4 January 2015) :
- All OSs:
  - Add support for old TrueCrypt 6.0.
  - Change naming of cascades algorithms in GUI for a better description.  
- Linux/MacOSX: 
  - Make cancel button of the preference dialog working.
  - Solve impossibility to enter a one digit size for the volume.
  - Add wait dialog to the benchmark calculation.
- Windows:
  - For Windows XP, correct the installer graphical artefacts.
  - Add TrueCrypt mode to the mounted volume information.

##### Changes between 1.0e and 1.0f (30 December 2014) :
- All OSs:
  - Add support for mounting TrueCrypt volumes.
  - Add support for converting TrueCrypt containers and non-system partitions.
  - Add support for SHA-256 for volume encryption.
  - Make SHA-512 the default key derivation algorithm and change the order of preference of derivation algorithms : SHA-512 -> Whirlpool -> SHA-256 -> RIPEMD160
  - Deprecate RIPEMD160 for non-system encryption.
  - Speedup mount operation by enabling choice of correct hash algorithm.
  - Display a wait dialog during lengthy operations to avoid freezing the GUI.
  - Implement creation of multiple keyfiles at once, with predefined or random size.
  - Always display random gathering dialog before performing sensitive operations.
  - Links in the application now points to the online resources on Codeplex
  - First version of proper VeraCrypt User Guide
- MacOSX: 
  - Implement support for hard drives with a large sector size (> 512).
  - Link against new wxWidgets version 3.0.2
  - Solve truncated text in some Wizard windows.
- Linux:
  - Add support of NTFS formatting of volumes.
  - Correct issue on opening of the user guide PDF
  - Better support for hard drives with a large sector size (> 512).
  - Link against new wxWidgets version 3.0.2
- Windows:
  - Security: fix vulnerability in bootloader detected by Open Crypto Audit and make it more robust.
  - Add support for SHA-256 in system boot encryption.
  - Various optimizations in bootloader.
  - Complete fix of ShellExecute security issue.
  - Kernel driver: check that the password length received from bootloader is less or equal to 64.
  - Correct a random crash when clicking the link for more information on keyfiles
  - Implement option to auto-dismount when user session is locked
  - Add self-test vectors for SHA-256
  - Modern look-and-feel by enabling visual styles.
  - few minor fixed.

## 1.0f – 2015-01-01

Binaries for Windows, Linux and MacOSX are available at [Sourceforge](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.0f/) and [CodePlex](https://veracrypt.codeplex.com/releases/view/565079).

##### Changes between 1.0e and 1.0f (30 December 2014) :
- All OSs:
  - Add support for mounting TrueCrypt volumes.
  - Add support for converting TrueCrypt containers and non-system partitions.
  - Add support for SHA-256 for volume encryption.
  - Make SHA-512 the default key derivation algorithm and change the order of preference of derivation algorithms : SHA-512 -> Whirlpool -> SHA-256 -> RIPEMD160
  - Deprecate RIPEMD160 for non-system encryption.
  - Speedup mount operation by enabling choice of correct hash algorithm.
  - Display a wait dialog during lengthy operations to avoid freezing the GUI.
  - Implement creation of multiple keyfiles at once, with predefined or random size.
  - Always display random gathering dialog before performing sensitive operations.
  - Links in the application now points to the online resources on Codeplex
  - First version of proper VeraCrypt User Guide
- MacOSX: 
  - Implement support for hard drives with a large sector size (> 512).
  - Link against new wxWidgets version 3.0.2
  - Solve truncated text in some Wizard windows.
- Linux:
  - Add support of NTFS formatting of volumes.
  - Correct issue on opening of the user guide PDF
  - Better support for hard drives with a large sector size (> 512).
  - Link against new wxWidgets version 3.0.2
- Windows:
  - Security: fix vulnerability in bootloader detected by Open Crypto Audit and make it more robust.
  - Add support for SHA-256 in system boot encryption.
  - Various optimizations in bootloader.
  - Complete fix of ShellExecute security issue.
  - Kernel driver: check that the password length received from bootloader is less or equal to 64.
  - Correct a random crash when clicking the link for more information on keyfiles
  - Implement option to auto-dismount when user session is locked
  - Add self-test vectors for SHA-256
  - Modern look-and-feel by enabling visual styles.
  - few minor fixed.

## 1.0e – 2014-11-16

VeraCrypt 1.0e is out with many security fixes and performance enhancements. Download for [Windows is here](https://veracrypt.codeplex.com/downloads/get/904891). As usual, a [MacOSX version is available](https://veracrypt.codeplex.com/downloads/get/909095). It supports MacOSX 10.6 and above and it requires OSXFUSE 2.3 and later(https://osxfuse.github.io/). MacFUSE compatibility layer must checked during OSXFUSE installation.
Also a [Linux version is available](https://veracrypt.codeplex.com/downloads/get/908955).The package contains the installation scripts for 32-bit and 64-bit versions, and for GUI and console-only version (choose which script is adapted the best to your machine).

The SHA2 sums of the files and their pgp signature is available in the [Sourceforge download section](https://sourceforge.net/projects/veracrypt/files/VeraCrypt%201.0e/) for this release.

##### Changes between 1.0d and 1.0e (04 September 2014) :
- Correct most of the security vulnerabilities reported by the Open Crypto Audit Project.
- Correct security issues detected by Static Code Analysis, mainly under Windows.
- Correct issue of unresponsiveness when changing password/key file of a volume. Reduce overall time taken for creating encrypted volume/partition.
- Minor fixes (look at git history for more details).
