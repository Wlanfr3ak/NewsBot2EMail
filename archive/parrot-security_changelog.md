# Changelog: Parrot Security

Quelle: https://parrotsec.org/blog/
Stand: 03.10.2026 20:01

---

## parrot-7.4 – 2026-10-03

**Parrot 7.4 Release Notes**

ParrotOS 7.4 brings together several months of application rewrites, desktop improvements and package maintenance. AnonSurf gains a Go backend and a Qt6 interface, Discovery's first-run tour now helps install useful software and Rocket 2.0 makes containerized tools easier to manage. The Echo desktop, Home and Security menu policies, ARM images and build infrastructure also receive practical improvements.

> **Upgrade an existing Parrot installation with:** `sudo parrot-upgrade`

### AnonSurf 6.0, rebuilt with a new graphical interface

Behind a familiar surface, the old stack was replaced with a Go backend and daemon alongside a new Qt6 and QML graphical interface designed for modern Plasma desktops, the result of a long run of focused engineering work.

![AnonSurf 6](/assets/blog/7.4/anonsurf.png)

Lifecycle is now orchestrated by a dedicated daemon and exposed through systemd, so starting, stopping, restarting, handling boot and requesting a new Tor identity flow through proper units instead of ad-hoc bash scripts. That shift made two long-requested properties possible. Changes to DNS, firewall, IPv6 and Tor configuration are now applied and rolled back transactionally, and interrupted sessions recover automatically at boot before Tor starts. At the same time Tor can be restarted without briefly restoring clearnet routing, so protection holds across transitions, with progress published to systemd and shown by the interactive command line.

The command line interface (CLI) itself was redesigned to be helpful both interactively and in scripts, with structured JSON output, unified DNS feedback, public IP and Tor status checks, an integrated DNS tool and Nyx monitoring. Separately, the optional SafeKill action requests termination of selected applications and uses BleachBit to clean selected caches, history and sessions before routing changes. It does not terminate every running process: unsaved work may be lost and the cleaning cannot be undone.

Most of the work went into Tor and network hardening, with generated Tor configuration handling the Parrot base, safety options, bridges, HTTP proxy rendering and monitor configuration through atomic writes, strict permissions and isolated backups that survive across filesystems. Bridge validation was tightened and malformed input is rejected. ICMP is no longer redirected into Tor, while DHCP, loopback, private networks and local resolvers are preserved together with resolver symlinks, permissions and NetworkManager DNS ownership.

Pre-existing direct TCP/UDP connections to public IPv4 destinations are blocked rather than migrated into Tor, apart from Tor-owned traffic and the DHCP exception; TCP applications must reconnect. TCP DNS uses the transparent proxy and UDP DNS uses the dedicated DNS port. Per-interface IPv6 restoration now covers complex interface names as well, Tor control authentication stays private, control requests are bounded, and bootstrap is allowed to finish undisturbed.

The graphical interface stays deliberately unprivileged, reading status from the CLI and sending authorized lifecycle requests over system D-Bus, with single-instance activation, system tray controls and desktop notifications.

Upgrades are part of the migration too: the old `anonsurf-gtk` package transitions to `anonsurf-gui`, and the CLI package can take ownership of the manual page previously shipped by AnonSurf 5 without a file conflict. Separate CLI and GUI launchers avoid duplicate menu entries.

### Raspberry Pi and ARM images from 7.3 to 7.4

Repository priorities were tuned so tightly coupled library sets stay consistent from one source instead of mixing builds, which resolves dependency failures when installing desktop applications. SSH host keys are now generated independently of first-boot detection while preserving existing device keys and cleaning keys accidentally recreated from the build machine during export. Export also refreshes menu launchers, prepares directories hidden by temporary mounts for package hooks, removes obsolete boot overrides with validation of the kernel command line and distinguishes Home and Security menu editions so Home shows only what is actually installed while pulling in the right edition-specific packages.

The ARM lineup is also expanding with **arm64 ISO images** and a first Orange Pi beta. The planned beta download targets the **Orange Pi 5 Ultra**, not (yet) the entire Orange Pi range. We would like to thank the Orange Pi team for their support.

Its first-boot console flow creates the user's account before enabling SSH and the desktop; the image is designed without shared login credentials or pre-generated SSH host keys. The Ultra also receives board-specific SDIO Wi-Fi integration.

### Optimized ISO images for modern CPUs

The previous parrot version has introduced a new experimental feature that tries to recompile the parrot packages targeting modern revisions of the arm64 and amd64 architectures. This translates directly into faster operations and longer battery life on all computers that support such modern architecture revisions.

Now we are pleased to announce our official optimized iso files that ship with such opt-in feature enabled by default. They target the `amd64v3` and `armv8.2` microarchitecture versions of amd64 and aarch64, which means all the x64 computers built after 2015, and  arm boards like the Raspberry Pi 5, Apple Silicon M series, and Cortex X1 will benefit from such optimizations.

- `amd64v3` targets x86-64-v3, using instructions such as AVX2, FMA and BMI2 on compatible Intel and AMD processors.
- `arm64v8.2` targets ARMv8.2-A with LSE atomics, dot-product, FP16 and cryptography extensions on compatible ARM hardware.

The optimized package selection prioritizes shared libraries and compute-heavy applications, including compression and cryptography libraries, FFmpeg, NumPy and OpenBLAS. Performance gains depend on the workload: compute-intensive tasks can benefit, while I/O-bound operations may see little difference. Packages outside this selection remain at the standard baseline.

**Check CPU compatibility before choosing an optimized image**: unsupported instructions can cause programs to fail with an illegal instruction error. Standard images remain the compatibility choice for older hardware: Raspberry Pi 3 and 4, for example, do not meet the ARM requirements.

See the [Parrot optimized builds guide](https://www.parrotsec.org/docs/configuration/parrot-optimized-builds/) for compatibility checks, setup instructions and the current package list.

### Onboarding tool that installs things

A new tool has been added to our collection: Parrot Discovery is our first-run welcome application and full setup tool for your system.

![Parrot Discovery](/assets/blog/7.4/discovery.webp)

A guided checklist covers tool profiles, with selectable cards for everyday applications such as browsers, editors, chat apps, containers, gaming and privacy tools, all installed through curated APT and Flatpak commands that the user reviews and confirms.

Package states are detected asynchronously, the system updater opens directly from the tour, next-step and tools cards close the flow, and autostart respects the stored preference while staying correctly disabled in live mode. Discovery provides a guided path from a fresh desktop to a working setup.

### Rocket 2.0, a redesigned workspace for containerized tools

Rocket receives a substantial update, not just packaging fixes. Its redesigned PySide6 interface combines a searchable tool catalog, image availability and running-container status with a Dockerfile manager: users now can create or generate Dockerfiles from catalog entries, edit and save them, build images and run the resulting containers from the same application.

Container operations and status refreshes run asynchronously, keeping the interface responsive while images are checked or containers are stopped. The catalog gains additional assessment tools and per-tool runtime profiles, which also apply to generated Dockerfiles.

The runtime policy is explicit: Rocket prefers healthy rootless Podman, while Docker fallback requires the user's approval for the current session. That approval expires when Rocket closes. Rocket does not automatically switch to rootful Podman or invoke it through sudo.

### Echo integration now goes beyond appearance

`parrot-core` 7.4.1 moves KDE appearance and daemon defaults into `/etc/xdg` rather than relying on frozen per-user skeleton copies. It disables Baloo indexing by default, reduces automatically loaded KDE background modules, exposes Parrot wallpapers in the wallpaper selector and removes hardcoded activity identifiers and obsolete Plasma configuration. The desktop metapackages explicitly pull in `echo-themes-kde` or `echo-themes-lxqt`, fixing upgrades that could lose the corresponding theme assets after the theme package split.

![Parrot Updater](/assets/blog/7.4/updater.png)

Parrot Updater 2.2.0 adopts the Echo styling and keeps its terminal output visible and scrollable after an update finishes, so users can review what happened instead of losing the log when the job exits. The new Discovery opens this updater directly.

Smaller fixes have visible effects too: a malformed PATH in `/etc/profile` was corrected so commands under `/usr/sbin` are found again in login shells, and the amd64 kernel configuration enables the Lenovo WMI Hotkey Utilities module. Realtek RTL8188EUS and Broadcom STA driver packaging was refreshed too.

#### Home and Security menus, with explicit edition policies

The Go-based launcher system introduced in 7.3 now separates common menu infrastructure from the policy that exposes tools available for installation. `parrot-menu-security` enables install-on-demand entries; it does **not** install the security tool suite by itself. Installed tools of course keep their launchers regardless of that policy.

The current image builders apply the policy differently by format:

Administrators can override the package presets with `ShowInstallableLaunchers` in `/etc/parrot-menu/launcher.conf`. Launcher generation also handles package ownership and command quoting more consistently, restores missing entries and bounds generated labels so they do not unnecessarily widen the Plasma menu.

## Updated tools and utilities

- Linux kernel [7.1.13]
- aesedb [0.1.8]
- airgeddon [12.02]
- anonsurf [6.0.1]
- base-files [7.4]
- bettercap [2.41.7]
- broadcom-sta [6.30.223.271]
- bytecode-viewer [2.13.2]
- certipy-ad [5.1.0]
- colly [2.3.0]
- crowbar [4.2]
- desktop-base [7.0]
- discovery [1.0.3]
- dnsx [1.3.0]
- echo-themes [1.3]
- ffuf [2.2.1]
- freeradius-wpe [3.2.3]
- getallurls [2.2.4]
- golang-github-nlnwa-whatwg-url [0.6.2]
- hakrawler [2.1]
- jadx [1.5.5]
- kismet [2025.09.R1]
- ligolo-ng [0.9.1]
- mcpwn [1.3.0]
- metasploit-framework [6.5.4]
- naabu [2.6.1]
- node26 [26.7.0]
- osrframework [0.20.5]
- parrot-core [7.4.1]
- parrot-interface [7.4.2]
- parrot-menu [7.4.3]
- parrot-updater [2.2.0]
- pyexcel [0.7.0]
- pyexcel-io [0.6.6]
- pyexcel-ods [0.6.0]
- pyexcel-text [0.2.7.1]
- pyexcel-xls [0.7.0]
- pyexcel-xlsx [0.6.0]
- pymavlink [2.4.37]
- realtek-rtl8188eus-dkms [5.3.9~git20260622]
- rocket [2.0.0]
- subjack [3.0.0]
- theharvester [4.10.1]

Additional maintenance also covered asleap, calamares-settings-parrot and sbd.

### Build system for ISO, VM, containers and alternative targets

The ISO builder includes Discovery as the welcome and setup screen, and adopts the edition-specific menu policy described above.

VM builds explicitly target **arm64 for UTM on Apple Silicon**, while the other current VM formats retain their amd64 build matrix. UTM bundles gain a custom Parrot icon. Cross-architecture builds handle `binfmt_misc`, and Security image creation fails explicitly when the required security tool installation is unsuccessful instead of producing a silently incomplete image.

The optimized-image hooks retain the architecture-aware setup added during the 7.3 preparation: Home and Security builds select `amd64v3` or `arm64v8.2` according to the target architecture and configure APT pinning for the selected optimized component. This is continued support for the existing optimized builds, not a new architecture announcement for 7.4.

### More predictable MCP tool execution via mcpwn 1.3

mcpwn, the MCP server for running security tools, gains configurable per-tool timeouts, output-preview limits and accepted exit codes, along with stricter configuration validation and explicit execution errors. Full command output can be retained locally and inspected through read, tail and search helpers rather than being lost when an MCP response is truncated. Tool arguments are no longer written to execution logs.

This new version also adds Subfinder and dnsx discovery tools, fixes dnsx list input and preserves extra arguments containing spaces.

### Parrot web presence

Documentation moves to **Astro/Starlight** with graphical navigation cards, revised search placement, dark-theme improvements and clearer code blocks. Existing guides and assets were ported to the new framework, with deployment fixes so pages and links resolve correctly under `/docs`. The content work matters as much as the redesign: the Parrot 7 upgrade guide's repository snippets, SSD TRIM options and broken internal links were corrected, duplicated WSL guides were consolidated, and image verification instructions now require checking the signed hash list before trusting its checksums.

The Arsenal Explorer builds its tool dataset from *package and menu information and enriches missing metadata from the package archives*. Its redesigned header, search and filter controls are joined by an alphabetically sorted tool list and initial-letter filtering on larger screens.

Over the same development window, the main website receives redesigned edition-download controls, more consistent recommendations and better mobile layouts. The Markdown rendering pipeline is also updated to current remark/rehype and React rendering APIs.

**Taken together**, this is a consolidation release with several substantial application updates. AnonSurf modernizes Tor routing and recovery, Discovery makes a fresh install productive, Rocket improves the workflow for containerized tools, and the desktop and ARM images become more consistent. Thanks to everyone contributing code, packaging, documentation and testing.

Happy hacking, and happy updating!

## parrot-7.3 – 2026-06-29

**Parrot 7.3 Release Notes**

Parrot 7.3 is out, and every edition has been rebuilt on it. This release landed only a few months after the previous one, and most of the work went into the system itself rather than the toolset, with two targets in mind: faster execution on recent hardware, and smoother day-to-day use. 
The build scripts changed little this round, with the effort going into smaller images and into dropping preinstalled tools that the Home and Security editions did not need.

Furthermore, we would like to thank our contributors, whose quick feedback and dedication keep the packaged tools up-to-date.

> **Upgrade with:** `sudo parrot-upgrade`
 
### Highlights

*   **Optimized builds**: an opt-in repository of packages recompiled for newer CPU baselines, with 20% to 50% gains on compute-heavy work.
*   **A new menu system rewritten in Go** (`parrot-exec` and `launcher-updater`), with one-click installation of any tool straight from the menu.
*   **Official Vagrant boxes** for the Home and Security editions, amd64.
*   **A new Firefox start page**, built with Vite, that collects no data.


## Table of Contents

## Optimized builds for modern CPUs

For the sake of broad compatibility, standard Debian and Parrot packages have always been built against the 2003 x86-64 baseline, which leaves more than two decades of CPU improvements on the table. Parrot 7.3 offers a way around that with an opt-in set of recompiled packages, shipped as extra repository components alongside the standard archive.

Selected packages are rebuilt against newer baselines, x86-64-v3 on amd64 and ARMv8.2-A on arm64, which switches on instructions such as AVX2, FMA, BMI2, LSE atomics and DOTPROD. How much this helps depends entirely on the workload. It does close to nothing on I/O-bound tasks, while compute-bound work such as compression, encryption, hashing and media encoding can run 20% to 50% faster.

Only packages where the gain is measurable are included, which in practice means shared libraries, language runtimes, and compute-heavy utilities such as ffmpeg, inkscape and numpy. Network daemons, shells and similar infrastructure stay on the baseline build, since they would gain nothing from the change.

![Parrot Optimized Builds](/assets/blog/7.3/optimized-builds.png)

The packages are delivered as repository components rather than as separate Debian architectures, which sidesteps multiarch path collisions and needs no changes to APT or dpkg. Selection comes down to version comparison alone, so an optimized package like `1.2.3-parrot1+amd64v3optimized1` ranks above the standard `1.2.3-1`, while a newer standard release such as `1.2.3-2` still takes priority, which is what keeps security updates landing immediately instead of waiting for an optimized rebuild.

A hardware guard prevents the packages from installing on a CPU that cannot run them. A small support package runs a feature check at install time, and every optimized package depends on it, so the install aborts cleanly on incompatible hardware. Turning the feature on requires a compatible CPU (Intel Haswell or AMD Zen and newer for amd64v3, and Apple M1 or newer, Raspberry Pi 5, Graviton 2 or equivalent for arm64v8.2), one extra apt source, and a run of `sudo parrot-upgrade`. The full package list and the compatibility checks are documented at [parrotsec.org/docs/configuration/parrot-optimized-builds](https://parrotsec.org/docs/configuration/parrot-optimized-builds).

## A new menu system, rewritten in Go

Two core components have moved off shell scripts and onto Go, `parrot-exec` and `launcher-updater`, which leaves two small binaries with no dependencies and a menu where every tool is visible and installable in a single click.

### parrot-exec

Installed at `/usr/bin/parrot-exec`, it is the launcher behind every ParrotOS `.desktop` file. It covers direct execution, sudo-elevated terminal commands, graphical applications through pkexec (with DISPLAY and XAUTHORITY forwarded explicitly so X11 apps still work under privilege escalation), and directory listing for resource-based launchers such as wordlists and webshells.

Its most useful behavior is on-demand installation. When you click a `[not installed]` entry, parrot-exec checks the local apt cache with `apt-cache policy` and stops with an error if the package has no candidate. When there is one, it installs the package and then triggers `update-launchers` right away, so the template entry is swapped for the real launcher. The terminal stays open after a command by default, and `attachStdio()` wires the child streams directly to the parent process, which keeps every session interactive.

![New Parrot Menu](/assets/blog/7.3/parrot-menu.png)

### launcher-updater

Installed under `/usr/share/parrot-menu/`, it handles the full lifecycle of Parrot desktop files through three internal packages: `dpkg`, which reads `/var/lib/dpkg/status` directly for O(1) lookups, `desktop`, which handles parsing and template generation, and `launcher`, which holds the sync logic.

Every desktop file carries an `X-Parrot-Package=` field. If that package is installed, the file is copied into `/usr/share/applications/` with the `.png` extension stripped from `Icon=` lines along the way. If it is not installed, a template is generated instead, carrying the not-installed prefix, the software-manager icon, and `Exec=parrot-exec --install <package>`. Upstream Debian `.desktop` files from packages such as wireshark, ettercap and chirp are suppressed whenever a Parrot wrapper for the same tool already exists, which keeps duplicates out of the menu. Legacy naming is cleaned up during the same sync, so when a `serv-*` launcher is deployed, any leftover `parrot-*` entry with the matching suffix is removed, finishing the move off the old naming convention without leaving stale entries behind.

Once the sync is done, `kbuildsycoca6` runs as the original user (resolved through SUDO\_USER or logname, with the correct DBUS\_SESSION\_BUS\_ADDRESS) to refresh the KDE menu cache, because running it as root would miss the user's D-Bus session entirely. That step is skipped when the tool is invoked with `wait_dpkg`, which avoids redundant rebuilds during batch operations.

## Official Vagrant boxes

Parrot 7.3 ships official Vagrant boxes for the Home and Security editions, amd64 only, so security professionals can bring up a reproducible ParrotOS environment with a single command. The build mounts a pre-installed `.qcow2` image through qemu-nbd, installs and enables SSH, sets up password authentication, and packages the result as a standard Vagrant box for libvirt. Once the box is added to your environment, writing a Vagrantfile and running `vagrant up` is all it takes to land in a clean ParrotOS instance in a known state, with no manual setup and no configuration drift. The same box can be shared across a team or wired into a CI pipeline, which brings Parrot into an Infrastructure as Code workflow.

## New Firefox start page

Firefox now opens to a new start page by default, and you can still point it somewhere else if you prefer. It is a lightweight landing page built with Vite, with search through DuckDuckGo, Qwant or Google, plus the latest articles and a set of documents worth reading before getting into Parrot. No data is collected here, and the same holds for the main website and the other web services.

![New Start Page](/assets/blog/7.3/start-page.png)

## Updated tools

This release pulls in current versions of the tools people rely on most:

- Linux kernel [7.0.9]
- sherlock [0.16.0]
- bettercap [2.41.5]
- caido [0.55.2]
- seclists [2026.1]
- rocket [1.5.1]
- evil-winrm-py [1.6.0]
- bloodyad [2.5.4]
- airgeddon [12.0]
- enum4linux-ng [1.3.10]
- goshs [2.1.0]
- metasploit [6.4.136]
- sqlmap [1.10.4]
- ghidra [12.0.4]

Generic tools such as Firefox and a range of libraries, including Python modules, were updated to their latest releases as well.

## Internal packages and bug fixes

All internal `parrot-*` packages, including core and interface, were updated. `parrot-updater` went through a refactor that split configuration management away from notifications, and it now calls pkexec directly rather than through `/bin/sh`, which tightens the privilege-escalation path. Two bugs in the updater were also fixed: the update-complete dialog now reads "Close" instead of "Ok", and clicking the start button several times no longer fires off multiple completion dialogs.

## parrot-7.2 – 2026-05-07

**Parrot 7.2 Release Notes**

Our 2026 roadmap is proceeding at full speed and, as of today, Parrot 7.2 is available for download. This new version brings together all the updates from recent months, but focuses primarily on several significant technical improvements: to our infrastructure, our Docker containers, and the update of various security tools, as well as updates to several OS-related side projects.

It is worth noting that this version includes Linux kernel v6.19.13, which, as many of you may have already read online, includes the patch for the recent CVE-2026-31431 "Copy Fail". We strive to stay proactive regarding global developments and do our best to ensure you receive the most stable and up-to-date updates.

Finally, before diving into the detailed update logs, we want to thank the contributors who chose to support us for this new release. Even a simple change adds value to the project, and seeing new community members contribute to some aspects of the OS fuels our drive to deliver continuous improvements.

## Table of Contents

- Tools
- Website and Documentation
- Builder scripts update

# Tools

We have worked diligently to integrate the latest versions of the community’s most essential tools, focusing on seamless compatibility, stability, and robust security across the following packages:

- Linux kernel [6.19.13]
- netexec [1.5.1]
- zaproxy [2.16.1]
- bloodhound [9.0.0]
- beef-xss [0.6.0.0]
- certipy-ad [5.0.4]
- evilginx [3.3.0]
- evil-winrm-py [1.6.0]
- sqlmap [1.10.3]
- mcpwn [1.2.0]
- parrot-updater [2.0.8]
- metasploit [6.4.127]
- enum4linux-ng [1.3.5]
- gdb-gef [2026.01]
- legion [0.7.0]
- httpx-toolkit [1.7.4]
- pypsrp [0.8.1]

Significant updates have also been implemented for parrot-menu, as the migration to the new Go codebase continues and new desktop entries have been added. Other core components, including parrot-themes and parrot-tools have received improvements.

Specifically, parrot-core now includes a built-in check for packages installed via Flatpak, automatically handling updates for them as needed. Furthermore, we have refined the post installation logic to improve system stability during home directory synchronization from Parrot 6 "Lory".

Additionally, this release synchronizes Parrot with the latest Debian upstream updates. By aligning with the Debian project, we ensure that all core packages benefit from the most recent security fixes and stability patches.

# Website and Documentation

Our website renewal process is well underway, take a tour to see the new style changes that align with our UX vision. The same applies to our documentation, where several sections have undergone significant revisions to ensure a more professional and fluent reading experience. Moving forward, the entire documentation will receive a substantial UI/UX overhaul, so stay tuned!

# Builder scripts update

The virtual machine codebase has undergone a refactor to enhance modularity and readability, as well as to streamline builds via CI/CD. This will allow us to expand the range of Parrot editions and variants, also for the ARM architecture.

We also took the opportunity to identify and resolve several bugs, specifically targeting the build process. We focused on improving rsync's cloning reliability by implementing path anchoring for exclusions, preserving extended attributes and hard links, and ensuring consistent UID/GID mapping. Also, on the btrfs side, we optimized performance for virtual environments by fine-tuning mount options like noatime and discard=async, and we resolved bootstrapping issues by ensuring all necessary dependencies are verified before the build begins. Crucially, we addressed a critical kernel loading issue on BTRFS systems by refining how boot files are handled during installation, disabling compression and CoW on the boot partition.

For the end user, these changes translate into seamlessly improved stability and a more efficient system.

In addition, this infrastructure now supports image generation for the Hack The Box Edition across both ISO and VM formats.
