# Changelog: Parted Magic

Quelle: https://partedmagic.com/news/
Stand: 16.10.2026 01:13

---

## Parted Magic 26.10_3 – 2026-10

This update includes Parted Magic Secure Boot, allows Clone to duplicate more installations onto a smaller or larger disk, and makes VisParted safer when it resizes partitions containing Windows.

### Parted Magic Secure Boot

Parted Magic Secure Boot has been added. This utility will display every Secure Boot list, PK, KEK, db and dbx, as well as shim’s MOK and MOKX. It will provide the entity that issued each certificate, and the date by which each one expires. All entries can be copied into a directory. It can add Microsoft’s 2023 certificates and the latest revocation list, using Microsoft’s own signed files. As these files reside within Parted Magic, there is no need for network access. Prior to writing the revocation list, it checks Parted Magic’s boot files to ensure they are not listed. It provides the option for users to either add or remove their Machine Owner Keys via shim’s MokManager. Also included is the enrollment of your own Platform Key, KEK and db key within Setup Mode. Users will locate it on the Desktop and in the System menu. Included is mokutil.

### Clone 2.31

Clone has been updated to duplicate those installs it would previously refuse to clone or would simply make a bit-by-bit copy of. BitLocker remains encrypted. When cloning to a larger disk, the new space is placed immediately after C:. However, if the disk uses GPT and the target disk is smaller than the source disk, Clone will calculate how much you should reduce the size of C: in Windows first. Clone will resize your non-encrypted LVM Linux installs, and your LUKS-encrypted ones once you have entered your passphrase. The cloned install retains the same encryption key. Clone can now shrink ext4 partitions that it previously could not read.

In previous versions of Clone, any Windows install that had been powered down with Fast Startup enabled or was in Hibernation mode was resized while in one of those states. Now, Clone will leave C: at its current size and, when cloning to a smaller disk, will prompt you to restart Windows before continuing. A resized NTFS copy will be clean again, so Windows can extend or shrink C: right away. On an MBR disk, Clone will now allow you to grow and move C:, and Clone adjusts Windows’ boot and recovery configuration accordingly.

### VisParted

When VisParted reduces the size of Windows’ C:, it now allocates enough space for Windows Reserved Storage (which is required for Windows to successfully start). If you request a smaller size, VisParted identifies the DISM command that turns off reserved storage.

I discovered a bug in ntfsresize where it could potentially place part of a file outside of an NTFS partition that has been reduced in size. Parted Magic’s version of ntfsresize has been corrected to fix this issue, and VisParted now verifies all NTFS reductions in size. If the check fails, VisParted will stop reducing the partition size before completing the operation.

An NTFS volume resized by VisParted is no longer marked dirty. Therefore, Windows does not require a scan to perform Extend Volume, nor does Windows deny the request to extend a volume based upon being dirty. The minimum NTFS size now allocates at least 1 MiB of unused space, allowing Windows to mount the volume. Warning messages have been added for deleting Windows 11’s Microsoft reserved partition, since deleting this partition prevents Windows 11 from booting. An interrupted JFS grow, and an NTFS reduction in size that was interrupted while close to completion, will complete as soon as you resume.

### Erase

Erase has changed so that the scroll bar on the drive list is always visible. Thus, identifying drives that appear below the bottom edge of the window is easier. Spinning the mouse wheel above a method menu now scrolls the list rather than changing the method.

### Plain language

All messages, help screens and manuals in Erase, Clone, VisParted, Rescue, PSID Unlocker, Disk Verifier, Drive Grader, ATA Security Disable, Wipe Free Space and the Erase menu are now written using plain language. The warning that every revert erases your data has been removed from PSID Unlocker, since a drive whose locking was never turned on keeps its data.

## Parted Magic 26.10_2 – 2026-10

In this point release, Erase will examine SSDs more closely; Disk Verifier will track all drives based upon their unique serial numbers; and network booting via NFS and SSH login will function automatically.

### Erase

When an SSD’s Enhanced Secure Erase fills the drive, Erase will require that fill on every sector. Thus if a fill was interrupted before completion it would be reported as Erase Incomplete and the location of remaining data would be identified. If an SSD performs a cryptographic erase instead, then the readability of its sectors will be verified. The certificate will identify whether the drive filled its sectors or performed a cryptographic erase.

### Disk Verifier 1.3

In the log, drives are named using both model and serial number. The new Uniform Fill mode will accept any vendor specified wipe pattern (for example, Seagate uses a 33 cc 55 aa pattern), fail anything else and indicate the wipe pattern detected.

### PM Report Server

Any time that a session has a drive that did not pass, it will be shown in red. Each individual drive’s results are displayed on its own row, showing that particular drive’s results.

### VisParted

NTFS partitions will take their backup boot sector along when moved or copied. Device Info displays how much smaller a filesystem is compared to its associated partition, and a long list of findings scrolls, thus keeping the same window size.

### Network boot and SSH

NFS-based PXE booting functions correctly; the sample PXE menu in the ISO includes pre-built HTTP, TFTP and NFS entries. An additional file called pm2pxe.sh enables you to simply copy necessary files needed by a PXE server and create its menu. You may also SSH into Parted Magic while it is running with the password partedmagic, as partedmagic or root.

## Parted Magic 26.10 – 2026-10

The October version. Parted Magic Rescue takes over from TestDisk and PhotoRec; VisParted 2.3 reads and writes ten partition table formats and formats nine more filesystems; and Erase can overwrite a drive whose own erase command you would rather not rely on.

### Parted Magic Rescue

Parted Magic Rescue has taken over from both TestDisk and PhotoRec. It will recover deleted files from NTFS, exFAT, FAT and ext2/ext3/ext4 filesystems with actual file name, folder name and timestamp information. This software also carves out what the filesystem no longer remembers. Finally, this program finds lost partitions on a disk, and VisParted puts them back in the partition table. It never writes anything to the drive it is recovering from. Once a BitLocker or LUKS encrypted volume has been unlocked, it may be read as well. It operates within a window, through the Terminal and from the command line.

After every recovery, there is a full report of what was recovered and what was unable to be recovered. The report may be sent directly to the PM Report Server, where it is given its own web page. When reading a failing drive, Rescue only reads each bad area once. Therefore, when a file spans one of these areas, it will come back labeled “partial”.

### VisParted 2.3

Besides GPT and MBR, VisParted now reads and writes BSD disklabel, Sun VTOC, SGI volume header, Apple partition map, PC-98, Amiga RDB and Atari AHDI format partition tables, as well as a disk with no partition table at all (i.e., an unpartitioned disk). It also formats F2FS, JFS, NILFS2, ReiserFS, Reiser4, HFS, HFS+, UDF and MINIX. Further, if LUKS volumes are available on a disk, they may be resized. If LVM physical volumes are available on a disk, they too may be resized. Also, ext3, ext4, Btrfs, XFS, JFS and NILFS2 filesystems that have already been mounted may be grown in size; similarly, Btrfs and NILFS2 filesystems that have already been mounted may be shrunk in size. A copy of a partition may be written over an existing partition. Extended partitions may be resized and moved based upon their borders. Partitions on GPT and MBR disks may be aligned to MiB boundaries, cylinder boundaries or any sector. Software RAID arrays are listed in the device list and may be partitioned exactly like any other disk.

VisParted will also repair boot sectors; a damaged NTFS, exFAT or FAT32 boot sector will be replaced with its backup copy; NTFS MFT records will be retrieved from their mirror; and a lost NTFS or FAT boot sector can be reconstructed based on what was found by searching the partition. BitLocker partitions are identified, including the encryption method used for each one and how each one unlocks.

### Erase

The option to switch to Block Wipe exists for drives that have a firmware erase, thus allowing a drive whose own erase command may be untrustworthy to be overwritten end to end. This can be done using the Block Wipe box on the drive’s card, the m key in the terminal, or using --block-wipe and pmerase_blockwipe= for unattended runs. The certificate will clearly identify the method used and certify it Clear.

eMMC storage which supports Sanitize can now be erased using Erase and then Sanitize. This is the recommended method stated in the eMMC 5.1 standard and will also be certified Clear.

Both Save & Close and email now carry logs for every single drive along with its certificate. This allows users to check the log hash printed on the certificate against the saved log. If logs are stored on a USB stick or network share, they no longer receive the warning that they only exist in memory. The tooltip window for every single drive’s card lists all of that drive’s partitions. If a drive was dropped prior to completion during a run it will have its pass recorded along with how far through the process the drive got.

### Clone

Clone names BitLocker volumes as “BitLocker” within its plan, certificate and device list. When cloning to a disk larger than the source disk, Clone grows the largest partition into the available space of the destination disk (on an MBR disk, when it is the last primary partition). A small boot or recovery partition will keep its original size. The window fits a 1280×800 screen with the panel showing.

### Mount

Volume labels are displayed exactly as they were written (i.e., all capitalization, spaces and accented letters). When Lock fails to close a BitLocker or LUKS volume, it will display the reason why it failed: where the volume is still mounted; what other device is built upon this volume; or which application is currently using the volume.

### PM Report Server

The report server keeps each of Parted Magic Rescue’s reports on its own page, with the data that was found but not recovered first, followed by the recovered data. Unattended runs that refused their policy, runs that were aborted from the console and destruction certificates are now reported as Refused, Aborted and Destruction. Alerts from these runs say what happened.

### Smaller things

Every window of every Parted Magic utility displays its own icon in both the title bar and the window list. The screen also does not blank or go to sleep during periods of inactivity. The text mode menu also includes options for running Parted Magic Rescue and VisParted.

## Parted Magic 26.09_5 – 2026-09

A point release. Erase takes on more drives and confirms every result with the drive itself, File Viewer can search and copy text, and a round of Slackware security updates is in.

### Erase

On laptops whose firmware blocks a self-encrypting drive’s security commands at power-on (TCG Block SID, which many ThinkPads set), Erase can now ask the firmware to lift the block at the next start, where the firmware supports it. It is one button on the confirmation screen, or the o key in the terminal. After the restart the drive gets its cryptographic erase, a Purge in seconds, and the results screen can put the block back.

Erase now reads each drive’s own answer to every command it sends. A drive that turns an erase down is shown as refused, with the drive’s reason written on the record, and Erase moves on to the next method that can erase it.

SAS and SCSI drives complete their Sanitize as Purge in the window, the terminal and unattended mode alike, and Erase confirms the outcome with the drive before it certifies. SATA drives formatted with 520-byte sectors, the way storage arrays leave them, are erased by their own firmware and verified in their own sector size, which Linux itself cannot read.

Certificates name the method itself, such as NVMe Format User Data Erase or ATA Secure Erase, and the media type in full, and a drive that reads back as its own repeating fill pattern has that pattern named. The terminal and unattended mode show verification progress drive by drive, the window fits a 1024×768 console screen, an NVMe drive’s brief temperature warning is reported as heat rather than as a failing drive, and setting the clock from Erase keeps it right across a restart.

### File Viewer 0.2

Find (Ctrl+F) searches PDFs, text and log files, Word and OpenDocument documents, RTF, PowerPoint and spreadsheets. In a PDF you can now select and copy text, and open a password-protected file. Spreadsheets keep their currency symbols and negative-number formats, and Word tables show every cell in full.

### Time Config

Time Config sets the hardware clock the way the next boot reads it, so the time stays right after a restart and in Windows. Behind a router that blocks the NTP port it gets the time from partedmagic.com over HTTPS instead, and every time it shows carries its zone.

### Clone

A whole disk copied onto a smaller one keeps its EFI system partition and Windows recovery partition at full size while the other partitions share the difference, and the plan and the certificate name every partition that was resized. An NTFS volume shrunk or grown in flight keeps its backup boot sector on the partition’s last sector, where Windows and the repair tools look for it.

### TestDisk

Recovering lost partitions on a GPT disk keeps the disk GPT, so every partition of a UEFI Windows disk can be put back. Stop ends a scan at once.

### Hex Editor

Whole drives open with their bytes on screen, an unreadable sector shows as ?? in red and the editor carries on, and Find, Go To and Replace all open. A long search runs while the window stays responsive, and Stop ends it.

### Mount and File Manager

A filesystem made or repaired on an existing partition, by TestDisk, mkfs or a format, shows up in Mount straight away. In the file manager the status bar follows the selection and counts folders, and folder sizes stay within their own filesystem.

### Smaller things

Save Session stamps each session with the release it was saved on, so booting it on a different release warns you, as the manual describes. Keyboard Layout gets the right layout for about fifty more keymaps, Dvorak, Croatian, Korean and Serbian among them. The ddrescue window groups its counts with commas and keeps its output scrolling, Drive Grader jumps to a drive’s result on the first click, VisParted names partitions the same way before and after a plan, and the Erase menu describes each tool as it is today.

### Updated packages

54 packages updated from Slackware -current, with security updates to Firefox (153.4.0esr), expat, PCRE2, util-linux and groff. Among the rest are parted 3.8, which now recognizes exFAT, nvme-cli 3.1, Samba 4.25.0, rsync 3.5.1 and ntfs-3g 2026.9.28.

## Parted Magic 26.09_4 – 2026-09

A point release, and the headline is ThinkPads.

### ThinkPads, erased where they sit

For close to ten years, erasing the SSD in many Lenovo ThinkPads has meant changing a BIOS setting, finding the PSID printed on the drive’s label, or taking the drive out and erasing it in another machine, because the drive refuses the erase command it is supposed to obey.

Parted Magic Erase now does it in the laptop. When a self-encrypting drive refuses its erase command, Erase takes ownership of the drive’s encryption and resets it, which throws away the key everything on the drive was written with. That is a NIST Purge, it takes less than a second, and the certificate records it as TCG Opal Cryptographic Erase. --no-tcg-revert turns it off.

On a ThinkPad T480s whose drive refused its erase command even with the BIOS lock switched off, the whole drive was erased this way without a BIOS change, a PSID or a second computer. A search of every sector afterwards found none of the data written to it before.

### More in Secure Erase

Drives with a Host Protected Area are erased directly, because their own Sanitize and Secure Erase cover the hidden sectors too. A drive left locked by an interrupted erase is listed and erased with no separate unlock step, and a locked self-encrypting drive tries the same password before asking for its PSID.

Verification after a block erase accepts both erased states, zeros and 0xFF, and a Sanitize that is still making progress is waited for however long it takes. Parted Magic Erase clears any partition table left at either end of a drive after its firmware erase, so an erased drive shows up blank. A SCSI Format Unit shows its progress, and durations and speeds stay right if the clock is changed during a run.

The results screen and the certificate name the method that actually erased each drive, a successful erase is shown without notes, and the full sequence is in the Advanced log. A drive whose erase did not succeed certifies as Not completed. Each drive now gets its own CSV log beside its other logs and its certificate.

Unattended mode runs without a report server, keeping the evidence on the machine and staying powered on when that copy is only in RAM, and it wakes frozen drives with a short sleep, the way the Sleep button does. A drive plugged in after a copy-to-RAM boot is no longer mistaken for the boot stick.

### Disk Verifier

A drive with a Host Protected Area passes, with the number of hidden sectors stated in the result.

### Updated packages

TigerVNC 1.16.2, up from 1.12.0, and the CPU frequency panel plugin 1.2.9.

## Parted Magic 26.09_3 – 2026-09

A point release: Erase does more, the boot is quicker, and VLC works again.

### Secure Erase

A verification mismatch now reads Erase Incomplete instead of Erase Failed, the certificate no longer claims Purge when the sanitization did not complete, and the record says where the surviving data is. On the drives that led to this change, it is the very last sector, because of a fault in their firmware. A drive whose firmware refuses its own hardware erase is now overwritten instead of just failing, and the certificate records it as Clear, the level an overwrite reaches.

A drive that stops responding can be dropped, so the rest of the batch finishes and every other drive still gets its log and certificate. A SCSI Sanitize that never reports completion is no longer waited on forever. With dozens of drives selected, the window no longer grows wider than the screen. Erase also asks each drive whether the BIOS has blocked its security commands, which is common on business laptops, and tells you before you start instead of after.

If the PM Report Server is unreachable, the screen says so and the evidence is kept rather than lost; erase --report-sync sends it once the server is back.

### Clone and VisParted

All three programs now share one report server setting, so you enter it once. Clone hid that field unless a server was already configured, which is exactly the machine where you need to type one in, and its terminal version had no way to set one at all.

### VLC

VLC refused to start, saying it would not run as root. It is rebuilt with the option that allows it, so it plays again. It is in Parted Magic to check recovered video files.

### A quicker boot

Services that do not have to finish before the desktop appears now start together instead of one after another. A three second wait and a hardware database rebuild, which the image repeated on every boot, are now done once, when the image is built.

### Updated packages

68 packages updated from Slackware -current, among them Firefox 153.3.0esr, Mesa, FFmpeg and glibc.

## Parted Magic 26.09_2 – 2026-09

A point release: five programs fixed.

### Erase

The certificate called a healthy drive damaged whenever verification mismatched, because Operational/Damaged was taken from the erase result instead of the drive’s own SMART. The two are now independent fields. Four smaller things with it: --technician-title prints on the certificate, timestamps carry their UTC offset, the log hash is SHA-256 instead of MD5, and asking for a sanitize method the drive does not advertise now says so instead of quietly using a different one.

### Boot sector repair

Repairing a boot sector did nothing at all on GPT disks, which modern Windows uses, and the damaged partition was not even offered when its boot sector was the broken part. Both are fixed. NTFS, exFAT and FAT32 now recover from their backup copy.

### ddrescue

It would let you recover a partition onto the disk that contains it, or image a drive to a file on that same drive, and report success while destroying what you were rescuing. Both are refused now, and the boot medium is no longer offered as a destination.

### Package Manager

It was pointed at the Slackware 15.0 repository while the image is built on -current, so anything it installed was years too old to run. It now uses -current, and the Parted Magic packages are protected from being replaced by stock ones.

### Virus scanner

Quarantine moved files off your drive with no confirmation, and the quarantine folder lives in RAM, so a large file could disappear at the next reboot. It now asks first and tells you where the files are going.

## Parted Magic 26.09_1 – 2026-09

A point release: four fixes and one new program.

### If you use my USB installer

The installer inside 26.09 refuses this ISO with “expected exactly one pmagic/pmodules/PMAGIC_*.SQFS, found 0”. It could not read the _1 on a point release. Use the installer from this ISO instead. The install/ folder is at the top of the ISO and opens in Windows Explorer, with 7-Zip, or by mounting the ISO on Linux. You do not need a working stick to get it.

### Clone

Clone refused to write an image to a Samba or NFS share, saying the share was in RAM. Shares are now recognized as storage on another machine and accepted for images, journals and saved plans.

Clone also refused to copy a partition between a 512-byte-sector drive and a 4K native drive. ext2, ext3, ext4 and btrfs partitions now copy across that boundary. NTFS, FAT, exFAT and XFS partitions are still refused, as is any whole-disk copy.

### Mount

Adding a Samba share with the wrong password could freeze the window. A retry ran a bare mount command with no credentials, and that waits forever for a password prompt that is not there. Fixed.

### Servers with no video

On servers with Matrox G200 or ASPEED BMC graphics, X picked the old chipset driver, which refuses to run beside the kernel’s own driver, and the display died at handover. X now uses modesetting on those chips, as other distributions do. Old Matrox cards (Millennium, G400, G450, G550) are unaffected.

### Serial console

New Failsafe entry, “Serial console – no video needed”: no graphical desktop, and a login on the first serial port at 115200. For servers reached over iDRAC, iLO or IPMI serial-over-LAN. Edit the entry for a different port or speed.

### Btrfs Assistant

New, because a user asked for it. Subvolumes, snapshots, balance and scrub, and snapper integration for browsing snapshots and restoring files out of them. It can roll a subvolume back to a snapshot, which is the reason to run it from a live disc. In the menu under System.

### Removed

“Force vesa workaround” and “Force refresh rate” are gone from the Failsafe menus. Both set a boot option that copies a file the image does not contain, so neither ever did anything.

## Parted Magic 26.09 – 2026-09

There is a new disk cloner in this release. Wipe Free Space has been rewritten and no longer depends on an outside tool. Every other program I write has been read line by line and then run against real drives on a bench machine kept for that purpose, and the bugs that came out of it are fixed. Underneath all of that the base system has been rebuilt on Slackware-current, the desktop moved from Xfce 4.16 to Xfce 4.20, and the wallpaper changed for the first time in over ten years.

The release is named differently too, and it is signed. Both are explained at the end.

### Clone

Parted Magic Clone is new. It copies a disk, a partition, or an image of either, and it produces evidence that the copy is right.

The source is never written. Clone opens it read-only, and every change, whether that is filling in a later slice, repairing a filesystem, growing it to fill a larger disk or repointing a boot loader, is made to the copy, after the copy has been read back and verified.

Clone is not a rescue tool. Reads that keep failing mean the drive needs rescuing, and Clone says so and stops. ddrescue is the tool for that job.

Clone reads the allocation state out of the filesystem itself: FAT12/16/32, exFAT and NTFS cluster maps, ext2/3/4 block bitmaps, XFS, and the partition table with its logical chain. Every map is checked against that filesystem’s own counters before it is used. A map that disagrees by a single block is thrown away and the region is copied in full instead, with the reason printed in the plan. Btrfs is always copied whole, because two different maps for it turned out to be wrong in real use.

Free space inside a filesystem is not copied. Neither is unpartitioned space, beyond what has to be. The table, the first 64 MiB ahead of the first partition where boot loaders live, gaps up to 16 MiB, the last megabyte of the disk and any partition Clone does not recognize are all copied verbatim. Larger gaps are skipped, and both the plan and the certificate state how much was skipped. When byte-for-byte is what you want, --full-range, or the “copy every byte” box in the window, gives you that.

Clonezilla works the same way. On my own test disks, 198 of the 235 GiB being moved for one image was unpartitioned space. The same job now moves 37.94 GiB.

Images are raw: the bytes of the device exactly as they are, sparse where nothing was copied. There is no header or container format, so an image never needs converting. Compression is on by default and changes none of that: a compressed image is an ordinary zstd file, and zstdcat name.img.zst | dd of=/dev/sdX restores it on any machine with that machine’s own tools. On FAT32, where a file cannot reach 4 GiB, the image is written in numbered parts, each one a valid source on its own.

Reading a compressed image used to mean decompressing it. The frame table lives in the certificate beside the image, and if that certificate had been lost the table was rebuilt by one pass over the whole file. On a 235 GiB image that was 22 minutes, and the free space to hold the result, in order to produce a listing. The table now also rides inside the image, in a frame that zstdcat ignores, written as soon as the copy finishes. Images made by older versions still read the old way.

Chunks that nothing lands in are no longer built, hashed or compressed, and the read-back takes the known digest for them instead of reading them again. With the gap rule above, one image job on the bench went from 1,972 seconds to 965, and its verification pass from 943 seconds to 15.

Onto a smaller disk the table is regenerated, the largest shrinkable partition gives up the difference, and on GPT the partitions after it move inward. Onto a bigger one the largest growable partition takes the difference and the rest move out of its way. FAT, exFAT, NTFS and ext filesystems are shrunk or grown in flight: the whole change is computed against the read-only source, and the resized filesystem is streamed to the destination. Clone refuses a dirty or damaged volume and says why.

The journal is built to survive a power cut on the boot stick. Every file is sized once and written in place, the log is append-only and fsynced, and the digest goes down before the data it describes. resume picks the job up where it stopped.

Where a sector will not read, Clone salvages around it, and the damage report names what each zero-filled range landed in, by file and by directory, so you know which files were hit.

Every job ends with a read-back and a sealed certificate carrying both devices’ identities, per-chunk digests, a Merkle root, the map of anything unreadable and the timings. verify checks that a certificate is intact at any time; verify --deep re-reads the media behind it. Certificates can be sent to the PM Report Server.

Clone runs in a GTK window that looks like VisParted’s, in a full-screen terminal interface for a machine with no graphics, and from a command line with probe, plan, clone, apply, resume, verify, damage and report. All three use the same code and show the same messages.

Before release it was run in the window, the terminal and the command line against five real drives: nine partition copies, a whole disk to a compressed image and back onto a larger disk twice, a larger disk onto a smaller one with 194 GiB of gaps closed and fifteen partitions moved inward, an interrupt and resume, image sources and destinations, split sets, saved plans, and read-error salvage through a deliberately broken sector range. Every copy came back fsck-clean, every file comparison was identical, and every verify --deep passed. Twenty-three certificates were countersigned by the report server. Fifteen bugs were found during that run and fixed before this release.

### Erase

Erase works by issuing the drive’s own hardware erase command rather than overwriting from software, so remapped sectors and areas the operating system cannot reach are covered too. It picks from nine paths per drive, automatically: ATA Sanitize, ATA Secure Erase and Enhanced Secure Erase, NVMe Sanitize and NVMe Format, SCSI Sanitize and SCSI Format Unit, eMMC/SD hardware erase, and a software block wipe where a drive has none of them. Where a drive advertises more than one variant you can pick which one is issued, because the final state of the media differs between them.

Every log and every certificate now carries a Verification Result line: how many bytes were actually read back off the medium, how the samples were spread across it, which check was applied, what anomalies were found, how long it took and at what rate. The certificate is still one page.

The rest of the changes came out of the bench.

The boot stick could be offered for erasure. After a copy-to-RAM boot the medium is unmounted, and the check that protects it only knew about mounts and swap, so the stick you booted from was invisible to it. It is now identified from the device the system actually booted from.

The certificate’s note about a Host Protected Area described the kernel’s view of the drive from before the erase started, not what the verification had covered. It now states the drive’s native sector count and what the read-back actually reached.

The identity in the log header came from dmidecode at the time the log was written. One of my test machines corrupts a byte of its own SMBIOS manufacturer string after a suspend, which meant a certificate could carry a mangled machine name. Erase now takes that from the copy the kernel made at boot.

An empty card reader was offered as a zero-byte wipe target. A completed normal run left its result files behind, so the next launch reported the previous one as having ended abnormally. The terminal interface lost its drive selection when a drive was frozen at startup.

The read-back check after a firmware Secure Erase still runs: it samples the media after the drive’s firmware reports success and fails the drive if recognizable data survived. It applies to hard disks only. SSDs are left out because a cryptographic erase leaves random-looking data behind, and that is the expected result.

Five full erase runs were done across SSD, NVMe and spinning disks, each by that drive’s own native method, including a 6 hour 28 minute Secure Erase on a drive with 3,975 reallocated sectors followed by a 6 hour 15 minute verification. A 4 TB SAS drive took 12 hours 43 minutes for a Format Unit and 45 minutes to verify. Every run ended in a signed certificate.

### VisParted

The partition editor. Twelve changes, nearly all of them bugs found by using it on real disks.

--resize --size max used to mean something ambiguous. It now means the largest size the partition can reach where it sits. Asking for more than that is refused and names --expand, which is the verb that relocates neighbors to make room. The dialogs show both figures so the difference is in front of you.

An NTFS volume could only be resized once per Windows boot. VisParted’s own resize set the volume’s dirty flag, and the next plan then refused to touch it and suggested a fix that could not clear that flag.

A grow that fit inside the partition’s own gap moved the next partition anyway. Relocate-end produced an overlapping layout when the end of the disk was occupied. A newly created extended container lost its EBR to the ghost wipe, after which the reader blocked every plan on that disk. Format could run before the new partition’s device node existed. resume could not find a journal in a directory the operator had chosen, and it wrote before checking that the disk had not changed since the interruption. --set-type refused the linux and windows aliases that --type already accepted.

It was tested across all five bench drives: every filesystem it creates, the native FAT16, FAT32 and exFAT resizers in both directions with seeded data, tool resizes, overlapping moves, same-disk and cross-disk copies, shred, delete, GPT to MBR and back with logical partitions, spec mode, resume from every state, and the same work again through the terminal interface and the window. Every data check passed.

### Wipe Free Space

Rewritten. The old version was a window around an outside program. It did one filesystem per run and broke the ext3/ext4 journal every time, which then had to be repaired. Version 2.0 does the work itself and no longer uses that program at all.

It is for one job: you delete your files, then you sell the computer, and what you deleted cannot be brought back, while the computer still boots. It does not empty the Recycle Bin, so do that first.

It fills the free space through the mounted volume with zeros or random data, one to three passes, and then runs a small-file phase that reaches the gaps between your existing files, which a plain fill cannot get into. On SSDs it runs fstrim afterwards. Then, per filesystem: NTFS gets its unused MFT records, directory indexes, $LogFile, file tails and page file wiped with ntfswipe; ext3 and ext4 have their journal set aside before the fill and re-created after, with a directory optimization pass; FAT and exFAT have deleted directory slots overwritten with dummy entries, so the names go too. XFS and btrfs get free space and TRIM only, and the results screen says plainly that file names may remain on them.

There is a headless --auto DEVICE mode for scripting, and the four-step wizard is otherwise unchanged.

It was tested on twelve 8 GiB volumes, NTFS, ext4, btrfs, XFS, FAT32 and exFAT on both an SSD and a hard disk, each seeded with 30 files kept and 30 files deleted, then searched raw. Deleted file contents went from 30 found to 0 on every filesystem. Deleted file names were gone on NTFS, ext4, FAT and exFAT. ntfsundelete and extundelete recover nothing. Kept files were intact, journals were back, and nothing was left mounted.

One problem had been defeating the old version. ext4 holds back a reserve that even root cannot write into. After a fill that reported itself complete, 29 of 30 deleted files were still readable in the gaps between the kept ones. That reserve is now released for the duration of the fill and restored afterwards. XFS has the same kind of reserve and is handled the same way.

Wipe Free Space needs ntfswipe, so this release also carries a rebuilt ntfs-3g that includes it.

### Disk Verifier

The read-only checker that tests whether a drive reads back as all zeros, all ones, or just readable. It is what the erase menu offers after an erase.

Sectors hidden behind a Host Protected Area or a Device Configuration Overlay passed silently. The verifier reported a clean drive while never having seen part of it. It now notes the hidden region in the log and fails the drive with a “hidden” result and the count of sectors it could not reach.

--auto crashed without an X display, which made it useless for the scripting it was made for. There is now a headless mode with progress on the terminal and Ctrl-C as Cancel, and it scans the same way as the window.

An empty card reader was offered as a zero-byte disk. The boot medium now carries a badge. Step 3 has Select All and Clear. Reads no longer push everything else out of the page cache.

### Drive Grader

Several of the numbers the grades were based on were wrong, and each one changed a grade.

SSD wear was picked by SMART attribute ID alone, so a WD Green was being graded on attribute 233, its count of NAND gigabytes written, instead of its actual wear indicator at 230. The ID list is now a preference order, and an attribute only counts as wear if the drive database describes it as wear, life or endurance.

SMART 188 was read as a packed raw value. A Seagate reporting two command timeouts came through as 4,295,032,834 and graded F. Only the low 16 bits are read now. Power-on hours had the same problem, which is how one drive came to report 2.5 trillion hours.

A drive’s own SMART self-assessment was ignored entirely. A drive that says FAILED in as many words could still be graded on its attributes alone. That verdict is now the first row of the report.

SAS and SCSI drives graded “?” in every column. There is now a SCSI path reading health status, grown defects and uncorrected read and write errors, confirmed against a real 4 TB SAS drive. Surface-scan counts are in 4 KiB blocks and now say so.

### ATA Security Disable

This is the recovery tool for an interrupted Secure Erase, which leaves the drive with a password set on it.

A drive that had been locked came back at 0 bytes after being unlocked. The rescan re-reads the kernel’s cached identify data, which still described the locked drive, so the size never updated. The tool now deletes the SCSI device and rescans its host when the size is still zero, and reports what the kernel is saying.

A refused password showed hdparm’s raw SG_IO sense bytes. It is now translated into words: the password was not accepted, or the retry counter has expired. The log header comes from the kernel’s copy of the machine identity for the same reason as Erase. The manual and the on-screen help for a frozen drive now cover the drive-password prompt some BIOSes show at power-on.

It was tested on a real drive taken through the whole sequence: password set, locked, retry lockout, security level maximum with a master password, and then recovered.

### PSID Unlocker

If you rely on PSID revert, read this.

A PSID revert does not necessarily erase your data. On a self-encrypting drive that was never taken into ownership, which is the normal state of most drives people are holding, the revert can report revertTper completed successfully and leave the partition table, the filesystem and every file exactly where they were. I reproduced this on a Samsung 980: a GPT, an ext4 filesystem and 636 files all survived. Only with the Locking SP active did the revert regenerate the key.

The tool now samples the media before and after the revert, and when the data survived it says so: “Reverted, data NOT erased”, in amber, in a banner and in the log, and it points you at the Erase suite. Success is confirmed by querying the drive afterwards rather than by trusting the command’s exit status, and the kernel’s cached partition table is flushed and re-read. The manual has a new section titled with the question directly.

### Mount and File Manager

Thirteen fixes across the mount window and the file manager, most of them around encrypted and LVM volumes.

LUKS and BitLocker volumes offered Mount, which failed with “unknown filesystem type”, and an unlocked volume then disappeared from the list. Those cards now have locked, unlocked and mounted states, with Unlock, Mount, Lock and Unmount-and-lock as appropriate. Unlock LUKS found nothing at all, because the background daemon had already written every LUKS partition into fstab and the dialog was excluding fstab devices.

LVM logical volumes were never listed. Neither were whole-disk filesystems: a drive formatted with no partition table at all, the way most USB sticks and camera cards arrive. Mounts that fstab did not know about had no card at all. All three are listed now.

A wiped partition kept its old fstab entry indefinitely. A previous entry is now kept only while the device cannot be read.

The live boot medium could be unmounted or ejected. It is marked as the boot medium and protected. Erase and Clone were missing from the guard that stops a volume being mounted out from under a running disk tool.

In the file manager, the sidebar showed fstab only and now reads actual mounts as well. A LUKS row ran mount on the encrypted device; it carries a lock icon now and opens the unlock dialog. Copying a file larger than 4 GB onto FAT32 returned “[Errno 27] File too large” with no explanation, and now gets one.

### The wallpaper

The desktop wallpaper has changed for the first time in over ten years.

The old one was built for 1920×1200 screens: a two-tone blue split with a damask pattern down the right side, a line-art circuit board, and the logo with the “partition | clone | rescue” tagline beneath it.

The new one is 3840×2160 and much quieter. A deep navy field, light coming across the lower left, faint circuit traces at the edges, and a large, softly drawn disc platter in the upper right. The gold corners are still there. The wordmark sits along the bottom center, where a desktop full of icons will not sit on top of it. It scales down to 1080p cleanly.

### The base system

Parted Magic is no longer built on Slackware 15.0. It is built on Slackware-current, and everything underneath moved at once. The package count went from 992 to 1082.

previous release26.09glibc2.422.44Python3.9.253.12.14OpenSSL1.1.13.5.8Xorg server1.20.1421.1.24Xwayland21.1.424.1.13Mesa26.1.826.2.2GTK 33.24.313.24.52GLib2.70.32.90.0Pango / HarfBuzz1.48.11 / 3.2.01.58.2 / 14.4.0fontconfig / FreeType2.13.92 / 2.13.32.18.3 / 2.14.3

The kernel is 7.0.0-31-generic, signed for Secure Boot as always. The NVIDIA driver is 610.57.04, up from 595.71.05. It is the open GSP-based module, so it covers Turing and later, which is the GTX 16 and RTX 20 series and everything after. Older cards fall back to nouveau on their own, with no cheat code needed.

The desktop went from Xfce 4.16 to Xfce 4.20. That is xfwm4 4.20.0, xfce4-panel 4.20.8, xfce4-session 4.20.4, xfce4-settings 4.20.5, xfdesktop 4.20.2, Thunar and tumbler 4.20.2, garcon 4.20.0, xfce4-power-manager 4.20.1, catfish 4.20.1, xfce4-terminal 1.2.0 up from 0.8.10, Mousepad 0.7.0 and Xfburn 0.7.0.

New in the image: apfs-fuse, which reads Apple APFS volumes from macOS 10.13 and later; rclone 1.75.0, now properly packaged; hfsprescue 3.6.

Updated, for disk work: exfatprogs 1.4.3 from 1.1.3, LVM2 2.03.42 from 2.03.13, cryptsetup 2.8.8, GParted 1.8.1, gptfdisk 1.0.10, f2fs-tools 1.16.0, ms-sys 2.8.0, dc3dd 7.3.1, os-prober 1.85, GRUB 2.14.

For hardware: smartmontools 7.5, hdparm 9.65, nvme-cli 2.16, pciutils 3.15.0 from 3.7.0, usbutils 019 from 014, hardinfo2 2.3.1, bluez 5.87, memtester 4.7.1.

For the network: NetworkManager 1.58.1 from 1.32.12, Samba 4.24.7 from 4.18.9, OpenSSH 10.5p1, nfs-utils 2.9.2, cifs-utils 7.7, rsync 3.5.0, curl 8.22.0, nmap 7.991, dhcpcd 10.5.2, wpa_supplicant 2.12.

For checking that recovered files actually play: FFmpeg 9.0.1 from 4.4.6, VLC 3.0.23, GStreamer 1.28.7, PipeWire 1.6.8, PulseAudio 17.0.

And the rest: Firefox 153 ESR from 140 ESR, nano 9.2 from 6.0, vim 9.2, htop 3.5.3, Midnight Commander 4.8.33, tmux 3.7c, screen 5.0.2, gvfs 1.60.2.

A few things were tidied while I was in there. The running system identifies itself as Parted Magic and the release number in /etc/os-release, /etc/issue and /etc/motd, instead of reporting itself as Slackware. Nothing listens on the network that does not need to: the system logger no longer accepts remote messages on UDP 514, the SNMP daemon no longer starts, and the mail system listens on loopback only. Outgoing mail is untouched, which is what Erase uses to send you logs and certificates. Font configuration was repaired. Dead menu entries and dangling links were swept out, along with about 100 MB of static libraries and link-time objects that exist only to compile against, on a disc that carries no compiler.

### The name

From this release the ISO is named pmagic_26.09.iso, year and month, and releases are monthly.

The old pmagic_YYYY_MM_DD form was being misread by somewhere between a third and a half of customers, who read it day first. In Germany, 2026_06_04 is the 4th of June to me and the 6th of April to them. 26.09 cannot be misread.

### Signatures

Every release is signed from now on. Beside the ISO you will find pmagic_26.09.iso.asc, a detached OpenPGP signature.

The signing key is RSA 4096, created 3 September 2026:

pub rsa4096/6C49227C1EBA24AD 2026-09-03 [SC]
F674 69C6 8A0B 8FC1 70B2 B1B5 6C49 227C 1EBA 24AD
uid Patrick Verner <sales@partedmagic.com>

Check that fingerprint against what you imported before you trust a signature it made.

Get the key from https://partedmagic.com/store/GPG-KEY, or from install/GPG-KEY inside the ISO, or from the block printed below. Then:

gpg --import GPG-KEY
gpg --verify pmagic_26.09.iso.asc pmagic_26.09.iso

-----BEGIN PGP PUBLIC KEY BLOCK-----

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
=5Fzd
-----END PGP PUBLIC KEY BLOCK-----

### Writing it to a USB stick

Parted Magic now ships its own installer for flash drives, for Windows and for Linux. I would rather not send you to Rufus, Etcher or UNetbootin for something this basic.

It is in the install/ folder on the ISO: pmusb-gui.exe and pmusb.exe for Windows, a .txz for Slackware, a .deb for Debian and Ubuntu, an .rpm for Fedora and Red Hat, and the source. Both Windows executables are signed with Parted Magic’s EV code-signing certificate and timestamped.

It writes a plain FAT32 stick that boots on legacy BIOS and on UEFI with Secure Boot enabled, verifies every file it wrote before it tells you it succeeded, and can upgrade a stick in place. On Linux it hands the drive back to your desktop cleanly when it has finished.

## August 19, 2026

The PM Report Server now has a full GUI with history. Please download pmagic_2026_06_04_17.iso from your account. The report server is in the root (top level) of the ISO image.

## August 18, 2026



## The PM Report Server

Every Parted Magic license includes the PM Report Server. If you erase more than the occasional drive, it is probably the most useful thing in the download.

Parted Magic runs entirely in RAM. That keeps the installed system safe, because Parted Magic never touches it, but it also means the logs and certificates from an erase stay in memory until you save them somewhere. If you save them to the wrong drive, lose power, or forget on the last machine of a long day, the record is gone, even though the drive was erased.

The report server fixes that by getting the evidence off the machine while the erase is still running. Copy the file pmagic_report_server from the root of the ISO to any always-on computer with Python 3 (Linux, Windows or Mac) and start it. It needs nothing else installed. Then put that machine’s address in the Report Server field before you start an erase, and every drive reports to it automatically.

What you get is a dashboard on your own network showing every session you have ever run: which machine, which drives, which method, pass or fail, updating live as drives finish. Every log and every certificate is there to download. There is a CSV of every drive across every session, which is usually the fastest way to answer “prove you erased that serial number” months later. Any session also exports as a signed evidence pack that your customer can verify offline, without an account.

It runs on your own hardware and network, and nothing is sent to us. It keeps working whether or not you still buy from us. You can watch a bench of machines from your phone while they run.

If you erase drives for other people, the report server gives you a record you can hand to an auditor. Details are on the Secure Erase page, and a real evidence pack, with the verifier, is published at partedmagic.com/verify so you can check one yourself before setting anything up.

## August 11, 2026

Parted Magic Erase Monitor is now on Google Play. It is a free companion app for the PM Report Server: point it at the server address you already gave the Erase utility, and every session on the bench shows up on your phone while it runs, including drives that fail. It talks only to your own server on your own network. Its Google Play data safety entry says it collects and shares no data.

Parted Magic Erase Monitor on Google Play

## June 19, 2026

Parted Magic’s store now supports the EU right of withdrawal function.

## Parted Magic 2026_06_04 – 2026-06-04

This release rolls up fixes for all the new apps and adds a few features. Those app fixes first shipped in the _23 revision of the 2026_03_20 release.

The features worth calling out in the 2026_06_04 release are the NVIDIA open driver and automatic Live mode detection. If you’re low on RAM and select the “Default to RAM” option, the system now switches to Live mode on its own so it can still boot. It also detects which NVIDIA driver is the best fit for your machine. I think most people can just pick the default option now and end up with a working setup.

If you haven’t updated Parted Magic in a while, you’ll be pleasantly surprised by what you find.

The Erase program is completely new. It replaces four separate programs (Secure Erase, ATA Sanitize, NVMe Secure Erase and NVMe Sanitize) with one program that identifies each drive and picks the right method itself. It handles ATA, NVMe, SAS/SCSI and eMMC/SD, follows NIST SP 800-88r2 (September 2025), and conforms to IEEE 2883 for technology-specific techniques.

Every erased drive now gets a signed PDF certificate with the fields of the sample Certificate of Sanitization in NIST’s Appendix C. The PM Report Server streams status, logs and certificates off the machine while the erase is still running, so a power cut can’t take the record with it, and you can watch a whole bench from your phone. Every session exports as a cryptographically signed evidence pack that your customer can verify offline with the included verifier, without an account or a network connection. There is also an unattended PXE mode: boot, wipe to policy, report and power down, with nobody at a keyboard. The report server and the verifier ship in the root of the ISO, and there is nothing extra to buy or install.

VisParted 2.0 was rebuilt from an empty file. It shares no source code with GParted or GNU Parted (I compared the complete source trees to be sure), and as of 2.0 it links no other project’s library at run time, including libparted, which earlier releases loaded to resize FAT. It reads and writes GPT, MBR and extended boot records itself, and after every operation it re-reads the disk and checks that the result matches the plan. If it does not, the operation is reported as failed, even when every tool involved reported success.

Moves are journaled and resumable, so losing power partway through no longer means starting over or guessing what state the partition is in. It converts MBR to GPT in place without data loss. It also opens every disk with a list of the problems it found, and the fixes for them.

If you used VisParted 1, the operation queue and Undo are gone on purpose. A queue plans against a picture of the disk that stops being true as soon as the first operation runs, and once data has moved, a partition table change cannot be undone. Each action now becomes its own plan that you read and approve, checked against the disk as it is right now, and journaled so it can be finished after an interruption.

There’s also a new GTK wrapper for Clonezilla that makes it much easier to run, with options to go back and save information between runs.

The Wipe Free Space app is brand new too and far more capable than the old clunky version. The mounting app has been rebuilt as well and now has a lot more mounting options than before. You can mount BitLocker, NFS, LUKS, FTP, and more. It’s paired with our own GTK file manager, built from scratch.

## Parted Magic 2026_03_20 – 2026-03-20

This is the release the current Parted Magic starts from, and the biggest change to the project since the original Secure Erase GUI in 2013.

Over the years Parted Magic had collected a lot of programs almost nobody used. The default boot mode loads the whole image into RAM, and the image had grown to need 16GB to run reliably, which also made PXE deployment impractical in many places. Unused and redundant packages are gone, and the compression moved from xz to zstd with optimized caching. Parted Magic now boots comfortably in the default mode on machines with 8GB, and the time from the GRUB menu to a loaded desktop is at least ten times faster.

Development of the new Erase program was already well underway when NIST published the SP 800-88r2 update in September 2025. I spent a good while bringing the program into compliance with the revised standard, and those changes shipped in pmagic_2026_03_20_5.iso. If you bought the 2026_03_20 release before that, log into your account and download the updated image at no additional cost.

Save Session was rewritten. The old one blindly copied all of /home and /etc to the flash drive. The new smart detection saves only what actually changed, including installed packages and objects in /usr, and it excludes transient paths like /var and /tmp. Delete a file and save, and that file is transparently removed on the next boot. A later update fixed a remaining Save Session problem and added Ventoy support, which puts a /pmagic folder in your ISO directory.

The Mount GUI and the file manager it is paired with were both written from scratch and tied directly to the Mounter. They are considerably more stable in a live environment than lightweight alternatives that depend on trash directories and udisks. There are also new keyboard layout and language configuration utilities, and a shutdown menu with an optional countdown that makes accidental shutdowns and reboots much harder.

Feedback on all of this helps, and it shapes what gets built. Bug reports, notes on how you use Parted Magic, and even word that something works as expected are all useful.

News entries prior to Parted Magic 2026_03_20 are archived at https://partedmagic.com/news.txt

<div
