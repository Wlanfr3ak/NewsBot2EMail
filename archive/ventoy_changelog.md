# Changelog: Ventoy

Quelle: https://www.ventoy.net/en/doc_news.html
Stand: 09.10.2026 08:10

---

## 1.1.18 – 2026-10-09

- Experimental support for SteamOS recovery images. (#3712 #2875 #1815)
- Improve the Linux remount feature to make the ISO partition mountable out of the box on mainstream desktop distros. ( Notes )
- Suppress the duplicate disk icons in the sidebar on some Linux desktop distros.
- Change the ISO partition dm name to stable /dev/mapper/VentoyPart, please refer Notes
- Make the ISO partition mountable for CloneZilla. (#3274)
- Fix Fedora 45 beta boot issue.
- Fix the Windows/WinPE secure boot version check failed issue.
- Fix Persistence intermittently fails on Ubuntu desktop. (#3718)
- Fix the boot issue for Grml 2026.09. (#3751)
- Add support for custom Syslinux-based ISO. (#3760)
- Improvement for latest LinuxConsole release. (#3745)
- Add check for Boot Conf Replace entries in VentoyPlugson. (#3727 #3593)

## 1.1.17 – 2026-07-24

- Optimization for Secure Boot process.
- Fix the boot issue for some UOS release.
- Add support for some EulerOS release.
- Fix the disk_write logic error (#3693)
- Add log for live injection process.
- Add support for Athena OS (#3689)
- Fix the boot issue for latest GhostBSD (#3664)
- Fix the PATH broken in Ventoy2Disk.sh (#3615)
- Fix fdisk detection on BusyBox systems (#3614)
- Fix the issue that proxmox-ve can not boot after install in grub2 mode.
- Languages update.

## 1.1.16 – 2026-06-25

- Fix the boot issue with old UEFI version firmware when secure boot is disabled.
- Fix the latest Kicksecure boot issue. (#3651)
- Fix the issue that VTOY_WIN_UEFI_RES_LOCK option reset when enter VentoyPlugson.
- Languages update.

## 1.1.15 – 2026-06-25

- Fix the boot issue when Secure Boot is disabled in the UEFI firmware. (#3650) Attention: Ventoy use a new UEFI secure boot CA since v1.1.14, so you need to enroll the new key for the first boot time. Please refer Notes

## 1.1.14 – 2026-06-24

- Update secure boot shim file to solve the UEFI CA 2023 issue. This release use a new CA, so you need to enroll the new key for the first boot.
- VentoyPlugson update synchronously.
- Global control plugin add a VTOY_SECURE_BOOT_POLICY option. Notes

## 1.1.13 – 2026-06-24

- This release was deprecated due to a mistake.

## 1.1.12 – 2026-04-23

- Bugfix for ubuntu24.04.4 install failure. (#3567).
- Fix the VirtualBox UEFI display issue when booting Windows. (#3570)
- Improve for UEFI boot Windows/WinPE resolution issue fix.
- Fix Oracle Linux 6.9 install issue

## 1.1.11 – 2026-04-05 ((6th Anniversary Ver.))

- Fix the display issue when UEFI booting Windows/WinPE ISO.
- Add VT_WINDOWS_DISK_NONVTOY_CLOSEST_XXX, VT_LINUX_DISK_NONVTOY_CLOSEST_XXX options in AutoInstall plugin.
- Improvement for Ventoy2Disk.sh (#3537)
- Improvement for porteus-hook.sh (#3532)
- Improvement for booting T2SDE. (#3526 #3468)
- Add support for KylinSecOS

## 1.1.10 – 2025-12-21

- Ventoy2Disk.sh supports musl libc envrionment. (#3332)
- Fix the LinuxGUI program crash issue in wayland environment. (#3406)
- Fix the boot issue with Kylin Server V11. (#3369)
- Fix a Windows boot issue in F2 mode.
- Fix the vhd.vtoy file boot issue in ext4 file system. (#3444)
- Add support for AerynOS. (#3433)
- Language update

## 1.1.09 – 2025-12-12

- Fix the boot issue for openSUSE 16.0 (#3379)
- Experimental support for btrfs file system. (#3438 #3431 #3077 #2093). Please refer About btrfs for details.
- Fix the issue that persistence plugin does not work for latest Arch Linux (#3407)
- Fix VentoyPlugson WebUI display bugs. (#3252)

## 1.1.08 – 2025-12-08

- Add support for FreeBSD 15.0
- New tested ISO. (Total 1300+)

## 1.1.07 – 2025-08-18

- Fix an issue (introduced in v1.1.06) that Ventoy ISO partition cannot be mounted after boot linux distro.

## 1.1.06 – 2025-08-18

- Support TrueNAS Scale (Linux) distro. (#3069 #3137)
- Update xfs to latest. (#3284)
- Fix the boot issue for Parted Magic. (#3304)
- Fix Libreelec 12.2.0 fails to boot. (#3323)
- Fix the order issue in TreeView mode. (#3218)
- Fix the issue that cannot boot Tails 6.13+ (#3171)

## 1.1.05 – 2025-02-24

- Fix the resolution issue when boot some Windows/WinPE ISO in UEFI mode.

## 1.1.04 – 2025-02-22

- Fix the 0x80070001 error when boot and install Windows 11.
- Fix the issue that SLES/OpenSUSE can not boot after install in Ventoy grub2 mode.
- Fix the boot issue for pfSense 2.7.x
- Fix the boot issue for latest TinyCore Linux

## 1.1.03 – 2025-02-21

- This release was deprecated, because it introducted a problem in LinuxGUI version (Windows version and Linux CLI version are OK). Please use latest release.

## 1.1.02 – 2025-02-12

- Fix the Unsupported vtoy type unknown error when boot a VDI file created by VBox7.
- vtoyboot-1.0.36 relese. Please refer Link

## 1.1.01 – 2025-02-10

- Optimization for VTOY_LINUX_REMOUNT implementation to support all Linux distros. Please refer Notes
- Now linux remount is supported by default. So VTOY_LINUX_REMOUNT option now is removed, we don't need it anymore. Please refer Notes

## 1.1.00 – 2025-01-22

- Update to latest Shim (Fix verifying shim SBAT data failed) (#2947)
- Support eweOS ISO (#3068)
- Fix the boot issue of SystemRescue 11.02+ (#2958) (#3058)

## 1.0.99 – 2024-06-08

- Upadte EFI boot files. Fix the Linpus Lite error on some computer.
- Fix the issue that VTOY_LINUX_REMOUNT can not take effect in latest openSUSE. (#2551)
- Fix the issue when installing on /dev/mdX device. (#2846)
- languages.json update

## 1.0.98 – 2024-05-19

- Upadte EFI boot files.
- Fix the issue that can not recognize Ext4 filesytem created with latest gparted.
- Fix the issue that VTOY_LINUX_REMOUNT=1 can not take effect in RHEL9/CentOS9. (#2827)
- Fix the boot issue for latest archlinux. (#2825 #2824)
- Fix the boot issue for latest KAOS.
- languages.json update
- vtoyboot-1.0.35 release. Notes
- New tested ISO. (Total 1200+)
- Wana boot and install OS through network (PXE)? Welcome to my new project, iVentoy https://www.iventoy.com

## 1.0.97 – 2024-01-24

- Add support for FreeBSD 14.0. (#2636)
- Fix Proxmox 8.1 boot issue. (#2657)
- Fix VTOY_LINUX_REMOUNT option does not work with latest linux kernel version. (#2661 #2674)
- Fix the VentoyPlugson issue that default_file value is wrong for more than 10 theme files. (#2608)
- vtoyboot-1.0.31 release. Notes
- Wana boot and install OS through network (PXE)? Welcome to my new project, iVentoy https://www.iventoy.com

## 1.0.96 – 2023-10-06

- Fix that bootpwd not working for VentoyPlugson. (#2584)
- Add escaping for path in VentoyPlugson.sh (#2585)
- Fix the warning prompt for Ventoy2Disk.sh (#2593)
- Fix the issue that VTOY_LINUX_REMOUNT=1 does not work on some distros. (#2475 #2551)
- vtoyboot-1.0.30 release. Notes
- languages.json update

## 1.0.95 – 2023-08-23

- Drag to resize Ventoy2Disk.exe dialog width.
- Fix a bug when booting veket_24.
- Fix a bug when booting the latest UOS server ISO.
- New distro support: vanilladpup
- New distro support: FydeOS 17
- languages.json update

## 1.0.94 – 2023-07-20

- Fix Synchronous Exception on some ARM cpus. (#2488)
- languages.json update

## 1.0.93 – 2023-06-23

- Fix the boot issue for Fedora/CentOS when file name contains special character. (#2360)
- Support unattended auto install for Deepin/UOS.
- Fix a bug that if you plug-out the USB drive during installation, Ventoy will be probabilistically installed to other disk.
- Correct EFI chainloader image device path. (#2397)
- languages.json update.

## 1.0.91 – 2023-04-05

- Add support for FreeBSD 14-CURRENT.
- Fix the issue for booting Bliss OS 15.x (#2329)
- Fix a bug that Fedora boot error if Ventoy partition is NTFS. (#2333)
- Add Recognition for NTFS with large cluster size (greater than 64KB).
- Improve grub2 mode process for legacy BIOS mode.
- languages.json update.

## 1.0.90 – 2023-03-26

- Fix the issue that VTOY_LINUX_REMOUNT option can not work for (Kernel 5.18+) + (Intel Gen11+ CPU).
- Support LibreELEC 11.0+. (#2281)
- Fix the issue that Fedora Rawhide install media not detected. (#2283)
- Add support for chimera linux. (#2309)
- Optimization for Fedora boot process.
- languages.json update.
- New iso support. (Total 1100+)

## 1.0.89 – 2023-03-07

- Fix the issue that VTOY_LINUX_REMOUNT can not work in new linux kernel.
- Fix the issue that Ventoy2Disk_X64.exe can not run under altexe directory.
- Fix the issue that VentoyPlugson_X64.exe exit silently.
- Add missing /FS option for Ventoy2Disk.exe in Windows command line mode.
- Ventoy2Disk.exe automatically change current directory when started from other directory.
- Add tip message when theme file contains non-enclosed literal values. (#2166)
- Ignore reserved space when do non-destructive installation via GUI. (#2168)
- Fix the menu missing issue when there exist an invalid vlnk file. (#2228)
- languages.json update

## 1.0.88 – 2023-01-13

- Fix the VHD(x) boot issue introduced in 1.0.87.
- Add more options for Windows command line mode. Notes
- VentoyPlguson: Fix VTOY_WIN11_BYPASS_CHECK option web page display issue.
- Fix that workaround #2 not working for Legacy BIOS access limit.
- Fix a syntax error in F4 localboot.
- Show file checksum menu title according to the existence of checksum value.
- Automatically switch to en_US when use text mode.
- Add unsupported tip message for 4k native disk.
- languages.json update

## 1.0.87 – 2023-01-07

- Add return to previous menu in secondary boot menu for convenience.
- Add max value for screen resolution option in theme plugin. Notes
- Fix the bug when F2 browse and boot VHD/VHDX files in an extend logic partition.
- Fix the menu title of F5 Tools ---> Power ---> $VTLANG_POWER_REBOOT_EFIFW
- Support BSD style for .md5/.sha1/.sh256/.sha512 checksum file. (#2112)
- Support VENTOY_CHECKSUM file for checksum value match. Notes
- Disable Fn hotkeys in autoinstall/persistence/wim select menu.
- Fix the blank item in the last of Language select menu.
- Fix the menu display issue when use persistence (VTLANG_NO_PERSISTENCE).
- Add support for Lenovo Product Recovery iso file.
- Add support for Dell PER ISO. (#2113)
- grub2 mode supports Porteus ISO file.
- Fix the file path when file checksum in F2 browse mode.
- Add new menu languages
- languages.json update

## 1.0.86 – 2022-12-24

- Add F5 Tools ---> Temporary Control Settings menu. Notes
- Ventoy2Disk.exe now supports command line mode. Notes
- Add VTOY_WIN11_BYPASS_NRO option in global control plugin to bypass online account requirement when intall Windows 11.
- Enable VTOY_WIN11_BYPASS_CHECK and VTOY_WIN11_BYPASS_NRO by default.
- Add resolution_fit option in theme plugin. Notes
- Change the MBR partition type to 0xC if user selects FAT32 when intall Ventoy.
- VentoyPlugson: Add duplicate file path check in different lower/upper cases.
- Change egrep to grep -E for some scripts. (#2083)
- Add new menu languages
- languages.json update

## 1.0.85 – 2022-12-18

- Fix the NTFS/FAT32 format failure in some cases when install Ventoy.
- Grub2 mode supports KNOPPIX.
- Auto memdisk plugin support some IMA/IMG files.
- Optimization for booting memtest86-usb.img.
- Fix the issue when booting Peux distro iso files.
- Add new menu languages
- languages.json update

## 1.0.84 – 2022-12-04

- Add L hotkey to choose language.
- Change F1 hotkey from memdisk mode to help information.
- Add Ctrl+d hotkey for memdisk mode.
- Add VTOY_MENU_LANGUAGE option in Global Control Plugin for default menu language.
- Remove VTOY_HELP_TXT_LANGUAGE option, use VTOY_MENU_LANGUAGE option uniformly.
- Ventoy2Disk.exe: Add Cluster Size option for Ventoy install.
- Ventoy2Disk.exe: Support FAT32 for 32GB+ disk.
- Ventoy2Disk.exe: Fix the format failure when install Ventoy in some WinPE/Lite Windows.
- Ventoy2Disk.exe: Change the lock icon for secure boot option to a yellow picture.
- Ventoy2Disk.exe: Show a tip message for cluster size when the mouse hover on the file system string.
- Ventoy2Disk.exe: Add UDF file system for Ventoy install.
- VentoyPlugson.exe: Fix the garbled characters when preview json which contains unicode characters.
- Add VentoyPlugson_X64.exe for convenience when used in WinPE.
- Update Shim/Mokmanager efi files.
- languages.json update

## 1.0.82 – 2022-11-17

- Ventoy2Disk.exe: Add exFAT/NTFS/FAT32 options in Option-->Partition Configuration for Ventoy installation.
- Ventoy2Disk.exe: Display Ventoy partition file system in selected disk
- Ventoy2Disk.exe: Fix the issue that string "Status x%" is missing for translations (#1667)
- Update Shim/Mokmanager efi file from Fedora 37.
- Add VTOY_SHOW_PASSWORD_ASTERISK option in global control plugon. (#1931)
- VentoyPlugson: Fix the issue that secondary boot menu option mismatch between web page and json file.
- Fix the issue that Linux WEB/GUI version does not restore MBR when updating. (#1935)
- Change Ventoy LiveCD GUI default language to English (#1938)
- Fix the issue that help line disappears when auto-going to a Fn submenu. (#1939)
- Fix an issue that CGI backup tool can not open after boot WePE.
- Optimization for Windows unattended install process.
- Fix the disk display error when pCloud virtual disk is installed in Windows OS.
- languages.json update

## 1.0.81 – 2022-10-25

- Show asterisks ('*') when typing password (PR #1868)
- Disable Fn hotkey during secondary boot menu.
- Fix the issue that VTOY_LINUX_REMOUNT=1 does not work with Batocera 35 (#1878)
- Fix the issue that rockcluster, part of config missing during install. (#1900)
- Fix VentoyPlugson issue when ISO partition has a drive label with a space. (#1901)
- Add support for easyOS easy-4.4.2-amd64.img. (#1926)
- VentoyPlugson: Add json preview feature.
- VentoyPlugson: Add reset button.
- VentoyPlugson: Add configuration active identifier for each tab.
- Add _VTNORMAL identifier.
- languages.json update

## 1.0.80 – 2022-09-21

- Add secondary boot menu for boot compatibility improvement. Notes
- Now wimboot mode supports WinPE ISO files.
- Make injection plugin available in WIMBOOT mode. (#1834)
- Add support for HoloISO. (#1644)
- Bugfix for booting latest Gentoo live. (#1770)
- Bugfix for booting latest ALT linux. (#1784)
- Always use /bin/bash to launch VentoyPlugson.sh (#1809)
- Add w and r hotkey for WIMBOOT and GRUB2 mode. (#1837)
- Fix typo in VentoyPlugson web page. (#1782)
- Fix the 'overflow is detected' error in WIMBOOT mode for large ISO file.
- Fix a bug when ISO contains a ks=file:/xxx boot parameter.
- languages.json update
- Total 1000+ iso files tested. (A big milestone)

## 1.0.79 – 2022-07-28

- Rollback Super-UEFIinSecureBoot-Disk to v3.3
- Support Fedora CoreOS (#1727)
- Fix a bug when rhel based distribution has an external kickstart file. (#1717)
- Fix a bug that VTOY_LINUX_REMOUNT option doesn't take effect in openSUSE. (#1729)
- Fix a bug that autosel option doesn't work (#1716)
- Fix a bug for Ventoy2Disk.gtk that reserved space can not contains digit 9. (#1753)
- Fix a bug that can not find repo when install Kylin V10SP2 Server.
- vtoyboot-1.0.24 release. Notes
- languages.json update
- New ISO support (total 940+)

## 1.0.78 – 2022-07-01

- Improvement for Boot Conf Replace Plugin , now can replace at most 2 files. Notes
- Update Super-UEFIinSecureBoot-Disk to v3.4 (#1695)
- .ventoyignore also works in F2 Browser Mode.
- Fix the bug when booting latest KaOS. (#1696)
- Fix a bug when booting TrueNAS Core 13.0. (#1684)
- Fix a bug when booting StorageCraft StorageProtect SPX. (#1683)
- Auto remove the redundant trailing slash when set directory path on VentoyPlugson page.
- languages.json update
- New ISO support (total 920+)
- Document: How To Delete Ventoy Secure Boot Key

## 1.0.77 – 2022-06-19

- Fix the UEFI memory alloc failure in some computer. (#1671)
- Fix the issue that install media not recognized when install Clear Linux. (#1674)
- Fix a bug when booting daphile-21.01
- languages.json update

## 1.0.76 – 2022-06-12

- Enable secure boot support option by default when install Ventoy. Notes
- Fix the issue when enrolling key for secure boot with Super UEFIinSecureBoot Disk v3-3.
- Auto use memdisk/grub2/wimboot mode if the ISO file name contains special identifier. Notes
- Fix a bug when booting linux vdisk (.vtoy) file in Legacy BIOS mode with F2 or ventoy_grub.cfg.
- Support EasyOS partition resize at the first boot time.
- Support EasyOS 4.0
- Support Stratodesk NoTouch OS. (#1652)
- Update languages.json
- New ISO support (total 900+)

## 1.0.75 – 2022-05-31

- Update Super UEFIinSecureBoot Disk v3-2
- By default use memdisk mode when booting iKuai OS.
- Fix the bug when booting linx iso (#1600)
- Fix a bug when booting latest Alpine linux.
- Fix a bug when booting easyos 3.4.3+
- Fix a bug when booting ATLAS Windows ISO.
- Fix a bug when UEFI booting KaOS-2022.04-x86_64.iso.
- Fix the bug when booting ALT Linux in UEFI mode. (#1645)
- Support programs loading for DLC Boot PE. (#1647)
- Fix a bug in menu tip plugin webpage of VentoyPlugson. (#1602)
- Fix a bug when booting RHEL/CentOS/Fedora with LVM device in the computer.
- Fix a bug when boot in F2 browser mode if the computer has more than one disks with same size.
- Update languages.json
- New ISO support (total 880+)

## 1.0.74 – 2022-04-28

- Show the directory path in the return menu for TreeView mode and Browser mode.
- Fix a bug that Windows ISO in local disk can not install when boot through F2 browser mode in Legacy BIOS mode.
- Fix a bug when install Ventoy if the USB already mounted at a path which contains space.
- Fix the issue when booting customized CentOS7 with inst.ks=cdrom:/xxx boot parameter.
- Fix a bug for Linux GUI program when update from old release. (#1590)
- Fix the issue when booting Fedora with VTOY_LINUX_REMOUNT=1
- Fix the log and ini file owner attribute for VentoyGUI in linux.
- Fix the issue when booting Prime OS 2.1.0.
- Fix the issue when booting Euler OS V2
- Update languages.json
- Document: About USB hardware problem
- New ISO support (total 850+)

## 1.0.73 – 2022-04-06

- A dialog will be popped up when you click install button if Ventoy already installed in the disk. Then you must enter YES in the text box manually to confirm the installation.
- If the ISO file name is too long to displayed completely. You can press left or right arrow keys ← → to scroll the menu.
- Add F5 Tools --> Power --> Reboot to EFI setup menu in UEFI mode, (reboot to UEFI BIOS Setup).
- Add F5 Tools --> Hardware Information menu.
- We can set menu tip position and color for per-theme. Notes
- Prevent DLL search order hijacking for Ventoy2Disk.exe/VentoyPlugson.exe/VentoyVlnk.exe.
- Fixed a bug that VTOY_LINUX_REMOUNT option does not take effect for Manjaro/Arch.
- vtoyboot-1.0.21 release. Notes
- languages.json update

## 1.0.72 – 2022-03-26

- Add support for venomlinux (#1526)
- Add missing execute bit when packing (#1530)
- vtoyboot-1.0.20 release. Notes
- Fix some typo and grammar mistakes in the document and language.json

## 1.0.71 – 2022-03-11

- VTOY_DEFAULT_IMAGE can be set to F2> to automatically enter F2 browser mode.
- Fix the bug when booting FreeBSD 13.0 in F2 browser mode.
- Auto use memdisk mode for Memtest86+ and KolibriOS iso file.
- Support Easy Recovery Essentials for Win10/Win11.
- Suppress Fn hotkey when VTOY_DEFAULT_IMAGE is set to Fn> .
- New ISO support (total 830+)

## 1.0.70 – 2022-02-19

- Fix Porteus Kiosk boot issue in latest Ventoy release. (#1446)
- Add cmdline mode for VentoyVlnk.exe
- Support latest Qubes 4.1.0 release.
- Auto use grub2 mode for krd.iso.
- Fix a few bugs for VentoyPlugson web.
- Add a tip when save ventoy.json failed in VentoyPlugson.
- Fix the bug when booting Windows 7 iso files in local disk.
- Update help text.
- Update languages.json

## 1.0.69 – 2022-02-15

- Fix a BUG that Ventoy shows NO ISO found ... if the partition for ISO files is in NTFS format. (introduced in 1.0.68 which has been deprecated)

## 1.0.68 – 2022-02-15

- Support F2 to browse Ventoy self. Notes
- Optimize menu generation speed when browsing files
- Skip System Volume Information directory when browsing files.
- Vlnk supports files in Ventoy disk reserved space.
- Make VTOY_TREE_VIEW_MENU_STYLE also control the browser menu style. (#1439)

## 1.0.67 – 2022-02-14

- Move the reboot/halt menu from F2 to F5 Tools/Power
- Change default menu display mode back to ListView mode. (Powerful habit :) )
- Fix the bug when booting SystemRescue 8.X/9.X
- Fix the bug in VentoyVlnk.sh when create vlnk file for files in a NTFS partition. (#1430)
- Fix the bug that the 1st menu item is not always selected when switching between submenus.
- Fix the bug that file injection does not take effect for windows.(introduced in 1.0.66).

## 1.0.66 – 2022-02-13

- Change the default menu display mode to TreeView mode.
- Fix a bug when booting the latest recalbox-x86_64.img. (#1423)
- Fix a bug about the CGI tool after boot WePE.
- Support /dev/disk/by-id/xxx format input in Ventoy2Disk.sh (#1422)
- languages.json update

## 1.0.65 – 2022-02-04

- Auto Installation Plugin now supports cloud-init for latest ubuntu server release (20.x+).
- Fix Ventoy Plugson Web update and language display issue.
- Update the tip message for VTOY_DEFAULT_SEARCH_ROOT (#1373)
- Add check for size in CreatePersistentImg.sh (#1384)
- VTOY_LINUX_REMOUNT support for both 64bit(x86_64) and 32bit(i386) linux.
- languages.json update
- New ISO support (total 800+)

## 1.0.64 – 2022-01-08

- Support CentOS-9-Stream (#1335)
- Add an experimental option VTOY_LINUX_REMOUNT in global control plugin . Notes This option make the image partition where the ISO files locate mountable after boot into a linux live environment.

## 1.0.63 – 2021-12-20

- VentoyPlugson.exe fixed the "plugson.tar.xz not found" error, when the path contains unicode characters.
- Add check for invalid characters in menu_class plugin in VentoyPlugson.
- Fixed a bug when booting latest Solus in UEFI mode.
- Optimization for Ventoy2Disk.sh
- languages.json update

## 1.0.62 – 2021-12-02

- Add default_file option in theme plugin. Notes
- Add F5 Tools --> Theme Select menu to switch between themes. Notes
- Automatically fix volume abnormal status when do non-destructive install in Windows.
- Optimization for FreeBSD boot process.
- Optimization for Ventoy2Disk.sh
- languages.json update

## 1.0.61 – 2021-11-13

- Fix some BUGs when do update after non-destructive installation.
- Before non-destructive installation in Windows, use chkdsk to fix the volume if needed.
- Add dir option in menu_tip plugin. Notes
- languages.json update

## 1.0.60 – 2021-11-12

- Fix some BUGs when do non-destructive installation with GPT disk. Now 1.0.59 release is deprecated.
- Add non-destructive installation support in Linux Ventoy2Disk.sh. Notes
- Optimization for Ventoy2Disk.exe. Use powershell as an alternative when VDS is unavailable.
- Document: About GRUB2 Mode
- Help information language update
- languages.json update

## 1.0.59 – 2021-11-10

- Show a warning message if ventoy.json is in UCS-2 encoding. (#1125)

## 1.0.58 – 2021-11-06

- Add Ventoy2Disk_X64.exe/Ventoy2Disk_ARM.exe/Ventoy2Disk_ARM64.exe . Notes
- Fix the false error report about ventoy.jsonxxx file. (#1190)
- Fix a bug when booting HDM17x64_17.20.0_ADV_Linux_Downloadly.ir.iso
- languages.json update

## 1.0.57 – 2021-10-29

- Optimization for Ventoy2Disk.exe. Improve the success rate of upgrade.
- Change help hotkey from Ctrl+h to h .
- Change checksum hotkey from Ctrl+m to m .
- Add Checksum file compare feature. Notes
- Improvement for multi-mode option. Now you can use for example theme_uefi and theme at the same time. Notes
- Improve Boot Conf Replace Plugin for systemd-boot in UEFI mode. Notes
- Fix a bug when booting latest ROSA distro in Legacy BIOS mode.
- Help information translation update
- languages.json update

## 1.0.56 – 2021-10-22

- Add Ctrl+h hotkey for help.
- Add VTOY_HELP_TXT_LANGUAGE option in Global Control plugin. Notes
- Add Ctrl+m hotkey for file cheksum. Notes
- Add timeout option in Auto Install plugin. Notes
- Add support for Eset SysRescue image file. (#1162)
- Fix the long delay when boot tails in UEFI mode.
- languages.json update
- New image support ( total 760+ )

## 1.0.55 – 2021-10-17

- Optimization for Ventoy2Disk.exe. Improve the success rate of installation and upgrade.
- Add VTOY_WIN11_BYPASS_CHECK option in Global Control plugin. Notes
- Add VentoyAutoRun feature for Windows ISO in Injection Plugin . Notes
- Compatibility improvement for WinPE ISO
- languages.json update

## 1.0.54 – 2021-10-12

- Ventoy Live CD update and has a GUI now. Notes
- Support WinPE with PESET.EXE
- Fix a bug when booting trisquel 10 (#1127)
- Fix a bug when install Untangle (#1120)
- Fix a bug that menu_tip is not shown for the default menu item.
- Support Porteus v5.0rc3
- Document When Ventoy2Disk.exe Failed To Update
- languages.json update

## 1.0.53 – 2021-09-27

- Add menu_tip plugin. Notes
- Add --qt5 parameter for VentoyGUI. Notes
- Support nondestructively shrink persistence dat file. Notes
- Document How to inject files to Linux Live OS
- Document Replace ISO boot menu background
- languages.json update

## 1.0.52 – 2021-09-13

- Add support for Emergency Boot Kit
- Continue to boot when the ISO file size is invalid.
- Fix a bug when booting puppy-4.3.1
- languages.json update

## 1.0.51 – 2021-08-27

- Fix the mount issue for 2K10 Win7x64 PE
- Support 2k10 PE x86 series
- Support escaped quotes (\") in ventoy.json. (#1062)
- Support Lenovo EasyStartup
- New image support

## 1.0.50 – 2021-08-14

- Support synoboot.img v1.02b
- Fix the boot issue for some Win7PE
- Fix the boot issue for Windows in UEFI mode on some Dell server
- Fix the boot issue for Untangle distro
- Fix the boot issue when install some Lite Windows version with special file name.
- Fix "Failed to open random seed file" error message for arch linux in some UEFI machine.
- Fix the check media issue for SUSE/openSUSE.
- Add F5-->Tools-->Ventoy UEFI Utilities-->Show EFI Drivers menu
- vtoyboot-1.0.18 release Notes
- languages.ini update

## 1.0.49 – 2021-08-03

- Compatibility improvement for some WinPE
- Optimization for booting SUSE/openSUSE
- Fixed the boot issue for "StorageCraft Recovery Environment" ISO in UEFI mode (#1034)
- languages.ini update

## 1.0.48 – 2021-08-01

- Add Option --> Generate VTSI File feature. Notes
- Fix the missing program issue for EasyU
- Fix Windows boot issue when Ventoy is booted from rEFInd
- Fix the boot issue for latest release of Artix Linux
- Fix some bugs for nested boot (e.g. Ventoy-->rEFInd-->Ventoy).
- Better support for custom arch iso (#1021)
- Remove VentoyWebDeepin.sh
- languages.ini update

## 1.0.47 – 2021-07-17

- Optimizations for booting openwrt
- Support some floppy images in Memdisk mode
- Remove the 2TB limit for the reserved space in Ventoy2Disk.exe
- Fixed a bug when booting big boot.wim file.
- Compatibility improvement for WinPE which contains PECMD.EXE
- Fix Parabola rEFInd booting (#989)
- Add check for the built-in browser in WebDeepin.sh
- Speedup md5sum/sha1sum/sha256sum/sha512sum command
- vtoyboot-1.0.16 release. Fixed the corruption after update kernel or install Nvidia driver. Notes
- vdiskchain-1.3 release. Notes
- languages.ini update
- New image support

## 1.0.46 – 2021-06-13

- Compatibility improvement for booting Linux ISO file in Legacy BIOS mode.
- vtoyboot-1.0.13 release. Notes
- Windows VHD(x) boot plugin vhdimg v3.0 release. Notes
- Fix a bug about ventoy version message position when VTOY_DEFAULT_IMG was set to F6>xxx
- Optimization for booting CRUX distro
- Make priority key>parent in menu class plugin
- languages.ini update
- New image support

## 1.0.45 – 2021-05-29

- Add random theme select support. Notes
- Add parent option in auto_install plugin. Notes
- Add parent option in injection plugin. Notes
- Add ExtendPersistentImg.sh for lossless expansion of persistent dat file. Notes
- Print progress when use md5sum/sha1sum/sha256sum/sha512sum in grub shell.
- Fix pack error in vDisk env (#912)
- languages.ini update

## 1.0.44 – 2021-05-15

- Add WIMBOOT Mode. Notes
- Fix issue when install Fedora Server Edition
- Add -o option in CreatePersistentImg.sh (#903)
- Add parent/isopwd/wimpwd/imgpwd/efipwd/vhdpwd/vtoypwd options in password plugin. Notes
- Fix a bug about unaligned read in UEFI mode.

## 1.0.43 – 2021-05-08

- Change the UTF-16 languages.ini to UTF-8 languages.json
- The update button is available even if data corrupted in VTOYEFI partition.
- Set the default focus to No when you click Install button in Ventoy2Disk.exe.
- Fix a BUG when booting Windows VHD(x) with the latest ventoy_vhdboot.img.
- Support boot Windows VHD(x) files at local disk. Notes

## 1.0.42 – 2021-04-27

- Add * fuzzy matching for menu_alias/image_list/auto_install/persistence ... plugins. Notes
- Add parent option in menu_class plugin. Notes
- Add F4boot F5tool builtin class in menu_class plugin.
- By default the submenu will use its parent's class in F4 boot and F5 tool menu.

## 1.0.41 – 2021-04-21

- Add support for OpenWrt IMG file. Notes
- Add support for MidnightBSD 2.x release
- Add support for new GhostBSD release
- Fix a bug about source media missing when boot openEuler
- Fix a bug about source media missing when boot CentOS 8
- languages.ini update
- New image support ( total 700+ )

## 1.0.40 – 2021-04-10

- persistence support for Fedora series. Notes
- persistence support for ArchLinux series (Arch/ArchMan/ArchBang/BlackArch...). Notes
- Fixup a bug when booting special Windows/WinPE ISO file.
- Add a workaround for #815
- Support RHEL6/CentOS6 auto install
- Clear input key before show main menu. (#824)
- languages.ini update

## 1.0.39 – 2021-03-28

- Add VTOY_DEFAULT_KBD_LAYOUT option in global control plugin. Notes
- Add F7 hotkey for text mode. Notes
- Add a workaround for buggy bootloader's out-of-range access
- Support latest CentOS Stream 8 distro. (#799)
- languages.ini update
- New iso support

## 1.0.38 – 2021-03-16

- Optimization for VentoyWebDeepin.sh
- Fix a bug for image_blacklist plugin
- Add VTOY_FILE_FLT_XXX option in control plugin. Notes
- languages.ini update
- New iso support( total 650+ )

## 1.0.37 – 2021-03-06

- Add VentoyWebDeepin.sh script for Deepin/UOS. Notes
- Add VTOY_MAX_SEARCH_LEVEL option in global control plugin. Notes
- Improvement for UEFI boot compatibility.
- remove the ASSERT warning in UEFI mode when boot fail.
- use uname -m to detect architecture in shell script (PR #774)
- Change the partition configuration dialogbox layout in Ventoy2Disk.exe to fit text area. (issue #769)
- languages.ini update
- Document: Ventoy Search Configuration

## 1.0.36 – 2021-02-27

- Align the partitions with 4KB by default when install Ventoy. (improvement for performance and Legacy BIOS compatibility)
- Add a 🔒 icon to identify secure boot option in Ventoy2Disk.exe.
- Add a Show All Devices option in Ventoy2Disk.exe.
- Ventoy2Disk.exe doesn't check partition active flag anymore.
- Optimization for Ventoy2Disk.sh
- languages.ini update
- Add support for nbd device in Ventoy2Disk.sh (PR #746)

## 1.0.35 – 2021-02-08 ((Happy Spring Festival))

- Display a tip when scanning files.
- Optimization for booting TinyCore series distros.
- Fix a bug about invalid iso file size false positive in i386-pc
- Optimization for vtoyboot when secureboot is enabled.
- New iso support

## 1.0.34 – 2021-02-03

- vtoyboot-1.0.8 release. Notes
- vdiskchain-1.2 release. Notes
- Display a warning message if ventoy.json was mistakenly placed in the EFI partition.
- Display a warning message if ISO file has an invalid size.
- Fix a bug when booting vdisk file with secure boot enabled (issue #714)
- Update VentoyLiveCD from i686 to x86_64
- Optimization for boot slax distro
- Add image_blacklist option. Notes
- New iso support

## 1.0.33 – 2021-01-21

- Add support for Keyboard layout F5 Tools ---> Keyboard Layouts
- Add support for boot Linux vDisk file from other bootloaders. Notes
- Add persistence support for Kali/CloneZilla
- Fix a bug when using workaround for Legacy BIOS access limitation in GPT partition style.
- Fix a bug when using Ventoy2Disk.sh -l (PR #703)
- New iso support

## 1.0.32 – 2021-01-06

- Linux vhd/vdi/raw file now is bootable in both Legacy BIOS mode and UEFI mode. Notes
- vtoyboot-1.0.7 release. Notes
- Add support for DragonFly BSD distro
- Fix a bug when booting wifislax64-2.1-final.iso
- New iso support( total 600+ )

## 1.0.31 – 2020-12-23

- Fix a bug in Ventoy2Disk.exe for 2TB+ disk
- Fix a bug when use workaround for Legacy BIOS access limitation.
- Fix a bug about source media missing when boot rhel 8.3/CentOS 8.3
- Rebuild some x86_64 binraries with musl-libc to avoid virus false positive. (issue #660)
- Change default label from ventoy to Ventoy in Ventoy2Disk.sh (PR #656)
- New iso support

## 1.0.30 – 2020-12-12

- Expand dual mode option to multi-mode option. Notes
- Add a simple Password plugin. Notes
- Fix a bug in Ventoy2Disk.exe for 2TB+ disk (issue #614)
- Keep the Secure Boot Support option when update Ventoy. (issue #630)
- Add class property for submenu of Ventoy UEFI Utilities
- New iso support ( total 580+ )

## 1.0.29 – 2020-11-19

- Image file name now can contain space and unicode characters(Chinese/Japanese/Korean ...).
- Add Driver Update Disk (DUD) plugin. Notes
- Skip Ventoy EFI part when searching for bootx64.efi (issue #592)
- Display a warning message when booting a non-bootable WIM file
- Add -l command in Ventoy2Disk.sh to display Ventoy information in disk.

## 1.0.28 – 2020-11-14

- Add -L option in Ventoy2Disk.sh to set the label of 1st partition (default is ventoy)
- Expansion for option VTOY_DEFAULT_IMAGE (e.g. F4>Search and boot Windows ). Notes
- Persistence support for Kaspersky Rescue Disk Notes
- Prohibit the use of Ventoy in unofficial environments. Notes
- vtoyboot-1.0.5 release. Notes
- New iso support

## 1.0.27 – 2020-10-31

- New Boot Conf Replace Plugin to dynamically modify the boot options in configuration file. Notes
- Add an menu to enter Text Mode in F5 Tools ==> Screen Display Mode
- Fix issue #555 (treeview mode VTOY_DEFAULT_IMAGE ineffective in special case)
- vtoyboot-1.0.4 release. Notes
- New iso support

## 1.0.26 – 2020-10-24

- Display a warning message if syntax error detected in ventoy.json .
- Use the original order from image list plugin (if exist) in boot menu. Notes
- vtoyboot-1.0.3 release Notes
- Optimization for the tip message in Ventoy2Disk.sh

## 1.0.25 – 2020-10-21

- Add image list plugin. Notes
- Optimization for Linux vDisk boot in Legacy BIOS mode. vtoyboot-1.0.1 release Notes
- Support different themes for Legacy BIOS mode and UEFI mode. Notes
- Fix bug for VTOY_DEFAULT_IMAGE in TreeView mode when VTOY_DEFAULT_SEARCH_ROOT was set.
- New iso support

## 1.0.24 – 2020-10-17

- Disable "Pass parameter by ACPI table" feature introduced in 1.0.23 by default. It's not compatible with Windows 7/8 and will cause error.
- Fix apt mirror bug when install Debian series distros
- New iso support

## 1.0.23 – 2020-10-16

- Make VTOY_DEFAULT_IMAGE avaliable in both ListView mode and TreeView mode
- Add VTOY_TREE_VIEW_MENU_STYLE option in global control plugin
- Change the default resolution to 1024x768
- Pass ventoy runtime parameter to OS by ACPI table
- Fix issue #521 (blackarch 2020.06.01 boot fail)
- Fix issue #516 (archlinux 2020.10.01 boot fail in UEFI mode)
- Fix issue #512 (file with name .iso)
- Fix Parabola EFI booting (PR #508)
- Fix a bug when booting VentoyLiveCD iso
- New iso support

## 1.0.22 – 2020-09-27

- Change the check policy when Ventoy is running on a partition which is not created by Ventoy2Disk
- Add disk signature to Ventoy os parameter structure
- Fix bugs in Ventoy2Disk.sh for install Ventoy on NVMe disk
- Fix a bug with error message null src bitmap in grub_video_bitmap_create_scaled
- Add VTOY_SORT_CASE_SENSITIVE in global control plugin
- Optimization for boot Manjaro series distros
- New iso support

## 1.0.21 – 2020-09-12

- Add Ventoy LiveCD package(Not ISO version of Ventoy, just used to install Ventoy). Notes
- Add auto memdisk plugin. Notes
- Change F5 Debug to F5 Tools and add a menu to set resolution
- Optimization for F4 Search and boot Windows
- Optimization for boot atrix and archlinux series distros
- Fix a bug when boot Debian series distros with preseed configuration. issue #456
- Ventoy2Disk.exe doesn't check partition active flag anymore
- New iso support

## 1.0.20 – 2020-08-30

- Fixed a bug about booting Debian i386 netinstall.iso
- Change the default directory and file permissions in linux tarball issue #392
- New image support
- New iso support ( total 550+ )

## 1.0.19 – 2020-08-14

- Experimental support for booting IMG file (only two Linux distros supported now)
- Boot menu over serial supported, see Notes
- Optimization for booting Solus distro
- Optimization for booting .efi file
- Fixed a bug about booting Debian-10.5.0
- Fixed a bug about install Ventoy to a 2TB+ disk, issue #387
- New image support
- New iso support

## 1.0.18 – 2020-08-01

- Optimization for booting Tails distro
- Ignore the 0xEF partition type when checking local version
- New ISO support ( total 450+ )

## 1.0.17 – 2020-07-25 ((bugfix release))

- Fixed a bug about injection plugin in GPT partition style or MBR style with reserved space.
- Fixed a bug about update operation in GPT partition style.

## 1.0.16 – 2020-07-23

- Add injection plugin , see Notes
- Add menu extension plugin , you can define your own grub2 menu now, see Notes
- Fixed a bug about booting Qubes in UEFI mode.
- List all the drive letters belong to the disk in Ventoy2Disk's device combox.
- Add an example of ventoy.json and theme in the install package
- Add a DistroWatch support list in the website. See DistroWatch Support List
- New iso support ( total 420+ )

## 1.0.15 – 2020-07-09

- Add a Refresh button in Ventoy2Disk.exe
- Add a Clear Ventoy option in Ventoy2Disk.exe
- Add dir option in menu_class plugin, see Notes
- Add dir option in menu_alias plugin, see Notes
- Add autosel option in auto_install plugin, see Notes
- Add autosel option in persistence plugin, see Notes
- Change the property of Ventoy2Disk.exe, now it's NOT always topmost
- Fixed a bug when boot Windows/WinPE/Wim in UEFI mode with another active CDROM or USB-CDROM
- Optimization and bug fix for booting Parted Magic
- Optimization for booting Debian series distros
- Fixed a bug when boot.wim is in LZMS compression format
- New iso support

## 1.0.14 – 2020-06-25

- When install Ventoy you can reserve some disk space, see Notes
- New feature to boot .efi file directly in UEFI mode. (for cases like firmware upgrade, hardware diagnosis ...)
- Auto skip Press any key to boot from CD or DVD... prompt when booting Windows/WinPE ISO files (Legacy + UEFI)
- Add Menu Class plugin to show icon in boot menu, see Notes
- Add VTOY_MENU_TIMEOUT and VTOY_DEFAULT_IMAGE options in global control plugin, see Notes
- Add fonts option in theme plugin to load customized font, see Notes
- Fixed a bug about repository group missing with RHEL6
- Add 'Search and boot Grub4dos' option in F4 Localboot menu
- New iso support ( total 300+ )

## 1.0.13 – 2020-06-14

- Add support for N in 1 type of Windows/WinPE ISO files
- Add menu alias plugin to set an alias name for the ISO file, see Notes
- Add display_mode option in theme plugin, see Notes (issue #166)
- Add F4 localboot menu to boot OS in local disk
- Add F5 debug menu to check the plugin json configuration(theme,persistence,autoinstall...) and for other debug option
- Add a workaround for Legacy BIOS access limitation, see Notes
- Optimization for UEFI boot process (for No bootfile found for UEFI error)
- Optimization for Sergei Strelec's WinPE (external tools available)
- Optimization for boot process of archlinux and distros based on it (e.g. archbang/Archman/acrhlab...)
- Optimization for boot process of Fedora
- Fix a bug about auto install and persistence configuration when VTOY_DEFAULT_SEARCH_ROOT is set
- Fix a bug about halt function in F2 power menu
- Fix a bug about F2 & F3 menu nesting
- Fix a bug about boot Kaspersky krd.iso
- Fix a bug about boot distros based on rhel7/CentOS7 with a kickstart cfg
- Fix a iPXE build error with GCC 10 (issue #201)
- Change the EFI partition label to VTOYEFI (issue #175)
- New iso support

## 1.0.12 – 2020-05-30

- Expand the configuration, now you can specify more than one auto installation scripts for one ISO file
- Add a prompt for the iso with auto installation config, you can choose whether to use the auto installation script and which one to use for this time
