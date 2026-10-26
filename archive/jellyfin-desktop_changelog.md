# Changelog: Jellyfin Desktop

Quelle: https://github.com/jellyfin/jellyfin-desktop/releases
Stand: 23.10.2026 06:45

---

## 1.12.0 – 2025-03-20

This version fixes a bunch of bugs and removes the obsolete third party plugin for intro skipping. Please note this release drops support for MacOS 12 due to GitHub Actions dropping runner support.

Changes:
  * Prevent issue where wayland has black screen due to broken gpu accel (#165, #610)
  * Prevent SRT text being squished and unreadable (#643)
  * Handle server connection timeout. (#747)
  * Remove obsolete skip intro support.
  * Update branding
  * Fix caching issues to prevent broken web client when the server web version updates
  * Auto fill last used server into server box if server connection fails on startup
  * Fix SSL certificate verification issues on Linux

About Windows Downloads:
 - If your CPU is older than roughly 2013 or you get a `0xc0000142` error you need to use the x64-legacy build.
 - The desktop installer requires administrator rights.
 - You can avoid warnings on files by unblocking the file in the properties dialog.
 - You can manually build a release [using these instructions](https://github.com/jellyfin/jellyfin-media-player#building-for-windows).

## 1.11.1 – 2024-06-08

This is a hotfix which fixes the previous release so it can work on servers which are running on a subpath/base url (i.e. `example.com/jellyfin` instead of `jellyfin.example.com`).

Note: It is normal to have to log into your servers again after installing this update if you are upgrading from v1.10.1 or older.

About Windows Downloads:
 - The desktop installer requires administrator rights.
 - You can avoid warnings on files by unblocking the file in the properties dialog.
 - You can manually build a release [using these instructions](https://github.com/jellyfin/jellyfin-media-player#building-for-windows).

## 1.11.0 – 2024-06-07

This release switches Jellyfin Media Player to always use the external web client so that updates to `jellyfin-web` take effect immediately instead of when I get a chance to release the application.

Note: It is normal to have to log into your servers again after installing this update.

## 1.10.1 – 2024-05-18

# This build REQUIRES Jellyfin 10.9.1 or later to work. You will get a blank home screen if you don't use a new enough server version.

Changes:

  * Upgrade jellyfin-web to 10.9.2.
  * Fix overscroll and inability to launch on MacOS (#628)
  * Update skip intro plugin.
  * Fix setBackdropTransparency.

## 1.10.0 – 2024-05-15

# This build REQUIRES Jellyfin 10.9.1 or later to work. You will get a blank home screen if you don't use a new enough server version.

This release upgrades Jellyfin Media Player to work better with the latest version of the Jellyfin server. Numerous features and improvements have also been added by the community.

  * Update web client to 10.9.1.
  * Switch to native Jellyfin Trickplay support.
  * Update mpv version to latest git version.
  * Misc fixes and cleanup. (#603)
  * Fix trailing slash when adding server causes connection faliure. (#601)
  * Fix compatibility with mpv 0.38.0. (#597)
  * Fix appstream metadata (#592)
  * Show what's playing in MacOS's "now playing" (#580)
  * Add Apple silicon build. (#571)
  * Add tooltips and settings for MPV config. (#561)
  * Fix mpv deprecations. (#549)
  * Add support for FreeBSD. (#547)
  * Fix icon for Wayland. (#515)
  * Improve customization for subtitles. (#508)
  * Ensure that volume is always a Number. (#493)
  * Fix window restoring on opening with Hyprland. (#481)
  * Fix window switching monitor when exiting fullscreen. (#478)
  * Fix skipintro plugin client freeze. (#456)
  * Set max audio channels for transcode profile based on JMP settings. (#445)
  * Add Default Playback Speed settings. (#435)
  * Remember playback speed. (#434)

If you have issues with media playback due to hardware decoding (green/purple or artifacts), you can [disable it using these instructions](https://github.com/jellyfin/jellyfin-media-player/wiki/Disabling-Hardware-Decoding).

## 1.9.1 – 2023-04-24

This release is primarily to get the updated `jellyfin-web` to correct the stored XSS vulnerability [GHSA-89hp-h43h-r5pq](https://github.com/jellyfin/jellyfin-web/security/advisories/GHSA-89hp-h43h-r5pq). While JMP is not vulnerable to most XSS vulnerabilities due to being an isolated application, this one could affect it.

Changes:

  * Update web client to 10.8.10 to patch stored XSS issue.
  * Skip searching for SSL bundles on Linux. (#301)
  * Disallow flac from video transcoding. (#423)
  * Allow disabling dovi transcode rule.
  * Fix missing port in translation. (#288)
  * Censor token from new stored creds block.

## 1.9.0 – 2023-03-13

The goal of this release was to clean up a bunch of bugs and issues. You can now set the aspect ratio from the player. I also added a bunch of codec profile settings and force transcode Dolby Vision content. Using a web client provided by your Jellyfin server instead of the built-in one is now supported too.

 - Add aspect ratio controls to player. (#388)
 - Don't reset mute between videos. (#349)
 - Auto-detect and switch SteamOS to TV mode. (#237)
 - Add options to disable Windows integrations. (#351 #342)
 - Allow forcing transcodes for HEVC, Hi10p, 4K, HDR, and/or AV1.
     - Media profile settings now work without a client restart.
 - Allow requesting the server to transcode to HEVC.
 - Improve usability of client API to make integrations with other clients easier.
     - New documentation on integrations is [available here](https://github.com/jellyfin/jellyfin-media-player/blob/master/for-web-developers.md).
 - Allow running JMP without an embedded webclient.
     - This will make it easier for upsteam distributions to package the software.
     - You can opt-in to using a server-provided web client through client settings.
     - This may also be useful for people who modify their web client on the server.
 - JMP now uses the official webclient build from repo.jellyfin.org.
 - Switch to [custom mpv build](https://github.com/iwalton3/mpv-winbuild-cmake/releases/tag/v20230304-git-362256e) which has working TLS 1.3 support.
 - Fix time breakage from skipIntroPlugin. (#387)
 - Add delay to prevent broken update dialog. (#373)
 - Prevent Dolby Vision content playing without server transcoding.
    - This fixes colors in media but requires a GPU on the server to support playback.
    - I have disabled remuxing of HEVC due to a bug in the server for now. You can re-enable it in settings but it will break this Dolby Vision fix.
    - If you want to direct play Dolby Vision, you could try using the experimental gpu-next mpv mode with MPV Shim.

## 1.8.1 – 2023-02-13

This version is primarily for updating dependency versions such as the web client and MPV, which notably is now up to date and compiling properly for Windows whereas it used to be pinned to a 2021 release.

Additionally experimental support for [Skip Intro](https://github.com/ConfusedPolarBear/intro-skipper) and [Jellyscrub](https://github.com/nicknsy/jellyscrub) is included. You need to install these **unofficial** plugins to your Jellyfin server manually and enable support in client settings. Support is implemented in the form of [separate plugins](https://github.com/jellyfin/jellyfin-media-player/tree/master/native) which I have adapted from the original web client modifications so that the integration is cleaner.

Note: Adding support for this is intended to alleviate the alternative which is people manually patching the client. **Please do not bother other Jellyfin client maintainers to add unofficial plugin support.** In the event that official Jellyfin functionality replaces unofficial plugins or renders them unusable, unofficial plugins will be dropped.

Changes:

  * Update web client to 10.8.9.
  * Add support for Jellyscrub and Skip Intro. (Must be enabled manually, requires third-party plugins.)
  * Update to MPV version 20230205 e439ddc (Windows).
  * Update to MPV version v0.35.1 (Flatpak).
  * Add input map for DualShock 4 connected via USB (#359)
  * Add support for DVBSUB subtitles (#279)
  * Allow screensaver when video is paused (#276)
  * Fix Debian package for bookworm.
  * Fix issue where plugin support was not enabled correctly by configuration (#371).

## 1.8.0 – 2023-02-13

(This release has been replaced by v1.8.1 due to #371. Sorry for the inconvenience.)

## 1.7.1 – 2022-06-27

This is a hotfix that fixes some important issues. Changes:

 - Fix audio and subtitle selection for 10.8.0. (#271)
 - Stop forcing fullscreen on Windows when visibility changes. (#94)
 - Update jellyfin-web client to 10.8.1.

If you have issues with media playback due to hardware decoding (green/purple or artifacts), you can [disable it using these instructions](https://github.com/jellyfin/jellyfin-media-player/wiki/Disabling-Hardware-Decoding).

## 1.7.0 – 2022-06-11

This is the first release of JMP targeting Jellyfin 10.8.0 stable. Thank you to everyone who tested the pre-releases!

Changes:
  * Update web client to 10.8.0.
  * Add --platform option. (#159)
  * Added Xbox input mapping. (#197)
  * Disable youtube-dl attempts on media errors.
  * Allow retry with transcode instead of usng a hard failure. (#127)
  * Add exit app function (#198)
  * Set the MaxStaticBitrate to avoid server hard-coded 8 mbps limit.
  * Add build for Ubuntu 22.04 (#256)
  * Enable windows dark mode support. (#247)

## 1.6.1 – 2021-08-01

Changes:

  * Update jellyfin-web to 10.7.6.
  * Add dependency to libqt5xml5. (#103)
  * Fix hang after playback error. (#88)
  * Fix alt+tab switching on GNOME. (#84)
  * Fix media key pause/play on Windows. (#83)

## 1.6.0 – 2021-05-05

For Windows users this release features system-wide media key support and the addition of the option to create a desktop icon.

![image](https://user-images.githubusercontent.com/8078788/117087308-10a77980-ad1d-11eb-96f2-796d8f14c0e5.png)

This version also changes the default hardware decoding mode to decode.copy, which has been found to be effective for 98 percent of users and less prone to color problems. It also includes all of the jellyfin-web fixes recently released in Jellyfin 10.7.5.

Changes:
 - Always set volume on playback. (#78)
 - Allow user to theme application icon on Linux. (#75)
 - Fix ignoreSSLErrors option on Linux. (#74)
 - Add Global Windows Media Key/OSD integration. (#73)
 - Enable drag-drop file uploads into web client. (#56)
 - Add option to create a Windows Desktop Shortcut.
 - Use smaller jellyfin icon on macOS to match other icons.
 - Change default hwdec from enabled to copy.
 - Allow smaller window size.
 - Add more error handling to AutoSet feature.

## 1.5.0 – 2021-04-25

Note! Hardware decoding may break playback for some people! Please [complete this survey](https://forms.gle/omTCojdHctSb3Atn7) so I can make an informed decision about the default.

If you were still using MPV Shim for the subtitle feature, you will be happy to know this release will remember your subtitle preference between episodes! Note that you must start playing the next episode for this to happen. 

You can also apply custom CSS per-user and per-client:
![image](https://user-images.githubusercontent.com/8078788/115976750-222f9b00-a53f-11eb-95af-4b627cdb29f4.png)

And finally, you can control the player from the Windows Taskbar:
![image](https://user-images.githubusercontent.com/8078788/115976756-370c2e80-a53f-11eb-8954-987f67e767dc.png)

Changes:

 - Remember intended subtitle and audio selection between episodes.
     - If you stop playback right at the end of an episode, it will *not* apply it to the next one.
 - Allow disabling the server's custom CSS.
     - Important for troubleshooting as at least one theme is known to break TV mode.
 - Allow using custom CSS locally on the client. (Per user)
 - Fix scroll bar styling on TV mode.
 - Add Windows taskbar integration. (#61)
 - Fix volume OSD not showing on mute toggle. (#63)

## 1.4.1 – 2021-04-20

Changes:

 - Add update notifier.
 - Add option to disable input repeat. (#49)
 - Add config-only option to ignore SSL certificates. (#48)
 - Fix excessive width of options drop-downs in some cases.
 - Actually update the web client for Debian/Ubuntu packages.

## 1.4.0 – 2021-04-18

This release fixes the issue where images did not show up in the web client. It also brings back TV mode, which can now be remote controlled. For instance in my testing I was able to control the client using a PS3 controller!

**If you are upgrading from 1.2.1 or earlier you must log out and log back in or casting, state updates, and SyncPlay will not work.**

Changes:

 - Backport fix for images not loading.
 - Enable mouse back/forward buttons. (#42)
 - Fix subtitle offset support. (#35)
 - Add back support for TV mode, and also use configuration/command line flags.
 - Add support for some media keys, remotes, and controllers through inputmanager.
     - Using TV mode is suggested if you want to remote control the client.
 - Enable hardware video decoding by default.
     - If this breaks video playback, you can shut it off in "Client Settings".
 - Allow file download option in web client again.
 - Fix more warnings in the codebase. (#32)

## 1.3.1 – 2021-04-14

This release adds more packages and fixes a rather serious performance problem that causes increasing numbers of unnecessary API calls to the Jellyfin server, particularly with music.

**If you are upgrading from 1.2.1 or earlier you must log out and log back in or casting, state updates, and SyncPlay will not work.**

Changes:

  * Fix music performance issue where there were excessive API calls (#22)
  * Add builds for win32, debian, and ubuntu. All packages are built in CI now!
  * Fix fullscreen button in web player.
  * Add maximized window state preserving (#26)
  * Fix QT warnings (#24)       
  * Fix wayland and wayland hwdec support (#20, #23)
  * Set white font color on modal and add class for css themes.
  * Upgrade jellyfin-web to 10.7.2.

**The Mac OS build has been fixed, and has been signed. Please use "1.3.1a", in place of the older download.**

## 1.3.0 – 2021-04-11

This release exposes a ton of settings previously buried in the config file. Additionally it contains many other improvements.  
**Please log out and log back into your Jellyfin server after updating.**
![2021-04-11-014902_762x766_scrot](https://user-images.githubusercontent.com/8078788/114293899-1dabb280-9a68-11eb-963d-7b528e526dd2.png)

Changes:
 - Add settings menu for built-in player settings.
     - Hardware video acceleration can be enabled.
     - Subtitle position, color, and scaling options. (Support varies by subtitle type.)
     - Fullscreen keeps the player fullscreen at all times.
     - The screen the player opens on can be set.
     - Setting the display refresh rate to content. (Requires Fullscreen)
     - Changing audio devices, including enabling codec passthrough. (Not Tested)
     - Deinterlacing can be enabled. (Not Tested)
 - Add hardware acceleration in the web view. (disable with `--disable-gpu`)
 - Properly advertise player name, version, and computer name.
     - This has the side effect of sadly breaking all existing sessions.
     - If you do not log out and back in, remote control, SyncPlay, and UI updates break.
 - Make subtitle position and scale settings work with SSA and bitmap subtitles.
 - Switch to NativeShell interface for jellyfin-web extensions.
 - Fix video download option to open links in browser.
 - Fix up next dialog hiding the player UI.
 - Add support for remote devtools.
 - Fix F11 key for fullscreen.
 - Upgrade webclient to jellyfin-web 10.7.1.

## 1.2.1 – 2021-04-06

Changes:
 - Fix external subtitle support.
 - Fix skipping to previous song twice setting random volume.
 - Make easier to compile on Linux.

## 1.2.0 – 2021-04-06

Changes:

 - Add native music playback.
 - Fix HTTPS on Windows.
 - Remove breakpad.
 - Fix web player error "undefined onErrorInternal".

## 1.1.0 – 2021-04-05

Changes:

 - Added support for setting playback rate.
 - Added SyncPlay support. (Note there are still some glitches.)
 - Fixed issue where exiting video would go back a page.
 - Fixed issue where video reloads every time you seek.
 - Fixed some play/pause event issues.

## 1.0.0 – 2021-04-04

This is the first release of a new desktop player for Jellyfin which is based on, but not affiliated with, PlexMediaPlayer. It plays media in the webview instead of using a separate window like Jellyfin Desktop does and uses the same MPV playback engine. Note that SyncPlay is not supported and the client is currently considered experimental.
