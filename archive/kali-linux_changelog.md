# Changelog: Kali Linux

Quelle: https://www.kali.org/blog/
Stand: 21.09.2026 09:35

---

## 2026.2 – 2026-06-29

**Kali Linux 2026.2 Release (GNOME 50, KDE 6.6, Helper Scripts, APT Formats & VM Boot Tweaking)**

Table of Contents
- [Desktop Environments Updates](#desktop-environments-updates)[GNOME 50](#gnome-50)
- [KDE Plasma 6.6](#kde-plasma-66)

- [Improved Consistency For Services Helper Scripts](#improved-consistency-for-services-helper-scripts)
- [APT Gets A New Sources Format](#apt-gets-a-new-sources-format)
- [No More Graphics Firmware Pre-installed For VM Use-cases](#no-more-graphics-firmware-pre-installed-for-vm-use-cases)
- [Disruptive Package Updates](#disruptive-package-updates)
- [Linux Kernel For This Release: 6.19](#linux-kernel-for-this-release-619)
- [A Sneak Peek: Build Scripts](#a-sneak-peek-build-scripts)
- [New Tools in Kali](#new-tools-in-kali)
- [Kali NetHunter Updates](#kali-nethunter-updates)[The Qcacld3.0 Injection Story](#the-qcacld30-injection-story)
- [Wifite On TV](#wifite-on-tv)
- [Magisk Standalone Kernel Installer](#magisk-standalone-kernel-installer)
- [New Kernels](#new-kernels)
- [NetHunter Pro](#nethunter-pro)
- [NetHunter Podcast Episode 3](#nethunter-podcast-episode-3)

- [Kali Website Updates](#kali-website-updates)[Kali Documentation](#kali-documentation)
- [New Kali Mirrors](#new-kali-mirrors)

- [Get Kali Linux 2026.2](#get-kali-linux-20262)

It’s the final week of Q2, and Kali Linux 2026.2 is here - right on schedule ;) We have been heads down since our last release, and we are ready to share what we have been working on. This release is a mix of desktop refreshes, infrastructure improvements, and quality-of-life changes that we think you will appreciate.

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2026.1 release from March](https://www.kali.org/blog/kali-linux-2026-1-release/) is:

- [Desktop Environments](#desktop-environments-updates) - Bump to GNOME 50 and KDE Plasma 6.6
- [Helper Scripts Consistency](#improved-consistency-for-services-helper-scripts) - Consistency to our little launches at starting services
- [APT Format](#apt-gets-a-new-sources-format) - Goodbye sources.list, hello sources.list.d/kali.source
- [VM Boot Optimisation](#no-more-graphics-firmware-pre-installed-for-vm-use-cases) - Smaller initrd + faster boot times = happy virtual machine users
- [Reboot Warning](#disruptive-package-updates) - Heads-up, polkit and xrdp upgrades require a system reboot
- [Kali Kernel Incoming](#linux-kernel-for-this-release-619) - Staying with 6.19 for now, how to get 7.0 early
- [Build Scripts Incoming](#a-sneak-peek-build-scripts) - Heads-up with some changing on the way
- [New Tools](#new-tools-in-kali) - As always, various new shiny packages have been added (9!)

### Desktop Environments UpdatesAs we do roughly every six months, every other Kali release, our [desktop environments](https://www.kali.org/docs/general-use/switching-desktop-environments/) get a major update. This time it’s for: [GNOME](#gnome-50) and [KDE Plasma](#kde-plasma-6-6). Neither brings sweeping changes, but both have put real effort into refining performance and usability across the whole ecosystem.

#### GNOME 50GNOME 50 brings usability and performance improvements across the desktop. The file manager received significant optimizations, resulting in faster thumbnail and icon loading, improved responsiveness, and reduced memory usage. The desktop also received new accessibility enhancements through a brand-new preferences window, tweaks to the screen reader, and automatic language switching.

Another addition is support for document annotations in the Document Viewer app, making it easier to add text notes and highlights directly to documents.

Here you can read more about all the changes with this new GNOME release: [GNOME 50 release announcement](https://release.gnome.org/50/).

https://www.kali.org/blog/kali-linux-2026-2-release/images/gnome-50.png

#### KDE Plasma 6.6KDE Plasma 6.6 focuses on improving usability and accessibility while introducing several new features, including a new on-screen keyboard, providing a better experience particularly for touch-enabled devices.

The Spectacle screenshot utility can now recognize and extract text directly from screenshots, making OCR functionality available from the desktop. Accessibility has also been enhanced with new color-vision support options, improvements to Zoom and Magnifier, support for Slow Keys on Wayland, and adoption of the standardized Reduced Motion setting.

Here you can read more about all the changes with this new Plasma release: [KDE Plasma 6.6 release announcement](https://kde.org/announcements/plasma/6/6.6.0/).

https://www.kali.org/blog/kali-linux-2026-2-release/images/kde-6.6.png

### Improved Consistency For Services Helper ScriptsTo improve consistency across tools that depend on a service, we have updated our helper scripts. Previously, a tool that required a service might only let you start it (with no way to stop) - and the information displayed back was inconsistent (mixture of service status, how to access, default credentials or nothing at all). With this change, multiple packages have been updated to use these new scripts, which now handle the following tasks:

- Manage the service - start/stop
- Check if the service is already running - avoiding starting it twice
- Show the service status
- Show any [default credentials](https://www.kali.org/docs/introduction/default-credentials/)
- Show how to access it - such as if it’s a web UI, the URL (and bonus, automatically open it in the browser!)

We also make sure that any Kali packages which include a service use <tool>-start/<tool>-stop for their command names.

Hopefully this makes the little things a little easier.

https://www.kali.org/blog/kali-linux-2026-2-release/images/kali-services.png

### APT Gets A New Sources FormatSince the beginning of time, the APT sources for Kali Linux were configured in the file /etc/apt/sources.list. This file tells APT from where to update your system, and it’s so fundamental that pretty much everyone (that is, Kali users) knows this file and its content:

┌──(kali㉿kali)-[~]
└─$ cat /etc/apt/sources.list
# See https://www.kali.org/docs/general-use/kali-linux-sources-list-repositories/
deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware

Well, it’s a “once in a distro lifetime” kind of thing, and here it is - /etc/apt/sources.list is retired, in favor of the new file /etc/apt/sources.list.d/kali.sources:

┌──(kali㉿kali)-[~]
└─$ cat /etc/apt/sources.list.d/kali.sources
# See https://www.kali.org/docs/general-use/kali-apt-sources/
Types: deb
URIs: http://http.kali.org/kali/
Suites: kali-rolling
Components: main contrib non-free non-free-firmware
Signed-By: /usr/share/keyrings/kali-archive-keyring.gpg

All the freshly-installed systems will be configured as such. Existing systems won’t be changed. Both files are equivalent and work just the same. However, in the near future, APT will warn if the old file is in use, and will suggest modernizing it.

Note that, for those in the know, this isn’t anything new: both formats have existed for a long time now, and you could use either one or the other. What’s happening is that the default is slowly changing, from the old “one-line-style” to the new “deb822-style”. This is happening in Debian and in Debian-derivatives like Ubuntu. Kali is just following suit.

And for the curious, there’s a very complete and detailed manual page:

┌──(kali㉿kali)-[~]
└─$ man sources.list

### No More Graphics Firmware Pre-installed For VM Use-casesKali has had a long tradition of pre-installing a lot of firmware in its images. The upside is that users didn’t need to know what firmware they needed to install for their hardware to work: it was already there. And the downside, obviously, was that all the firmware that wasn’t needed was nevertheless installed and taking space for nothing.

It worked for us so far, in the sense that we don’t get too many bug reports related to missing firmware. But lately the changing landscape of graphics firmware forced us to re-evaluate this decision.

The issue with graphics firmware is that it just keeps growing bigger, and right now having it installed for [NVidia](https://www.kali.org/docs/general-use/install-nvidia-drivers-on-kali-linux/), AMD and Intel GPUs takes almost 300 MB. But what’s even worse: some bits and pieces of these firmware packages need to be loaded very early, and therefore they are also installed in the initrd (note: the initrd, or initramfs, is this “minimal” system that is loaded early on by the kernel at boot time). And lately, the Kali initrd peaked at around 200 MB, mainly due to graphics firmware. What does that mean in practice? A bigger initrd means slower boot time, and can potentially fill up your /boot partition if ever it’s too small.

So we thought we could improve the situation for VM users here: the vast majority probably don’t need graphics firmware, ever. The only use-case we can think of is a VM with a dedicated GPU + GPU passthrough enabled. If you’re in this case, you might need graphics firmware.

So, what changed in practice, you may ask?

- [Pre-built VM images](https://www.kali.org/get-kali/#kali-virtual-machines) don’t come with graphics firmware anymore
- [Installer images](https://www.kali.org/get-kali/#kali-installer-images) now detect if installation happens in a VM, and in that case graphics firmware is not installed

As a result, the initrd is down to 60 MB for VM users, and the boot time is cut by ~3x (tested for QEMU VM on a Linux host, your mileage may vary). That’s a massive improvement in boot time.

For baremetal users: nothing changed, so you still get a 200 MB initrd with all graphics firmware pre-installed. If you’d like to optimize, it’s on you to uninstall the firmware that you don’t need. A word of caution though: make sure to know what you’re doing, because removing graphics firmware that is needed might leave you with a [system without graphics after reboot](https://www.kali.org/docs/troubleshooting/graphics-issues-on-bare-metal-installation/).

### Disruptive Package UpdatesWe’ve got some slightly disruptive updates in this release.

polkit: a reboot is required

The update of the polkitd package requires a reboot, otherwise trying to start GUI applications as root will fail with cryptic error messages.

There’s an indication of this reboot requirement in the output of apt full-upgrade, when the polkitd package is updated. It’s just not very obvious, the hint is buried with the rest of the logs:

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt full-upgrade
[...]
Setting up libpolkit-gobject-1-0:amd64 (127+really127-0kali1)…
Setting up libpolkit-agent-1-0:amd64 (127+really127-0kali1)…
Setting up polkitd (127+really127-0kali1)…
Upgrading to this polkitd version requires a reboot, please reboot the system when convenient.
Created symlink '/etc/systemd/system/sockets.target.wants/polkit-agent-helper.socket' → '/usr/lib/systemd/system/polkit-agent-helper.socket'.
[...]

After a reboot, and if ever you still can’t run applications as root, make sure that polkit-agent-helper is started:

┌──(kali㉿kali)-[~]
└─$ sudo systemctl enable --now polkit-agent-helper.socket

If you’re still having issues, reach out on our [bug tracker](https://bugs.kali.org/).

xrdp: a reboot is required

In this Kali release, we updated xrdp and xorgxrdp to the v0.10 series. [xrdp](https://www.kali.org/docs/general-use/xfce-with-rdp/) is an open-source Remote Desktop Protocol server: you might use it if you connect to your Kali instance remotely. If you’re an xrdp user, you’ll need to reboot after this upgrade.

For those who run Kali in Hyper-V, using the [Enhanced Session Mode](https://www.kali.org/docs/virtualization/install-hyper-v-guest-enhanced-session-mode/): you’re an xrdp user, even if you didn’t know it! We did our best to ensure a smooth transition, and yet we got reports that xrdp wasn’t functional after the upgrade. If ever you’re in this case, you can try to run kali-tweaks, and in the Virtualization section you can try to disable, and then enable again the Hyper-V Enhanced Session Mode. That might fix the issue. Don’t forget to reboot!

As always, if you’re still having issues after that, feel free to reach out on the [Kali bug tracker](https://bugs.kali.org/).

### Linux Kernel For This Release: 6.19Regarding the version of the [Linux kernel](https://pkg.kali.org/pkg/linux) to include in this release of Kali, it’s been a tough decision.

On one hand, we’d like to release with the latest version of the Linux kernel, due to all the recent vulnerability disclosures ([Copy Fail/CVE-2026-31431](https://en.wikipedia.org/wiki/Copy_Fail), [Dirty Frag/CVE-2026-43284 & CVE-2026-43500](https://github.com/V4bel/dirtyfrag) and others ). On the other hand, when the 7.0 kernel reached Debian, there were [reports of incompatibilities with the NVidia DKMS drivers](https://bugs.debian.org/1135362) .

We decided to release with a 6.19 kernel to avoid breaking [NVidia users](https://www.kali.org/docs/general-use/install-nvidia-drivers-on-kali-linux/). At the same time, for those who prefer to get the latest kernel and don’t care about NVidia compatibility, we have the kernel 7.0 ready for you in kali-experimental. Make sure to check our documentation that explains [how to enable the kali-experimental repository](https://www.kali.org/docs/general-use/kali-apt-sources/#enabling-kali-additional-branches). The 7.0 kernel is also available in kali-rolling, so you can just [update your whole system](https://www.kali.org/docs/general-use/updating-kali/) and get the latest packages from [kali-rolling](https://www.kali.org/docs/general-use/kali-branches/).

### A Sneak Peek: Build ScriptsOur [build scripts](https://gitlab.com/kalilinux/build-scripts/) are what we use to produce every Kali image - ARM SBCs, Base (Installer and live ISOs), Cloud, Containers, VMs, WSL & NetHunter/Pro. Each lives in its own repo, and over time they have each grown in slightly different directions. For the next release, Kali 2026.3, we are doing a consistency pass across all of them: same structure, same conventions, same behaviour throughout.

As a result of these changes, some CI pipelines or workflows may need tweaking.

### New Tools in KaliThis release brings 9 new tools (to the network repositories). As always, we have been busy adding to the arsenal:

- [arsenal-ng](https://www.kali.org/tools/arsenal-ng/) - Go-based command library equipped with 200+ cybersecurity cheat-sheets
- [hydra-gtk](https://www.kali.org/tools/hydra/) - [Re-added] Very fast network logon cracker - GTK+ based GUI
- [legba](https://www.kali.org/tools/legba/) - Multiprotocol credentials bruteforcer / password sprayer and enumerator
- [oletools](https://www.kali.org/tools/oletools/) - Analyze MS OLE2 files and MS Office documents
- [penelope](https://www.kali.org/tools/penelope/) - Powerful shell handler
- [shell-gpt](https://www.kali.org/tools/shell-gpt/) - Command-line productivity tool powered by AI large language models
- [tailscale](https://www.kali.org/tools/tailscale/) - Secure connectivity platform
- [tookie-osint](https://www.kali.org/tools/tookie-osint/) - OSINT information gathering tool for finding social media accounts
- [uro](https://www.kali.org/tools/uro/) - Declutter URLs for crawling/pentesting

There has also been numerous packages updates and new libraries as well. We also bump the [Kali kernel to 6.19](#linux-kernel-for-this-release-619).

### Kali NetHunter Updateshttps://www.kali.org/blog/kali-linux-2026-2-release/images/nethunter-eviltwin.jpg

We have a tremendous amount of news for the lovers of mobile hacking! The [Kali NetHunter app](https://store.nethunter.com/packages/com.offsec.nethunter/) launches instantly now, various bugs have been fixed with the [custom commands](https://www.kali.org/docs/nethunter/nethunter-custom-commands/) and [chroot manager](https://www.kali.org/docs/nethunter/nethunter-chroot-manager/) . A new EvilTwin (Wi-Fi Fake AP) tab has been added with password verification captive portal, which brought along a really needed iptables fix. So now after using [Wifipumpkin3](https://www.kali.org/docs/nethunter/nethunter-wifipumpkin/) or EvilTwin, Android Hotspot will work properly. Huge thanks to the incredible work by [@dr.rootsu](https://gitlab.com/dr1408). The [kernel flasher tab](https://www.kali.org/docs/nethunter/nethunter-kernel/) has also received a refresh.

However, this release’s spotlight is on the beginning of the [Qcacld-3.0 injection patch](#the-qcacld30-injection-story) wave.

#### The Qcacld3.0 Injection StoryWe finally came to a milestone, shout-out to all the developers that worked on injection through the years!

[@kimocoder](https://gitlab.com/kimocoder) easily spent more than anyone else on this goal. His original injection implementation came to life, on a specific device: the OnePlus Nord (AC2003). You can find the commit [here](https://github.com/kimocoder/android_kernel_oneplus_avicii/commit/8eb5de1047e7bf069cb4de38c3a35489b35df189). Then [@Loukious](https://gitlab.com/Loukious) came in the mix and his modifications made it to work on other devices with [this port](https://github.com/Loukious/android_kernel_xiaomi_sm8150/commit/18c57c61ecd8f02de778e36db6be9b41167a8825). Finally, [@cyberknight777](https://gitlab.com/cyberknight777) did some housekeeping, removed unnecessary changes, logging, and restored the correct authorship while attributing @Loukious as co-author. The result, [this patch](https://github.com/Neternels/android_kernel_xiaomi_sunny/commit/1a4a7d313acc75cfca9a5e97673745d721b6ccea) is the almost universal one which brought many devices into the injection world, starting with the ones below for both kernel 4.x and 5.x versions:

- [OnePlus 7](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-oneplus-7/) (LineageOS 23.2)
- OnePlus 9 / 9 Pro
- OnePlus Nord
- POCO X3 Pro
- Redmi Note 10
- Samsung A73
- [Xiaomi Mi A3](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-xiaomi-mi-a3/) (LineageOS 23.2)
- Xiaomi Poco X3 NFC (PixelOS Android 16)
- Xiaomi Redmi Note 8

#### Wifite On TVhttps://www.kali.org/blog/kali-linux-2026-2-release/images/nethunter-wifite2-netflix-bloodhounds-s02e01.jpg

In the meantime, his continuous work on improving [wifite](https://www.kali.org/tools/wifite/) caught some attention - spotted on Netflix twice. Not bad!

#### Magisk Standalone Kernel InstallerThe kernel flasher tab (still experimental on some devices) is back in a new shape, giving a hint for the possible future look for the NetHunter app.

The Magisk standalone kernel flashing support is now here - you can simply open any newly built kernel installer zip in the Magisk app that was built using the [kali-nethunter-installer](https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-installer).

#### New KernelsIn addition to the kernels that now support the qcacld3 injection, there are several [new versions and phones](https://nethunter.kali.org/kernels.html):

- Google Pixel 6a (LineageOS 23.2)
- OnePlus 7 [SM8150] (LineageOS 23.2)
- Redmi 5A (crDroid 14)
- Samsung Note 20 Ultra (Android 13)
- [Samsung S10](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-samsung-galaxy-s10/) (LineageOS 23.2)
- Samsung S10 5G (LineageOS 23.2)
- Samsung S10+ (LineageOS 23.2)
- Samsung S10e (LineageOS 23.2)

#### NetHunter ProKali bare metal now on more phones, thanks to [Kali NetHunter Pro](https://www.kali.org/docs/nethunter-pro/)! New devices added in build thanks to the awesome work by [@shubhamvis98](https://gitlab.com/Shubhamvis98) and [Mobian Team](https://salsa.debian.org/Mobian-team):

- Fairphone FP5 (QCM6490) (fp5)
- Google Pixel 3 (SDM845) (blueline)
- Google Pixel 3a (SDM670) (sargo)
- Google Pixel 3a XL SDC panel (SDM670) (bonito-sdc)
- Google Pixel 3a XL Tianma panel (SDM670) (bonito-tianma)
- Google Pixel 4a (SDM730) (sunfish)
- LG G7 ThinQ (SDM845) (judyln)
- LG V35 ThinQ (SDM845) (judyp)
- Samsung Galaxy S9 China (SDM845) (starqltechn)
- SHIFTphone 8 (QCM6490) (otter)
- Sony Xperia 10 III (SM6350) (pdx213)
- Sony Xperia XZ2 (SDM845) (xperia-tama-apollo)
- Sony Xperia XZ2 Compact (SDM845) (xperia-tama-akari)
- Sony Xperia XZ2 Premium (SDM845) (xperia-tama-akatsuki)
- Xiaomi Mi 10T Lite (SM7225) (toco)
- Xiaomi Mi 9 Pro 5G (SM8150) (tucana)
- Xiaomi Mi 9T Pro Samsung panel (SM8150) (davinci-samsung)
- Xiaomi Mi 9T Pro Visionox panel (SM8150) (davinci-visionox)
- Xiaomi Mi Mix 2S (SDM845) (polaris)
- Xiaomi Poco X3 Huaxing panel (SM7150) (surya-huaxing)
- Xiaomi Poco X3 Tianma panel (SM7150) (surya-tianma)
- Xiaomi Redmi Note 10 Pro (SM7150) (sweet)

Previously SDM845 devices, USB On-The-Go (OTG) wasn’t working. However, thanks to [Max Furman](https://github.com/taygoth)’s work, USB switching has been added to OnePlus 6/6T devices (and DTB doesn’t need to be patched). This work will hopefully be ported to other devices and kernels in upcoming releases.

#### NetHunter Podcast Episode 3[@yesimxev](https://gitlab.com/yesimxev) and [@Kristopher Wilson](https://www.linkedin.com/in/kristopher-wilson-208b59123) joined for a discussion about NetHunter in cars, and leveraging AI for Bug Bounty projects and more.

### Kali Website UpdatesSince our last release, Kali 2026.1, we have been keeping the website and documentation up-to-date. Here is a quick summary of what has changed.

#### Kali DocumentationMost of the [documentation](https://www.kali.org/docs/) updates this cycle are around NetHunter device support and the new APT sources format. Pages which got something more than a tweak:

- [Creating A Custom Kali ISO](https://www.kali.org/docs/development/live-build-a-custom-kali-iso/) (updated)
- [Handling common APT problems](https://www.kali.org/docs/troubleshooting/handling-common-apt-errors/) (updated)
- [Installing NetHunter on the Samsung Galaxy S10](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-samsung-galaxy-s10/) (updated)
- [Installing NetHunter on the TicWatch Pro 3](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-ticwatch-pro-3/) (updated)
- [Installing NetHunter on the TicWatch Pro](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-ticwatch-pro/) (updated)
- [Installing NetHunter on the Xiaomi Mi A2](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-xiaomi-mi-a2/) (updated)
- [Installing NetHunter on the Xiaomi Mi A3](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-xiaomi-mi-a3/) (updated)
- [Kali NetHunter](https://www.kali.org/docs/nethunter/) (updated)
- [Kali Network Repositories (/etc/apt/sources.list)](https://www.kali.org/docs/general-use/kali-apt-sources/) (updated)
- [Kali’s Default Credentials](https://www.kali.org/docs/introduction/default-credentials/) (updated)
- [Submitting Bugs for Kali Linux](https://www.kali.org/docs/community/submitting-issues-kali-bug-tracker/) (updated)

We also want to say a little thank you to the following for their work on the sites:

- [@Chris Southerland Jr](https://gitlab.com/chrisjr404)
- [@mr00k3](https://gitlab.com/mr00k3)
- [@Simeon_YT](https://gitlab.com/Simeon53424)
- [@V0lk3n](https://gitlab.com/V0lk3n)

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

#### New Kali MirrorsWe welcomed 1 new mirror during this release cycle, but that’s a significant one: our first mirror in Africa! Hoping that many others will follow ;)

The mirror is located in South Africa, online at [mirror.africloud.com](https://mirror.africloud.com/kali/). It is sponsored by [AFRICLOUD](https://africloud.com/), and was setup thanks to Oluniyi Ajao.

If you have the disk space and bandwidth, [we always welcome new mirrors](https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/).

### Get Kali Linux 2026.2Fresh Images

So what’s stopping you? Go and [get Kali](https://www.kali.org/get-kali/) already!

If you cannot wait for the next release, we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) which include the latest packages at the time of download, meaning fewer updates needed on first boot. These are automated builds rather than QA’d releases like our standard [release images](https://www.kali.org/releases/), but we still welcome [bug reports](https://bugs.kali.org/) on them. The earlier we catch issues, the sooner they get fixed.

Existing Installs

Using Kali already? Great! You can [keep it up-to-date](https://www.kali.org/docs/general-use/updating-kali/) by doing:

┌──(kali㉿kali)-[~]
└─$ sudo tee /etc/apt/sources.list.d/kali.sources << 'EOF'
Types: deb
URIs: http://http.kali.org/kali/
Suites: kali-rolling
Components: main contrib non-free non-free-firmware
Signed-By: /usr/share/keyrings/kali-archive-keyring.gpg
EOF
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~/
[...]

┌──(kali㉿kali)-[~]
└─$ sudo reboot -f

Remember, we recommend doing [a reboot for this release](#disruptive-package-updates)!

You should now be on Kali Linux 2026.2. We can double check this by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2026.2"
VERSION_ID="2026.2"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Kali 6.19.14-1+kali1 (2026-05-05)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.19.14+kali-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, if you run into anything broken, please [report it](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And Social networks are not bug trackers!

Want to keep up-to-date easier? We’ve got you!

- [Blog](https://www.kali.org/blog/)? Use our [RSS feed](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/)
- [Download](https://www.kali.org/get-kali/)? We have a [Torrent RSS feed](https://www.kali.org/torrents.xml)
- [Socials](https://www.kali.org/docs/community/list-of-official-kali-sites/#social-media-networks)? [Bluesky](https://bsky.app/profile/kalilinux.bsky.social), [Facebook](https://www.facebook.com/KaliLinux/), [Instagram](https://www.instagram.com/kalilinux/), [Mastodon](https://infosec.exchange/@kalilinux) & [X](https://x.com/kalilinux)

## 2026.1 – 2026-03-24

**Kali Linux 2026.1 Release (2026 Theme & BackTrack Mode)**

Table of Contents
- [2026 Theme Refresh](#2026-theme-refresh)
- [BackTrack Mode For Kali-Undercover](#backtrack-mode-for-kali-undercover)
- [Kali’s 13th Birthday Event](#kalis-13th-birthday-event)
- [New Tools in Kali](#new-tools-in-kali)
- [Known Issues](#known-issues)
- [Kali NetHunter Updates](#kali-nethunter-updates)[Kali Blog Recap](#kali-blog-recap)

- [Community Shout-Outs](#community-shout-outs)[New Kali Mirrors](#new-kali-mirrors)

- [Get Kali Linux 2026.1](#get-kali-linux-20261)

New year, new release - Kali 2026.1 is here! There is everything from a fresh coat of paint to a nod to our roots, with normal ongoing improvements.
Building on from [December’s 2025.4](https://www.kali.org/blog/kali-linux-2025-4-release/), the summary of the [changelog](https://bugs.kali.org/changelog_page.php):

- [2026 Theme Refresh](#2026-theme-refresh) - Our yearly theme refresh
- [BackTrack Mode For Kali-Undercover](#backtrack-mode-for-kali-undercover) - New mode celebrating BackTrack’s 20th anniversary
- [Kali’s 13th Birthday Event](#kalis-13th-birthday-event) - A little community event
- [New Tools](#new-tools-in-kali) - 8 new programs

### 2026 Theme RefreshAs with previous 20xx.1 releases, this major update brings our annual theme refresh, a long-standing tradition that keeps the Kali Linux interface as modern and innovative. This year’s release unveils a brand-new theme from the moment you boot. Everything from the boot menu, installer to the login display, and a fresh set of [desktop wallpapers](https://www.kali.org/wallpapers/).

Boot Animation

The changes to the boot animation are subtle, but now the animation is fixed for live images, where it used to get stuck at the beginning, showing only the tail. It will also restart the loop in case the boot process takes longer, making it look smoother.

Your browser does not support the video tag.Boot Menu

https://www.kali.org/blog/kali-linux-2026-1-release/images/kali-grub.png

Graphical Installer

https://www.kali.org/blog/kali-linux-2026-1-release/images/kali-installer.png

Login

https://www.kali.org/blog/kali-linux-2026-1-release/images/kali-login.png

Desktop

https://www.kali.org/blog/kali-linux-2026-1-release/images/kali-desktop.png

Kali Purple Desktop

https://www.kali.org/blog/kali-linux-2026-1-release/images/kali-desktop-purple.png

New Wallpapers

https://www.kali.org/blog/kali-linux-2026-1-release/images/kali-wallpapers.jpg

### BackTrack Mode For Kali-Undercover2026 marks the 20th anniversary of [BackTrack Linux](https://www.backtrack-linux.org/), the [predecessor to Kali](https://www.kali.org/docs/introduction/kali-linux-history/). To celebrate this milestone, we wanted to bring back some nostalgia for longtime users of this legendary cybersecurity distribution by adding a “BackTrack mode” to kali-undercover. This mode transforms the desktop to recreate the look and feel of BackTrack 5, with the same wallpaper, colors, and window themes.

You can run it directly from the menu or by running kali-undercover --backtrack in the terminal. You can switch back to the default Kali desktop (or not) by running it again.

Your browser does not support the video tag.Here is a screenshot of BackTrack 5, so you can compare it with our theme:

https://www.kali.org/blog/kali-linux-2026-1-release/images/backtrack5-screenshot.png

### Kali’s 13th Birthday EventKali recently had our 13th birthday. To celebrate this, [our discord](https://discord.kali.org/) had a little event and prize give away to mark the occasion.
Shout-out to the people who managed to solve it already:

- @AI Program
- @Arszilla
- @UltraStrawberryDream

Even though the top 3 places and prizes have been claimed, we will keep it open for a little longer.
To help you get started, Kali is always getting [new tools](#new-tools-in-kali), it can take some patience to learn about each of them.

The Quieter You Become, The More You Are Able To Hear

Thanks to @BeamOfOldLight and @cr4mb0 from the DAFreqs for creating the puzzles!

### New Tools in KaliIt would not be a Kali release without some new tools!
Here is a quick rundown of the 8 new tools which have been added (to the network repositories):

- [AdaptixC2](https://www.kali.org/tools/adaptixc2/) - Extensible post-exploitation and adversarial emulation framework
- [Atomic-Operator](https://www.kali.org/tools/atomic-operator/) - Execute Atomic Red Team tests across multiple operating system environments
- [Fluxion](https://www.kali.org/tools/fluxion/) - Security auditing and social-engineering research tool
- [GEF](https://www.kali.org/tools/gef/) - Modern experience for GDB with advanced debugging capabilities
- [MetasploitMCP](https://www.kali.org/tools/metasploitmcp/) - MCP server for Metasploit
- [SSTImap](https://www.kali.org/tools/sstimap/) - Automatic SSTI detection tool with interactive interface
- [WPProbe](https://www.kali.org/tools/wpprobe/) - Fast WordPress plugin enumeration tool
- [XSStrike](https://www.kali.org/tools/xsstrike/) - Advanced XSS scanner

There have been a total of 25 new packages, 9 removed, and 183 updates. On top of that, we also bump the Kali kernel to 6.18.

### Known IssuesBad news for users of the kali-tools-sdr metapackage (aka. Software Defined Radio): the GNU Radio ecosystem is not in great shape in this release. Tools like gr-air-modes or gqrx-sdr are known to be broken. Maybe other related tools as well. We expect it to be fixed in the next release though, so no need to panic!

### Kali NetHunter UpdatesWe are starting this year fresh with some cleaning, providing improvements to the [Kali NetHunter app](https://store.nethunter.com/packages/com.offsec.nethunter/), such as the WPS scan bug, HID permission check, or the back button issue.

https://www.kali.org/blog/kali-linux-2026-1-release/images/nethunter-Redmi-Note-8-%28ginkgo%29.png

Redmi Note 8 (Ginkgo)

The [Redmi Note 8](https://nethunter.kali.org/device-kernels.html) now has a [new kernel](https://nethunter.kali.org/kernels.html) for [Android 16](https://nethunter.kali.org/android-versions.html) by [@ikteach](https://gitlab.com/ikteach).

Wardriving with Samsung S10

The Samsung S10 series are now even happier thanks to [@Quazi Anwar](https://github.com/pr0misc), his patch of [libnexmonkali](https://github.com/pr0misc/Libnexmonkali-Plus) fixes the use of internal wireless firmware in Kali chroot. That means [reaver](https://www.kali.org/tools/reaver/), [bully](https://www.kali.org/tools/bully/), and even [kismet](https://www.kali.org/tools/kismet/) is finally working!

https://www.kali.org/blog/kali-linux-2026-1-release/images/nethunter-honda.png

KITT is alive and he is hacking all the things!

[Kristopher Wilson](https://www.linkedin.com/in/kristopher-wilson-208b59123) has turned his [Civic Type-R into a pentesting tool using Kali NetHunter rootless on 4 wheels](https://www.linkedin.com/pulse/kitt-from-knight-rider-real-runs-nmap-kristopher-wilson-yycec).

And if AI is your thing, you can read what [he is done using that](https://www.linkedin.com/pulse/i-built-ai-can-ssh-my-cars-head-unit-from-virtual-machine-wilson-plffc).

https://www.kali.org/blog/kali-linux-2026-1-release/images/nethunter-wifi-injection-test2.jpg

Wireless Injection on QCACLD-3.0

Drumroll - the first working patch for injection is landed by [@Loukious](https://github.com/Loukious) after several years! That will potentially unlock the ability to port the patch to most of phones that use Qualcomm chipsets. If you would like to try it on your kernel source, you can find [the commit here](https://github.com/Loukious/android_kernel_xiaomi_sm8150/commit/8f0698bf92abef517980fe9a84615cd8bad16622).

Kali NetHunter Podcast - Nexmon Team

Meet the Nexmon team! The masters behind wireless injection on internal chipsets. If you ever wondered who are they, and how they started working on firmware reversing, [@yesimxev](https://gitlab.com/yesimxev) had a great talk on episode 2 with [@Matthias Schulz](https://www.linkedin.com/in/matthiasschulz1) and [@Jakob Link](https://github.com/jlinktu). We appreciate them for coming onto their first podcast ever! The session is also [available on Spotify](https://open.spotify.com/episode/46wU1TlAFHbwtCwEand6MX) if you want to listen on the go.

#### Kali Blog RecapSince our last release, we have published the following [blog posts](https://www.kali.org/blog/):

- [Kali & LLM: macOS with Claude Desktop & Anthropic Sonnet LLM](https://www.kali.org/blog/kali-llm-claude-desktop/)
- [Kali & LLM: Completely local with Ollama & 5ire](https://www.kali.org/blog/kali-llm-ollama-5ire/)

### Community Shout-OutsThese are members of the community who have supported Kali and the team throughout the last release. We want to recognize and thank them for their contributions (we believe in giving credit where it is due!):

Packaging:

- [@Arszilla](https://gitlab.com/Arszilla) who has been helping with [kali-meta](https://www.kali.org/tools/kali-meta/) and [netexec](https://www.kali.org/tools/netexec/)
- [@Giovanni Terranova](https://gitlab.com/mambu020) who has been helping with [legion](https://www.kali.org/tools/legion/)
- [@Jürgen](https://gitlab.com/jloehel) who has been helping with [mcp-kali-server](https://www.kali.org/tools/mcp-kali-server/)
- [@Shubham Vishwakarma](https://gitlab.com/Shubhamvis98) who has been helping with [kali-meta](https://www.kali.org/tools/kali-meta/)

Kali Documentation:

- [@Chen-Yuanmeng](https://gitlab.com/Chen-Yuanmeng)
- [@mr00k3](https://gitlab.com/mr00k3)
- [@Simeon_YT](https://gitlab.com/Simeon53424)
- [@Soroush Nekoozadeh](https://gitlab.com/Soroushnk80)

Anyone and everyone is welcomed to get [involved](https://www.kali.org/docs/community/contribute/)!

@Tristram has a few words they would like to say:

As a defender, my role centers on protecting organizations, strengthening systems, and continuously identifying opportunities for improvement. But effective security is not built by defenders alone. It is shaped through the combined efforts of both blue teamers and penetration testers, each bringing a different perspective to the same mission. Where one side looks to defend, the other works to challenge, expose gaps, and ultimately make those defenses stronger.

That relationship is critical. Penetration testers help uncover weaknesses before adversaries do, while defenders take those insights and turn them into actionable improvements. When that exchange is rooted in respect and a shared purpose, it creates a feedback loop that benefits the entire cybersecurity ecosystem. The result is not just better tools or processes, but a more resilient and adaptive security posture.

With that in mind, I want to call out @Aura and @Greenjam for their contributions to the Kali Linux Community. Their work represents the best of what this collaboration should look like. Through their willingness to share knowledge, support others, and contribute meaningfully to the community, they help bridge the gap between offensive and defensive security in a way that strengthens both sides.

In a field that is constantly evolving, it is this kind of collaboration and mindset that makes the difference. Whether you are on the blue team or working in an offensive role, we are all working toward the same goal. Contributions like theirs help ensure that we continue to learn from one another, improve together, and build a stronger, more unified cybersecurity community.

With love,

Tristram

#### New Kali MirrorsWe welcomed 4 new mirrors during this release cycle:

- Azerbaijan: [mirror.yer.az](https://mirror.yer.az/kali/), sponsored by [YER Hosting](https://yer.az/).
- China: [mirrors.qlu.edu.cn](https://mirrors.qlu.edu.cn/kali/), sponsored by the [Qilu University of Technology](https://www.qlu.edu.cn/) and thanks to 刘正阳.
- South Korea: [mirror.wane.kr](https://mirror.wane.kr/kali/), thanks to “@parkard” and “@kmw”.
- Spain: [mirror.raiolanetworks.com](https://mirror.raiolanetworks.com/kali/), sponsored by [Raiola Networks](https://raiolanetworks.com) and thanks to Martin Gomez.

If you have the disk space and bandwidth, [we always welcome new mirrors](https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/).

### Get Kali Linux 2026.1Fresh Images:
So what are you waiting for? Go [get Kali](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for those who are not, we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you will have fewer updates to do.
Just know that these are automated builds that we do, not QA like we do for our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~/
[...]

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2026.1. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2026.1"
VERSION_ID="2026.1"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Kali 6.18.12-1kali1 (2026-02-25)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.18.12+kali-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And Social networks are not bug trackers!

Want to keep up-to-date easier? We’ve got you!

- [Blog](https://www.kali.org/blog/)? Use our [RSS feed](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/)
- [Download](https://www.kali.org/get-kali/)? We have a [Torrent RSS feed](https://www.kali.org/torrents.xml)
- [Socials](https://www.kali.org/docs/community/list-of-official-kali-sites/#social-media-networks)? [Bluesky](https://bsky.app/profile/kalilinux.bsky.social), [Facebook](https://www.facebook.com/KaliLinux/), [Instagram](https://www.instagram.com/kalilinux/), [Mastodon](https://infosec.exchange/@kalilinux) & [X](https://x.com/kalilinux)

## 2025.4 – 2025-12-12

**Kali Linux 2025.4 Release (Desktop Environments, Wayland & Halloween Mode)**

Table of Contents
- [Desktop Environments](#desktop-environments)[GNOME 49](#gnome-49)
- [KDE Plasma 6.5](#kde-plasma-65)
- [New Colors for Xfce Desktop](#new-colors-for-xfce-desktop)

- [VM Guest Utils Support For Wayland](#vm-guest-utils-support-for-wayland)
- [Kali Halloween Mode](#kali-halloween-mode)
- [Kali Live image Is Now Distributed Over BitTorrent Only](#kali-live-image-is-now-distributed-over-bittorrent-only)
- [New Tools in Kali](#new-tools-in-kali)
- [Kali NetHunter Updates](#kali-nethunter-updates)
- [Kali Documentation](#kali-documentation)
- [Community Shout-Outs](#community-shout-outs)[New Kali Mirrors](#new-kali-mirrors)

- [Miscellaneous](#miscellaneous)
- [Get Kali Linux 2025.4](#get-kali-linux-20254)

Say hello to Kali Linux 2025.4!
Expect updated tools, performance tweaks, and improved support - no fluff, just the essentials.

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2025.3 release from September](https://www.kali.org/blog/kali-linux-2025-3-release/) is:

- [Desktop Environments](#desktop-environments) - Changes to all! GNOME, KDE & Xfce
- [Wayland](#vm-guest-utils-support-for-wayland) - VM Guest Utils Support
- [Halloween Mode](#kali-halloween-mode) - dresses the desktop for the occasion
- [3 New Tools](#new-tools-in-kali) - As always, new packages added and upgraded!

### Desktop Environments#### GNOME 49As with previous GNOME updates in Kali, we’ve given all our themes a fresh coat of paint - everything has been tuned to look sharp and feel smooth.

The Totem video player has been replaced with the new Showtime app, and the app grid now finally organizes Kali tools into folders, just like the menu does, making it far more intuitive to find the tool you need.

https://www.kali.org/blog/kali-linux-2025-4-release/images/gnome-kali-tools-app-grid.png

Changes to the application grid do not affect already installed versions of Kali. This is done to avoid overwriting the user’s application layout. If you still want to see the new folders in the application grid, you can force the update with the following command:

┌──(kali㉿kali)-[~]
└─$ cat /etc/dconf/db/local.d/kali-menu | dconf load /

Another quality-of-life improvement is the addition of a shortcut to quickly open a terminal (finally!), using Ctrl+Alt+T or Win+T - just like in our other desktops.

One of the major changes in GNOME 49 is the removal of X11 session support. Wayland is now the default - and only - window server, but do not worry: the transition is seamless and, as we explain later, even VM support is excellent.

If you want to know more about the details of the new shell version, check out the official [GNOME 49 release notes](https://release.gnome.org/49/).

#### KDE Plasma 6.5KDE Plasma desktop has been bumped up to version 6.5, which brings two major releases of the desktop together. Here are some of the most relevant new features:

- More flexible window tiling
- New screenshot tool, with extra editing features
- Quick access to pinned clipboard items in the panel
- Fuzzy matching support for KRunner (Plasma’s search/launch/calculator/… tool), which means that even if you misspell an app’s name, it will still find it for you.

If you want to learn more about the new changes for this awesome DE, check out the [Plasma 6.4 announcement](https://kde.org/announcements/plasma/6/6.4.0/) and [Plasma 6.5 announcement](https://kde.org/announcements/plasma/6/6.5.0/).

https://www.kali.org/blog/kali-linux-2025-4-release/images/kali-plasma-6.5.png

#### New Colors for Xfce DesktopWith this update, we wanted to bring support for color themes to Xfce, putting it on par with the already available settings in the other desktops (GNOME and KDE). Now you can fully customize the colors of your Kali installation with the new themes for icons, GTK 3/4 windows, Qt 5/6 windows, and Xfce’s window manager decorations.

https://www.kali.org/blog/kali-linux-2025-4-release/images/xfce-themes.png

All these settings can be changed through the “Appearance” application, except for Qt programs, which require separate themes and can be tweaked through qt5ct or qt6ct (both installed by default).

https://www.kali.org/blog/kali-linux-2025-4-release/images/xfce-themes-settings.png

### VM Guest Utils Support For Wayland[Wayland](https://www.kali.org/docs/general-use/wayland/) is a modern display protocol that serves as the successor to the older X11 system for handling graphics in Linux. It specifies how graphical applications (clients) communicate with a display server to render content and process user input. For years, X11 has been the default system in most UNIX desktops, but the time has come for a change to more modern software with a more efficient and secure architecture.

Now that [GNOME has moved to only supporting Wayland](#gnome-49), and KDE in Kali has already used it by default for a few years (since [Kali Linux 2023.1](https://www.kali.org/blog/kali-linux-2023-1-release/)), we wanted to ensure that the transition and experience were seamless. The only thing that we felt was missing was support for [VM guest tools](https://www.kali.org/docs/virtualization/), like clipboard sharing and window scaling, but things have been progressing, and now all the major VM software fully supports Wayland.

We have tested Kali installations with Wayland as the guest OS in [VirtualBox](https://www.kali.org/docs/virtualization/install-virtualbox-guest-vm/), [VMware](https://www.kali.org/docs/virtualization/install-vmware-guest-vm/), and [QEMU](https://www.kali.org/docs/virtualization/install-qemu-guest-vm/), configured the missing parts, and we are happy to announce that all of the VM guest additions that you expected in X11 before are now working in Wayland without trouble.

### Kali Halloween ModeDuring last Halloween season, we wanted to celebrate by launching a Kali/Hacker-themed pumpkin carving contest. We also launched a new mode for kali-undercover called Halloween mode, which dresses the desktop for the occasion!

Your browser does not support the video tag.While the Halloween mode has now been hidden from the menu, you can still launch it from your terminal in case you missed it and want to give it a try.

┌──(kali㉿kali)-[~]
└─$ kali-undercover --halloween

### Kali Live image Is Now Distributed Over BitTorrent OnlyTo download Kali images, we usually provide two options: direct HTTP download or BitTorrent. HTTP downloads are served either by a mirror from the community, or the [Cloudflare CDN](https://blog.cloudflare.com/cloudflare-repositories-ftw/). For the later, there’s a hard size limit: around 5 GB, or 5,049,942,016 bytes to be precise.

We already have an image that is way, way too big for the CDN: it’s the [Everything image](https://www.kali.org/docs/introduction/what-image-to-download/#everything), which contains all Kali tools, and peaks at 13 GB (installer) and 15 GB (live). This image can only be downloaded via BitTorrent.

With this release, another image will now be available only over BitTorrent: it’s the [Live image](https://www.kali.org/get-kali/#kali-live)

For more background: we try hard to provide the same Kali Linux experience by default, for all images: whether you download a [Pre-built VM](https://www.kali.org/docs/introduction/download-official-kali-linux-images/), [a Installer ISO or a Live ISO](https://www.kali.org/docs/introduction/what-image-to-download/), you’ll get the same Kali, with the same Xfce desktop environment, and the same set of tools pre-installed. We also try to keep the default set of tools relatively stable, so that the tools that you use today are still present in the next release.

As time passes, packages tend to gain new dependencies, acquire more features, and generally speaking: everything gets bigger and bigger, and so do our Kali images. The Live image has been flirting with the 5 GB limit for a while, and this time it’s over the limit for good.

The Live image has always been an outlier in terms of size: it is a fully-fledged and ready-to-run Kali system, but it can also be used to install Kali, meaning that it also contains the Kali installer with a minimal pool of packages. For this reason, this image has always been bigger than any others.

After discussions with the team, we decided that we did not want to remove tools from the default installation, as other images are well below the size limit. We do not want to remove tools from the Live image only either, as it’s going to be confusing, and it’s just going to make the Live image less useful. So our only option at this point is to remove the Live image from the HTTP distribution channel, and distribute it over BitTorrent only. Like we already do for the everything image.

Just to be geeky, here’s a breakdown of sizes for the last 2025.3 release, and the explanation for their sizes:

- [Pre-built VM](https://www.kali.org/get-kali/#kali-virtual-machines): 3.5 GB, these are the smaller images, basically it’s your default Kali Linux that is pre-installed and compressed with xz. That’s the best we can do in terms of compression.
- [Installer](https://www.kali.org/get-kali/#kali-installer-images): 4.3 GB, it contains the same set of packages, but uninstalled (ie. as .deb files), so in terms of compression it’s a mixed bag of gz and xz compression (gz compresses much less than xz). Additionally it contains the Kali installer, which is a kind of mini OS dedicated to installing Kali.
- [Live](https://www.kali.org/get-kali/#kali-live): 4.7 GB, as said above, it’s a pre-installed Kali system, compressed with xz, plus the Kali installer, plus a minimal pool of packages.

### New Tools in KaliAs with every Kali release, new tools have been introduced (to the network repositories). Below is a brief summary of the additions:

- [bpf-linker](https://www.kali.org/tools/bpf-linker/) - Simple BPF static linker
- [evil-winrm-py](https://www.kali.org/tools/evil-winrm-py/) - Python-based tool for executing commands on remote Windows machines using the WinRM
- [hexstrike-ai](https://www.kali.org/tools/hexstrike-ai/) - MCP server that lets AI agents autonomously run tools

In addition, numerous packages have been updated, and new libraries have been incorporated. We also bump the Kali kernel to 6.16.

### Kali NetHunter UpdatesWe are delighted to start this year’s winter season with awesome news! As usual, snowfall is now back on the Kali NetHunter app. Bugfixes, new features, new devices, an interview, and a live showcase podcast with offensive attacks.

https://www.kali.org/blog/kali-linux-2025-4-release/images/Kali-NetHunter-christmas.jpg

Android 16 Support

Our recommended device family kicks in the door of Android 16. Made by [@V0lk3n](https://gitlab.com/V0lk3n), the Samsung Galaxy S10, S10e, S10 Plus, and S10 5G running LineageOS 23 are now added with all the Kali NetHunter features including CAN, as well as internal wireless injection support. Check out the [install guide for the S10](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-samsung-galaxy-s10/) as an example. OnePlus Nord now also has Android 16 support by [@kimocoder](https://gitlab.com/kimocoder). Last but not least, [@k0d14k](https://gitlab.com/k0d14k) added support for Xiaomi Mi 9 on Android 15.

https://www.kali.org/blog/kali-linux-2025-4-release/images/Kali-NetHunter-devices.jpg

Kali NetHunter Terminal

We are extremely thankful for your patience since the last release. The [Terminal](https://store.nethunter.com/packages/com.offsec.nhterm/) is now up and running again, thanks to the team effort of @yesimxev, @kimocoder, and [@martin](https://gitlab.com/Martinvlba). At the same time, @kimocoder added support for any Magisk version that has interactive mode. Therefore, hitting CTRL+C would not close the terminal session anymore.

As of this writing, Magisk v30.6 is supported by the Terminal app.

Wifipumpkin 3

Wifipumpkin3 tab now has preview available in in NH app, updated by @yesimxev. He also added the latest templates of @IKTEACH and @dr.rootsu - Facebook, Instagram, iCloud, Snapchat. Credits for the great collaboration.

https://www.kali.org/blog/kali-linux-2025-4-release/images/Kali-NetHunter-Wifipumpkin.jpg

Miscellaneous

The kernel install tab is temporarily disabled as it needs some more maintenance. You will notice that @kimocoder started transforming some of the fragments to the new style. He also added a very early alpha version of the in-app terminal. You can enable in Kali NetHunter app settings if you’d like to check it out. Most commands will still go to the external Terminal app. Magisk installer now supports modules install, credits to [@cyberknight777](https://gitlab.com/cyberknight777). Therefore, installed Kali NetHunter kernel modules will show up in Modules tab.

Kali NetHunter Live Podcast

@yesimxev hosted the first NetHunter Live Podcast featuring [@Lukas Stefanko](https://github.com/androidmalware), also known as Mobile Hacker. Live wireless attacks from phone and smartwatch, kon-boot Windows password bypass using smartwatch, Q&A, and guest talk. Make sure you check out if you missed the live stream! Episode two coming in January. Feedbacks are very welcomed.

Kali NetHunter Blog Interview

A [deep dive](https://www.mobile-hacker.com/2025/11/11/inside-the-mind-of-a-kali-nethunter-developer-a-deep-dive-with-yesimxev/) into our lead Kali NetHunter developer, @yesimxev’s mind. His story of how he’s got into cybersecurity and NetHunter, a brief overview of features, devices, future plans, and more!

### Kali DocumentationWe have refreshed our[Kali documentation](https://www.kali.org/docs/) with updates to current pages and a handful of new ones:

- [Graphics issues on bare-metal installation](https://www.kali.org/docs/troubleshooting/graphics-issues-on-bare-metal-installation/) (new)
- [Installing NetHunter on the Samsung Galaxy S10](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-samsung-galaxy-s10/) (new)
- [Setting up a system for packaging](https://www.kali.org/docs/development/setting-up-packaging-system/) (updated)

### Community Shout-OutsThese are community members who contributed to Kali during the latest release, and we want to recognize their efforts (we believe in giving credit where it’s due!).

- [@Hackman2381](https://gitlab.com/Hackman2381)
- [@Soroush Nekoozadeh](https://gitlab.com/Soroushnk80)
- [@V0lk3n](https://gitlab.com/V0lk3n)
- [@yesimxev](https://gitlab.com/yesimxev)

Anyone is welcome to contribute, and anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

#### New Kali MirrorsWe have 3 new mirrors in Asia! Those are:

- India: [mirrors.esto.network](https://mirrors.esto.network/kali/), sponsored by [Esto Networks](https://esto.network/) and thanks to Rahul Makhija.
- South Korea: [mirror2.keiminem.com](https://mirror2.keiminem.com/kali/), sponsored by [Keiverse](https://keiminem.com/).
- South Korea: [mirror.eliv.digital](https://mirror.eliv.digital/kali/), sponsored by [PROJECT ELIV](https://eliv.digital/) and thanks to Chobi.

And 1 new mirror in North America:

- United States: [mirror.us.cdn-perfprod.com](https://mirror.us.cdn-perfprod.com/kali/), thanks to Marc Gómez.

If you have the disk space and bandwidth, [we always welcome new mirrors](https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/).

### MiscellaneousHere are a few additional Kali updates we are calling out, though they do not warrant a deep dive:

- Our [status page](https://status.kali.org/) has been refreshed!
- Early this year, [@arnaudr](https://gitlab.com/arnaudr) gave a talk at [DebCon25](https://debconf25.debconf.org/talks/122-kali-linux-delivery-of-a-rolling-distro-at-scale-with-mirrorbits/) about mirrorbits ([Slides](https://arnaudr.io/static/debconf25-kali-mirrorbits/), [Video](https://meetings-archive.debian.net/pub/debian-meetings/2025/DebConf25/debconf25-217-kali-linux-delivery-of-a-rolling-distro-at-scale-with-mirrorbits.av1.webm))
- Various CI fixes for [Kali Cloud](https://gitlab.com/kalilinux/build-scripts/kali-cloud) & [Kali WSL App](https://gitlab.com/kalilinux/build-scripts/kali-wsl-app)

### Get Kali Linux 2025.4Fresh Images:
So what are you waiting for? Go [get Kali](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for those who are not, we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you will have fewer updates to do.
Just know that these are automated builds that we do, not QA like we do for our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~/
[...]

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2025.4. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2025.4"
VERSION_ID="2025.4"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Kali 6.16.8-1kali1 (2025-09-24)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.16.8+kali-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And Social networks are not bug trackers!

Want to keep up-to-date easier? We’ve got you!

- [Blog](https://www.kali.org/blog/)? Use our [RSS feed](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/)
- [Download](https://www.kali.org/get-kali/)? We have a [Torrent RSS feed](https://www.kali.org/torrents.xml)
- [Socials](https://www.kali.org/docs/community/list-of-official-kali-sites/#social-media-networks)? [Bluesky](https://bsky.app/profile/kalilinux.bsky.social), [Facebook](https://www.facebook.com/KaliLinux/), [Instagram](https://www.instagram.com/kalilinux/), [Mastodon](https://infosec.exchange/@kalilinux) & [X](https://x.com/kalilinux)

## 2025.3 – 2025-09-23

**Kali Linux 2025.3 Release (Vagrant & Nexmon)**

Table of Contents
- [HashiCorp: Packer & Vagrant](#hashicorp-packer--vagrant)
- [Nexmon Support](#nexmon-support)
- [Dropping ARMel](#dropping-armel)
- [Configurable VPN IP panel plugin (Xfce)](#configurable-vpn-ip-panel-plugin-xfce)
- [New Tools in Kali](#new-tools-in-kali)
- [Kali NetHunter Updates](#kali-nethunter-updates)[Wireless Injection](#wireless-injection)
- [CARsenal Update](#carsenal-update)
- [Modules in Magisk](#modules-in-magisk)
- [Bugfixes & Improvements](#bugfixes--improvements)
- [Playground](#playground)

- [Kali ARM SBC Updates](#kali-arm-sbc-updates)
- [Miscellaneous](#miscellaneous)
- [Kali Documentation](#kali-documentation)
- [Kali Blog Recap](#kali-blog-recap)
- [Community Shout-Outs](#community-shout-outs)[New Kali Mirrors](#new-kali-mirrors)

- [Get Kali Linux 2025.3](#get-kali-linux-20253)

Another quarter, another drop - Kali 2025.3 is now here! Bringing you another round of updates, new features and introducing some new tools - pushing Kali further.
The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2025.2 release from June](https://www.kali.org/blog/kali-linux-2025-2-release/) is:

- [Packer & Vagrant](#hashicorp-packer--vagrant) - HashiCorp’s products have had a refresh
- [Nexmon Support](#nexmon-support) - Monitor mode and injection for Raspberry Pi’s in-built Wi-Fi
- [10 New Tools](#new-tools-in-kali) - As always, various new packages added (as well as updates)

### HashiCorp: Packer & VagrantKali has been using two HashiCorp products, which go hand-in-hand with each other:

- [Packer](https://developer.hashicorp.com/packer) - Creating VMs for multiple platforms from a single source configuration
- [Vagrant](https://developer.hashicorp.com/vagrant) - Building and managing VM environments

Until now, we have been using our Packer build-script to generate our Vagrant VMs. This has been working well for us.
We wanted to streamline our platform building process more, which prompted us to revisit how we generate Vagrant VMs.
Whilst it is possible to automate Packer, it was not ideal for our infrastructure setup and workflow (e.g. trying to build Hyper-V images on Linux).

This caused us to refresh a few items:

- [Kali pre-seed examples](https://gitlab.com/kalilinux/recipes/kali-preseed-examples) - Packer uses pre-seed to automate the Kali installer - we made sure they are all consistent.
- [Kali Packer build-scripts](https://gitlab.com/kalilinux/build-scripts/kali-packer/-/tree/main) - We were using v1 of the standards. We upgraded to v2.
- [Kali VM build-scripts](https://gitlab.com/kalilinux/build-scripts/kali-vm) - Vagrant images are VMs which a few tweaks done to them. We added these modification to our existing VM build-scripts.

For more information, please keep reading our blog post: [Kali Vagrant Rebuilt: Out With Packer, In With DebOS](https://www.kali.org/blog/kali-vagrant-rebuilt/)

### Nexmon SupportNexmon is a “patched” firmware, for certain wireless chips, to extend their functionally to allow:

- Monitor mode - able to sniff packets
- Injection mode - frame injection allows for custom raw packets to be sent, outside of the “standard” stack ordering

Both are really useful when it comes to information security!
For the record, it is possible to-do both of the features above without Nexmon, as it depends on the device’s chipset and drivers.

Now, Nexmon supported wireless chips are Broadcom & Cypress, which are in a various devices, including the Raspberry Pi’s in-built Wi-Fi!
In [Kali 2025.1](https://www.kali.org/blog/kali-linux-2025-1-release/), we changed how we package our Raspberry Pi kernel, as well as bump to a new major version. Now Nexmon support is back as well as supporting Raspberry Pi 5!
Other devices can also use Nexmon, its not limited to Raspberry Pis.

To find out more, please see our previous blog post: [The Raspberry Pi’s Wi-Fi Glow-Up](https://www.kali.org/blog/raspberry-pi-wi-fi-glow-up/)

### Dropping ARMelWe are announcing that we too are dropping support for ARMel (Acorn RISC Machine, Little-Endian). We are [following Debian’s footsteps in this decision](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1113680): Debian “trixie” 13 is the [last release with ARMel support](https://www.debian.org/releases/trixie/release-notes/issues.en.html#armel-last-release), and Debian testing (which Kali is based on) doesn’t provide ARMel packages anymore.

Luckily, the [amount of devices](https://arm.kali.org/images.html) which use this architecture is very limited:

- Raspberry Pi 1 (Original)
- Raspberry Pi Zero W
- ODROID-W, which already is End-Of-Life.

We cannot justify the amount of resources, both human power as well as hardware, required to support such a limited amount of legacy hardware. We would much rather put the time into RISC-V…

### Configurable VPN IP panel plugin (Xfce)In [Kali 2024.1](https://www.kali.org/blog/kali-linux-2024-1-release/), we introduced a new Xfce panel plugin that allows users to quickly check and copy the current IP address of their VPN connection. Until now, it was only possible to view the IP of the first VPN, but if you were using multiple connections or wanted to check a different interface, there was no way to switch it. To improve the usability of this plugin, we have now added the option to choose which network interface the plugin monitors.

https://www.kali.org/blog/kali-linux-2025-3-release/images/xfce-vpn-ip-plugin.png

To configure it, right-click the VPN-IP plugin and open the preferences dialog, where you can set the new interface at the end of the “Command” parameter. If you don’t see the VPN-IP plugin, you can find it in the panel preferences by searching for the “Generic Monitor” plugin in the “Items” tab.

### New Tools in KaliIt would not be a Kali release if there were not any new tools added! A quick run down of the 10 tools which have been added to the network repositories:

- [Caido](https://www.kali.org/tools/caido/) - The client side of caido (the graphical/desktop aka the main interface) - a web security auditing toolkit
- [Caido-cli](https://www.kali.org/tools/caido-cli/) - The server section of caido - a web security auditing toolkit
- [Detect It Easy (DiE)](https://www.kali.org/tools/detect-it-easy/) - File type identification
- [Gemini CLI](https://www.kali.org/tools/gemini-cli/) - An open-source AI agent that brings the power of Gemini directly into your terminal
- [krbrelayx](https://www.kali.org/tools/krbrelayx/) - Kerberos relaying and unconstrained delegation abuse toolkit
- [ligolo-mp](https://www.kali.org/tools/ligolo-mp/) - Multiplayer pivoting solution
- [llm-tools-nmap](https://www.kali.org/tools/llm-tools-nmap/) - Enables LLMs to perform network discovery and security scanning tasks using the nmap
- [mcp-kali-server](https://www.kali.org/tools/mcp-kali-server/) - MCP configuration to connect AI agent to Kali
- [patchleaks](https://www.kali.org/tools/patchleaks/) - Spots the security fix and provides detailed description so you can validate - or weaponize - it fast
- [vwifi-dkms](https://www.kali.org/tools/vwifi-dkms/) - Setup “dummy” Wi-Fi networks, establishing connections, and disconnecting from them

There have also been numerous packages updates and new libraries as well.

As a heads up, we are looking at altering the tools which get installed by default in Kali 2025.4, via the kali-linux-default metapackage.

### Kali NetHunter UpdatesKali NetHunter team and the community has been busy working away on Kali on mobile devices, with Kali NetHunter, [app](https://store.nethunter.com/packages/com.offsec.nethunter/) and [terminal](https://store.nethunter.com/packages/com.offsec.nhterm/)!

#### Wireless Injectionhttps://www.kali.org/blog/kali-linux-2025-3-release/images/Kali-NetHunter-WiFi-Injection.jpeg

We are happy to announce that we finally have a new budget friendly device since Nexus 5, which supports internal monitor mode with injection on both 2.4Ghz and 5Ghz. After an awesome collaboration, the Kali NetHunter Samsung Galaxy S10 is born. The [Nexmon team](https://github.com/seemoo-lab/nexmon) patched the broadcom firmware, [@V0lk3n](https://linktr.ee/v0lk3n) ported the Kali NetHunter kernel, and [@yesimxev](https://gitlab.com/yesimxev) released Hijacker arm64 version to avoid app crashes. The install guide is available here for [Nexmon](https://forums.kali.org/t/hijacker-on-the-samsung-galaxy-s10-with-wireless-injection/10305) and [Kali NetHunter](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-samsung-galaxy-s10/).

#### CARsenal UpdateKali NetHunter Car Hacking, CARsenal, continues to expand with a lot of change and new features by @V0lk3n!

You will need to run the setup again, to apply all the new changes and install any new packages.

Even if it’s a “Car Hacking” toolset, we discourage you from trying this on your daily driver. Use it on a controlled environment. Either OffSec or the Kali team will not take responsibility for your actions, especially if you break your car.

What’s New?

- Main - Settings has been moved to menu bar and all service commands can be edited by long pressing oranges buttons. New RFCOMM Connect service.
- Tools - Settings has been moved to menu bar. When configuring your settings, tools buttons will be updated with it, and all tools commands can be edited by long pressing oranges buttons.
- CAN-USB - Settings as been moved to menu bar. When configuring your settings, Run button will be updated with it.
- Caring Caribou - All modules and sub-modules as been added to Caribou, excepted doip which should come in 2025.4 update and DCM which is replaced by UDS. All module spinner have been merged into modules and submodules spinner. Settings parameters is now displayed depending of the module/submodule chosen.
- ICSim rewrite - ICSim is renamed to Simulator, and UDSim has been added to it - enjoy more simulation for learning and testing purpose! Also a new feature to hide/display the controls view and to make ICSim/UDSim a float-able window has been added! Keep the simulator in front of your eyes while running tools from CARsenal or NetHunter Terminal!
- New MSF tab - A new MSF tab has been added, providing automotive modules for [Metasploit-Framework](https://www.kali.org/tools/metasploit-framework/). Setup a hardware bridge, connect to it and run post modules!
- About dialog - About dialog page and it’s credit has been updated.

What Else?

- UI - User Interface has been updated a lot! Thanks to @kimocoder for inspiration!
- Bug Fix - A lot of bug fix and no more outdated libraries used! Thanks again to @kimocoder for this!
- CARsenal Refactoring - Refactoring process of CAN Arsenal to CARsenal is now complete.
- Documentation - Complete rewrite of [CARsenal documentation](https://www.kali.org/docs/nethunter/nethunter-carsenal/) for 2025.3 content (no change for the kernel documentation part).
- New Kernel Supporting CAN - OnePlus6 for LineageOS 22.2 (Android 15). Note that it was made for OnePlus6 and not it’s 6T variant. This will be updated soon as well to support it.

What to come next?

Expect to see for 2025.4 more UI update, better MSF screen terminal, Simulator update and more! We are also planning to make series of videos demonstrating CARsenal, If you notice a bug or simply wish to have a feature added to CARsenal, get in touch!

#### Modules in MagiskKernel modules install with Magisk is now supported and are included in the released install images. It is still in experimental state. Credits to @yesimxev and [@cyberknight777](https://gitlab.com/cyberknight777).

#### Bugfixes & ImprovementsThanks largely to [@kimocode](https://x.com/kimocoder) who made a lot of code updates improving UI, stability and more!
Bellow is a list of changes:

- Boot animation is now fixed
- Improved/Added API 21 to API 34+
- Made busybox_nh available in Android (SU) shell
- Made the bootkali" and “killkali” scripts available in Android (SU) shell
- Removed the non-working ‘Deauth’ tab (fragment)
- Replaced many deprecated libraries
- Replaced the deprecated ‘AsyncTask’ with ‘Executer’ which improves threading and background tasks making the application for stable and improve performance
- Updated all libraries in use to latest
- Updated BusyBox binaries
- Updated Gradle / JAVA
- Updated the “Audio” fragment
- Updated the “GPS” fragment
- Updated the kernel “Modules” fragment
- Updated vulnerable database list (WPS)
- WP3: Fix templates not showing in the Spinner

#### Playground@yesimxev had fun on his car radio again. Let’s combine a Kali NetHunter phone, RTL-SDR, and a car radio. The result? [Airspace visualizer](https://github.com/mebrown47/airspace-visualizer) in your car, bringing the wardriving vibes, especially with the radar design. Credits to @ElbaSatGuy for creating this awesome project.

Finally, he tried out the Bad Bluetooth Attack on his smartwatch, to take over a Samsung tablet.

### Kali ARM SBC UpdatesOther than Nexmon, which we have already covered, Kali ARM has also had a few other improvements:

- We have fixed an issue with the Kernels not always getting updated.
- For our Raspberry Pi images, we are now recommending to use the 64-bit (arm64) image rather than 32-bit (armhf).
- The Raspberry Pi 64-bit (arm64) image will also do Raspberry Pi 5! There is no longer a dedicated image just for this device.
- The Raspberry Pi 2 doesn’t support 64-bit (arm64), so if you are still rocking it, grab the 32-bit (armhf).

### MiscellaneousBelow are a few other things which have been updated in Kali, which we are calling out, which do not have as much detail:

- New [community wallpapers](https://www.kali.org/wallpapers/community/) in multiple colors (thanks [@IAmNewbie99](https://gitlab.com/IAmNewbie99))
- OffSec, the company who founded Kali, will be soon offering a free “Capture The Flag” (CTF) event in October with $100,000 in prizes. For more information, and to pre-register see “[The Gauntlet](https://www.offsec.com/events/the-gauntlet/?utm_source=kali&utm_medium=web&utm_campaign=blog)”
- A great guide to read: [So You Want To Build A NetHunter Kernel](https://gitlab.com/akabulous/So_You_Want_To_Build_A_Nethunter_Kernel)

### Kali DocumentationOur [Kali documentation](https://www.kali.org/docs/) has had various updates to existing pages as well as new pages:

- [Installing Docker on Kali Linux](https://www.kali.org/docs/containers/installing-docker-on-kali/) (Updated)
- [Resolving APT Errors Caused by an Expired Kali Linux Signing Key](https://www.kali.org/docs/general-use/gpgkey-expiry/) (New)
- [Setting up a system for packaging](https://www.kali.org/docs/development/setting-up-packaging-system/) (Updated)
- [Reset Bloodhound’s admin password](https://www.kali.org/tools/bloodhound/#reset-bloodhounds-admin-password) (Updated)

### Kali Blog RecapSince our last release, we did the following [blog posts](https://www.kali.org/blog/):

- [The Raspberry Pi’s Wi-Fi Glow-Up](https://www.kali.org/blog/raspberry-pi-wi-fi-glow-up/)
- [Kali Linux & Containerization (Apple’s Container)](https://www.kali.org/blog/kali-apple-container-containerization/)
- [Kali Vagrant Rebuilt: Out With Packer, In With DebOS](https://www.kali.org/blog/kali-vagrant-rebuilt/)

### Community Shout-OutsThese are people from the public who have helped Kali and the team for the last release. And we want to praise them for their work (we like to give credit where due!):

- [@Arszilla](https://gitlab.com/Arszilla)
- [@Chris Patterson](https://gitlab.com/cjp256)
- [@Eko Wibowo](https://gitlab.com/eko.wibowo87)
- [@Funeoz](https://gitlab.com/Funeoz)
- [@hinoshiba](https://gitlab.com/hinoshiba)
- [@IAmNewbie99](https://gitlab.com/IAmNewbie99)
- [@serval](https://gitlab.com/serval123)

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

#### New Kali MirrorsFirst, we have a new machine to host our tier-0 mirror archive.kali.org! The tier-0 mirror is the source from where all the other mirrors sync. This new machine has more bandwidth; we went from 500 Mb/s to 3 Gb/s, in other words we increased capacity by 6! In practical terms, it means mirrors will sync faster, which is especially relevant for “big syncs”, when a lot of new packages land in the repository at once. Faster mirror syncs means users get new packages faster, and it means smoother operations overall. This is a very welcome upgrade, long overdue!

Now, for the list of new Kali mirrors, this release cycle was again busy, we welcomed 6 new mirrors in Asia:

- China: [mirror.nju.edu.cn](https://mirror.nju.edu.cn/kali/), sponsored by the [eScience Center, Nanjing University](https://sci.nju.edu.cn/), thanks to YAO Ge.
- China: [mirror.nyist.edu.cn](https://mirror.nyist.edu.cn/kali/), sponsored by the [Nanyang Institute of Technology](https://www.nyist.edu.cn/), thanks to Palve.
- China: [mirrors.tuna.tsinghua.edu.cn](https://mirrors.tuna.tsinghua.edu.cn/kali/), sponsored by the [Tsinghua University](https://www.tsinghua.edu.cn/en/), thanks to Miao Wang.
- Japan: [mirror.tefexia.net](https://mirror.tefexia.net/kali/), sponsored by [Tefexia](https://www.tefexia.net/), thanks to Seungha Lee.
- South Korea: [mirror.jeonnam.school](https://mirror.jeonnam.school/kali/), sponsored by [Jeonnam High School](http://jeonnam.gen.hs.kr/), thanks to Wonchan Lee.
- South Korea: [mirror.zzunipark.com](https://mirror.zzunipark.com/kali/), sponsored by [zzuniMirror](https://homelab.zzunipark.com/), thanks to MinJun Park.

We also welcomed a pair of mirrors sponsored by [IONOS](https://www.ionos.com/), thanks to William Fleurant:

- Germany: [eu.mirror.ionos.com](https://eu.mirror.ionos.com/kali/)
- United States: [us.mirror.ionos.com](https://us.mirror.ionos.com/kali/)

If you have the disk space and bandwidth, [we always welcome new mirrors](https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/).

### Get Kali Linux 2025.3Fresh Images:
So what are you waiting for? Go [get Kali](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for those who are not, we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you will have fewer updates to do.
Just know that these are automated builds that we do, not QA like we do for our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~/
[...]

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2025.3. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2025.3"
VERSION_ID="2025.3"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Kali 6.12.38-1kali1 (2025-08-12)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.12.38+kali-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And Social networks are not bug trackers!

Want to keep up-to-date easier? We’ve got you!

- [Blog](https://www.kali.org/blog/)? Use our [RSS feed](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/)
- [Download](https://www.kali.org/get-kali/)? We have a [Torrent RSS feed](https://www.kali.org/torrents.xml)
- [Socials](https://www.kali.org/docs/community/list-of-official-kali-sites/#social-media-networks)? [Bluesky](https://bsky.app/profile/kalilinux.bsky.social), [Facebook](https://www.facebook.com/KaliLinux/), [Instagram](https://www.instagram.com/kalilinux/), [Mastodon](https://infosec.exchange/@kalilinux) & [X](https://x.com/kalilinux)

## 2025.2 – 2025-06-13

**Kali Linux 2025.2 Release (Kali Menu Refresh, BloodHound CE & CARsenal)**

Table of Contents
- [Desktop Updates](#desktop-updates)[Kali Menu Refresh](#kali-menu-refresh)
- [GNOME 48](#gnome-48)[New GNOME VPN IP Extension](#new-gnome-vpn-ip-extension)

- [KDE Plasma 6.3](#kde-plasma-63)
- [New Community Wallpapers](#new-community-wallpapers)

- [BloodHound Community Edition](#bloodhound-community-edition)
- [New Tools in Kali](#new-tools-in-kali)[Xclip pre-installed](#xclip-pre-installed)

- [Kali NetHunter Updates](#kali-nethunter-updates)[Smartwatch Wi-Fi Injection](#smartwatch-wi-fi-injection)
- [CARsenal](#carsenal)
- [Android Radio](#android-radio)
- [Kali NetHunter Kernels](#kali-nethunter-kernels)

- [Kali ARM SBC Updates](#kali-arm-sbc-updates)
- [Kali Website Updates](#kali-website-updates)[Kali Documentation](#kali-documentation)
- [Kali Blog Recap](#kali-blog-recap)

- [Kali Team Updates](#kali-team-updates)
- [Community Shout-Outs](#community-shout-outs)[The ROKFOSS initiative, by and for Korean users](#the-rokfoss-initiative-by-and-for-korean-users)
- [New Kali Mirrors](#new-kali-mirrors)

- [Miscellaneous](#miscellaneous)
- [Get Kali Linux 2025.2](#get-kali-linux-20252)

We’re almost half way through 2025 already, and we’ve got a lot to share with you in this release, Kali 2025.2.

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2025.1 release from March](https://www.kali.org/blog/kali-linux-2025-1-release/) is:

- [Desktop Updates](#desktop-updates) - Kali-Menu refresh, GNOME 48 & KDE 6.3 updates
- [BloodHound Community Edition](#bloodhound-community-edition) - Major upgrade with full set of ingestors
- [Kali NetHunter Smartwatch Wi-Fi Injection](#smartwatch-wi-fi-injection) - TicWatch Pro 3 now able to de-authenticate and capture WPA2 handshakes
- [Kali NetHunter CARsenal](#carsenal) - Car hacking tool set!
- [New Tools](#new-tools-in-kali) - 13 new shinny tools added (and various updates)

### Desktop Updates#### Kali Menu RefreshWe’ve completely reworked the Kali Menu! It’s now reorganized to follow the [MITRE ATT&CK framework](https://attack.mitre.org/) structure – which means that finding the right tool for your task should now be a lot more intuitive for red and blue teams alike.

Previously the Kali menu structure followed what was in BackTrack… which followed WHAX before it. The previous structure was an in-house item, [before MITRE was a thing](https://attack.mitre.org/resources/faq/).
When our menu was first created, there wasn’t as much design planning done, which we suffered for later. It meant that over time, scaling and adding new tools became difficult for us.
The knock on effect was that this made it harder for you, the end-users, to discover new tools as similar tools with overlapping functions were in different places or missing entries.
Yes, seasoned professionals may not use the menu to start up items, using shortcuts such as super key and typing the tool name, or via a terminal window. We see the menu as a way to discover tools.

The final nail in the coffin in the setup was the fact that it was manually managed. Yes, all those entries were previously created by-hand (which also may explain a few things).
As a result, we had stopped adding new tools to the menu… until now.

Now, we have created a new system and automated many aspects, making it easier for us to manage, and easier for you to discover items. Win win.
Over time, we hope to start to add this to [kali.org/tools/](https://www.kali.org/tools/).

Currently Kali Purple still follows [NIST CSF](https://www.nist.gov/cyberframework) (National Institute of Standards and Technology Critical Infrastructure Cybersecurity), rather than [MITRE D3FEND](https://d3fend.mitre.org/).

This is a big change, and we want your feedback! Think something should be renamed, moved, or see a tool that’s missing? Help us improve the menu by editing the structure directly — it’s all open and managed through a [simple YAML file](https://gitlab.com/kalilinux/packages/kali-menu/-/blob/kali/master/categories.yaml).

https://www.kali.org/blog/kali-linux-2025-2-release/images/kali-menu.png

#### GNOME 48GNOME has been bumped up to version 48, and brings with it:

- Notification Stacking
- Performance Improvements
- Dynamic triple buffering
- Enhanced Image Viewer
- Digital Wellbeing
- Preserve Battery Health
- HDR (High Dynamic Range) Support
- Updated Text Editor

https://www.kali.org/blog/kali-linux-2025-2-release/images/gnome-48.png

As with previous GNOME updates in Kali, we’ve given all our themes a fresh coat of paint – everything’s been tuned to look sharp and feel smooth. The document reader evince has been replaced with the new papers app. If you’re rocking Kali with GNOME, this update is definitely worth the reboot. Want the full scoop? Check out the [official GNOME 48 release notes](https://release.gnome.org/48/).

##### New GNOME VPN IP ExtensionJust like we did for Xfce back in [Kali 2024.1](https://www.kali.org/blog/kali-linux-2024-1-release/#xfce), we’ve now brought the VPN IP indicator to GNOME too!

It shows the IP address of your current VPN connection right in the panel — and with a simple click, it copies it straight to your clipboard. Handy, right?

https://www.kali.org/blog/kali-linux-2025-2-release/images/gnome-vpn-extension.png

Huge thanks to [@Sarthak Priyadarshi](https://github.com/sarthakpriyadarshi/) who not only came up with the idea, but also provided all of the coding to make it happen. Community contributions like this make Kali better for everyone!

#### KDE Plasma 6.3KDE Plasma fans, rejoice – we’ve included Plasma 6.3, and it’s packed with polish:

- Huge overhaul of fractional scaling
- Accurate screen colors when using the Night Light
- More accurate CPU usage in system sonitor
- Info Center provides more information, like GPUs data or batteries’ cycle counts
- More customization features

https://www.kali.org/blog/kali-linux-2025-2-release/images/plasma-6.3.png

Whether you’re into tiling window madness or prefer a traditional desktop setup, Plasma 6.3 brings both flexibility and style. You can read more about all the new changes for Plasma desktop in their [official release post](https://kde.org/announcements/plasma/6/6.3.0/).

#### New Community WallpapersThere are also new changes in the [Community Wallpapers](https://www.kali.org/wallpapers/community/) package ([pkg](https://pkg.kali.org/pkg/kali-community-wallpapers)), including 2 new backgrounds provided by [@Onix32032044](https://x.com/Onix32032044) and 1 background provided by [@Arszilla](https://gitlab.com/Arszilla).

To access these wallpapers, simply install the kali-community-wallpapers package, which also offers many other stunning backgrounds created by our community contributors.

https://www.kali.org/wallpapers/community/

### BloodHound Community EditionIf you’re doing Active Directory recon, this upgrade is a game changer. BloodHound just got a major upgrade – we’ve bumped it up to the latest version: BloodHound Community Edition (CE). With this update, we’re also shipping the full set of ingestors to support it:

- [azurehound](https://www.kali.org/tools/azurehound/)
- [bloodhound-ce-python](https://www.kali.org/tools/bloodhound-ce-python/)
- [sharphound](https://www.kali.org/tools/sharphound/)

Heads up: bloodhound-ce-python is the ingestor made specifically for BloodHound CE.
Don’t mix it up with the old bloodhound-python, which only work with the legacy version.

So what’s new in BloodHound CE? Expect a smoother interface, better performance, and new capabilities for mapping complex Active Directory environments.

You can check our guide about how to configure a new installation of Bloodhound-CE in Kali [here](https://www.kali.org/tools/bloodhound/).

https://www.kali.org/blog/kali-linux-2025-2-release/images/bloodhound.png

### New Tools in KaliIt would not be a Kali release if there were not any new tools added! A quick run down of what has been added (to the network repositories):

- [azurehound](https://www.kali.org/tools/azurehound/) - BloodHound data collector for Microsoft Azure
- [binwalk3](https://www.kali.org/tools/binwalk3/) - Firmware Analysis Tool
- [bloodhound-ce-python](https://www.kali.org/tools/bloodhound-ce-python/) - Python based ingestor for BloodHound CE
- [bopscrk](https://www.kali.org/tools/bopscrk/) - Generate smart and powerful wordlists
- [chisel-common-binaries](https://www.kali.org/tools/chisel-common-binaries/) - Prebuilt binaries for chisel
- [crlfuzz](https://www.kali.org/tools/crlfuzz/) - Fast tool to scan CRLF vulnerability written in Go (Submitted by [@Arszilla](https://gitlab.com/Arszilla))
- [donut-shellcode](https://www.kali.org/tools/donut-shellcode/) - Generates position-independent shellcode from memory and runs them
- [gitxray](https://www.kali.org/tools/gitxray/) - Scan GitHub repositories and contributors to collect data (Submitted by [@weirdlantern](https://gitlab.com/weirdlantern/))
- [ldeep](https://www.kali.org/tools/ldeep/) - In-depth LDAP enumeration utility
- [ligolo-ng-common-binaries](https://www.kali.org/tools/ligolo-ng-common-binaries/) - Prebuilt binaries for Advanced ligolo-ng
- [rubeus](https://www.kali.org/tools/rubeus/) - Raw Kerberos interaction and abuses
- [sharphound](https://www.kali.org/tools/sharphound/) - BloodHound CE collector
- [tinja](https://www.kali.org/tools/tinja/) - CLI tool for testing web pages for template injection

There has also been numerous new libraries as well as packages updates as well, such as PowerShell and [code-oss](https://pkg.kali.org/pkg/code-oss).

#### Xclip pre-installedWe’ve added [xclip](https://www.kali.org/tools/xclip/) by default across all desktop environments in Kali.

Why? Because being able to quickly send output to the clipboard from the terminal is incredibly useful — especially during reporting, note-taking, or sharing on-the-fly.

Here are a few quick examples:

┌──(kali㉿kali)-[~/Downloads]
└─$ ip a | grep inet | xclip -selection clipboard

Boom — now your IP info is in your clipboard, ready to paste.

Or maybe you’ve just cracked a hash and want to copy the flag:

┌──(kali㉿kali)-[~/Downloads]
└─$ grep FLAG crackme.txt | xclip -sel c

# Or pass it to the next command
┌──(kali㉿kali)-[~/Downloads]
└─$ xclip -o -sel c | grep FLAG

No more mouse highlighting or right-click gymnastics. Just pipe it to xclip and paste wherever you need. Small tool, big quality-of-life boost.

### Kali NetHunter Updates#### Smartwatch Wi-Fi Injectionhttps://www.kali.org/blog/kali-linux-2025-2-release/images/nethunter-watch.jpg

After 3 years, we are proud to introduce the first actual smartwatch that finally has wireless injection support! Thanks to the exceptional collaboration by [@yesimxev](https://gitlab.com/yesimxev) and [@Jakob Link](https://github.com/jlinktu) from [NexMon](https://github.com/seemoo-lab/nexmon) team. Countless emails, lost brain cells, but it was worth it. Now Kali NetHunter on the TicWatch Pro 3 (all variants with bcm43436b0 chipset) supports wireless injection, de-authentication, and able to capture WPA2 handshakes! Check out the [install guide](https://forums.kali.org/t/hijacker-on-ticwatch-pro-3-with-wireless-injection/6242).

#### CARsenalCAN Arsenal come with a new version by [@V0lk3n](https://gitlab.com/V0lk3n). It is now renamed as CARsenal, to better match the goal which is to provide a car hacking tool set.

Code got a lot of rewrite, and provide a more friendly UI.

Also it come with new tools such as:

- hlcand: Modified slcand for ELM327 use
- VIN Info: Decode your VIN identifier
- CaringCaribou: Actually provide Listener, Dump, Fuzzer, Send, UDS and XCP modules
- ICSim: Provide a great simulator to play with VCAN and test CARsenal toolset without hardware needed

Actual kernel with CAN support enabled:

- Samsung Galaxy S9 (A13/exynos9810)
- Samsung Galaxy S10 (A14 & A15/exynos9820)
- (NEW!) Realme C15 (A10)
- (NEW!) Redmi Note 11 (A15)

Its [documentations](https://www.kali.org/docs/nethunter/nethunter-carsenal/) and [kernel configuration](https://www.kali.org/docs/nethunter/nethunter-kernel-9-config-8/) has been updated as well.

#### Android Radiohttps://www.kali.org/blog/kali-linux-2025-2-release/images/nethunter-car-radio.png

There’s another possibly first use case of Kali NetHunter KeX running on Android radio. A teaser to the upcoming Android Auto support…

#### Kali NetHunter Kernels[Kali NetHunter kernels](https://nethunter.kali.org/kernels.html) updates:

- (NEW!) Xiaomi Redmi 4/4X (A13) (by [@MomboteQ](https://gitlab.com/momboteq))
- (NEW!) Xiaomi Redmi Note 11 (A15) (by [@Madara273](https://gitlab.com/Madara273))
- Updated Realme C15 (A10) (by [@Frostleaft07](https://gitlab.com/Frostleaft07))
- Updated Samsung Galaxy S10 (A14,A15/exynos9820) (by [@V0lk3n](https://gitlab.com/V0lk3n))
- Updated Samsung Galaxy S9 (A13/exynos9810) (by [@V0lk3n](https://gitlab.com/V0lk3n))

### Kali ARM SBC UpdatesWe will start off with some Raspberry Pi updates:

- We have combined some of our Raspberry Pi images, so that Raspberry Pi 5 does not need its own separate image . It is now supported by our 64-bit image! This is reflected by the new name of the download link on [get-kali](https://www.kali.org/get-kali/).
- Raspberry Pi devices have had their kernel upgraded to a 6.12 based kernel. This was made possible thanks to [@Nurse Jackass](https://gitlab.com/nursejackass) who add support to the brcmfmac nexmon driver.
- Additionally, the udev rule that used to allow you to run vgencmd without requiring root rights on Raspberry Pi devices was updated, so you no longer need elevated privileges to run it.

Now onto some USB Armory MKII:

- It also has had its kernel upgraded to a 6.12 based kernel.
- The bootloader upgraded to 2025.04.

PowerShell on the ARM images has been bumped from 7.1.3 to 7.5.1

[Build-scripts](https://gitlab.com/kalilinux/build-scripts/kali-arm):

- Mirror replacement is fixed, so if you want to build a custom image pointing at a specific mirror, just follow the instructions in the README
- Occasionally there would be a build failure with no output. This was tracked down to the limit_cpu function and has been fixed so we no longer swallow the error code when there is one, and pass it on so when a failure happens we can know why.

### Kali Website Updates
- [Kali Linux Community and Support](https://www.kali.org/community/)
- [Meet The Kali Team](https://www.kali.org/about-us/)

#### Kali DocumentationOur [Kali documentation](https://www.kali.org/docs/) has had various updates to existing pages as well as new pages:

- [Adding Encrypted Persistence to a Kali Linux Live USB Drive](https://www.kali.org/docs/usb/usb-persistence-encryption/) (updated)
- [Adding Persistence to a Kali Linux Live USB Drive](https://www.kali.org/docs/usb/usb-persistence/) (updated)
- [Fixing PostgreSQL ‘collation version mismatch’](https://www.kali.org/docs/troubleshooting/postgresql-collation-mismatch-error/) (new)
- [Installing NetHunter on the OnePlus 5T](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-oneplus-5t/) (new by [@Güray Çakmak](https://gitlab.com/i-liek-turtals))
- [Installing NetHunter on the Xiaomi Mi A3](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-xiaomi-mi-a3/) (new by [@mr00k3](https://gitlab.com/mr00k3))
- [Making a Kali Bootable USB Drive (Linux)](https://www.kali.org/docs/usb/live-usb-install-with-linux/) (updated)
- [Making a Kali Bootable USB Drive (macOS/OS X)](https://www.kali.org/docs/usb/live-usb-install-with-mac/) (updated)
- [NetHunter Wardriving](https://www.kali.org/docs/nethunter/nethunter-wardriving/) (new by [@Alex](https://gitlab.com/gh0stbuster))
- [Official Kali Linux Sites](https://www.kali.org/docs/community/list-of-official-kali-sites/) (updated)
- [Raspberry Pi 1 (Original)](https://www.kali.org/docs/arm/raspberry-pi/) (updated)
- [Raspberry Pi 2 v1.2](https://www.kali.org/docs/arm/raspberry-pi-64-bit/) (updated)
- [Raspberry Pi 2](https://www.kali.org/docs/arm/raspberry-pi-2/) (updated)
- [Raspberry Pi 3](https://www.kali.org/docs/arm/raspberry-pi-3/) (updated)
- [Raspberry Pi 400](https://www.kali.org/docs/arm/raspberry-pi-400/) (updated)
- [Raspberry Pi 4](https://www.kali.org/docs/arm/raspberry-pi-4/) (updated)
- [Raspberry Pi 5](https://www.kali.org/docs/arm/raspberry-pi-5/) (updated)
- [Raspberry Pi Zero](https://www.kali.org/docs/arm/raspberry-pi-zero/) (updated)
- [Raspberry Pi Zero W](https://www.kali.org/docs/arm/raspberry-pi-zero-w/) (updated)
- [Raspberry Pi Zero 2 W](https://www.kali.org/docs/arm/raspberry-pi-zero-2-w/) (updated)
- [Verifying USB Write](https://www.kali.org/docs/usb/verify-usb-write/) (new by [@serval](https://gitlab.com/serval123))
- [Where and How to Contribute to Kali](https://www.kali.org/docs/community/contribute/) (updated)

#### Kali Blog RecapSince our last release, we did the following [blog posts](https://www.kali.org/blog/):

- [A New Kali Linux Archive Signing Key](https://www.kali.org/blog/new-kali-archive-signing-key/)

### Kali Team UpdatesIt’s also with a heavy heart to announce that both [@elwood](https://mastodon.social/@_elwood_) as well as [@gamb1t](https://gitlab.com/Gamb1t) have stepped down and are no longer part of the [Kali team](https://www.kali.org/about-us/). We hope you join us in wishing them all the best with their adventures going forward.
@elwood has been part of Kali before it was called Kali and @gamb1t joined the team back in 2019. Both of them were very active and well known in Kali’s history as well as community.

[Shubham Vishwakarma (@shubhamvis98)](https://bsky.app/profile/shubhamvis98.bsky.social) has been doing a lot of heavy lifting with Kali NetHunter Pro since the start and has now fully joined the team.

[@v0lk3n](https://infosec.exchange/@v0lk3n) has now been active and passionate for a while, with his work and efforts into the project it makes sense for him to have joined the Kali NetHunter team.

Please welcome [@Aura](https://infosec.exchange/@graylsidus), [James Green (@greenjam94)](https://infosec.exchange/@Greenjam94) and [@Tristram](https://github.com/gh0x0st) as Kali’s Community Leaders! You will see them in various places, such as our real-time chat and forums. Come and say hi to them.

### Community Shout-OutsThese are people from the public who have helped Kali and the team for the last release. We want to praise them for their work (we like to give credit where due!):

- [@Alex](https://gitlab.com/gh0stbuster)
- [@Arszilla](https://gitlab.com/Arszilla)
- [@chewbaqa](https://gitlab.com/Vishal)
- [@Data 19C](https://gitlab.com/Data_19C)
- [@florent4014](https://gitlab.com/florent4014)
- [@Frostleaf](https://gitlab.com/Frostleaft07)
- [@Güray Çakmak](https://gitlab.com/i-liek-turtals)
- [@Kimo Coder](https://gitlab.com/k1m0cod3r)
- [@Kyle Olmstead](https://gitlab.com/k.olmstead)
- [@Madara273](https://gitlab.com/Madara273)
- [@MomboteQ](https://gitlab.com/momboteq)
- [@mr00k3](https://gitlab.com/mr00k3)
- [@Nurse Jackass](https://gitlab.com/nursejackass)
- [@serval](https://gitlab.com/serval123)
- [@SkyW4r33x](https://gitlab.com/SkyW4r33x)
- [@soffensive](https://gitlab.com/soffensive)
- [@V0lk3n](https://gitlab.com/V0lk3n)
- [@Volodymyr BOBER](https://gitlab.com/bv3)
- [@x](https://gitlab.com/xenix4845)

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

#### The ROKFOSS initiative, by and for Korean usersIn South Korea, a group of users that go by the name of [ROKFOSS](https://krfoss.org/) have been very active lately. Over the last few months, they have helped to setup new Kali Linux mirrors, and we now have a total of 6 mirrors in this country thanks to their support.

But the initiative goes further: they now provide a translation of the [Kali Linux documentation in Korean](https://kali.krfoss.org), along with a [chat instance](https://chat.krfoss.org/).

Big thanks for this initiative!

#### New Kali MirrorsWe added 2 new mirrors to the pool during this release cycle:

- India: [mirror.del2.albony.in](https://mirror.del2.albony.in/kali-images/), sponsored by [Albony Network](https://albony.in/) and thanks to Shrirang Kahale.
- South Korea: [mirror.hemino.net](https://mirror.hemino.net/kali/), thanks to “QuietSky”.

If you have the disk space and bandwidth, [we always welcome new mirrors](https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/).

### MiscellaneousBelow are a few other things which have been updated in Kali, which we are calling out which do not have as much detail:

- Community post: [What I Learned About Kali Purple Hub, MALCOLM, and Autopilot at Black Hat Asia 2025](https://medium.com/@yzw.joe/what-i-learned-about-kali-purple-hub-malcolm-and-autopilot-at-black-hat-asia-2025-89bf697559b2)
- Community post: [[KDE] My first rice](https://www.reddit.com/r/unixporn/comments/1k6bg0l/kde_my_first_rice/#lightbox)
- Community post: Kali on Pi4 [Cyberdeck - Triskel_mk1](https://www.thingiverse.com/thing:7010296)
- Community post: [NetHunter C-deck](https://hackaday.io/project/203116-nethunter-c-deck)
- Kali is now on [Bluesky, @kalilinux.bsky.social](https://bsky.app/profile/kalilinux.bsky.social)
- Kali is now on [PeerTube, [email protected]](https://video.infosec.exchange/c/kalilinux/videos)
- We updated our [preseed examples repos](https://gitlab.com/kalilinux/recipes/kali-preseed-examples)
- These changes are all the public items, if you would like a peak behind the curtain to see other items we have been working on check out GitLab [activity](https://gitlab.com/groups/kalilinux/-/activity) and [milestones](https://gitlab.com/groups/kalilinux/-/milestones/28)

### Get Kali Linux 2025.2Fresh Images:
So what are you waiting for? Go [get Kali](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for those who are not, we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you will have fewer updates to do.
Just know that these are automated builds that we do, not QA like we do for our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
[...]

┌──(kali㉿kali)-[~]
└─$ sudo wget https://archive.kali.org/archive-keyring.gpg -O /usr/share/keyrings/kali-archive-keyring.gpg
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~/
[...]

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

Do make sure your [kali-archive-keyring has been updated](https://www.kali.org/blog/new-kali-archive-signing-key/).

You should now be on Kali Linux 2025.2. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION_ID="2025.2"
VERSION="2025.2"
VERSION_CODENAME=kali-rolling

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Kali 6.12.25-1kali1 (2025-04-30)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.12.25-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And Social networks are not bug trackers!

Want to keep up-to-date easier? We’ve got you!

- [Blog](https://www.kali.org/blog/)? Use our [RSS feed](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/)
- [Download](https://www.kali.org/get-kali/)? We have a [Torrent RSS feed](https://www.kali.org/torrents.xml)
- [Socials](https://www.kali.org/docs/community/list-of-official-kali-sites/#social-media-networks)? [Bluesky](https://bsky.app/profile/kalilinux.bsky.social), [Facebook](https://www.facebook.com/KaliLinux/), [Instagram](https://www.instagram.com/kalilinux/), [Mastodon](https://infosec.exchange/@kalilinux) & [X](https://x.com/kalilinux)

## 2025.1 – 2025-03-19

**Kali Linux 2025.1a Release (2025 Theme, & Raspberry Pi)**

Table of Contents
- [2025 Theme Refresh](#2025-theme-refresh)
- [Desktop Environments](#desktop-environments)[KDE Plasma 6.2](#kde-plasma-62)
- [Xfce 4.20](#xfce-420)

- [Raspberry Pi](#raspberry-pi)
- [Kali NetHunter Updates](#kali-nethunter-updates)
- [New Tools in Kali](#new-tools-in-kali)
- [Miscellaneous](#miscellaneous)
- [Kali Website Updates](#kali-website-updates)[Kali Documentation](#kali-documentation)
- [Kali Blog Recap](#kali-blog-recap)

- [Community Shout-Outs](#community-shout-outs)[New Kali Mirrors](#new-kali-mirrors)

- [Get Kali Linux 2025.1a](#get-kali-linux-20251a)

We are kicking off 2025 with Kali Linux 2025.1a! This update builds on existing features, bringing enhancements and improvements to streamline your experience. It is now available to [download](https://www.kali.org/get-kali/) or [upgrade if you’re already running Kali Linux](https://www.kali.org/docs/general-use/updating-kali/).
Kali Linux 2025.1a? What happened to 2025.1? There was a last minute bug discovered in a package after already producing our images. As a result, a re-build was needed, with a fix.

Here is a recap of the [changelog](https://bugs.kali.org/changelog_page.php) since our [December 2024.4 release](https://www.kali.org/blog/kali-linux-2024-4-release/):

- [2025 Theme Refresh](#2025-theme-refresh) - Our yearly theme refresh
- Desktop Environment Updates - [KDE Plasma 6.2](#kde-plasma-62) & [Xfce 4.20](#kde-plasma-62)
- [Raspberry Pi](#raspberry-pi) - New major kernel
- [Kali NetHunter CAN](#kali-nethunter-updates) - Car hacking in your pocket
- [Packages](#new-tools-in-kali) - Various new packages added & numerous packages updated

### 2025 Theme RefreshJust like our previous releases, the first one of the year, 20xx.1, has our annual theme refresh, a tradition that keeps our interface as modern as our tools. This year, we are excited to unveil our latest theme, thoughtfully designed to enhance the user experience from the moment you start up. Expect notable updates to the boot menu, login screen, and a stunning selection of desktop wallpapers for both Kali and Kali Purple editions. Our commitment extends beyond cybersecurity advancements; we strive to ensure that our platform’s aesthetics are just as impressive as its capabilities.

Boot Menu:

https://www.kali.org/blog/kali-linux-2025-1-release/images/kali-linux-boot-theme.png

Login Display:

https://www.kali.org/blog/kali-linux-2025-1-release/images/kali-linux-2025-login.png

Desktop:

https://www.kali.org/blog/kali-linux-2025-1-release/images/kali-linux-2025-desktop.png

Kali Purple Desktop:

https://www.kali.org/blog/kali-linux-2025-1-release/images/kali-linux-2025-desktop-purple.png

New Wallpapers:

https://www.kali.org/blog/kali-linux-2025-1-release/images/kali-linux-2025-wallpapers.png

There are also new changes in the Community Wallpapers package, including 1 new background provided by [Onix32032044](https://x.com/Onix32032044) and 2 backgrounds that were not included in the default theme refresh.

To access these wallpapers, simply install the kali-community-wallpapers package, which also offers many other stunning backgrounds created by our community contributors.

https://www.kali.org/blog/kali-linux-2025-1-release/images/kali-linux-community-wallpapers.png

### Desktop Environments#### KDE Plasma 6.2After a long wait, we are excited to announce that Plasma 6 is finally available in Kali, specifically version 6.2. This is a major update, as the previous version included in Kali was Plasma 5.27, making the scope of changes difficult to summarize. For a more in-depth look at each release, check out the official announcements: [6.0](https://kde.org/announcements/megarelease/6/), [6.1](https://kde.org/announcements/plasma/6/6.1.0/), and [6.2](https://kde.org/announcements/plasma/6/6.2.0/).

On our end, we have updated all themes to align with the new environment, featuring refreshed window and desktop visuals. And our favorite new addition from KDE? Floating panels!

https://www.kali.org/blog/kali-linux-2025-1-release/images/kali-linux-2025-plasma.png

#### Xfce 4.20Our default desktop environment, Xfce, has also had a [minor software bump](https://alexxcons.github.io/blogpost_14.html) from 4.18 to [4.20](https://xfce.org/download/changelogs/4.20/). Two years of development has gone this, which was formally released on December 15, 2024. It is the stable series follow-up to the Xfce 4.18 release that made its debut during Christmas of 2022 (Kali 2023.1).

https://www.kali.org/blog/kali-linux-2025-1-release/images/kali-linux-xfce-4-20.png

New keyboard shortcuts:

To enhance the experience for users transitioning from other operating systems, we have added a few extra keyboard shortcuts to make desktop navigation even faster:

- Ctrl + Alt + F: File Manager
- Super + E: File Manager
- Super + F: File Manager
- Super + R: Run Command (in addition to the previous shortcut Alt + F2)
- Super + T: Open Terminal (in addition to the previous shortcut Ctrl + Alt + T)
- Super + W: Open Browser
- Super + F1: Find Cursor
- Super + D: Show Desktop (in addition to the previous shortcut Ctrl + Alt + D)

Window Manager shortcuts:

- Super + Shift + Down: Move window to monitor down
- Super + Shift + Up: Move window to monitor up
- Super + Shift + Left: Move window to monitor left
- Super + Shift + Right: Move window to monitor right
- Super + KeyPad_1: Tile window down left
- Super + KeyPad_3: Tile window down right
- Super + KeyPad_7: Tile window up left
- Super + KeyPad_9: Tile window up right

You can check all the other Xfce keyboard shortcuts in the keyboard settings dialog or in the XFWM4 keyboard section.

https://www.kali.org/blog/kali-linux-2025-1-release/images/kali-linux-xfce-shortcuts.png

### Raspberry PiThere has been various Raspberry Pi image changes for 2025.1a:

A newer package, raspi-firmware, is now being used.
We now use the same raspi-firmware package as Raspberry Pi OS.

A new kernel, which is based on version 6.6.74 and is now from the Raspberry Pi OS kernel.
It is now included in all our images, including support for the Raspberry Pi 5!

The new kernel packages are:

- linux-image-rpi-2712 - arm64 kernel for the Raspberry Pi 5/500
- linux-image-rpi-v8 - arm64 kernel for the Raspberry Pi 02W/2/3/4/400
- linux-image-rpi-v7l - armhf kernel for the Raspberry Pi 02W/4/400
- linux-image-rpi-v7 - armhf kernel for the Raspberry Pi 2/3
- linux-image-rpi-v6 - armel kernel for the Raspberry Pi 0/0W/1

The respective header packages are linux-headers-rpi-2712, linux-headers-rpi-v8, linux-headers-rpi-v7l, linux-headers-rpi-v7, and linux-headers-rpi-v6.
These headers come pre-installed on the Raspberry Pi images that we build.
Additionally, 64-bit images include both 2712 and v8, while 32-bit images include v7l and v7.

The Nexmon kernel module is now DKMS-enabled and available as [brcmfmac-nexmon-dkms](https://pkg.kali.org/pkg/brcmfmac-nexmon-dkms), allowing it to be updated separately from the kernel.
However, the Nexmon firmware is not included in this release.
We are still evaluating the best approach to manage firmware updates with minimal disruption and will include it in a future update.

A new partition layout is introduced, mirroring Raspberry Pi OS images.
The first (vfat) partition is now mounted at /boot/firmware instead of /boot.
This means that if you need to modify config.txt, you should now edit /boot/firmware/config.txt.
Similarly, for changes to the kernel command line, edit /boot/firmware/cmdline.txt.
A /boot/config.txt file is included as a reference, containing a warning and pointing to the correct location.

Speaking of config.txt, it has now been simplified, as the newer boot firmware handles many tasks automatically.

There are a lot of changes that have happened under the hood, and as such, 2025.1a for Raspberry Pi devices means starting over from a new image, and not just following our [update documentation](https://www.kali.org/docs/general-use/updating-kali/).
If you are happy with your current setup on the 5.15 kernel, updating will not break anything, as the new packages will not be installed by an update, but we highly recommend starting with a fresh image as we do not support upgrading to the new kernels.

### Kali NetHunter Updateshttps://www.kali.org/blog/kali-linux-2025-1-release/images/cankali.png

We also have some fascinating Kali NetHunter updates for this release. Straight out of the blue, [V0lk3n](https://gitlab.com/V0lk3n) added the all new “CAN Arsenal” tab to [NetHunter app](https://store.nethunter.com/packages/com.offsec.nethunter/) so you can now have a car hacked straight from your pocket!
He also added brand new kernels for Samsung phones, with successfully ported Samsung HID patch, which has not work since the Samsung Galaxy S7.

Our installer now comes with a dynamic wallpaper thanks to [Robin](https://gitlab.com/MrRob0-X). Therefore, if you want to add a new device with a unique resolution, you will not need to port an existing wallpaper. There are additionally various bug fixes from [yesimxev](https://gitlab.com/yesimxev), [Robin](https://gitlab.com/MrRob0-X), and [g0tmi1k](https://gitlab.com/g0tmi1k)

We appreciate all the support coming from unofficial threads and our official [Discord server](https://discord.kali.org/). It is amazing how everyone helps each other out. This project really would not work without you!

New [Kali NetHunter kernels](https://nethunter.kali.org/kernels.html):

- Samsung Galaxy S9 (Exynos9810 - LineageOS 20/Android 13) - Thanks [V0lk3n](https://gitlab.com/V0lk3n)
- Samsung Galaxy S10 (Exynos9820 - LineageOS 21 & LineageOS 22.1) - Thanks [V0lk3n](https://gitlab.com/V0lk3n)
- Xiaomi Redmi Note 6 Pro (Android 11) - Thanks [TheKidBaby](https://gitlab.com/TheKidBaby)

### New Tools in KaliThis release, there has been more of a focus on updating packages. We also bump the Kali kernel to 6.12.
Still, a Kali release would not be complete without something new being added (to the network repositories):

- [hoaxshell](https://www.kali.org/tools/hoaxshell/) - Windows reverse shell payload generator and handler that abuses the http(s) protocol to establish a beacon-like reverse shell

### MiscellaneousBelow are a few other things which have been updated in Kali, which we are calling out which do not have as much detail:

- Split live-config build-script into [kali-installer](https://gitlab.com/kalilinux/build-scripts/kali-installer) & [kali-live](https://gitlab.com/kalilinux/build-scripts/kali-live)
- We are hoping to refresh Kali-menu in 2025.2

### Kali Website UpdatesWe have added 3x new pages to [kali.org](https://www.kali.org/):

- [Official Kali Linux Wallpapers](https://www.kali.org/wallpapers/) - Kali 2019.4 and onwards
- [Legacy Kali Linux Wallpapers](https://www.kali.org/wallpapers/legacy/) - BackTrack to Kali 2019.3
- [Community Kali Linux Wallpapers](https://www.kali.org/wallpapers/community/) - Our fantastic users creations

https://www.kali.org/blog/kali-linux-2025-1-release/images/kali-www-wallpapers.png

#### Kali DocumentationOur [Kali documentation](https://www.kali.org/docs/) has had various updates to existing pages as well as new pages:

- [Configuring the Kernel - CAN](https://www.kali.org/docs/nethunter/nethunter-kernel-9-config-8/) (new)
- [NetHunter CAN-Arsenal](https://www.kali.org/docs/nethunter/nethunter-carsenal/) (new)
- [NetHunter Pro - Enable OTG in SDM845 (OnePlus6/6T and POCO F1)](https://www.kali.org/docs/nethunter-pro/enable-otg-sdm845/) (new)

#### Kali Blog RecapSince our last release, we did the following [blog posts](https://www.kali.org/blog/):

- [Kali Linux On The New Modern WSL](https://www.kali.org/blog/kali-linux-modern-wsl/)

### Community Shout-OutsThese are people from the public who have helped Kali and the team for the last release.
And we want to praise them for their work (we like to give credit where due!):

Kali Documentation:

- [@V0lk3n](https://gitlab.com/V0lk3n)

Kali Forums:

- @barry99705
- @Eris2Cats
- @Fred
- @Serval
- @ShadowKhan

Kali Community Wallpapers:

- [@Onix32032044](https://x.com/Onix32032044)

Packaging:

- [@hogezero](https://gitlab.com/hogezero)
- [@X0RW3LL](https://gitlab.com/X0RW3LL)

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

#### New Kali MirrorsWe have some new mirrors!
As often, listing it takes us on a trip around the world.

First, in Asia, we get 6 new mirrors:

- Japan: [mirror.hashy0917.net](https://mirror.hashy0917.net/kali/), thanks to [hashy0917](https://www.hashy0917.net/).
- Nepal: [mirrors.nepalicloud.com](https://mirrors.nepalicloud.com/kali-images/), sponsored by [Nepali Cloud](https://nepalicloud.com/) and thanks to Arun Kumar Pariyar - our first mirror in Nepal!
- Singapore: [mirror.sg.gs](https://mirror.sg.gs/kali/), sponsored by [SG.GS](https://sg.gs/) and thanks to Amos.
- South Korea: [mirror2.amuksa.com](https://mirror2.amuksa.com/kali/), sponsored by [daxnet](https://mirror.amuksa.com/).
- South Korea: [mirror.keiminem.com](https://mirror.keiminem.com/kali/), sponsored by [Keiminem](https://keiminem.com/).
- South Korea: [mirror.techlabs.co.kr](https://mirror.techlabs.co.kr/kali/), sponsored by [TechLabs](https://www.techlabs.co.kr/) and thanks to Eric Kim.

Then in Europe, and thanks to the amazing Marc Gómez, we get 3 new mirrors in the following countries:

- Netherlands: [mirror.nl.cdn-perfprod.com](https://mirror.nl.cdn-perfprod.com/kali/).
- Romania: [mirror.ro.cdn-perfprod.com](https://mirror.ro.cdn-perfprod.com/kali/), sponsored by [iHostART](https://www.ihostart.com) - our first mirror in Romania!
- Spain: [mirror.es.cdn-perfprod.com](https://mirror.es.cdn-perfprod.com/kali/), sponsored by Marc himself - our first mirror in Spain!

Finally, 2 more mirrors in Europe and Eastern Europe:

- Azerbaijan: [mirror.ourhost.az](https://mirror.ourhost.az/kali/), sponsored by [OUR.Host](https://ourhost.az/en/) and thanks to Orkhan Guliyev.
- Denmark: [mirror.it-privat.dk](https://mirror.it-privat.dk/kali/), thanks to [Daniel Ytterdal](https://ytterdal.dk).

That is a total of 11 new mirrors!
Huge thanks to the community for helping us distribute Kali everywhere in the world <3.

As always, if you have the disk space and bandwidth, [we always welcome new mirrors](https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/).

### Get Kali Linux 2025.1aFresh Images:
So what are you waiting for? Go [get Kali](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for those who are not, we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you will have fewer updates to do.
Just know that these are automated builds that we do, not QA like we do for our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~/
[...]

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2025.1a. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2025.1"
VERSION_ID="2025.1"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Kali 6.12.13-1kali1 (2025-02-11)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.12.13-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And Social networks are not bug trackers!

Want to keep up-to-date easier? We’ve got you!

- [Blog](https://www.kali.org/blog/)? Use our [RSS feeds](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/)
- Download? We have a [Torrent RSS feed](https://www.kali.org/torrents.xml)
- Socials? [Facebook](https://www.facebook.com/KaliLinux/), [Instagram](https://www.instagram.com/kalilinux/), [Mastodon](https://infosec.exchange/@kalilinux) & [X/Twitter](https://x.com/kalilinux)

## 2024.4 – 2024-12-16

**Kali Linux 2024.4 Release (Python 3.12, Goodbye i386, Raspberry Pi Imager & Kali NetHunter)**

Table of Contents
- [A New Python Version: 3.12](#a-new-python-version-312)
- [The End Of The i386 Kernel And Images](#the-end-of-the-i386-kernel-and-images)
- [Deprecations In The SSH Client: DSA keys](#deprecations-in-the-ssh-client-dsa-keys)
- [Raspberry Pi Imager Customizations Support](#raspberry-pi-imager-customizations-support)[How Does It Work?](#how-does-it-work)
- [Default Settings For Non-Customized Images](#default-settings-for-non-customized-images)

- [GNOME 47](#gnome-47)
- [Kali Forums Refresh](#kali-forums-refresh)
- [New Tools In Kali](#new-tools-in-kali)
- [Kali NetHunter Updates](#kali-nethunter-updates)[App](#app)
- [Store](#store)
- [Installer](#installer)
- [Website](#website)
- [Kernel/Device](#kerneldevice)
- [Package](#package)

- [Kali NetHunter Pro Updates](#kali-nethunter-pro-updates)
- [Kali ARM SBC Updates](#kali-arm-sbc-updates)
- [Kali Website Updates](#kali-website-updates)[Kali Documentation](#kali-documentation)
- [Kali Blog Recap](#kali-blog-recap)

- [Community Shout-Outs](#community-shout-outs)
- [Miscellaneous](#miscellaneous)
- [Get Kali Linux 2024.4](#get-kali-linux-20244)

Just before the year starts to wrap up, we are getting the final 2024 release out! This contains a wide range of updates and changes, which are in already in effect, ready for immediate [download](https://www.kali.org/get-kali/), or [updating](https://www.kali.org/docs/general-use/updating-kali/).

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2024.3 release from September](https://www.kali.org/blog/kali-linux-2024-3-release/) is:

- [Python 3.12](#a-new-python-version-312) - New default Python version (Au revoir pip, hello [pipx](https://pipx.pypa.io/stable/))
- [The End Of The i386 Kernel and Images](#the-end-of-the-i386-kernel-and-images) - Farewell x86 (images), but not goodbye (packages)
- [Deprecations in the SSH Client: DSA keys](#deprecations-in-the-ssh-client-dsa-keys) - Reminder about using ssh1 if required
- [Raspberry Pi Imager Customizations Support](#raspberry-pi-imager-customizations-support) - Able to alter settings at write time
- [GNOME 47](#gnome-47) - Now able to synchronize your favorite colors
- [Kali Forums Refresh](#kali-forums-refresh) - New heart of the community home
- [Kali NetHunter](#kali-nethunter-updates) - Updates to the app, kernels, installer, store and website!
- [New Tools](#new-tools-in-kali) - 14 new shiny toys added (and countless updated!)

### A New Python Version: 3.12Python 3.12 is now the default Python interpreter. While it was [released upstream](https://docs.python.org/3/whatsnew/3.12.html) a year ago, it took a bit of time to become the [default in Debian](https://tracker.debian.org/news/1542739/python3-defaults-3122-1-migrated-to-testing/), and then even more time to [make it to Kali Linux](https://pkg.kali.org/news/601805/python3-defaults-3125-1-imported-into-kali-rolling/), but finally it’s here. Every new version of Python brings along some deprecations or subtle changes of behavior, which in turn breaks some Python packages, and we have to investigate and fix all the issues reported by our QA system. Hence the delay.

There is a major change with this new Python version: installing third-party Python packages via pip is now strongly discouraged and disallowed by default. This change has been coming for a long time, [we wrote about it 18 months ago already](https://www.kali.org/blog/python-externally-managed/), been given little reminders in each release blog post since and we gave another push about it in the [2024.3 release blog post](https://www.kali.org/blog/kali-linux-2024-3-release/). Now it’s finally effective.

pip users, fear not! It’s not the end of the world: there is [pipx](https://pipx.pypa.io/) as a replacement. On the surface, it provides a similar user experience, but under the hood it overcomes the one outstanding issue with pip: the lack of environment isolation.

For more details, please check our dedicated documentation page: [Installing Python Applications via pipx](https://www.kali.org/docs/general-use/python3-external-packages/). If you still have a hard time running a third-party Python application in Kali, please reach out to us via our [bug tracker](https://bugs.kali.org/).

### The End Of The i386 Kernel And Images…but not packages.

History lesson: i386 is a 32-bit CPU architecture, maybe more widely known by the name x86. It was the CPU architecture of the first generations of Intel Pentium, AMD K6, and Athlon. In short, it was ubiquitous in personal computers back in the 90s. Starting in 2003, a 64-bit version of the x86 architecture appeared, usually named x86-64 (or amd64 in Debian-based Linux distributions). It marked the end of the 32-bit x86 CPUs.

Despite being long obsolete, this architecture remained supported in software for years. 2019 was the year when major Linux distributions ([Fedora 31](https://fedoraproject.org/wiki/Changes/Stop_Building_i686_Kernels) & [Ubuntu](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes)) started to drop it. Finally, in [October 2024](https://lists.debian.org/debian-release/2024/10/msg00064.html), Debian stopped building a i386 kernel (and OS images, as a consequence). Kali Linux, being based on Debian, [follow suit](https://www.kali.org/blog/end-of-i386-kernel-and-images/): images and releases will no longer be created for this platform.

It’s important to note that this is not an instant death for i386 though. This is not how architectures die. The i386 kernel and images are gone, however i386 packages in general are not removed from the repository. It means that it’s still possible to run i386 programs on a 64-bit system. Either directly via the package manager (APT supports installation of i386 packages on a amd64 system), or via [i386 Docker images](https://hub.docker.com/r/kalilinux/kali-rolling/tags).

With time, surely more and more i386 packages will disappear, but nobody really knows in advance which packages and ecosystems will go first, and how long others will remain. In particular, one of the biggest areas that keeps i386 alive is gaming: old games that were compiled for 32-bit x86 are still around, and enjoyed by gamers. As a consequence, there are people out there putting effort into keeping it working, and we can hope that a baseline of i386 packages will remain functional for the time being.

If you are impacted by this change and need more guidance to run your i386 binaries on Kali Linux, please reach out to us via our [bug tracker](https://bugs.kali.org/), we will do our best to help.

### Deprecations In The SSH Client: DSA keysThe latest version of OpenSSH (9.8p1) , available in this release of Kali Linux, deprecates DSA keys for good. If you need this support to connect to very old SSH servers, you will need to use the command ssh1 instead of ssh. Let’s take this chance to review how Kali Linux deals with SSH deprecations, and what it provides to make it easier to use the SSH client for pentesting purpose.

Out of the box, Kali comes with a “standard” SSH client, as provided by Debian. It means that SSH is pre-configured with security in mind: some legacy ciphers and algorithms are disabled by default, to prevent you from using potentially weak encryption without knowing.

For pentesting purposes though, we often need to use all these legacy features, because we need to know if the server that we target has it enabled. To easily enable all the legacy features at once, we provide the command-line tool [kali-tweaks](https://www.kali.org/tools/kali-tweaks/). This tool is a simple menu that allows you to configure various aspects of Kali. In the Hardening section, you can configure SSH for Wide Compatibility (instead of the default Strong Security), and that’s all you need to do to maximize the capabilities of your SSH client.

With that said, when some legacy features are not even compiled in the SSH client anymore (as is the case with DSA keys), you will need to resort to another SSH client: ssh1. [ssh1](https://www.kali.org/tools/openssh-ssh1/) comes pre-installed in this new release of Kali Linux. In practicality, ssh1 is the SSH client frozen at version 7.5 (released in March 2017). This is the last release of OpenSSH that supports the SSH v.1 protocol, and of course it also supports DSA keys. If you target very old SSH servers, you might need to use this client, assuming you are using the SSH client directly from the command-line. However, if you use it indirectly (via some tool that uses SSH), it’s possible that the tool does not know about the ssh1 command, so in practice you will lose support for DSA keys with this new Kali release. If you are in this situation, talk to us (via our [our Discord server](https://discord.kali.org/) or our [bug tracker](https://bugs.kali.org/)), and we might be able to help.

All of this information (and more) is [available in our documentation](https://www.kali.org/docs/general-use/ssh-configuration/).

### Raspberry Pi Imager Customizations SupportThe moment that Pi users have been waiting for has arrived! We are thrilled to announce that Kali’s Raspberry Pi images now support applying customizations directly from the [Raspberry Pi Imager software](https://www.raspberrypi.com/software/)! This is a huge step forward, and we are so excited to bring this much-requested feature to our users. Whether you are a seasoned pro or just getting started, this update is going to make your Raspberry Pi experience even more seamless.

https://www.kali.org/blog/kali-linux-2024-4-release/images/raspberry-pi-imager-custom-image-1.png

For those who might not be familiar with the Raspberry Pi Imager, it was [first introduced in 2020](https://www.raspberrypi.com/news/raspberry-pi-imager-imaging-utility/) by the Raspberry Pi Foundation. This incredibly handy tool allows users to easily write Raspberry Pi operating system images onto an SD card or USB drive with just a few clicks. But that’s not all — it also lets you apply essential customizations before you even boot up your Pi! You can pre-configure a range of settings, from setting a custom username and password to choosing a hostname, connecting to a Wi-Fi network, and even adding an SSH key for remote access.

https://www.kali.org/blog/kali-linux-2024-4-release/images/raspberry-pi-imager-custom-image-2.png

With this latest release, you can now apply these customizations to all Raspberry Pi images — with the exception of the PiTail images, which are highly specialized with their own network and user settings. Unfortunately, due to these customizations, applying them via the Raspberry Pi Imager software is not supported for PiTail images. But for everything else, the sky’s the limit!

https://www.kali.org/blog/kali-linux-2024-4-release/images/raspberry-pi-imager-custom-image-3.png

#### How Does It Work?The magic happens when you write a Raspberry Pi image to your SD card or USB drive using the imager software. If you choose to enable customizations, the settings are stored in two key files on the /boot partition of the drive:

- user-data: This file contains all your personal settings, including the username and password, any locale or timezone preferences, and even your SSH public key (if you have chosen to enable SSH).
- network-config: Here you will find your Wi-Fi network settings, including the pre-computed PSK (Password Security Key) for seamless connectivity.

Once the Raspberry Pi boots for the first time, these files will apply the custom settings automatically.

A quick tip: Do not forget to delete these files after the first boot to keep things secure.

#### Default Settings For Non-Customized ImagesFor users who do not wish to enable customizations, do not worry! The default settings for Raspberry Pi images will remain the same, with [kali/kali for the username and password](https://www.kali.org/docs/introduction/default-credentials/).

### GNOME 47We are excited to announce that the latest update to the GNOME Desktop, [GNOME 47](https://release.gnome.org/47/), is now available! This update brings numerous changes and desktop enhancements, but the most notable feature is the new support for accent color customization. You can now choose your favorite color for window and shell widgets, giving you more control over your desktop’s look and feel.

From Kali’s side, we have also worked on synchronizing this new setting with the icon theme and legacy GTK window themes to ensure a cohesive visual experience. To complement this feature, we have created multiple variants of the icon theme to match each accent color. These themes are also available across other desktop environments, allowing you to personalize your Kali experience.

Your browser does not support the video tag.Other Improvements:

- New login theme

https://www.kali.org/blog/kali-linux-2024-4-release/images/gnome-login-theme.png

- New system-monitor panel extension

https://www.kali.org/blog/kali-linux-2024-4-release/images/gnome-panel-system-monitor.png

- Improved color-schemes for gnome-text-editor

### Kali Forums RefreshA couple of weeks ago we launched the refresh of our [Kali Forums](https://forums.kali.org/). With this refresh we are now running a Discourse-powered forum with a new set of moderators thanks to our community moderators from Discord. We are very happy with the activity we have seen on it so far and hope to see you there!

For more information, please check out our [blog post about the refresh](https://www.kali.org/blog/forums-refresh/).

https://www.kali.org/blog/kali-linux-2024-4-release/images/kali-forums.png

### New Tools In KaliAs always, we have various new tools added (to the network repositories) - 14 this time! Summarizing what has been added:

- [bloodyad](https://www.kali.org/tools/bloodyad/) - Active Directory privilege escalation framework (Submitted by [Arszilla](https://gitlab.com/Arszilla))
- [certi](https://www.kali.org/tools/certi/) - Ask for certificates to ADCS and discover templates (Submitted by [Arszilla](https://gitlab.com/Arszilla))
- [chainsaw](https://www.kali.org/tools/chainsaw/) - Rapidly search and hunt through Windows forensic artefacts (Submitted by [Arszilla](https://gitlab.com/Arszilla))
- [findomain](https://www.kali.org/tools/findomain/) - Fastest and most complete solution for domain recognition (Submitted by [Arszilla](https://gitlab.com/Arszilla))
- [hexwalk](https://www.kali.org/tools/hexwalk/) - Hex analyzer, editor and viewer
- [linkedin2username](https://www.kali.org/tools/linkedin2username/) - Generate username lists for companies on LinkedIn
- [mssqlpwner](https://www.kali.org/tools/mssqlpwner/) - Interact and pwn MSSQL servers
- [openssh-ssh1](https://www.kali.org/tools/openssh-ssh1/) - Secure SHell (SSH) client for legacy SSH1 protocol
- [proximoth](https://www.kali.org/tools/proximoth/) - Control frame attack vulnerability detection tool (Submitted by [TechnicalUserX](https://gitlab.com/TechnicalUserX))
- [python-pipx](https://www.kali.org/tools/python-pipx/) - Execute binaries from Python packages in isolated environments
- [sara](https://www.kali.org/tools/sara/) - RouterOS Security Inspector (Submitted by [casterbyte](https://gitlab.com/casterbyte))
- [web-cache-vulnerability-scanner](https://www.kali.org/tools/web-cache-vulnerability-scanner/) - Go-based CLI tool for testing for web cache poisoning (Submitted by [Arszilla](https://gitlab.com/Arszilla))
- [xsrfprobe](https://www.kali.org/tools/xsrfprobe/) - An advanced Cross Site Request Forgery (CSRF/XSRF) audit and exploitation toolkit.
- [zenmap](https://www.kali.org/tools/nmap/#zenmap) - The Network Mapper (nmap) front end (zenmap-kbx is no longer needed!)

There have also been numerous packages updates and new libraries as well. We also bump the Kali kernel to 6.11!

### Kali NetHunter Updates…There’s a lot here!

#### AppFor the [Kali NetHunter app](https://store.nethunter.com/packages/com.offsec.nethunter/), we are very glad to introduce the Mana toolkit replacement, Wifipumpkin3. After years of silence regarding android restrictions, [yesimxev](https://gitlab.com/yesimxev)’s research solved the Android IP rules mystery and he added [Wifipumpkin3](https://www.kali.org/tools/wifipumpkin3/), which allows you to create a fake AP with working internet, even on mobile network!

https://www.kali.org/blog/kali-linux-2024-4-release/images/wifipumpkin3.png

We have a [quick demo of Wifipumpkin3](https://www.youtube.com/shorts/20Df3fgjs4M) in action if you want to see the results.

Sticking with the Kali NetHunter app, @yesimxev has added a new tab, kernel, which will allow people to flash their kernel without using recovery - direct from the app!

#### Storehttps://www.kali.org/blog/kali-linux-2024-4-release/images/nethunter-store.png

The [Kali NetHunter store](https://store.nethunter.com/) has had a (long overdue) update. This is powered by [F-Droid](https://f-droid.org/), and [completely open-source](https://gitlab.com/kalilinux/nethunter/store/), including the [website](https://gitlab.com/kalilinux/nethunter/store/nethunter-store-website), the [metadata](https://gitlab.com/kalilinux/nethunter/store/nethunter-store-data) and the apps ([#1](https://gitlab.com/kalilinux/nethunter/apps/kali-nethunter-store-client) & [#2](https://gitlab.com/kalilinux/nethunter/apps/kali-nethunter-store-privileged-extension)) that goes with it.

We hope to work on the store more over the next few Kali releases.

At the same time, we have generated new [certificates](https://store.nethunter.com/repo/) & [keys](http://store.nethunter.com/store@nethunter.com-signing.gpg), so please do not be alarmed of the change.

- GPG Key: AA 12 5C D4 16 57 56 83 93 BD 57 5E E1 4B 60 F8 EF 29 08 9C
- Repo Certificate: aa:cb:a8:f5:23:89:39:f9

We have also bump’d privileged extension app to the latest version upstream too.

#### InstallerThe Kali NetHunter installer has had some work on it too!
It now has a new home in its own [git repo](https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-installer) (so does [rootfs](https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-rootfs) & [rootless](https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-rootless)) .

Currently its possible to install Kali NetHunter using either methods:

- Recovery (we recommend using [TWRP](https://twrp.me/)) - the original method
- [Magisk](https://github.com/topjohnwu/Magisk) (which also give “root” permissions) - the future method

We have been supporting both methods for a while, and tried to keep them in sync with each other (as much as possible).
Long term, we will be putting our focus into Magisk method (as that is our preferred method of “root” access).

As of Kali 2024.4, the installer now supports fully supports Magisk (able to flash the kernel) and also added support for v28 and higher! As well as installing via command line (Magisk & TWRP), thanks to adb! There has been work done also for [APatch](https://apatch.dev/) and [KernelSU](https://kernelsu.org/).

There has also been a ton of bug fixes and improvements made too.

#### WebsiteAnother Kali NetHunter change happened is our [NetHunter subdomain website](https://nethunter.kali.org/) (which is [automated CI output](https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernels)).

The new structure should give an easier overview and understanding of the whole process":

- All [pre-created images](https://nethunter.kali.org/images.html) - the items that [ready to download](https://www.kali.org/get-kali/#kali-mobile)
- All [supported devices for the pre-created images](https://nethunter.kali.org/image-models.html) - Some devices, like OnePlus 7 may have multiple items to download (for multiple Android versions)
- Which [devices have the most options](https://nethunter.kali.org/device-kernels.html) - how many supported kernels/Android versions and pre-created images
- [Supported kernels](https://nethunter.kali.org/kernels.html) - Overview of ROMs and Android versions
- Which and how many [Android Versions](https://nethunter.kali.org/android-versions.html) are supported

#### Kernel/DeviceFrom a Kali NetNethunter kernel/device point of view:

- We now support 100 devices!Added support to Realme X7 Max 5G (RMX3031) (Thanks [dek0der](https://gitlab.com/dek0der))
- Added support to Xiaomi Mi 9 Lite / CC9 (pyxis)
- Updated support for Nokia 6.1 & 6.1 Plus (drg)
- Updated support for Realme C11 (RMX2185) (Thanks [Frostleaft07](https://gitlab.com/Frostleaft07))
- Updated support for Xiaomi Mi 9T (davinci)
- Updated support for Xiaomi Mi A3 (xiaomi-laurel)
- Updated support for Xiaomi Pocophone F1 (beryllium)

- First Android 15 device support (Xiaomi Mi A3 (xiaomi-laurel))
- Generating a lot more pre-created images
- The “body of knowledge” file, devices.cfg, which indexes everything, has now been turned into YAML, devices.yml.

#### PackageThe nethunter-utils package has [a new home](https://gitlab.com/kalilinux/packages/nethunter-utils) too.
And to go with it, [Robin](https://gitlab.com/MrRob0-X) has done a lot of audio work.

### Kali NetHunter Pro UpdatesJust a quick message to say that Kali NetHunter Pro now includes “NetHunter” and “Hijacker” apps.

And if you are trying to enable On-The-Go (OTG) on Xiaomi Pocophone F1 and OnePlus 6/6T, you may want to [watch this guide](https://www.youtube.com/watch?v=bjhgKxhgmIY).

### Kali ARM SBC UpdatesAlongside the customizable Raspberry Pi images, we have packed in several other improvements:

- Raspberry Pi 500 Support: The Raspberry Pi 5 image should also have support for the recently announced [Raspberry Pi 500](https://www.raspberrypi.com/news/raspberry-pi-500-and-raspberry-pi-monitor-on-sale-now/) however, we do not have the hardware to test, so please let us know if you do!
- Raspberry Pi 5:By default, KMS (Kernel Mode Setting) is now enabled for a smoother graphical experience. If you prefer to disable it, just comment out the dtoverlay=vc4-kms-v3d line in the /boot/config.txt file.
- Auto Detection Enhancements: We have added improved detection for DSI displays and cameras. The system will automatically load the appropriate overlays, saving you time and effort during setup. It will not work for every one, but it should work for most.

- Gateworks Newport: The second partition on the Gateworks Newport image is no longer set as bootable.
- USB Armory MKII: We have upgraded to u-boot 2024.10, the latest version of the bootloader that it uses.
- Console Fix: The character map has been set to UTF-8, so you will no longer experience corrupt characters at the console. If you are upgrading an existing installation, you can fix this by editing the /etc/default/console-setup file and setting CHARMAP="UTF-8".
- BeagleBone Black: Thanks to a community member, the Beaglebone Black build script (which is community supported) is now able to build images successfully again.

### Kali Website Updates#### Kali DocumentationOur [Kali documentation](https://www.kali.org/docs/) has had a few various major updates to existing pages as well as new pages:

- [Installing NetHunter on the OnePlus One](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-oneplus-one/) (new)
- [Installing NetHunter](https://www.kali.org/docs/nethunter/installing-nethunter/) (updated)
- [Installing old i386 images](https://www.kali.org/docs/installation/installing-old-i386/) (new)
- [Installing Python Applications via pipx](https://www.kali.org/docs/general-use/python3-external-packages/) (new)
- [NetHunter Audio](https://www.kali.org/docs/nethunter/nethunter-audio/) (new)
- [NetHunter Kernel](https://www.kali.org/docs/nethunter/nethunter-kernel/) (new)
- [NetHunter Kex](https://www.kali.org/docs/nethunter/nethunter-kex/) (new)
- [NetHunter Modules](https://www.kali.org/docs/nethunter/nethunter-modules/) (new)
- [NetHunter Settings](https://www.kali.org/docs/nethunter/nethunter-settings/) (new)
- [NetHunter WifiPumpkin](https://www.kali.org/docs/nethunter/nethunter-wifipumpkin/) (new)
- [NetHunter WPS Attacks](https://www.kali.org/docs/nethunter/nethunter-wps/) (new)
- [Where and How to Contribute to Kali](https://www.kali.org/docs/community/contribute/) (updated)

This does not include numerous minor tweaking, or typo fixing!

#### Kali Blog RecapRecapping since since our last release, we did the following [blog posts](https://www.kali.org/blog/):

- [The end of the i386 kernel and images](https://www.kali.org/blog/end-of-i386-kernel-and-images/)
- [Forums Refresh](https://www.kali.org/blog/forums-refresh/)
- [Contributing to Kali](https://www.kali.org/blog/contributing-to-kali/)

### Community Shout-OutsThese are people from the public who have helped Kali and [the team](https://www.kali.org/about-us/) for the last release. And we want to praise them for their work (we like to give credit where due!):

- [@107cwk](https://gitlab.com/107cwk)
- [@Arszilla](https://gitlab.com/Arszilla)
- [@Atlas Co](https://gitlab.com/atlas_c0)
- [@Ayusman Avisek Nanda](https://gitlab.com/ayusman-nanda)
- [@Caster](https://gitlab.com/casterbyte)
- [@ChrisFDev00](https://gitlab.com/ChrisFDev00)
- [@Christian Bremvåg](https://gitlab.com/kimoc0der)
- [@Dario Camonita](https://gitlab.com/danterolle)
- [@David Cheeseman](https://gitlab.com/nuvious)
- [@dek0der](https://gitlab.com/dek0der)
- [@Dũng Đinh](https://gitlab.com/dungdinhmanh)
- [@Elliot](https://gitlab.com/whthomas22)
- [@hexan](https://twitter.com/sohrminir)
- [@Robin](https://gitlab.com/MrRob0-X)
- [@S3L33](https://infosec.exchange/@S3L33)
- [@Salty](https://gitlab.com/Salty_)
- [@serval](https://gitlab.com/serval123)
- [@Sourabh Panchal](https://gitlab.com/IamCOD3X)
- [@Strix Vyxlor](https://gitlab.com/Strix-Vyxlor)
- [@Shubham Vishwakarma](https://gitlab.com/Shubhamvis98)
- [@yesimxev](https://gitlab.com/yesimxev)
- [@Yuki Nix](https://gitlab.com/Umaru-Xi)
- [@自由的铁矿](https://gitlab.com/vvvbbbcz)

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

### MiscellaneousBelow are a few other things which have been updated in Kali, which we are calling out which do not have as much detail:

- @elwood gave a talk at [SINCON 2024](https://www.infosec-city.com/schedule/sin24-con) back in May 2024, which is now public: [Kali Linux: Unveiling the Hidden Gems of the Industry Standard - by Jim O’Gorman](https://www.youtube.com/watch?v=3O2W7_NkAfQ)
- (Xfce4) xcape no longer required for super key (menu) shortcut
- (GNOME) gnome-text-editor sysntax highlighting theme has been improved
- Fixed LightDM session not loading profile configuration files

### Get Kali Linux 2024.4Fresh Images:
So what are you waiting for? Go [get Kali](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for those who are not, we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you will have fewer updates to do.
Just know that these are automated builds that we do, not QA like we do for our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~/
[...]

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2024.4. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION_ID="2024.4"
VERSION="2024.4"
VERSION_CODENAME=kali-rolling

┌──(kali㉿kali)-[~]
└─$     uname -v
#1 SMP PREEMPT_DYNAMIC Kali 6.11.2-1kali1 (2024-10-15)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.11.2-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And Social networks are not bug trackers!

Want to keep up-to-date easier? We have got you!

- [Blog](https://www.kali.org/blog/)? Use our [RSS feeds](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/)
- Download? We have a [Torrent RSS feed](https://www.kali.org/torrents.xml)
- Socials? [Facebook](https://www.facebook.com/KaliLinux/), [Instagram](https://www.instagram.com/kalilinux/), [Mastodon](https://infosec.exchange/@kalilinux) & [X/Twitter](https://x.com/kalilinux)

## 2024.3 – 2024-09-11

**Kali Linux 2024.3 Release (Multiple transitions)**

Table of Contents
- [New Tools in Kali](#new-tools-in-kali)
- [Kali NetHunter Updates](#kali-nethunter-updates)
- [Kali ARM SBC Updates](#kali-arm-sbc-updates)[Kali Documentation](#kali-documentation)

- [Community Shout-Outs](#community-shout-outs)[New Kali Mirrors](#new-kali-mirrors)

- [Get Kali Linux 2024.3](#get-kali-linux-20243)

With summer coming to an end, so are package migrations, and Kali 2024.3 can now be released. You can now start [downloading](https://www.kali.org/get-kali/) or [upgrading if you have an existing Kali installation](https://www.kali.org/docs/general-use/updating-kali/).

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2024.2 release from June](https://www.kali.org/blog/kali-linux-2024-2-release/) is:

- [Qualcomm NetHunter Pro Devices](#kali-nethunter-updates) - Qualcomm Snapdragon SDM845 SoC now supported
- [New Tools](#new-tools-in-kali) - 11x new tools in your arsenal

Our focus has been on a lot of behind the scenes updates and optimizations since the last release. There have been some messy migrations, with multiple stacks, all interrelating (transition have been like buses, all coming at once!). After the [t64 transition](https://www.kali.org/blog/kali-linux-2024-2-release/) finished up, it was straight into multiple other transitions: GCC 14, the glibc 2.40, and Python 3.12.

This last one is the most significant! This new Python release removed some long-deprecated APIs, breaking a fair number of packages. We have been busy fixing it all (weeks of work!), we are almost there, Python 3.12 will be the default in the next version of Kali - 2024.4. With Python 3.12, there will be a major change for users: it won’t be possible to install Python packages with pip anymore. [We wrote about that a year ago already](https://www.kali.org/blog/python-externally-managed/), we invite you to read that again if you are an avid user of pip.

But that will be for the next Kali release, 2024.4, due by the end of the year. In the meantime, this new release 2024.3 still has Python 3.11 as the default Python interpreter.

An unfortunate consequence of this situation is that, as the whole Python 3.12 stack did not enter [Kali-rolling](https://www.kali.org/docs/general-use/kali-branches/) yet, it also blocked other packages (seemingly unrelated to Python) from entering Kali-rolling. In other words, over the last 2 months the pace of updates in Kali-rolling went down, making this release less exciting than usual. This temporary slowdown should end in the coming days and weeks, as Python 3.12 finally hits Kali-rolling. At this point packages will resume flowing as usual, so users of Kali-rolling should be ready for a lot of updates!

To finish: apart from packaging, various projects either got started or continued to make progress, but are not ready for release just yet (such as having a new Kali forum, NetHunter Store updates and refreshing Kali-menu).

### New Tools in KaliThis Kali release is about package updates.
For end users its mostly about new tools added, for us, its about the updated stacks!

The community once again has set up and added various new tools. Long term contributor [Arszilla](https://gitlab.com/arszilla) has been busy again!
Here is a highlight of what new tools have been added (to the network repositories):

- [goshs](https://www.kali.org/tools/goshs/) - Think SimpleHTTPServer, but written in Go, and with more features
- [graudit](https://www.kali.org/tools/graudit/) - Grep Rough AUDIT: source code auditing tool
- [gsocket](https://www.kali.org/tools/gsocket/) - Allows two machines on different networks to communicate with each other
- [hekatomb](https://www.kali.org/tools/hekatomb/) - Extract and decrypt all credentials from all domain computers (Submitted by [Arszilla](https://gitlab.com/arszilla))
- [mxcheck](https://www.kali.org/tools/mxcheck/) - Info and security scanner for e-mail servers (Submitted by [Arszilla](https://gitlab.com/arszilla))
- [netexec](https://www.kali.org/tools/netexec/) - Network service exploitation tool that helps automate assessing the security of large networks (Submitted by [Arszilla](https://gitlab.com/arszilla))
- [netscanner](https://www.kali.org/tools/netscanner/) - Network scanner & diagnostic tool with modern TUI (Submitted by [Arszilla](https://gitlab.com/arszilla))
- [obsidian](https://www.kali.org/tools/obsidian/) - Private and flexible writing app that adapts to the way you think
- [sippts](https://www.kali.org/tools/sippts/) - Set of tools to audit SIP based VoIP Systems (Submitted by [Arszilla](https://gitlab.com/arszilla))
- [sprayhound](https://www.kali.org/tools/sprayhound/) - Password spraying tool and Bloodhound integration (Submitted by [Arszilla](https://gitlab.com/arszilla))
- [sqlmc](https://www.kali.org/tools/sqlmc/) - Check all URLls of a domain for SQL injections (Submitted by [Arszilla](https://gitlab.com/arszilla))

It goes without saying, that there has been numerous packages updates and new libraries as well.

Again, we want to shout out Arszilla and his multiple contributions. Always remember, you can contribute as well! We are always open for engagement from you if you want to get involved.

As hinted in [our previous 2024.2 release](https://www.kali.org/blog/kali-linux-2024-2-release/#new-tools-in-kali), the [Kali kernel](https://pkg.kali.org/pkg/linux) is now also at 6.8.

### Kali NetHunter UpdatesKali NetHunter 2024.3 has been held back for the the time being, as we are busy upating the build infrastructure.
We will release the updated images when they are ready (hopefully in a few weeks), and talk whats new with them in the next Kali release 2024.4 (Bye Mana!).

Fortunately, we can say there are new supported devices!
We are excited to release Kali NetHunter Pro images for devices with a Qualcomm Snapdragon SDM845 SoC (System on a Chip), such as:

- OnePlus 6 (enchilada)/6T (fajita) [SDM845]
- SHIFT SHIFT6mq (axolotl) [SDM845]
- Xiaomi Pocophone F1 (beryllium ebbg/tianma) [SDM845]
- Xiaomi Mi MIX 2S (polaris) [SDM845]
- Fairphone 4 [SM7225]
- …amd64 image to be used in a VM for testing/deployment

Thanks to [Shubhamvis98](https://gitlab.com/Shubhamvis98) for his amazing work to make this happen!

https://www.kali.org/blog/kali-linux-2024-3-release/images/Hack-es-Langos.png

There is also good news for Hungarian NetHunters! Check out “HnLVIP NetHunter” (1st August 2024), in this podcast by [hackeslangos](https://hackeslangos.show/) featuring [yesimxev](https://gitlab.com/yesimxev), talking about getting into NetHunter, an OffSec journey and more! You can listen to it here:

- [Apple](https://podcasts.apple.com/podcast/hnlvip-nethunter/id1334043708?i=1000664073443)
- [Spotify](https://open.spotify.com/episode/2fKvY6LzScpToRktIDKdWN)

### Kali ARM SBC Updates
- We now pass QEMU_CPU=cortex-a72 to the build scripts when building an arm64 image on an amd64 host, which should speed things back up considerably.
- USBArmory devices should now properly start their DHCP server
- Support has been added for the Raspberry Pi 4 Compute Module Wi-Fi device
- Raspberry Pi 5 kernel version has been bumped to 6.6additionally due to the new firmware in use on it, if you use an A2 rated microSD card, you should see 2-3x speedup of random access

- Pinebook kernel has been reverted back to a 6.1 kernel due to graphical glitches, and LCD not working on newer kernels
- We have cleaned up the build dependencies list, so we do not make users install a bunch of dependencies that are no longer used when building their own custom image.

#### Kali DocumentationOur [Kali documentation](https://www.kali.org/docs/) has had various updates to existing pages as well as new pages:

- [Install NVIDIA GPU Drivers - Hashcat not detecting GPU](https://www.kali.org/docs/general-use/install-nvidia-drivers-on-kali-linux/#hashcat) (updated)
- [Kali inside VirtualBox (Guest VM) - Expanding Storage](https://www.kali.org/docs/virtualization/install-virtualbox-guest-vm/#expanding-storage) (updated)
- [Kali inside VMware (Guest VM) - Expanding Storage](https://www.kali.org/docs/virtualization/install-vmware-guest-vm/#expand-storage) (updated)
- [NetHunter Pro Waydroid](https://www.kali.org/docs/nethunter-pro/waydroid/) (new)
- [Windows Anti-virus Warning](https://www.kali.org/docs/troubleshooting/windows-antivirus-warning/) (new)

### Community Shout-OutsThere has been various people from the Kali community, who have directly helped the project this release. And we want to praise them for their work (we love to give credit where due!):

Kali Documentation:

- [Jakob](https://gitlab.com/SIMULATAN)
- [ROYGBYTE](https://gitlab.com/roygbyte)
- [devdevs](https://gitlab.com/devndevs)
- [Ram Prashanth](https://gitlab.com/ram-prashanth)
- [Robert Thornton](https://gitlab.com/320gigabytes)
- [SAIKAT KARMAKAR](https://gitlab.com/Aviksaikat)
- [Bassem Essam](https://gitlab.com/bassem-essam)
- [Ravindu Deshan](https://gitlab.com/ravindu644)
- [serval](https://gitlab.com/serval123)
- [Shubham Vishwakarma](https://gitlab.com/Shubhamvis98)

And remember, the door is always open for you to be listed here next month!

Tool Documentation:

- [Andyshafferco](https://gitlab.com/andyshafferco) for updating sparrow-wifi tool documentation page

Packaging:

- [Arszilla](https://gitlab.com/arszilla) who helped packaging many new tools
- [X0RW3LL](https://gitlab.com/X0RW3LL) for help in fixing various packages for Python 3.12

Support:

- [rcfa](https://gitlab.com/rcfa), for providing the info needed to enable the Wi-Fi on Raspberry Pi 4 Compute Module
- [Salty_](https://gitlab.com/Salty_) who has once again helped with testing the Raspberry Pi images for release

Bug Fixes:

- [Henrique Campo](https://gitlab.com/henry701) for [Kali-Win-Kex](https://gitlab.com/kalilinux/packages/kali-win-kex/-/merge_requests/9) fixes and updated version support
- [Kenji Yamada](https://gitlab.com/melito) for [Kali-Win-Kex](https://gitlab.com/kalilinux/packages/kali-win-kex/-/merge_requests/8) fixes

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

#### New Kali MirrorsIt was a quiet release cycle on this front, with 2 new mirrors joining our network, and 2 former mirrors making a comeback, for a total of 4 new mirrors. Here they are:

- Bulgaria: [mirror.telepoint.bg](https://mirror.telepoint.bg/kali/) sponsored by [Telepoint](https://www.telepoint.bg/) and thanks to Valentin Nikolov
- Italy: [kali.mirror.garr.it](https://kali.mirror.garr.it/kali/) sponsored by [GARR The Italian Research and Education Network](https://mirror.garr.it/index_en.html) and thanks to Vincenzo Caracciolo
- Netherlands: [mirror.serverion.com](https://mirror.serverion.com/kali/) sponsored by [Serverion](https://www.serverion.com/) and thanks to Desmond van der Winden
- South Korea: [mirror.siwoo.org](https://mirror.siwoo.org/kali/) thanks to Siwoo Lim

As always, a big thanks to all the mirrors who support Kali distribution all around the world. If you have the disk space and bandwidth, [we always welcome new mirrors](https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/).

### Get Kali Linux 2024.3Fresh Images:
So what are you waiting for? Go [get Kali](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for those who are not, we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you will have fewer updates to do.
Just know that these are automated builds that we do, not QA like we do for our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~/
[...]

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2024.3. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2024.3"
VERSION_ID="2024.3"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Kali 6.8.11-1kali2 (2024-05-30)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.8.11-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And Social networks are not bug trackers!

Want to keep up-to-date easier? We’ve got you!

- [Blog](https://www.kali.org/blog/)? Use our [RSS feeds](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/)
- Download? We have a [Torrent RSS feed](https://www.kali.org/torrents.xml)
- Socials? [Facebook](https://www.facebook.com/KaliLinux/), [Instagram](https://www.instagram.com/kalilinux/), [Mastodon](https://infosec.exchange/@kalilinux) & [Twitter/X](https://x.com/kalilinux)

## 2024.2 – 2024-06-05

**Kali Linux 2024.2 Release (t64, GNOME 46 & Community Packages)**

Table of Contents
- [The t64 transition is done in Kali](#the-t64-transition-is-done-in-kali)
- [Desktop changes](#desktop-changes)[GNOME 46](#gnome-46)
- [Xfce desktop changes](#xfce-desktop-changes)

- [New Tools in Kali](#new-tools-in-kali)
- [Miscellaneous](#miscellaneous)
- [Kali NetHunter Updates](#kali-nethunter-updates)
- [Kali ARM SBC Updates](#kali-arm-sbc-updates)[Kali Documentation](#kali-documentation)
- [Kali Blog Recap](#kali-blog-recap)

- [Community Shout-Outs](#community-shout-outs)[New Kali Mirrors](#new-kali-mirrors)

- [Kali Team Discord Chat](#kali-team-discord-chat)
- [Get Kali Linux 2024.2](#get-kali-linux-20242)

A little later than usual, but Kali 2024.2 is here! The delay has been due to changes under the hood to make this happen, which is where a lot of focus has been. The community has helped out a huge amount, and this time they’ve not only been adding new packages, but updating and fixing bugs too! If you are reading this, Kali 2024.2 is finally ready to be [downloaded](https://www.kali.org/get-kali/) or [upgraded if you have an existing Kali Linux installation](https://www.kali.org/docs/general-use/updating-kali/).

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2024.1 release from February](https://www.kali.org/blog/kali-linux-2024-1-release/) is:

- [t64](#the-t64-transition-is-done-in-kali) - Future package compatibility for 32-bit platforms
- [Desktop Changes](#desktop-changes) - GNOME 46 & Xfce improvements
- [New Tools](#new-tools-in-kali) - 17x new tools, and countless updates

### The t64 transition is done in KaliKali Linux is a rolling distribution based on Debian testing, and as such, all the work done in Debian is incorporated in Kali pretty quickly after it lands in Debian testing. We have some solid QA and automation for that to happen, and usually most packages just “roll in” with minimal intervention from the Kali team. Our QA tells us when new packages from Debian break packages in Kali: in those cases packages are stuck in [kali-dev](https://www.kali.org/docs/general-use/kali-branches/#the-kali-dev-repository) (a development suite that is NOT meant to be used by end users), we fix it, and then they are allowed to roll in [kali-rolling](https://www.kali.org/docs/general-use/kali-branches/#the-kali-rolling-repository) (which is what most end users use). This is part of what the Kali team does every day.

During the last cycle, this routine was interrupted by a major change in Debian: [the t64 transition](https://wiki.debian.org/ReleaseGoals/64bit-time). What is that? In short: t64 refers to 64-bit time_t type. For those not familiar with C, time_t is the type to store a Unix timestamp (quantity of seconds relative to the Unix Epoch), and the size for this type depends on the architecture. For those architectures that have a 32-bit time_t type, there will be an issue in the year 2038, as the maximum value possible will be reached, and the value will roll over beyond +2147483647 into negative values. The [glibc page](https://sourceware.org/glibc/wiki/Y2038ProofnessDesign) has all the technical details, for those who want to read more.

To prevent the Year 2038 issue, the size for the time_t type had to be changed to be 64-bit, on those architectures where it was 32-bit. For Kali Linux, that means the two 32-bit ARM architectures that we support: armhf and armel. These architectures are used mainly for [ARM images](https://www.kali.org/get-kali/#kali-arm) (eg. Raspberry Pi) and a few [NetHunter images](https://www.kali.org/get-kali/#kali-mobile). Note that the i386 architecture (ie. legacy PC) didn’t change: this architecture still will have a 32-bit time_t type, and that will not change. Kali has always treated ARM platform as a first-class citizen.

Changing the size of a widely used type provided by the C library is a big deal. It means that a huge number of packages need to be rebuilt, it is in fact [the largest ABI transition ever done in Debian](https://www.phoronix.com/news/Debian-Experimental-64bit-Time). And in a sense, it affects all architectures, as all libraries that expose a time_t type were rebuilt and renamed with a t64 suffix, even for those architectures where the type was already 64-bit (in this case, the only change is a package rename).

Enough background, now what does it mean for Kali users?

- The transition was completed in kali-rolling on Monday 20th May, and is now released with Kali 2024.2. For users of Kali rolling who updated their system, the transition is behind them already.
- The vast majority of Kali users are running on amd64 or arm64: the only visible change will be a lot of packages upgraded, and a lot of new packages with a t64 suffix in their name. Since there was no ABI change for those architectures, there should be no issue. Additionally, old packages (without t64 suffix) are co-installable with the new t64 packages, so upgrading should be no problem for APT.
- The users that might be impacted are those running Kali on a armel or armhf ARM board. If you upgrade your system, make sure to use the command apt full-upgrade (do NOT use apt upgrade) , [as documented already](https://www.kali.org/docs/general-use/updating-kali/). After your system is upgraded, hopefully all goes well and works as usual, but if ever you notice issues, please report it on the [Kali Linux bugtracker](https://bugs.kali.org/).

So just to repeat it again, for those who jumped straight to the last line: please upgrade your system [as documented](https://www.kali.org/docs/general-use/updating-kali/), using the pair of commands apt update && apt full-upgrade, and everything should be fine. Please report bugs in case of issues. Thank you!

### Desktop changes#### GNOME 46Roughly every half-year, there is a new version bump for the GNOME desktop environment. Of which, Kali 2024.2 brings the latest version, [GNOME 46](https://release.gnome.org/46/). As you would expect, this is a more polished experience following the work introduced in previous versions.

All themes and extensions have been updated to support the new shell:

https://www.kali.org/blog/kali-linux-2024-2-release/images/gnome-46.png

#### Xfce desktop changesWe are excited to announce updates to the Xfce desktop, specifically for [Kali-Undercover](https://www.kali.org/docs/introduction/kali-undercover/) and [HiDPI](https://www.kali.org/docs/general-use/hidpi/) modes. These updates enhance stability and include several minor bug fixes, ensuring better support for the latest desktop improvements.

https://www.kali.org/blog/kali-linux-2024-2-release/images/kali-undercover.png

### New Tools in KaliThere has not been a single Kali release without any new shiny tools added, and this release is no exception.
We are overjoyed that there have been multiple tools packaged up from the community, which are now in Kali too!
It goes without saying that countless packages have been updated to the latest version, however the summary of new tools which have been added (to the network repositories):

- [autorecon](https://www.kali.org/tools/autorecon/) - Multi-threaded network reconnaissance tool (Submitted by [Arszilla](https://gitlab.com/arszilla))
- [coercer](https://www.kali.org/tools/coercer/) - Automatically coerce a Windows server to authenticate on an arbitrary machine (Submitted by [Caster](https://gitlab.com/casterbyte))
- [dploot](https://www.kali.org/tools/dploot/) - Python rewrite of SharpDPAPI (Submitted by [Arszilla](https://gitlab.com/arszilla))
- [getsploit](https://www.kali.org/tools/getsploit/) - Command line utility for searching and downloading exploits (Submitted by [Arszilla](https://gitlab.com/arszilla))
- [gowitness](https://www.kali.org/tools/gowitness/) - Web screenshot utility using Chrome Headless
- [horst](https://www.kali.org/tools/horst/) - Highly Optimized Radio Scanning Tool
- [ligolo-ng](https://www.kali.org/tools/ligolo-ng/) - Advanced, yet simple, tunneling/pivoting tool that uses a TUN interface
- [mitm6](https://www.kali.org/tools/mitm6/) - pwning IPv4 via IPv6 (Submitted by [Caster](https://gitlab.com/casterbyte))
- [pspy](https://www.kali.org/tools/pspy/) - Monitor Linux processes without root permissions
- [pyinstaller](https://www.kali.org/tools/pyinstaller/) - Converts (packages) Python programs into stand-alone executables.
- [pyinstxtractor](https://www.kali.org/tools/pyinstxtractor/) - PyInstalller Extractor (Submitted by [Arszilla](https://gitlab.com/arszilla))
- [sharpshooter](https://www.kali.org/tools/sharpshooter/) - Payload Generation Framework
- [sickle](https://www.kali.org/tools/sickle-tool/) - Payload development tool (Submitted by [Arszilla](https://gitlab.com/arszilla))
- [snort](https://www.kali.org/tools/snort/) - Flexible Network Intrusion Detection System
- [sploitscan](https://www.kali.org/tools/sploitscan/) - Search for CVE information
- [vopono](https://www.kali.org/tools/vopono/) - Run applications through VPN tunnels with temporary network namespaces (Submitted by [Arszilla](https://gitlab.com/arszilla))
- [waybackpy](https://www.kali.org/tools/waybackpy/) - Access Wayback Machine’s API using Python (Submitted by [Arszilla](https://gitlab.com/arszilla))

There have also been numerous new libraries as well!

We just missed out on having kernel 6.8 included. It will be available shortly after this release and may already be out by the time of reading.

### MiscellaneousThere have been a few mirror tweaks and changes to Kali which we are calling out below as they don’t need much detail:

- During testing, a bug was found in 6.6 kernel which could causes slow downs and system crashes when using certain virtualization software. This has been addressed in the upcoming [6.8 kernel](https://pkg.kali.org/pkg/linux).
- [nmap](https://www.kali.org/tools/nmap/) has been tweaked, allowing for users to run privileged TCP SYN (Stealth) scans (-sS) without using sudo or being root.

### Kali NetHunter UpdatesThere have been also a few improvements to Kali NetHunter over the last few months, such as:

- Support for Android 14
- The long awaited modules loader has been added by [yesimxev](https://gitlab.com/yesimxev)
- Class selection for Bad Bluetooth also by [yesimxev](https://gitlab.com/yesimxev)
- We also improved the permission and root validations
- Thanks to [shubhamvis98](https://gitlab.com/shubhamvis98), who added Bluetooth rubberducky support
- There have been various fixes though-out
- Kali NetHunter Pro images will be out shortly after the release, due to t64

With all of this, 5x new [Kali NetHunter kernels](https://nethunter.kali.org/kernels.html) covering:

- Huawei P9 for LineageOS 16
- Nothing Phone 1 for Android 12, 13 & 14
- Poco F3 for Android 14

https://www.kali.org/blog/kali-linux-2024-2-release/images/nethunter_poco_f3.png

### Kali ARM SBC UpdatesKali on ARM Single Board Computer (SBC) devices has also received a few changes:

- [Gateworks Newport](https://www.kali.org/docs/arm/gateworks-newport/) kernel updated to 5.15
- [Raspberry Pi 5](https://www.kali.org/docs/arm/raspberry-pi-5/) kernel updated to 6.1.77
- Unfortunately we cannot provide support for [Gateworks Ventana](https://www.kali.org/docs/arm/gateworks-ventana/), and as a result no longer are able to offer a pre-built image

#### Kali DocumentationOur [Kali documentation](https://www.kali.org/docs/) has had several updates to existing pages as well as new pages:

- [AWS](https://www.kali.org/docs/cloud/aws/) (updated)
- [Fixing Dual Boot](https://www.kali.org/docs/troubleshooting/dual-boot/) (new)
- [Install NVIDIA GPU Drivers](https://www.kali.org/docs/general-use/install-nvidia-drivers-on-kali-linux/) (updated)
- [Installing VirtualBox on Kali (Host)](https://www.kali.org/docs/virtualization/install-virtualbox-host/) (updated)
- [Installing VMware on Kali (Host)](https://www.kali.org/docs/virtualization/install-vmware-host/) (updated)
- [Kali inside Proxmox (Guest VM)](https://www.kali.org/docs/virtualization/install-proxmox-guest-vm/) (updated)
- [Porting NetHunter to New Devices with kernel builder](https://www.kali.org/docs/nethunter/porting-nethunter-kernel-builder/) (updated)
- [Updating a Package](https://www.kali.org/docs/general-use/updating-a-package/) (new)

#### Kali Blog RecapSince 2024.1, there was a lot of activity around xz-utils, which is why we published the following [blog posts](https://www.kali.org/blog/):

- [All about the xz-utils backdoor](https://www.kali.org/blog/about-the-xz-backdoor/)
- [xz-utils backdoor: how to get started](https://www.kali.org/blog/xz-backdoor-getting-started/)

### Community Shout-OutsThese are people from the public who have helped Kali and the team for the last release, and we wanted to praise them for their work (we like to give credit where due!):

Packaging:

- [Arszilla](https://gitlab.com/arszilla)
- [Caster](https://gitlab.com/casterbyte)

Kali Documentation:

- [Arszilla](https://gitlab.com/Arszilla)
- [David Tomaschik](https://gitlab.com/matir)
- [EDLLT](https://gitlab.com/EDLLT)
- [FalseProfit](https://gitlab.com/FalseProfit)
- [gader](https://gitlab.com/gad3r)
- [Henrik Lund](https://gitlab.com/bootorder)
- [Jane Rysavy](https://gitlab.com/janerysavy17)
- [Jordan](https://gitlab.com/Fetti.Wop)
- [Net LAG](https://gitlab.com/netlag)
- [prplhaz4](https://gitlab.com/prplhaz4)
- [Theo Melo](https://gitlab.com/melotheo)
- [X0RW3LL](https://gitlab.com/X0RW3LL)
- [Zachary Miller](https://gitlab.com/bigdipper553)

Tool Documentation:

- [Simon Bennetts](https://gitlab.com/psiinon)

Support:

- [Salty_](https://gitlab.com/Salty_)

Kali is open-source, allowing YOU to help out. Anyone is able to get [involved](https://www.kali.org/docs/community/contribute/)!

#### New Kali MirrorsDuring this release cycle, we welcomed 7 new mirrors! Thanks to all of you who reached out and helped with distributing Kali around the world.

So we have 3 new mirrors in North America:

- Canada: [kali.mirror.rafal.ca](https://kali.mirror.rafal.ca/kali/)
- US: [mirror.math.princeton.edu](https://mirror.math.princeton.edu/pub/kali/) sponsored by the [Princeton University, Department of Mathematics](https://www.math.princeton.edu/) and thanks to Benjamin Rose
- US: [ftp2.osuosl.org](https://ftp2.osuosl.org/pub/kali-images/) sponsored by the [Oregon State University Open Source Lab (OSUOSL)](https://osuosl.org/) and thanks to Lance Albertson

Then 3 new mirrors in Asia:

- Singapore: [mirror.freedif.org](https://mirror.freedif.org/kali/)
- Taiwan: [free.nchc.org.tw](https://free.nchc.org.tw/kali/) sponsored by the [National Center for High-Performance Computing](https://www.nchc.org.tw/en/) and thanks to Ceasar Sun
- Taiwan: [mirror.twds.com.tw](https://mirror.twds.com.tw/kali/) sponsored by [Taiwan Digital Streaming Co.](https://www.twds.com.tw/) and thanks to Jasper Yu

And finally, the [Micro Mirror CDN](https://www.kali.org/blog/kali-linux-2024-1-release/#introducing-the-micro-mirror-free-software-cdn) provided us with a new mirror in Europe:

- Switzerland: [ipng.mm.fcix.net](https://ipng.mm.fcix.net/kali-images/) sponsored by [IPng Networks](https://ipng.ch/).

If you have the disk space and bandwidth, [we always welcome new mirrors](https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/).

### Kali Team Discord ChatWe are keeping the tradition going and doing another hour long voice chat with the Kali team and community. If you want your questions answered or your ideas heard, this is the place for it! We just hope they are related to Kali or the information security industry.

The next session will happen a week after the release, Friday, 21st June 2024 17:00 -> 18:00 [UTC/+0 GMT](https://time.is/compare/0500PM_21_June_2024_in_UTC) on [OffSec’s Discord](https://discord.com/servers/offsec-780824470113615893).

- [Discord invite](https://discord.gg/invite/offsec)
- [iCalendar invite](./Kali-Discord-2024.2.ics)

Please note, we will not be recording this event - it is live only.

### Get Kali Linux 2024.2Fresh Images:
So what are you waiting for? [Get Kali](https://www.kali.org/get-kali/)!

For those who are new to Kali Linux, you may not be aware that we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/), which are also available for download. If you are eager to get the latest packages and bug fixes without waiting for our next release, the weekly image is a great option.
This will save you from having to do more updates later on.
However, please note that these weekly builds are automated and have not undergone the same level of testing as our [standard release images](https://www.kali.org/releases/). We still appreciate any [bug reports](https://bugs.kali.org/) you may have, as we want to address any issues before our next release.

Existing Installs:
If you already have an existing Kali Linux installation, remember you can [update](https://www.kali.org/docs/general-use/updating-kali/) it by doing:

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~/
[...]

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2024.2.
We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2024.2"
VERSION_ID="2024.2"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Kali 6.6.15-2kali1 (2024-05-17)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.6.15-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

If you encounter any issues or bugs in Kali, please report them to our dedicated [bug tracker](https://bugs.kali.org/). Your feedback is crucial in helping us identify and fix problems. Remember, we can not fix what we do not know is broken! Do not rely on social media to report bugs; instead, use our official bug tracker to ensure your issues are properly documented and addressed.

Want to keep up-to-date easier? We’ve got you!

- [Blog](https://www.kali.org/blog/)? Use our [RSS feeds](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/)
- Download? We have a [Torrent RSS feed](https://www.kali.org/torrents.xml)
- Socials? [Facebook](https://www.facebook.com/KaliLinux/), [Instagram](https://www.instagram.com/kalilinux/), [Mastodon](https://infosec.exchange/@kalilinux) & [Twitter/X](https://x.com/kalilinux)

## 2024.1 – 2024-02-28

**Kali Linux 2024.1 Release (Micro Mirror)**

Table of Contents
- [Introducing the Micro Mirror Free Software CDN](#introducing-the-micro-mirror-free-software-cdn)
- [2024 Theme Refresh](#2024-theme-refresh)
- [Other desktop changes](#other-desktop-changes)[Xfce](#xfce)
- [Gnome-Shell](#gnome-shell)
- [Icon Theme](#icon-theme)

- [Kali NetHunter Updates](#kali-nethunter-updates)
- [New Tools in Kali](#new-tools-in-kali)[Community Packages](#community-packages)

- [Miscellaneous](#miscellaneous)
- [Kali Website Updates](#kali-website-updates)[Kali Documentation](#kali-documentation)
- [Tool Documentation](#tool-documentation)
- [Kali Blog Recap](#kali-blog-recap)

- [Community Shout-Outs](#community-shout-outs)[New Kali Mirrors](#new-kali-mirrors)

- [Kali Team Discord Chat](#kali-team-discord-chat)
- [Get Kali Linux 2024.1](#get-kali-linux-20241)

Hello 2024! Today we are unveiling Kali Linux 2024.1. As this is our the first [release](https://www.kali.org/releases/) of the year, it does include new visual elements! Along with this we also have some exciting new mirrors to talk about, and of course some package changes - both new tools and upgrades to existing ones. If you want to see the new theme for yourself and maybe try out one of those new mirrors, [download a new image](https://www.kali.org/get-kali/) or [upgrade if you have an existing Kali Linux installation](https://www.kali.org/docs/general-use/updating-kali/).

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2023.4 release from December](https://www.kali.org/blog/kali-linux-2023-4-release/) is:

- [Micro Mirror Free Software CDN](#introducing-the-micro-mirror-free-software-cdn) - FCIX Software Mirror reached out offering to host our images, and we said yes
- [2024 Theme Refresh](#2024-theme-refresh) - Our yearly theme refresh with all new wallpapers and GRUB theme
- [Other Desktop Environment Changes](#other-desktop-changes) - A few new tweaks to our default environments
- [NetHunter Updates](#kali-nethunter-updates) - NetHunter Rootless for Android 14, Bad Bluetooth HID attacks, and other updates
- [New Tools](#new-tools-in-kali) - As always, various new shiny tools!

### Introducing the Micro Mirror Free Software CDNWith this latest release of Kali Linux, our network of [community mirrors](https://http.kali.org/README?mirrorlist) grew much stronger, thanks to the help of the Micro Mirror CDN! Here’s the story.

Last month we replied to a long-forgotten email from Kenneth Finnegan from the [FCIX Software Mirror](https://mirror.fcix.net/). The FCIX is a rather big mirror located in California, and they reached out to offer to host the Kali images on their mirror. To which we answered yes please, and that was it; shortly after, the [Kali images were added to the FCIX mirror](https://mirror.fcix.net/kali-images/). So far so good, and it could have been the end of the story, but then Kenneth followed up:

We’re now also operating another 32 other mirrors which are optimized for minimal storage and hosting only the highest traffic projects […] Would the Kali project be willing to accept ten additional mirrors from the FCIX organization?

Wow, 10 additional mirrors, that sounds very nice indeed! But, wait, 32 mirrors??? How come? Where do all those mirrors come from? That was intriguing. As it turns out, Kenneth operates a network of mirrors, which was officially announced back in May 2023 on his blog: [Building the Micro Mirror Free Software CDN](https://blog.thelifeofkenneth.com/2023/05/building-micro-mirror-free-software-cdn.html). For anyone interested in Internet infrastructure, we encourage you to read it, that’s a well-written blog post right there, waiting for you.

So what is the Micro Mirror CDN exactly? One-liner: a network of mirrors dedicated to serving Linux and Free Software. Contrary to traditional mirrors that host around 50TB of project files, Micro Mirrors are machines with “only” a few TB of storage, that focus on hosting only the most high-demand projects. In other words: they provide additional bandwidth where it’s needed the most. Another important difference with traditional mirrors is that those machines are not managed by the sponsor (the organization that funds the mirror). Usually, a sponsor provides the bandwidth, the mirror, and also administrates it. While here, the sponsor only provides the bandwidth, and it’s the FCIX Micro Mirror team that does everything else: buy the hardware, ship it to the data-center, and then manage it remotely via their [public Ansible playbook](https://github.com/PhirePhly/micromirrors).

For anyone familiar with mirroring, it’s quite exciting to see such a project taking shape. Free software and Linux distributions have been distributed thanks to community-supported mirrors [for almost three decades now](http://www.ibiblio.org/pub/historic-linux/distributions/debian-0.91/debian-0.91/RELEASE-0.91), it’s a long tradition. It’s true that we’ve seen some changes over the last years, and these days some of the biggest FOSS projects [are entirely distributed via a CDN](https://news.apache.org/foundation/entry/apache-software-foundation-moves-to), leaving behind the mirroring system. For Kali Linux we use a mixed approach: it is distributed in part thanks to 50+ mirrors across the world, and in part thanks to the Cloudflare CDN that acts as a ubiquitous mirror. We are lucky to benefit from a [very generous sponsorship from Cloudflare](https://blog.cloudflare.com/cloudflare-repositories-ftw) since 2019. But smaller or newer projects don’t get this chance, thus community mirrors are still essential to free software distribution. That’s why it’s nice to see a project like the Micro Mirror CDN, it’s a novel approach in the field of mirroring, and with Kali Linux we are very grateful to be part of the journey.

For any organization out there that has spare bandwidth and wants to support free software, the Micro Mirror project might be something you are interested in. You might want to look at their [product brief](https://github.com/PhirePhly/micromirrors/blob/main/doc/product-brief.md) for a more thorough description of the service, and email mirror at fcix dot net for more information. we’ll just quote one line that summarize it really well:

From the hosting sponsor’s perspective, the Micro Mirror is a turnkey appliance, where they only need to provide network connectivity and remote hands to install the hardware, where all sysadmin and monitor work is handled by the FCIX team with the economy of scale on our side.

A big thanks to the FCIX team, and Kenneth Finnegan in particular, for their generous offer. Thanks to their help, the Kali images are now served from ten additional mirrors: seven in the US, one in Colombia, one in the UK and one in Australia.

And while we are talking about mirrors: we also got plenty of new mirrors from various sponsors during this release cycle, check the [dedicated section below](#new-kali-mirrors) for details.

### 2024 Theme RefreshAs for previous 20**.1 releases, this update brings with it our annual theme refresh, a tradition that keeps our interface as cutting-edge as our tools. This year marks the unveiling of our newest theme, meticulously crafted to enhance user experience from the moment you boot up. With significant updates to the boot menu, login display, and an array of captivating desktop wallpapers, for both our regular Kali and Kali Purple editions. We are dedicated to not only advancing our cybersecurity capabilities but also ensuring that the aesthetic appeal of our platform matches the power within.

Boot menu:

https://www.kali.org/blog/kali-linux-2024-1-release/images/boot-menu.png

Login display:

https://www.kali.org/blog/kali-linux-2024-1-release/images/login.png

Desktop:

https://www.kali.org/blog/kali-linux-2024-1-release/images/desktop.png

Kali-Purple desktop:

https://www.kali.org/blog/kali-linux-2024-1-release/images/desktop-purple.png

New wallpapers:

https://www.kali.org/blog/kali-linux-2024-1-release/images/wallpapers.png

Special thanks to [arszilla](https://gitlab.com/arszilla) for not only suggesting two wallpaper variants but also contributing to the creation of one of the default wallpapers featured in this release. These additional images were crafted to complement the background colors of the Nord and Dracula color schemes. To access these wallpapers, simply install the kali-community-wallpapers package, which also offer many other stunning backgrounds created by our community contributors.

https://www.kali.org/blog/kali-linux-2024-1-release/images/dracula-nord-wallpapers.png

### Other desktop changes#### XfceWe are excited to introduce a convenient enhancement to our Xfce desktop. Now, users can effortlessly copy their VPN IP address to the clipboard with just a click, simplifying the workflow and enhancing productivity for our users. To take advantage of this functionality, ensure that xclip is installed on your system (sudo apt update && sudo apt -y install xclip). With this improvement, managing your VPN connections on Kali Linux becomes even more seamless and intuitive.

Thank you [lucas.parsy](https://gitlab.com/lucas.parsy) for your contribution that made this feature possible!

https://www.kali.org/blog/kali-linux-2024-1-release/images/vpn-plugin.png

Other Xfce changes:

- Kali-undercover updated to fix compatibility with latest Xfce
- Fixed a bug with xfce-panel and Kali’s customized cpugraph plug-in

#### Gnome-ShellFor Gnome desktop one notable change is the replacement of the eye-of-gnome (eog) image viewer with Loupe, continuing the transition to GTK4 based applications. Additionally, the latest update of Nautilus file manager arrived to Kali’s repositories, delivering a significant boost in file search speed and introducing a refreshed sidebar design.

https://www.kali.org/blog/kali-linux-2024-1-release/images/gnome.png

#### Icon ThemeFollowing with the desktop enhancements, we’ve added a few new app icons, ensuring a fully themed experience for default installations of Kali Linux. Additionally, we’ve refreshed our icon theme with new symbolic icons, enhancing consistency system-wide.

https://www.kali.org/blog/kali-linux-2024-1-release/images/icons.png

### Kali NetHunter Updateshttps://www.kali.org/blog/kali-linux-2024-1-release/images/NetHunter-S24Ultra.png

We finally got our hands on a brand new Samsung Galaxy S24 Ultra and yes!, [NetHunter rootless](https://www.kali.org/docs/nethunter/nethunter-rootless/) runs like a dream. Fortunately, Android 14 lets us disable child process restrictions in developer settings so we no longer have to use the adb command line to enable [KeX support](https://www.kali.org/docs/nethunter/nethunter-kex-manager/).
We have updated our [documentation](https://www.kali.org/docs/nethunter/nethunter-rootless/) to reflect these changes.

[yesimxev](https://gitlab.com/yesimxev) managed to add the popular Bad Bluetooth HID attack the the NetHunter app for both phones and even smartwatches!

Your browser does not support the video tag.The icons for our NetHunter and NHTerm apps have received a makeover and [@kimocoder](https://gitlab.com/kimocoder) & [@martinvlba](https://twitter.com/martindatoss) spent countless days updating the codebase to ensure compatibility with the latest Android version.

The community engagement is at an all time high, which is reflected by the following [new kernels](https://nethunter.kali.org/kernels.html):

- Realme C15
- TicWatch Pro 3
- (Updated) Samsung Galaxy S9+
- Xiaomi Poco X3 NFC

Thanks heaps to everyone that [contributed](https://www.kali.org/docs/community/contribute/), we wouldn’t be here without you!

Stay tuned as there are many more kernels already on the way!

### New Tools in KaliThe following new tools made it into this Kali release (via the network repositories):

- [blue-hydra](https://www.kali.org/tools/blue-hydra/) - Bluetooth device discovery service
- [opentaxii](https://www.kali.org/tools/opentaxii/) - TAXII server implementation from EclecticIQ
- [readpe](https://www.kali.org/tools/readpe/) - Command-line tools to manipulate Windows PE files
- [snort](https://www.kali.org/tools/snort/) - Flexible Network Intrusion Detection System

The focus was adding new libraries this release, and there is always numerous packages updates. Plus we also bump the Kali kernel to 6.6!

#### Community PackagesThere has also been a tool submitted from the community which has been merged into Kali:

- [above](https://www.kali.org/tools/above/) - Invisible protocol sniffer for finding vulnerabilities in the network

If you are wanting a tool in Kali quicker than what we can add, please see [our blog post from a previous release](https://www.kali.org/blog/kali-linux-2023-3-release/#rekono---community-package-submission).

### MiscellaneousBelow are a few other things which have been updated in Kali, which we are calling out which do not have as much detail:

- Due to the ongoing /usr-merge transition in Debian, using 2023.4 or older versions of [our netboot images](https://www.kali.org/docs/installation/network-pxe/#download-kali-pxe-netboot-images) will no longer work. Make sure to either grab weekly image or Kali 2024.1!
- Friendly reminder, if you are getting “weird special characters” when trying to use keyboard shortcuts to copy/paste clipboard, the default is to use “ctrl+shift+c” and “ctrl+shift+v”.ctrl+c (without shift) in Unix is used to kill programs!
- Should you wish, you can alter the default behaviour in your favourite terminal program

### Kali Website Updates#### Kali DocumentationOur [Kali documentation](https://www.kali.org/docs/) has had various updates:

- [Installing VMware on Apple Silicon (M1/M2/M3) Macs (Host)](https://www.kali.org/docs/virtualization/install-vmware-silicon-host/) (updated)
- [Kali Installation Sizes](https://www.kali.org/docs/installation/installation-sizes/) (updated)

A way to make a project even stronger is to help its [documentation](https://www.kali.org/docs/). Kali is no exception. If you are able to please do [contributed](https://www.kali.org/docs/community/contribute/).

#### Tool DocumentationOur [tool documentation](https://www.kali.org/tools/) is always getting various updates from us, but we received a great contribution from [Daniel](https://gitlab.com/etd):

- [Dradis](https://www.kali.org/tools/dradis/)

If you are wanting to help Kali, and give back, submitting to [kali.org/tools](https://www.kali.org/tools/) is a great way to [contributed](https://www.kali.org/docs/community/contribute/).

#### Kali Blog RecapSince our last release, we did the following [blog posts](https://www.kali.org/blog/):

- [The great non-free-firmware transition](https://www.kali.org/blog/non-free-firmware-transition/)
- [Kali Linux DEI Promise](https://www.kali.org/blog/dei-promise/)

### Community Shout-OutsThese are people from the public who have helped Kali and the team for the last release. And we want to praise them for their work (we like to give credit where due!):

- [Arszilla](https://gitlab.com/Arszilla)
- [Caster](https://gitlab.com/casterbyte)
- [Daniel](https://gitlab.com/etd)
- [Jane Rysavy](https://gitlab.com/janerysavy17)
- [Jordan](https://gitlab.com/Fetti.Wop)
- [Lucas Parsy](https://gitlab.com/lucas.parsy)
- [ronbo](https://gitlab.com/ronbo)

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

#### New Kali MirrorsWe have some new mirrors! Plenty of new mirrors, in fact. The last quarter was quite incredible on this front, and now is the time to give credits.

Let’s start with North America:

- US: [mirror.fcix.net](http://mirror.fcix.net/kali-images/) sponsored by FCIX aka. the [Fremont Cabal Internet Exchange](https://fcix.net/). Thanks to Kenneth Finnegan for reaching out… one and a half year ago! Thankfully we rediscovered the email and that was worth it.
- Canada: [mirror.xenyth.net](http://mirror.xenyth.net/kali-images/) sponsored by [Xenyth Cloud](https://xenyth.net/), and thanks to Sepehr Ahmadi.
- Canada: [mirror.quantum5.ca](http://mirror.quantum5.ca/kali-images/) sponsored by [Dynamic Quantum Networks](https://dynamicquantum.net), and thanks to Guanzhong Chen.
- Canada: [mirror.accuris.ca](http://mirror.accuris.ca/kali/) sponsored by [Accuris Technologies Ltd.](https://accuristechnologies.ca/), thanks to Peter Potvin.
- Canada: [mirror.0xem.ma](http://mirror.0xem.ma/kali/) sponsored by [Emma Ruby](https://0xem.ma/).

Now for the rest of the world:

- Chile: [elmirror.cl](http://elmirror.cl/kali/), sponsored by [ElMirror](https://elmirror.cl/), and thanks to Jonathan Gutierrez, who also maintains the other Kali Linux mirror in Chile: [mirror.ufro.cl](https://mirror.ufro.cl/). As a reminder: we really lack mirrors in South America, any help would be welcome to help Kali reach this part of the world.
- China: [mirrors.ustc.edu.cn](http://mirrors.ustc.edu.cn/kali/), sponsored by the USTC aka. the [University of Science and Technology of China](https://en.ustc.edu.cn/), and thanks to Keyu Tao.
- France: [mirror.johnnybegood.fr](http://mirror.johnnybegood.fr/kali/), sponsored by the [Johnnybegood Society](https://johnnybegood.fr/).
- Portugal: [mirror.leitecastro.com](http://mirror.leitecastro.com/kali/), sponsored by [Tomás Leite de Castro](https://leitecastro.com/).
- South Korea: [mirror.amuksa.com](http://mirror.amuksa.com/kali/).

On top of that, as said above, there is now the Micro Mirror CDN that serves Kali images via 10 points of presence: 7 in the US, 1 in Colombia, 1 in the UK and 1 in Australia!

To wrap that up: THANK YOU to all of you, individuals and companies, who provide bandwidth and help us distribute Kali to everyone out there!

If you have the disk space and bandwidth, [we always welcome new mirrors](https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/).

### Kali Team Discord ChatSince the launch of [our Discord server](https://discord.kali.org/) with [Kali 2022.3](https://www.kali.org/blog/kali-linux-2022-3-release/), we have been doing an hour long voice chat with a number of Kali team members. This is when anyone can ask questions (hopefully relating to Kali or the information security industry) to us.

The next session will happen a little later than normal, Friday, 22nd March 2024 18:00 -> 19:00 [UTC/+0 GMT](https://time.is/UTC).
It will once again be on [OffSec’s Discord](https://discord.com/servers/offsec-780824470113615893).

- [Discord invite](https://discord.gg/invite/offsec)
- [iCalendar invite](./Kali-Discord-2024.1.ics)

Please note, we will not be making a recording of this event - its live only.

### Get Kali Linux 2024.1Fresh Images:
So what are you waiting for? Go [get Kali](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for those who are not, we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you will have fewer updates to do.
Just know that these are automated builds that we do, not QA like we do for our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~/
[...]

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2024.1. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2024.1"
VERSION_ID="2024.1"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Kali 6.6.9-1kali1 (2024-01-08)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.6.9-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And Social networks are not bug trackers!

Want to keep in up-to-date easier? Automate it! We have a [RSS feeds](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/) of our [blog](https://www.kali.org/blog/) to help you.

## 2023.4 – 2023-12-05

**Kali Linux 2023.4 Release (Cloud ARM64, Vagrant Hyper-V & Raspberry Pi 5)**

Table of Contents
- [Cloud ARM64 Marketplaces](#cloud-arm64-marketplaces)
- [Vagrant Hyper-V Support](#vagrant-hyper-v-support)
- [Raspberry Pi 5](#raspberry-pi-5)
- [GNOME 45](#gnome-45)
- [Internal Infrastructure](#internal-infrastructure)[Enters Mirrorbits](#enters-mirrorbits)

- [New Tools in Kali](#new-tools-in-kali)[Community Packages](#community-packages)

- [Miscellaneous](#miscellaneous)
- [Kali NetHunter Updates](#kali-nethunter-updates)
- [Kali ARM Updates](#kali-arm-updates)
- [Kali Website Updates](#kali-website-updates)
- [Community Shout-Outs](#community-shout-outs)[New Kali Mirrors](#new-kali-mirrors)

- [Kali Team Discord Chat](#kali-team-discord-chat)
- [Get Kali Linux 2023.4](#get-kali-linux-20234)

With 2023 coming to an end and before the holiday season starts, we thought today would be a good time to [release](https://www.kali.org/releases/) Kali 2023.4. Whilst this release may not have the most end-user features in it again, there are a number of new platform offerings and there has still been a lot of changes going on behind-the-scenes for us, which has a positive knock-on effect resulting in a benefit for everyone.
News, platforms, and features aside, it would not be a Kali release if there was not a number of changes to our packages - both new tools and upgrades to existing ones.
If you want to see what is new for yourself [download](https://www.kali.org/get-kali/) a new image or [upgrade if you already have a Kali Linux installation](https://www.kali.org/docs/general-use/updating-kali/).

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2023.3 release from August](https://www.kali.org/blog/kali-linux-2023-3-release/) is:

- [Cloud ARM64](#cloud-arm64-marketplaces) - Now Amazon AWS and Microsoft Azure marketplaces have an ARM64 option
- [Vagrant Hyper-V](#vagrant-hyper-v-support) - Our Vagrant offering now supports Hyper-V
- [Raspberry Pi 5](#raspberry-pi-5) - Kali on the latest Raspberry Pi foundation device
- [GNOME 45](#gnome-45) - Kali theme is on the latest versions
- [Internal Infrastructure](#internal-infrastructure) - Peak at what is going on behind the scenes with mirrorbits
- [New Tools](#new-tools-in-kali) - As always, various new & updated packages

### Cloud ARM64 MarketplacesStarting from Kali 2023.4, we will now be offering both Kali Linux AMD64 and ARM64 on [Amazon AWS](https://aws.amazon.com/marketplace/seller-profile?id=3fd16b5c-a3f6-43b5-b254-0a6ae8f6a350) and [Microsoft Azure](https://azuremarketplace.microsoft.com/en/marketplace/apps/kali-linux.kali?tab=overview) marketplaces.

The advantage that ARM64 brings to the table is more options and flexibility in instance offerings, which leads to improved price-to-performance ratio.
The draw back is, even though Kali Linux has always treated ARM a first class citizen, not every package has an ARM64 offering - most do and we are working on improving this every day!
Try setting up a lab in the cloud and performing your own benchmarks to compare performances.

Amazon AWS:

- [Kali Linux (AMD64)](https://aws.amazon.com/marketplace/pp/prodview-fznsw3f7mq7to)
- [Kali Linux (ARM64)](https://aws.amazon.com/marketplace/pp/prodview-kie6xvt5r3spi)

Microsoft Azure:

- [Kali Linux](https://azuremarketplace.microsoft.com/en/marketplace/apps/kali-linux.kali?tab=overview)

https://www.kali.org/blog/kali-linux-2023-4-release/images/kali-azure-arm64.png

If you need some help using Kali Linux in the cloud, be sure to check our [documentation](https://www.kali.org/docs/cloud/).
Otherwise, if you want to see how we generate these images, see our [cloud build-scripts](https://gitlab.com/kalilinux/build-scripts/kali-cloud).

### Vagrant Hyper-V SupportWith [our recent work](https://www.kali.org/blog/kali-linux-2023-2-release/#new-hyper-v-vm-image) with adding support to our [VM build-scripts](https://gitlab.com/kalilinux/build-scripts/kali-vm) to create Microsoft Hyper-V virtual machines, we have kept on going down the rabbit hole of development. [Our Vagrant offering](https://app.vagrantup.com/kalilinux/boxes/rolling) now includes a Hyper-V environment!

If you are not too familiar with Vagrant, think of it as a command-line interface for VMware, VirtualBox, and now Hyper-V.

At a higher level, in the same way that Docker uses Dockerfile, Vagrant uses Vagrantfile.
These files go on to define how to create the virtual machine and further provisions, such as which operating system to use, CPU, RAM, storage, networking, and also any scripts or commands that the VM should execute to further install and configure.

That means our [our Vagrant offering](https://app.vagrantup.com/kalilinux/boxes/rolling) has support for:

- Hyper-V
- QEMU
- VirtualBox
- VMware

If this is something you like the sound of, we have further reading on our documentation:

- [Customizing a Kali Vagrant Vagrantfile](https://www.kali.org/docs/virtualization/customizing-kali-vagrant/)
- [Kali inside Vagrant (Guest VM)](https://www.kali.org/docs/virtualization/install-vagrant-guest-vm/)

We also have our [vagrant build-scripts](https://gitlab.com/kalilinux/build-scripts/kali-vagrant) public if you want to see how it is done.

### Raspberry Pi 5If you have been lucky enough to get your hands on the newest Raspberry Pi, Kali Linux can now be used on a Raspberry Pi 5!

We have created a new dedicated image which can either be [downloaded direct](https://www.kali.org/get-kali/#kali-arm), or automated using [Raspberry Pi Imager](https://www.kali.org/docs/arm/using-rpi-imager-to-write-raspberry-pi-images/).

You can [build the image yourself](https://gitlab.com/kalilinux/build-scripts/kali-arm) if you wish to tinker and customize any aspect of it, such as changing the default desktop environment, packages, settings etc.

Please note, Nexmon support is not yet working with the in-built Wi-Fi (so no monitor mode or frame injection without an external card).

You can keep an eye on progress by checking our [documentation](https://www.kali.org/docs/arm/raspberry-pi-5/) about it. Please keep in mind that while the image is now available for use, we would consider it to be in a BETA state. For the time being, the image is for ARM64 architecture, hopefully additional flavors will come later.

We want to give a huge shout-out as there were a lot of volunteers from the community who were willing to test and report issues with the image.
There was one person who really stood out, and this image would not be possible without BakaValen’s assistance, support, reporting of issues, and ideas.

Additionally, David Bombal’s [Raspberry Pi 5 Kali Linux install in 10 minutes](https://youtube.com/watch?v=paN5F1EmjfA) came out to show off our initial work of Kali Linux on the Raspberry Pi 5.

### GNOME 45With GNOME 45 hot off the press, Kali Linux is now supporting it! And is looking pretty in the process!

https://www.kali.org/blog/kali-linux-2023-4-release/images/gnome-45.png

For people who opt to use GNOME as their desktop environment, [GNOME 45](https://release.gnome.org/45/) is now here! If you do not read their changelog, below is a quick summary mixed with some of our tweaks:

- Full-height sidebars in many updated apps
- Highly improved speed of search in nautilus file managerUnfortunately the update for nautilus was not ready for this release, but it will arrive as a later update soon

- Improved settings app (gnome-control-center)
- Updated color-schemes for gnome-text-editor
- Updated themes for shell, libadwaita, gtk-3 and gtk-4
- Updated gnome-shell extensions
- Shell updates, including a new workspace indicator, replacing the previous “Activities” buttonIt is also possible to scroll your mouse wheel while hovering over the indicator to switch between workspaces

https://www.kali.org/blog/kali-linux-2023-4-release/images/gnome-45-activities-indicator.gif

### Internal InfrastructureWe are still undergoing big changes with our infrastructure, and as always, it is taking longer than planned! The wait has been worth it, and long standing items are getting fixed or replaced!

#### Enters MirrorbitsOne of the projects which is now complete is the migration of our “mirror redirector”. This is our biggest user-facing service, as without this, all default Kali installations would not be able to use apt (aka http.kali.org), or being able to download Kali image (cdimage.kali.org). This service sits in-front of our mirrors (archive*.kali.org), [community mirrors](https://http.kali.org/README?mirrorlist) and Cloudflare (kali.download). It is responsible for redirecting every request to its nearest mirror, based on a few factors such as geographic location, mirror speed, and [mirror “freshness”](https://mirror-traces.kali.org/).

Since Kali was launched back in March 2013, until November 2023 we had been using [MirrorBrain](https://mirrorbrain.org/). Unfortunately, the project has been unmaintained since 2015, and so after 10 years in production, it was really time to say good-bye. Today, we are now using [Mirrorbits](https://github.com/videolabs/mirrorbits).

The first thing we can say is that, with Mirrorbits, we find ourselves lucky: this is a rock-solid piece of software, built on modern tech (Go and Redis), initially released 10 years ago, and running in production for just as long. It was initially developed by [Ludovic Fauvet](https://blog.l0cal.com/) from VideoLAN in order to distribute the VLC media player. And over these years, it has been adopted by a growing number of FOSS projects such as GNOME, Jenkins, Lineage OS, and many others.

As it happens, our use-case of Mirrorbits is different to what it was originally created for: distributing VLC, or in other words, a rather small set of static files. Kali Linux being a complete Linux distribution, it means that we distribute a huge number of files (at times there can be millions of files in our repo). Being a rolling distribution means that Mirrorbits must cope with fast-changing metadata in the repository. We also need to distribute Kali over both HTTP and HTTPS, which was not well supported.

Thus, the transition to Mirrorbits was not trivial, it did not work “out-of-the-box” for us, and we had to rework some pieces here and there, and basically hammer at it until it does the job. But it was well worth it, and in the end our modifications were clean enough that we could submit it all [upstream](https://github.com/videolabs/mirrorbits). We really hope that all of this work will be accepted, thus making it easier for Linux distributions in general to use Mirrorbits going forward. Oh, and we have created and are maintaining the [Debian package](https://tracker.debian.org/pkg/mirrorbits)!

Much more could be written on the topic, and we plan a longer blog post dedicated to it. But for now, enough’s been said.

### New Tools in KaliIt would not be a Kali release if there were not any new tools added! A quick run down of what has been added (to the network repositories):

- [cabby](https://pkg.kali.org/pkg/cabby) - TAXII client implementation
- [cti-taxii-client](https://pkg.kali.org/pkg/cti-taxii-client) - TAXII 2 client library
- [enum4linux-ng](https://www.kali.org/tools/enum4linux-ng/) - Next generation version of enum4linux with additional features (a Windows/Samba enumeration tool)
- [exiflooter](https://www.kali.org/tools/exiflooter/) - Finds geolocation on all image URLs and directories
- [h8mail](https://www.kali.org/tools/h8mail/) - Email OSINT & Password breach hunting tool
- [Havoc](https://www.kali.org/tools/havoc/) - Modern and malleable post-exploitation command and control framework
- [OpenTAXII](https://pkg.kali.org/pkg/opentaxii) - TAXII server implementation
- [PassDetective](https://www.kali.org/tools/passdetective/) - Scans shell command history to detect mistakenly written passwords, API keys, and secrets
- [Portspoof](https://www.kali.org/tools/portspoof/) - All 65535 TCP ports are always open & emulates services
- [Raven](https://www.kali.org/tools/raven/) - Lightweight HTTP file upload service
- [ReconSpider](https://www.kali.org/tools/reconspider/) - Most Advanced Open Source Intelligence (OSINT) Framework
- [rling](https://www.kali.org/tools/rling/) - RLI Next Gen (Rling), a faster multi-threaded, feature rich alternative to rli
- [Sigma-Cli](https://www.kali.org/tools/sigma-cli/) - List and convert Sigma rules into query languages
- [sn0int](https://www.kali.org/tools/sn0int/) - Semi-automatic OSINT framework and package manager
- [SPIRE](https://www.kali.org/tools/spire/) - SPIFFE Runtime Environment is a toolchain of APIs for establishing trust between software systems

There have also been numerous packages updates and new libraries as well. We also bump the Kali kernel to 6.5.0!

#### Community PackagesThere have been multiple tools submitted from the community, ready to be merged into Kali:

- [h8mail](https://www.kali.org/tools/h8mail/) - Credit to: [Jason “5nacks” Kregting](https://github.com/5nacks) & [TraceLabs](https://github.com/tracelabs)
- [PassDetective](https://www.kali.org/tools/passdetective/) - Credit to: [Yunus “aydinnyunus” AYDIN](https://gitlab.com/yunusaydin0)
- [sn0int](https://www.kali.org/tools/sn0int/) - Credit to: [kpcyrd](https://vulns.xyz/)

For more information about this, please see [our blog post from previous release](https://www.kali.org/blog/kali-linux-2023-3-release/#rekono---community-package-submission).

### MiscellaneousBelow are a few other things which have been updated in Kali, which we are calling out which do not have as much detail on:

- We have changed [our newsletter](https://www.kali.org/newsletter/) provider to Substack!If you want our blog posts, and only that in your inbox, sign up!

- We have seen an [issue with VMware currently (VMware workstation 17.5), where it appears input (keyboard/mouse) will freeze](https://github.com/vmware/open-vm-tools/issues/696) after a period of timeCheck the above link for a workaround solution
- If you use [our pre-generated VMs](https://www.kali.org/get-kali/#kali-virtual-machines), the patch has already been applied

- There also appears to be an issue with KDE inside a virtual machine, where certain functions between host/guest are not working, such as shared clipboard (copy/paste)
- We have added support for QT6 themes
- A friendly reminder about [Python v3.12 PIP install change which will alter “soon”](https://www.kali.org/blog/python-externally-managed/)

### Kali NetHunter UpdatesWe have seen a few things from the community worth calling out:

- [Doom on @kalilinux NetHunter TicWatch Pro 3](https://twitter.com/yesimxev/status/1725792218512847358)
- [Kali Linux NetHunter install in 8 minutes (rootless) and includes Android 14](https://www.youtube.com/watch?v=GmfM8VCAu-I)
- [How I Ported Kali NetHunter to Unsupported Device - Essential Phone](https://odysee.com/@z2rec:1/how-i-ported-kali-nethunter-to-unsupported-device:c)

### Kali ARM UpdatesThere are not a lot of changes to the ARM images this release, aside from the previously mentioned Raspberry Pi 5 support. However, they are no less important.

- The Raspberry Pi Zero W image now properly starts up into the command line interface instead of launching X.
- Accessing network configuration remotely now properly works again.
- [eyewitness](https://www.kali.org/tools/eyewitness/) is now available for ARM64 platform.

### Kali Website UpdatesWe have recently created a [Frequently Asked Questions](https://www.kali.org/faq/) with answers that we commonly keep seeing crop up.

Our [Kali documentation](https://www.kali.org/docs/) has had various updates to existing pages as well as new pages:

- [Configuring the Kernel - NFS](https://www.kali.org/docs/nethunter/nethunter-kernel-8-config-7/) (new)
- [Kali Installation Sizes](https://www.kali.org/docs/installation/installation-sizes/) (new)
- [Raspberry Pi 5](https://www.kali.org/docs/arm/raspberry-pi-5/) (new)
- [Raspberry Pi-Tail Zero W](https://www.kali.org/docs/arm/raspberry-pi-zero-w-pi-tail/) (updated)

We also want to say a little thank you to following for their work on the sites:

- [David Verbenyi](https://gitlab.com/dverbenyi)
- [Heikki Miinalainen](https://gitlab.com/Hegezcc)
- [Brian Matus](https://gitlab.com/matusb42)
- [X0RW3LL](https://gitlab.com/X0RW3LL)
- [yesimxev](https://gitlab.com/yesimxev)

### Community Shout-OutsThese are people from the public who have helped Kali and the team for the last release. And we want to praise them for their work (we like to give credit where due!):

- [AI Program](https://gitlab.com/aiprogram.v32) - Helped testing base images
- BakaValen - Helped with testing, troubleshooting and offering ideas with the Raspberry Pi 5 image
- [David Bombal](https://www.youtube.com/@davidbombal) - Helped with testing the Raspberry Pi 5 image
- [Salty_](https://gitlab.com/Salty_) - Helped with testing base images
- [X0RW3LL](https://gitlab.com/X0RW3LL) - Helped with testing base images

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

#### New Kali MirrorsWe have some new mirrors! Those are:

- Japan: [repo.jing.rocks](http://repo.jing.rocks/kali). Thanks to Jing Luo for reaching out and hosting this mirror!
- Serbia: [mirror1.sox.rs](http://mirror1.sox.rs/kali) sponsored by SOX, the [Serbian Open eXchange](https://www.sox.rs/en/). Thanks to Sasa Ristic for reaching out to us!

If you have the disk space and bandwidth, [we always welcome new mirrors](https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/).

### Kali Team Discord ChatOnce the Kali release is over, we have been doing an hour long voice chat with a number of Kali team members. This is where anyone can ask questions to us about Kali or the information security industry as a whole.

The next session will be held slightly differently to our previous ones, later in the day, on the Friday that is coming up, and on [OffSec’s Discord](https://discord.com/servers/offsec-780824470113615893) - Friday, 8th December 2023 18:00 -> 19:00 [UTC/+0 GMT](https://time.is/UTC) ([Discord](https://discord.gg/invite/offsec) link & [iCalendar](./Kali-Discord-2023.4.ics) invite).

Please note, there will not be a recording of this - its live only.

### Get Kali Linux 2023.4Fresh Images:
So what are you waiting for? Go and [grab Kali](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for the ones who are not, we do also have [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use as well. If you cannot wait for our next release next quarter to get the latest packages or bug fixes you can download these images instead.
Just know that these are automated builds that we do not QA like we do our standard [point release images](https://www.kali.org/releases/). We also welcome any [bug reports](https://bugs.kali.org/) about those images too!!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~/
[...]

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2023.4!
We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2023.4"
VERSION_ID="2023.4"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Debian 6.5.6-1kali1 (2023-10-09)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.5.0-kali3-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you discover any issues with Kali, please search then submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And social networks are not bug trackers!

Want to keep up-to-date? Easy!
We have a [RSS feeds](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/) of our [blog](https://www.kali.org/blog/) to help you. Our social networks are in the footer of this page!

## 2023.3 – 2023-08-23

**Kali Linux 2023.3 Release (Internal Infrastructure & Kali Autopilot)**

Table of Contents
- [Internal Infrastructure](#internal-infrastructure)[Mirror Traces](#mirror-traces)
- [Packaging Tools](#packaging-tools)

- [Kali Autopilot](#kali-autopilot)
- [New Tools in Kali](#new-tools-in-kali)[Rekono - Community Package Submission](#rekono---community-package-submission)

- [Miscellaneous](#miscellaneous)
- [Kali NetHunter Updates](#kali-nethunter-updates)
- [Kali ARM Updates](#kali-arm-updates)
- [Kali Website Updates](#kali-website-updates)
- [Community Shout-Outs](#community-shout-outs)[New Kali Mirrors](#new-kali-mirrors)

- [Kali Team Discord Chat](#kali-team-discord-chat)
- [Get Kali Linux 2023.3](#get-kali-linux-20233)

Today we are delighted to introduce our latest [release of Kali](https://www.kali.org/releases/), 2023.3. This release blog post does not have the most features in it, as a lot of the changes have been behind-the-scenes, which brings a huge benefit to us and an indirect positive effect to you as end-users. It always goes without saying, but there are a number of new packages and tools as well as the standard updates. If you want to see what’s new for yourself [download](https://www.kali.org/get-kali/) or [upgrade if you have an existing Kali Linux installation](https://www.kali.org/docs/general-use/updating-kali/).

The highlights of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2023.2 release from May](https://www.kali.org/blog/kali-linux-2023-2-release/):

- [Internal Infrastructure](#internal-infrastructure) - Major stack changes is under way
- [Kali Autopilot](#kali-autopilot) - The automation attack framework has had an major overhaul
- [New Tools](#new-tools-in-kali) - 9 new tools added this time round!

### Internal InfrastructureWith the release of Debian 12 which came out this summer, we took this opportunity to re-work, re-design, and re-architecture our infrastructure. It is as massive as it sounds, and should not be a surprise that its not yet complete! This is where a good amount of our focus has been for this release-cycle (and also the next one unfortunately). We are hoping that the majority of it will be done by the end of the year (so we can get back to what we do best!)

This gives an excuse and the motivation to simplify our software stack as much as possible.
Example, using one single:

- OS version (Debian 12)
- CDN/WAF (Cloudflare)
- Web server service (Nginx)
- Infrastructure as Code (Ansible)

We also have some other goals, and replacing certain software with others (phase #2).

At the same time, we have automated some actions such as:

- The cleaning up of suites (aka [branches](https://www.kali.org/docs/general-use/kali-branches/) - kali-experimental and [kali-bleeding-edge](https://www.kali.org/docs/general-use/kali-bleeding-edge/))

We are very much underway with these projects already (as bug bounty hunters may notice the changes)!

#### Mirror TracesWe have a new sub-domain, [mirror-traces.kali.org](https://mirror-traces.kali.org/)! This is to help mirror admins for our community mirrors. This now gives everyone using it more details and insight which is useful when troubleshooting and debugging issues.

True to our word, we are doing more in the open, the git repository can be found here: [gitlab.com/kalilinux/tools/mirror-status](https://gitlab.com/kalilinux/tools/mirror-status).

#### Packaging ToolsFor a long time, we have shared our [home-made scripts](https://gitlab.com/kalilinux/tools/packaging) publicly, which is our helping aid to manage all our packages in Kali.
Recently we have expanded on them by giving the existing files a refresh by adding additional features and various quality-of-life improvements, as well as including new ones.

As a recap, if you want to have a peek at some back-end development:

- [Autopkgtest](https://autopkgtest.kali.org/) - Using debci in a CI fashion, we can test packages being built.This integrates into Britney.

- [Britney2](http://repo.kali.org/britney) ([Git repo](https://gitlab.com/kalilinux/tools/britney2)) - Migrates packages between all of our suites (aka [branches](https://www.kali.org/docs/general-use/kali-branches/), such as “debian-testing”, “kali-rolling”, and “kali-last-snapshot” to name a few).
- [Build-Logs](http://repo.kali.org/build-logs/) - Output of [our images/platform](https://gitlab.com/kalilinux/build-scripts/) as well as [packages](https://gitlab.com/kalilinux/packages) being created on each supported architecture.
- Janitor - Kali Bot - This is our automated packager as it will apply everything from minor formatting changes to preparing an package update.The long term goal of this is to have it handle kali-bleeding-edge, linking into Autopkgtest.

- [Package Tracker](https://pkg.kali.org/) - Tracks each packages version’s history.
- [Packaging CI Overview](https://kalilinux.gitlab.io/tools/packaging/) ([Git repo](https://gitlab.com/kalilinux/tools/packaging/-/blob/main/bin/gitlab-overview?ref_type=heads)) - Quick (and dirty) overview of our package’s CI status.
- [Upstream-Watch](https://kalilinux.gitlab.io/tools/upstream-watch/) ([Git repo](https://gitlab.com/kalilinux/tools/upstream-watch)) - Monitors when there is an update upstream.

### Kali AutopilotWith the release of [Kali Purple](https://gitlab.com/kalilinux/kali-purple/documentation/-/wikis/home) in [Kali 2023.1](https://www.kali.org/blog/kali-linux-2023-1-release/), we also had the debut of [Kali Autopilot](https://gitlab.com/re4son/kali-autopilot/-/wikis/home). Since then, its been worked on and is unrecognizable with its redesigned GUI and multitudinous amount of features added.

What is Kali Autopilot? We are glad you asked!
Kali Autopilot is an automated attack framework. It is a bit like an “AutoPwner”, which follows pre-defined “attack scenarios”.
The motivation originally started its development for the defensive side of Kali.

It is a lot easier to demonstrate Kali’s offensive side, especially when you start seeing the shells popping up.
But when it comes to the defensive side, how do you know if you have set things up? You start to ask questions:

- Are the Intrusion Detection System (IDS) and the Web Application Firewall (WAF) detecting malicious activities?
- Is the Security information and event management (SIEM) ingesting the right logs?
- Are the dashboards and alerts tuned to detect attacks?
- Are the analysts trained in finding the needle in the haystack?
- Has it been tested? How can you test?

Either you can wait for someone to try and break in, or you could do it yourself. This is where Kali Autopilot comes in.

https://www.kali.org/blog/kali-linux-2023-3-release/images/kali-autopilot.png

Kali Autopilot consists of a GUI tool to design attacks and to generate attack scripts that perform those attack sequences, either manually or as a service, together with a web API interface for remote control.
You can also download example attack scripts from the [Kali Purple Hub](https://gitlab.com/kalilinux/kali-purple/purple-hub). We currently have scripts for [juice-shop](https://www.kali.org/tools/juice-shop/) and [DWVA](https://www.kali.org/tools/dvwa/). Just download the JSON from the hub and import it into Kali Autopilot.

This tool has come along a lot in the last 6 months, and no plans on slowing down. As always, its shaped by the [community](https://www.kali.org/community/); ideas, features, and direction can be submitted and shaped by YOU.
If you have developed attack scripts for vulnerable machines, we would love to include it on our [Kali Purple Hub](https://gitlab.com/kalilinux/kali-purple/purple-hub).

### New Tools in KaliWe will kick it off with what’s new (to the network repositories):

- [Calico](https://www.kali.org/tools/calico/) - Cloud native networking and network security
- [cri-tools](https://www.kali.org/tools/cri-tools/) - CLI and validation tools for Kubelet Container Runtime Interface
- [Hubble](https://www.kali.org/tools/hubble/) - Network, Service & Security Observability for Kubernetes using eBPF
- [ImHex](https://www.kali.org/tools/imhex/) - A Hex Editor for reverse engineers, programmers and people who value their retinas when working at 3 AM
- [kustomize](https://www.kali.org/tools/kustomize/) - Customization of kubernetes YAML configurations
- [Rekono](https://www.kali.org/tools/rekono-kbx/) - Automation platform that combines different hacking tools to complete pentesting processes
- [rz-ghidra](https://www.kali.org/tools/rz-ghidra/) - Deep ghidra decompiler and sleigh disassembler integration for rizin
- [unblob](https://www.kali.org/tools/unblob/) - Extract files from any kind of container formats
- [Villain](https://www.kali.org/tools/villain/) - C2 framework that can handle multiple reverse shells, enhance their functionality and share them among instances

We also bumped the Kali kernel to 6.3.7.

Along with new tools being added to Kali, there has been numerous packages and libraries updates, both major and minor version such as: [Greenbone](https://www.kali.org/tools/gvm/), [Humble](https://www.kali.org/tools/humble/), [Impacket](https://www.kali.org/tools/impacket/), [jSQL](https://www.kali.org/tools/jsql/), [OWASP ZAP](https://www.kali.org/tools/zaproxy/), [Rizin](https://www.kali.org/tools/rizin-cutter/), [Tetragon](https://www.kali.org/tools/tetragon/), [theHarvester](https://www.kali.org/tools/theharvester/), [Wireshark](https://www.kali.org/tools/wireshark/) and many many more.

Unfortunately [we had to drop a few packages](https://www.kali.org/docs/tools/removed-tools/) from Kali:

- [king-phisher](https://www.kali.org/tools/king-phisher/) - The tool is no longer maintained by the original authorAs an alternative, check [GoPhish](https://www.kali.org/tools/gophish/) as a replacement

- [plecost](https://www.kali.org/tools/king-phisher/) - Tool does not work with Python 3.11, and no response from original authorFor an replacement, try [WPScan](https://www.kali.org/tools/wpscan/)

#### Rekono - Community Package SubmissionWe get a large amount of requests to add tools into Kali. We do have a [policy of what tools are added to Kali](https://www.kali.org/docs/policy/penetration-testing-tools-policy/) and a process of how tools are packaged up and added (from network repositories to the default installed toolset). The draw back is that we do not have enough human power to be able to process them all.
Our solution to this has been to help tool authors and/or anyone from the [Kali community](https://www.kali.org/community/) create packages by writing a series of detailed, step-by-step guides covering the complete process and workflow of how we built those packages:

- [Setting up a system for packaging](https://www.kali.org/docs/development/setting-up-packaging-system/)
- [Introduction to packaging step-by-step example](https://www.kali.org/docs/development/intro-to-packaging-example/) - [Instaloader](https://www.kali.org/tools/instaloader/)
- [Intermediate packaging step-by-step example](https://www.kali.org/docs/development/intermediate-packaging-example/) - [Photon](https://www.kali.org/tools/photon/)
- [Advanced Packaging Step-By-Step Example](https://www.kali.org/docs/development/advanced-packaging-example/) - [FinalRecon](https://www.kali.org/tools/finalrecon/) & [Python-icmplib](https://pkg.kali.org/pkg/python-icmplib)
- [Packaging Applications with Kaboxer](https://www.kali.org/docs/development/packaging-apps-with-kaboxer/) - “Hello World” with a Docker container

When the tool was originally submitted by the tool author, we reviewed it, liked it, and agreed it should be in Kali. We did not have the cycles to process it ourselves quick enough, but the tool author did. They step up, and then re-submitted it again with them packaging up their tool.
This saved us a lot of leg work, so reviewing the package became a breeze, and shortly after was added into Kali.

If you are wanting a tool added into Kali - and you would like for it to happen sooner than we can do, have a go at trying to package yourself!
There are other sources of doing “Debian packaging” out there, as well as our linked guides above. There is a initial learning curve, but its not as complex as you may think (especially if you are comfortable using Linux).

Please note, we compile packages from [source](https://www.kali.org/docs/policy/kali-linux-open-source-policy/). Submitting a binary *.deb file will not be accepted.

### MiscellaneousBelow are a few other things which have been updated in Kali, which we are calling out which do not have as much detail:

- Added Pipewire support when using Hyper-V in enhanced session mode
- Added kali-hidpi-mode to support Kali-Purple
- Improved installation of Kali-Purple by removing the need to run any commands after installing kali-themes-purple
- Kali-Purple has a purple menu icon!
- The final reminder about [the breaking change with Python 3.12 & PIP](https://www.kali.org/blog/python-externally-managed/)

### Kali NetHunter UpdatesWe are proud to introduce a redesigned Kali NetHunter app and a completely new NetHunter Terminal, thanks to the amazing work of our very own [@martin](https://twitter.com/martindatoss) and [@yesimxev](https://gitlab.com/yesimxev).

On the [Kali NetHunter kernel](https://nethunter.kali.org/kernels.html) side, there are numerous updates:

- LG V20 for Lineage 19.1
- Nexus 6P for Android 8.0 (Oreo)
- Nothing Phone (1) for Android 12 (Snow cone) and 13 (Tiramisu) (new)
- Pixel 3/XL for Android 13 (Tiramisu)
- Samsung Galaxy A7 for LineageOS 18.1 (new)
- Xiaomi Mi A3 for Lineage 20
- Xiaomi Redmi 4/4X for VoltageOS 2.5

https://www.kali.org/blog/kali-linux-2023-3-release/images/NetHunter-Nothing.png

Also worth mentioning:

- By popular demand we have added a SELinux disabler.
- Please note until we are able to replace Mana Toolkit, we have had to temporary downgrade iptables.

### Kali ARM UpdatesThe [Raspberry Pi Zero W](https://www.kali.org/docs/arm/raspberry-pi-zero-w/) image now boots to CLI and not [GUI](https://www.kali.org/docs/general-use/switching-desktop-environments/).
This change is in line with what we did with the [Raspberry Pi 1](https://www.kali.org/docs/arm/raspberry-pi/) image a few releases ago. If you do not create a wpa_supplicant.conf to use, the easiest way to connect to a Wi-Fi network on the command line is to use the nmtui command.
Alternatively, you can use sudo nmcli --ask dev wifi connect network-ssid to have it ask you for the password on the command line, without it showing up in your history.

[USBArmory MKI](https://www.kali.org/docs/arm/usb-armory-mki/) and [MKII](https://www.kali.org/docs/arm/usb-armory-mkii/) have had their bootloaders updated to 2023.07.

The [ARM build scripts](https://gitlab.com/kalilinux/build-scripts/kali-arm/) have had some minor tweaks to deal with [policykit](https://pkg.kali.org/pkg/policykit-1) updates to make sure the pkla files are properly created.

### Kali Website UpdatesOur [Kali documentation](https://www.kali.org/docs/) has had various updates to existing pages as well as new pages:

- [Contribute to Kali](https://www.kali.org/docs/community/contribute/) (updated)
- [Deploying Kali over Network PXE Install](https://www.kali.org/docs/installation/network-pxe/) (updated)
- [Wayland](https://www.kali.org/docs/general-use/wayland/) (new)

A website is never complete, and our homepage is no exception. Recently we have been making some improvements:

- [Get Kali](https://www.kali.org/get-kali/) - Should be a little easier to scroll and move about the page now, switching between platforms
- [Partnerships](https://www.kali.org/partnerships/) - Updated to say a thank you to the new partnerships!

Since our last release, we also did the following [blog posts](https://www.kali.org/blog/):

- [Pip install and Python’s externally managed](https://www.kali.org/blog/python-externally-managed/)

### Community Shout-OutsThese are people from the public who have helped Kali and the team for the last release. And we want to praise them for their work (we like to give credit where due!):

- [Anutrix](https://gitlab.com/Anutrix) - who helped with [kali.org/docs/](https://www.kali.org/docs/)
- [Arszilla](https://gitlab.com/Arszilla) - who helped with [i3](https://www.kali.org/tools/kali-meta/)
- [Croluy](https://gitlab.com/Croluy) - who helped with [kali.org/docs/](https://www.kali.org/docs/)
- [Pablo Santiago López](https://github.com/pablosnt) - who helped with [rekono-kbx](https://www.kali.org/tools/rekono-kbx/)
- [ron190](https://gitlab.com/ron190) - who helped with [kali.org/tools/](https://www.kali.org/tools/)
- [Salty_](https://gitlab.com/Salty_) - helping with the Raspberry Pi release testing.

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

#### New Kali MirrorsWe have another community mirror:

- Armenia: [kali.mirror1.gnc.am](http://kali.mirror1.gnc.am/) and [kali.mirror2.gnc.am](http://kali.mirror2.gnc.am/), sponsored by [GNC-ALFA CJSC](http://www.gnc.am/), thanks to Vahe Avagyan.

If you have the disk space and bandwidth, [we always welcome new mirrors](https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/).

### Kali Team Discord ChatSince the launch of [our Discord server](https://discord.kali.org) with [Kali 2022.3](https://www.kali.org/blog/kali-linux-2022-3-release/), we have been doing an hour long voice chat with a number of Kali team members. This is when anyone can ask questions (hopefully relating to Kali or the information security industry) to us.

The next session will happen a week after the release, Wednesday, 30th August 2023 16:00 -> 17:00 [UTC/+0 GMT](https://time.is/UTC).

Please note we will not be recording this session. This is a live event only.

### Get Kali Linux 2023.3Fresh Images:
Simple, [Get Kali](https://www.kali.org/get-kali/)!

Did you know, we do also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use as well.
These are for people who cannot wait for our next release and you want the latest packages (or bug fixes). This way you will have fewer updates to do.
Just know that these are automated builds that we do, not QA like we do for our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~/
[...]

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2023.3. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2023.3"
VERSION_ID="2023.3"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Debian 6.3.7-1kali1 (2023-06-29)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.3.0-kali1-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And Social networks are not bug trackers!

Want to keep in up-to-date easier? Automate it! We have a [RSS feeds](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/) of our [blog](https://www.kali.org/blog/) to help you.

## 2023.2 – 2023-05-30

**Kali Linux 2023.2 Release (Hyper-V & PipeWire)**

Table of Contents
- [New Hyper-V VM Image](#new-hyper-v-vm-image)
- [Xfce & PipeWire](#xfce--pipewire)
- [i3 Desktop Overhaul](#i3-desktop-overhaul)
- [Desktop Updates](#desktop-updates)[Xfce](#xfce)
- [GNOME 44](#gnome-44)[Tiling Assistant Extension](#tiling-assistant-extension)

- [App Icons and Kali Menu Updates](#app-icons-and-kali-menu-updates)
- [New Tools in Kali](#new-tools-in-kali)
- [Miscellaneous](#miscellaneous)
- [Kali ARM Updates](#kali-arm-updates)
- [Kali Documentation Updates](#kali-documentation-updates)
- [Kali Blog Recap](#kali-blog-recap)
- [Community Shout-Outs](#community-shout-outs)[New Kali Mirrors](#new-kali-mirrors)

- [Kali Team Discord Chat Session](#kali-team-discord-chat-session)
- [Get Kali Linux 2023.2](#get-kali-linux-20232)

Quick off the mark from previous [10 year anniversary](https://www.kali.org/blog/10-years/), Kali Linux 2023.2 is now here. It is ready for immediate [download](https://www.kali.org/get-kali/) or [upgrading](https://www.kali.org/docs/general-use/updating-kali/) if you have an existing Kali Linux installation.

The [changelog](https://bugs.kali.org/changelog_page.php) highlights over the last few weeks since March’s [release](https://www.kali.org/releases/) of [2023.1](https://www.kali.org/blog/kali-linux-2023-1-release/) is:

- [New VM image for Hyper-V](#new-hyper-v-vm-image) - With “Enhanced Session Mode” out of the box
- [Xfce audio stack update: enters PipeWire](#xfce--pipewire) - Better audio for Kali’s default desktop
- [i3 desktop overhaul](#i3-desktop-overhaul) - i3-gaps merged with i3
- [Desktop updates](#xfce) - Easy hashing in Xfce
- [GNOME 44](#gnome-44) - Gnome Shell version bump
- [Icons & menus updates](#gnome-44) - New apps and icons in menu
- [New tools](#new-tools-in-kali) - As always, various new packages added

### New Hyper-V VM ImageWith this release, we welcome a new member in the family of pre-built VM images! We now provide an [image for Microsoft Hyper-V](https://www.kali.org/get-kali/#kali-virtual-machines).

For those familiar with the matter, let’s jump straight into the details. This is a GEN2 image for Hyper-V, pre-configured for Enhanced Session Mode. All you need to do is to download the image, unpack it, then run the script install-vm.bat. Afterwards open the Hyper-V Manager and start the VM. Hyper-V should automatically propose to connect via Enhanced Session Mode (aka. xRDP over HvSocket), thereby greatly improving the user experience.

https://www.kali.org/blog/kali-linux-2023-2-release/images/kali-hyperv-connect.png

Before that, enabling Enhanced Session Mode required some manual steps, both on Windows and in the Kali VM, and it was not super easy. We hope that this new images provides a better out-of-the box experience for Hyper-V users. In fact, there should now be zero configuration required.

More details about this new image can be found in our documentation, on the page [Import Pre-Made Kali Hyper-V VM](https://www.kali.org/docs/virtualization/import-premade-hyper-v/).

### Xfce & PipeWireWith this release, we changed the audio stack for Kali’s default desktop: [PipeWire](https://pipewire.org/) now replaces PulseAudio.

Some background information: PipeWire is a “server for handling audio, video streams, and hardware on Linux”. It was initially released in 2017, is actively developed, and is poised to become the de-facto sound server in pretty much every Linux distribution out there, therefore replacing PulseAudio. The GNOME desktop already uses PipeWire by default in most Linux distributions, including Kali Linux since version [2022.4](https://www.kali.org/blog/kali-linux-2022-4-release/) . Most users never noticed the change.

But let’s get back to Kali’s default desktop environment: Xfce. Xfce does not really “support” PipeWire per se, but it does not need to. PipeWire provides a compatibility layer, under the form of the pipewire-pulse daemon. And that’s what make the magic happens: applications that were meant to work with PulseAudio keep working as if nothing happened, blissfully unaware of the change.

We do not expect any issue with this transition, actually we expect the opposite, some well-known issues should be fixed, sound should work better overall.

What should you do about it? Nothing special. For users who upgrade their Kali installation though, a reminder: the right command to upgrade your system is sudo apt update && sudo apt full-upgrade. Let us put the emphasis on full-upgrade, rather than upgrade: [it matters](https://www.kali.org/docs/troubleshooting/handling-common-apt-errors/).

Should this change cause any problem with your setup, head to the page [No sound on Kali 2023.2](https://www.kali.org/docs/troubleshooting/no-sound/) for tentative solutions.

### i3 Desktop OverhaulThe Kali i3 desktop was completely redone!

For context: [i3](https://i3wm.org/) is a tiling window manager. You might not have heard of it, it’s not available from the Kali’s installer, and it can be said to be a desktop for advanced users. Nevertheless, Kali used to propose a i3 desktop (provided by the metapackage kali-desktop-i3) and also a i3-gaps desktop (metapackage kali-desktop-i3-gaps), which was a sort of alternative version of i3.

The upstream projects [i3-gaps and i3 merged recently](https://github.com/Airblader/i3), so it was awkward for Kali to have two separate metapackages. Therefore those two packages were merged, and only kali-desktop-i3 remains. This metapackage now provides a complete desktop environment (rather than a bare minimum, as it used to).

All of that work was done by long-time i3 user and Kali contributor, [Arszilla](https://arszilla.com/), and we’re really thankful for that. He shared some screenshots of his setup, so that he can give you an idea of what a i3 desktop can look like:

Lock Screen:

https://www.kali.org/blog/kali-linux-2023-2-release/images/i3-locked-screen.png

On/Off Menu:

https://www.kali.org/blog/kali-linux-2023-2-release/images/i3-power-menu.png

Desktop with tiled windows (note how inactive windows become transparent):

https://www.kali.org/blog/kali-linux-2023-2-release/images/i3-tiled-windows.png

Desktop with floating windows

https://www.kali.org/blog/kali-linux-2023-2-release/images/i3-floating-windows.png

How can you try it out? Maybe the cleanest way is to [build yourself a custom installer iso](https://www.kali.org/docs/development/live-build-a-custom-kali-iso/#configuring-the-kali-iso-build-optional) that includes the i3 desktop, and then install it on your machine of choice. After booting it up, refer to the [installation guide](https://gitlab.com/Arszilla/i3-dotfiles#installation), there are a few manual steps to run if you want to configure your i3 desktop to something similar to the screenshots above.

### Desktop Updates#### XfceIn this release we pre-installed a nifty extension for the Xfce File Manager: [GtkHash](https://gtkhash.org/). This extension provides the option to quickly compute checksums, simply by doing a right-click on a file and then opening the Checksums tab. No need to open a terminal and type the command manually! Screenshot below:

https://www.kali.org/blog/kali-linux-2023-2-release/images/gtkhash.png

#### GNOME 44Like for (almost) every half-year, there is a new version bump for the GNOME desktop environment. Kali 2023.2 brings the new version, [GNOME 44](https://release.gnome.org/44/), which is a more polished experienced following the work previously introduced in previous version.

Here are some of the new features for this update:

- Enhanced Shell Quick Settings PanelQuickly connect or disconnect to bluetooth devices

- Updated Settings App
- GNOME’s file chooser dialog can now display thumbnails
- Updated Kali theming

https://www.kali.org/blog/kali-linux-2023-2-release/images/gnome-44-1.png

https://www.kali.org/blog/kali-linux-2023-2-release/images/gnome-44-2.png

##### Tiling Assistant ExtensionWith this release, we are excited to introduce a new extension for Kali’s GNOME Shell desktop: Tiling Assistant. This extension elevates the default tiling experience, placing it on par with the quarter tiling support found in KDE and Xfce. With Tiling Assistant, you can surpass the limitations of the 2 column layout and unlock a range of powerful features. Enjoy intuitive window snapping, multi-monitor support, customizable keyboard shortcuts, and personalized settings, all designed to enhance your productivity and workflow.

Your browser does not support the video tag.### App Icons and Kali Menu UpdatesBeginning with this release, we are excited to announce that we have initiated work on updates and improvements for the Kali menu. Our primary focus is on enhancing the tools listed in the top 100 on the [kali.org/tools page](https://www.kali.org/tools/). This entails improving existing icons, introducing new ones, and enhancing the organization of Kali’s menu categories.

To provide you with a sneak peek, we have included a screenshot showcasing the new and updated app icons. We value your feedback, so if you believe that any particular tool would benefit from a new icon, please don’t hesitate to open a bug report at [bugs.kali.org](https://bugs.kali.org/). Your input will contribute to the continued refinement of Kali’s menu experience.

https://www.kali.org/blog/kali-linux-2023-2-release/images/gnome-44-new-icons.png

### New Tools in KaliIt would not be a Kali release if there were not any new tools added! A quick run down of what has been added (to the network repositories):

- [Cilium-cli](https://www.kali.org/tools/cilium-cli/) - Install, manage & troubleshoot Kubernetes clusters
- [Cosign](https://www.kali.org/tools/cosign/) - Container Signing
- [Eksctl](https://www.kali.org/tools/eksctl/) - Official CLI for Amazon EKS
- [Evilginx](https://www.kali.org/tools/evilginx2/) - Standalone man-in-the-middle attack framework used for phishing login credentials along with session cookies, allowing for the bypass of 2-factor authentication
- [GoPhish](https://www.kali.org/tools/gophish/) - Open-Source Phishing Toolkit
- [Humble](https://www.kali.org/tools/humble/) - A fast security-oriented HTTP headers analyzer
- [Slim(toolkit)](https://www.kali.org/tools/slimtoolkit/) - Don’t change anything in your container image and minify it
- [Syft](https://www.kali.org/tools/syft/) - Generating a Software Bill of Materials from container images and filesystems
- [Terraform](https://www.kali.org/tools/terraform/) - Safely and predictably create, change, and improve infrastructure
- [Tetragon](https://www.kali.org/tools/tetragon/) - eBPF-based Security Observability and Runtime Enforcement
- [TheHive](https://pkg.kali.org/pkg/thehive/) - A Scalable, Open Source and Free Security Incident Response Platform
- [Trivy](https://www.kali.org/tools/trivy/) - Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more
- [Wsgidav](https://www.kali.org/tools/wsgidav/) - Generic and extendable WebDAV server based on WSGI

There has also been numerous packages updates and new libraries as well.

### MiscellaneousBelow are a few other things which have been updated in Kali, that do not have as much detail:

- [Python PIP changes](https://www.kali.org/blog/kali-linux-2023-1-release/#python-updates--changes) - Friendly reminder about pip’s behavior changing in Kali 2023.4!
- When using kali-tweaks, altering OpenSSL security will now have an effect for Python based libraries as well!
- Our [Kali WSL rootfs build-script](https://gitlab.com/kalilinux/build-scripts/kali-wsl-rootfs) got a overhaul. The result will now give a similar experience both using it as well as the output as it will include more of the standard packages by default.

### Kali ARM UpdatesWhen using the [ARM build-scripts](https://www.kali.org/docs/development/arm-build-scripts/), it will now prompt you to reboot after installing build dependencies if required.

Plus, we are now including additional firmware on all ARM images.

The [USBArmory MKII](https://www.kali.org/docs/arm/usb-armory-mkii/) image currently only supports the 512MB variant. The version of u-boot has been bumped.

The [Raspberry Pi P4wnP1 image](https://www.kali.org/docs/arm/raspberry-pi-zero-w-p4wnp1-aloa/) is now considered community supported. Unfortunately the upstream project does not support newer versions of bluez that Kali has, so until that is fixed, we do not want to ship an image that does not work properly.

### Kali Documentation UpdatesOur [Kali documentation](https://www.kali.org/docs/) has had various updates to existing pages as well as the following new pages:

- [Handling common APT problems](https://www.kali.org/docs/troubleshooting/handling-common-apt-errors/)
- [Import Pre-Made Kali Hyper-V VM](https://www.kali.org/docs/virtualization/import-premade-hyper-v/)
- [Kali WSL](https://www.kali.org/docs/wsl/wsl-preparations/)
- [No sound on Kali 2023.2](https://www.kali.org/docs/troubleshooting/no-sound/)
- [Troubleshooting Kali VMware VM](https://www.kali.org/docs/virtualization/troubleshooting-vmware/)

We also want to say a little thank you to following for their work:

- [107 cwk](https://gitlab.com/107cwk)
- [8bitBoy VT100](https://gitlab.com/8bitBoy)
- [Dennis Wehrmann](https://gitlab.com/dwehrmann)
- [Kamal](https://gitlab.com/kamalmjt)
- [snowcra5h](https://gitlab.com/snowcra5h)
- [X0RW3LL](https://gitlab.com/X0RW3LL)

### Kali Blog RecapSince our last release, we did the following [blog posts](https://www.kali.org/blog/):

- [Happy 10th anniversary & Kali’s story …so far](https://www.kali.org/blog/10-years/)

### Community Shout-OutsThese are people from the public who have helped Kali and the team for the last release. And we want to praise them for their work (we like to give credit where due!):

- [@Francisco Jose Rodriguez Martos](https://twitter.com/FrangaLinux) - improving the arm build scripts yet again. Thank you so very much!
- [@Salty_](https://gitlab.com/Salty_) - doing the release testing for the Raspberry Pi 4.
- @Mihir Parekh - reporting an issue with Kali KDE desktop in VMware, along with the workaround.

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

#### New Kali MirrorsWe have some new mirrors since the year started! Those are:

- UK: [mirror.vinehost.net](https://mirror.vinehost.net/kali), sponsored by [VineHost](https://www.vinehost.net), thanks to Callum White.
- Moldova: [md.mirrors.hacktegic.com](https://md.mirrors.hacktegic.com/kali), sponsored by [Hacktegic Technologies SRL](https://hacktegic.com/), thanks to Artiom Mocrenco.
- Indonesia: [xsrv.moratelindo.io](https://xsrv.moratelindo.io/kali), sponsored by [PT Mora Telematika Indonesia](https://www.moratelindo.co.id/eng/index.html), thanks to Deddy Harison.
- Ukraine: [fastmirror.pp.ua](https://fastmirror.pp.ua/kali), thanks to Ivan Barabash.

We almost got a new mirror in South America, but it did not work out, and we realized that we really lack mirrors in this region of the world. If you’re an organization in South America with quite some bandwidth to spare, and you want to improve Kali Linux availability in South America, check our guide on [how to setup a Kali Linux Mirror](https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/). If you think it’s for you, please [reach out](https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/#making-it-public---getting-in-contact)!

### Kali Team Discord Chat SessionThe next [Kali Discord](https://discord.kali.org/) session will happen a week after the release, Wednesday, 7th June 2023 16:00 -> 17:00 [UTC/+0 GMT](https://time.is/UTC).

Please note, we will not be recording these sessions. These are live sessions only.

### Get Kali Linux 2023.2Fresh Images:
So what are you waiting for? Go [get Kali](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for those who are not, we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you will have fewer updates to do.
Just know that these are automated builds that we do, not QA like we do for our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~/
[...]

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2023.2. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2023.2"
VERSION_ID="2023.2"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Debian 6.1.27-1kali1 (2023-05-12)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.1.0-kali9-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And social networks are not Bug Trackers!

Want to keep in up-to-date easier? We have a [RSS feeds](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/) of our [blog](https://www.kali.org/blog/)!

## 2023.1 – 2023-03-13

**Kali Linux 2023.1 Release (Kali Purple & Python Changes)**

Table of Contents
- [Kali Purple](#kali-purple)[Screenshots](#screenshots)

- [Python Updates & Changes](#python-updates--changes)[APT](#apt)
- [venv](#venv)
- [break-system-packages](#break-system-packages)

- [2023 Theme Refresh](#2023-theme-refresh)[All new wallpapers](#all-new-wallpapers)

- [Desktop Updates](#desktop-updates)[Xfce 4.18](#xfce-418)[Panel profiles](#panel-profiles)

- [KDE Plasma 5.27](#kde-plasma-527)[New tiling system](#new-tiling-system)

- [GNOME](#gnome)

- [Default Kernel Settings](#default-kernel-settings)
- [Known Issues](#known-issues)
- [Miscellaneous](#miscellaneous)
- [New Tools in Kali](#new-tools-in-kali)
- [Kali NetHunter Updates](#kali-nethunter-updates)
- [Kali ARM Updates](#kali-arm-updates)
- [Kali Documentation Updates](#kali-documentation-updates)
- [Kali Blog Recap](#kali-blog-recap)
- [Community Shout-Outs](#community-shout-outs)
- [Kali Team Discord Chat & Reddit AMA](#kali-team-discord-chat--reddit-ama)
- [Get Kali Linux 2023.1](#get-kali-linux-20231)

Today we are releasing Kali 2023.1 (and on our 10th anniversary)! It will be ready for immediate [download](https://www.kali.org/get-kali/) or [updating](https://www.kali.org/docs/general-use/updating-kali/) by the time you have finished reading this post.

Given its our 10th anniversary, we are delighted to announce there are a few special things lined up to help celebrate. Stay tuned for a blog post coming out for more information! Edit: [Its out](https://www.kali.org/blog/10-years/)!

The [changelog](https://bugs.kali.org/changelog_page.php) summary since the [2022.4 release from December](https://www.kali.org/blog/kali-linux-2022-4-release/):

- [Kali Purple](#kali-purple) - The dawn of a new era. Kali is not only Offense, but starting to be defense
- [Python Changes](#python-updates--changes) - Python 3.11 & PIP changes going forward
- [2023 Theme](#2023-theme-refresh) - Our once a year theme update! This time, what’s old is new again
- [Desktop Updates](#desktop-updates) - Xfce 4.18 & KDE Plasma 5.27
- [Default Kernel Settings](#default-kernel-settings) - What makes the Kali kernel different
- [New Tools](#new-tools-in-kali) - As always, various new tools added

### Kali PurpleWe are leveling the playing field!

Over the years, we have perfected what we have specialized in, offensive security. We are now starting to branch into a new area, defensive security!
We are doing an initial technical preview pre-launch of “Kali Purple”. This is still in its infancy and is going to need time to mature. But you can start to see the direction Kali is expanding into. You can also be a part of helping to shape the direction!

https://www.kali.org/blog/kali-linux-2023-1-release/images/kali-purple-icon.svg

What is Kali Purple?

The one stop shop for blue and purple Teams.

Feeling red? Feeling blue? Kali Purple: You do You!

Remember what we did a decade ago with Kali Linux? Or with [BackTrack](https://www.backtrack-linux.org/) before that? We made offensive security accessible to everyone. No expensive licenses required, no need for commercial grade infrastructure, no writing code or compiling tools to make it all work… Just download Kali Linux and do your thing.

We are excited to start a new journey with the mission to do exactly the same for defensive security: Just download Kali Purple and do your thing.

Kali Purple is starting out as a Proof of Concept, evolving into a framework, then a platform (just like how Kali is today). The goal is to make enterprise grade security accessible to everyone.

What is in Kali Purple?

On a higher level, Kali Purple consists of:

- A reference architecture for the ultimate SOC In-A-Box; perfect for:Learning
- Practicing SOC analysis and threat hunting
- Security control design and testing
- Blue / Red / Purple teaming exercises
- Kali spy vs. spy competitions ( bare knuckle Blue vs. Red )
- Protection of small to medium size environments

- Over 100 defensive tools, such as:[Arkime](https://pkg.kali.org/pkg/arkime) - Full packet capture and analysis
- [CyberChef](https://pkg.kali.org/pkg/cyberchef) - The cyber swiss army knife
- Elastic Security - Security Information and Event Management
- [GVM](https://www.kali.org/tools/gvm/) - Vulnerability scanner
- [TheHive](https://pkg.kali.org/pkg/thehive) - Incident response platform
- Malcolm - Network traffic analysis tool suite
- [Suricata](https://pkg.kali.org/pkg/suricata) - Intrusion Detection System
- [Zeek](https://pkg.kali.org/pkg/zeek) - (another) Intrusion Detection System (both have their use-cases!)
- …and of course all the usual [Kali tools](https://www.kali.org/tools/)

- Defensive tools [documentations](https://gitlab.com/kalilinux/kali-purple/documentation)
- [Pre-generated image](https://www.kali.org/get-kali/)
- Kali Autopilot - an attack script builder / framework for automated attacks
- Kali Purple Hub for the community to share:Practice pcaps
- Kali Autopilot scripts for blue teaming exercises

- [Community Wiki](https://gitlab.com/kalilinux/kali-purple/documentation/-/wikis/home)
- A defensive menu structure according to NIST CSF (National Institute of Standards and Technology Critical Infrastructure Cybersecurity):Identify
- Protect
- Detect
- Respond
- Recover

- Kali Purple [Discord](https://discord.kali.org/) channels for community collaboration and fun
- And theme: installer, menu entries & Xfce!

…And this is just the beginning of our journey.

#### ScreenshotsThis is what it looks like. Some defensive tools:

Elastic SIEM:

https://www.kali.org/blog/kali-linux-2023-1-release/images/Elastic-01-Dashboard-OPNsense.png

Arkime:

https://www.kali.org/blog/kali-linux-2023-1-release/images/Malcolm-01-Arkime.png

Malcolm:

https://www.kali.org/blog/kali-linux-2023-1-release/images/Malcolm-10-Dashboard.png

Installer, menu, and Xfce:

https://www.kali.org/blog/kali-linux-2023-1-release/images/Kali-Purple_installer.png

https://www.kali.org/blog/kali-linux-2023-1-release/images/Kali-Purple_menu.png

https://www.kali.org/blog/kali-linux-2023-1-release/images/Kali-Purple_xfce.png

Please head over to the [Kali Purple wiki](https://gitlab.com/kalilinux/documentation/kali-purple/-/wikis/home) to join the movement.

### Python Updates & ChangesDebian is gearing up to do its next stable version (happens roughly every 2 years, and its looking like it could be this summer). As a result, packages are getting updated all over the place. Active package maintainers are upgrading their work to be the latest version, otherwise, its a long wait for the next release!
Python is no exception, and Python 3.11 is now in Debian, which comes with more informative error tracebacks and huge speed increase ([between 10-60%](https://docs.python.org/3/whatsnew/3.11.html)). The upgrade should not have as big of an impact as say [python being removed from $PATH](https://www.kali.org/blog/kali-linux-2021-4-release/), or even [Python 2 -> Python 3 migration](https://www.kali.org/blog/python-2-end-of-life/). But it has caused us some headaches with supporting older packages.

However, there is something which may catch people off-guard and cause an effect on some users, especially if you have been using Python “incorrectly”. Python’s PIP behavior. This is already in effect with Debian testing, we have recently applied a temporary patch to give our users a little more time. Does either of the following look familiar? Can you spot what is wrong?

┌──(kali㉿kali)-[~]
└─$ pip install --user thisisapythonmodule

┌──(kali㉿kali)-[~]
└─$ sudo pip install anotherpythonmodule

Anything stand out? The two commands above would try and install a Python module, using Python’s package manager pip (Pip Installs Packages). The issue is, they can clash thus break the operating system’s package management ecosystem, apt (Advanced Package Tool)!
What should you do differently then? Three options:

- Use apt install python3-<package> (easy, simple & recommended)
- Use venv (slightly more complicated but still recommended)
- Use --break-system-packages (warning warning warning!)

Like we said before, our patch is only temporary. Our current behavior will change (like Debian has already). When Kali 2023.4 is released 4th quarter of this year, we will drop our patch, and Pip will refuse to install packages system-wide. Thus you can do one of the three actions below.
We will be reminding you of this with each Kali version building up to the change. We hope you were already using the correct procedure. If you were not, we hope there is enough time for scripts, pipeline and documentation to be updated to one of the supported & recommended ways.

#### APTOur personal preferred approach and what we see as being the easiest way, apt. We would want to see if there is already a Debian package of the Python module, and use that (if possible). A quick rule of thumb would be to-do either blind guess the name, or search:

┌──(kali㉿kali)-[~]
└─$ sudo apt install python3-thisisapythonmodule
[...]

┌──(kali㉿kali)-[~]
└─$ apt search python3 anotherpythonmodule
[...]

If you want a Python module packaged up, [let us know](https://bugs.kali.org/). If you want a Python module updated, again [let us know](https://bugs.kali.org/).

#### venvThere are times where apt may not work for you, such as if there is not yet a Debian package or what is in our network repository is outdated. Look, we get it. You may need the latest version of a Python library and thus pulling from Pip gives you what you are after. However, there are then repercussions of files getting added/updated/removed which either package manager is not aware of. Things may not break straight away, but they might. An example could be when either package manager has an update of the module, or you try and install a module using the other ecosystem.
Enter. venv (Virtual environment). This creates an area which is completely independent. For a quick crash course to help remind you:

┌──(kali㉿kali)-[~]
└─$ sudo apt install python3-venv

┌──(kali㉿kali)-[~]
└─$ mkdir -pv ~/.venvs/

┌──(kali㉿kali)-[~]
└─$ python3 -m venv ~/.venvs/myfirstvenv

Now, you can interact with the new virtual environment one of two ways.
You can do either the “one off action” one-liner:

┌──(kali㉿kali)-[~]
└─$ ~/.venvs/myfirstvenv/bin/python -m pip install thisisapythonmodule

┌──(kali㉿kali)-[~]
└─$ ~/.venvs/myfirstvenv/bin/python -m pip list
[...]

Otherwise, you can load into the virtual environment which is a little bit more persistent:

┌──(kali㉿kali)-[~]
└─$ source ~/.venvs/myfirstvenv/bin/activate

┌──(myfirstvenv)(kali㉿kali)-[~]
└─# pip list
[...]

┌──(myfirstvenv)(kali㉿kali)-[~]
└─# deactivate

┌──(kali㉿kali)-[~]
└─$

Do either method, whichever is best for your needs, requirements, and setup!

#### break-system-packagesOkay, enough telling off.
If you want to ignore everything, and do not care for the repercussions, add --break-system-packages to the end of the command. The name of the option speaks for itself, do not tell us we did not warn you! And please, do not open bug reports when Python’s things stop working. Just please read [this, pep-0668](https://peps.python.org/pep-0668/). Example:

┌──(kali㉿kali)-[~]
└─$ sudo apt install python3-pip

┌──(kali㉿kali)-[~]
└─$ sudo pip install python-nmap
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.11/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation
or OS distribution provider. You can override this, at the risk of breaking
your Python installation or OS, by passing --break-system-packages.

hint: See PEP 668 for the detailed specification.

┌──(kali㉿kali)-[~]
└─$ sudo pip install --break-system-packages python-nmap
[...]

### 2023 Theme RefreshSince [Kali 2021.2](https://www.kali.org/blog/kali-linux-2021-2-release/), all our first year releases (20xx.1) introduce a visual theme refresh. Using a yearly life cycle, it makes it easier to recognize the different versions of Kali Linux over time. This update includes new wallpapers for desktop, login, and boot displays, in addition to new variants of all the themes but now in Kali Purple flavor. Kali Purple will use the white mode them by default, but if you feel so you can perfectly change it to Dark Purple theme. Now you can enjoy any of our main desktops (KDE Plasma, GNOME Shell and Xfce) with new Purple themes and icons.

This time, given its our 10 year anniversary, the theme is a nod to where we have came from, and the backgrounds we have designed are a direct reference to previous iconic Kali releases:

- Boot - Kali 1.0
- Login/Lock - Kali 2.0
- Wallpaper - Kali 1.1

Next you can see the screenshot of how the latest Kali looks, accompanied with the screenshots or images that they are reference of:

Boot menu:

https://www.kali.org/blog/kali-linux-2023-1-release/images/boot-wallpaper.png

Login/Lock:

https://www.kali.org/blog/kali-linux-2023-1-release/images/login-wallpaper.png

Desktop:

https://www.kali.org/blog/kali-linux-2023-1-release/images/desktop-wallpaper.png

#### All new wallpapershttps://www.kali.org/blog/kali-linux-2023-1-release/images/all-wallpapers.png

Special thanks to [/u/Albert-III-](https://www.reddit.com/user/Albert-III-/) who [originally created the background](https://www.reddit.com/r/Kalilinux/comments/n71zqp/i_made_a_wallpaper_from_the_ascii_art_from/) used in the Kali Sticker wallpaper, and to [TJ Null](https://github.com/tjnull) for creating the cool red stickers that inspirited the final version of the same image.

Some extra variants of this image have been uploaded to [kali-wallpapers-legacy](https://www.kali.org/tools/kali-wallpapers/#kali-wallpapers-legacy) package, and can also be found [here](https://gitlab.com/kalilinux/packages/kali-wallpapers/-/tree/kali/master/legacy/backgrounds/kali-sticker). These can be installed by running the following command in your Kali terminal:

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y install kali-wallpapers-legacy

### Desktop UpdatesWe have also make sure to update our three main desktop environments, Xfce, KDE and GNOME to be the latest versions. We then make sure Kali looks stunning using them, as long as putting in various tweaks.

#### Xfce 4.18Nearly two years of development has gone into shaping [Xfce 4.18](https://www.xfce.org/about/tour418), which was formally released on December 15, 2022. It is the stable series follow-up to the Xfce 4.16 release that made its debut during Christmas of 2020.

Main changes for Kali are found in:

- Improved support for UI scaling - fixing many blurry icons while using HiDPI settings
- Thunar - Xfce’s file-manager, received most of the attention:File color highlight
- Recursive search - integrated in the same window
- Split view

https://www.kali.org/blog/kali-linux-2023-1-release/images/xfce-thunar-updates.png

On our side, we have also updated kali-undercover mode to support the latest desktop changes, bringing some light improvements, and solving some minor bugs.

##### Panel profilesAnother great addition for Xfce is the support for panel profiles with import/export functionality. Now you can modify the desktop panels to your liking and save it somewhere safe (or even share them!). Apart from all the pre-built layouts that the app includes, we have added profiles for default Kali settings and a new Kali compact one, which better fits smaller displays.

Your browser does not support the video tag.#### KDE Plasma 5.27Kali now includes the new version 5.27 of KDE Plasma, which brings exciting new improvements to your desktop. You can learn more about the latest changes in the [Plasma 5.27 release announcement publication](https://kde.org/announcements/plasma/5/5.27.0/).

Some of the new features include a window tiling system, a more stylish app theme, cleaner and more usable tools, and widgets that give you more control over your machine. Additionally, Plasma 5.27 is a Long Term Support version with tons of stability work and bug fixes.

##### New tiling systemYou can tile a window dragging it while holding down the Shift key. To create custom tile layouts, hold down the Meta ("Windows") key, and then press T.

Your browser does not support the video tag.#### GNOMEGNOME’s next big update is being released soon, but for now, we still have to wait until Kali’s next release. However, that has not stopped us from introducing some improvements to one of the most popular Linux desktops.

We observed that in Xfce and KDE desktops, one can quickly open a terminal in the file-manager’s current folder by just pressing the F4 key. To make all 3 main Kali desktops behave in a similar manner, we have configured the same functionality for Nautilus, GNOME’s file-manager.

https://www.kali.org/blog/kali-linux-2023-1-release/images/gnome-open-terminal-here.png

### Default Kernel SettingsWe updated some of our kernel default values. These are rather minor changes, mainly for usability, based on user feedback. If needed, those settings can be modified easily with kali-tweaks.

Those settings are:

- No more privileged ports: no need to be root to run a program that binds to a port below 1024 (ported from [Kali 2021.2](https://www.kali.org/blog/kali-linux-2021-2-release/))
- dmesg is now unrestricted by defaults: no need to be root to run dmesg.

If you are curious to know what make the Kali kernel different from the usual, we added a documentation page [Kernel Configuration](https://www.kali.org/docs/general-use/kernel-configuration/).

### Known IssuesFor Nvidia users, this release might not be the best ever. The 525 series of Nvidia drivers is known to break with some GPU models. We do not know which one exactly, but there are various reports from basically all the Linux distributions that started to distribute those drivers, including Debian, Ubuntu and Arch Linux. We are all impacted, and Kali Linux is no exception.

Symptoms include a system that is slow, unresponsive, or completely frozen. If you are one of those unlucky users, your best bet is to uninstall the Nvidia drivers, then reboot:

┌──(kali㉿kali)-[~]
└─$ sudo apt purge "*nvidia*"
[...]

┌──(kali㉿kali)-[~]
└─$ sudo reboot -f

You might need to boot in Recovery Mode so that you can get your hand on a working console and run the command above.

If you want more details about this issue, check the reports on the Nvidia forums:

- [“ERROR: GPU:0: Idling display engine timed out:” since 524.X and linux 6.1.5](https://forums.developer.nvidia.com/t/error-gpu-idling-display-engine-timed-out-since-524-x-and-linux-6-1-5/242543)
- [External monitor via HDMI drops to 1FPS after update to 6.1.0-kali5-amd64](https://forums.developer.nvidia.com/t/external-monitor-via-hdmi-drops-to-1fps-after-update-to-6-1-0-kali5-amd64/245193)

### MiscellaneousBelow are a few other things which have been updated in Kali, which we are calling out for not having as much detail.

- In [Debian 12](https://www.debian.org/devel/debian-installer/News/2023/20230219), they have included a non-free-firmware component. We have followed suit and added this to our build-scripts for Kali 2023.1. Therefore all fresh installs of Kali 2023.1, will have seamless upgrades going forwards. [Upgrading from previous versions will require an additional step](https://www.kali.org/docs/general-use/updating-kali/) of adding it to your sources.
- [kali.org](https://www.kali.org/) will now respect the desktop setting for “dark mode” and automatically toggle between them depending on the OS preferences. Colors of the dark mode have also been improved for better readability and contrast.
- The broken speech synthesizer and Metasploit-framework and libssl1.1/OpenSSL v3 issues stated from our last release have been fixed.
- We have been also working on paying back some internal technical debt to our infrastructure.
- We have been working with numerous mirror administrators doing various maintenance checks, who are very kindly running our community mirrors!
- We have made public our [WSL application](https://gitlab.com/kalilinux/build-scripts/kali-wsl-app) repository. Previously it was just the rootfs part. This is now the application side, which is the launcher for the rootfs.

### New Tools in KaliIt would not be a Kali release if there were not any new tools added! A quick run down of what has been added (to the network repositories):

- [Arkime](https://pkg.kali.org/pkg/arkime) - large-scale, open-source, indexed packet capture and search tool
- [CyberChef](https://pkg.kali.org/pkg/cyberchef) - Cyber Swiss Army Knife
- [Dscan](https://www.kali.org/tools/dscan/) - Distributed Nmap, wrapper around Nmap to allow distributed network enumeration
- [Kubernetes-Helm](https://www.kali.org/tools/kubernetes-helm/) - managing Charts
- [PACK2](https://pkg.kali.org/pkg/pack2) - replacement for iphelix’s PACK
- [Redeye](https://www.kali.org/tools/redeye/) - help you manage your data during a pentest operation in the most efficient and organized way.
- [Unicrypto](https://pkg.kali.org/pkg/unicrypto) - Unified interface for some crypto algos

There have also been numerous packages updates and new libraries as well. We also bump the Kali kernel to 6.1!

### Kali NetHunter UpdatesThere has been some new activity with Kali NetHunter recently.

Following on from [Kali 2022.4](https://www.kali.org/blog/kali-linux-2022-4-release/), we have added Internal bluetooth support for our current smart watch device, TicWatch Pro.

There has been also [new kernel](https://nethunter.kali.org/kernels.html) support added for the following devices & ROMs:

- Motorola X4 on LineageOS 20
- Samsung Galaxy S20 FE 5G using OneUI 5.0 (Android 13)

We have also now got full support for LG V20 running LineageOS 18.1.

And finally, there has been some additional kernel patches added to our [kernel-builder](https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernel-builder).

### Kali ARM Updates[Radxa Zero](https://www.kali.org/docs/arm/radxa-zero-emmc/) is the star of the show for this quarter getting the most of the attention for kali-arm SBC this release:

- Radxa Zero gets larger partition for eMMC booting (16MB -> 32MB)
- Radxa Zero gets audio support!
- Improve building when using ARM64
- Where possible, switch from debootstrap to mmdebstrap to generate chroot

### Kali Documentation UpdatesOur [Kali documentation](https://www.kali.org/docs/) has had various updates to existing pages as well as the following new pages:

- [Kali Linux image overview](https://www.kali.org/docs/introduction/kali-linux-image-overview/)
- [Kernel Configuration](https://www.kali.org/docs/general-use/kernel-configuration/)
- [Making a Kali Bootable USB Drive](https://www.kali.org/docs/installation/create-bootable-media/)

### Kali Blog RecapSince our last release, we did the following [blog posts](https://www.kali.org/blog/):

- [Kali Linux (is) Everywhere!](https://www.kali.org/blog/kali-linux-is-everywhere/)

### Community Shout-OutsThese are people from the public who have helped Kali and the team for the last release. And we want to praise them for their work (we like to give credit where due!):

- [Arszilla](https://arszilla.com/) for maintaining the kali-desktop-i3 metapackage.
- [Daniele Faugiana](https://gitlab.com/turbopapero) for helping with packaging Rizin’s Ghidra plugin.
- snowcrash#0001 on the Kali discord, being super helpful with sharing his personal notes when helping others.
- The entire [Kali Linux & Friends](https://discord.kali.org/) moderation team!

The following people have helped with our documentation:

- [Moshe Kaplan](https://gitlab.com/moshekaplan)
- [Salty_](https://gitlab.com/Salty_)
- [Saurav Kumar](https://gitlab.com/skumar141)
- [Vladimir Prokopenko](https://gitlab.com/vladimirprokopenko87)
- [Snowcrash](https://gitlab.com/snowcra5h)
- [X0RW3LL](https://gitlab.com/X0RW3LL)

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

### Kali Team Discord Chat & Reddit AMAThe next [Kali Discord](https://discord.kali.org/) session will happen tomorrow, Tuesday, 14th March 2023 16:00 -> 17:00 [UTC/+0 GMT](https://time.is/UTC).

Please note, we will not be recording these sessions. These are live sessions only.

If voice chat is not your thing, or its to short notice, we also have a special one-off “Ask Me Anything” (AMA) happening on [reddit.com/r/offensive_security](https://www.reddit.com/r/offensive_security/comments/11fifxl/hi_im_g0tmi1k_lead_developer_for_kali_linux/), Thursday, 16th March 2023 16:00 -> 18:00 [UTC/+0 GMT](https://time.is/UTC).

### Get Kali Linux 2023.1Fresh Images:
So what are you waiting for? Go [get Kali](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for those who are not, we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you will have fewer updates to do.
Just know that these are automated builds that we do, not QA like we do for our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~/
[...]

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2023.1. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2023.1"
VERSION_ID="2023.1"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Debian 6.1.12-1kali2 (2023-02-23)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.1.0-kali5-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And [Twitter](https://twitter.com/kalilinux) is not a Bug Tracker!

Want to keep up-to-date more easily? We have a [RSS feeds](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/) of our [blog](https://www.kali.org/blog/)!

## 2022.4 – 2022-12-06

**Kali Linux 2022.4 Release (Azure, Social & Kali NetHunter Pro)**

Table of Contents
- [Microsoft Azure](#microsoft-azure)
- [More Platforms](#more-platforms)
- [Social Networks](#social-networks)[Press Pack](#press-pack)
- [Media Enquiries](#media-enquiries)

- [Kali NetHunter Pro Release](#kali-nethunter-pro-release)
- [Kali NetHunter Update](#kali-nethunter-update)
- [Desktop Updates](#desktop-updates)[GNOME](#gnome)
- [KDE Plasma](#kde-plasma)

- [Miscellaneous](#miscellaneous)
- [New Tools in Kali](#new-tools-in-kali)
- [Kali ARM Updates](#kali-arm-updates)
- [Kali Documentation Updates](#kali-documentation-updates)
- [Recent Kali Blog Posts](#recent-kali-blog-posts)
- [Community Shout-Outs](#community-shout-outs)
- [Discord Chat](#discord-chat)
- [Get Kali Linux 2022.4](#get-kali-linux-20224)

Before the year is over, we thought it was best to get the final 2022 release out. Today we are publishing Kali Linux 2022.4. This is ready for immediate [download](https://www.kali.org/get-kali/) or [updating](https://www.kali.org/docs/general-use/updating-kali/) existing installations.

A summary of the [changelog](https://bugs.kali.org/changelog_page.php) since [August’s 2022.3 release](https://www.kali.org/blog/kali-linux-2022-3-release/):

- [Microsoft Azure](#microsoft-azure) - We are back on the Microsoft Azure store
- [More Platforms](#more-platforms) - Generic Cloud, QEMU VM image & Vagrant libvirt
- [Social Networks](#social-networks) - New homes, keeping in touch & press packs
- [Kali NetHunter Pro](#kali-nethunter-pro-release) - Announcing the first release of a “true” Kali Linux on the mobile phone (PinePhone / Pro)
- [Kali NetHunter](#kali-nethunter-update) - Internal Bluetooth support, kernel porting video, firmware updates & other improvements
- [Desktop Updates](#desktop-updates) - GNOME 43 & KDE 5.26
- [New Tools](#new-tools-in-kali) - As always, various new packages added

### Microsoft AzureIts been a long time coming, but we are very happy to announce that Kali has been added to [Microsoft Azure](https://azuremarketplace.microsoft.com/en/marketplace/apps/kali-linux.kali) (again - and this time to stay)! [Following in the foot steps](https://www.kali.org/blog/kali-linux-2020-4-release/) of our [Amazon AWS](https://aws.amazon.com/marketplace/pp/B08LL91KKB) image, we are using the same [kali-cloud build-scripts](https://gitlab.com/kalilinux/build-scripts/kali-cloud) now to automate publishing to Microsoft Azure store.

Out of the box, currently, there is no graphical user interface, or any tools pre-installed. Should you want the default toolset (kali-linux-default) or any other combination of [metapackages](https://www.kali.org/docs/general-use/metapackages/), it should be like any other Kali platform. For installing a desktop environment, we have the following kali-docs page: [Setting up RDP with Xfce](https://www.kali.org/docs/general-use/xfce-with-rdp/)

We hope in 2023 we can revisit this again and are looking at doing ARM64 architecture, as well as different variations of images, allowing you to choose from a mixture of headless bare-bones install, the traditional environment, and a mixture of everything in-between.

### More PlatformsWe are now including a QEMU image with our [pre-generated images](https://www.kali.org/get-kali/). We hope this makes it easier for the people who use self-hosted Proxmox Virtual Environments (VE), [virt-manager](https://pkg.kali.org/pkg/virt-manager), or [libvirt](https://pkg.kali.org/pkg/libvirt)!

On that subject, [elrey (alex)](https://gitlab.com/elreydetoda) from the community has added libvirt support to our [kali-vagrant build-script](https://gitlab.com/kalilinux/build-scripts/kali-vagrant).

In Kali 2022.3, we have produced a Generic Cloud image. The idea of this image is that it should work in “most” cloud providers This is coming from our [kali-cloud build-scripts](https://gitlab.com/kalilinux/build-scripts/kali-cloud).
So if you are self-hosting OpenStack, this is a great way of getting Kali loaded up!

### Social NetworksWe have expanded the social networks which we post on, as well as refreshing the current ones. As a recap:

- Facebook: [facebook.com/KaliLinux](https://www.facebook.com/KaliLinux/)
- NEW Instagram: [instagram.com/KaliLinux](https://www.instagram.com/kalilinux/)
- NEW Mastodon: [[email protected]](https://infosec.exchange/@kalilinux)
- Twitter: [twitter.com/KaliLinux](https://twitter.com/kalilinux)

As a reminder, we don’t use social networks for technical support - you can receive community support via [discord](https://discord.kali.org/) or our [forums](https://forums.kali.org/) and bug reports should go to the [bug tracker](https://bugs.kali.org/)!
Instead, we automatically post [blog posts](https://www.kali.org/blog/) thus these accounts are mostly unmonitored!

If social networks are not your thing, you can also keep in touch via:

- Email: [Newsletter](https://www.kali.org/newsletter/)
- RSS: [kali.org/rss.xml](https://www.kali.org/rss.xml)

#### Press PackWe have also taken the time to create a Press Pack (aka Press kit) for Kali. Here you can find all our product media resources to use, including:

- Logomark (our dragon logos)
- Logomark and Wordmark (our iconic avatars - dragon logo with text)
- Wordmark (text as an image)
- Various different image formats (png, svg, jpg)
- Official colours

Please bear in mind that they are under [copyright & trademark](https://www.kali.org/docs/policy/trademark/) when using them!

You can [download them all](https://gitlab.com/kalilinux/documentation/press-pack/-/archive/main/press-pack-main.zip), or you can [view them online](https://gitlab.com/kalilinux/documentation/press-pack/-/tree/main/).

https://gitlab.com/kalilinux/documentation/press-pack/-/tree/main/Kali/Logomark_and_Wordmark
https://gitlab.com/kalilinux/documentation/press-pack/-/tree/main/Kali_NetHunter/Logomark_and_Wordmark
https://gitlab.com/kalilinux/documentation/press-pack/-/tree/main/Kali_NetHunter_Pro/Logomark_and_Wordmark

#### Media EnquiriesAnd on the subject, we do have a page for [Press and Media enquiries](https://www.kali.org/contact/).

### Kali NetHunter Pro Releasehttps://www.kali.org/blog/kali-linux-2022-4-release/images/NetHunterPro.png

We are very excited to announce the official support of the Pine64 PinePhone and PinePhone Pro thanks to the amazing work of [shubhamvis98](https://gitlab.com/shubhamvis98) and the vibrant community.

The launch of Kali NetHunter Pro is the beginning of a new chapter for Kali Linux and NetHunter, a bare metal installation of Kali Linux with Phosh desktop environment, optimized for mobile devices.

First of all we make available SD card images for the PinePhone and the PinePhone Pro to dual boot alongside the main OS. Soon we will release alternative versions with Plasma Mobile as well as installers so you can install Kali NetHunter Pro onto the internal flash memory.

For all those that have a PinePhone or a PinePhone Pro, hop over to our [download page](https://www.kali.org/get-kali/#kali-mobile) and join the brave new world of mobile hacking. For those that don’t have a PinePhone yet: What are you waiting for? Get one :-)

Please help us with the development by testing the images, submitting bugs and improvements in our [GitLab repository](https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-pro), and become a part of the vibrant Kali NetHunter community.

### Kali NetHunter UpdateInternal Bluetooth support has finally arrived, thanks to [yesimxev](https://gitlab.com/yesimxev) and the awesome [community](https://www.kali.org/community/)! We have added support to some [devices](https://nethunter.kali.org/device-kernels.html) already, however as each [kernel](https://nethunter.kali.org/kernels.html) needs new Bluetooth drivers enabled, it takes time to rebuild each of them.
You are more than welcome to [contribute](https://www.kali.org/docs/nethunter/nethunter-kernel-2-config-1/) if your device is Kali NetHunter supported already without the new drivers.

[yesimxev](https://gitlab.com/yesimxev) has released the ultimate [Kali NetHunter Complete Kernel Porting Guide](https://www.youtube.com/watch?v=FwSHbZqY88k). Have you ever dreamt of porting Kali NetHunter to your device but didn’t know where to start? This video has it all so get cracking.

Wardriving has been updated with bugfixes, [Bluetooth](https://www.kali.org/docs/nethunter/nethunter-btarsenal/), RTL-SDR, and MouseJack support. That’s good news for QCACLD-3.0 users (most devices out there) as you will be able to use wardriving with internal wireless and Bluetooth chipsets, if OTG adapters are not an option.

[KeX](https://www.kali.org/docs/nethunter/nethunter-kex-manager/) also received the status fix along with audio support.
Now you can play any audio in KeX session.

Wireless firmware has been updated, and Magisk firmware flashing is now patched.

Android 11/12 crashing when starting the [Kali NetHunter app](https://www.kali.org/docs/nethunter/#70-kali-nethunter-application) has also been fixed with this release.

Last but not least, let’s welcome the OnePlus 6t, Pixel 4a 5g and Realme 5 Pro devices to the list of the Android 12 supported [devices](https://nethunter.kali.org/device-kernels.html).

### Desktop UpdatesBoth the [GNOME](#gnome) and [KDE Plasma](#kde-plasma) desktops have received a major version bump.

#### GNOMEFor people who opt to use GNOME as their desktop environment, [GNOME 43](https://release.gnome.org/43/) is now in Kali! If you do not read their changelog, below is a quick summary mixed with some of our tweaks:

- Shell updates, including a new quick settings panel and an improved theme.
Unfortunately, we had to say goodbye to the extension proxyswitcher, as it was no longer compatible with this new release
- Continues the migration of multiple programs to GTK4 with the libadwaita library.
The previous text editor (gedit) has been replaced with the brand new gnome-text-editor, which includes an updated Kali color-scheme theme.
- New GTK3 theme based on the adw-gtk3 project with Kali’s tweaks, which brings a fresh look, and makes the interface coherent between the different GUI libraries. With it, GTK3-based programs don’t seem out of place with the recently introduced libadwaita-based ones.

https://www.kali.org/blog/kali-linux-2022-4-release/images/gnome-43.png

#### KDE PlasmaKali now includes the new version 5.26 of KDE, which improves the overall desktop experience, and brings tweaks for multiple widgets. You can learn more about the latest changes in the [Plasma 5.26 release announcement](https://kde.org/announcements/plasma/5/5.26.0/) publication.

### MiscellaneousBelow is a quick list of minor updates:

- The Kali dragon logo is now in [nerd-fonts](https://www.nerdfonts.com/cheat-sheet) (f327 aka nf-linux-kali_linux).
- We are aware of a bug with the installation using speech synthesiser.As a work around, you can use [Kali 2022.2](https://cdimage.kali.org/kali-2022.2/), and [upgrade](https://www.kali.org/docs/general-use/updating-kali/).
- We will put out a message on [social networks](#social-networks) when to grab the weekly images with the fix.

- We are aware of a bug with Metasploit-framework and libssl1.1/OpenSSL v3. As a result, there are issues with payloads using */*/reverse_https.We will address this as quickly as we can.
- We will put out a message on [social networks](#social-networks) when to grab the weekly images with the fix.

- RSS feed for torrents! [kali.org/torrents.xml](https://www.kali.org/torrents.xml).If your client supports it, you can use regex then to filter out which image you prefer:

https://www.kali.org/blog/kali-linux-2022-4-release/images/torrents.png

### New Tools in KaliIt would not be a Kali release if there were not any new tools added! A quick run down of what has been added (to the network repositories):

- [bloodhound.py](https://www.kali.org/tools/bloodhound.py/) - A Python based ingestor for BloodHound
- [certipy](https://www.kali.org/tools/certipy-ad/) - Tool for Active Directory Certificate Services enumeration and abuse
- [hak5-wifi-coconut](https://www.kali.org/tools/hak5-wifi-coconut/) - A user-space driver for USB Wi-Fi NICs and the Hak5 Wi-Fi Coconut
- [ldapdomaindump](https://www.kali.org/tools/python-ldapdomaindump/) - Active Directory information dumper via LDAP
- [peass-ng](https://www.kali.org/tools/peass-ng/) - Privilege escalation tools for Windows and Linux/Unix* and MacOS.
- [rizin-cutter](https://www.kali.org/tools/rizin-cutter/) - reverse engineering platform powered by rizin

This is new tools, there are numerous updates to existing tools.

### Kali ARM UpdatesWe are happy to say that Kali has been added to [Raspberry Pi Imager](https://www.raspberrypi.com/software/) (rpi-imager), making it even easier to flash Kali to your SDs (as long as you can buy an RPi!). We have also written up [a quick guide](https://www.kali.org/docs/arm/using-rpi-imager-to-write-raspberry-pi-images/) on it.

https://www.kali.org/blog/kali-linux-2022-4-release/images/rpi-imager.png

The Kali user’s sudoers edit is now its own file in /etc/sudoers.d and users should no longer be prompted on what to do when an update for sudo comes in. This change does not occur on an upgrade, only fresh installs.

The [USBArmory MKII](https://www.kali.org/docs/arm/usb-armory-mkii/) has had the u-boot bootloader bumped to 2022.10.

The build-script for the [ODROID-C2](https://www.kali.org/docs/arm/cubox/) has been fixed and should now properly create images again. Thanks to [M Beekhuizen](https://gitlab.com/Beekhuizen) for reporting the issue.

[Radxa Zero](https://www.kali.org/docs/arm/radxa-zero-emmc/) images created from the build-scripts should now have firmware to support the wireless card on newer models (1.51+). Thanks to Stefan Lehner (from Discord) for reporting the issue.

[Pinebook Pro](https://www.kali.org/docs/arm/pinebook-pro/) images have firmware to support the new wireless card on more recent models. Thanks to [Jonathan Cox](https://gitlab.com/dravenwolfgang) for reporting the issue.

The [kali-arm build-scripts](https://gitlab.com/kalilinux/build-scripts/kali-arm) got a big makeover, thanks to [Arszilla](https://gitlab.com/Arszilla) for putting in the work to do this.

### Kali Documentation UpdatesOur [kali-docs](https://www.kali.org/docs/) has had various updates to existing pages as well as the following new pages:

- [Using the Raspberry Pi Imager software to write Kali Raspberry Pi Images](https://www.kali.org/docs/arm/using-rpi-imager-to-write-raspberry-pi-images/)
- [Azure](https://www.kali.org/docs/cloud/azure/)
- [Kali Linux Image Overview](https://www.kali.org/docs/introduction/kali-linux-image-overview/)
- [NetHunter Social Engineer Toolkit](https://www.kali.org/docs/nethunter/nethunter-set/)
- [Customizing a Kali Vagrant Vagrantfile](https://www.kali.org/docs/virtualization/customizing-kali-vagrant/)
- [Kali inside Proxmox (Guest VM)](https://www.kali.org/docs/virtualization/install-proxmox-guest-vm/)
- [Running Kali Linux as a Virtual Machine in Windows](https://www.kali.org/docs/virtualization/running-kali-vm-windows/)
- [Preparing a system for WSL](https://www.kali.org/docs/wsl/wsl-preparations/)

Thank you for their work!

- [2hexed](https://gitlab.com/2hexed)
- [Fabrizio Fiandanese](https://gitlab.com/fabfianda-gitlab)
- [Jelmer Vernooij](https://gitlab.com/jelmer)
- [Jesse Rotenberg](https://gitlab.com/JesseRotenberg)
- [Koh You Liang](https://gitlab.com/isopach)
- [OW87](https://gitlab.com/m.01001101.01010110)
- [Rclev4Sec](https://gitlab.com/rclev4sec)
- [yesimxev](https://gitlab.com/yesimxev)

### Recent Kali Blog PostsRecapping our [blog posts](https://www.kali.org/blog/) since the last release:

- [Community Showcase: Raspberry Pi Zero W P4wnP1 A.L.O.A.](https://www.kali.org/blog/community-showcase-using-kali-pi-p4wnp1-aloa/)
- [Kali Community Themes](https://www.kali.org/blog/kali-community-themes/)
- [Remotely Accessing Secure Kali Pi](https://www.kali.org/blog/remotely-accessing-secure-kali-raspberry-pi/)

### Community Shout-OutsThere have been various contributions since our release. Thank you guys!
Out of these, a few people’s actions have helped make a significant improvement to Kali, so giving them credit:

- [Alex Henrie](https://gitlab.com/alexhenrie) - Fixed a long-standing issue with the prompt in the Docker images, thanks so much!
- [Arszilla](https://gitlab.com/arszilla) - Kali ARM and i3-gap work
- “Fred Sheehan” on the Kali-forums - Super helpful, great poster!
- [Shubham Vishwakarma](https://gitlab.com/Shubhamvis98) - Bringing Kali to the PinePhone!

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

### Discord ChatThe next [Kali Discord](https://discord.kali.org/) session will happen a week after the release, Tuesday, 13th December 2022 16:00 -> 17:00 [UTC/+0 GMT](https://time.is/UTC).

Please note, we will not be recording these sessions. These are live sessions only.

### Get Kali Linux 2022.4Fresh Images:
So what are you waiting for? Go [get Kali](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for those who are not, we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you will have fewer updates to do.
Just know that these are automated builds that we do, not QA like we do for our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list
[...]

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade
[...]

┌──(kali㉿kali)-[~]
└─$ cp -vrbi /etc/skel/. ~
[...]

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2022.4. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2022.4"
VERSION_ID="2022.4"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Debian 6.0.7-1kali1 (2022-11-07)

┌──(kali㉿kali)-[~]
└─$ uname -r
6.0.0-kali3-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken!

## 2022.3 – 2022-08-09

**Kali Linux 2022.3 Release (Discord & Test Lab)**

Table of Contents
- [Kali is on Discord](#kali-is-on-discord)
- [Test Lab Environment](#test-lab-environment)
- [Kali for Virtual Machines](#kali-for-virtual-machines)
- [Help Wanted](#help-wanted)
- [Other Kali updates](#other-kali-updates)
- [New Tools in Kali](#new-tools-in-kali)
- [Kali NetHunter Updates](#kali-nethunter-updates)
- [Kali ARM Updates](#kali-arm-updates)
- [Kali Documentation Updates](#kali-documentation-updates)[Kali Tools Documentation](#kali-tools-documentation)

- [Kali Blog Recap](#kali-blog-recap)
- [Community Shout-Outs](#community-shout-outs)
- [Get Kali Linux 2022.3](#get-kali-linux-20223)

In light of “Hacker Summer Camp 2022” (BlackHat USA, BSides LV, and DEFCON) occurring right now, we wanted to push out Kali Linux 2022.3 as a nice surprise for everyone to enjoy! With the publishing of this blog post, we have the download links ready for immediate [access](https://www.kali.org/get-kali/), or you can [update any existing installation](https://www.kali.org/docs/general-use/updating-kali/).

The highlights for Kali’s 2022.3’s release:

- [Discord Server](#kali-is-on-discord) - Kali’s new community real-time chat option has launched!
- [Test Lab Environment](#test-lab-environment) - Quickly create a test bed to learn, practice, and benchmark tools and compare their results
- [Opening Kali-Tools Repo](#kali-tools-documentation) - We have opened up the Kali tools repository & are accepting your submissions!
- [Help Wanted](#help-wanted) - We are looking for a Go developer to help us on an open-source project
- [Kali NetHunter Updates](#kali-nethunter-updates) - New releases in our NetHunter store
- [Virtual Machines Updates](#kali-for-virtual-machines) - New VirtualBox image format, weekly images, and build-scripts to build your own
- [New Tools In Kali](#new-tools-in-kali) - Would not be a release without some new tools!

For more details, see the [bug tracker changelog](https://bugs.kali.org/changelog_page.php).

### Kali is on DiscordWe have started up a new discord server, [Kali Linux & Friends](https://discord.kali.org/). This is our new place for the Kali community to get together and chat in real-time all about Kali Linux (as well as other [community projects](https://www.offsec.com/community/?utm_source=kali&utm_medium=web&utm_campaign=blog#projects) that OffSec has to offer).

This is a community server, all with common interests. We do not have the goal to get as many users as possible, instead, we are growing a place for each other to help one another. We are focusing on quality not quantity.
Please bear in mind, if you are looking for help, first search for your problem, ask questions, then wait for the community support from your peers. Remember no one is under obligation to help you, and you are more likely to get assistance if you are polite and show you have put some effort into solving your own issue.

Speaking of “real-time chatting”, we are going to be starting a new tradition. We will be doing an hour long session after every Kali release where various Kali developers will come and voice chat on Discord, answer questions about Kali and its direction, take your input, and so on. We will be sure to add details about this in every blog post release going forwards.

The first one is on Tuesday, 16th August 2022 16:00 -> 17:00 [UTC/+0 GMT](https://time.is/UTC).

Feel free to be a fly on the wall, come by to say a hello, or ask questions! This is a great opportunity to ask questions, provide your input on what can help improve Kali, or get involved and contribute!

Please note, we will not be recording these sessions. These are live sessions only.

Why Discord? In short, people are already there. It’s a common and popular platform that has become very popular over the years. People have already gone through the process of signing up and becoming familiar with the UI. For those who are not, you can register and within minutes be chatting. It’s simple and straight forward to get going.

Real-time chat can be seen like a social network, as it’s only as good as the people who are on it.

Why not use Matrix? In short, same reasons as above, the user-base. Going into a bit more depth, the entry barrier is higher. It’s a bit more complex to get setup and it’s not as user-friendly.

Matrix is great (and various team members do use it daily)! [Kali being open-source](https://www.kali.org/docs/policy/kali-linux-open-source-policy/), using open-source solutions to match does make sense.
But we are not trying to be a trend setter - we are going with the crowd. We believe the key to a successful community is the community itself. We are not wanting to reinvent the wheel, we are not wanting people to sign up once again to another service, using another chat application, another thing that’s giving you notifications. If people are already there, we are going with them.

Lastly, we do not want to be focusing on running and maintaining infrastructure of a self-hosted solution for a real-time chat, as that takes us away from developing an OS with everything that goes with it.

What happened to IRC? In short, it’s still there. We are still using it from a Kali development perspective. The network may have changed (from Freenode to Libera Chat), but [we still do use Internet Relay Chat](https://www.kali.org/docs/community/kali-linux-irc-channel/).

Back in the heyday of Freenode, it was the place to be. “Everyone” was on it. It did slowly start to lose some users, before the crash in 2021. Libera Chat stepped it, and did recover some of the broken pieces but various homes moved on to other networks or even protocols.

The IRC channels are public, so anyone can join in on the development side of things. However the Kali community focus will be on Discord.

### Test Lab Environment“A craftsman is only as good as their tools.”

This is true, even outside of Information Security field, you need to understand your tools to master your craft.
You can read their code to understand how they work (or a very detailed REAME at times), help screens and their manuals (if they have one) will give you a starting point on how to use them. But where do you use them especially when they are security tools? What output should the tool give? What is a successful run? How long does the tool take? What is its baseline? How can I get experience with it? All valid questions which need answers.

To try and achieve these answers, most seasoned professionals will practice first (hopefully in a known, controlled environment!). This is where a “Test Bed/Laboratory” comes into play. Theory is different to practical (You may remember this the first time you were tasked of something new to accomplish). You can take the static theory-based output from help screens, READMEs, and manual pages and hands-on enter the data into programs and monitor the dynamic output and practical response. Its one thing to read something, its another to do it. The result often gives people a deeper understanding.

Practice makes perfect permanent. So practice, practice, practice!
Inquisitive minds can then start to experiment with new configurations, options, commands and flags. Then start to chain items together, or compare similar and alternative solutions, then compare the results, to become more educated and build up a benchmark of knowledge. This grows experience.

We are trying to make it a bit easier to build up your test lab. So we have packaged up:

- [DVWA](https://www.kali.org/tools/dvwa/) - Damn Vulnerable Web Application
- [Juice Shop](https://www.kali.org/tools/juice-shop/) - OWASP Juice Shop

All you have to do is apt install <package>, else you can use the kali-linux-labs [metapackage](https://www.kali.org/docs/general-use/metapackages/) to get them all!
This list will be growing in the upcoming Kali releases!

At times, you may be running codes that are designed to be vulnerable. Please take the necessary steps to secure your environment.

Practice tools, sharpen skills, and benchmark alternatives

If you put all your trust into something without understanding it, there could be complications…

https://www.kali.org/blog/kali-linux-2022-3-release/images/tape_messure.jpg

Credit: unknown!

### Kali for Virtual MachinesWe have already provided Kali Linux images for [VMware](https://www.kali.org/docs/virtualization/install-vmware-guest-vm/) and [VirtualBox](https://www.kali.org/docs/virtualization/install-virtualbox-guest-vm/) since the [start](https://www.kali.org/releases/). For this release, there’s been a few changes worth noting.

We now distribute the VirtualBox image as a VDI disk and a .vbox metadata file, or to say it short: the native format for VirtualBox images. It should be a bit faster to download, as those images have a better compression ratio compared to the OVA images that we used to provide. It should also be a bit more straightforward to use it, you just need to unpack the image in your VirtualBox folder and run it. In case you need help, refer to our documentation: [Import Pre-Made Kali VirtualBox VM](https://www.kali.org/docs/virtualization/import-premade-virtualbox/).

Additionally, we just started to provide [weekly builds of our VM images](https://www.kali.org/get-kali/#kali-virtual-machines). These images are built from the [kali-rolling branch](https://www.kali.org/docs/general-use/kali-branches/), meaning that they have the most up-to-date packages, but on the other hand they don’t receive as much testing as our quarterly releases.

Last but not least, the scripts that we use to build those images are now available [on GitLab](https://gitlab.com/kalilinux/build-scripts/kali-vm). If you need to build custom Kali VM images, this is the place to go!

### Help WantedDo you know Go? The Kali team is looking for some help! Bonus points if you know Redis as well!

This work would be going into an already existing Open-Source project, [MirrorBits](https://github.com/videolabs/mirrorbits). We have a few desirable features we would love to be added into it.

Interested? Let’s talk. Please get in touch by emailing icanhelp at kali dot org, or [tweeting at us directly](https://twitter.com/kalilinux). If you have any previous work to showcase, even better.

Why are you guys not doing it? Our development team has a maxed out roadmap and we don’t want to be waiting until items are closed out before this goes into production.

### Other Kali updates
- For people who use Xrdp (like [Win-KeX](https://www.kali.org/docs/wsl/win-kex/)), there is a new look to the login
- We have fixed up some confusion between fuse and fuse3
- We did some maintenance to our network repository, and shrank /kali from 1.7Tb to 520Gb!

### New Tools in KaliIt would not be a Kali release if there were not any new tools added! A quick run down of what has been added (to the network repositories):

- [DefectDojo](https://www.kali.org/tools/defectdojo/) - Open-source application vulnerability correlation and security orchestration tool
- [shellfire](https://www.kali.org/tools/shellfire/) - Exploiting LFI/RFI and command injection vulnerabilities
- [SprayingToolkit](https://www.kali.org/tools/sprayingtoolkit/) - Password spraying attacks against Lync/S4B, OWA and O365

There have been numerous packages updates as well.

### Kali NetHunter UpdatesFull Android 12 support is getting closer to being a reality with 6 new kernels in our [NetHunter repository](https://gitlab.com/kalilinux/nethunter/build-scripts) and updates to the [NetHunter app](https://store.nethunter.com/en/packages/com.offsec.nethunter/). It is still not for the fainthearted as a little tinkering is required to install all the components individually but we’re getting closer to releasing the first OnePlus image soon.

For the meantime, we have updated the apps in our [NetHunter Store](https://store.nethunter.com/) to the latest releases, including:

- aRDP, aSPICE, bVNC, Opaque = v5.1.0
- Connectbot = 1.9.8-oss
- Intercepter-NG = 2.8
- OONI Probe = 3.7.0
- OpenVPN = 0.7.38
- Orbot = 16.4.1-RC-2-tor.0.4.4.6
- SnoopSnitch = 2.0.12-nbc
- Termux = 118
- Termux-API = 51
- Termux-Styling = 29
- Termux-Tasker = 6
- Termux-Widget = 13
- Termux-Float = 15
- WiGLE WiFi Wardriving = 2.64

If you would like to get involved and help out with the development, or just like to chat to like-minded Android tinkerers, why don’t you join us in the NetHunter channels on our [new Discord server](https://discord.kali.org/)? We’d love to see you around!

### Kali ARM Updates
- All Raspberry Pi devices have had their kernel upgraded to 5.15.
- Created [arm.kali.org](https://arm.kali.org/) to have a overview and statistics for [kali-arm](https://gitlab.com/kalilinux/build-scripts/kali-arm) (very similar to [nethunter.kali.org](https://nethunter.kali.org/)).
- Every Kali ARM device has had their default size for the boot partition set to 256 MB.
- [Pinebook](https://www.kali.org/docs/arm/pinebook/) has had the broken sleep modes removed, so it should no longer go to sleep and be unable to wake up.
- [USBArmory MKII](https://www.kali.org/docs/arm/usb-armory-mkii/) moved to the 2022.04 u-boot release.

### Kali Documentation UpdatesThere has been a number of new pages added to our kali-docs sub section, as well as numerous updates to existing pages, keeping them up-to-date as well as adding more details.
A summary of the new pages added:

- [Radxa Zero (eMMC)](https://www.kali.org/docs/arm/radxa-zero-emmc/)
- [Radxa Zero (sdcard)](https://www.kali.org/docs/arm/radxa-zero-sdcard/)
- [Raspberry Pi Zero W P4wnP1 A.L.O.A (A Little Offensive Application)](https://www.kali.org/docs/arm/raspberry-pi-zero-w-p4wnp1-aloa/)
- [Linode](https://www.kali.org/docs/cloud/linode/)
- [Using Kali Linux Podman Images](https://www.kali.org/docs/containers/using-kali-podman-images/)
- [Bare-bones Kali](https://www.kali.org/docs/installation/barebone-kali/)
- [Discovering Problems With Download Speed](https://www.kali.org/docs/troubleshooting/download-speed-issues/)
- [No sound on Kali 2022.2](https://www.kali.org/docs/troubleshooting/no-sound/)
- [USB Boot in VirtualBox](https://www.kali.org/docs/usb/boot-usb-in-virtualbox/)
- [Import Pre-Made Kali VirtualBox VM](https://www.kali.org/docs/virtualization/import-premade-virtualbox/)
- [Import Pre-Made Kali VMware VM](https://www.kali.org/docs/virtualization/import-premade-vmware/)
- [Improving Virtual Machine Performance for VMware](https://www.kali.org/docs/virtualization/improving-vm-performance-vmware/)
- [Kali inside Hyper-V (Guest VM)](https://www.kali.org/docs/virtualization/install-hyper-v-guest-vm/)
- [Kali inside QEMU/LibVirt with virt-manager (Guest VM)](https://www.kali.org/docs/virtualization/install-qemu-guest-vm/)
- [Kali inside UTM (Guest VM)](https://www.kali.org/docs/virtualization/install-utm-guest-vm/)
- [Kali inside Vagrant (Guest VM)](https://www.kali.org/docs/virtualization/install-vagrant-guest-vm/)
- [Installing VMware on Apple Silicon (M1/M2) Macs (Host)](https://www.kali.org/docs/virtualization/install-vmware-silicon-host/)

#### Kali Tools DocumentationA little off-topic, but also worth mentioning. Kali-docs is our documentation of Kali as an operating system. Kali-tools is our documentation for the tools inside of Kali.
We have also opened up the [kali-tools repository](https://gitlab.com/kalilinux/documentation/kali-tools), allowing for community contributions as well.

We will be updating this on a frequent basis. But you can help speed this up! Our goal is to have general information about every tool, as well as examples of the tool being used, and how to use the tool. If you want to get involved with Kali Linux, this is a great way to!

We are after any media format possible, text, images, and videos ([asciinema](https://asciinema.org/) is our preferred option for videos rather than Vimeo/YouTube).

Please note, if there is too much “self-promotion”, submissions will be declined.

### Kali Blog RecapIn case you missed our recent [blog posts](https://www.kali.org/blog/), here’s what you missed:

- [Kali Linux in Linode’s Cloud](https://www.kali.org/blog/kali-and-linode/)
- [Secure Kali Pi (2022)](https://www.kali.org/blog/secure-kali-raspberry-pi/)
- [Weekly Virtual Machines, with Build Scripts](https://www.kali.org/blog/kali-vm-builder-weekly/)

If you would like them straight to your e-mail inbox, sign up to the [newsletter](https://www.kali.org/newsletter/).

### Community Shout-OutsIn this last quarter, there have been multiple contributions from a number of people (the joy of [Kali Linux being open-source](https://www.kali.org/docs/policy/kali-linux-open-source-policy/)). We do thank you guys! A few of these people’s actions have helped make a significant improvement to Kali, so we want to call them out:

- [Cloudflare](https://blog.cloudflare.com/cloudflare-repositories-ftw/)’s Jade Wang who has been working on some behind the scene stuff for us
- [Lorenzo Bernardi](https://gitlab.com/fastlorenzo) for helping with Azure (Yes, it’s coming back soon…)
- [Mark Egan-Fuller](https://gitlab.com/markeganfuller) and [elrey (alex)](https://gitlab.com/elreydetoda) for helping get a QEMU Vagrant image building - go [check it out](https://app.vagrantup.com/kalilinux/boxes/rolling)!

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)! And, in case you didn’t know, you can always follow how Kali is going by checking out the [activity](https://gitlab.com/groups/kalilinux/-/activity) page of our GitLab!

### Get Kali Linux 2022.3Fresh Images:
So what are you waiting for? Go [get Kali](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for those who are not, we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you will have fewer updates to do.
Just know that these are automated builds that we do, not QA like we do for our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade

┌──(kali㉿kali)-[~]
└─$ cp -rbi /etc/skel/. ~

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2022.3. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2022.3"
VERSION_ID="2022.3"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT_DYNAMIC Debian 5.18.5-1kali6 (2022-07-07)

┌──(kali㉿kali)-[~]
└─$ uname -r
5.18.0-kali5-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And [Twitter](https://twitter.com/kalilinux) is not a Bug Tracker!

Want to keep in up-to-date easier? We have a [RSS feeds](https://www.kali.org/rss.xml) and [newsletter](https://www.kali.org/newsletter/) of our [blog](https://www.kali.org/blog/)!

## 2022.2 – 2022-05-16

**Kali Linux 2022.2 Release (GNOME 42, KDE 5.24 & hollywood-activate)**

Table of Contents
- [GNOME 42](#gnome-42)[GNOME 42’s Built-In Screenshot and Screencast Tool](#gnome-42s-built-in-screenshot-and-screencast-tool)

- [KDE Plasma 5.24](#kde-plasma-524)
- [Other Desktop Enhancements](#other-desktop-enhancements)[Xfce Tweaks](#xfce-tweaks)
- [App Icons](#app-icons)
- [Automated Copy of Missing Configurations:](#automated-copy-of-missing-configurations)
- [VirtualBox Shared Folder Support](#virtualbox-shared-folder-support)

- [Tweaks for the Terminal](#tweaks-for-the-terminal)
- [Hollywood Activate / Kali Screensaver (April Fools)](#hollywood-activate--kali-screensaver-april-fools)
- [Kali Unkaputtbar](#kali-unkaputtbar)[Features](#features)

- [Win-KeX 3.1](#win-kex-31)
- [New Tools in Kali](#new-tools-in-kali)
- [Kali NetHunter Updates](#kali-nethunter-updates)
- [Kali ARM Updates](#kali-arm-updates)
- [Kali Documentation Updates](#kali-documentation-updates)
- [Download Kali Linux 2022.2](#download-kali-linux-20222)

It’s that [time of year](https://www.kali.org/releases/) again, time for another Kali Linux release! Quarter #2 - Kali Linux 2022.2. This release has various impressive updates, all of which are ready for immediate [download](https://www.kali.org/get-kali/) or [updating](https://www.kali.org/docs/general-use/updating-kali/).

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2022.1 release from February 2022](https://www.kali.org/blog/kali-linux-2022-1-release/) is:

- [GNOME 42](#gnome-42) - Major release update of the popular desktop environment
- [KDE Plasma 5.24](#kde-plasma-524) - Version bump with a more polished experience
- [Multiple desktop enhancements](#other-desktop-enhancements) - Disabled motherboard beep on Xfce, alternative panel layout for ARM, better support for VirtualBox shared folders, and lots more
- [Tweaks for the terminal](#tweaks-for-the-terminal) - Enhanced Zsh syntax-highlighting, inclusion of Python3-pip and Python3-virtualenv by default
- [April fools - Hollywood mode](#hollywood-activate--kali-screensaver-april-fools) - Awesome screensaver
- [Kali Unkaputtbar**](#kali-unkaputtbar) - BTRFS snapshot support for Kali
- [Win-KeX 3.1](#win-kex-31) - sudo support for GUI apps
- [New tools](#new-tools-in-kali) - Various new tools added
- [WPS attacks in Kali NetHunter](#kali-nethunter-updates) - Added WPS attacks tab to the NetHunter app

### GNOME 42Like for every (almost) half-year, there is a new version bump for the GNOME desktop environment. Kali 2022.2 brings the new version, GNOME 42, which is a more polished experienced following the work previously introduced in versions 40 and 41.

The shell theme now includes a more modern look, removing the arrows from the pop-up menus and using more rounded edges. In addition, we’ve upgraded and tweaked the dash-to-dock extension, making it integrate better with the new look and fixing some bugs.

Here is a preview of the upgraded Kali themes for gnome-shell:

Kali-Dark:

https://www.kali.org/blog/kali-linux-2022-2-release/images/gnome-42-dark-theme.png

Kali-Light:

https://www.kali.org/blog/kali-linux-2022-2-release/images/gnome-42-light-theme.png

#### GNOME 42’s Built-In Screenshot and Screencast ToolWith GNOME 42, there is one new feature that is brighter than all of the others: the screenshot and screen-recording tool. It’s an enormous improvement in terms of user experience. Screenshots are, at the same time, saved to the ~/Pictures/Screenshots/ folder and copied to the clipboard, so the user does not need to find them.

Quick shortcuts to skip the On Screen Display (OSD) dialog:

- Window screenshot: Alt + PtrScr
- Full-screen screenshot: Shift + PtrScr

https://www.kali.org/blog/kali-linux-2022-2-release/images/gnome-42-screenshot-tool.png

### KDE Plasma 5.24This new Plasma release focuses on smoothing out wrinkles, evolving the design, and improving the overall feel and usability of the environment:

https://www.kali.org/blog/kali-linux-2022-2-release/images/kde-5.24.png

### Other Desktop Enhancements##### Xfce Tweaks
- Disable noisy motherboard beep when clicking the logout dialog!
Thank you [@DavidAlvesWeb](https://twitter.com/DavidAlvesWeb)!
- Configure mousepad (text editor) to add the missing newline at the end of the file (POSIX standard):
It was especially problematic if you used the text file in the terminal. Printing two files would show their respective last and first lines joined.
- Set the default wallpaper for multi-monitor setups
- Fix mouse pointer size to prevent auto-scaling in large displays
- New simplified panel layout for arm devices:
The layout we generally use for Xfce works perfectly, but it could not fit in undersized displays. This issue was common on ARM devices like the Raspberry Pi, which can use a screen the size of the board. Therefore, we have created an alternative panel layout that gets automatically applied for all ARM-based images. Here is an example of a display with a 800x480 resolution:

https://www.kali.org/blog/kali-linux-2022-2-release/images/arm-xfce-light-panel-theme.png

This modification also removes the CPU graph widget, not only due to the horizontal space it required, but also because it had a performance hit in low spec ARM devices.

##### App IconsIt has been some time since the last update of the kali menu. This time the icons for [nmap](https://www.kali.org/tools/nmap/), [ffuf](https://www.kali.org/tools/ffuf/), and [edb-debugger](https://www.kali.org/tools/edb-debugger/) were improved and updated, and new ones were added for [evil-winrm](https://www.kali.org/tools/evil-winrm/) and [bloodhound](https://www.kali.org/tools/bloodhound/).

Another improvement for the app dashboard is that the programs that include a user interface will now respect the custom icon provided by Kali. Previously, the icon in the app drawer showed the proper image, but once you launched it, the icon hardcoded to the program took preference, usually using a lower quality and pixelated image. This change will only affect KDE and GNOME desktops and, unfortunately, does not work on Xfce. Thankfully, this issue was more noticeable in these desktops, as icons in Xfce’s panel are tiny.

Before:

https://www.kali.org/blog/kali-linux-2022-2-release/images/running-app-icons-old.png

After:

https://www.kali.org/blog/kali-linux-2022-2-release/images/running-app-icons-new.png

##### Automated Copy of Missing Configurations:Generally, configuration files in Kali are stored outside of the $HOME directory, but some programs do not support this. As a workaround, some config-files need to be copied to the user’s home directory when it gets created.

This method has two issues:

- Firstly, if the user removes an important file inside their folder, the system might not behave as expected.
- Alternatively, the user will only receive the config-files available the moment it gets created. Therefore, if an OS update or program adds a new file (or modifies and existing), the user will not receive it unless they manually copy it.

With this change, the system will automatically copy any file from /etc/skel found missing in your home folder without replacing the already existing ones (do not worry, your changes will not get overwritten). So if, for example, you remove the Zsh shell configuration file, ~/.zshrc, the next time you log in, the file will be replaced.

##### VirtualBox Shared Folder SupportIf you are using VirtualBox, when a user account is created, it is now automatically added to the vboxsf group by default. This means if you are using VirtualBox, there is now one less step if you want to use shared folders.

### Tweaks for the Terminal
- Small changes to the Zsh syntax-highlighting colours to improving legibility.
- python3-pip and python3-virtualenv are now included by default Kali installations.
- Added shell autocompletion for John The Ripper.
- All …2john tools (zip2john, 7z2john, pdf2john, etc.) can now be called directly by just typing their name, no need to cd /usr/share/john/ first.
- Resource packages (wordlists, windows-resources, powersploit, etc.) now show a much clearer output with colours differentiating the type of file or directory:

https://www.kali.org/blog/kali-linux-2022-2-release/images/kali-treecd-tweaks.png

### Hollywood Activate / Kali Screensaver (April Fools)[Last year](https://twitter.com/kalilinux/status/1377659731913871362) for April Fools Day we did our “Kali 4 Kids” joke, which a scarily large number of people took VERY seriously. The number of organizations that contacted us wanting access to Kali 4 Kids was crazy.

This year, instead of celebrating with a joke, we wanted to give everyone something fun.

We have all seen Kali show up in movies and TV shows (like [Mr. Robot](https://www.kali.org/blog/mr-robot-arg-society/)) over the years. Hacking as shown in popular media, has ranged from really fun to completely absurd, so we saw the opportunity to do a tribute to some of our favourite instances (and get a little nostalgic).

Your browser does not support the video tag.Even though this project was designed for 1st April it still works as an awesome screensaver. For this reason, we thought it would be a good idea to keep it in our repository so you can install it whenever you want:

Installation:

┌──(kali㉿kali)-[~]
└─$ sudo apt -y install kali-screensaver

You can also install the hollywood-activate command to be able to launch it immediately from the terminal and avoid waiting for the screensaver to launch:

┌──(kali㉿kali)-[~]
└─$ sudo apt -y install hollywood-activate

┌──(kali㉿kali)-[~]
└─$ hollywood-activate

If you want this on macOS or Windows, [download the video file](https://gitlab.com/kalilinux/packages/kali-screensaver/-/blob/kali/master/hollywood-activate.mp4), and then use something like:

- macOS: [SaveHollywood](http://s.sudre.free.fr/Software/SaveHollywood/about.html)
- Windows: [videosaver](https://sourceforge.net/projects/videosaver/)

### Kali Unkaputtbar[Last March](https://www.kali.org/blog/unkaputtbar/) we introduced the official support for BTRFS snapshotting in Kali Linux. We call it [Kali Unkaputtbar](https://www.kali.org/docs/installation/btrfs/)!
Sounds great, doesn’t it!

Unkaputtbar brings Virtual Machines’ (VMs’) snapshot feature to bare-metal and injects some steroids.

Have you ever wished you could travel back in time after deleting that important customer report or after installing a broken driver (Nvidia?) just before heading into a board meeting? Well, you’d better read on, because now you can!

#### Features
- Boot snapshot
- Diff snapshots
- Browse snapshots
- Additional automatic snapshots

For more information, here you have all the [documentation for BTRFS Installation](https://www.kali.org/docs/installation/btrfs/).

https://www.kali.org/blog/kali-linux-2022-2-release/images/btrfs-rollback.png

Preview of Kali Unkaputtbar in action, showing all the previous snapshots you can choose from the boot menu.

### Win-KeX 3.1This update eliminates a restriction preventing GUI application from being run as root. Now you can start any GUI application with sudo, e.g.

sudo wireshark

https://www.kali.org/blog/kali-linux-2022-2-release/images/win-kex_sudo.png

### New Tools in KaliIt would not be a Kali release if there were not any new tools added! A quick run down of what has been added (to the network repositories):

- [BruteShark](https://www.kali.org/tools/bruteshark/) - Network Forensic Analysis Tool (NFAT)
- [Evil-WinRM](https://www.kali.org/tools/evil-winrm/) - Ultimate WinRM shell
- [Hakrawler](https://www.kali.org/tools/hakrawler/) - Web crawler designed for easy, quick discovery of endpoints and assets
- [Httpx](https://www.kali.org/tools/httpx-toolkit/) - Fast and multi-purpose HTTP toolkit
- [LAPSDumper](https://www.kali.org/tools/lapsdumper/) - Dumps LAPS passwords
- [PhpSploit](https://www.kali.org/tools/phpsploit/) - Stealth post-exploitation framework
- [PEDump](https://www.kali.org/tools/ruby-pedump/) - Dump Win32 executable files
- [SentryPeer](https://www.kali.org/tools/sentrypeer/) - SIP peer-to-peer honeypot for VoIP
- [Sparrow-wifi](https://www.kali.org/tools/sparrow-wifi/) - Graphical Wi-Fi Analyzer for Linux
- [wifipumpkin3](https://www.kali.org/tools/wifipumpkin3/) - Powerful framework for rogue access points

We want Kali to be able to access and interact with as many different services as possible. We all know that databases often contain juicy information. And [MongoDB](https://pkg.kali.org/pkg/mongodb) is no exception. The client has been restored & fixed up. Sorry for the down time!

There have been numerous packages updates as well.

### Kali NetHunter Updateshttps://www.kali.org/blog/kali-linux-2022-2-release/images/WPSonNH-Watch.png

The legendary [yesimxev](https://gitlab.com/yesimxev) has added a new WPS Attacks tab to the Kali NetHunter app, which utilizes OneShot to perform various WPS attacks without monitor mode from your internal wireless chip, even from your Kali NetHunter watch!

The TicWatch Pro 3 GPS, LTE, Ultra GPS, Ultra LTEare receiving initial NetHunter support. It features the same functionalities as the TicWatch Pro, except BadUSB. We are Trying Harder to bring you even more for the next release on this watch! In the meantime, all TicWatch Pros are now supported - TicWatch Pro, Pro 2020, Pro 4G/LTE.

Head over to our [documentation site](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-ticwatch-pro-3/) for a step-by-step guide on how to install Kali NetHunter on your TicWatch Pro 3 device.

### Kali ARM UpdatesRaspberry Pi:

- Bump kernel to 5.10.103
- Bluetooth is fixed, for real this time
- Wi-Fi firmware now uses 7.45.206 by default instead of 7.45.154, with nexmon patches applied
- Raspberry Pi Zero 2 W is now supported by nexmon
- Improvements to the wpa_supplicant.conf handling
- Kernel has NVME support built in, instead of module, so Raspberry Pi Compute Modules that use NVMe for their root device will work out of the box
- The Raspberry Pi userland is now packaged up for ARM64 instead of built manually at image creation

Pinebook Pro:

- Use the Kali kernel and u-boot instead of compiling our own

USB Armory MKII:

- Bump to kernel 5.15

Radxa Zero:

- Build scripts available for either eMMC or SD Card. Documentation still needs to be written, but loosely follow the instructions on the Radxa Zero wiki

Build Script improvements:

- command-not-found and kali-tweaks are included in minimal builds
- The base directory is now cleaned up at build completion instead of an empty directory left around

We would also like to give a [community shout-out](https://www.kali.org/docs/community/contribute/) to [Syndrowm](https://www.kali.org/cdn-cgi/l/email-protection#7b0802151f09140c163b1c161a121755181416), who improved wpa_supplicant.conf handling on Raspberry Pi devices - thank you!

### Kali Documentation UpdatesWe’ve pushed a couple of changes to the [Kali-Docs](https://www.kali.org/docs/) during this time as well. One new page that we think Apple silicon users will enjoy, and a sizeable change to another page that will interest any users wishing to access a “Desktop” (aka Graphical User Interface - GUI) from a normally strictly headless instance.

- [Running x86 on ARM](https://www.kali.org/docs/arm/x86-on-arm/) (New)
- [Accessing Xfce with RDP](https://www.kali.org/docs/general-use/xfce-with-rdp/) (Updated)

### Download Kali Linux 2022.2Fresh Images:
So what are you waiting for? Start [downloading](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for those who are not, we also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead. This way you will have fewer updates to do.

Just know that these are automated builds that we do, not QA like we do for our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2022.2. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2022.2"
VERSION_ID="2022.2"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP PREEMPT Debian 5.16.18-1kali1 (2022-04-01)

┌──(kali㉿kali)-[~]
└─$ uname -r
5.16.0-kali7-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And [Twitter](https://twitter.com/kalilinux) is not a Bug Tracker!

Want to keep in up-to-date easier? We have a [RSS feeds](https://www.kali.org/rss.xml) & [newsletter](https://www.kali.org/newsletter/) of our [blog](https://www.kali.org/blog/)!

## 2022.1 – 2022-02-14

**Kali Linux 2022.1 Release (Visual Updates, Kali Everything ISOs, Legacy SSH)**

Table of Contents
- [Visual Refresh: Theme Updates](#visual-refresh-theme-updates)
- [Shell Prompt Changes](#shell-prompt-changes)
- [Refreshed Browser Landing Page](#refreshed-browser-landing-page)
- [Kali Everything Image: Everything in one place](#kali-everything-image-everything-in-one-place)
- [Kali-Tweaks: Legacy SSH Made Easy](#kali-tweaks-legacy-ssh-made-easy)
- [VMware i3 Improvements](#vmware-i3-improvements)
- [Accessibility: Talk To Me](#accessibility-talk-to-me)
- [New Tools in Kali](#new-tools-in-kali)
- [Kali ARM Updates](#kali-arm-updates)
- [Community Shout-Outs](#community-shout-outs)
- [Download Kali Linux 2022.1](#download-kali-linux-20221)

Today we are pushing out the first Kali Linux [release](https://www.kali.org/releases/) of the new year with Kali Linux 2022.1, and just in time for Valentine’s Day! This release brings various visual updates and tweaks to existing features, and is ready to be [downloaded](https://www.kali.org/get-kali/) or [upgraded if you have an existing Kali Linux installation](https://www.kali.org/docs/general-use/updating-kali/).

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2021.4 release from December 2021](https://www.kali.org/blog/kali-linux-2021-4-release/) is:

- [Visual Refresh](#visual-refresh-theme-updates) - Updated wallpapers and GRUB theme
- [Shell Prompt Changes](#shell-prompt-changes) - Visual improvements to improve readability when copying code
- [Refreshed Browser Landing Page](#refreshed-browser-landing-page) - Firefox and Chromium homepage has had a makeover to help you access everything Kali you need
- [Kali Everything Image](#kali-everything-image-everything-in-one-place) - An all-packages-in-one solution now available to download
- [Kali-Tweaks Meets SSH](#kali-tweaks-legacy-ssh-made-easy) - Connect to old SSH servers using legacy SSH protocols and ciphers
- [VMware i3 Improvements](#vmware-i3-improvements) - Host-guest features properly work now on i3
- [Accessibility Features](#accessibility-talk-to-me) - Speech synthesis is back in the Kali installer
- [New Tools](#new-tools-in-kali) - Various new tools added, many from ProjectDiscovery!

Besides that, we have been working on a new feature, which just isn’t quite ready yet (as the [documentation](https://www.kali.org/docs/) is still in progress!). It’s a large one, so it’s going to have its own blog post once ready to help demonstrate its importance to us. This one is for you bare-metal installers!

Edit: [Now out](https://www.kali.org/blog/unkaputtbar/)!

### Visual Refresh: Theme UpdatesAs promised back in [Kali 2021.2](https://www.kali.org/blog/kali-linux-2021-2-release/), beginning with this release (2022.1) going forwards, our yearly 20xx.1 versions will be the only releases to have the main visual updates. Using a yearly lifecycle, it makes it easier to recognize the different versions of Kali Linux over time. This update includes new wallpapers for desktop, login, and boot displays, in addition to a refreshed installer theme which you may have seen if you have recently [updated](https://www.kali.org/docs/general-use/updating-kali/).

https://www.kali.org/blog/kali-linux-2022-1-release/images/desktop-wallpaper.png

https://www.kali.org/blog/kali-linux-2022-1-release/images/login-wallpaper.png

Moreover, the functions, theme and layout of the boot menu present in our ISO images have been improved. With these changes, it makes them consistent throughout. Previously, the menus in the UEFI and the BIOS boot menus had different options, designs, and were also written differently, making them confusing. Throw into the mix that there were multiple differences between “installer”, “live”, “netinstall” and “mini” options as well. All of these problems have been addressed and they now have a universal feel to them all.

https://www.kali.org/blog/kali-linux-2022-1-release/images/boot-theme.png

### Shell Prompt ChangesYou talked, we listened. We have made a few tweaks which we hope will make your life easier since our last prompt update in [2020.4](https://www.kali.org/blog/kali-linux-2020-4-release/). Examples of this problem may be when writing a professional pentesting report or collaborating on debugging code and sharing the terminal, the right-side prompt (which had the exit code and the number of background processes) may of gotten in the way. So it has been removed from our default shell, ZSH. Along with this, the skull in the root prompt has been replaced with a simple ㉿. For those that miss the root skull (💀), you can easily edit your ~/.zshrc:

┌──(root㉿kali)-[~]
└─# sed -i 's/prompt_symbol=㉿/prompt_symbol=💀/' ~/.zshrc

┌──(root㉿kali)-[~]
└─# source ~/.zshrc

┌──(root💀kali)-[~]
└─#

If you do a fresh install of Kali 2022.1, you will have these changes. If you are upgrading, you will need to manually apply these edits by doing the following:

┌──(kali㉿kali)-[~]
└─$ cp -i /etc/skel/.{bash,zsh}rc ~/

### Refreshed Browser Landing PageThis release comes with a fresh new look for the default landing page shipped inside Kali. Utilizing the refreshed documentation sites ([Kali-Docs](https://www.kali.org/docs/) and [Kali-Tools](https://www.kali.org/tools/)), the search function will help you find almost anything you could need using Kali Linux!

https://www.kali.org/blog/kali-linux-2022-1-release/images/firefox-home-page.png

### Kali Everything Image: Everything in one placeThis release will welcome a new flavor, the “kali-linux-everything” image. This allows for a complete offline standalone image (ISO), for those who require all of Kali’s tools to be pre-installed. Unlike [previously](https://www.kali.org/blog/kali-linux-2020-2-release/), users will not be required to download the “kali-linux-everything” packages during Kali’s setup via a network mirror, as they will be located on the same media, but the image is much larger to initially download due to this. Because of the size increase, (~2.8GB to ~9.4GB), these images will be only initially offered using a technology that its designed to handle the traffic, BitTorrent. Additionally, as there are more packages, it will take longer to also install Kali.

If you understand what you are doing, and this sounds like something you would like, [grab the torrents](https://www.kali.org/get-kali/) and give it a try!

To learn more about the grouping of Kali’s packages, please see our documentation about [metapackages](https://www.kali.org/docs/general-use/metapackages/).

This will not include [Kaboxer](https://www.kali.org/blog/introducing-kaboxer/) applications at this point in time, due to a known limitation.

### Kali-Tweaks: Legacy SSH Made EasyThere is a new setting in the kali-tweaks Hardening section! It is now possible to configure Kali’s SSH client for Wide Compatibility, which means that old algorithms and ciphers are enabled. Thanks to that, connecting to old servers that use those is now straightforward, no need to pass additional options explicitly on the command-line.

The purpose of this setting is to make it easier to discover vulnerable SSH servers, just like [explained previously](https://www.kali.org/blog/kali-linux-2021-3-release/) this opens up more potential attack surfaces (which is how this came about, due to a recent pentest, a Uninterruptible Power Supply gave us our foothold to complete network pwnage).

Please note, unlike [OpenSSL](https://www.kali.org/blog/kali-linux-2021-3-release/) and [Samba](https://www.kali.org/blog/kali-linux-2021-4-release/), this weakened behaviour is NOT enabled by default, as SSH is a sensitive enough component that we prefer to keep it Secure by default. Therefore if you are interested in this setting, you will have to run kali-tweaks, enter the Hardening section and enable it in there.

Here is what the Hardening screen looks like currently:

https://www.kali.org/blog/kali-linux-2022-1-release/images/kali-tweaks-hardening.png

### VMware i3 ImprovementsFor users that use Kali in a guest VM with the i3 desktop environment (kali-desktop-i3), VMware’s host-guest features (e.g. drag ’n’ drop, copy/paste) were not enabled by default, it had to be done manually. This is now fixed and you should not have anything to do, it should work out of the box. This was enabled with package [i3-wm](https://pkg.kali.org/pkg/i3-wm) 4.20.1-1.

### Accessibility: Talk To MeWe have always tried to support as many users of Kali as possible. This is true from our [early releases](https://www.kali.org/blog/kali-linux-1-0-3-release/) through to today.

To help blind and visually impaired users, we are pleased to say speech synthesis is back in the Kali setup. When we released [Kali 2021.4](https://www.kali.org/blog/kali-linux-2021-4-release/), the sound in the installer broke. This was due to a packaging bug in the sound driver, and unfortunately this issue went unnoticed for a while. This is now fixed. Big thanks to isfr8585 who reported the [issue](https://bugs.kali.org/view.php?id=7467)!

### New Tools in KaliBetween numerous packages updates, there has been various new tools added! A quick breakdown of what has been added (to the network repositories):

- [dnsx](https://pkg.kali.org/pkg/dnsx) - Fast and multi-purpose DNS toolkit allow to run multiple DNS queries
- [email2phonenumber](https://pkg.kali.org/pkg/email2phonenumber) - An OSINT tool to obtain a target’s phone number just by having his email address
- [naabu](https://pkg.kali.org/pkg/naabu) - A fast port scanner with a focus on reliability and simplicity
- [nuclei](https://pkg.kali.org/pkg/nuclei) - Targeted scanning based on templates
- [PoshC2](https://pkg.kali.org/pkg/poshc2) - A proxy aware C2 framework with post-exploitation and lateral movement
- [proxify](https://pkg.kali.org/pkg/proxify) - Swiss Army knife Proxy tool for HTTP/HTTPS traffic capture, manipulation, and replay on the go

Shout-out to [ProjectDiscovery](https://projectdiscovery.io/) for their work & tools!

### Kali ARM UpdatesA list of packages that were previously not available for the arm64 architecture, and that have been added in this release:

- [feroxbuster](https://pkg.kali.org/pkg/feroxbuster)
- [ghidra](https://pkg.kali.org/pkg/ghidra)

Bluetooth should now be fixed on the RaspberryPi images, aside from the Zero 2 W, which we are still hunting down a fix for and will release an updated image when it is ready. There was a change with the bootloader that changed the serial device name being used.

Image file names have changed to be a bit more verbose with their naming, instead of using short-hand or nicknames of devices.

The build scripts now have a [documentation page](https://www.kali.org/docs/development/arm-build-scripts/) that explains them a bit more in depth.

The RaspberryPi Zero 2 W device has documentation now as well.

### Community Shout-OutsThese are people from the public who have helped Kali and the team for the last release. And we want to praise them for their work (we like to give credit where due!):

- [@Greg Myers](https://infosec.exchange/@gre9) who helped to clean up our kali-docs
- [@Void Your Warranty](https://gitlab.com/voidyourwarranty) who contributed a very helpful [encrypted standalone USB](https://www.kali.org/docs/usb/usb-standalone-encrypted/) kali-docs page
- [@D](https://gitlab.com/cyrus104) for his contributions on the Gatworks Ventana and Gateworks Newport Kali ARM build-scripts
- [@1y](https://gitlab.com/1y) for contributing the i.MX6ULL EVK Kali ARM build-script, which we accidentally dropped during the refactoring. It has now been restored.

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

### Download Kali Linux 2022.1Fresh Images:
So what are you waiting for? Start [downloading](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for the ones who are not, we do also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use as well. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you will have fewer updates to do.
Just know that these are automated builds that we do not QA like we do our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade

┌──(kali㉿kali)-[~]
└─$ cp -rbi /etc/skel/. ~

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2022.1. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2022.1"
VERSION_ID="2022.1"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP Debian 5.15.15-2kali1 (2022-01-31)

┌──(kali㉿kali)-[~]
└─$ uname -r
5.15.0-kali3-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We will never be able to fix what we do not know is broken! And [Twitter](https://twitter.com/kalilinux) is not a Bug Tracker!

Want to keep in up-to-date easier? We have a [RSS feeds](https://www.kali.org/rss.xml) & [newsletter](https://www.kali.org/newsletter/) of our [blog](https://www.kali.org/blog/)!

## 2021.4 – 2021-12-09

**Kali Linux 2021.4 Release**

Table of Contents
- [Kali on the Apple M1](#kali-on-the-apple-m1)
- [Extended Compatibility for the Samba Client](#extended-compatibility-for-the-samba-client)
- [Easy Package Manager Mirror Configuration](#easy-package-manager-mirror-configuration)
- [Kaboxer Theme Support](#kaboxer-theme-support)
- [New Tools in Kali](#new-tools-in-kali)
- [Desktop & Theme Enhancement](#desktop--theme-enhancement)[Xfce](#xfce)
- [GNOME 41](#gnome-41)
- [KDE 5.23](#kde-523)
- [How to Upgrade Your Kali Theme](#how-to-upgrade-your-kali-theme)

- [Kali NetHunter Updates](#kali-nethunter-updates)
- [Kali ARM Updates](#kali-arm-updates)
- [Kali-Docs Updates](#kali-docs-updates)
- [Miscellaneous](#miscellaneous)
- [Download Kali Linux 2021.4](#download-kali-linux-20214)

With the end of 2021 just around the corner, we are pushing out the last [release](https://www.kali.org/releases/) of the year with Kali Linux 2021.4, which is ready for immediate [download](https://www.kali.org/get-kali/) or [updating](https://www.kali.org/docs/general-use/updating-kali/).

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2021.3 release from September 2021](https://www.kali.org/blog/kali-linux-2021-3-release/) is:

- [Improved Apple M1 support](#kali-on-the-apple-m1)
- [Wide compatibility for Samba](#extended-compatibility-for-the-samba-client)
- [Switching package manager mirrors](#easy-package-manager-mirror-configuration)
- [Kaboxer theming](#kaboxer-theme-support)
- [Updates to Xfce, GNOME and KDE](#desktop--theme-enhancement)
- [Raspberry Pi Zero 2 W + USBArmory MkII ARM images](#kali-arm-updates)
- [More tools](#new-tools-in-kali)

### Kali on the Apple M1As we announced in [Kali 2021.1](https://www.kali.org/blog/kali-linux-2021-1-release/) we supported installing Kali Linux on Parallels on Apple Silicon Macs, well with 2021.4, we now also support it on the [VMware Fusion Public Tech Preview](https://blogs.vmware.com/teamfusion/2021/09/fusion-for-m1-public-tech-preview-now-available.html) thanks to the [5.14 kernel](https://pkg.kali.org/pkg/linux) having the modules needed for the virtual GPU used. We also have updated the open-vm-tools [package](https://pkg.kali.org/pkg/open-vm-tools), and [Kali’s installer](https://pkg.kali.org/pkg/debian-installer) will automatically detect if you are installing under VMware and install the open-vm-tools-desktop package, which should allow you to change the resolution out of the box. As a reminder, this is still a preview from VMware, so there may be some rough edges. There is no extra [documentation](https://www.kali.org/docs/virtualization/install-vmware-guest-vm/) for this because the [installation process](https://www.kali.org/docs/installation/hard-disk-install/) is the same as VMWare on 64-bit and 32-bit Intel systems, just using the [arm64 ISO](https://www.kali.org/get-kali/).

As a reminder, virtual machines on Apple Silicon are still limited to arm64 architecture only.

### Extended Compatibility for the Samba ClientStarting Kali Linux 2021.4, the [Samba](https://pkg.kali.org/pkg/samba) client is now configured for Wide Compatibility so that it can connect to pretty much every Samba server out there, regardless of the version of the protocol in use. This change should make it easier to discover vulnerable Samba servers “out of the box”, without having to configure Kali.

This setting can be changed easily via the command-line tool kali-tweaks. In the Hardening section, one can choose the value Default instead, which reverts back to Samba’s usual default, and only allow using modern versions of the Samba protocol.

https://www.kali.org/blog/kali-linux-2021-4-release/images/kali-tweaks-hardening.png

As one can see on this screenshot, there’s also a similar setting for [OpenSSL](https://pkg.kali.org/pkg/openssl). You might want to refer to the [2021.3 release announcement](https://www.kali.org/blog/kali-linux-2021-3-release/) for more details on this setting.

### Easy Package Manager Mirror ConfigurationBy default, when a Kali system is updated, the package manager ([APT](https://pkg.kali.org/pkg/apt)) downloads packages from a [community mirror](https://www.kali.org/docs/general-use/kali-apt-sources/) nearby. But did you know that it’s also possible to configure Kali to get its package from the [Cloudflare CDN](https://blog.cloudflare.com/cloudflare-repositories-ftw/)? To be honest, [this is old news](https://www.kali.org/blog/kali-linux-2019-3-release/). But what’s new is that you can now use kali-tweaks to quickly configure whether APT should use community mirrors or the Cloudflare CDN.

https://www.kali.org/blog/kali-linux-2021-4-release/images/kali-tweaks-mirrors.png

So which one is best, community mirrors or Cloudflare CDN? There’s no good answer. The time that it actually takes to update Kali can vary greatly and depends on many factors, including the speed of your Internet connection, your location, and even the time of day, if ever you live in a place where Internet traffic jam occurs at rush hour. The point is: if ever Kali updates are slow, the best you can do is to try to switch from community mirrors to Cloudflare CDN, or the other way round, and find what works best for you. And with kali-tweaks, it’s never been easier!

### Kaboxer Theme SupportWith the latest update of [Kaboxer](https://pkg.kali.org/pkg/kaboxer) tools no longer look out of place, as it brings support for window themes and icon themes (placed respectively inside /usr/share/themes and /usr/share/icons). This allows the program to properly integrate with the rest of the desktop and avoids the usage of ugly fallback themes.

Here is a comparison of how zenmap (zenmap-kbx [package](https://pkg.kali.org/pkg/zenmap-kbx)) looks with the default Kali Dark theme, compared to the old appearance:

https://www.kali.org/blog/kali-linux-2021-4-release/images/kaboxer-theme-support.png

### New Tools in KaliIt would not be a Kali release if there were not any new tools added! A quick run down of what’s been added (to the [network repositories](https://www.kali.org/docs/general-use/kali-apt-sources/)):

- [Dufflebag](https://pkg.kali.org/pkg/dufflebag) - Search exposed EBS volumes for secrets
- [Maryam](https://pkg.kali.org/pkg/maryam) - Open-source Intelligence (OSINT) Framework
- [Name-That-Hash](https://pkg.kali.org/pkg/name-that-hash) - Do not know what type of hash it is? Name That Hash will name that hash type!
- [Proxmark3](https://pkg.kali.org/pkg/proxmark3) - if you are into Proxmark3 and RFID hacking
- [Reverse Proxy Grapher](https://pkg.kali.org/pkg/rev-proxy-grapher) - graphviz graph illustrating your reverse proxy flow
- [S3Scanner](https://pkg.kali.org/pkg/s3scanner) - Scan for open S3 buckets and dump the contents
- [Spraykatz](https://pkg.kali.org/pkg/spraykatz) - Credentials gathering tool automating remote procdump and parse of lsass process.
- [truffleHog](https://pkg.kali.org/pkg/trufflehog) - Searches through git repositories for high entropy strings and secrets, digging deep into commit history
- [Web of trust grapher (wotmate)](https://pkg.kali.org/pkg/wotmate) - reimplement the defunct PGP pathfinder without needing anything other than your own keyring

### Desktop & Theme EnhancementThis release brings updates for all the 3 main desktops ([Xfce](https://pkg.kali.org/pkg/xfce4), [GNOME](https://pkg.kali.org/pkg/gnome-shell), and [KDE](https://pkg.kali.org/pkg/kde-plasma-desktop)), but one that is common to all of them is the new window buttons design. Previous buttons were designed to fit the window theme of Xfce but did not work well with the other desktops and lacked personality. The new design looks elegant on any of the desktops and makes it easier to spot the currently focused window.

https://www.kali.org/blog/kali-linux-2021-4-release/images/new-window-buttons.png

#### XfceThe panel layout has been tweaked to optimize horizontal space and make room for 2 new widgets: the CPU usage widget and the VPN IP widget, which remains hidden unless a VPN connection is established.

Following the steps of other desktops, the task manager has been configured to “icons only”, which, with the slight increase in the panel’s height, makes the overall look cleaner and improves multitasking in smaller displays.

The workspaces overview has been configured to the “Buttons” appearance, as the previous configuration “Miniature view” was too wide and a bit confusing for some users. Now that each workspace button takes less space in the panel, we have increased the default number of workspaces to 4, as it’s a usual arrangement in Linux desktops.

To finish with the modifications, a shortcut to PowerShell has been added to the terminals dropdown menu. With this addition, you can now choose between the regular terminal, root terminal, and PowerShell.

If you prefer the previous configuration for any of the widgets, you can modify or remove them by pressing Ctrl + Right-Click over it.

https://www.kali.org/blog/kali-linux-2021-4-release/images/xfce-layout-updates.png

In addition to the Xfce design tweaks, In the image above, we can also observe the new customized prompt for PowerShell (in the two-line mode). Same as for [zsh](https://pkg.kali.org/pkg/zsh) and [bash](https://pkg.kali.org/pkg/bash), it includes an alternative one-line prompt that can be configured with kali-tweaks.

Bonus Tips For Virtual Desktops!

- You can add or remove workspaces with the shortcuts: Alt + Insert / Alt + Delete
- You can move through workspaces with the shortcuts:Ctrl + Alt + <ARROW_KEY> to move in the direction of the arrow key.(if you add Shift you move the current focused window)

- Ctrl + Alt + <WORKSPACE_NUM> to move to a specific workspace, based on its number.
- Ctrl + Super + <WORKSPACE_NUM> to move a window to a specific workspace, based on its number.

https://www.kali.org/blog/kali-linux-2021-4-release/images/workspaces-shortcuts-demo.gif

#### GNOME 41In this update, GNOME desktop has received not one, but two version bumps. It’s been one year since the last major update of the GNOME desktop in Kali (with GNOME 3.38) and since then there have been two releases of the desktop environment:

- [Introducing GNOME 40](https://help.gnome.org/misc/release-notes/40.0/)
- [Introducing GNOME 41](https://help.gnome.org/misc/release-notes/41.0/)

All themes and extensions have been updated to support the new shell:

https://www.kali.org/blog/kali-linux-2021-4-release/images/gnome41.png

https://www.kali.org/blog/kali-linux-2021-4-release/images/gnome41-overview.png

#### KDE 5.23The KDE team celebrated its 25th anniversary releasing the update [5.23](https://kde.org/announcements/plasma/5/5.23.0/) of the Plasma desktop. This update, now available in Kali, brings a new design for the Breeze theme, which improves the look of Plasma with details that add glossiness and style to the desktop. Along with the theme improvements, the System Settings (Under Global Theme > Colors) brings a new option to pick the desktop accent color.

From Kali’s side, the new window theme for KDE is now based on the source code of the breeze theme instead of using the Aurorae theme engine. This fixes previous issues with window scaling for [HiDPI displays](https://www.kali.org/docs/general-use/hidpi/).

#### How to Upgrade Your Kali ThemeWith these theme changes, you may not get them if you [upgrade](https://www.kali.org/docs/general-use/updating-kali/) Kali. This is because the theme settings are copied to your home folder when your user is first created. When you upgrade Kali, it is upgrading the operating system, so upgrading does not alter personal files (just system files). As a result, in order to get these theme tweaks, you need to either:

- Do a fresh Kali install
- Create a new user and switch to that
- Delete your Desktop environment profile for the current user and force reboot. Example of Xfce can be found below:

kali@kali:~$ mv ~/.config/xfce4{,-$(date +%Y.%m.%d-%H.%M.%S)}
kali@kali:~$
kali@kali:~$ cp -rbi /etc/skel/. ~/
kali@kali:~$
kali@kali:~$ xfce4-session-logout --reboot --fast

### Kali NetHunter Updateshttps://www.kali.org/blog/kali-linux-2021-4-release/images/NH-SET.png

Thanks to the amazing work of [yesimxev](https://gitlab.com/yesimxev), we have a new addition to the NetHunter app: The Social-Engineer Toolkit!

This release features the first module from SET: the Spear Phishing Email Attack, with many more to come - watch this space…

Now you can use the Kali NetHunter app to customise your own Facebook, Messenger, or Twitter direct message email notifications for your social engineering attacks:

Your browser does not support the video tag.Thanks to everyone that contributed to this feature by participating in the [Twitter poll](https://twitter.com/yesimxev/status/1451314339554660359). We could not have done it without your input!

### Kali ARM UpdatesNotable changes this release

- All images now use ext4 for their root filesystem, and resize the root filesystem on first boot. This results in a speed-up over previous releases which were using ext3, and a reduced boot time on the first reboot when resize happens.
- Raspberry Pi Zero 2 W support has been added, but like the Raspberry Pi 400, there is no Nexmon support.
- Speaking of the Raspberry Pi Zero 2 W, since it is so similar to the Zero W, we have also added a PiTail image to support the new processor with better performance.
- Raspberry Pi images now support USB booting out of the box since we no longer hardcode the root device.
- Raspberry Pi images now include versioned Nexmon firmware. A future release of kalipi-config will allow you to switch between them, if you would like to test different versions.
- Images that use a vendor kernel will now be able to set the regulatory domain properly, so setting your country will give access to channels properly for wireless.
- Pinebook Pro can now be overclocked. The big cores get 2GHz and the little cores get 1.5GHz added.echo 1 | sudo tee /sys/devices/system/cpu/cpufreq/boost to enable
- echo 0 | sudo tee /sys/devices/system/cpu/cpufreq/boost to disable

- USBArmory MkII image has been added.

[Kali ARM build-scripts](https://gitlab.com/kalilinux/build-scripts/kali-arm) have seen a massive amount of changes:

- They are vastly more simplified - thanks to [@Francisco Jose Rodriguez Martos](https://twitter.com/FrangaLinux), and [@cyrus104](https://gitlab.com/cyrus104) for all of their contributions to make this happen.
- You can now choose which desktop you would like to install (or none at all using --minimal)
- There is even an option of no desktop and no tools (--slim) if you would like to build a custom image up from scratch

### Kali-Docs Updates
- [Installing Flatpak on Kali Linux](https://www.kali.org/docs/tools/flatpak/) is now well documented
- A new page for the [Raspberry Pi Zero 2 W](https://www.kali.org/docs/arm/raspberry-pi-zero-2-w/) has been added
- The [Kali branches](https://www.kali.org/docs/general-use/kali-branches/) page has been refreshed with best practices and references to kali-tweaks that help you follow those best practices to enable (or disable) some of the supplementary repositories.
- We added a [list of removed tools](https://www.kali.org/docs/tools/removed-tools/) so that you can learn why a package got dropped from Kali.
- Thanks also to [Aman Kumar Maurya](https://gitlab.com/mayomacam) for the [nVidia](https://www.kali.org/docs/general-use/install-nvidia-drivers-on-kali-linux/) guide

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

### MiscellaneousKali-Cloud & Cron

Some [users](https://twitter.com/DHAhole) noticed that the venerable cron [package](https://pkg.kali.org/pkg/cron) was missing from the [Kali AWS Cloud image](https://www.kali.org/get-kali/#kali-cloud). This was not intentional, and it’s now fixed.

Remote Desktop Protocol Audio

“The quieter you become, the more you are able to hear”, goes the saying. And for those running Kali in a VM and using RDP to connect, it’s been very quiet indeed, as the sound never worked with this configuration. However this long period of silence is coming to an end! Sound should be enabled and work out of the box from now on. If ever it does not, make yourself heard on the [bug tracker](https://bugs.kali.org/) ;)

Python Command

The command python is no more! Instead, you need to use python3 (or [if you have to](https://www.kali.org/docs/general-use/using-eol-python-versions/), python2 due it being at [End Of Life](https://www.kali.org/blog/python-2-end-of-life/)). Alternatively you can install python-is-python3 to restore python as an alias for python3.

### Download Kali Linux 2021.4Fresh Images:
So what are you waiting for? Start [downloading](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for the ones who are not, we do also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use as well. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you’ll have fewer updates to do.
Just know that these are automated builds that we do not QA like we do our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade

┌──(kali㉿kali)-[~]
└─$ cp -rbi /etc/skel/. ~

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2021.4. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2021.4"
VERSION_ID="2021.4"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP Debian 5.14.16-1kali1 (2021-11-05)

┌──(kali㉿kali)-[~]
└─$ uname -r
5.14.0-kali4-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We’ll never be able to fix what we do not know is broken! And [Twitter](https://twitter.com/kalilinux) is not a Bug Tracker!

## 2021.3 – 2021-09-14

**Kali Linux 2021.3 Release (OpenSSL, Kali-Tools, Kali Live VM Support, Kali NetHunter Smartwatch)**

Table of Contents
- [OpenSSL: wide compatibility by default](#openssl-wide-compatibility-by-default)
- [Kali-Tools](#kali-tools)
- [Virtualization: improvements all over the place](#virtualization-improvements-all-over-the-place)
- [New Tools in Kali](#new-tools-in-kali)
- [Kali NetHunter Updates](#kali-nethunter-updates)[Kali NetHunter Watch](#kali-nethunter-watch)
- [Kali NetHunter Installation via Magisk](#kali-nethunter-installation-via-magisk)
- [Kali NetHunter installation step-by-step guide for our preferred device, the OnePlus 7](#kali-nethunter-installation-step-by-step-guide-for-our-preferred-device-the-oneplus-7)

- [Kali ARM Updates](#kali-arm-updates)
- [Desktop & Theme Updates](#desktop--theme-updates)
- [Kali-Docs Updates](#kali-docs-updates)
- [GitLab Commit 2021](#gitlab-commit-2021)
- [Ampere & ARM](#ampere--arm)
- [Upcoming Changes](#upcoming-changes)
- [Download Kali Linux 2021.3](#download-kali-linux-20213)

Today we have released the newest version of Kali Linux, 2021.3 (quarter #3), which is now ready for [download](https://www.kali.org/get-kali/) or [updating](https://www.kali.org/docs/general-use/updating-kali/).

A summary of the [changes](https://bugs.kali.org/changelog_page.php) since the [2021.2 release from June](https://www.kali.org/blog/kali-linux-2021-2-release/) are:

- [OpenSSL](#openssl-wide-compatibility-by-default) - Wide compatibility by default - Keep reading for what that means
- [New Kali-Tools site](#kali-tools) - Following the footsteps of Kali-Docs, Kali-Tools has had a complete refresh
- [Better VM support in the Live image session](#virtualization-improvements-all-over-the-place) - Copy & paste and drag & drop from your machine into a Kali VM by default
- [New tools](#new-tools-in-kali) - From adversary emulation, to subdomain takeover to Wi-Fi attacks
- [Kali NetHunter smartwatch](#kali-nethunter-updates) - First of its kind, for TicHunter Pro
- [KDE 5.21](#desktop--theme-updates) - Plasma desktop received a version bump

### OpenSSL: wide compatibility by defaultGoing forwards from Kali Linux 2021.3, OpenSSL has now been configured for wider compatibility to allow Kali to talk to as many services as possible. This means that legacy protocols (such as TLS 1.0 and TLS 1.1) and older ciphers are enabled by default. This is done to help increase Kali’s ability to talk to older, obsolete systems and servers that are still using these older protocols. This may potentially increase your options on available attack surfaces (if your target has these End of Life (EoL) services running, having then forgotten about them, what else could this uncover?). While this is not a configuration that would be good for a general purpose operating systems, this setting makes sense for Kali as it enables the user to engage and talk with more potential targets.

This setting is easy to modify via the command-line tool kali-tweaks though. Enter the Hardening section, and from there you can configure OpenSSL for Strong Security mode instead, which uses today’s current modern standard allowing for secure communication.

For more details, refer to the documentation: [kali.org/docs/general-use/openssl-configuration/](https://www.kali.org/docs/general-use/openssl-configuration/)

### Kali-ToolsIn [2019.4](https://www.kali.org/blog/kali-linux-2019-4-release/) we moved our documentation over to our updated [/docs/](https://www.kali.org/docs/) page. It’s now finally the turn of our [Kali-Tools](https://www.kali.org/tools/) site!

We have refreshed every aspect of the previous site, giving a new, faster, layout, content, and system! The backend is now in a semi-automated state and more in the open, which like before, allows for anyone to help out and [contribute](https://www.kali.org/docs/community/contribute/).

Once these sites have settled down from all the changes and matured a bit, we will start to package these both up, allowing for offline reading.

https://www.kali.org/blog/kali-linux-2021-3-release/images/kali-tools.png

### Virtualization: improvements all over the placeThe Kali Live image received some love during this release cycle! We worked hard to make the experience smoother for those who run the Live image in [virtualized environments](https://www.kali.org/docs/virtualization/). Basic features like copy’n’paste and drag’n’drop between the host and the guest should now work out of the box. And this is really for everyone: VMware, VirtualBox, Hyper-V and QEMU+Spice. Did we forget anyone? Drop us a word on the [Kali bug tracker](https://bugs.kali.org/)!

On the same line: it’s now very easy to configure Kali for [Hyper-V Enhanced Session Mode](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/learn-more/use-local-resources-on-hyper-v-virtual-machine-with-vmconnect). Open kali-tweaks in a terminal, select Virtualization, and if Kali is running under Hyper-V, you’ll see a setting to turn on Hyper-V Enhanced Session Mode. It’s now as simple as hitting Enter!

If you use this feature, make sure to visit [kali.org/docs/virtualization/install-hyper-v-guest-enhanced-session-mode/](https://www.kali.org/docs/virtualization/install-hyper-v-guest-enhanced-session-mode/), as there are a few additional things to be aware of.

Many thanks to [Shane Bennett](https://gitlab.com/jetbennett), who spent a tremendous amount of time testing this feature, provided extremely detailed feedback all along, and even helped us with the documentation. Kudos Shane!

### New Tools in KaliIt wouldn’t be a Kali release if there weren’t any new tools added! A quick run down of what’s been added (to the network repositories):

- [Berate_ap](https://pkg.kali.org/pkg/berate-ap) - Orchestrating MANA rogue Wi-Fi Access Points
- [CALDERA](https://pkg.kali.org/pkg/caldera) - Scalable automated adversary emulation platform
- [EAPHammer](https://pkg.kali.org/pkg/eaphammer) - Targeted evil twin attacks against WPA2-Enterprise Wi-Fi networks
- [HostHunter](https://pkg.kali.org/pkg/hosthunter) - Recon tool for discovering hostnames using OSINT techniques
- [RouterKeygenPC](https://pkg.kali.org/pkg/routerkeygenpc) - Generate default WPA/WEP Wi-Fi keys
- [Subjack](https://pkg.kali.org/pkg/subjack) - Subdomain takeover
- [WPA_Sycophant](https://pkg.kali.org/pkg/wpa-sycophant) - Evil client portion of EAP relay attack

### Kali NetHunter Updateshttps://www.kali.org/blog/kali-linux-2021-3-release/images/NHWheader.png

#### Kali NetHunter WatchWe proudly introduce the world’s first Kali NetHunter smartwatch, the TicHunter Pro thanks to the outstanding work of our very own NetHunter developer [yesimxev](https://gitlab.com/yesimxev). It is still experimental, hence the features are limited to USB attacks, and some basic functions. The hardware also has limitations, as such a small battery won’t supply enough voltage for any OTG adapters, so huge antennas won’t stick out of your wrist! The future is very promising, bringing support for Nexmon and internal bluetooth usage.

The image is available on our [download page](https://www.kali.org/get-kali/).

Please note that those images contain a “nano Kali rootfs” due to technical reasons. The detailed installation guide can be found in our [Kali documentation](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-ticwatch-pro/). Feel free to join the adventure!

#### Kali NetHunter Installation via MagiskThanks to the amazing work of [@Mominul Islam](https://twitter.com/Mominul00650279), we can now bring Kali NetHunter to Android 11 devices without a fully working TWRP!

Each Kali NetHunter image can be flashed as a Magisk module. This work is still in its infancy and more work is needed to bring it up to par with the traditional installer through TWRP.

One of the missing parts is the kernel installation. We haven’t been able to install the kernel through Magisk yet. That has to be done via kernel installers like the “Franco Kernel Manager”. If you are keen to get NetHunter onto your Android 11 device, just give it a crack. If you are interested in helping out with getting the kernel part finished, please get in touch with us through our [GitLab issue tracker](https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-project/-/work_items). Any help is greatly appreciated!

#### Kali NetHunter installation step-by-step guide for our preferred device, the OnePlus 7Our preferred device for Kali NetHunter is the OnePlus 7 running Android 10 (stock ROM).

For a step-by-step installation guide and links to all the files required to restore your phone to the latest stock Android 10 ROM, install TWRP, Magisk and Kali NetHunter, head over to our [Kali documentation](https://www.kali.org/docs/nethunter/installing-nethunter-on-the-oneplus-7/) page.

### Kali ARM UpdatesWe have been busy doing various tweaks and tinkering on our [Kali ARM images](https://www.kali.org/docs/arm/), which covers:

- Our [Kali ARM build-scripts](https://gitlab.com/kalilinux/build-scripts/kali-arm) have been re-worked.Thanks to [@cyrus104](https://gitlab.com/cyrus104), we now have a [build-script to support the Gateworks Newport](https://gitlab.com/kalilinux/build-scripts/kali-arm/-/blob/main/gateworks-newport.sh) board, and he also added [documentation](https://www.kali.org/docs/arm/gateworks-newport/) for it.
- [@Re4son](https://bsky.app/profile/re4son.bsky.social) contributed a [build-script](https://gitlab.com/kalilinux/build-scripts/kali-arm/-/blob/main/rpi0w-pitail.sh) for the Raspberry Pi Zero W based [“Pi-Tail”](https://whitedome.com.au/re4son/pi-tail/) (Find [more information here](https://www.kali.org/docs/arm/raspberry-pi-zero-w-pi-tail/)).
- Additionally, the RaspberryPi Zero W based [“P4wnP1” build-script](https://gitlab.com/kalilinux/build-scripts/kali-arm/-/blob/main/rpi0w-nexmon-p4wnp1-aloa.sh) has undergone some major changes.

- All images should finally resize the file-system on the first boot.
- We now re-generate the default snakeoil cert, which fixes a couple of tools that were failing to run previously.
- Images default to iptables-legacy and ip6tables-legacy for iptables support.
- We now set a default locale of en_US.UTF-8 on all images, you can, of course, change this to your preferred locale.
- The Kali user on ARM images is now in all of the same groups as base images by default, and uses zsh for the default shell. You can change your default shell by using the kali-tweaks tool which also comes pre-installed.
- Raspberry Pi images can now use a wpa_supplicant.conf file on the /boot partition.
- Raspberry Pi images now come with kalipi-config, and kalipi-tft-config pre-installed.
- Pinebook Pro’s kernel has been updated to 5.14, and you now get messages on the LCD screen as it’s booting, instead of a blinking cursor until X starts.

### Desktop & Theme UpdatesThere are also some changes in the desktop space:

- Improved GTK3 theme for Xfce’s notifications and logout-dialog
- Redesigned GTK2 theme for a better fit of older programs
- Improved Kali-Dark and Kali-Light syntax-highlighting themes for GNOME and Xfce

In addition to these changes, one of Kali’s preferred desktops, KDE plasma, has received a version bump, now including version [5.21](https://kde.org/announcements/plasma/5/5.21.0/). This update brings an updated look, with a new application launcher and theme improvements. Here’s a preview of how it looks with Kali’s customization:

https://www.kali.org/blog/kali-linux-2021-3-release/images/KDE_5.21.png

### Kali-Docs UpdatesOur documentation site, as well as the pages mentioned already in this blog post, the following other pages have received major changes:

- [Download Kali Linux Images Securely](https://www.kali.org/docs/introduction/download-images-securely/)
- [Kali Linux & WSL & Mesa](https://www.kali.org/docs/wsl/mesa-21/)
- [Kali Linux IRC Channel](https://www.kali.org/docs/community/kali-linux-irc-channel/)
- [Contributing runtime tests](https://www.kali.org/docs/development/contributing-runtime-tests/)

### GitLab Commit 2021We participated in GitLab’s virtual conference this year and [g0tmi1k](https://gitlab.com/g0tmi1k) gave a talk on the [Dynamic between Kali Linux and OffSec](https://www.youtube.com/watch?v=M7ixTe-6Oyw). Give it a watch!

### Ampere & ARMFollowing our [announcement](https://www.kali.org/blog/ampere/) of our [partnerships](https://www.kali.org/partnerships/) with Ampere, we have now fully moved our ARM package building machines over to their hardware, and loving the speed increase! Thank you again to Ampere for the assistance! If you need some ARM servers give them a look! If they are nice enough to help us out this way, we are sure they will treat you good as well.

### Upcoming ChangesLooking forward, we are going to be announcing the following changes:

- Kali-Menu refresh - We know you may not use it, but for the people who do, we are planning on making some major alterations in its structure. This will hopefully be live for testing in 2021.4, and then made default in a later release based on user response. You will be able to change the menu layout by using kali-tweaks. If you want to provide input on this change, get engaged with us and make your voice heard!
- Load Balancer (http.kali.org & cdimage.kali.org) - This handles apt packages as well as OS images. We will be switching from MirrorBrain to MirrorBits. We will be soon in touch with all the community mirror maintainers to give them notice of our infrastructure changes. If you would like to become a mirror, please see [our guide](https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/).

### Download Kali Linux 2021.3Fresh Images:
So what are you waiting for? Start [downloading](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for the those who are not, we do also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use as well. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead. This way you’ll have fewer updates to do. Just know that these are automated builds that we do not QA like we do our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade

┌──(kali㉿kali)-[~]
└─$ cp -rbi /etc/skel/. ~

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2021.3. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2021.3"
VERSION_ID="2021.3"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP Debian 5.10.46-4kali1 (2021-08-09)

┌──(kali㉿kali)-[~]
└─$ uname -r
5.10.0-kali9-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We’ll never be able to fix what we do not know is broken! And [Twitter](https://twitter.com/kalilinux) is not a Bug Tracker!

## 2021.2 – 2021-06-01

**Kali Linux 2021.2 Release (Kaboxer, Kali-Tweaks, Bleeding-Edge & Privileged Ports)**

Table of Contents
- [Introducing Kaboxer v1.0 (Again)](#introducing-kaboxer-v10-_again_)
- [Releasing Kali-Tweaks v1.0](#releasing-kali-tweaks-v10)
- [Refreshed Bleeding-Edge Branch](#refreshed-bleeding-edge-branch)
- [Disabled Privileged Ports](#disabled-privileged-ports)
- [New Tools in Kali](#new-tools-in-kali)
- [Theme Enhancement](#theme-enhancement)[Command Line](#command-line)
- [Xfc4](#xfc4)[Desktop Wallpaper & Login Background](#desktop-wallpaper--login-background)

- [Raspberry Pi Recharged](#raspberry-pi-recharged)
- [Kali NetHunter Updates](#kali-nethunter-updates)
- [More Docker support/Parallels support/Bug fixes](#more-docker-supportparallels-supportbug-fixes)
- [Download Kali Linux 2021.2](#download-kali-linux-20212)

Say hello to Kali Linux 2021.2! This release welcomes a mixture of new items as well as enhancements of existing features, and is ready to be [downloaded (from our updated page)](https://www.kali.org/get-kali/) or [upgraded if you have an existing Kali Linux installation](https://www.kali.org/docs/general-use/updating-kali/).

A quick summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2021.1 release from February 2021](https://www.kali.org/blog/kali-linux-2021-1-release/) is:

- [Releasing Kaboxer v1.0](#introducing-kaboxer-v10-_again_) - Introducing Kali Applications Boxer v1.0! Applications in containers
- [Releasing Kali-Tweaks v1.0](#releasing-kali-tweaks-v10) - Our way to make it easier to configure Kali Linux to your taste
- [Refreshed Bleeding-Edge branch](#refreshed-bleeding-edge-branch) - We did a complete make over for our backend that produces packages for the latest updates
- [Disabled privileged ports](#disabled-privileged-ports) - Opening a listener on ports 1024/TCP-UDP and below no longer requires super-user access
- [New tools added](#new-tools-in-kali) - Ghidra & Visual Studio Code. Along with CloudBrute, Dirsearch, Feroxbuster, pacu, peirates, & Quark-Engine
- [Theme enhancements](#theme-enhancement) - We added a way to quickly swap between double & one-line terminal prompt and made Xfce4 Quick launch + file manager tweaks
- [Desktop wallpaper & login background updates](#desktop-wallpaper--login-background) - Default images have changed with more to choose from
- [Raspberry Pi images recharged](#raspberry-pi-recharged) - RPi 400 fully supported, built-in bluetooth working, & first-run wait time dramatically reduced
- [Kali NetHunter support for Android 11](#kali-nethunter-updates) - Android 11 support and various other improvements for our NetHunter platform
- [More Docker support](#more-docker-supportparallels-supportbug-fixes) - Now supporting ARM64 & ARM v7 (along with previous AMD64)
- [Parallels support](#more-docker-supportparallels-supportbug-fixes) - Kali is fully supported for Apple M1 users who have Parallels
- [Various bug fixes](#more-docker-supportparallels-supportbug-fixes) - Pkexec patched, Wireshark permissions, command-not-found issues, & more accessibility features are all resolved

### Introducing Kaboxer v1.0 (Again)In case you missed it, we have previously covered [Kaboxer](https://pkg.kali.org/pkg/kaboxer) in it’s own [dedicated blog post](https://www.kali.org/blog/introducing-kaboxer/), which goes into a lot more detail of why we love it so! For developers, this is a great new tool in the arsenal. Users will, hopefully, not realise that they are using it, only noticing that previously problematic tools now work correctly!

Without repeating what has already been posted, this technology allows us to correctly package up programs that were previously difficult, with items such as complex dependencies or legacy programs & libraries (such as [Python 2](https://www.kali.org/docs/general-use/using-eol-python-versions/) or dated SSL/TLS).

With Kaboxer’s launch, we have released 3 packages using it:

- [Covenant](https://pkg.kali.org/pkg/covenant-kbx) - Daemon using server/client network model
- [Firefox (Developer Edition)](https://pkg.kali.org/pkg/firefox-developer-edition-kbx) - Big GUI desktop application
- [Zenmap](https://pkg.kali.org/pkg/zenmap-kbx) - Legacy libraries ([Python 2](https://www.kali.org/docs/general-use/using-eol-python-versions/)) application

If you want to read more, please see either our [blog post](https://www.kali.org/blog/introducing-kaboxer/) covering it, or our [documentation](https://www.kali.org/docs/development/packaging-apps-with-kaboxer/) around it.

Kaboxer is still in its infancy, so please be nice & patient with it.

### Releasing Kali-Tweaks v1.0Announcing [Kali-Tweaks](https://pkg.kali.org/pkg/kali-tweaks)! This is our little helping hand for Kali users, with the idea to help customize Kali to your own personal taste quickly, simply, and the correct way. This should help you to stop doing repetitive tasks.

https://www.kali.org/blog/kali-linux-2021-2-release/images/kali-tweaks.png

Currently Kali-Tweaks will help out with:

- Metapackages - Installing/removing [groups of tools](https://www.kali.org/docs/general-use/metapackages/), which may not have been available while installing Kali if you did not use the installer image
- Network Repositories - Enabling/disabling “bleeding-edge” & “experimental” [branches](https://www.kali.org/docs/general-use/kali-branches/)
- Shell & Prompt - Switch between [two or one line prompt](https://www.kali.org/blog/kali-linux-2020-4-release/), enable/disable the extra line before the prompt, or configure [Bash or ZSH](https://www.kali.org/blog/kali-linux-2020-3-release/) as the default shell
- Virtualization - Using Kali as a [guest VM](https://www.kali.org/docs/virtualization/)? Do a few actions to make the experience easier!

Our philosophy is to always understand what you are running, before you run it. That way, it reduces the chances of any undesirable nasty surprises. Which is why we will always encourage anyone to do actions manually before automating it, so you get to understand what is happening under the hood. On the flip side, we also understand there is so much to remember. Then when you sprinkle in people’s bad habits, which often have long term implications and end up breaking Kali, there is room for improvement. So, we started developing Kali-Tweaks. Where possible, Kali-Tweaks will also display what commands are being executed to help educate users.

We do want to mention a few things:

- kali-tweaks has been marked as “recommended” rather than “required”. As a result, if you are upgrading Kali, it may not be included. On the other hand, you can remove kali-tweaks without removing anything else
- On the subject of upgrading; depending on how old your Kali installation is, you may need to reset your shell resource (e.g. .bashrc & .zshrc) before you can use the “configure prompt” section. This is because it will not have the necessary variables. Should you want to, make sure to backup, reset, and restore
- The last thing to point out, when changing the default login shell; please log out and in again (either graphically or remote console) for it to have an effect

It is still early days with Kali-Tweaks, and we already have ideas of what to expand into, but we welcome [any suggestions from you](https://gitlab.com/kalilinux/packages/kali-tweaks/-/work_items)!

Kali-Tweaks is still in its infancy, so please be nice & patient with it.

### Refreshed Bleeding-Edge BranchKali’s Bleeding-Edge branch has been around since [March 2013](https://www.kali.org/blog/bleeding-edge-kali-repositories/), but we have recently completely restructured the backend.

For those not too familiar with Bleeding-Edge branch, here is a breakdown:

- Kali by default opts to be stable where possible when packaging. This means some tools may appear to be “out-dated”
- We do this by looking to see when the tool author(s) signals “everything up to to this point is good”, by doing a “point release” (e.g. 1.0 or 2.1)
- Developers often use source-code version control, allowing them to track any changes
- How programmers use source-code version control depends on their work flow, experience, and team sizeDevelopers can use a “tag” feature found in most source-code version control to signal when there is a new version (this is what Kali prefers)
- However, some people may say if it makes it to “master” or “main” branch, then it is “production ready”

- There are times where it has been “a while” (months or even years) since doing a tag for a stable release (aka point release), and people get frustrated that there are no updates (e.g. [hashcat](https://pkg.kali.org/pkg/hashcat) or [impacket](https://pkg.kali.org/pkg/impacket)).In other cases, you want the latest code which may include an exploit 0day (e.g. [Metasploit-framework](https://pkg.kali.org/pkg/metasploit-framework), [Empire](https://pkg.kali.org/pkg/powershell-empire), or [Exploit-DB](https://pkg.kali.org/pkg/exploitdb)) so waiting for a tag release may not be an option

You may then end up skipping the Kali package and compiling your favorite tool’s source-code. This might then conflict with Kali’s packaging, and it is your responsibility to maintain the program. This is where bleeding-edge branch comes in.

Since [moving over to GitLab](https://www.kali.org/blog/kali-linux-roadmap-2019-2020/), we have been able to create [Kali-Bot](https://www.kali.org/docs/development/leveraging-the-kali-bot/) to help with heavy lifting and automation

- Automatically package tag’d releases to kali-experimental branch
- Automatically package the last commit to kali-bleeding-edge branch

This is a fully automated procedure, as a result, the testing that goes into our packaging is automated as well (unlike anything that is in kali-rolling branch which has manual testing involved). If there has not been a unit test created, its not going to be tested for. This means there is a chance packages will be broken, and more trust goes into the tool author having correctly developed the tool.

If you want to give it a try, have a look at our [kali-bleeding-edge documentation](https://www.kali.org/docs/general-use/kali-bleeding-edge/) to learn how to enable the repository and how to tell apt to select a package from this repository. Once the repository has been enabled, it looks like this:

kali@kali:~$ dpkg -l \
  | grep ffuf
ii  ffuf             1.3.1-0kali1                        amd64        Fast web fuzzer written in Go (program)
kali@kali:~$
kali@kali:~$ sudo apt install -y ffuf/kali-bleeding-edge
...
kali@kali:~$
kali@kali:~$ dpkg -l \
  | grep ffuf
ii  ffuf             1.3.1+git20210505.1.f032167-0kali1~jan+nus1 amd64        Fast web fuzzer written in Go (program)
kali@kali:~$

Not every tool has made it to the new system yet as there are still many limitations to overcome, but to see what is supported and also how many:

kali@kali:~$ curl -s -L 'http://http.kali.org/kali/dists/kali-bleeding-edge/main/binary-amd64/Packages' \
  | awk -F ': ' '/^Package: /{print $2}'
...
kali@kali:~$
kali@kali:~$ curl -s -L 'http://http.kali.org/kali/dists/kali-bleeding-edge/main/binary-amd64/Packages' \
  | awk -F ': ' '/^Package: /{print $2}' \
  | wc -l
78
kali@kali:~$
kali@kali:~$ curl -s -L 'http://http.kali.org/kali/dists/kali-experimental/main/binary-amd64/Packages' \
  | awk -F ': ' '/^Package: /{print $2}' \
  | wc -l
192
kali@kali:~$
kali@kali:~$ curl -s -L 'http://http.kali.org/kali/dists/kali-rolling/main/binary-amd64/Packages' \
  | awk -F ': ' '/^Package: /{print $2}' \
  | wc -l
59518
kali@kali:~$

The numbers will only grow bigger and better as time goes on, with less bugs in the code and more unit tests in place!

If you are a tool author and want to get your software on the list, please [chat to us](https://forums.kali.org/), and we can show how to [enable webhooks](https://www.kali.org/docs/development/leveraging-the-kali-bot/)!

### Disabled Privileged PortsWe have patched our kernel to remove the restriction of requiring privilege permission in order to use TCP & UDP ports under 1024 (meaning 0/TCP-UDP <= 1023/TCP-UDP). This was done because:

- We see Kali as a desktop OS, rather than a server
- This “well-known” privileged port range is reserved for server services (e.g. 80/TCP HTTP, 443/TCP HTTPS)
- With the switch from Kali’s [root to non-root user by default](https://www.kali.org/blog/kali-default-non-root-user/), rather than doing a port forward from outside the privilege ports to a restricted port, people were just running the program with super-user permissions insteadWe get it. It’s quicker to run: $ sudo <program>,
- Rather than remembering something like: $ sudo iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8888
- It also can get complex and confusing with a lot of redirects setup in place
- Alternatively people were using authbind to allow certain users to use certain ports

- This defeats the point of switching to non-root user!Let’s reduce any possible attack surface!

Now, this change won’t appear in all instances as some flavors of Kali operate without our kernel. This depends on which platform you use (such as Cloud instances, Docker or WSL). If you are on a platform that does not use our customized Kernel, this change will not be applied. For example, the top one uses Kali’s kernel on a bare metal install, and below uses Kali in a docker container, so its using the host’s kernel:

kali@kali:~$ uname -r
5.10.0-kali7-amd64
kali@kali:~$

...vs...

$ docker run --rm --interactive --tty kalilinux/kali-rolling:latest uname -r
5.10.25-linuxkit
$

### New Tools in KaliIt would not be a Kali release if there were not any new tools added! A quick run down of what’s been added (to Kali’s archive and network repositories):

- [CloudBrute](https://pkg.kali.org/pkg/cloudbrute) - Find a company infrastructure, files, and apps on the top cloud providers
- [Dirsearch](https://pkg.kali.org/pkg/dirsearch) - Brute force directories and files in web servers
- [Feroxbuster](https://pkg.kali.org/pkg/feroxbuster) - Simple, fast, recursive content discovery
- [Ghidra](https://pkg.kali.org/pkg/ghidra) - Reverse engineering framework
- [Pacu](https://pkg.kali.org/pkg/pacu) - AWS exploitation framework
- [Peirates](https://pkg.kali.org/pkg/peirates) - Kubernetes penetration
- [Quark-Engine](https://pkg.kali.org/pkg/quark-engine) - Android malware scoring system
- [VSCode](https://pkg.kali.org/pkg/code-oss) a.k.a. Visual Studio Code Open Source (“Code-OSS”) - Code editor

Ghidra and VSCode have been included into the kali-linux-large [metapackage](https://www.kali.org/docs/general-use/metapackages/), so they are included on the installer image for people doing a fresh install. Otherwise you will need to upgrade Kali (if you already have the kali-linux-large install) or manually install them (if you want them!):

kali@kali:~$ sudo apt update && sudo apt install -y ghidra code-oss

A few notes about code-oss (aka VSCode):

- We are compiling this from [source](https://gitlab.com/kalilinux/packages/code-oss), rather than using the pre-built binariesThe upside to this is that [telemetry data is disabled by default](https://code.visualstudio.com/docs/getstarted/telemetry)
- The downside is that some aspects of the marketplace may not work. If you find these limitations a problem, you may wish to uninstall the Kali package and switch to the VSCode pre-built binaries

- You also may question why it was named code-oss, rather than codeCode-OSS is what the [source-code](https://github.com/microsoft/vscode/blob/8f11975c47c9d97b3248e14caf9f7bc4c372d84f/src/vs/platform/product/common/product.ts#L60) calls [itself](https://github.com/microsoft/vscode/blob/8f11975c47c9d97b3248e14caf9f7bc4c372d84f/product.json#L4), which is used as the base before the configurations are applied for the pre-compiled binaries that gets distributed as “code”
- As we are using the source-code, we used the variables defined by it
- The two different names help to distinguish the differences between them (also prevents any clashes and conflicts!)
- We also included various aliases in our package to help bridge between the two different versions. Meaning, calling vscode and code will use our package, code-oss, with a friendly notice (when installed)

- If you already have the pre-compiled version installed, upgrading Kali will not replace itHowever, when manually installing code-oss, it will then replace it!

### Theme Enhancement#### Command LineIf you are using ZSH, with the latest Kali profile applied, you can toggle between the two-line prompt and one-line prompt by pressing: CTRL + p (at the same time).
This will only have an effect for the current session. If you would like to set it permanently, see kali-tweaks.

Your browser does not support the video tag.#### Xfc4We have switched up the quick launch tray in the top left, by:

- Dropping the screen recorder button (as a result package can also be removed, kazam)
- Adding a text editor shortcut (this uses mousepad as it is a quick and light)_If you are looking for something that is more substantial, try code-oss

- Adding in a web browser icon, which starts the default browser (often FireFox)
- Adding a drop-down menu to select the user for default terminal (terminal or root terminal & Kali’s default is QTerminal)

https://www.kali.org/blog/kali-linux-2021-2-release/images/cli-tray.png

To give you an idea of how the toggling between the terminal user works:

Your browser does not support the video tag.Inside of Thunar (Xfce’s default file manager), if you right-click in the main window, you should have a new option, Open as Root:

https://www.kali.org/blog/kali-linux-2021-2-release/images/cli-thunar.png

With these theme changes, you may not get them if you upgrade Kali. This is because the theme settings are copied to your home folder when your user is first created. When you upgrade Kali, it is upgrading the operating system, so upgrading does not alter personal files (just system files). As a result, in order to get these theme tweaks, you need to either:

- Do a fresh Kali install
- Create a new user and switch to that
- Delete your Xfce profile for the current user and force reboot

kali@kali:~$ mv ~/.config/xfce4{,-$(date +%Y.%m.%d-%H.%M.%S)}
kali@kali:~$ mv ~/.config/qterminal.org{,-$(date +%Y.%m.%d-%H.%M.%S)}
kali@kali:~$ mv ~/.config/qt5ct{,-$(date +%Y.%m.%d-%H.%M.%S)}
kali@kali:~$ mv ~/.config/Thunar{,-$(date +%Y.%m.%d-%H.%M.%S)}
kali@kali:~$
kali@kali:~$ cp -rbi /etc/skel/. ~
kali@kali:~$
kali@kali:~$ xfce4-session-logout --reboot --fast

##### Desktop Wallpaper & Login BackgroundPeople who have upgraded, you may have spotted that there is a new default login wallpaper and desktop background, but there are extras as well in this release:

https://www.kali.org/blog/kali-linux-2021-2-release/images/wallpapers.png

Whilst on the subject of wallpapers, if you have not noticed, previously we had been operating on an refresh cycle about every 6 months, where we would change the default login and desktop as well as included other art work if they were not to your taste. Going forwards, we are aiming to change the defaults at every 20xx.1 release (meaning it happens right at the start of every year). So it will still change again in 6 months, but this will be the last time! We will still aim to add extra wallpapers every 6 months, however, only change the defaults yearly.

Finally, we have updated kali-community-wallpapers & kali-wallpapers-legacy packages as well!

### Raspberry Pi RechargedTwo new packages:

- [kalipi-config](http://pkg.kali.org/pkg/kalipi-config) - raspi-config on steroids to assist in the initial setup of Kali Linux on a Raspberry Pi
- [kalipi-tft-config](http://pkg.kali.org/pkg/kalipi-tft-config)- assist in the initial setup of TFT displays on a Raspberry Pi

And other improvements:

- Got built-in Bluetooth working on Raspberry Pi 4 & Raspberry Pi 400 (meaning all Raspberry Pi’s built-in bluetooth work!)This is due to bluez, bluez-firmware, and pi-bluetooth packages forked and patched

- Raspberry Pi kernel updated to 5.4.83
- mt76 devices now work on Raspberry Pi 2 and 3 if you pass the option disable_usb_sg=1 when loading the mt76_usb module
- 1500% performance improvement
- First boot from 20 minutes to 15 seconds
- Console scrolling working

### Kali NetHunter UpdatesPlenty of improvements under the hood, including:

- Improved compatibility with dynamic partitions
- Improvements to persistence of Magisk root
- Improvements to Bluetooth and settings menus
- Inclusion of rtl88xxau patches for older kernels in the kernel builder

And the highlight:

Android 11 support for:

- Nokia 6.1
- OnePlus Nord
- OnePlus One
- Samsung Galaxy S20 FE 5G
- Xiaomi Mi A3
- Xiaomi Poco F1

The Kali NetHunter repository now contains [179 kernels](https://nethunter.kali.org/kernels.html) for [72 devices](https://nethunter.kali.org/device-kernels.html) and 32 pre-built images are available on our [download page](https://www.kali.org/kali-nethunter/)

Huge thanks to [kim0coder](https://gitlab.com/kimoc0der), [yesimxev](https://gitlab.com/yesimxev), [Svirusx](https://gitlab.com/Svirusx), [Martinvlba](https://gitlab.com/Martinvlba), [CaliBerrr](https://gitlab.com/CaliBerrr), [maade69](https://gitlab.com/maade69) and the entire Kali NetHunter community for making this release happen. You absolutely rock!

### More Docker support/Parallels support/Bug fixesThere are even more improvements to Kali, that are outside of the above text. Below are other note-worthy items:

- Our [Kali-Docker images](https://hub.docker.com/r/kalilinux/kali-rolling/tags) are now available for arm64 and armhf as well as amd64
- We have patched pkexec, so now Qt applications which have been ran as root will maintain the dark theme and the HiDPI setting
- On a fresh Kali install, wireshark can now be run by unprivileged users
- A couple of bugs were fixed in [command-not-found](https://www.kali.org/blog/kali-linux-2021-1-release/), which is the terminal helper that helps you installing missing programs
- Accessibility features were not installed by default (this was a mistake on our side that is now fixed)
- Fixed a terminal font issue with special characters
- Apple M1 users, [Parallels](https://kb.parallels.com/en/124805) is no longer in “Technical Preview” and as part of the release, they’ve fixed Kali image detection.
- Win-KeX v2.10 has been released which now supports multiscreen
- Kali’s logo is now included in the [nerd-fonts](https://www.nerdfonts.com/) project, so, with their next release you’ll be able to customize your terminal with the dragon. If you want to try it now, we’ve created a [patched Fira-Code font](fonts/Fira-Code-Regular-Nerd-Font-Complete.ttf) with these new changes (the code for the logo is \uF32B)

https://www.kali.org/blog/kali-linux-2021-2-release/images/nerd-fonts-kali.png

### Download Kali Linux 2021.2Fresh Images:
So what are you waiting for? Start [grabbing Kali](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for the ones who are not, we do also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use as well. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.

This way you’ll have fewer updates to do.

Just know that these are automated builds that we do not QA like we do our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade

┌──(kali㉿kali)-[~]
└─$ for x in xfce4 qterminal.org qt5ct Thunar; do mv ~/.config/$x{,-$(date +%Y.%m.%d-%H.%M.%S)}; done

┌──(kali㉿kali)-[~]
└─$ cp -rbi /etc/skel/. ~

┌──(kali㉿kali)-[~]
└─$ sudo reboot -f

You should now be on Kali Linux 2021.2. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2021.2"
VERSION_ID="2021.2"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP Debian 5.10.28-1kali1 (2021-04-12)

┌──(kali㉿kali)-[~]
└─$ uname -r
5.10.0-kali7-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We’ll never be able to fix what we do not know is broken! And [Twitter](https://twitter.com/kalilinux) is not a Bug Tracker!

## 2021.1 – 2021-02-24

**Kali Linux 2021.1 Release (Command-Not-Found)**

Table of Contents
- [Xfce & KDE Updates](#xfce--kde-updates)
- [Terminals Tweaks](#terminals-tweaks)
- [Finding Commands That Didn’t Want To Be Found](#finding-commands-that-didnt-want-to-be-found)
- [Partnerships with Tools Authors](#partnerships-with-tools-authors)
- [New Tools in Kali](#new-tools-in-kali)
- [Kali’s Website](#kalis-website)
- [Wallpapers](#wallpapers)
- [Kali NetHunter Updates](#kali-nethunter-updates)
- [Kali ARM Updates](#kali-arm-updates)
- [Download Kali Linux 2021.1](#download-kali-linux-20211)

Today we’re pushing out the first Kali Linux [release](https://www.kali.org/releases/) of the year with Kali Linux 2021.1. This edition brings enhancements of existing features, and is ready to be [downloaded](https://www.kali.org/get-kali/) or [upgraded if you have an existing Kali Linux installation](https://www.kali.org/docs/general-use/updating-kali/).

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2020.4 release from November 2020](https://www.kali.org/blog/kali-linux-2020-4-release/) is:

- [Xfce 4.16](#xfce--kde-updates) - Our preferred and current default desktop environment has been updated and tweaked
- [KDE 5.20](#xfce--kde-updates) - Plasma also received a version bump
- [Terminals](#terminals-tweaks) - mate-terminal, terminator and tilix all had various work carried out on them
- [Command Not Found](#finding-commands-that-didnt-want-to-be-found) - A helping hand to say if a program needs to be installed
- [Partnership with more tool authors](#partnerships-with-tools-authors) - BC Security & Joohoi have been producing great tools and we want to support them
- [New tools & updates](#new-tools-in-kali) - Multiple new tools have been added to Kali and are ready for you
- [Kali NetHunter](#kali-nethunter-updates) - New BusyBox & Rucky version, and boot-animation
- [Kali ARM](#kali-arm-updates) - Preliminary support for Parallels on Apple Silicon (Apple M1) & Raspberry Pi 400 (WiFi Support)

The Kali project itself also has a couple different changes:

- [New Kali website](#kalis-website) - You may have noticed a few things looking different
- [Kali newsletter](https://www.kali.org/newsletter/) - Rather than you coming to us for updates, we can push them to your inbox

### Xfce & KDE UpdatesHow you choose to interact with Kali is completely up to you. You may want to access Kali locally or remotely, either graphically or on the command line. Even when you pick a method, there are still options you can choose from, such as a desktop environment.

By default, Kali uses [Xfce](https://www.kali.org/blog/kali-linux-2019-4-release/), but during the setup process, allows for GNOME, KDE, or no GUI to be selected. After the setup is complete, [you can install even more](https://www.kali.org/docs/general-use/switching-desktop-environments/). We have pre-configurations for Enlightenment, i3, LXDE, and MATE as well.

So when a desktop environment gets an update, they often enhance day-to-day activities for their users. It’s best to hear it straight from the authors, for a tour of what’s changed:

- [Xfce 4.16](https://www.xfce.org/about/tour416)
- [KDE 5.20](https://kde.org/announcements/plasma/5/5.20.0/)

Below is our tweaked GTK3 theme, on Xfce:

https://www.kali.org/blog/kali-linux-2021-1-release/images/xfce-414-new.png

### Terminals TweaksWhen we use Kali, we spend a significant amount of time using the command line. A lot of the time, we do it using a local terminal (rather than in a console or remote SSH). With the options of desktop environments, there are also choices when it comes to the terminals (same with what shell to use). We have been working away on various terminals (xfce4-terminal, tmux, tilix, konsole, qterminal, and mate-terminal) to “Kali-fy” them:

https://www.kali.org/blog/kali-linux-2021-1-release/images/kali-terminals.png

### Finding Commands That Didn’t Want To Be Found[A while ago](https://www.kali.org/blog/major-metapackage-makeover/), we changed the default set of tools installed in Kali. Most users know they can either install a one-off package, or revert back to the old set of defaults (apt install kali-linux-large). But to help communicate our changes (as well as any new tools), we have now included command-not-found by default. This is an “optional” package, which can be removed without removing all of kali-linux-default.

Without command-not-found installed:

┌──(kali㉿kali)-[~]
└─$ gitleaks
gitleaks: command not found

If you are wondering “How does this help me?”, or has the above ever happened to you, we like to think people’s next stage would be to do apt-cache search gitleaks and see it in the network repositories. But we can do better. Now with command-not-found:

┌──(kali㉿kali)-[~]
└─$ gitleaks
Command 'gitleaks' not found, but can be installed with:
sudo apt install gitleaks

┌──(kali㉿kali)-[~]
└─$ gitleakss
Command 'gitleakss' not found, did you mean:
  command 'gitleaks' from deb gitleaks
Try: sudo apt install <deb name>

┌──(kali㉿kali)-[~]
└─$ badcmd
badcmd: command not found

As you can see from the above example:

- gitleaks - If the command you entered is the name of an executable available in Kali, it will say the package that you need to install (if its not already!)
- gitleakss - If you are “fat fingered” and make a typo, it may make a suggestion
- badcmd - If you typed in an invalid command that doesn’t exist in Kali, it will give the original message of “command not found”.

So, how can I get this magic? Good question! If you’re:

- Doing a fresh install of Kali Linux 2021.1 or later, it will “just happen” during the setup.
- Updating Kali and you are using a Bash shell, then it will “just happen” too.
- Updating Kali and you are using a Zsh shell, you will need to add the following lines to your ~/.zshrc:

# enable command-not-found if installed
if [ -f /etc/zsh_command_not_found ]; then
    . /etc/zsh_command_not_found
fi

But it doesn’t have to end here. By adding COMMAND_NOT_FOUND_INSTALL_PROMPT=1 to your shell’s environment (e.g. ~/.bashrc or ~/.zshrc), command-not-found will take it one step further, and also prompt you if you want to install the missing package. This change is something we will be putting in in a future release.

Hope it helps!

### Partnerships with Tools AuthorsCarrying on from our [previous partnership](https://www.kali.org/blog/kali-linux-2020-4-release/) with byt3bl33d3r, we have expanded to supporting:

- [BC Security](https://www.kali.org/blog/empire-starkiller/) - Giving Kali exclusive early access to “[Empire](https://pkg.kali.org/pkg/powershell-empire)” (powershell-empire) & “[StarKiller](https://pkg.kali.org/pkg/starkiller)”
- [@Joohoi](https://twitter.com/joohoi) - The creator of “Fuzz Faster U Fool ([ffuf](https://pkg.kali.org/pkg/ffuf))”

The announcement with Joohoi is new for Kali 2021.1. Like the previous sponsorships, you can either [sponsor him directly](https://github.com/sponsors/joohoi) to get the latest access to ffuf, [use Kali Linux](https://www.kali.org/), or wait 30 days until the [source code](https://github.com/ffuf/ffuf) becomes public. However, he has [also announced](https://github.com/ffuf/ffuf#access-the-sponsorware-through-code-contributions) anyone who makes a significant contribution, which gets accepted into the project, also gets access!

### New Tools in KaliIt wouldn’t be a Kali release if there weren’t any new tools added! A quick run down of what’s been added (to the network repositories):

- [Airgeddon](https://pkg.kali.org/pkg/airgeddon) - Audit wireless networks
- [AltDNS](https://pkg.kali.org/pkg/altdns) - Generates permutations, alterations and mutations of subdomains and then resolves them
- [Arjun](https://pkg.kali.org/pkg/arjun) - HTTP parameter discovery suite
- [Chisel](https://pkg.kali.org/pkg/chisel) - A fast TCP/UDP tunnel over HTTP
- [DNSGen](https://pkg.kali.org/pkg/dnsgen) - Generates combination of domain names from the provided input
- [DumpsterDiver](https://pkg.kali.org/pkg/dumpsterdiver) - Search secrets in various filetypes
- [GetAllUrls](https://pkg.kali.org/pkg/getallurls) - Fetch known URLs from AlienVault’s Open Threat Exchange, the Wayback Machine, and Common Crawl
- [GitLeaks](https://pkg.kali.org/pkg/gitleaks) - Searches Git repo’s history for secrets and keys
- [HTTProbe](https://pkg.kali.org/pkg/httprobe) - Take a list of domains and probe for working HTTP and HTTPS servers
- [MassDNS](https://pkg.kali.org/pkg/massdns) - A high-performance DNS stub resolver for bulk lookups and reconnaissance
- [PSKracker](https://pkg.kali.org/pkg/pskracker) - WPA/WPS toolkit for generating default keys/pins
- [WordlistRaider](https://pkg.kali.org/pkg/wordlistraider) - Preparing existing wordlists

Happy hacking!

### Kali’s WebsiteUntil recently, the only way you could be reading this would have been from our [RSS feed](https://www.kali.org/rss.xml) or directly from our [blog](https://www.kali.org/blog/) (as we only recently made the [announcement](https://www.kali.org/blog/kali-linux-newsletter-keeping-in-touch/) of the [Kali Newletter](https://www.kali.org/newsletter/)). You may of noticed already, and [we said](https://www.kali.org/blog/2019-2020-review-onwards-with-2021/) that it was coming, and it finally has - [kali.org](https://www.kali.org/) has had a face-lift!

We have (finally) moved away from WordPress to Hugo. Similarly to Kali, the website will also be a rolling distribution. The recent change is mostly cosmetic and content (both were long overdue), and we have made plans for new features to be added.

Another upside of the switch is that we can take more advantage of what GitLab has to offer. We recently had [an interview with GitLab](https://about.gitlab.com/blog/2021/02/18/kali-linux-movingtogitlab/) about the switch.

On the subject of interviews, we also had a word with [Mr Robot’s ARG Society](https://www.kali.org/blog/mr-robot-arg-society/) if you missed that.

### WallpapersJust a quick little thing, we have tweaked our wallpaper packages:

- kali-wallpapers-2020.4 - Kali’s wallpapers from 2020.4 and onwards (for the time being)
- kali-wallpapers-2019.4 - Kali’s wallpapers between 2019.4 and 2020.3.
- kali-wallpapers-legacy - BackTrack & Kali nostalgic backgrounds
- kali-wallpapers-all - Every wallpaper
- kali-community-wallpapers - created and submitted by the community ([submit yours](https://gitlab.com/kalilinux/packages/kali-community-wallpapers/-/merge_requests) today!)

With the alterations to the packages, we have taken the time to improve support for Xfce when using them.

Enjoy!

### Kali NetHunter UpdatesBusyBox, one of the core engines of Kali NetHunter, has received a well deserved upgrade to version “1.32.0-nethunter”. BusyBox is used internally to ensure that NetHunter tools and commands are executed consistently across the vast number of different Android versions and vendor modifications. This change, whilst big, should go unnoticed by users and will help developers to port their code to NetHunter with no hassles at all. [yesimxev](https://gitlab.com/yesimxev) has added a handy section to the settings menu, which allows developers to select different BusyBox versions for testing:

https://www.kali.org/blog/kali-linux-2021-1-release/images/BusyBoxSelector.jpg

Speaking of developers: If you have any cool ideas you’d like to see included in Kali NetHunter or if you would like to contribute to this amazing project, please reach out to us in our [forums](https://forums.kali.org/) or on [GitLab](https://gitlab.com/kalilinux/nethunter). We would love to hear from you!

Tools have been updated to the latest versions, notably Rucky - the “modern looking USB Rubber Ducky Editor and Attack Launcher”, which has been completely re-written by its author [@mayankmetha](https://twitter.com/mayank_metha) and [released in the Kali NetHunter App Store as version 2.1](https://staging.nethunter.com/en/packages/com.mayank.rucky/).

We’ve also been busy working on the visual aspects of Kali NetHunter, with [@s133py](https://twitter.com/thiviyann) adding a stunning new boot-animation to the growing selection:

https://www.kali.org/blog/kali-linux-2021-1-release/images/res_raw_boot_glitch.gif

If you have a cool boot-animation you’d like to share, please submit a merge request to our [Kali NetHunter Boot Animation repository](https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-bootanimation).

### Kali ARM UpdatesAs you may have heard, Apple have released new Macs with their own processors, known as Apple Silicon (Apple M1). So far, only Parallels have released something publicly that people can use for virtualization. To that end, we have generated both an installer & live ISOs (kali-linux-2021.1-installer-arm64.iso and kali-linux-2021.1-live-arm64.iso) that can be used with VMs on Apple Silicon Macs. Many thanks to the people who reached out and offered to test and helped us to iron out the bugs. If you’d like to see it in action, [@David Bombal](https://twitter.com/davidbombal) has put out a [video](https://www.youtube.com/watch?v=uBzKDF67eWY) of it.

We have also added support for the Raspberry Pi 400’s wireless card, however it is very important to note that this is not a [nexmon](https://github.com/seemoo-lab/nexmon) firmware, as nexmon does not currently support it.

The [Kali ARM build scripts](https://gitlab.com/kalilinux/build-scripts/kali-arm/) have seen a few more improvements from [@Francisco Jose Rodriguez Martos](https://twitter.com/FrangaLinux) and we appreciate the assistance greatly. If you’d like to get involved with ARM, check out the [GitLab issue list](https://gitlab.com/kalilinux/build-scripts/kali-arm/-/work_items).

### Download Kali Linux 2021.1Fresh Images:
So what are you waiting for? Start [downloading](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for the ones who are not, we do also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use as well. If you cannot wait for our next release and you want the latest packages (or bug fixes) when you download the image, you can just use the weekly image instead.
This way you’ll have fewer updates to do.
Just know that these are automated builds that we do not QA like we do our standard [release images](https://www.kali.org/releases/). But we gladly take [bug reports](https://bugs.kali.org/) about those images because we want any issues to be fixed before our next release!

Existing Installs:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

┌──(kali㉿kali)-[~]
└─$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list

┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt -y full-upgrade

┌──(kali㉿kali)-[~]
└─$ [ -f /var/run/reboot-required ] && sudo reboot -f

You should now be on Kali Linux 2021.1. We can do a quick check by doing:

┌──(kali㉿kali)-[~]
└─$ grep VERSION /etc/os-release
VERSION="2021.1"
VERSION_ID="2021.1"
VERSION_CODENAME="kali-rolling"

┌──(kali㉿kali)-[~]
└─$ uname -v
#1 SMP Debian 5.10.13-1kali1 (2021-02-08)

┌──(kali㉿kali)-[~]
└─$ uname -r
5.10.0-kali3-amd64

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/). We’ll never be able to fix what we do not know is broken! And [Twitter](https://twitter.com/kalilinux) is not a Bug Tracker!

## 2020.4 – 2020-11-18

**Kali Linux 2020.4 Release (ZSH, Bash, CME, MOTD, AWS, Docs, Win-KeX & Vagrant)**

Table of Contents
- [ZSH Shell By Default](#zsh-shell-by-default)
- [Bash Shell Makeover](#bash-shell-makeover)
- [Partnership with tools authors: byt3bl33d3r’s CrackMapExec (CME)](#partnership-with-tools-authors-byt3bl33d3rs-crackmapexec-cme)
- [Message At Login](#message-at-login)
- [AWS EC2 Cloud Image Refresh](#aws-ec2-cloud-image-refresh)
- [Kali-Docs & Packaging Guides](#kali-docs--packaging-guides)
- [New Tools & Updates](#new-tools--updates)
- [Kali NetHunter](#kali-nethunter)
- [Win-KeX 2.5](#win-kex-25)
- [Kali Vagrant & VMware](#kali-vagrant--vmware)
- [Kali ARM devices](#kali-arm-devices)
- [Community Shoutouts](#community-shoutouts)
- [Download Kali Linux 2020.4](#download-kali-linux-20204)

We find ourselves in the 4th quarter of 2020, and we are ecstatic to announce the release of Kali Linux 2020.4, which is ready for immediate [download](https://www.kali.org/get-kali/) or [updating](https://www.kali.org/docs/general-use/updating-kali/).

What’s different with this release since [2020.3 in August 2020](https://www.kali.org/blog/kali-linux-2020-3-release/) is:

- [ZSH is the new default shell](#zsh-shell-by-default) - We said it was happening last time, Now it has. ZSH. Is. Now. Default.
- [Bash shell makeover](#bash-shell-makeover) - It may not function like ZSH, but now Bash looks like ZSH.
- [Partnership with tools authors](#partnership-with-tools-authors-byt3bl33d3rs-crackmapexec-cme) - We are teaming up with [@byt3bl33d3r](https://twitter.com/byt3bl33d3r).
- [Message at login](#message-at-login) - Proactively pointing users to resources.
- [AWS image refresh](#aws-ec2-cloud-image-refresh) - Now on GovCloud. Includes Kali’s default (command line) tools again. And there is a new URL.
- [Packaging guides](#kali-docs--packaging-guides) - Want to start getting your tool inside of Kali? This should help.
- [New tools & updates](#new-tools--updates) - New Kernel and various new tools and updates for existing ones, as well as setting Proxychains 4 as default.
- [NetHunter updates](#kali-nethunter) - New NetHunter settings menu, select from different boot animations, and persistent Magisk.
- [Win-KeX 2.5](#win-kex-25) - New “Enhanced Session Mode” brings Win-KeX to ARM devices.
- [Vagrant & VMware](#kali-vagrant--vmware) - We now support VMware users who use Vagrant.

### ZSH Shell By DefaultIn our [previous quarterly release, 2020.3](https://www.kali.org/blog/kali-linux-2020-3-release/), we gave a heads up that we will be switching from Bash to ZSH as our default shell going forwards (where possible). We are happy to announce that after testing and feedback from users, the switch has now happened. Say hello to ZSH:

┌──(kali㉿kali)-[~]
└─$ echo "Hello World. I'm $0"
Hello World. I'm zsh

┌──(kali㉿kali)-[~]
└─$

Thank you to everyone who provided positive and constructive feedback. We are happy with it, and hope you are too. With that said, we know we cannot please everyone with it (so if you wish to revert back to Bash, please do: chsh -s /bin/bash).

ZSH will be the default shell on our [desktop images](https://www.kali.org/docs/installation/) (amd64/i386), and [cloud](https://www.kali.org/docs/cloud/).
For the time being, other platforms (e.g. [ARM](https://www.kali.org/docs/arm/), [containers](https://www.kali.org/docs/containers/), [NetHunter](https://www.kali.org/docs/nethunter/), [WSL](https://www.kali.org/docs/wsl/)/) will still use Bash. We hope to switch more over in later versions.
If you use adduser, regardless of the platform, it will also default to Bash for the time being (to avoid some edge cases of items breaking). In time, this will be changed as well.

How do I get it? Good question! If you:

- Do a fresh install of Kali Linux 2020.4 or later, it will “just happen” during the setup.
- If you are [updating Kali](https://www.kali.org/docs/general-use/updating-kali/), you will need to switch each user to ZSH (e.g. non-root & root since Kali Linux does not use the root account since [2020.1](https://www.kali.org/blog/kali-linux-2020-1-release/)/).

I need to switch. How do I? This can be done by applying our default zshrc file. If you are not already using ZSH, you can simply copy it over. If you are, you will need to overwrite (make sure to backup first):

kali@kali:~$ [ -e ~/.zshrc ] && cp -i ~/.zshrc{,.bak}
kali@kali:~$
kali@kali:~$ cp -i /etc/skel/.zshrc ~/
kali@kali:~$
kali@kali:~$ chsh -s /bin/zsh
kali@kali:~$
kali@kali:~$ zsh

If you’re reading this, you may also be the type of person who likes Easter eggs - our prompts contain a few! If you go looking you may find a few gems (e.g. new_line_before_prompt & root vs non-root)._

### Bash Shell MakeoverKali Linux now has a universal, cross-shell theme.

Whilst we were tweaking ZSH, we also updated our Bash prompt ($PS1), to make it feel similar (but not act similar) to our ZSH prompt. We started playing with the Bash prompt in [Kali Linux 2020.3](https://www.kali.org/blog/kali-linux-2020-3-release/), when the colors changed for non-root users, from red to blue. Before then, we had not changed it since Kali Linux was [first released](https://www.kali.org/blog/kali-linux-1-0-0-release/).

https://www.kali.org/blog/kali-linux-2020-4-release/images/bash.png

How do I get it? Another good question! Very similar answer to ZSH, but this time using .bashrc instead. If you are doing:

- A fresh installation of Kali Linux 2020.4 or later, it’s already applied.
- If you are [updating Kali](https://www.kali.org/docs/general-use/updating-kali/), you will need to configure each user (e.g. non-root & root/)

If you have made any alterations to ~/.bashrc, make sure to back it up before replacing it:

kali@kali:~$ cp -i .bashrc{,.bak}
kali@kali:~$
kali@kali:~$ cp -i /etc/skel/.bashrc ~/
kali@kali:~$
kali@kali:~$ source ~/.bashrc
┌──(kali㉿kali)-[~]
└─$ echo "Hello World. I'm $0"
Hello World. I'm bash
┌──(kali㉿kali)-[~]
└─$

If you look & edit the contents of .bashrc, you can switch to the red “[BackTrack](https://www.backtrack-linux.org/)” prompt to be nostalgic.

### Partnership with tools authors: byt3bl33d3r’s CrackMapExec (CME)Kali Linux is part of the greater community and we want to support tool authors where possible. If you have not heard of [CrackMapExec (a.k.a CME)](https://pkg.kali.org/pkg/crackmapexec), you may be missing a trick (or three) when it comes to doing infrastructure assessments (especially involving Active Directory).

We noticed that [@byt3bl33d3r](https://twitter.com/byt3bl33d3r/status/1275611300194705409) made the decision to move to a sponsorware model. You may or may not agree with his decision, but we understand [his reasoning](https://porchetta.industries/2020/11/17/And-Now-For-Something-Completely-Diffrent/). The tools which he makes are highly valuable and relied upon by many. We want to support him and our Kali Linux users. After various calls and email exchanges, we are delighted to reveal Kali has partnered with byt3bl33d3r.

What does this mean for me? The Kali package of CME is now pulling from a private source, allowing Kali Linux users to get access to the newest changes in CME 30 days before the tool is made public to everyone else. If you don’t use Kali, you either need to [sponsor directly](https://github.com/sponsors/byt3bl33d3r) or wait for it to be released after 30 days.

Why are you doing this? Because we believe in Open-source and the community as a whole. This way, everyone benefits; both authors and users.

Kali is Open-source. What is stopping me from stealing/ripping/cloning from you? The code will be distributed with a banner saying something along the lines of, “for Kali users only”. Removing/altering the code will break the software license thus breaking copyright law. Do not be that guy.

Is that it? Yes! [Kali Linux is Open-source](https://www.kali.org/docs/policy/kali-linux-open-source-policy/). We understand and respect software licenses, and by doing so we hope to keep everything Open-source as much as possible. Putting checks & protection in place, you may be happy using someone else’s cracked/pirated software (warez) - but do you know [what has been altered under the hood](https://blog.cobaltstrike.com/2013/09/05/how-to-crack-cobalt-strike-and-backdoor-it/)?

But Kali Linux being Open-source, has to respect other people license agreements, as do any other respectable organizations. This also includes when tools which have their license agreements changed in [software updates](https://github.com/volatilityfoundation/volatility3/issues/208), as a result, we have removed them from Kali.

We have more to announce about direction step in a 2021.x release (as well as looking for other authors to sponsor with). Stay tuned for more information!

### Message At LoginWe have noticed there being a large uprise of the amount of people saying “Kali Linux is missing ‘XYZ’” or “XYZ feature is broken”, when this is not always the case. We have done our best to write up various issues on [our docs pages](https://www.kali.org/docs/), however it appears they are not always being read. We also know that not everyone has a unix beard as long as [elwood-offsec](https://www.kali.org/about-us/), but hope you still are an [experienced Linux user](https://www.kali.org/docs/introduction/should-i-use-kali-linux/). There is always a reason why something is the way it is, but it may require more than the usual basic troubleshooting.

With all of that said, we are wanting to improve our communications going forwards. Most of the actions in Kali are done by the command line. So now, upon logging into a Kali terminal or console, you may be presented with a mixture of the following (depending on the configuration of your system, as it is dynamic):

$ ssh [[email protected]](https://www.kali.org/cdn-cgi/l/email-protection)
Last login: Thu Nov 12 15:12:29 2020 from 172.16.13.1
┏━(Message from Kali developers)
┃
┃ This is a minimal installation of Kali Linux, you likely
┃ want to install supplementary tools. Learn how:
┃ ⇒ https://www.kali.org/docs/troubleshooting/common-minimum-setup/
┃
┃ This is a cloud installation of Kali Linux. Learn more about
┃ the specificities of the various cloud images:
┃ ⇒ https://www.kali.org/docs/troubleshooting/common-cloud-setup/
┃
┃ We have kept /usr/bin/python pointing to Python 2 for backwards
┃ compatibility. Learn how to change this and avoid this message:
┃ ⇒ https://www.kali.org/docs/general-use/python3-transition/
┃
┗━(Run "touch ~/.hushlogin"
┌──(kali㉿kali)-[~]
└─$

We hope this helps various common problems to be quickly fixed, but at the same time, not feel intrusive. Each of the issues have a link to our documentation page in order to correct the issue. After its been addressed, the message should not be displayed again. For whatever reason (unable or do not want to), you can permanently hide any messages from us being displayed by doing: touch ~/.hushlogin (per user) or touch /etc/kali-motd/disable-all (for a global setting).

We have a few other things in the works to help communicate items out planned for 2021.x. Stay tuned!

### AWS EC2 Cloud Image RefreshKali Linux has been on [AWS](https://www.kali.org/docs/cloud/aws/) since [1.0.6](https://www.kali.org/blog/kali-linux-1-0-6-release/). Over the years, we have done various refreshes of our [build-scripts](https://gitlab.com/kalilinux/build-scripts) to produce the [cloud images](https://gitlab.com/kalilinux/build-scripts/kali-cloud). Finally with Kali 2020.2, we have a fully automated system in place. However during the changeover, we were shipping the image without any GUI or any tools by default. This was to give the cleanest, smallest image as possible. In hindsight, we didn’t communicate this change over well, and a lot of you noticed “tools missing” (as kali-linux-default was not included/). However, in 2020.4, we have created a new metapackage, kali-linux-headless, and included it which only has the default set of command line tools.

Upon doing the refresh, we have worked with AWS to get Kali Linux added to “[GovCloud](https://twitter.com/kalilinux/status/1321453286067707904)”. Which may be useful to a certain audience. With how the accounts were setup, we have had to start from fresh. As a result, we have a [new marketplace entry](https://aws.amazon.com/marketplace/pp/B08LL91KKB).

What does this mean for people who are using the old entry? As Kali Linux is a rolling distribution, not a lot! You can still keep [updating Kali Linux](https://www.kali.org/docs/general-use/updating-kali/) as usual. However, you will no longer be able to spin up the latest version using the latest instance. For that, you will need to switch to the new entry.

Note: We have tried to say it as many different places as possible, but putting it here is not going to hurt. The default login for AWS EC2 username is “kali” (not the standard “ec2-user”).

### Kali-Docs & Packaging GuidesIn [2019.4](https://www.kali.org/blog/kali-linux-2019-4-release/), we moved https://docs.kali.org/ from a WordPress solution to https://www.kali.org/docs/ using Hugo. In September, we finished (for now) tweaking the theme, making it easier to use, super fast at loading and easier to anyone to edit.

We have started to go though all the pages and refreshing them, bringing them all up-to-date, and adding more in. We are doing it section by section, and so far have completed the first three (so we still have a way to go! After it is completed, it will be easier to keep them up-to-date, making it an on-going task. For the sections that are missing or lacking content, we have been generating [issues to help track](https://gitlab.com/kalilinux/documentation/kali-docs/-/boards/1429718). If you want to help get [involved with Kali Linux](https://www.kali.org/docs/community/contribute/), this is an easy place to start.

We have also created various new pages, all about our packaging process:

- [Setting Up A System For Packaging](https://www.kali.org/docs/development/setting-up-packaging-system/)
- [Introduction to Packaging (Instaloader)](https://www.kali.org/docs/development/intro-to-packaging-example/)
- [Intermediate Packaging (Photon)](https://www.kali.org/docs/development/intermediate-packaging-example/)
- [Advanced Packaging (FinalRecon & Python-icmplib)](https://www.kali.org/docs/development/advanced-packaging-example/)

We have also the pages from our login messages:

- [Common Cloud Based Setup Information](https://www.kali.org/docs/troubleshooting/common-cloud-setup/)
- [Everything you need to know about the switch to Python 3](https://www.kali.org/docs/general-use/python3-transition/)
- [Minimum Install Setup Information](https://www.kali.org/docs/troubleshooting/common-minimum-setup/)

And various other pages created:

- [AWS](https://www.kali.org/docs/cloud/aws/)
- [Kali inside VirtualBox (Guest VM)](https://www.kali.org/docs/virtualization/install-virtualbox-guest-vm/)
- [Using EoL Python Versions on Kali](https://www.kali.org/docs/general-use/using-eol-python-versions/)
- [Win-KeX v2](https://www.kali.org/docs/wsl/win-kex/)
- [Win-KeX SL](https://www.kali.org/docs/wsl/win-kex-sl/)
- [Win-KeX Win](https://www.kali.org/docs/wsl/win-kex-win/)

### New Tools & UpdatesAs with every Kali release, there are new tools and updates. The [kernel](https://pkg.kali.org/pkg/linux) got an upgrade to 5.9, so you benefit with all the loveliness that that brings. We have switched to “[proxychains4](https://pkg.kali.org/pkg/proxychains-ng)” (aka [ProxyChains-NG](https://github.com/rofl0r/proxychains-ng)) as the default (everything from v3 should still work: same flags and configuration files & folder locations for legacy users, else the paths will reflect the version if starting from fresh). Also, [GNOME](https://pkg.kali.org/pkg/meta-gnome3) was updated to 3.38 & [KDE](https://pkg.kali.org/pkg/meta-kde) to 5.19.

New tools in Kali Linux:

- [Apple bleee](https://pkg.kali.org/pkg/apple-bleee)
- [CertGraph](https://pkg.kali.org/pkg/certgraph)
- [dnscat2](https://pkg.kali.org/pkg/dnscat2)
- [FinalRecon](https://pkg.kali.org/pkg/finalrecon)
- [goDoH](https://pkg.kali.org/pkg/godoh)
- [hostapd-mana](https://pkg.kali.org/pkg/hostapd-mana)
- [Metasploit Framework v6](https://pkg.kali.org/pkg/metasploit-framework)
- [Whatmask](https://pkg.kali.org/pkg/whatmask)

One last thing. We have tweaked how we handle our wallpaper packages:

- kali-wallpapers-all ~ Give me all the wallpapers
- kali-wallpapers-2019.4 ~ Default for Kali Linux between 2019.4 and 2020.3
- kali-wallpapers-2020.4 ~ Default for Kali Linux between 2020.4 and onwards
- kali-wallpapers-legacy ~ Nostalgic value

### Kali NetHunter@yesimxev has added a new settings menu, allowing for easy back up and restore of configuration files. It also allows you to change the Kali NetHunter boot animation. How is this as a teaser?

https://www.kali.org/blog/kali-linux-2020-4-release/images/boot-kali.gif

Call on all boot animation devs out there: We’d love to hear from you. If you have a cool boot animation you’d like to share, please submit a merge request to our [Kali NetHunter Boot Animation repository](https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-bootanimation).

The new images also contain a “Magisk persistence” module, so we no longer have to flash Magisk again after we installed Kali NetHunter.

### Win-KeX 2.5Win-KeX 2.5 includes a new “[Enhanced Session Mode](https://www.kali.org/docs/virtualization/install-hyper-v-guest-enhanced-session-mode/) (–esm)”, which works like the “Window” mode but uses the Remote Deskop Protocol (RDP/) & client native to Windows. This mode will allow users of “Windows on ARM” devices to use Win-KeX and it adds sharpness to Win-KeX on HiDPI devices.

We have also added a --ip option to address a bug in WoA causing massive packet losses when using “localhost”. To start Win-KeX with sound on arm devices, just type:

kali@kali:~$ kex --esm --ip --sound
kali@kali:~$

The --ip parameter has one little downside though: Win-KeX asks for the Kali Linux user password when launched for the first time and stores it in the Windows credentials store. Since the IP address changes after every reboot, you will be prompted again. This is a known WSL2 bug and we’ll expect it to be fixed soon so that we can drop the --ip parameter and we’ll never have to enter the password again.

https://www.kali.org/blog/kali-linux-2020-4-release/images/surface-kex.png

### Kali Vagrant & VMwareWe have had a Vagrant image since [Kali Linux 2018.3](https://www.kali.org/blog/kali-linux-2018-3-release/). However, it’s always been for VirtualBox. Until now. We are now also producing a VMware [Vagrant image](https://app.vagrantup.com/kalilinux/boxes/rolling)!

Note, you will need to have a separate license for both VMware and [Vagrant](https://www.vagrantup.com/vmware) for this to work, as it is a paid-for plugin.
For more information, you can see [here](https://www.vagrantup.com/docs/providers/vmware/usage) and [here](https://www.vagrantup.com/docs/providers/basic_usage).

### Kali ARM devicesWe have been working away on our [ARM images](https://www.kali.org/get-kali/#kali-arm) as usual, and this release is no exception. We have reduced the amount of pre-generated images (now 14) as there has not been the demand for these other devices. We have left their [build scripts](https://gitlab.com/kalilinux/build-scripts/kali-arm) (now up to 43 devices supported), in case you wish to generate the images yourself.

### Community ShoutoutsFollowing on from last time, these are people from the public who have helped Kali and the team for the last release. We are super grateful and want to praise them for their work (giving credit where due!):

- @1y for generating a ARM build script for a new device, imx6-ull-evk
- [dracode](https://gitlab.com/dracode) for the awesome work on NetHunter, in particular the GPS fixes.
- [mirivan](https://gitlab.com/Mirivan) for all the amazing additions and fixes to NetHunter as well as helping out with the issue tracker.
- [TheMMcOfficial](https://gitlab.com/TheMMcOfficial) for his continued help with NetHunter and DuckHunter
- [Martinvlba](https://gitlab.com/Martinvlba) for his great contributions to NetHunter, especially hostapd
- [s133py](https://gitlab.com/s133py) for all the tireless work on NetHunter and helping with issues

Not a community member per se, but we do want to give an honorable mention to [GitLab](https://gitlab.com/). Kali Linux is now a [Open-Source Partner](https://about.gitlab.com/solutions/open-source/partners/) (different to their [Open-Source Program](https://about.gitlab.com/solutions/open-source/)). We made the switch [middle of 2019](https://www.kali.org/blog/kali-linux-roadmap-2019-2020/), and we could not have been happier. Thank you GitLab for supporting [us](https://gitlab.com/kalilinux), and for everything you do for the Open-source communities as a whole!

https://www.kali.org/blog/kali-linux-2020-4-release/images/gitlab.png

And on the subject, [Kali Linux](https://hub.docker.com/u/kalilinux) is apart of [Docker’s Open-source Community](https://www.docker.com/blog/expanded-support-for-open-source-software-projects/).

### Download Kali Linux 2020.4Fresh Images:
So what are you waiting for? Start [downloading](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for the ones who are not, we do also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use as well. If you cannot wait for our next release and you want the latest packages when you download the image, you can just use the weekly image instead. This way you’ll have fewer updates to do. Just know that these are automated builds that we do not QA like we do our standard release images. But we gladly take bug reports about those images because we want any issues to be fixed before our next release.

Existing Upgrades:
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/), followed by setting the default shell to ZSH. If you’re already using ZSH, and want our new configuration, you can do the following:

kali@kali:~$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list
kali@kali:~$
kali@kali:~$ sudo apt update && sudo apt -y full-upgrade
kali@kali:~$
kali@kali:~$ cp -i /etc/skel/.bashrc ~/
kali@kali:~$
kali@kali:~$ cp -i /etc/skel/.zshrc ~/
kali@kali:~$
kali@kali:~$ chsh -s /bin/zsh
kali@kali:~$
kali@kali:~$ [ -f /var/run/reboot-required ] && sudo reboot -f
kali@kali:~$

You should now be on Kali Linux 2020.4. We can do a quick check by doing:

kali@kali:~$ grep VERSION /etc/os-release
VERSION="2020.4"
VERSION_ID="2020.4"
VERSION_CODENAME="kali-rolling"
kali@kali:~$
kali@kali:~$ uname -v
#1 SMP Debian 5.9.1-1kali2 (2020-10-29)
kali@kali:~$
kali@kali:~$ uname -r
5.9.0-kali1-amd64
kali@kali:~$

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/main_page.php). We’ll never be able to fix what we do not know is broken! And [Twitter](https://twitter.com/kalilinux) is not a Bug Tracker!

## 2020.3 – 2020-08-18

**Kali Linux 2020.3 Release (ZSH, Win-KeX, HiDPI & Bluetooth Arsenal)**

Table of Contents
- [New Shell (Is Coming)](#new-shell-is-coming)
- [Win-KeX](#win-kex)
- [Automating HiDPI](#automating-hidpi)
- [Tool Icons](#tool-icons)
- [Kali NetHunter Bluetooth Arsenal](#kali-nethunter-bluetooth-arsenal)
- [Kali NetHunter for Nokia Phones](#kali-nethunter-for-nokia-phones)
- [Setup Process](#setup-process)
- [ARM Device Updates](#arm-device-updates)
- [Desktop Environment](#desktop-environment)
- [Community Shoutouts](#community-shoutouts)
- [Download Kali Linux 2020.3](#download-kali-linux-20203)

Its that [time of year](https://www.kali.org/releases/) again, time for another Kali Linux release! Quarter #3 - Kali Linux 2020.3. This release has various impressive updates, all of which are ready for immediate [download](https://www.kali.org/get-kali/) or [updating](https://www.kali.org/docs/general-use/updating-kali/).

A quick overview of what’s new since the last release in [May 2020](https://www.kali.org/blog/kali-linux-2020-2-release/):

- [New Shell](#new-shell-is-coming) - Starting the process to switch from “Bash” to “ZSH”
- The release of [Win-KeX](#win-kex) - Get ready WSL2
- [Automating HiDPI](#automating-hidpi) support - Easy switching mode
- [Tool Icons](#tool-icons) - Every default tool now has its own unique icon
- [Bluetooth Arsenal](#kali-nethunter-bluetooth-arsenal) - New set of tools for Kali NetHunter
- [Nokia Support](#kali-nethunter-for-nokia-phones) - New devices for Kali NetHunter
- [Setup Process](#setup-process) - No more missing network repositories and quicker installs

### New Shell (Is Coming)Most people who use Kali Linux, ([we hope](https://www.kali.org/docs/introduction/should-i-use-kali-linux/)), are very experienced Linux users. As a result, they feel very comfortable around the command line. We understand that “shells” are a very personal and precious thing to everyone (local or remote!), as that is how most people interact with Kali Linux. To the point where lots of experienced users only use a “GUI” to spin up multiple terminals. By default, Kali Linux has always used “bash” (aka “Bourne-Again SHell”) as the default shell, when you open up a terminal or console. Any seasoned Kali user would know the prompt kali@kali:~$ (or root@kali:~# for the older users!/) very well!

Today, we are announcing the plan to switch over to ZSH shell. This is currently scheduled to be the default shell in 2020.4 (for this 2020.3 release, bash will still be the default).

If you have a fresh default install of Kali Linux 2020.3, you should have ZSH already installed (if not, do sudo apt install -y zsh zsh-syntax-highlighting zsh-autosuggestions), ready for a try.
However if you installed an earlier version of Kali Linux and have upgraded to 2020.3, your user will be lacking the default ZSH configuration that we cooked with lots of love. So for upgrade users only, make sure to copy the configuration file:

kali@kali:~$ cp /etc/skel/.zshrc ~/
kali@kali:~$

Then all you need to do is switch to ZSH:

kali@kali:~$ zsh
┌──(kali㉿kali)-[~]
└─$

https://www.kali.org/blog/kali-linux-2020-3-release/images/release-2020.3-zsh.png

If you like what you see, you can set ZSH as your default (replacing bash) by doing chsh -s /bin/zsh. Which is what we will be doing in 2020.4.

We wanted to give the community a notice before this switch happens. This is a very large change (some may argue larger than the [Gnome to Xfce switch last year](https://www.kali.org/blog/kali-linux-2019-4-release/)). We are also looking for [feedback](https://bugs.kali.org/main_page.php). We hope we have the right balance of design and functionality, but we know these typically don’t get done perfect the first time. And, we don’t want to overload the default shell with too many features, as lower powered devices will then struggle or it may be hard to on the eyes to read. ZSH has been something we have wanted to do for a long time (even before the switch over to [Xfce](https://www.kali.org/blog/kali-linux-2019-4-release/)!).

We will be doing extensive testing during this next cycle so we reserve the right to delay the default change, or change direction all together. Again, we encourage you to provide [feedback](https://bugs.kali.org/main_page.php) on this process. There is no way we can cover every use case on our own, so your help is important.

Q.) Why did you make the switch? What’s wrong with bash?
A.) You can do a lot of advanced things with bash, and customize it to do even more, but ZSH allows you to do even more. This was one really large selling point.

Q.) Why did you pick ZSH and not fish?
A.) In the discussion of switching shells, one of the options that came up is Fish (Friendly Interactive SHell). Fish is a nice shell (probably nicer than ZSH), but realistically it was not a real consideration due to the fact that it is not POSIX compatible. This would cause a lot of issues, as common one-liners just won’t work.

Q.) Are you going to use any ZSH frameworks (e.g. Oh-My-ZSH or Prezto)?
A.) At this point in time, by default, no. The weight of these would not be workable for lower powered devices. You can still install them yourself afterwards (as many of our team do).

### Win-KeXHaving Kali Linux on “Windows Subsystem for Linux” (WSL) is something [we have been taking advantage of](https://www.kali.org/blog/kali-on-the-windows-subsystem-for-linux/) since it came out. With the release of [WSLv2](https://www.kali.org/blog/wsl2-and-kali/), the overall functionality and user experience improved dramatically.

Today, the experience is improving once more with the introduction of Win-KeX (Windows + Kali Desktop EXperience). After installing it, typing in kex, or clicking on the button, Win-KeX will give you a persistent-session GUI.

https://www.kali.org/blog/kali-linux-2020-3-release/images/release-2020.3-win-kex.png

After getting WSL installed (there’s countless guides online, or you can follow [ours](https://www.kali.org/docs/wsl/win-kex/)/), you can install Win-KeX by doing the following:

sudo apt update && sudo apt install -y kali-win-kex

Afterwards, if you want to make a shortcut, follow our [guide](https://www.kali.org/docs/wsl/win-kex/), or you can just type in kex!

On the subject of WSL (and this is true for Docker and AWS EC2) something we have seen a bit is after getting a desktop environment, people have noticed the tools are not “there”. This is because they are not included by default, to keep the image as small as possible. You either need to manually install them one by one, or grab the [default metapackage](https://www.kali.org/docs/general-use/metapackages/) to get all the tools from out-of-the-box: sudo apt install -y kali-linux-default

Please note, Win-KeX does require WSL v2 on x64 as it’s not compatible with WSL v1, or arm64.

For more information, please see our [documentation page on Win-KeX](https://www.kali.org/docs/wsl/win-kex/)

### Automating HiDPIHiDPI displays are getting more and more common. Unfortunately, Linux support, out of the box, hasn’t been great (older Linux users may remember a time where this was very common for a lot of hardware changes.). Which means after doing a fresh install, there is a bit of tweaking required to get it working, otherwise the font/text/display may be very small to read. We have [had a guide](https://www.kali.org/docs/general-use/hidpi/) out explaining the process required to get it working, but the process before was a little “fiddly”. We wanted to do better.

So we made kali-hidpi-mode. Now, either typing in kali-hidpi-mode or selecting it from the menu (as shown below), should automate switching between HiDPI modes.

https://www.kali.org/blog/kali-linux-2020-3-release/images/release-2020.3-hidpi.gif

### Tool IconsOver the last few releases, we have been showing the progress on getting more themed icons for tools. We can now say, if you use the default tool listing (kali-linux-default), every tool in the menu (and then a few extra ones!), should have their own icon now.

https://www.kali.org/blog/kali-linux-2020-3-release/images/release-2020.3-icons.png

We will be working on adding missing tools to the menu (and creating icons for them) over the next few releases of Kali, as well as expanding into the kali-linux-large [metapackage](https://www.kali.org/docs/general-use/metapackages/) (then kali-tools-everything/). We also have plans for these icons, outside of the menu - more information in an upcoming release!

### Kali NetHunter Bluetooth ArsenalWe are proud to introduce Bluetooth Arsenal by [yesimxev](https://gitlab.com/yesimxev) from the [Kali NetHunter team](https://www.kali.org/about-us/). It combines a set of bluetooth tools in the Kali NetHunter app with some pre-configured workflows and exciting use cases. You can use your external adapter for reconnaissance, spoofing, listening to and injecting audio into various devices, including speakers, headsets, watches, or even cars.

Please note that RFCOMM and RFCOMM tty will need to be enabled in kernels from now on to support some of the tools.

https://www.kali.org/blog/kali-linux-2020-3-release/images/release-2020.3-nh-bluetooth.png

### Kali NetHunter for Nokia PhonesKali NetHunter now supports the Nokia 3.1 and Nokia 6.1 phones, thanks to [yesimxev](https://gitlab.com/yesimxev). Images are available on our [download site](https://www.kali.org/get-kali/#kali-mobile). Please note that those images contain a “minimal Kali rootfs” due to technical reasons but you can easily install all the default tools via sudo apt install -y kali-linux-default.

https://www.kali.org/blog/kali-linux-2020-3-release/images/release-2020.3-nokia-nethunter.png

### Setup ProcessThe full installer image always had all the packages required for an offline installation but if you installed a Kali Linux system with this image and without disabling the network, the installer would automatically run dist-upgrade during the install. This is done to make sure that you have the latest packages on first boot. And that step can take a very long time, especially after a few months after a release when lots of updates have accumulated. Starting with 2020.3, we disabled the network mirror in the full installer so that you always get the same installation speed, and the same packages and versions for that release - just make sure to [update](https://www.kali.org/docs/general-use/updating-kali/) after installing!

Whilst we were at it, we fixed another related issue. If you didn’t have network access (either voluntarily or otherwise) during installation, you would get an empty [network repository](https://www.kali.org/docs/general-use/kali-apt-sources/) (/etc/apt/sources.list/). This means, you would not be able to use apt to install additional packages. While there might be some users who will never have network, we believe that it’s best to actually configure that file in all cases. So that’s what we did. By default, any fresh installs going forward after 2020.3 will have network repositories pre-defined.

### ARM Device UpdatesWe have (along with the work of [@Francisco Jose Rodríguez Martos](https://twitter.com/FrangaLinux) who did a lot of the back end changes) refreshed our [build-scripts for our ARM devices](https://gitlab.com/kalilinux/build-scripts/kali-arm). We [pre-generated various different ARM images](https://www.kali.org/get-kali/#kali-arm) (as of 2020.3 - 19 images) to allow for quick download and deployment, but we have build scripts for more (as of 2020.3 - 39 images). If your device is not one of ones that we release images for, you’ll need to use the scripts to self generate the image.

Notable changes in ARM’s 2020.3 release:

- All of the ARM images come with kali-linux-default [metapackage](https://www.kali.org/docs/general-use/metapackages/) installed, bringing them in line with the rest of our releases, so more tools are available when you first boot
- We have reduced the size of all our ARM images that are created, so downloads should be smaller. However, you will still need to use at least a 16GB sdcard/USB drive/eMMC
- Pinebook and Pinebook Pro images can now be used on either sdcard or eMMC
- The Pinebook image now has the WiFi driver built during image creation, instead of on first boot, this should speed up first boot time massively
- The Pinebook Pro has a change from the upstream firmware, which changes ccode=DE to ccode=all - this allows access to more 2.4GHz and 5GHz channels
- The 64-bit RaspberryPi images now have the RaspberryPi userland utilities built during image creation, so vcgencmd and various other utilities that were previously only available on the 32-bit image are now usable on 64-bit as well
- The ODROID-C2 image now uses the Kali kernel, instead of a vendor provided one. This means in the future, an apt dist-upgrade will get you kernel updates instead of waiting for a new Kali release
- The /etc/fstab file now includes the root partition via UUID, this should make it easier when trying to use a USB drive instead of sdcard on devices that support it

A few things which are work in progress:

- RaspberryPi images are using 4.19 kernels. We would like to move to 5.4 however, nexmon isn’t working properly with it (as the new kernel requires firmware version => 7.45.202) for which [no nexmon patch exists yet](https://github.com/seemoo-lab/nexmon/issues/423)
- There is a new USBArmory Mk2 [build script](https://gitlab.com/kalilinux/build-scripts/kali-arm). We don’t have the hardware to test it however, so we are looking for community feedback who is able to test it out
- Veyron image will be released at a later date to kernel issues that haven’t yet been tracked down

### Desktop EnvironmentAs there has been minor update to Gnome, we have been taking some advantages of the new settings:

- GNOME’s file manager nautilus has a new theme
- GNOME’s system-monitor now matches the colors and also has stacked CPU charts
- Improved the design for “nested headerbars” (example, in the Settings Window, where the left headerbar is joined with the side-navbar)

https://www.kali.org/blog/kali-linux-2020-3-release/images/release-2020.3-gnome.png

### Community ShoutoutsA new section in the release notes, community shoutouts. These are people from the public who have helped Kali and the team for the last release. And we want to praise them for their work (we like to give credit where due!):

- [@Crash](https://twitter.com/crashbrz) who has been helping the community for some time now, thank you!
- [@FrangaL](https://twitter.com/FrangaLinux) who has been doing some great work with Kali Linux ARM, thank you!

Anyone can help out, anyone can get [involved](https://www.kali.org/docs/community/contribute/)!

### Download Kali Linux 2020.3Fresh Images
So what are you waiting for? Start [downloading](https://www.kali.org/get-kali/) already!

Seasoned Kali Linux users are already aware of this, but for the ones who are not, we do also produce [weekly builds](https://cdimage.kali.org/kali-images/kali-weekly/) that you can use as well. If you can’t wait for our next release and you want the latest packages when you download the image, you can just use the weekly image instead. This way you’ll have fewer updates to do. Just know these are automated builds that we don’t QA like we do our standard release images. But we gladly take bug reports about those images because we want any issues to be fixed before our next release.

Existing Upgrades
If you already have an existing Kali Linux installation, remember you can always do a quick [update](https://www.kali.org/docs/general-use/updating-kali/):

kali@kali:~$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list
kali@kali:~$
kali@kali:~$ sudo apt update && sudo apt -y full-upgrade
kali@kali:~$
kali@kali:~$ [ -f /var/run/reboot-required ] && sudo reboot -f
kali@kali:~$

You should now be on Kali Linux 2020.3. We can do a quick check by doing:

kali@kali:~$ grep VERSION /etc/os-release
VERSION="2020.3"
VERSION_ID="2020.3"
VERSION_CODENAME="kali-rolling"
kali@kali:~$
kali@kali:~$ uname -v
#1 SMP Debian 5.7.6-1kali2 (2020-07-01)
kali@kali:~$
kali@kali:~$ uname -r
5.7.0-kali1-amd64
kali@kali:~$

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux-latest).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/main_page.php). We’ll never be able to fix what we don’t know is broken! And [Twitter](https://twitter.com/kalilinux) is not a Bug Tracker!

## 2020.2 – 2020-05-12

**Kali Linux 2020.2 Release (KDE & PowerShell)**

Table of Contents
- [KDE Plasma Makeover & Login](#kde-plasma-makeover--login)
- [PowerShell by Default. Kind of.](#powershell-by-default-_kind-of_)
- [Kali on ARM Improvements](#kali-on-arm-improvements)
- [Lessons From Installer Changes](#lessons-from-installer-changes)
- [New Key Packages & Icons](#new-key-packages--icons)
- [WSLconf](#wslconf)
- [Behind the Scenes, Infrastructure Improvements](#behind-the-scenes-infrastructure-improvements)
- [Kali NetHunter](#kali-nethunter)
- [Download Kali Linux 2020.2](#download-kali-linux-20202)

Despite the turmoil in the world, we are thrilled to be bringing you an awesome update with Kali Linux 2020.2! And it is available for immediate [download](https://www.kali.org/get-kali/).

A quick overview of what’s new since [January](https://www.kali.org/blog/kali-linux-2020-1-release/):

- KDE Plasma Makeover & Login
- PowerShell by Default. Kind of.
- Kali on ARM Improvements
- Lessons From The Installer Changes
- New Key Packages & Icons
- Behind the Scenes, Infrastructure Improvements

### KDE Plasma Makeover & LoginWith [Xfce](https://www.kali.org/blog/kali-linux-2019-4-release/) and GNOME having had a Kali Linux look and feel update, it’s time to go back to our roots (days of [BackTrack](https://www.backtrack-linux.org/)) and give some love and attention to KDE Plasma. Introducing our dark and light themes for KDE Plasma:

https://www.kali.org/blog/kali-linux-2020-2-release/images/release-2020.2-kali-kde-dark.png

https://www.kali.org/blog/kali-linux-2020-2-release/images/release-2020.2-kali-kde-light.png

On the subject of theming, we have also tweaked the login screen ([lightdm](https://pkg.kali.org/pkg/lightdm)). It looks different, both graphically and the layout (the login boxes are aligned now)!

https://www.kali.org/blog/kali-linux-2020-2-release/images/release-2020.2-login-dark.png

https://www.kali.org/blog/kali-linux-2020-2-release/images/release-2020.2-login-light.png

### PowerShell by Default. Kind of.[A while ago](https://www.kali.org/blog/kali-linux-2019-4-release/), we put PowerShell into [Kali Linux’s network repository](https://www.kali.org/docs/general-use/kali-apt-sources/). This means if you wanted powershell, you had to install the package as a one off by doing:

kali@kali:~$ sudo apt install -y powershell

We now have put PowerShell into one of our (primary) [metapackages](https://www.kali.org/docs/general-use/metapackages/), kali-linux-large. This means, if you choose to install this metapackage during system setup, or once Kali is up and running (sudo apt install -y kali-linux-large), if PowerShell is compatible with your architecture, you can just jump straight into it (pwsh)!

PowerShell isn’t in the default metapackage (that’s kali-linux-default), but it is in the one that includes the default and many extras, and can be included during system setup.

### Kali on ARM ImprovementsWith [Kali Linux 2020.1](https://www.kali.org/blog/kali-linux-2020-1-release/), desktop images no longer used “root/toor” as the [default credentials](https://www.kali.org/docs/introduction/default-credentials/) to login, but had moved to “kali/kali”. Our ARM images are now the same. We are no longer using the super user account to login with.

We also warned back in [2019.4](https://www.kali.org/blog/kali-linux-2019-4-release/) that we would be moving away from a 8GB minimum SD card, and we are finally ready to pull the trigger on this. The requirement is now 16GB or larger.

One last note on the subject of ARM devices, we are not installing locales-all any more, so we highly recommend that you set your locale. This can be done by running the following command, sudo dpkg-reconfigure locales, then log out and back in.

### Lessons From Installer ChangesWith [Kali Linux 2020.1](https://www.kali.org/blog/kali-linux-2020-1-release/) we announced our new style of images, “installer” & “live”.

Issue
It was intended that both “installer” & “live” could be customized during setup, to select which metapackage and desktop environment to use. When we did that, we couldn’t include metapackages beyond default in those images, as it would create too large of an ISO. As the packages were not in the image, if you selected anything other than the default options it would require network access to obtain the missing packages beyond default. After release, we noticed some users selecting “everything” and then waiting hours for installs to happen. They couldn’t understand why the installs where taking so long.

We also have used different software on the back end to generate these images, and a few bugs slipped through the cracks (which explains the [2020.1a](https://bugs.kali.org/view.php?id=6053) and 2020.1b releases).

Solutions

- We have removed kali-linux-everything as an install time option (which is every package in the Kali Linux repository) in the installer image, as you can imagine that would have taken a long time to download and wait for during install
- We have cached kali-linux-large & every desktop environment into the install image (which is why its a little larger than previous to download) - allowing for a COMPLETE offline network install
- We have removed customization for “live” images - the installer switched back to copying the content of the live filesystem allowing again full offline install but forcing usage of our default XFCE desktop

https://www.kali.org/blog/kali-linux-2020-2-release/images/release-2020.2-setup.png

Summary

- If you are wanting to run Kali from a live image (DVD or USB stick), please use “live”
- If you are wanting anything else, please use “installer”
- If you are wanting anything other than XFCE as your desktop environment, please use “installer”
- If you are not sure, get “installer”

Also, please keep in mind on an actual assessment “more” is not always “better”. There are very few reasons to install kali-linux-everything, and many reasons not too. To those of you that were selecting this option, we highly suggest you [take some time and educate yourself on Kali](https://kali.training/) before using it. Kali, or any other pentest distribution, is not a “turn key auto hack” solution. You still need to learn your platform, learn your tools, and educate yourself in general.

Consider what you are really telling Kali to do when you are installing kali-linux-everything. Its similar to if you went into your phones app store and said “install everything!”. Thats likely not to have good results. We provide a lot of powerful tools and options in Kali, and while we may have a reputation of “Providing machine guns to monkeys”, but we actually expect you to know what you are doing. Kali is not going to hold your hand. It expects you to do the work of learning and Kali will be unforgiving if you don’t.

### New Key Packages & IconsJust like every Kali Linux release, we include the latest packages possible. Key ones to point out this release are:

- [GNOME 3.36](https://pkg.kali.org/pkg/meta-gnome3) - a few of you may have noticed a bug that slipped in during the first 12 hours of the update being available. We’re sorry about this, and have measures in place for it to not happen again
- [Joplin](https://pkg.kali.org/pkg/joplin) - we are planning on replacing [CherryTree](https://pkg.kali.org/pkg/cherrytree) with this in Kali Linux 2020.3!
- [Nextnet](https://pkg.kali.org/pkg/nextnet)
- [Python 3.8](https://pkg.kali.org/pkg/python3-defaults)
- [SpiderFoot](https://pkg.kali.org/pkg/spiderfoot)

For the time being, as a temporary measure due to certain tools needing it, we have re-included python2-pip. Python 2 has now reached “[End Of Life](https://www.kali.org/blog/python-2-end-of-life/)” and is no longer getting updated. Tool makers, please, please, please port to Python 3. Users of tools, if you notice that a tool is not Python 3 yet, you can help too! It is not going to be around forever.

Whilst talking about packages, we have also started to refresh our package logos for each tool. You’ll notice them in the Kali Linux menu, as well as the tools page on [GitLab](https://gitlab.com/kalilinux/packages/) (more information on this coming soon!)

https://www.kali.org/blog/kali-linux-2020-2-release/images/release-2020.2-icons.png

If your tool has a logo and we have missed it, please let us know on the [bug tracker](https://bugs.kali.org/bug_report_page.php).

### WSLconfWSLconf happened earlier this year, and [Steev](https://gitlab.com/steev) gave a 35 minute talk on “[How We Use WSL at Kali](https://www.youtube.com/watch?v=f8m6tKErjAI)”. Go check it out!

### Behind the Scenes, Infrastructure ImprovementsWe have been celebrating the arrival of new servers, which over the last few weeks we have been migrating too. This includes a new ARM build server and what we use for [package testing](https://autopkgtest.kali.org/).

This may not be directly noticeable, but you may reap the benefits of it! If you are wanting to help out with Kali, we have added a new section to our documentation showing how to submit a [autopkgtest](https://www.kali.org/docs/development/contributing-runtime-tests/). Feedback is welcome!

### Kali NetHunterWe were so excited about some of the work that has been happening with NetHunter recently, we already did a [mid-term release](https://www.kali.org/blog/kali-nethunter-updates/) to showcase them and get it to you as quick as possible.

On top of all the previous NetHunter news there is even more to announce this time around!

- Nexmon support has been revived, bringing WiFi monitor support and frame injection to wlan0 on the Nexus 6P, Nexus 5, Sony Xperia Z5 Compact, and more!
- OpenPlus 3T images have been added to the download page.
- We have crossed [160 different kernels in our repository](https://nethunter.kali.org/device-kernels.html), allowing NetHunter to [support over 64 devices](https://nethunter.kali.org/kernels.html)! Yes, over 160 kernels and over 64 devices supported. Amazing.
- Our documentation page has [received a well deserved refresh](https://www.kali.org/docs/nethunter/), especially the kernel development section.

One of the most common questions to come in about NetHunter is “What device should I run it on?”. Keep your [eye on this page](https://nethunter.kali.org/images.html) to see what your options are on an automatically updated basis!

When you think about the amount of power NetHunter provides in such a compact package, it really is mind blowing. Its been amazing to watch this progress, and the entire Kali team is excited to show you what is coming in the future.

### Download Kali Linux 2020.2Fresh images
So what are you waiting for? Start [downloading](https://www.kali.org/get-kali/) already!

Seasoned Kali users are already aware of this, but for the ones who are not, we do also produce [weekly builds](https://cdimage.kali.org/kali-weekly/) that you can use as well. If you can’t wait for our next release and you want the latest packages when you download the image, you can just use the weekly image instead. This way you’ll have fewer updates to do. Just know these are automated builds that we don’t QA like we do our standard release images.

Existing Upgrades
If you already have an existing Kali installation, remember you can always do a quick update:

kali@kali:~$ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list
kali@kali:~$
kali@kali:~$ sudo apt update && sudo apt -y full-upgrade
kali@kali:~$
kali@kali:~$ [ -f /var/run/reboot-required ] && sudo reboot -f
kali@kali:~$

You should now be on Kali Linux 2020.2. We can do a quick check by doing:

kali@kali:~$ grep VERSION /etc/os-release
VERSION="2020.2"
VERSION_ID="2020.2"
VERSION_CODENAME="kali-rolling"
kali@kali:~$
kali@kali:~$ uname -v
#1 SMP Debian 5.5.17-1kali1 (2020-04-21)
kali@kali:~$
kali@kali:~$ uname -r
5.5.0-kali2-amd64
kali@kali:~$

NOTE: The output of uname -r may be different depending on the system [architecture](https://pkg.kali.org/pkg/linux-latest).

As always, should you come across any bugs in Kali, please submit a report on our [bug tracker](https://bugs.kali.org/main_page.php). We’ll never be able to fix what we don’t know is broken! And Twitter is not a Bug Tracker!
