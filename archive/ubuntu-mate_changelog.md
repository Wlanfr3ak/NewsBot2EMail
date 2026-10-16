# Changelog: Ubuntu MATE

Quelle: https://ubuntu-mate.org/blog/
Stand: 14.10.2026 21:34

---

## stonking-stingray – 2026-10-14

**Ubuntu MATE 26.10 Release Notes**

Lo and behold 👐, Ubuntu MATE 26.10 (Stonking Stingray) is here! 🎊 We are back 🦾 after a hiatus where the project skipped the 26.04 LTS release 🌥️ earlier this year.

This is the first official release from the [new circle of friends](https://discourse.ubuntu.com/t/hello-from-the-new-ubuntu-mate-maintainers-team/84246) 💚. I thank them all for their love and grit 🏋️ in seeing UM revive and thrive. Sincere thanks also to members of the larger Ubuntu community for their guidance ➡️ , patience 🧘 and support ⚓. Thanks also to our users 👥; their testing, feedback and good wishes played a part in shaping the release. And we intend to continue the ‘Tenacious’ efforts into the future.🦖

Ubuntu MATE 26.10 is a standard release (non-LTS) and will be supported for 9 months, until July 2027.

### What changed in Ubuntu MATE 26.10?

The team! 😇😉

Joking apart, in terms of new features, we must admit we could not complete upgrade of all of MATE packages to their latest released version even with our best efforts. The urgency with which we gathered and worked, the high standard of Debian packaging, overall quality process involved in a release and not to forget the challenges of balancing personal life, all weighed in.

On a positive note though, the available packages are stable 🏛️. Many bugs 🦟 were fixed by upstream. Some of those fixes 🛠️ have made it to the release and we are planning to backport others after the release.

As Ubuntu MATE builds on top of Ubuntu, please see the [Ubuntu 26.10 Release Notes](https://documentation.ubuntu.com/release-notes/26.10/) for details of all the changes and improvements.

### Known Issues:

-
    On the login screen, if we click on the password box, the password reveal/conceal (👁️) icon is broken ([LP 2169382](https://bugs.launchpad.net/ubuntu-mate/+bug/2169382)).

-
    During installation, if you choose manual installation, the installer creates the EFI partition automatically (and forcefully), even when you have created one manually. However, there is no issue when manually creating other partitions like /boot, /, /home etc. Workaround is to leave creation of EFI partition to the installer itself and only create other partitions. ([1572](https://github.com/canonical/ubuntu-desktop-provision/issues/1572))

-
    If you are a visually challenged user, the screen-reader installation has a quirk. On ‘Select your timezone’ slide, you cannot come out of ‘Timezone’ box with a ‘Tab’. It keeps looping and reads timezone info. As a workaround, press ‘Shift+Tab’ twice, to reach ‘Next’ button in reverse direction. From there the installation continues without issue. This affects all flavors using ‘subiquity’ installer ([1571](https://github.com/canonical/ubuntu-desktop-provision/issues/1571)).

-
    If you are testing on virtual machine, you may see an error pop-up saying, “Sorry, Ubuntu XX.YY has experienced an internal error.”, and if you click on ‘Show details’, it will (mostly) be /usr/bin/blueman-applet. There is no issue on bare-metal installs with bluetooth support.

-
    In live-session, ‘redshift’ application may not work. This is because, the location service has either not started or failed to start. There is no issue on an installed system (vm or bare-metal) as tested.

-
    In the installer, the links shown in ‘Join the community’ slide needs updating ([LP 2170678](https://bugs.launchpad.net/ubuntu/+source/ubuntu-mate-settings/+bug/2170678)).

### Other Changes:

There are some changes that may affect some UM users who rely on scripting and automation 🧙. If you are using any of the following packages, please check and adjust accordingly.

-
    We have migrated to dracut from initramfs-tools. While the update-initramfs -u command still works, specific options that you used may not be available any more.

-
    We have dropped ifupdown and embraced netplan fully. This had to be done because ifupdown was failing to bring ethernet devices in live-session (due to deprecated dhclient being hard-coded). This also means, there will be no pppoeconf package which pulls-in ifupdown.

-
    Latest version of gdebi is broken. It fails when we click on ‘Install’ and enter password. Instead of shipping it in non-functional state, we decided to drop it from the iso. We will work to fix the bug ([LP 2151797](https://bugs.launchpad.net/ubuntu/+source/gdebi/+bug/2151797)).

### Download Ubuntu MATE 26.10

    ### Download Ubuntu MATE 26.10

    Available for 64-bit desktop computers!

        [Download](https://ubuntu-mate.org/download/)

### Upgrading to Ubuntu MATE 26.10

For upgrading information, refer to the discourse topic “[Upgrading to Ubuntu MATE 26.10](https://discourse.ubuntu.com/t/upgrading-to-ubuntu-mate-26-10/89421)”.

NOTE: There are no offline upgrade options for Ubuntu MATE. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.

## plucky-puffin – 2025-04-15

**Ubuntu MATE 25.04 Release Notes**

This post is more than a year old and may be outdated.

                    Ubuntu MATE 25.04 is ready to soar! 🪽 Celebrating our 10th anniversary as an official Ubuntu flavour with the reliable MATE Desktop experience you love, built on the latest Ubuntu foundations. Read on to learn more 👓️

### A Decade of MATE

This release marks the 10th anniversary of Ubuntu MATE becoming an official Ubuntu flavour. From our humble beginnings, we’ve developed a loyal following of users who value a traditional desktop experience with modern capabilities. Thanks to our amazing community, contributors, and users who have been with us throughout this journey. Here’s to many more years of Ubuntu MATE! 🥂

### What changed in Ubuntu MATE 25.04?

Here are the highlights of what’s new in the Plucky Puffin release:

- Celebrating 10 years as an official Ubuntu flavour! 🎂

- Optional full disk encryption in the installer 🔐

      Enhanced advanced partitioning options

- Better interaction with existing BitLocker-enabled Windows installations

- Improved experience when installing alongside other operating systems

### Major Applications

Accompanying MATE Desktop 🧉 and Linux 6.14 🐧 are Firefox 137 🔥🦊,
Evolution 3.56 📧, LibreOffice 25.2.2 📚

See the [Ubuntu 25.04 Release Notes](https://discourse.ubuntu.com/t/plucky-puffin-release-notes/48687)
for details of all the changes and improvements that Ubuntu MATE benefits from.

    ### Download Ubuntu MATE 25.04

    Available for 64-bit desktop computers!

        [Download](https://ubuntu-mate.org/download/)

### Upgrading to Ubuntu MATE 25.04

The upgrade process to Ubuntu MATE 25.04 is the same as Ubuntu.

- [Ubuntu 25.04 Upgrade Process](https://help.ubuntu.com/community/PluckyUpgrades)

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.

## oracular-oriole – 2024-10-07

**Ubuntu MATE 24.10 Release Notes**

This post is more than a year old and may be outdated.

                    Ubuntu MATE 24.10 is more of what you like, stable MATE Desktop on top of current Ubuntu. Read on to learn more 👓️

Ubuntu MATE 24.10

### Thank you! 🙇

My sincere thanks to everyone who has played an active role in improving Ubuntu MATE for this release 👏
I’d like to acknowledge the close collaboration with the Ubuntu Foundations team and the Ubuntu flavour teams, in particular [Erich Eickmeyer](https://launchpad.net/~eeickmeyer) who pushed critical fixes while I was travelling.
Thank you! 💚

### What changed since the Ubuntu MATE 24.04 LTS?

Here are the highlights of what’s changed since the [release of Ubuntu MATE 24.04](https://ubuntu-mate.org/blog/ubuntu-mate-noble-numbat-release-notes/)

- Ships stable [MATE Desktop](https://mate-desktop.org) 1.26.2 with a handful of bug fixes 🐛

- Switched back to Slick Greeter (replacing Arctica Greeter) due to race-condition in the boot process which results the display manager failing to initialise.

      Returning to Slick Greeter reintroduces the ability to easily configure the login screen via a graphical application, something users have been requesting be re-instated 👍

- Ubuntu MATE 24.10 .iso 📀 is now 3.3GB 🤏 Down from 4.1GB in the 24.04 LTS release.

      This is thanks to some fixes in the installer that no longer require as many packages in the live-seed.

Login Window

### What didn’t change since the Ubuntu MATE 24.04 LTS?

If you follow upstream MATE Desktop development, then you’ll have noticed that Ubuntu MATE 24.10 doesn’t ship with the recently released MATE Desktop 1.28 🧉

I have prepared packaging for MATE Desktop 1.28, along with the associated components but encountered some bugs and regressions 🐞 I wasn’t able to get things to a standard I’m happy to ship be default, so it is tried and true MATE 1.26.2 one last time 🪨

### Major Applications

Accompanying MATE Desktop 1.26.2 🧉 and Linux 6.11 🐧 are Firefox 131 🔥🦊,
Celluloid 0.27 🎥, Evolution 3.54 📧, LibreOffice 24.8.2 📚

See the [Ubuntu 24.10 Release Notes](https://discourse.ubuntu.com/t/oracular-oriole-release-notes/44878/1)
for details of all the changes and improvements that Ubuntu MATE benefits from.

    ### Download Ubuntu MATE 24.10

    Available for 64-bit desktop computers!

        [Download](https://ubuntu-mate.org/download/)

### Upgrading to Ubuntu MATE 24.10

The upgrade process to Ubuntu MATE 24.10 is the same as Ubuntu.

- [Ubuntu 24.10 Upgrade Process](https://help.ubuntu.com/community/OracularUpgrades)

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.

## noble-numbat – 2024-04-23

**Ubuntu MATE 24.04 LTS Release Notes**

This post is more than a year old and may be outdated.

                    Ubuntu MATE 24.04 is more of what you like, stable MATE Desktop on top of current Ubuntu.
This release rolls up some fixes and more closely aligns with Ubuntu. Read on to learn more 👓️

Ubuntu MATE 24.04 LTS

### Thank you! 🙇

I’d like to extend my sincere thanks to everyone who has played an active role in improving Ubuntu MATE for this release 👏
I’d like to acknowledge the close collaboration with all the Ubuntu flavour teams and the Ubuntu Foundations and Desktop Teams.
The assistance and support provided by [Erich Eickmeyer](https://launchpad.net/~eeickmeyer) (Ubuntu Studio), [Simon Quigley](https://launchpad.net/~tsimonq2) (Lubuntu) and [David Muhammed](https://launchpad.net/~fossfreedom) (Ubuntu Budgie) have been invaluable.
Thank you! 💚

### What changed since the Ubuntu MATE 23.10?

Here are the highlights of what’s changed since the [release of Ubuntu MATE 23.10](https://ubuntu-mate.org/blog/ubuntu-mate-mantic-minotaur-release-notes/)

- Ships stable [MATE Desktop](https://mate-desktop.org) 1.26.2 with a selection of bug fixes 🐛 and minor improvements 🩹 to associated components.

- Integrated the new ✨ [Ubuntu Desktop Bootstrap](https://snapcraft.io/ubuntu-desktop-bootstrap) installer 📀

- Added [GNOME Firmware](https://gitlab.gnome.org/World/gnome-firmware), that replaces [Firmware Updater](https://snapcraft.io/firmware-updater).

- Added [App Center](https://snapcraft.io/snap-store), that replaces Software Boutique.

- Retired Ubuntu MATE Welcome; although it is still available for Ubuntu MATE 23.10 and earlier.

### Major Applications

Accompanying MATE Desktop 1.26.2 🧉 and Linux 6.8 🐧 are Firefox 125 🔥🦊,
Celluloid 0.26 🎥, Evolution 3.52 📧, LibreOffice 24.2.2 📚

See the [Ubuntu 24.04 Release Notes](https://discourse.ubuntu.com/t/noble-numbat-release-notes/39890)
for details of all the changes and improvements that Ubuntu MATE benefits from.

    ### Download Ubuntu MATE 24.04

    Available for 64-bit desktop computers!

        [Download](https://ubuntu-mate.org/download/)

### Upgrading to Ubuntu MATE 24.04

The upgrade process to Ubuntu MATE 24.04 LTS from either Ubuntu MATE 22.04 LTS or
23.10 is the same as Ubuntu.

- [Ubuntu 24.04 Upgrade Process](https://help.ubuntu.com/community/NobleUpgrades)

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.

## mantic-minotaur – 2023-09-25

**Ubuntu MATE 23.10 Release Notes**

This post is more than a year old and may be outdated.

                    Ubuntu MATE 23.10 is more of what you like, stable MATE Desktop on top of current Ubuntu.
This release rolls up a number of bugs fixes and updates that continues to build on recent releases, where the focus has been on improving stability 🪨

Ubuntu MATE 23.10

### Thank you! 🙇

I’d like to extend my sincere thanks to everyone who has played an active role in improving Ubuntu MATE for this release 👏 From reporting bugs, submitting translations, providing patches, contributing to [our crowd-funding](https://www.patreon.com/ubuntu_mate), developing new features, creating artwork, offering community support, actively
testing and providing QA feedback to writing documentation or creating this fabulous website. Thank you! 💚

### What changed since the Ubuntu MATE 23.04?

Here are the highlights of what’s changed since the [release of Ubuntu MATE 23.04](https://ubuntu-mate.org/blog/ubuntu-mate-lunar-lobster-release-notes/)

#### MATE Desktop

[MATE Desktop](https://mate-desktop.org) has been updated to 1.26.2 with a selection of bugs fixes 🐛 and minor improvements 🩹 to associated components.

-
caja-rename 23.10.1-1 has been ported from Python to C.

-
libmatemixer 1.26.0-2+deb12u1 resolves heap corruption and application crashes when removing USB audio devices.

-
mate-desktop 1.26.2-1 improves portals support.

-
mate-notification-daemon 1.26.1-1 fixes several memory leaks.

-
mate-system-monitor 1.26.0-5 now picks up libexec files from /usr/libexec

-
mate-session-manager 1.26.1-2 set LIBEXECDIR to /usr/libexec/ for correct interaction with mate-system-monitor ☝️

-
mate-user-guide 1.26.2-1 is a new upstream release.

-
mate-utils 1.26.1-1 fixes several memory leaks.

##### Yet more AI Generated wallpaper

My friend [Simon Butcher](https://twitter.com/simonjbutcher) 🇬🇧 is Head of Research Platforms at Queen Mary University of London managing the Apocrita HPC cluster service. Once again, Simon has created a stunning AI-generated 🤖🧠 wallpaper for Ubuntu MATE using bleeding edge diffusion models 🖌 The sample below is 1920x1080 but the version included in Ubuntu MATE 23.10 are 3840x2160.

Here’s what Simon has to say about the process of creating this new wallpaper for Mantic Minotaur:

  Since Minotaurs are imaginary creatures, interpretations tend to vary widely. I wanted to produce an image of a powerful creature in a graphic novel style, although not gruesome like many depictions. The latest open source Stable Diffusion XL base model was trained at a higher resolution and the difference in quality has been noticeable, particularly at better overall consistency and detail, while reducing anatomical irregularities in images. The image was produced locally using Linux and an NVIDIA A100 80GB GPU, starting from an initial text prompt and refined using img2img, inpainting and upscaling features.

### Major Applications

Accompanying MATE Desktop 1.26.2 🧉 and Linux 6.5 🐧 are Firefox 118 🔥🦊,
Celluloid 0.25 🎥, Evolution 3.50 📧, LibreOffice 7.6.1 📚

See the [Ubuntu 23.10 Release Notes](https://discourse.ubuntu.com/t/mantic-minotaur-release-notes/35534)
for details of all the changes and improvements that Ubuntu MATE benefits from.

    ### Download Ubuntu MATE 23.10

    Available for 64-bit desktop computers!

        [Download](https://ubuntu-mate.org/download/)

### Upgrading from Ubuntu MATE 23.04

You can upgrade to Ubuntu MATE 23.10 from Ubuntu MATE 23.04. Ensure that you
have all updates installed for your current version of Ubuntu MATE before you
upgrade.

- Open the “Software & Updates” from the Control Center.

- Select the 3rd Tab called “Updates”.

- Set the “Notify me of a new Ubuntu version” drop down menu to “For any new version”.

- Press Alt+F2 and type in update-manager -c -d into the command box.

- Update Manager should open up and tell you: New distribution release ‘23.10’ is available.

      If not, you can use /usr/lib/ubuntu-release-upgrader/check-new-release-gtk

- Click “Upgrade” and follow the on-screen instructions.

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.

### Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).

## lunar-lobster – 2023-04-20

**Ubuntu MATE 23.04 Release Notes**

This post is more than a year old and may be outdated.

                    Ubuntu MATE 23.04 is the least exciting Ubuntu MATE release ever. The good news is, if you liked Ubuntu MATE 22.10 then it is more of the same; just with better artwork! 🖌️🖼️ I entered this development cycle full of energy and enthusiasm off the back of the [Ubuntu Summit in Prague](https://ubuntu.com/blog/ubuntu-summit-2022-reflections), but then I was seriously ill 🤒 and had a long stay in hospital. I’m recovering well and should be 100% in a couple of months. This setback and also changing jobs a couple of months ago has meant that I’ve not been able to invest the usual time and effort into Ubuntu MATE. I’m happy to say that I’ve been able to deliver another solid 🪨 release with the help of the Ubuntu community.

### Thank you! 🙇

**I’d like to extend my sincere thanks to everyone who has played an active role in improving Ubuntu MATE for this release 👏 From reporting bugs, submitting translations, providing patches, contributing to [our crowd-funding](https://www.patreon.com/ubuntu_mate), developing new features, creating artwork, offering community support, actively
testing and providing QA feedback to writing documentation or creating this fabulous website. Thank you! 💚

### What changed since the Ubuntu MATE 22.10?

Here are the highlights of what’s changed since the [release of Ubuntu MATE 22.10](https://ubuntu-mate.org/blog/ubuntu-mate-kinetic-kudu-release-notes/)

#### MATE Desktop

Both [MATE Desktop](https://mate-desktop.org) and
[Ayatana Indicators](https://github.com/AyatanaIndicators) have seen some version bumps that fix 🩹 an assortment of minor bugs 🐛

##### AI Generated wallpapers (yet again!)

My friend [Simon Butcher](https://twitter.com/simonjbutcher) 🇬🇧 is Head of Research Platforms at Queen Mary University of London managing the Apocrita HPC cluster service. Once again, Simon has created **some stunning **AI-generated 🤖🧠 ** for Ubuntu MATE using bleeding edge diffusion models** 🖌 The samples below are 1920x1080 but the versions included in Ubuntu MATE 23.04 are 3840x2160.

Here’s what Simon has to say about the process of creating these new wallpapers for Lunar Lobster:

  My usual workflow involves checking reddit, etc for the latest techniques, and then installing the latest open-source tools and checkpoints for unlimited experimentation (e.g. stable diffusion), plus some selective use of Dall-e and Midjourney, while trying not to exhaust my credits. I then experiment with lot of different prompts (including negative prompts to discourage certain features), settings, styles and ideas from each tool to see what sort of images I can get, then tweak and evolve my approach based on the results.

  Lobsters are fascinating creatures, but in real life, I find them a bit ugly, with all those antennae and legs akimbo. For the theme of “Lunar Lobster”, rather precise anatomy, I explored ideas of stylised alien robotic space lobsters, lunar landers and other lobster-themed spacecraft. After a producing a shortlist of varied images, I then perform any necessary AI processing such as inpainting, outpainting (generating new parts of an image beyond the existing canvas - particularly useful for getting the correct aspect ratio) and AI upscaling to make them suitable for use as wallpaper.

#### Flatpak

[Flatpak is no longer installed by default](https://discourse.ubuntu.com/t/ubuntu-flavor-packaging-defaults/34061), but can still be installed should you want to use it.

#### PipeWire

As a [podcaster](https://linuxdowntime.com/) and [streamer](https://twitch.tv/WimpysWorld) I’m delighted to have PipeWire installed by default since Ubuntu MATE 22.10. The Ubuntu MATE meta packages have been updated to correctly install the revised pipewire packages in Ubuntu. Special thanks to Erich Eickmeyer, from the Ubuntu Studio project, for his work on this.

### Major Applications

Accompanying MATE Desktop 1.26.1 🧉 and Linux 6.20 🐧 are Firefox 111 🔥🦊,
Celluloid 0.20 🎥, Evolution 3.48 📧, LibreOffice 7.5.2 📚

See the [Ubuntu 23.04 Release Notes](https://discourse.ubuntu.com/t/lunar-lobster-release-notes/31910)
for details of all the changes and improvements that Ubuntu MATE benefits from.

    ### Download Ubuntu MATE 23.04

    Available for 64-bit desktop computers!

        [Download](https://ubuntu-mate.org/download/)

### Upgrading from Ubuntu MATE 22.10

You can upgrade to Ubuntu MATE 23.04 from Ubuntu MATE 22.10. Ensure that you
have all updates installed for your current version of Ubuntu MATE before you
upgrade.

- Open the “Software & Updates” from the Control Center.

- Select the 3rd Tab called “Updates”.

- Set the “Notify me of a new Ubuntu version” drop down menu to “For any new version”.

- Press Alt+F2 and type in update-manager -c -d into the command box.

- Update Manager should open up and tell you: New distribution release ‘23.04’ is available.

      If not, you can use /usr/lib/ubuntu-release-upgrader/check-new-release-gtk

- Click “Upgrade” and follow the on-screen instructions.

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.

### Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).

## kinetic-kudu – 2022-09-29

**Ubuntu MATE 22.10 Release Notes**

This post is more than a year old and may be outdated.

                    Ubuntu MATE 22.10 is a modest update by recent standards and focused on “quality
of life improvements”. And there is good reason why this release of Ubuntu MATE
doesn’t feature the usual bucket 🪣 list of changes you’d typically expect, and
that’s because I’ve been helping bring the full Ubuntu MATE experience to Debian
MATE 🧉

This may raise some questions for Ubuntu MATE users, so let’s try and address them:

-
I’m not stepping away from Ubuntu or Ubuntu MATE. I will continue to use and develop Ubuntu MATE 👍

- I’ve closely collaborated with the MATE packaging team for Debian for over 8 years 👴

- Making the MATE experience in Debian and Ubuntu consistent makes maintenance easier for all involved 🛠

- Ubuntu MATE offers some modernisation of MATE via home-grown apps such as MATE Tweak and Ayatana Indicators. We want Debian users to benefit from those improvements too 💖

- We’re hopeful the MATE spin in Debian 12 will offer the same (or extremely similar) experience Ubuntu MATE users have enjoyed for some time 🎁

### Thank you! 🙇

I’d like to extend my sincere thanks to everyone who has played an active role
in improving Ubuntu MATE for this release 👏 From reporting bugs,
submitting translations, providing patches, contributing to
[our crowd funding](https://www.patreon.com/ubuntu_mate),
developing new features, creating artwork, offering community support, actively
testing and providing QA feedback to writing documentation or creating this
fabulous website. Thank you! Thank you all for getting out there and making a
difference! 💚

Ubuntu MATE 22.10 using the Pantheon layout and new centered panel applets and HUD

### What changed since the Ubuntu MATE 22.04?

Here are the highlights of what’s changed since the [release of Ubuntu MATE 22.04](https://ubuntu-mate.org/blog/ubuntu-mate-jammy-jellyfish-release-notes/)

#### MATE Desktop

The usual point release updates to [MATE Desktop](https://mate-desktop.org) and
[Ayatana Indicators](https://github.com/AyatanaIndicators) have been included
that fix 🩹 an assortment on minor bugs 🐛 The main change in MATE Desktop
is to MATE Panel, where we’ve included an early snapshot release of mate-panel
1.27.0 along with a patch set that adds centre alignment of panel applets.

This much requested feature comes from Ubuntu MATE community contributor
[Gordon N. Squash](https://github.com/thesquash) 🇺🇸 and allows panel applets to
be centre aligned, as well as the usual left and right alignment. I’m sure
you’ll all join me in thanking 🙇 Gordon for working on this feature.

Centre aligning of applet icons will ship with MATE Desktop 1.28, but we’re
including it early 🐓 for Ubuntu MATE users. We’ve updated MATE Tweak to
correctly save/restore custom layouts that use centre aligned applets and all
the panel layouts shipped with Ubuntu MATE 22.10 have been updated so they’re
compatible with center alignment of applets ✅

##### AI Generated wallpapers (again!)

My friend [Simon Butcher](https://twitter.com/simonjbutcher) 🇬🇧 is Head of
Research Platforms at Queen Mary University of London managing the Apocrita HPC
cluster service. Once again, Simon has created some stunning AI generated 🤖🧠
wallpapers for Ubuntu MATE using bleeding edge diffusion models 🖌 The samples
below are 1920x1080 but the versions include in Ubuntu MATE 22.10 are 3840x2160.

Here’s what Simon has to say about about some of the challenges he faced
creating these new wallpapers for Kinetic Kudu:

  AI image generation is continuing to improve at a mind-boggling rate. Yet, until recently, coherent human faces, hands and anatomically correct animals have proved rather tricky. Fortunately human faces are getting particular attention in the open source community after the release of Stable Diffusion. However, while an anthropomorphic portrait of a Kudu wearing a rather dapper suit will be stylishly rendered, getting consistent results for kudu in their natural habitat proved particularly tricky, exacerbated by their elegant horn structure. Often you will get rather wild interpretations of the horns, 5 legged creatures, or nightmarish output akin to the Pushmi-Pullyu from the Dr Doolittle stories.

AI-generated kudu are hard. They are happy posing for their portrait in a suit, but as soon as you want them to act normal, you get abominations like this double-headed beastie [#stablediffusion](https://twitter.com/hashtag/stablediffusion?src=hash&ref_src=twsrc%5Etfw) [https://t.co/BgPR3QBqru](https://t.co/BgPR3QBqru) [pic.twitter.com/RVCbgMsOAh](https://t.co/RVCbgMsOAh)

— Simon Butcher (@simonjbutcher) [September 21, 2022](https://twitter.com/simonjbutcher/status/1572574722612920322?ref_src=twsrc%5Etfw)

  Jellyfish, on the other hand, are a mass of tentacles and perhaps benefit aesthetically from the randomness induced by AI-generated images, in the same way that forests, mountains and hobbit villages generated by AI can be produced en-masse to a very satisfying extent. So while 1000 stunning unique images of jellyfish can be produced in a few minutes with a powerful GPU, the kudu was quite a challenge, and I had to experiment a lot with various prompts and styles, and a lot of cherry-picking - throwing away about 99% of the results that weren’t quite right. For the next release, I’m hoping we’ll see further AI innovation in time for the next release, or…maybe the next code name will be a lionfish?

#### PipeWire

PulseAudio has been replaced with PipeWire and Bluetooth audio codec support
has been expanded with the addition of AAC, LDAC, aptX and aptX HD.

As a [podcaster](https://linuxdowntime.com/) and [streamer](https://twitch.tv/WimpysWorld)
I’m delighted to have PipeWire installed by default in Ubuntu MATE 22.10. The
migration to PipeWire has resolved some longstanding minor annoyances I’ve had
with audio in that past and all the tools 🧰 I use for audio and video
production continue to function correctly.

##### PipeWire on Ubuntu MATE 22.04

If you like to ride the LTS train 🚆 but want to use PipeWire in Ubuntu MATE
22.04 (as I have been doing for some months) then this is how to make the
change:

sudo apt-get install gstreamer1.0-pipewire pipewire-audio-client-libraries wireplumber
sudo apt-get remove pulseaudio-module-bluetooth
sudo apt-get install libfdk-aac2 libldacbt-abr2 libldacbt-enc2 libopenaptx0 libspa-0.2-bluetooth libspa-0.2-jack

Once the installs/removals are complete restart your computer.

#### Ubuntu MATE Stuff

The “MATE HUD” has seen some significant work from community contributor
[twa022](https://github.com/twa022) 🌎. The HUD now supports MATE, XFCE
and Budgie, has improved accuracy for HUD placement (taking into account various
panel offsets/struts), is highly configurable and includes a new HUD settings app ✨

HUD Settings

##### MATE User Manager

A new utility, User Manager, has been added to complement the suite of MATE
tools. User Manager replaces the aging gnome-system-tools which was
removed from Ubuntu MATE in the 22.04 release and allows you to add/modify/remove
user accounts. It also includes the ability to define which users are Administrators,
enable/disable auto-login, set profile images and manage group memberships.

MATE User Manager

##### Yaru

And last but not least, the Ubuntu MATE Artwork package has been updated to
include all the refinements and improvements in the suite of
[Yaru](https://github.com/ubuntu/yaru) themes 🎨

### Major Applications

Accompanying MATE Desktop 1.26.1 🧉 and Linux 5.19 🐧 are Firefox 105 🔥🦊,
Celluloid 0.20 🎥, Evolution 3.46 📧, LibreOffice 7.4 📚

See the [Ubuntu 22.10 Release Notes](https://discourse.ubuntu.com/t/kinetic-kudu-release-notes/27976)
for details of all the changes and improvements that Ubuntu MATE benefits from.

    ### Download Ubuntu MATE 22.10

    This new release will be first available for PC/Mac users.

        [Download](https://ubuntu-mate.org/download/)

### Upgrading from Ubuntu MATE 22.04

You can upgrade to Ubuntu MATE 22.10 from Ubuntu MATE 22.04. Ensure that you
have all updates installed for your current version of Ubuntu MATE before you
upgrade.

- Open the “Software & Updates” from the Control Center.

- Select the 3rd Tab called “Updates”.

- Set the “Notify me of a new Ubuntu version” drop down menu to “For any new version”.

- Press Alt+F2 and type in update-manager -c -d into the command box.

- Update Manager should open up and tell you: New distribution release ‘22.10’ is available.

      If not, you can use /usr/lib/ubuntu-release-upgrader/check-new-release-gtk

- Click “Upgrade” and follow the on-screen instructions.

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.

### Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).

## jammy-jellyfish – 2022-03-29

**Ubuntu MATE 22.04 LTS Release Notes**

This post is more than a year old and may be outdated.

                    Ubuntu MATE 22.04 LTS is the culmination of 2 years of continual improvement 😅
to Ubuntu and MATE Desktop. As is tradition, the LTS development cycle has a
keen focus on eliminating paper 🧻 cuts 🔪 but we’ve jammed in some new
features and a fresh coat of paint too 🖌 The following is a summary of what’s
new [since Ubuntu MATE 21.10](https://ubuntu-mate.org/blog/ubuntu-mate-impish-indri-final-release/) and
some reminders of how we got here from 20.04. Read on to learn more 🧑‍🎓

### Thank you! 🙇

I’d like to extend my sincere thanks to everyone who has played an active role
in improving Ubuntu MATE for this LTS release 👏 From reporting bugs,
submitting translations, providing patches, contributing to our crowd funding,
developing new features, creating artwork, offering community support, actively
testing and providing QA feedback to writing documentation or creating this
fabulous website. Thank you! Thank you all for getting out there and making a
difference! 💚

Ubuntu MATE 22.04 LTS (Jammy Jellyfish) - Mutiny layout with Yark-MATE-dark

### What’s changed?

Here are the highlights of what’s changed recently.

#### MATE Desktop 1.26.1 🧉

Ubuntu MATE 22.04 features MATE Desktop 1.26.1. MATE Desktop 1.26.0 was introduced
in 21.10 and benefits from significant effort 😅 in fixing bugs 🐛
in MATE Desktop, optimising performance ⚡ and plugging memory leaks. MATE
Desktop 1.26.1 addresses the bugs we discovered following the initial 1.26.0
release. Our community also fixed some bugs in Plank and Brisk Menu 👍 and also
fixed the screen reader during installs for visually impaired users 🥰 In all
over 500 bugs have been addressed in this release 🩹

#### Yaru 🎨

Ubuntu MATE 21.04 was the first release to ship with a MATE variant of the
[Yaru theme](https://github.com/ubuntu/yaru). A year later and we’ve been working
hard with members of the Yaru and Ubuntu Desktop teams to bring full MATE
compatibility to upstream Yaru, including all the accent colour varieties.
All reported bugs 🐞 in the Yaru implementation for MATE have also been fixed 🛠

Yaru Themes in Ubuntu MATE 22.04 LTS

Ubuntu MATE 22.04 LTS ships with all the Yaru themes, including our own “chelsea
cucumber” version 🥒 The legacy Ambiant/Radiant themes are no longer
installed by default and neither are the stock MATE Desktop themes. We’ve added
an automatic settings migration to transition users who upgrade to an
appropriate Yaru MATE theme.

##### Cherries on top 🍒

In collaboration with [Paul Kepinski](https://github.com/Jupi007) 🇫🇷 (Yaru team)
and [Marco Trevisan](https://twitter.com/3v1n0) 🇮🇹 (Ubuntu Desktop
team) we’ve added dark/light panels and panel icons to Yaru for MATE Desktop
and Unity. I’ve added a collection of new dark/light panel icons to Yaru for
popular apps with indicators such as Steam, Dropbox, [uLauncher](https://ulauncher.io/),
[RedShift](http://jonls.dk/redshift/), [Transmission](https://transmissionbt.com/),
Variety, etc.

Light and Dark panels

I’ve added patches 🩹 to the Appearance Control Center that applies theme
changes to Plank (the dock), Pluma (text editor) and correctly toggles the
colour scheme preference for GNOME 42 apps. When you choose a dark theme,
everything will go dark in unison 🥷 and vice versa.

So, Ubuntu MATE 22.04 LTS is now using everything Yaru/Suru has to offer. 🎉

##### AI Generated wallpapers

My friend [Simon Butcher](https://twitter.com/simonjbutcher) 🇬🇧 is Head of
Research Platforms at Queen Mary University of London managing the Apocrita HPC
cluster service. He’s been creating AI 🤖 generated art using bleeding edge
CLIP guided diffusion models 🖌 The results are pretty incredible and we’ve
[included the 3 top voted “Jammy Jellyfish” in our wallpaper selection](https://twitter.com/m_wimpress/status/1504030749451862026)
as their vivid and vibrant styles compliment the Yaru accent colour theme options
very nicely indeed 😎

If you want the complete set, here’s a tarball  of all 8 wallpapers at 3840x2160:

-
[AI Generated “Jammy Jelly” by Simon Butcher](https://people.ubuntu.com/~flexiondotorg/Jammy_Jellyfish_AI_Wallpapers.tar.xz) 🎁 (22MB)

#### Ubuntu MATE stuff 🧉

Ubuntu MATE has a few distinctive apps and integrations of it’s own, here’s a
run down of what’s new and shiny ✨

##### MATE Tweak

Switching layouts with MATE Tweak is its most celebrated feature. We’ve improved
the reliability of desktop layout switching and restoring custom layouts is now 100%
accurate 💯

Having your desktop your way in Ubuntu MATE

We’ve removed mate-netbook from the default installation of Ubuntu MATE and
as a result the Netbook layout is no longer available. We did this because
mate-maximus, a component of mate-netbook, is the cause of some
compatibility issues with client side decorated (CSD) windows. There are still
several panel layouts that offer efficient resolution use 📐 for those who need
it.

MATE Tweak has refreshed its supported for 3rd party compositors. Support for
Compton has been dropped, as it is no longer actively maintained and
comprehensive support for [picom](https://github.com/yshui/picom) has been added.
picom has three compositor options: Xrender, GLX and Hybrid. All three are
can be selected via MATE Tweak as the performance and compatibility of each
varies depending on your hardware. Some people choose to use picom because
they get better gaming performance or screen tearing is reduced. Some just
like subtle animation effects picom adds 💖

##### MATE HUD

Recent versions of rofi, the tool used by MATE HUD to visualise menu
searches, has a new theme system. MATE HUD has been updated to support this
new theme engine and comes with two MATE specific themes (mate-hud and
mate-hud-rounded) that automatically adapt to match the currently selected
GTK theme.

You can add your own rofi themes to ~/.local/share/rofi/themes. Should you
want to, you can use any rofi theme in MATE HUD. Use Alt + F2
to run rofi-theme-selector to try out the different themes, and if there is
one you prefer you can set it as default by using running the following in a terminal:

gsettings set org.mate.hud rofi-theme <theme name>

MATE HUD uses the new rofi theme engine

##### Windows & Shadows

I’ve updated the Metacity/Marco (the MATE Window Manager) themes in Yaru to make
sure they match GNOME/CSD/Handy windows for a consistent look and feel across
all window types 🪟 and 3rd party compositors like picom. I even patched how
Marco and picom render shadows so windows they look cohesive regardless of
toolkit or compositor being used.

##### Ubuntu MATE Welcome & Boutique

The Software Boutique has been restocked with software for 22.04 and
Firefox 🔥🦊 ESR (.deb) has been added to the Browser Ballot in Ubuntu MATE Welcome.

Comprehensive browser options just a click away

#### 41% less fat 🍩

Ubuntu MATE, like it’s lead developer, was starting to get a bit large
around the mid section 😊 During the development of 22.04, the image 📀 got
to 4.1GB 😮

So, we put Ubuntu MATE on a strict diet 🥗  We’ve removed the proprietary NVIDIA
drivers from the local apt pool on the install media and thanks to migrating
fully to Yaru (which now features excellent de-duplication of icons) and also
removing our legacy themes/icons. And now the Yaru-MATE themes/icons are
completely in upstream Yaru, we were able to remove 3 snaps from the default
install and the image is now a much more reasonable 2.7GB; 41% smaller. 🗜

This is important to us, because the majority of our users are in countries
where Internet bandwidth is not always plentiful. Those of you with NVIDIA GPUs,
don’t worry. If you tick the 3rd party software and drivers during the install
the appropriate driver for your GPU will be downloaded and installed 👍

NVIDIA GPU owners should tick Install 3rd party software and drivers during install

While investigating 🕵 [a bug in Xorg Server that caused Marco (the MATE window manager)
to crash](https://pad.lv/1959995) we discovered that Marco has lower frame time
latency ⏱ when using Xrender with the NVIDIA proprietary drivers. We’ve
published a PPA where NVIDIA GPU users can install a version of Marco that uses
Xpresent for optimal performance ⚡

sudo apt-add-repository ppa:ubuntu-mate-dev/marco
sudo apt upgrade

Should you want to revert this change you install ppa-purge and run the
following from a terminal: sudo ppa-purge -o ubuntu-mate-dev -p marco.

##### But wait! There’s more! 😲

These reductions in size are after we added three new applications to the default
install on Ubuntu MATE: GNOME Clocks, Maps and Weather My family and I 👨‍👩‍👧 have
found these applications particularly useful and use them regularly on our
laptops without having to reach for a phone or tablet.

New additions to the default desktop application in Ubuntu MATE 22.04 LTS

For those of you who like a minimal base platform, then the minimal install
option is still available which delivers just the essential Ubuntu MATE Desktop
and Firefox browser. You can then build up from there 👷

##### Packages, packages, packages 📦

It doesn’t matter how you like to consume your Linux 🐧 packages, Ubuntu MATE
has got you covered with PPA, Snap, AppImage and FlatPak support baked in
by default. You’ll find flatpak, snapd and xdg-desktop-portal-gtk to
support Snap and FlatPak and the (ageing) libfuse2 to support AppImage are all
pre-installed.

Although flatpak is installed, [FlatHub](https://flathub.org/home) is not
enabled by default. To enable FlatHub run the following in a terminal:

flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

We’ve also included snapd-desktop-integration which provides a bridge
between the user’s session and snapd to integrate theme preferences 🎨 with
snapped apps and can also automatically install snapped themes 👔
All the Yaru themes shipped in Ubuntu MATE are fully snap aware.

#### Ayatana Indicators

Ubuntu MATE 20.10 transitioned to [Ayatana Indicators](https://github.com/AyatanaIndicators) 🚥
As a quick refresher, Ayatana Indicators are a fork of Ubuntu Indicators that
aim to be cross-distro compatible and re-usable for any desktop environment 👌

Ubuntu MATE 22.04 LTS comes with Ayatana Indicators 22.2.0 and sees the
return of Messages Indicator 📬 to the default install. Ayatana Indicators now
provide improved backwards compatibility to Ubuntu Indicators and no longer
requires the installation of two sets of libraries, saving RAM, CPU cycles and
improving battery endurance 🔋

Ayatana Indicators Settings

To compliment the BlueZ 5.64 protocol stack in Ubuntu, Ubuntu MATE ships
Blueman 2.2.4 which offers comprehensive management of Bluetooth devices and
much improved pairing compatibility 💙🦷

I also patched mate-power-manager, ayatana-indicator-power and Yaru to add
support for battery powered gaming input devices, such as controllers 🎮 and joysticks 🕹

#### Active Directory

And in case you missed it, the Ubuntu Desktop team added the option to enroll
your computer into an Active Directory domain 🔑 during install. Ubuntu MATE
has supported the same capability since it was first made available in the
20.10 release.

#### Raspberry Pi image 🥧

- Should be available very shortly after the release of 22.04.

#### Major Applications

Accompanying MATE Desktop 1.26.1 and Linux 5.15 are Firefox 99.0,
Celluloid 0.20, Evolution 3.44 & LibreOffice 7.3.2.1

See the [Ubuntu 22.04 Release Notes](https://discourse.ubuntu.com/t/jammy-jellyfish-release-notes/24668)
for details of all the changes and improvements that Ubuntu MATE benefits from.

    ### Download Ubuntu MATE 22.04 LTS

    This new release will be first available for PC/Mac users.

        [Download](https://ubuntu-mate.org/download/)

### Upgrading from Ubuntu MATE 20.04 LTS and 21.10

You can upgrade to Ubuntu MATE 22.04 LTS from Ubuntu MATE either 20.04 LTS or
21.10. Ensure that you have all updates installed for your current version of
Ubuntu MATE before you upgrade.

- Open the “Software & Updates” from the Control Center.

- Select the 3rd Tab called “Updates”.

- Set the “Notify me of a new Ubuntu version” drop down menu to “For long-term support versions” if you are using 20.04 LTS; set it to “For any new version” if you are using 21.10.

- Press Alt+F2 and type in update-manager -c -d into the command box.

- Update Manager should open up and tell you: New distribution release ‘XX.XX’ is available.

      If not, you can use /usr/lib/ubuntu-release-upgrader/check-new-release-gtk

- Click “Upgrade” and follow the on-screen instructions.

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.

### Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).

## groovy-gorilla – 2020-10-22

**Ubuntu MATE 20.10 Release Notes**

This post is more than a year old and may be outdated.

                    The releases following an LTS are always a good time ⌚ to make changes the set
the future direction 🗺️ of the distribution with an eye on where we want to be for
the next LTS release. Therefore, Ubuntu MATE 20.10 ships with that latest MATE
Desktop 1.24.1, keeps paces with other developments within Ubuntu (such as
Active Directory authentication) and migrated to the Ayatana Indicators project.

If you want bug fixes , kernel updates , a new web camera control ,
and a new indicator  experience, then 20.10 is for you . Ubuntu MATE 20.10
will be supported for 9 months until July 2021. If you need Long Term
Support, we recommend you use Ubuntu MATE 20.04 LTS.

Read on to learn more…

Ubuntu MATE 20.10 (Groovy Gorilla)

### What’s changed since Ubuntu MATE 20.04?

#### MATE Desktop

If you follow the [Ubuntu MATE twitter account](https://twitter.com/ubuntu_mate) 🐦
you’ll know that MATE Desktop 1.24.1 was recently released. Naturally Ubuntu
MATE 20.10 features that maintenance release of MATE Desktop. In addition, [we
have prepared updated MATE Desktop 1.24.1 packages for Ubuntu MATE 20.04](https://pad.lv/1891891)
that are currently in the SRU process. Given the number of MATE packages being
updated in 20.04, it might take some time ⏳ for all the updates to land, but
we’re hopeful that the fixes and improvements from MATE Desktop 1.24.1 will
soon be available for those of you running 20.04 LTS 👍

#### Active Directory

The Ubuntu Desktop team added the option to enroll your computer into an
Active Directory domain 🔑 during install. We’ve been tracking that work and the
same capability is available in Ubuntu MATE too.

Enroll your computer into an Active Directory domain

#### Ayatana Indicators

There is a significant under the hood change 🔧 in Ubuntu MATE 20.10 that you
might not even notice 👀 at a surface level; we’ve replaced Ubuntu Indicators
with [Ayatana Indicators](https://github.com/AyatanaIndicators).

We’ll explain some of the background, why we’ve made this change, the short
term impact and the long term benefits.

##### What are Ayatana Indicators?

In short, Ayatana Indicators is a fork of Ubuntu Indicators that aims to be
cross-distro compatible and re-usable for any desktop environment 👌 Indicators
were developed by Canonical some years ago, initially for the GNOME2
implementation in Ubuntu and then refined for use in the Unity desktop. Ubuntu
MATE has supported the Ubuntu Indicators for some years now and we’ve contributed
patches to integrate MATE support into the suite of Ubuntu Indicators. Existing
indicators are compatible with Ayatana Indicators.

We have migrated Ubuntu MATE 20.10 to Ayatana Indicators and Arctica Greeter. I
live streamed 📡 the development work to switch from Ubuntu Indicators to
Ayatana Indicators which you can find below if you’re interested in some of the
technical details 🤓

##### The benefits of Ayatana Indicators

Ubuntu MATE 20.10 is our first release to feature Ayatana Indicators and as
such there are a couple of drawbacks; there is no messages indicator and no
graphical tool to configure the display manager greeter (login window) 😞

Both will return in a future release and the greeter can be configured
using dconf-editor in the meantime.

Configuring Arctica Greeter with dconf-editor

That said, there are significant benefits that result from migrating to Ayatana
Indicators:

- Debian and Ubuntu MATE are now aligned with regards to Indicator support; patches are no longer required in Ubuntu MATE which reduces the maintenance overhead.

-
[MATE Tweak](https://github.com/ubuntu-mate/mate-tweak) is now a cross-distro application, without the need for distro specific patches.

- We’ve switched from [Slick Greeter](https://github.com/linuxmint/slick-greeter) to [Arctica Greeter](https://github.com/ArcticaProject/arctica-greeter) (both forks of Unity Greeter)

      Arctica Greeter integrates completely with Ayatana Indicators; so there is now a consistent Indicator experience in the greeter and desktop environment.

- Multiple projects are now using Ayatana Indicators, including desktop environments, distros and even mobile phone projects such as [UBports](https://ubports.com/). With more developers collaborating in one place we are seeing the collection of available indicators grow 📈

- Through UBports contributions to Ayatana Indicators we will soon have a Bluetooth indicator that can replace Blueman, providing a much simpler way to connect and manage Bluetooth devices. UBports have also been working on a network indicator and we hope to consolidate that to provide improved network management as well.

- Other indicators that are being worked on include printers, accessibility, keyboard (long absent from Ubuntu MATE), webmail and display.

So, that is the backstory about how developers from different projects come together to collaborate on a shared interest and improve software for their users 💪

#### Webcamoid

We’ve replaced Cheese  with Webcamoid  as the default webcam tool for
several reasons.

- Webcamoid is a full webcam/capture configuration tool with recording, overlays and more, unlike Cheese. While there were initial concerns , since
Webcamoid is a Qt5 app, nearly all the requirements in the image are pulled in via YouTube-DL .

- We’ve disabled notifications  for Webcamoid updates if installed from universe pocket as a deb-version, since this would cause errors in the  user’s system and force them to download a non-deb version. This only affects users who don’t have an existing Webcamoid configuration.

#### Linux Kernel

Ubuntu MATE 20.10 includes the 5.8 Linux kernel. This includes numerous
updates and added support since the 5.4 Linux kernel released in
Ubuntu 20.04 LTS. Some notable examples include:

- Airtime Queue limits for better WiFi connection quality

- Btrfs RAID1 with 3 and 4 copies and more checksum alternatives

- USB 4 (Thunderbolt 3 protocol) support added

- X86 Enable 5-level paging support by default

- Intel Gen11 (Ice Lake) and Gen12 (Tiger Lake) graphics support

- Initial support for AMD Family 19h (Zen 3)

- Thermal pressure tracking for systems for better task placement wrt CPU core

- XFS online repair

- OverlayFS pairing with VirtIO-FS

- General Notification Queue for key/keyring notification, mount changes, etc.

- Active State Power Management (ASPM) for improved power savings of PCIe-to-PCI devices

- Initial support for POWER10

### Raspberry Pi images

We have been preparing Ubuntu MATE 20.04 images for the Raspberry Pi and
we will be release final image for 20.04 and 20.10 in the coming days 🙂

### Major Applications

Accompanying MATE Desktop 1.24.1 and Linux 5.8 are Firefox
81, LibreOffice 7.0.2, Evolution 3.38 & Celluloid 0.18.

See the [Ubuntu 20.10 Release Notes](https://discourse.ubuntu.com/t/groovy-gorilla-release-notes/15533)
for details of all the changes and improvements that Ubuntu MATE benefits from.

    ### Download Ubuntu MATE Today

    This new release will be first available for PC/Mac users.

        [Download](https://ubuntu-mate.org/download/)

### Upgrading from Ubuntu MATE 20.04 LTS

You can upgrade to Ubuntu MATE 20.10 from Ubuntu MATE 20.04 LTS. Ensure that you
have all updates installed for your current version of Ubuntu MATE before you
upgrade.

- Open the “Software & Updates” from the Control Center.

- Select the 3rd Tab called “Updates”.

- Set the “Notify me of a new Ubuntu version” drop down menu to “For any new version”.

- Press Alt+F2 and type in update-manager -c -d into the command box.

- Update Manager should open up and tell you: New distribution release ‘XX.XX’ is available.

      If not, you can use /usr/lib/ubuntu-release-upgrader/check-new-release-gtk

- Click “Upgrade” and follow the on-screen instructions.

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.

### Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).

## focal-fossa – 2020-04-02

**Ubuntu MATE 20.04 Release Notes**

This post is more than a year old and may be outdated.

                    Ubuntu MATE 20.04 LTS represents 2 years  of continued improvement
to [MATE Desktop](https://mate-desktop.org) and Ubuntu MATE itself. For Ubuntu
MATE 19.10 we [focused on addressing as many “paper-cut” issues as possible](https://ubuntu-mate.org/blog/ubuntu-mate-19-10-eoan-ermine-release/).
That was a hugely successful  initiative, the community feedback was
overwhelmingly positive  and that is reflected in
adoption; the Ubuntu MATE 19.10 interim release is our most actively used
interim release to date!  This was only possible thanks to
dedicated group of QA testers [joining the Ubuntu MATE team](https://ubuntu-mate.org/about/team/)
and coordinating with developers to highlight  where attention was
needed.

Recognising that we’re on to a good thing,  we’ve repeated this
trick for Ubuntu MATE 20.04 LTS by once again by focusing
on the pain points our community is most vocal  about. You’ll
find details of everything we’ve improved or fixed since 19.10 plus a summary
of what’s changed since 18.04 below

I’d like to extend my sincere thanks to everyone who has played an active role
in improving Ubuntu MATE for this LTS release  From reporting bugs,
submitting translations, providing patches, contributing to our crowd funding,
developing new features, creating artwork, offering community support, actively
testing and providing QA feedback to writing documentation or creating this
fabulous website. Thank you! Thank you all for getting out there and making a
difference!

Ubuntu MATE 20.04 - Welcome now offers a few buckets of paint!

### What changed since the Ubuntu MATE 18.04 LTS?

Those of you who follow the desktop Linux news will know that
upstream [MATE Desktop recently released version 1.24](https://mate-desktop.org/blog/2020-02-10-mate-1-24-released/).
Ubuntu MATE 20.04 is shipping with MATE Desktop 1.24. Thus, all of the
improvements in MATE Desktop 1.24 are present in Ubuntu MATE 20.04 LTS.

Since the last LTS we worked on the following:

- Added multiple coloured theme variations  as one-click installs for those of you who simply don’t like Chelsea Cucumber

- Added experimental ZFS  install option.

- Added GameMode  from [Feral Interactive](https://github.com/FeralInteractive/gamemode).

- Fixed several crashers  in Brisk Menu and added keyboard  navigation.

- Fixed panel layout switching  which is now stable and reliable via MATE Tweak Tweak and Ubuntu MATE Welcome.

- Fixed rendering window controls on HiDPI  displays.

- Fixed irregular icon sizes  in MATE Control Center and made them render nicely on HiDPI displays.

- Fixed unresponsive Caja  extensions.

- Fixed mate-power-manager  to use upower-glib get_devices2().

- Fixed unresponsive Pluma  plugins.

- Fixed a crasher  in MATE Dock Applet due to an Attribute error in adjust_minimise_pos().

- Fixed auto-start errors in mate-session-manager.

- Fixed saving/restoring custom panel layouts via MATE Tweak.

- Gave Ubuntu MATE Welcome a fresh coat of .

- Updated the Ubuntu MATE Guide

- Updated the Ubiquity Slideshow

### Firmware updater

We’ve add a GTK front end for fwupd; this application can:

- Upgrade, Downgrade, & Reinstall firmware on devices supported by [Linux Vendor Firmware Service (LVFS)](https://fwupd.org/).

- Unlock locked fwupd devices.

- Verify firmware on supported devices.

- Display all releases for a fwupd device.

Ubuntu MATE 20.04 - Features an LVFS compatible Firmware management utility

#### Window Manager improvements

Marco is the Window Manager for MATE Desktop and in Ubuntu MATE 20.04
it brings a number of new features and fixes.

XPresent support is properly fixed, which means that screen tearing is now
a thing of the past and invisible window corners are finally here! Invisible
window corners mean that windows can be easily resized  without having to
precisely grab the window corners. HiDPI rendering improvements fix a number
of rendering problems that were present in various themes and components.
Most notably, windows controls are now HIDPI aware.

- Magnus (see below) provides screen magnification

- Marco supports invisible windows borders

- Marco has improved Alt + Tab behaviour

- Marco is free from screen tearing

- Marco frame performance when gaming is further improved

Minimized Application Preview

Minimized applications in the window list now present a thumbnail preview.

Alt+Tab navigation makes it possible to
traverse the application switcher via keyboard and mouse.
Alt + Tab.

Workspace Switcher allows you to switch between workspaces using a the keyboard and mouse.
Alt + Tab + Ctrl.

Compiz and Compton have been removed from the default Ubuntu MATE install.
The fundamental reasons for including them no longer exist.Only having one
window manager to target means we can promptly deliver new features and minimise
development effort. Which brings us to…

#### New Key-bindings

The key-bindings for window tiling have only worked on full keyboards
 with a 10-key pad. Few laptops  have a 10-key pad and not
all keyboards have a 10-key either. There are some well known key-bindings from
other platforms that were not recognised in Ubuntu MATE. So, we’ve had a think
:think: and have come up with this:

-
Maximise Window: Super + Up

-
Restore Window: Super + Down

-
Title Window right: Super + Right

-
Title Window left: Super + Left

-
Center Window: Alt + Super + c

-
Title Window to upper right corner: Alt + Super + Right

-
Title Window to upper left corner: Alt + Super + Left

-
Title Window to lower right corner: Shift + Alt + Super + Right

-
Title Window to lower left Corner: Shift + Alt + Super + Left

-
Shade Window: Control + Alt + s

It is now possible to tile a window to all screen quadrants
using any keyboard form factor. We updated the application launcher
key-bindings, some of these have existed in Ubuntu MATE for a while:

-
Cycle external displays: Super + P

-
Lock Screen: Super + L

-
Screenshot a rectangle: Shift + PrintScr

-
Open File Manager: Super + e

-
Open Terminal: Super + T

-
Open Control Center: Super + I

-
Open Search: Super + S

-
Open Task Manager: Control + Shift + Escape

-
Open System Information: Super + Pause

The key-bindings compliment existing well established alternatives. So if
Ctrl + Alt + T (Terminal) and
Ctrl + Alt + L (Lock Screen) are ingrained in
your muscle  memory 🧠 they are still available too. You can find all
the keyboard shortcuts documented in the Getting Started section of Ubuntu
MATE Welcome.

#### Brisk Menu

[Brisk Menu](https://github.com/getsolus/brisk-menu) is under the Solus GitHub
organisation, but it’s been a couple of years since it had a new release. The
Solus Project gave me administrative access  to the Brisk Menu repo and I’ve
made a new release. Thanks to the efforts of a couple of Ubuntu MATE
contributors, several bug  fixes have landed too, which includes
resolving frequent crashers  in Brisk Menu, preventing a scrollbar always
appearing in the category column of the menu, silencing sounds firing as you
rollover menu entries and adding keyboard  navigation.

#### MATE Panel

MATE Panel has had a long-standing bug fixed that caused it to crash  when
the panel was reset or replaced. This was most noticeable when switching panel
layouts via MATE Tweak and could result in the panel layout being left
incomplete or entirely absent. This bug is now fixed! MATE Tweak has been
updated to neatly integrate with with fixed MATE Panel behaviour so that
layout switching is now 100% reliable.

#### Indicators

A bug which resulted in oversized icons in indicators is finally resolved.

Before

After

However, it turned out some of the bugs were due to the icons  themselves.
Over  icons have been refactored ️ to correct their resolutions or aspect
ratio; as a result the panel and indicators both scale correctly.

A race condition that could result in two network status icons being
displayed is fixed, and when connected via VPN, lock icons are now
overlayed on the Network Indicator. The battery  indicator is improved
and now has a larger charging symbol while charging.

We’ve added the Date/Time Indicator and integrated it with MATE Desktop
and it now replaces the MATE clock applet which corrects the placement of
the clock and session indicators.

We’ve finally addressed a long standing issue which has been around since
Ubuntu MATE 14.10 🕸️: some of the monochrome symbolic icons used in the
indicators were also used in applications. The presented a couple of issues:

- In certain cases, you couldn’t easily see the icons against the window base colour.

- The mix of monochrome and full colour icons in applications looked inconsistent.

This issue is now resolved; monochrome symbolic icons are only used for
indicators and full colour icons are used in the Control Center, Sound
Preferences, Bluetooth, OSD, etc.

#### MATE Window Applets

[MATE Window Applets](https://github.com/ubuntu-mate/mate-window-applets)
have received a number of bug fixes and new features from a community
contributor. Window control icons now dynamically load from the currently
selected theme, rather than requiring manual user configuration.
A number of bugs (including significant memory leaks) have also been
resolved.

### Notification Center

Ubuntu MATE 20.04 includes a new Indicator that provides a “notification
center”  We worked with the [upstream developer to add new features
to indicator-notifications](https://github.com/trism/indicator-notifications)
and integrate it with MATE Notifications Daemon.

We now have a notification center that also offers a “do not disturb”
feature. When do not disturb is enabled, notifications will be muted and captured in the notification center for review. It’s also
possible to blacklist some notifications, so they are never stored by the
notification center. I’ve created an icon theme for the notification center so
it fits the look and feel of the default Ubuntu MATE theme. Notification hints
are also fixed so any notifications supplying additional media, such as
sounds or icons, now work.

### Evolution replaces Thunderbird

The Ubuntu MATE development team discussed the pros and cons of switching the
default mail  client in Ubuntu MATE to
[Evolution](https://wiki.gnome.org/Apps/Evolution). Here is a summary of our
assessment:

- Thunderbird does not integrate as well with the desktop.

      For example, theme integration, font integration, compatibility with HUD (which is increasingly difficult to support in Thunderbird), notifications with action buttons, locale and spell checking.

- Evolution integrates well with MATE Desktop given that both use GTK3.

-
Evolution includes interoperability with LibreOffice, for which Ubuntu MATE is already shipping the required components.

- Evolution has superior integration with Google Mail and Exchange, including calendar, contacts, tasks, and memos.

Indicator Date/Time also integrates with Evolution. It is fully functional,
including all the features of creating new events or opening upcoming events from the
indicator. Clicking on an individual day in the month displays the events for that day, etc.

For the many people who use web-mail exclusively, this change will have no
impact, but for those who use desktop mail we feel these productivity
improvements are significant.

For those of you who love  Thunderbird and wish to continue using it, we will
continue to offer Thunderbird in the Software Boutique for a one-click install.
Likewise, Evolution is now in the Software Boutique, and can be installed/removed
with one click.

### Magnus

Most desktop environments are lacking a screen magnifier, which is an essential
application for visually impaired  computer users, as well as accurate
graphical design or detail work. One of the reasons we ship Compiz in Ubuntu
MATE is because it has an excellent screen magnifier and was our solution for
people who need magnification

Martin and [Stuart Langridge](https://twitter.com/sil) collaborated
to create [Magnus](https://kryogenix.org/code/magnus/); a very simple
desktop magnifier, showing the area around the mouse pointer in a separate
window magnified two, three, four, or five times. Magnus is now shipped
by default in Ubuntu MATE 20.04.

### Ubuntu MATE Themes

Dozens of theme-related bugs have been fixed. The Ubuntu MATE themes have
been added to the gtk-common-themes used by snaps, so snapped applications
are now themed correctly for Ubuntu MATE users. This change is already
available all the way back to Ubuntu MATE 16.04.

The most noticeable resolved theme issues are sensibly sized expanders in tree
view (they were so tiny) that are easily clickable,
window controls are correctly proportioned on CSD windows and we’ve add a
splash of Chelsea Cucumber  to the Ubuntu MATE logo on the menu. Everything
the QA team highlighted has been fixed

### MATE Tweak and Ubuntu MATE Welcome

MATE Tweak now preserves user preferences when switching between custom
layouts thanks to a community contribution.

If you’re familiar with MATE Tweak, you’ll know it can switch panel layouts
to somewhat mimic other platforms and distros 🐧 We have now integrated a
graphical layout switcher in Ubuntu MATE Welcome to better promote the feature
and make it more accessible. We have actually had this feature since 18.04, but
the bugs in MATE Panel I mentioned earlier meant it didn’t work. With all the
associated panel bugs fixed  we now have this:

### NVIDIA drivers

If you’ve been following the news surrounding Ubuntu you’ll know that
Ubuntu will be shipping  the NVIDIA proprietary drivers on the ISO images.
Anyone selecting the additional 3rd party hardware drivers during installation
without an Internet connection will have the drivers available in offline
scenarios.

Post-install, Ubuntu MATE users with computers that support hybrid graphics
will see the MATE Optimus hybrid graphics applet displaying the NVIDIA logo.

We have given MATE Optimus an update. MATE Optimus adds support for NVIDIA On-Demand
and will now prompt users to log out when switching the GPU’s profile. MATE, XFCE, Budgie,
Cinnamon, GNOME, KDE and LXQt are all supported. Wrappers, called offload-glx
& offload-vulkan, can be used to easily offload games/apps to the PRIME
renderer. I’m also delighted to see Ubuntu Budgie 20.04 are shipping MATE
Optimus too!

The NVIDIA drivers are now going to receive updates via the official
Ubuntu software repository. So no need to add a PPA to get updates and more
importantly, the NVIDIA drivers are signed (which is not supported for
drivers distributed via PPA) so you can keep Secure Boot enabled.

#### Remote Desktop Awareness

Our MATE Desktop 1.24 packages ship support for
[Remote Desktop Awareness (RDA)](https://github.com/ArcticaProject/librda). RDA
makes MATE Desktop more aware of its execution context, so it behaves
differently when run inside a remote desktop session compared to when running
on local hardware. Different remote technology solutions support different
features and they can now be queried from within MATE components. The inclusion
of RDA offers the option to suspend your remote connection, supports folder
sharing in Caja and MIME type bindings for SSHFS shares, and allows session suspension
via the MATE screensaver.

### ZFS on root

Support for ZFS as the root filesystem is added as an experimental feature in 20.04.
The ZFS file system and partitioning layout is handled automatically directly via the
installer. zsys was added in 20.04 which now takes system snapshots before significant
installs or upgrades and inserts restore options into the GRUB bootloader menus should you
need to recover.

You can read more details on Didier Roche’s blogs:

- [Part 1 - Ubuntu ZFS support in 19.10: introduction](https://didrocks.fr/2019/08/06/ubuntu-zfs-support-in-19.10-introduction/)

- [Part 2 - Ubuntu ZFS support in 19.10: ZFS on root](https://didrocks.fr/2019/10/11/ubuntu-zfs-support-in-19.10-zfs-on-root/)

### Major Applications

Accompanying MATE Desktop 1.24.0 and Linux 5.4 are Firefox 75.0,
Celluloid 0.18, LibreOffice 6.4.2.2 and Evolution 3.36.1.

See the [Ubuntu 20.04 Release
Notes](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes) for details of all
the changes and improvements in Ubuntu that Ubuntu MATE benefits from.

    ### Download Ubuntu MATE Today

        [Download](https://ubuntu-mate.org/download/)

### Upgrading from Ubuntu MATE 18.04 LTS or 19.10

You can upgrade to Ubuntu 20.04 LTS from either Ubuntu MATE 18.04 LTS or Ubuntu
19.10. Ensure that you have all updates installed for your current version of
Ubuntu MATE before you upgrade.

- Open the “Software & Updates” from the Control Center.

- Select the 3rd Tab called “Updates”.

- Set the “Notify me of a new Ubuntu version” drop down menu to “For long-term support versions” if you are using 18.04 LTS; set it to “For any new version” if you are using 19.10.

- Press Alt+F2 and type in update-manager -c -d into the command box.

- Update Manager should open up and tell you: New distribution release ‘20.04’ is available.

      If not, you can use /usr/lib/ubuntu-release-upgrader/check-new-release-gtk

- Click “Upgrade” and follow the on-screen instructions.

There are no offline upgrade options for Ubuntu MATE. Please ensure you have
network connectivity to one of the official mirrors or to a locally accessible
mirror and follow the instructions above.

### Known Issues

Here are the known issues.

#### Ubuntu MATE

-
[Xorg crashes to Login prompt in VirtualMachines](https://bugs.launchpad.net/ubuntu/+source/xorg-server/+bug/1745345)

      When gstreamer-vaapi is installed it will cause Xorg to crash and bring the user back to the login prompt when running certain applications.

- See [Workaround for Xorg crashes to Login prompt in VirtualMachines 20.04](https://ubuntu-mate.community/t/workaround-for-xorg-crashes-to-login-prompt-in-virtualmachines-20-04/21368/2)

#### Ubuntu family issues

This is our known list of bugs that affects all flavours.

-
[Ubiquity slide shows are missing for OEM installs of Ubuntu MATE and Ubuntu Budgie](https://pad.lv/1713720)

      To work around this, run apt install oem-config-slideshow-ubuntu-mate in the OEM prepare session.

You’ll also want to check the Ubuntu MATE bug tracker to see what has already
been reported. These issues will be addressed in due course.

- [Ubuntu MATE Bug Tracker](https://bugs.launchpad.net/ubuntu-mate)

### Feedback

Is there anything you can help with or want to be involved in? Maybe you just
want to discuss your experiences or ask the maintainers some questions. Please
[come and talk to us](https://ubuntu-mate.community/).

## questing-quokka-hinweis – n/a

*Keine Release Notes auf ubuntu-mate.org für interim=25.10 gefunden.*
