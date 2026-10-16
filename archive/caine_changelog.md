# Changelog: CAINE

Quelle: https://www.caine-live.net/page6/files/category-release.html
Stand: 21.09.2026 07:47

---

## 14.0 Lightstream – 2025-03-24

CHANGELOG CAINE 14.0 "Lightstream"

Kernel 6.8.0-52

Based on Ubuntu 24.04 64BIT - UEFI Ready!

## 13.0 Warp – 2023-03-16

CHANGELOG CAINE 13.0 "WARP"

Kernel 5.15.0-67

Based on Ubuntu 22.04 64BIT - UEFI Ready!

CAINE 13.0 can boot on Uefi/Uefi/Legacy Bios/Bios.

If secureboot failed, try to disable it from UEFI.

If you want to create an hybrid image, try this:
isohybrid -u caine11.0.iso

The important news is CAINE 13.0 blocks all the block devices (e.g. /dev/sda), in Read-Only mode. You can use a tool with a GUI named Unblock present on CAINE's Desktop.

This new write-blocking method assures all disks are really preserved from accidentally writing operations, because they are locked in Read-Only mode.

If you need to write a disk, you can unlock it with UnBlock or using "Mounter" changing the policy in writable mode.

CAINE is always more fast during the boot.

CAINE 13.0 can boot to RAM (toram).

INSTALLING CAINE: UnBlock (blockdev) put the device in WRITABLE mode -> use Ubiquity -> Choose System Install -> Choose user: CAINE password: CAINE host: CAINE -> Go!

Ubiquity is the installer.
Then after the first boot, run Grub Customizer and put RW instead of RO in the boot menu.

All devices are blocked in Read-Only mode, by default.

HOW TO INSTALL CAINE - VIDEO
-->
ADDED/CHANGED:

IMPORTANT CHANGES:

No more Autopsy and Gimp installed, for ISO size problem.

many others fixing and software updating.

------------------------------------------------

------------------------------------------------

## 12.4 Sidereal – 2021-12-10

CHANGELOG CAINE 12.4 "SIDEREAL"

ADDED/CHANGED:

CAINE 11.0 Wormhole 64bit released!

## 11.0 Wormhole – 2019-12-01

CHANGELOG CAINE 11.0 "WORMHOLE"

ADDED/CHANGED:

All devices are blocked in Read-Only mode, by default.

New tools, new OSINT, Autopsy 4.13 onboard, APFS ready,BTRFS forensic tool, NVME SSD drivers ready!

SSH server disabled by default (see Manual page for enabling it).

SCRCPY - screen your android device

Autopsy 4.13 + additional plugins by McKinnon.

X11VNC Server - to control CAINE remotely.

hashcat

NEW SCRIPTS (Forensics Tools - Analysis menu)

AutoMacTc - a forensics tool for Mac.

Bitlocker - volatility plugin

Autotimeliner - Automagically extract forensic timeline from volatile memory dumps.

Firmwalker - firmware analyzer.

CDQR - Cold Disk Quick Response tool

many others fixing and software updating.

Windows Side:

CAINE has got a Windows IR/Live forensics tools.

If you need it you can use the IR/Live forensics framework you prefer, changing the tools in your pendrive.

------------------------------------------------

CAINE 10.0 Infinity 64bit released!

09/Nov/2018 1630 (Updated 18/Dec/2018)

CAINE 10.0 Infinity released 09/11/2018 (Updated 18/Dec/2018)

CHANGELOG CAINE 10.0 "INFINITY"

ADDED/CHANGED:

New tools, new OSINT, Autopsy 4.9.1 onboard, APFS ready,BTRFS forensic tool, NVME SSD drivers ready!

SSH server disabled by default (see Manual page for enabling it).

OSINT: Carbon14, OsintSpy added.

Mobile: gMTP and ADB added.

Added: Recoll, Afro, Stegosuite,etc. etc.

many others fixing and software updating.

Windows Side:

CAINE has got a Windows IR/Live forensics tools.

If you need it you can use the IR/Live forensics framework you prefer, changing the tools in your pendrive.

Tools: Nirsoft suite + launcher, WinAudit, MWSnap, Arsenal Image Mounter, FTK Imager, Hex Editor, JpegView, Network tools, NTFS Journal viewer, Photorec & TestDisk, QuickHash, NBTempoW, USB Write Protector, VLC, Windows File Analyzer.

HibernationRecon by Arsenal Recon

------------------------------------------------

CAINE 9.0 Quantum 64bit released!

25/Oct/2017 0830

CAINE 9.0 Quantum released 25/10/2017

CHANGELOG CAINE 9.0 "Quantum"

ADDED/CHANGED in CAINE 9.0:

RegRipper, VolDiff, SafeCopy, PFF tools, pslistutil, mouseemu, NBTempoX,Osint: Infoga, The Harvester, Tinfoleak regfmount and libregf-utils installed.

many and many scripts and programs....

SSH server disabled by default (see Manual page for enabling it).

Autopsy 2.24 fixed - srch_strings changed with "GNU strings" renamed in srch_strings.

many others fixing and software updating.

Windows Side:

Windows Side with for Incident Response/Live Analysis on Windows systems.

Tools: Nirsoft suite + launcher, WinAudit, MWSnap, Arsenal Image Mounter, FTK Imager, Hex Editor, JpegView, Network tools, NTFS Journal viewer, Photorec & TestDisk, QuickHash, NBTempoW, USB Write Protector, VLC, Windows File Analyzer.

CAINE 8.0 Blazar 64bit released!

30/Oct/2016 0830

CAINE 8.0 Blazar released 30/10/2016

CHANGELOG CAINE 8.0 "Blazar"

ADDED/CHANGED in CAINE 8.0:

The important news is CAINE 8.0 blocks all the block devices (e.g. /dev/sda), in Read-Only mode. You can use a tool with a GUI named BlockON/OFF present on Caine's Desktop.

This new write-blocking method assures all disks are really preserved from accidentally writing operations, because they are locked in Read-Only mode.

If you need to write a disk, you can unlock it with BlockOn/Off or using "Mounter" changing the policy in writable mode.

IMG_MAP (image dd/raw and ewf mounter)

XAll 1.5

RecuperaBit

SQLParse

PEFrame

Yara

PDF analysis

MemDump

ADB and LibMobileDevice

Gigolo (network filesystem client)

Shrew (VPN manager)

wxHexEditor

Jeex

XRCed

PffLib

imount, vhdimount and vhdiinfo

samba

vblade

iscsitarget

hashdb

Tilda

trim disabled

many and many scripts and programs....

CAINE 7.0 DeepSpace 64bit released!

05/Nov/2015 0830

CAINE 7.0 DeepSpace released 05/11/2015

CHANGELOG CAINE 7.0 "DeepSpace"

ADDED/CHANGED in CAINE 7.0:

The important news is CAINE 7.0 blocks all the block devices (e.g. /dev/sda), in Read-Only mode. You can use a tool with a GUI named BlockON/OFF present on Caine's Desktop.

This new write-blocking method assures all disks are really preserved from accidentally writing operations, because they are locked in Read-Only mode.

If you need to write a disk, you can unlock it with BlockOn/Off or using "Mounter" changing the policy in writable mode.

fixed FMOUNT

XAll

BTCScan (Bitcoin scanner)

dmraid

okteta

x11vnc server

gvncviewer

ssh

openssh

wput

unBlock (block in RO/RW block devices)

mount-nfs

scalpel 2.1

new
peframe

damm

find_times

parse_VSS_RFC

4n6 scripts updated

quickhash updated

bleachbit

usnj

vshot

zulucrypt

ddrescue-gui

ddrescueView

dd utility

iloot

python_regparse

libmobiledevice

ifuse

ddrescueview

INDEXparse.py, Shellbags.py, evtxexport.py, extxinfo.py

NFS client.

CAINE 6.0 Dark Matter 64bit released!

06/Oct/2014 0830

CAINE 6.0 Dark Matter released 06/10/2014

CHANGELOG CAINE 6.0 "Dark Matter"

Kernel 3.13.0-36

fixed password request in polkit

fixed password request in textmode e tty

Bash bug fixed shellshock

mount policy always in ro and loop mode

fstrim disabled (enabled uncommenting the row in /etc/cron.weekly/fstrim)

autopsy patched by Maxim Suhanov

Many others tools and GUI.

CAINE 5.0 Blackhole 64bit released!

01/Jan/2014 0830

CAINE 5.0 Blackhole released 17/01/2014

CHANGELOG CAINE 5.0 "Blackhole"

Kernel 3.8.0-35

Based on Ubuntu 12.04.3 64BIT - UEFI/SECURE BOOT Ready!

Caine 5.0 on pendrive can boot on Uefi/Uefi+secure boot/Legacy Bios/Bios.

Caine 5.0 on DVD can boot on Legacy Bios/Bios.

SystemBack is the new installer.

Caine has a new logo, thanks to Mr. Nino Salvati.

CAINE LittleStar 64bit released!

27/Sep/2013 0830

CAINE LittleStar released 2.0 30/10/2013

Changelog:
resolv.conf fixed

boot-repair and grub-customizer added

Broadcom Corporation BCM4313 wireless card drivers added

Main features:

CAINE LittleStar is a parallel project to the official CAINE distro, it is a lighter version of CAINE based on Ubuntu 13.04 64 BIT, only to have a CAINE 64 bit version.

It can be useful for installing on 64 bit machines and it is taylored expecially for the acquisition (forensic copy) of devices.
Download HERE

------------------------------------------------

Release

News

CAINE 4.0 released!

18/Mar/2013 0830

Main features:

CHANGELOG CAINE 4.0 "Pulsar"

Kernel 3.2.0-38

ADDED:

LibreOffice 4.0.1

Sqliteman

Remote Filesystem Mounter

sdparm

netdiscover

Fixings:

netcat works

GHex

Windows Side:

NIRLAUNCHER with FTK Imager and Sysinternals tools and many more (NirsoftMegaReport included)

------------------------------------------------

CAINE 3.0 released!

03/Oct/2012 0830

Main features:

CHANGELOG CAINE 3.0 "Quasar"

Kernel 3.2.0-31

ADDED:

MATE 1.4

iphonebackupanalyzer

exiftool phil harvey

tcpflow

tshark

john

wireshark

firefox

vinetto

mdbtool

gdisk

LVM2

tcpdump

Mobius

QuickHash

SQLiteBrowser

FRED

docanalyzer

nerohistanalyzer

knowmetanalyzer

PEFrame

grokEVT

zenmap (nmap)

blackberry tools

IDevice tools

------------------------------------------------

CAINE 2.5.1 released!

18/11/2011 1000

Main features:

CHANGELOG CAINE 2.5.1 "SuperNova"

Kernel 2.6-32.35

ADDED:

ZFS Fuse

exFat support

Epiphany browser

new mounter

new TSK (Sleuthkit)

some fixings

New NAUTILUS SCripts

ataraw

bloom

fiwalk

xnview

NOMODESET in starting menu

xmount

sshfs

Reporting by Caine Interface fixed

xmount-gui

nbtempo

fileinfo

TSK_Gui

Raid utils e bridge utils

SMBFS

BBT.py

------------------------------------------------

Widows Side:

Wintaylor updated & upgraded

CAINE 2.5 released!

19/09/2011 1000

Main features:

CHANGELOG CAINE 2.5 "SuperNova"

Kernel 2.6-32.33

ADDED:

New NAUTILUS SCripts

ataraw

bloom

fiwalk

xnview

NOMODESET in starting menu

xmount

sshfs

Reporting by Caine Interface fixed

xmount-gui

nbtempo

fileinfo

TSK_Gui

Raid utils e bridge utils

SMBFS

BBT.py

------------------------------------------------

Widows Side:

Wintaylor updated & upgraded

CAINE 2.0 released!

14/09/2010 10:00

Main features:

WinTaylor 2.1, forensic frontend for Windows environment

CHANGELOG CAINE 2.0 "NewLight"

Kernel 2.6-32.24

ADDED:

Air 2.0.0

MountManager

Disk Utility

Storage Device Manager

SSdeep

ByteInvestigator

DMIdecode

HDSentinel

WVSummary

Read_open_Xml

Fiwalk

Bulk Extractor

Log2Timeline

Midnight Commander

SQLJuicer

CDFS 2.6.27

Nautilus Scripts

Fake Casper patch

Manual updated

------------------------------------------------

Widows Side:

Wintaylor updated & upgraded

CAINE 1.5 released!
18/11/2009 11:00

Main features:

WinTaylor 1.5, forensic frontend for Windows environment

CHANGELOG CAINE 1.5

Kernel 2.6-24.25 updated.

ADDED:

lnk_parse

lnk.sh

mork

steghide

UserAssist

dos2unix

chntpw

tkdiff

xdeview

xsteg

md5deep,foremost updated

launchers fixed

manual updated

README.txt in the bash scripts directory

Photorec and Testdisk and XSteg in the Forensics menu

Window list and Show Desktop added.

------------------------------------------------

Widows Side:

Wintaylor updated

HexEdit added

Regmon updated

FTKImager updated

Index.html fixed

Photorec

Testdisk

Nigilant32

UsbWriteProtect

CAINE 1.0 released!
29/10/2009 16:00

Main features:

WinTaylor 1.0, forensic frontend for Windows environment

Patches
Keyboard layout changer
New tools

CAINE 0.5 released!
22/02/09 11:30

Main features:
- WinTaylor, forensic frontend for Windows environment
- Html page IE-compatible to run the forensic tools in Windows
- Ntfs-3g updated to 2009.1.1 (resolve a ntfs-3g bug)
- New boot option: text mode.
- Ubuntu 8.04 packages updated
- Firefox 3.0.6
- Gtkhash, frontend for hashing files
- New reporting features: investigators and case name added
- Multi-language report: italian, english, german, french and portuguese
- Firefox starts with the list of tools and a brief utilization manual.

This site is licensed under a Creative Commons License. Theme "Bravo" from Rapidweaver | Privacy & cookies
