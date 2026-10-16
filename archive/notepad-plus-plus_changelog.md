# Changelog: Notepad++

Quelle: https://notepad-plus-plus.org/downloads/
Stand: 24.09.2026 19:49

---

## 8.9.8.1 – 2026-09-24

**Notepad++ v8.9.8.1 vulnerability fixes, regression-fix, bug-fixes & new features**

- Vulnerability: Fix crash caused by “Open file” & “Search on Internet” commands. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-3hx4-x297-6752)
- Vulnerability: Fix Function List array out-of-bounds risks when parsing functions. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-9rr8-6vjg-gj52)
- Vulnerability: Fix UAC operations performed without verifying the caller. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-phqq-x4c2-7c2q)
- Vulnerability: Fix incomplete UNC detection allowing NTLM leak bypass. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-gr8w-74qx-pc2v)
- Vulnerability: Fix crash of NPPM API when invalid value passed as argument. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-8wmf-7r8c-wf2w)
- Regression: Fix failure to open files via Notepad++ symlink paths. (Fix [#18314](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18314))
- Fix a crash after canceling UAC saving operation. (Fix [commit](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/d68c048c59ad414fa5420bc4cdfd6edf9e6d12d2))
- Fix Network Path Warning dialog usability problem. (Fix [#18319 (comment)](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18319#issuecomment-5751250291))
- Fix symlinks setting for Folder as Workspace not remembered across sessions. (Fix [#18367](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18367))
- Fix continous validation of the same server when loading network path files. (Fix [#18319](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18319))
- Fix UDL line comments not being correctely detected. (Fix [#9193](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9193), [#18141](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18141))
- Fix Unicode text alternation in clipboard by Notepad++ encoding conversion. (Fix [#18356](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18356))
- Fix incorrect paste behaviour in column mode. (Fix [#18355](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18355))
- Fix visual glitch in the UDL dialog when main window uses vertical tabs. (Fix [#18335](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18335))
- Fix GDI leaks of tab context menu. (Fix [#18297](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18297))
- Fix inaccurate display information in PluginAdmin “Updates” tab. (Fix [#18312](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18312))

## 8.9.8 – 2026-08-23

**Notepad++ v8.9.8 vulnerability fixes, regression-fix, bug-fixes & new features**

- Vulnerabilty: Fix an eventual crash while loading UDL. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-5h8p-vvcf-xq8p)
- Vulnerabilty: Fix an eventual crash when loading a UTF-16 file. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-8jjh-4rq6-r2h8)
- Vulnerabilty: Fix out-of-bounds array write. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-h2wq-6x75-h8q2)
- Vulnerabilty: Fix authenticode verification bypass. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-cx87-7hhq-m2j3)
- Vulnerabilty: Fix a TOCTOU issue in the Notepad++ Updater (WinGUp). [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-hrvm-8rjc-v44x)
- Vulnerabilty: Fix session backup path-traversal allowing deletiion outside backup directory. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-hgmx-cr7v-p3c7)
- Vulnerabilty: Fix potential exposure of Windows login info (SMB/NTLM) via UNC path. [CVE ID not assigned yet 1](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-fw3m-3qpq-pvr8), [CVE ID not assigned yet 2](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-qmmp-22w3-mcwm), [CVE ID not assigned yet 3](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-rv8g-c295-pwcg), [CVE ID not assigned yet 4](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-7w2m-5769-p4q3)
- Vulnerabilty: Fix shortcuts.xml HMAC bypass via the “Run a Macro Multiple Times”. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-759j-g8j4-867p)
- Vulnerabilty: Fix Null pointer in NPPM_SAVESESSION handler causing crash. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-j85c-6wc9-p98p)
- Vulnerabilty: Fix stack buffer overflow caused by overlong session paths. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-pxgg-96p2-c3hx)
- Vulnerabilty: Fix Folder as Workspace “Run by system” target hijacking issue. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-w5xq-frjg-w4cw)
- Vulnerabilty: Fix install-path injection possibility with PowerShell. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-97rx-3h53-4cfj)
- Vulnerabilty: Fix lower IL (Integrity Level) process sends WM_COMMAND to higher IL Notepad++. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-grw6-cw7j-3qfg)
- Vulnerabilty: Fix Notepad++ UIPI Bypass via WM_COPYDATA. [CVE ID not assigned yet](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-pg39-63h5-cx35)
- Fix crash in WM_COPYDATA COPYDATA_PARAMS for invalid payload. (Fix [#18207](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18207))
- Fix crash in API NPPM_ALLOCATE* calls. (Fix [#18222](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18222))
- Add an option to allow loading symlinks in Folder as Workspace. (Fix [#18226](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18226))
- Regression: Fix loading session for alone subview and doc/tab with untitle name. (Fix [#18294](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18294))
- Fix CJK IME issues in Save As dialog. (Fix [#11582](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11582), [#15431](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15431), [#16772](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16772), [#12225](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12225), [#12366](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12366))
- Update to Scintilla 5.6.6 & Lexilla 5.5.3. (Implement [#18290](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18290))
- Add plugin deactivation capability. (Fix [#18206](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18206))
- Add “-monitoringMode” command line argument to open files with monitoring enabled. (Fix [#18188](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18188))
- Fix Proxy Settings issue in portable mode. (Fix [#13382](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13382))
- Fix langs.xml model update not not applying file extension fields. (Fix [#18220](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18220))
- Fix luminosity slider in ChooseColor not visible in dark mode. (Fix [#12451](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12451))
- Fix empty sub-menus in compact language menu. (Fix [#18202](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18202))
- Fix Search Results vertical scrolling not matching with OS mouse settings. (Implement [#18194](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18194))
- Use modern question mark icon in dark message box. (Fix [Repported in comment](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10171#issuecomment-4988491539))
- Format count numbers using current locale separators when needed. (Fix [#18190](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18190))

## 8.9.7 – 2026-07-14

**Notepad++ v8.9.7 vulnerability fixes, regression-fix, bug-fixes & new features**

- Vulnerability: Fix Stack Buffer Overflow in expandNppEnvironmentStrs. (Fix [CVE-2026-54758](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-gv94-327x-2gc5))
- Vulnerability: Enhance loading session.xml security by normalizing the file paths. (Fix [CVE-2026-52886](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-rqfm-pw34-r7j6))
- Vulnerability: Fix updater (WinGUp) path traversal (Zip Slip) issue.  (Fix [CVE-2026-57233](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-hjxw-84rf-wg5r))
- Vulnerability: Fix shortcuts.xml macro HMAC bypass issue. (Fix [CVE-2026-71858](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-f4rj-vqq4-wvg4))
- Vulnerability: Improve robustness of Powershell command in installer. (Fix [CVE-2026-73250](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-gp2r-262h-9hgf))
- Fix “Find in Files” unresponsive issue. (Fix [#11774](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11774))
- Fix regression where opening relative paths as file & in Explorer didn’t work. (Fix [#18114](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18114))
- Fix disappearing or duplicated file items in Folder as Workspace. (Fix [#10710](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10710), [#15831](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15831), [#16053](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16053), [#16197](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16197), [#18091](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18091))
- Fix freeze caused by directory symbolic links in Folder as Workspace root. (Fix [#1566](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/1566), [#18171](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18171))
- Update to Scintilla 5.6.4 & Lexilla 5.5.1. (Implement [#18193](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/18193))
- Fix undo in cloned document not scrolling to undone change in original document. (Fix [#17913](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17913))
- Fix crash issue caused by LexBaan. (Fix [#18186](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18186))
- Make XML CDATA color different from the enclosed elements. (Fix [#18122](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18122))
- Update pugixml to v1.16. (Implement [#18147](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18147))
- Remember Folder as Workspace expand/collapse state across sessions. (Fix [#4057](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4057), [#5979](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5979))
- Add “Count” option to improve Incremental Search performance. (Fix [#11613](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11613))
- Add “nth of count” information to Incremental Search. (Fix [#11899](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11899))
- Improve “Count” performance in Incremental Search. (Implement [#18185](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18185), [##18201](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/#18201), [#18209](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18209))
- Add full ANSI EscapeSequence lexing. (Fix [#17120](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17120), [#18065](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18065))
- Fix plugin toolbar icon not scaling correctly on high DPI displays. (Fix [#16723](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16723))
- Fix incorrectly disabled Paste command. (Fix [#18118](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18118))
- Add “Print FormFeed as Page Break” option. (Fix [#18059](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18059))
- Make message boxes dark via task dialogs. (Implement [#18132](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18132))
- Enhance color picker to remember custom colors across sessions. (Fix [#4782](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4782))
- Ensure searchResult stays last after styles XML merge. (Fix [issue](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/17299#issuecomment-4826979782))
- Update PHP keywords / auto-completion. (Implement [#18175](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18175))
- Update CSS keywords / auto-completion. (Fix [#13555](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13555))
- Fix truncted INS/OVR indicator on Status bar. (Fix [#18142](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18142))

## 8.9.6.4 – 2026-06-04

**Notepad++ v8.9.6.4 vulnerability fix regression-fix & bug-fix**

- Fix TOCTOU (Time-of-check to time-of-use) issue in HMAC implementation. (Fix [CVE-2026-52885](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-qm4c-qg8p-qfcr))
- Fix MSI installer regression that leaves old version entry in Add/Remove Programs. (Fix [#18071](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18071))
- Fix “Open Containing Folder in Explorer” launching extra explorer processes. (Fix [#17941](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17941))

## 8.9.6.2 – 2026-05-31

**Notepad++ v8.9.6.2 vulnerability-fixes**

- Fix bypass scenario ([CVE-2026-52884](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-p58x-r3c9-x9p6)) in the previously fixed vulnerability (CVE-2026-48800) that was not fully addressed. (Implement [commit](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/ea1508855e9c4528f6198ce9d345f13cb759ebf4))

## 8.9.6.1 – 2026-05-26

**Notepad++ v8.9.6.1 vulnerability-fixes**

- Fix bad formed COPYDATASTRUCT makes Notepad++ crash ([CVE-2026-48770](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-r39g-3mcw-xcg2)).
- Fix arbitrary code execution vulnerability via config.xml ([CVE-2026-48778](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-7hm3-wp5q-ccv9)).
- Fix arbitrary code execution vulnerability via shortcuts.xml ([CVE-2026-48800](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-3x3f-3j39-pj3v)).

## 8.9.6 – 2026-05-21

**Notepad++ v8.9.6 regression fixes, bug-fixes**

- Fix vulnerability (CVE-2026-46710) of v8.9.4 & v8.9.5 installer. (Implement [commit](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/1d4aabe2102d982667ead2dd974bee5e0b1f2d9c))
- Fix x86 installer regression of not showing installation entry in “Unstall a program” of Control Panel. (Fix [community discussion](https://community.notepad-plus-plus.org/topic/27531/notepad-release-8.9.5/4?_=1778972557613))
- Fix x86 installer regression where context menu not installed or uninstalled correctly. (Fix [community discussion](https://community.notepad-plus-plus.org/topic/27531/notepad-release-8.9.5/12?_=1779121076054))
- Fix UAC prompt display regression (“Notepad++ installer” instead of “Notepad++”) for Notepad++ v8.9.5. (Fix [GitHub comment](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/e49ab3219ed48f1c7cbc61c60c50d031e607821a#r185469222))
- Fix incorrect bevaviour when saving dirty read-only files. (Fix [#17956](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17956))
- Fix regression where saving a UDL file removed XML declaration. (Fix [GitHub comment](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/e338f80ef7399b519be20e10f480cb7d31a9fc9b#commitcomment-185005094))

## 8.9.5 – 2026-05-11

**Notepad++ v8.9.5 regression fixes, bug-fixes & new improvements**

- Fix updating issue where using v8.9.4 32-bits installer creates duplicate “Uninstall a program” entries. (Fix [#17979](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17979))
- Fix v8.9.4 64-bits installer error message caused by MSIX on Win10. (Fix [installer regression](https://community.notepad-plus-plus.org/topic/27512/notepad-release-8-9-4/4?_=1777481529353))
- Fix regression in UDL xml file EOL parsing issue. (Fix [#18022](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18022))
- Update Scintilla to 5.6.2 & Lexilla to 5.4.9. (Implement [#18011](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/18011))
- Add option to synchronize zoom level across views. (Fix [#17862](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17862))
- Fix MSI installer writting language info to HKCU instead of HKLM. (Fix [MSI issue](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2326#issuecomment-4291838308))
- Fix imported UDLs not appearing in the language menu without restarting Notepad++. (Fix [#17909](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17909))
- Make “(?)” tooltip in preferences & Find in Files dialogs persitant & reduce display delay. (Fix [#17995](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17995), [#16961](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16961))
- Fix visual glitch in Mark dialog when in reduced mode. (Fix [#17983](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17983))

## 8.9.4 – 2026-04-26

**Notepad++ v8.9.4 crash-fixexs, bug-fixes & new improvements**

- Fix crashes in FindInFiles when nativeLang.xml’s “find-result-hits” contains “%s”. (Fix [#17960](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17960), CVE-2026-3008, CVE-2026-6539)
- Fix drop-file crash when file path length reaches 259 characters. (Fix [#17921](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17921))
- Fix crash caused by undoing column editor bad input in virtual space. (Fix [#17915](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17915))
- Fix bad column editor input in reverse-direction column selection on virtual space. (Fix [#17915](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17915))
- Update to Scintilla 5.6.1 & Lexilla 5.4.8. (Fix [#17920](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17920), [#17864](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17864), [#13522](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13522), [#11746](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11746))
- Fix EOL conversion to Windows format not working (Scintilla update related). (Fix [#17920](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17920))
- Fix rendering corruption in .bat files (Lexilla update related). (Fix [#17864](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17864))
- Fix quote escaping causing incorrect JSON syntax highlighting (Lexilla update related). (Fix [#11746](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11746), [#13522](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13522))
- Fix MSI installation error due to context menu item registration. (Fix [#17918](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17918))
- Fix NSIS installation stalling caused by context menu registration issue. (Fix [#17308](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17308), [#17885](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17885))
- Add NPP_LANG property to install a specific localization file for MSI. (Fix [issue reported in comment](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2326#issuecomment-3583203052))
- Fix MSI installer display random Hexadecimal number as name on UAC. (Fix [#17967](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17967))
- Add version info into MSI file property (as value of “Comments”). (Fix [#17803](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17803))
- Fix minimized window not restoring in administrator mode. (Fix [#17945](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17945))
- Fix Unicode search mismatching ANSI character ‘?’. (Fix [#17125](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17125))
- Fix Column Editor regression with empty fields. (Fix [#17912](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17912))
- Fix floating dialog content not displaying in certain situations. (Fix [#17563](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17563))
- Fix visual glitch when toggling group view in Document List. (Fix [#14285](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14285))
- Support improved C++ 11 raw string literal handling. (Fix [#17875](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17875))
- Fix visual glitch in the Mark dialog. (Fix [#16084](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16084), [#17886](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17886))

## 8.9.3 – 2026-03-24

**Notepad++ v8.9.3 regression fixes, bug-fixes & new improvements**

- Regression fix: a crash in User Defined Language. (Fix [#17520](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17520))
- Regression fix: installing (or removing) plugin re-opens Notepad++ with permanent admin privilege (Fix [#17540](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17540))
- Regression-fix: wrongly added parenthesis for some multi-bytes characters. (Fix [#17521](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17521), [#17802](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17802))
- Regression-fix: incorrect function list text display for non-UTF8 documents. (Fix [#17847](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17847))
- Regression-fix: ProjectPanel Workspace text localization issue. (Fix [community report](https://community.notepad-plus-plus.org/topic/27437/localization-problem))
- Regression-fix: Change History margin not enabled by default. (Fix [comment repport](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/dc6a1168da8cb7aa021a8ff2f1fcc762ab10626b#commitcomment-177846109))
- Regression-fix: Notepad++ update & plugin download fail behind corporate MITM proxies. (Fix [community report](https://community.notepad-plus-plus.org/topic/27427/plugins-admin-gets-curl-error))
- Security enhancement: Update cURL to v8.19.0 in auto-updater (WinGUp) to fix cURL security issue (CVE-2025-14819). (Fix [#17869](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17869))
- Improve performance by migrating the XML parser from TinyXML to pugixml. (Fix [#16175](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16175))
- Update Scintilla to 5.6.0 & Lexilla to 5.4.7. (Implement [#17562](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17562))
- Fix the issue where printing caused Notepad++ to crash. (Fix [#6126](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6126), [#12645](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12645), [community report #1](https://community.notepad-plus-plus.org/topic/16133/notepad-7-5-8-64bit-is-crashing-while-printing-initiates), [community report #2](https://community.notepad-plus-plus.org/topic/16202/printing-issue), [community report #3](https://community.notepad-plus-plus.org/topic/13241/printer-preferences-crash-with-64-bits-version-of-npp-7-3-1-while-32-bits-version-is-ok?_=1773673896806))
- Fix Find in Files failing to search file content on disk. (Fix [#16177](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16177), [#17070](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17070))
- Add disableNppAutoUpdate.xml to disable auto-update when WinGUp (GUP.exe) is present. (Implement [#17836](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17836))
- Fix a memory leak on exit. (Fix [#17817](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17817))
- Fix installed auto-completion files not overwritten after update. (Fix [#14749](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14749))
- Add model capacity of shortcuts.xml & contexMenu.xml for administration. (Fix [#17872](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17872))
- Add an option to disable selected text drag-and-drop. (Fix [#2571](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2571), [#11335](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11335))
- Fix wrong theme-writing path for non-ProgramFiles installations. (Fix [comment repport](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12252#issuecomment-3948209565))
- Enhancement: prevent XML config files from being overwritten when updating portable package (copy/paste). (Fix [#9755](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9755), [#14279](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14279), [#15120](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15120))
- Fix incomplete Find dialg tab translation when 1st opêned from Project Panels. (Fix [community report](https://community.notepad-plus-plus.org/topic/27437/localization-problem))
- Fix Notepad++ spawning a new Windows Explorer process in Task Manager. (Fix [comment repport](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17524#issuecomment-3919405684))
- Add Function List & Autocompletion for D language. (Fix [#17349](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17349))

## 8.9.2 – 2026-02-16

**Notepad++ v8.9.2 new security enhancements, feature, regression fix & bug-fix**

- Security enhancement: Make updater check integrity & authenticity of server-returned XML (XMLDsig). (Implement [#17441](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17441))
- Security enhancement: Fix untrusted search path vulnerability by launching explorer.exe (Fix [CVE-2026-25926](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-rjvm-fcxw-2jxq))
- Security enhancement: Make auto-updater (WinGUp) even more secured. ([Remove unsecured options](https://github.com/notepad-plus-plus/wingup/commit/14b6a1a5444ad68c78db009128c6f759f1871ed3), [remove dll dependency](https://github.com/notepad-plus-plus/wingup/commit/c172e6874551d02814e1474cc6662fd4c9bd8eb2), [launch only signed program for plugin management](https://github.com/notepad-plus-plus/wingup/commit/8894320b18f31ea551ce06406466ac4915683d6c))
- Fix a plugin installation crash due to incorrect processing catch. (Fix [#issue](https://github.com/notepad-plus-plus/nppPluginList/issues/873))
- Add redact selection feature - Default: █, Modifier (Shift + Click): ●. (Fix [#17363](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17363))
- Fix context menu shortcut localization not aligning to the right regression. (Fix [#17467](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17467))

## 8.9.1 – 2026-01-26

**Notepad++ v8.9.1 new security enhancement, features, regression fixes & bug-fixes**

- Fix EOL duplication regression when playing back old recorded macros. (Fix [issue](https://community.notepad-plus-plus.org/topic/27339/enter-key-duplicated-in-macros))
- Remedy search failure for pasted text containing trailing invisible EOL character. (Fix [#17124](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17124), [#17187](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17187))
- Fix customized context menu regression where separator (id=“0”) escapes FolderName submenu. (Fix [#17342](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17342))
- Fix issue where a single undo reverted multiple changes after macro execution. (Fix [#9426](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9426))
- Fix visual glitch when dragging dockable dialogs on a 2nd monitor. (Fix [#16805](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16805), [#16155](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16155), [#16077](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16077))
- Fix inconsistent automatic search mode switching (RegEx to Extended) in Find dialog. (Fix [#17227](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17227))
- Fix incorrect URL parsing caused by Unicode special spaces. (Fix [#16856](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16856))
- Update to Boost 1.90.0. (Implement [#17326](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17326))
- Improve update themes feature: fix JavaScript.js edge case. (Fix [issue](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/17347#issuecomment-3753234119))
- Update javascript.js to better match javascript (embedded) in all themes. (Fix [issue](https://community.notepad-plus-plus.org/post/104325), [report](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/17299#issuecomment-3695060206))
- Function List: enhance for Perl & PHP; add for Nim. (Fix [#17382](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17382), [#17327](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17327), implement [#17377](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17377))
- Fix comments and highlighting in TCL. (Fix [#17315](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17315))
- Update perl syntax highliging keywords and autocomplete for 5.42. (Fix [#17332](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17332))
- Improvement: display Find dialog status message with invisible characters warning. (Fix [#17345](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17345))

## 8.9 – 2025-12-27

**Notepad++ v8.9 new security enhancement, features, regression fixes & bug-fixes**

- Remove Notepad++ self-signed certificate signature, use only the certificate issued by GlobalSign. (Fix [#16806](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16806))
- Security enhancement: Log security errors automatically in “%LOCALAPPDATA%\Notepad++\log\securityError.log” (Implement [#17305](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17305), [#WinGUp](https://github.com/notepad-plus-plus/wingup/commit/e84ada2e32763b3ef0ccc6826e5caaab71a92d66))
- Fix jarring color regression in dark mode (introduced in v8.8.9). (Fix [#17289](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17289))
- Fix “/noUpdater” installer option not working if updater was previously installed. (Fix [#17287](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17287))
- Fix column mode edit undo regression (introduced in v8.8.9). (Fix [#17295](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17295), [#17272](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17272), [#16784](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16784))
- Fix issue where an empty file opened without encoding under a UTF-8 system codepage. (Fix [#17258](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17258))
- Add makefile function list parser. (Fix [#17293](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17293))
- Improve performance & add missing file ext. from langs.model.xml to langs.xml.(Fix [#17290](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17290), implement [#17314](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17314), implement [#17306](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17306))
- Improve “Open containing folder in Explorer” command to avoid creating Explorer process. (Fix [#17060](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17060))
- Allow updating mouse scroll amount according to OS settings changes. (Implement [#17300](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17300))

## 8.8.9 – 2025-12-09

**Notepad++ v8.8.9 new security enhancement, features, regression fixes & bug-fixes**

- Vulnerability-fix: verify certificate & signature on downloaded update installer. (Implement [Notepad++ commit](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/bcf2aa68ef414338d717e20e059459570ed6c5ab), [WinGUp commit](https://github.com/notepad-plus-plus/wingup/commit/ce0037549995ed0396cc363544d14b3425614fdb))
- Fix corrupted file loading on Windows system using the full UTF-8 code page. (Fix [#17234](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17234))
- Fix crashing when hashing SHA-256 for large files. (Fix [#17243](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17243))
- Fix “Select & Find Next” command not working regression. (Fix [#17200](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17200))
- MSI improvement: Add NOUPDATER option & suppress REBOOT. (Fix [#ref1](https://community.notepad-plus-plus.org/topic/27250/notepad-8-8-8-release/12), [#ref2](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2326#issuecomment-3578029731))
- Fix Perl Function List causes Notepad++ to freeze on tab switch regression. (Fix [#17152](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17152))
- Fix context menu truncated regression on localization change. (Fix [#17249](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17249))
- Add ability to update users’ langs.xml & stylers.xml from model XML files. (Fix [#17128](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17128))
- Update to Scintilla 5.5.8 & Lexilla 5.4.6. (Update [#17191](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17191))
- Add feature to sort lines in a document by length. (Fix [#15615](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15615), [#17186](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17186))
- Undo & redo enhancement: restore vertical scroll position after undo & redo. (Fix [#17194](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17194))
- Fix mouse wheel horizontal scrolling amount not respecting Windows setting. (Fix [#9480](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9480))
- Fix document map regression with keyboard input. (Fix [#17224](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17224))
- Fix wrong system font scaling on Windows 7. (Fix [#17066](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17066))
- Update to nlohman json 3.11.3. (Update [#15041](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15041))

## 8.8.8 – 2025-11-18

**Notepad++ v8.8.8 new features, regression fixes & bug-fixes**

- Add Notepad++ MSI (x64) for enterprise IT deployment. (Fix [#2326](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2326), [#2368](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2368), [#16767](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16767))
- Security enhancement: prevent Notepad++ Updater from being hijacked. (Implement [#17116](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17116), [commit](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/3daa59326d32f75b53cdc737fa7f8e841330daf5))
- Fix multi-selection crash (regression) when smart highlighting is enabled. (Fix [#17086](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17086), [#17126](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17126))
- Add tab label length limitation option to have reasonable tab width. (Fix [#3332](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3332), [#5563](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5563), [#12563](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12563), [#16417](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16417))
- Improve the performance of saving session on exit. (Implement [#17079](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17079))
- Fix Distraction free mode disabling tab bar hiding regression. (Fix [#17102](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17102), [#16831](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16831))
- Add text scale support. (Fix [#16427](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16427), [#17167](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17167), [#17129](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17129))
- Fix switching among some encoding not working issue. (Fix [#17033](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17033))
- Fix Notepad++ not handle system default code page UTF-8 well. (Fix [#17057](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17057))
- Improve Rust handling: keywords and autoCompletion. (Fix [#16904](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16904))

## 8.8.7 – 2025-10-20

**Notepad++ v8.8.7 new enhancement & bug-fixes**

- Sign Notepad++ binaries with GlobalSign certificate to fix false-positive alerts. (Fix [#16971](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16971), [#16809](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16809), [#16812](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16812), [#16770](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16770), [#16773](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16773), [#16779](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16779), [#16785](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16785), [#17062](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17062))
- Fix Monitoring in one view affects selections and position in second view. (Fix [#17046](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17046))
- Fix Shortcut Mapper memory leak issue. (Fix [#17069](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17069))
- Enhance Perl FunctionList for class. (Fix [#17043](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17043))
- Fix pressing Alt or Tab causes controls redrawing problem in UDL dialog. (Fix [#17061](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17061))

## 8.8.6 – 2025-10-07

**Notepad++ v8.8.6 new features & bug-fixes**

- Add capacity of pasting multiline into Find/Replace fields. (Fix [#16952](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16952))
- Improve UAC in Notepad++ for seamless elevated operations. (Fix [#886](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/886), [#8655](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8655), [#9561](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9561), [#10302](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10302), [#14990](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14990), [#15008](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15008), [#15137](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15137), [#15323](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15323))
- Fix Pin Tab operation being too long with many opened documents. (Fix [#16117](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16117))
- Add 2 new full-readonly modes via command line argument (-fullReadOnly & -fullReadOnlySavingForbidden). (Fix [#15993](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15993), [#16532](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16532))
- Add apply/remove read-only for all documents commands. (Fix [#15993](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15993), [#16532](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16532))
- Column Editor enhancement: GUI input fields now support radix to match the output format. (Fix [#16912](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16912))
- Add Window dialog “File Modified Time” sorting capacity. (Fix [#16953](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16953))
- Fix NPPN_CMDLINEPLUGINMSG not working issue & define the pluginMessage usage protocol. (Fix [#17024](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17024), [#17022](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17022))
- Fix pasting from column mode to multi-selection issue due to different EOL. (Fix [#16889](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16889))
- Add NPPM_GETNPPSETTINGSDIRPATH message to get Notepad++ settings directory path. (Fix [#16944](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16944))
- Enhance SQL function list parser. (Fix [#16605](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16605))
- Fix C# function list not working with comments. (Fix [issue](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3643#issuecomment-1455254475))
- Add function list ability for CSS. (Implement [#17006](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17006))
- Allow user to customize max selected chars to auto-fill “Find what” field. (Fix [#16955](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16955))
- Restore undo/redo behaviour in Find/Replace fields after Copy/Paste or Ctrl-F. (Fix [issue 1](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/16976#issuecomment-3265850195), [issue 2](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16952#issuecomment-3263821316))
- Fix text corruption issue caused by selection within multibyte characters. (Fix [#16879](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16879))
- Fix DOCTYPE styling in xml and html. (Fix [#17012](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/17012))
- Fix double clicking on edit zone’s border creates a new tab issue. (Fix [issue](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/16561#issuecomment-2938756492))
- Update cURL in WinGUp (Notepad++ updater) for fixing CVE-2025-5399. (Fix [security issue](https://github.com/notepad-plus-plus/wingup/commit/696508ebe25bb78a07119e80644ac3a1f4341ea4))

## 8.8.5 – 2025-08-14

**Notepad++ v8.8.5 regression-fix**

- Fix “Edit with Notepad++” context menu not being installed correctly regression. (Fix [#16913](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16913))

## 8.8.4 – 2025-08-12

**Notepad++ v8.8.4 regression-fixes, bug-fixes & new features**

- Fix -notabbar & asNotepad.xml stop hiding tabbar regression (from v8.7.9). (Fix [#16794](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16794))
- Fix “Edit with Notepad++” not removed by uninstaller regression (from v8.8.3). (Fix [#16896](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16896))
- Fix possible heap memory leak. (implement [#16883](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16883))
- Increase search input length from 2046 to 16383. (Fix [#1088](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/1088), [#16749](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16749))
- Add warning tip for the max length on search input (Find/Replace). (Fix [#16749](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16749))
- Fix JavaScript listed twice in Language & Indent settings of Preferences issue. (Fix [#4521](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4521), [#16861](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16861), [#16884](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16884))
- Fix external lexers showing several time in Indent settings issue. (Fix [#16462](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16462))
- Add button to insert variables in the run dialog. (implement [#16820](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16820))
- Enhance “Go to settings”: guide users to the related setting explicitly. (Fix [#16846](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16846))
- Add a clear button for filter field in Shortcut Mapper. (Fix [#15742](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15742))
- Make NFO font overridable by adding font name in Lexer “nfo” of stylers.xml. (Fix [#16839](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16839))

## 8.8.3 – 2025-07-09

**Notepad++ v8.8.3 security-fixes & new enhancement**

- Use self-signed certificate to sign new release binaries. (Implement [commit](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/03063ebf4b2861ae15382e8eba8e8c0d87c53614))
- Fix uninstaller security issue (CVE-2025-49144). (Fix [#16787](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16787))
- Enhance security for DLL loading. (Fix [#13964](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13964))

## 8.8.2 – 2025-06-30

**Notepad++ v8.8.2 regression-fixes, bug-fixes & new features**

- Fix regression of folding state not being remembered through sessions. (Fix [#16597](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16597), [#16670](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16670))
- Fix “Go To Settings” links in Style Configurator regression (from v8.8). (Fix [#16592](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16592))
- Fix small regression of tab background (hovered) highlighting issue after drag&drop. (Fix [#16559](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16559))
- Fix an unresponsive (hang) issue due to hide lines. (Fix [#16316](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16316))
- Fix installer security issue by using the absolute path instead of an unspecified path (CVE-2025-49144). ([commit](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/f2346ea00d5b4d907ed39d8726b38d77c8198f30), fix [report on GitHub](https://github.com/notepad-plus-plus/notepad-plus-plus/security/advisories/GHSA-g5rj-m8mm-cgw6), fix [#16744](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16744))
- Installer component “WinGUp”: update cURL to 8.13.0 for fixing cURL’s security issue CVE-2025-0167. (Fix [#16531](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16531), [#16515](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16515))
- Update to scintilla 5.5.7 & Lexilla 5.4.5. (Implement [#16649](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/16649))
- Add feature to update Notepad++ on exit. (Fix [#16601](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16601), [#13749](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13749), [#10317](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10317), [#8495](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8495), [#8457](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8457), [#3755](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3755))
- Add “/relaunchNppAfterSilentInstall” command argument for installer. (Fix [#issue](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/15280#issuecomment-2246816010))
- Add feature to set read-only attribute on file so user can toggle (set/remove) read-only attribute of a file. (Fix [#326](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/326), [#4594](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4594), [#6216](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6216), [#7841](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7841), [#12520](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12520), [#15571](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15571), [#16603](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16603))
- Add new plugin API: NPPM_GETTOOLBARICONSETMODE & NPPN_TOOLBARICONSETCHANGED to get toolbar icon set choice. (Fix [#16547](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16547), [#16646](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16646))
- Deprecate 3 APIs: Deprecate NPPM_GETOPENFILENAMES, NPPM_GETOPENFILENAMESPRIMARY & NPPM_GETOPENFILENAMESSECOND. (Fix [#15997](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15997))
- Add new feature of using first line of untitled document for its tab name. (Fix [#3994](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3994), [#16584](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16584))
- Enhance NPPM_DARKMODESUBCLASSANDTHEME: Enable darkmode progress bar for plugins. (Fix [#16675](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16675))
- Various dark mode enhancements. (Fix [#16668](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16668), [#16674](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16674), [#16560](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16560), [#16537](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16537), [#issue](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/16548#issuecomment-2884419833))
- Fix right click on caption bar unhidding main menu. (Fix [#16652](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16652))
- Fix rename tab error message when tab name is unchanged. (Fix [#16661](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16661))
- Fix Python FunctionList absorbing next function issue if space after colon. (Fix [#16636](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16636))
- Remove .log from errorlist lexer’s default extensions. (Fix [#16627](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16627))
- Make raw string syntax highlighting work for Golang. (Fix [#16609](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16609))
- Fix Notepad++ tray icon lost after Windows Taskbar crashing & being relaunched. (Fix [#16588](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16588))
- Fix changing toolbar icon set not updating to matching panel icon set. (Fix [#16595](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16595))
- Fix Windows dialog file list not react with keystroke (character match). (Fix [#2239](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2239))
- Add “*” mark on modified file entries in “Windows” dropdown menu. (Fix [#16542](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16542))

## 8.8.1 – 2025-05-05

**Notepad++ v8.8.1 regression-fixes, bug-fixes & new features**

- Fix ShortcutMapper regression (from v8.7.6) of displaying wrong shortcut while editing. (Fix [#16491](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16491))
- Fix Find in files progress bar visual regression (from v8.8). (Fix [#16504](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16504))
- Fix search result cut off result content due to nul characters (’\0’). (Fix [#6281](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6281), [#15216](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15216), [#16466](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16466))
- Add Locale-based line sort feature. (Fix [#13456](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13456), [#927](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/927), [#8481](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8481), [#11261](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11261), [#16406](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16406), [#16409](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16409))
- Enable selection history for undo & redo. (Fix [#16488](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16488))
- Fix plugins removal failure issue (fixed in WinGUp).(Fix [#16364](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16364), [#15673](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15673), [#11819](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11819), [#9148](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9148), [WinGUp #82](https://github.com/notepad-plus-plus/wingup/issues/82))
- Fix tab settings for external lexers cannot be saved issue. (Fix [#16460](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16460))
- Add ErrorList syntax highlighting. (Fix [#16437](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16437), [#8078](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8078))
- Fix disabled Paste command with no previous text-data in clipboard. (Fix [#16456](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16456))
- Fix wrong directory opened for opening files issue. (Fix [#16465](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16465))
- Improve Find dialog look & feel (more space).

## 8.8 – 2025-04-28

**Notepad++ v8.8 new features, regression-fixes & bug-fixes**

- Update to Scintilla 5.5.6 & Lexilla 5.4.4. (Implement [#16373](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16373))
- Fix a hanging issue on regexp regression. (Implement [#16371](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16371))
- Fix vertical tab bar messed up regression. (Fix [#16385](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16385))
- Add option to apply different color to fluent toolbar icons. (Fix [#16369](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16369), [#15430](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15430))
- Add “Show only pinned button” option to prevent from inaccurate click. (Fix [#15963](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15963))
- Fix broken cloned file state after Notepad++ restart. (Fix [#16412](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16412))
- Fix inactive buffer reloading problem. (Fix [#16344](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16344))
- Dark mode enhancements: combobox, slider, treeview edit, inactive menu bar & toolbar chevron. (Fix [#16349](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16349), [#16379](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16379), [#16418](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16418), [#16445](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16445), [#10103](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10103))
- Reorganize GUI (add Toolbar & Tab Bar sections) of Preferences dialog. ([Commit](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/e45f72ae390c7672d9448769cff10c6ad9bcb63e), Implement [#16459](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16459))
- Fix invalid dot-character(s) handling in filenames checking. (Fix [#16328](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16328))
- Fix crash when using custom toolbar icons. (Fix [#16366](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16366))
- Add class & method recognization ability for JavaScript function list. (Fix [#13013](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13013))
- Remove toolbarIcons.xml, use toolbarButtonsConf.xml for toolbar custom icons & hidding buttons. (Fix [#16402](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16402))
- Add GUI option in Preferences dialog instead of using zero length enableSelectFgColor.xml. (Fix [#16391](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16391))
- Fix “Keep selection when right-click outside of selection” not working issue. (Fix [#16325](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16325))
- Fix Find dialog status text too left visual glitch. (Fix [#16359](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16359))
- Force npcNoInputC0 value as “true” by default to avoid C0 code input. (Fix [#16326](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16326), [#15839](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15839), [#15729](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15729))
- Remove “-pluginMessage” argument unnecessary restriction. (Fix [#16273](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16273))
- Fix an easter egg not showing issue. (Fix [#15170](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15170))

## 8.7.9 – 2025-04-02

**Notepad++ v8.7.9 regression-fixes, bug-fixes & new features**

- Fix incorrect syntax highlighting regressions. (Fix [#16271](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16271), [#16309](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16309) - Revert 4 of v8.7.8)
- Update to Scintilla 5.5.5 & Lexilla 5.4.3. (Implement [#16235](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16235))
- Fix bug where plugin button hiding settings in toolbarButtonsConf.xml are ignored. (Fix [#16280](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16280))
- Fix SQL Backslash Escape preference not taking effect immediately. (Fix [#16244](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16244))
- Add new low-level DirectX11 DirectWrite 1.1 Scintilla rendering mode. (Implement [#16284](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16284))
- Add versions of external libraries (Scintilla/Lexilla/Boost) to Debug Info. (Fix [#11466](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11466))

## 8.7.8 – 2025-03-08

**Notepad++ v8.7.8 regression-fixes, bug-fixes & new features**

- Fix regression (v8.7.1 - v8.7.7) of saving backup file without modifications. (Fix [#16186](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16186))
- Fix syntax highlighting regression while switching among UDL files. (Fix [#16154](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16154))
- Add ability to hide selected toolbar buttons via a XML configuration.(Fix [#15106](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15106), [#15440](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15440), [#16000](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16000))
- Optimize switching programming language performance for large files. (Fix [#16106](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16106))
- Improve folding/unfolding performance for large files. (Fix [#16064](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16064))
- Fix SQL Backslash Preference state regression (from v8.7). (Fix [#16249](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16249))
- Fix count operation on regex causing Notepad++ to hang. (Fix [#16207](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16207))
- Fix FunctionList not refreshing with current document lexer changes. (Fix [#16221](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16221))
- Improve Style Configurator GUI organization. (Fix [#15939](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15939))
- Adds SAS programming language support. (Fix [#16148](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16148))
- Make existing DirectWrite rendering modes accessible. (Fix [#16126](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16126))
- Allow DirectWrite use on non-Core Windows Server. (Fix [#15916](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15916))
- Use VTS instead of LTS for specific control code abbreviation. (Fix [#16107](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16107))
- Fix installer silent mode doLocalConf.xml setting handling issue. (Fix [#16233](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16233))

## 8.7.7 – 2025-02-07

**Notepad++ v8.7.7 regression-fix**

- Add new API NPPM_ADDSCNMODIFIEDFLAGS for some plugins to fix eventual regression regarding SCN_MODIFIED.  (Fix [#16121](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16121))

## 8.7.6 – 2025-01-28

**Notepad++ v8.7.6 bug-fixes & enhancements**

- Update to scintilla 5.5.3 & Lexilla 5.4.1. (Fix [#10528](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10528), [#15801](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15801), [#15817](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15817), implement [#15982](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15982))
- Enhance performance of syntax highlighting for large files. (Fix [#15952](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15952))
- Make “Show close/pin button on each inactive tab” optional. (Fix [#15912](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15912), [#16035](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16035))
- Add ShortcutMapper Multilingual ability, allowing the use of specific keys for non-en-US keyboards.  (Fix [#14395](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14395), [#15966](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15966), [#16071](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16071))
- Fix vertical tab crashes when enabling/disabling the pin tab feature. (Fix [#16033](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16033))
- Fix crash when passing an invalid buffer with NPPM_SETUNTITLEDNAME. (Fix [#15970](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15970))
- Fix floating panels position resetting regression in multi-monitor configurations. (Fix [#15498](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15498), [#16077](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16077))
- Fix incorrect “Replace all” behavior during the second replace in selection. (Fix [#14897](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14897), [#14624](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14624), [#15992](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15992))
- Fix backup file renaming bug for untitled tabs. (Fix [#16043](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16043))
- Enhance UX in “Find in file” action when the Directory field is empty. (Fix [#16051](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16051))
- Make the current line/position copyable in the Go to Line dialog. (Fix [#15950](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15950))
- GUI enhancement: hide right menu shortcuts on the fly. (Implement [#16065](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16065))
- Minor enhancements for JavaScript, CSS & HTML. (Fix [#15821](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15821), [#15825](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15825), [#16036](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/16036))

## 8.7.5 – 2024-12-25

**Notepad++ v8.7.5 regression-fixes, bug-fixes & enhancements**

- Fix nfo file losing modification issue (regression from v8.7.4). (Fix [#15964](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15964))
- Fix network file wrong modification detection (regression from v8.7.1). (Fix [#15819](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15819))
- Fix regression “Open Selected PathName(s)” command not working while all selected. (Fix [#15960](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15960))
- Fix unusuability after deleting files in split view. (Fix [#15922](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15922))
- Fix unsaved documents lost on next launch if portable Notepad++ change path. (Fix [#1587](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/1587), [#15886](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15886))
- Refactoring for the better performance & smaller binary size. (Fix [#15898](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15898))
- Improve “Copy Selected Lines” command. (Fix [#15803](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15803))
- Add Visual Basic function list. (Fix [#3239](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3239))
- Add Swift, TypeScript, and Go for advanced Auto-indent. (Fix [#15900](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15900))
- Fix UDL comment line not working due to conflict with stream comment definition. (Fix [#11897](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11897))
- Enhance “Follow current doc.” GUI action/option in Find in files. (Fix [#15908](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15908))
- Fix Reload Workspace not working. (Fix [#11551](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11551))
- Add “Show details” functionality in installer. (Fix [#15718](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15718))

## 8.7.4 – 2024-12-05

**Notepad++ v8.7.4 fix regression & bug-fixes**

- Fix regression of multi-line tabbar height not updated after closing tabs. (Fix [#15905](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15905))
- Fix the extension defined by user not override language default extensions. (Fix [#8035](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8035), [#8304](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8304), [#10609](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10609), [#15826](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15826))
- Fix encoding of nfo file cannot be changed bug. (Fix [#8823](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8823), [#9153](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9153), [#13905](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13905))

## 8.7.3 – 2024-11-31

**Notepad++ v8.7.3 fix regressions & new enhancements**

- Fix a crash while disabling “Pin tab” feature. (Fix [#15860](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15860))
- Fix drag&drop a folder in Notepad++ launch redundant dialog regression. (Fix [#15869](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15869))
- Fix docked panels invisibility in multi-instance mode. (Fix [#15873](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15873))
- Add “Pin/Unpin Tab” context menu item. (Fix [#15852](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15852))
- Add “Close All BUT Pinned” command. (Fix [#15863](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15863))
- Fix a possible buffer overflow issue. (Fix [#15850](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15850))

## 8.7.2 – 2024-11-27

**Notepad++ v8.7.2 new features & bug-fixes**

- Add Pin tab feature. (Fix [#5786](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5786), [#8377](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8377), [#12806](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12806), [#14216](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14216))
- Tabbar enhancement: Hide inactive tab Close & Pin buttons. (Fix [#15298](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15298))
- Tabbar enhancement: Highlight inactive darken tab on mouse hover. (Fix [#15791](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15791))
- Fix Ctrl-C not doing copy from Search result issue. (Fix [#15739](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15739))
- Add “Minimize / Close to” option for System tray. (Fix [#15771](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15771))
- Add ability to open/copy selected files from Search-results. (Fix [#15741](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15741))
- Fix replace field focus losing when Notepad++ is switched back. (Fix [#6021](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6021))

## 8.7.1 – 2024-11-04

**Notepad++ v8.7.1 bug-fixes & enhancements**

- Update cURL in Notepad++ updater (WinGUp) for fixing cURL’s CVE-2024-7264 issue. (Fix [#73](https://github.com/notepad-plus-plus/wingup/issues/73))
- Fix opened network files hanging while the network disconnected. (Fix [#4306](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4306), [#6178](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6178), [#8055](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8055), [#11388](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11388), [#12553](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12553), [#15540](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15540))
- Fix not being able to open folder via cammand argument regression. (Fix [#15645](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15645))
- Update to Scintilla 5.5.3 & Lexilla 5.4.1. (Fix [#15228](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15228), [#15368](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15368), [#15650](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15650))
- Fix modified Find dialog status msg colors not being remembered throu sessions. (Fix [#15724](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15724))
- Fix hanging issue while hiding lines. (Fix [#15630](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15630))
- Make left behide hide line close marker removable. (Fix [#15713](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15713))
- Fix Find dialog status bar wrong messaging (regression). (Fix [#15662](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15662))
- Fix URL parsing issue with ‘?’ after ‘#’. (Fix [#13583](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13583))
- Add “Close to system tray” ability.  (Fix [#4075](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4075), [#11627](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11627))
- Add tab created time tooltip for new opened untitled tab. (Fix [#15563](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15563))
- Improve GUI to avoid user confusion between Global override & Default Styles. (Fix [#15640](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15640))

## 8.7 – 2024-09-17

**Notepad++ v8.7 bug-fixes & enhancements**

- Update to scintilla 5.5.2 & Lexilla 5.4.0. (Implement [#15564](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15564))
- Fix monitoring large files with frequent writes freezing the UI issue. (Fix [#9661](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9661), [#15611](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15611))
- Fix regression of multiple selections in comboboxes of Find dialog. (Fix [#15583](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15583))
- Fix a single undo reverting many changes issue. (Fix [#9426](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9426))
- Improve Styler Configurator performance considerably. (Fix [#12436](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12436), implement [#15565](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15565))
- Fix CVE-2014-9456 (but CVE-2014-9456 is not a “Security Vulnerability”). (Fix [#12669](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12669))
- Make find dialog status messages color customizable via Style Configurator. (Fix [#5087](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5087))
- Make individual tab color customizable via Style Configurator. (Fix [#12156](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12156))
- Add new plugin command NPPM_GETNATIVELANGFILENAME & notification NPPN_NATIVELANGCHANGED for native language being changed. (Fix [#15513](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15513))
- Fix Folder as Workspace sorting problem for network storage (Samba, WebDAV, WSL, etc.). (Fix [#10557](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10557), [#15397](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15397))
- Fix closing unsaved clone document causing periodic backup loss issue. (Fix [#8227](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8227))
- Fix Style Config’s “User-defined keywords” not being saved properly after emptying it. (Fix [#15543](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15543), [#14303](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14303))
- Add user-defined keyword ability for some supported programming languages (ActionScript, ASP, Bash, C, C++, C#, GDScript, Go, HTML, Java, JS, JSP, Lua, PHP, Python, RC, Swift, TypeScript, & XML). (Fix [#15520](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15520))
- Add Fluent Icons for enhancing FunctionList, Folder as Workspace & project panels’ icons in lite mode. (Implement [#15541](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15541), [#15532](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15532))
- Fix Python smart indent issue when a string or comment line ends with a colon. (Fix [#15528](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15528), [#15534](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15534))
- Add file type filters for UDL in Save dialogs. (Fix [#8083](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8083), [#11096](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11096))
- Add TOML language (TOML format) support. (Fix [#5631](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5631))
- Add function list for TeX/LaTeX. (Implement [#15595](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15595))
- Recognize Cython files as Python. (Fix [3069#](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3069), [#3767](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3767))
- Fix edit zone not getting focus while clicking the active tab. (Fix [#8446](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8446))
- Add the ability to open the copy automatically after the “Save a Copy” command. (Fix [#11861](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11861))
- Fix inability to paste after removing read-only via menu. (Fix [issue](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13742#issuecomment-2233570312))
- Add one more option for auto-indent so C-Like language indent can be disabled. (Fix [#15396](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15396))
- Fix Style Configurator regression: “URL hovered”’s “Go to Settings” not working. (Fix [#15493](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15493))

## 8.6.9 – 2024-07-14

**Notepad++ v8.6.9 bug-fixes & enhancements**

- Make installation and updates easy & quiet by adding “Yes (Silent)” button. (Fix [#8514](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8514))
- Add new options ‘/closeRunningNpp’ & ‘/runNppAfterSilentInstall’ in the installer. (Implement [#15230](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15230), implement [#15280](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15280))
- Fix crash of “Next Search Result” command on the empty search result. (Fix [#15247](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15247))
- Fix the regression where the Find dialog size is not remembered across sessions. (Fix [#15294](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15294))
- Fix the regression of content lost by using Encoding “Convert to…” commands. (Fix [#15324](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15324), [#15271](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15271), [#3054](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3054), possibly [#9426](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9426))
- Fix the regression of exception/crash on Windows Server Core 2022. (Fix [#15313](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15313))
- Prevent DirectWrite from being enabled under Windows Server. ([commit](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/6b441b738a951ed225632f4085a46c95cd4aa13f))
- Enhance the quality of Fluent toolbar icon sets for different DPI settings. (Fix [#15253](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15253))
- Improve the look & feel of tabbar close button in dark mode. (Fix [#15321](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15321), implement [#15326](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15326))
- Improve the dark mode tab bar icon in the search results panel. (Implement [#15286](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15286))
- Add ability to pre-populate the predefined color sets for custom tones. (Fix [#15055](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15055))
- Add “Show All Character” popup menu on toolbar button. (Fix [#14832](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14832))
- Fix the rectangular selection copy-paste bug. (Fix [#15139](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15139), [#15151](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15151))
- Allow opening shortcut files (*.lnk) directly if the file extension is changed. (Fix [#9643](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9643), [#11089](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11089), [#10139](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10139))
- Fix the lost panels issue. (Fix [#13084](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13084))
- Add Backspace unindent option. (Fix [#15180](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15180))
- Fix CSS more indentation bug. (Fix [#14962](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14962))
- Include F13-F24 keys in Shortcut Mapper. (Fix [#11975](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11975))
- Fix the problem where the last empty clean untitled tab cannot be closed after renaming. (Fix [#15306](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15306))
- Add plugin a command (NPPM_SETUNTITLEDNAME) to rename untitled tab. (Fix [#8916](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8916))
- Display a message box with information about disabled backward regex searching. (Fix [#15239](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15239))
- Fix the display glitch for unsaved tabs containing tab characters. (Fix [#15202](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15202))
- Fix status bar and tab bar flicker during the GUI updated (fixed only for dark mode). (Fix [#15260](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15260))
- Fix the issue with “Begin/End Select” command after deletion. (Fix [#15221](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15221))
- Resolve the integer overflow problem in the Column Editor. (Fix [#15167](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15167))
- Adjust the position of hits text in the File Progress dialog. (Fix [#13426](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13426), [#15244](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15244))
- Fix the deployment of other software blocked due to NppShell. (Fix [#62](https://github.com/notepad-plus-plus/nppShell/issues/62))

## 8.6.8 – 2024-06-04

**Notepad++ v8.6.8 bug-fixes & enhancements**

- Fix a crash in Column Editor caused by an arithmetic overflow. (Fix [#15144](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15144))
- Fix the issue where any negative repeat value in Column Editor causes a hang. (Fix [#15153](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15153))
- Fix an extra space being inserted in HEX mode issue in Column Editor. (Fix [#15168](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15168))
- Fix a visual glitch of the toolbar pressed buttons in dark mode. (Fix [#15225](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15225))
- Add auto-indent feature for Python. (Fix [#15122](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15122))
- Fix the issue where “show control characters” settings not remembered when switching to another tab. (Fix [#13988](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13988))
- Fix the missing monitoring disabled state icon from the fluent icon set on the toolbar. (Fix [#15217](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15217))
- Adjusted the inaccurate naming of indent settings in thee Preferences dialog. (Fix [issue](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15180#issuecomment-2129892136))
- Fix the issue where the customized color of active tab in inactive view is missing. (Fix [#15140](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15140))
- Introduce a new plugin command “NPPM_GETTABCOLORID” to retrieve the current tab color ID. (Fix [#15115](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15115))
- Allow the tree view dark mode customization for plugins. (Fix [#15077](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15077))
- Fix the popup dialog for updating not metioning ‘Notepad++’. (Fix [#14668](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14668))

## 8.6.7 – 2024-05-13

**Notepad++ v8.6.7 bug-fixes & enhancements**

- Fix regression of multi-edit cursors placed wrongly issue. (Fix [#15126](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15126))
- Fix multi-editing not showing multiple cursors in dark mode. (Fix [#15075](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15075))
- Add auto-completion for Go & Raku, function list for Raku. (Implement [#15128](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15128))
- Fix symbol ‘&’ not showing in Document Switcher. (Fix [#15117](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15117))
- Allow syntax highlighting for custom tags in HTML. (Fix [#15093](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15093))
- Fix dialogs out of screen problem. (Fix [#11240](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11240), [#14913](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14913))

## 8.6.6 – 2024-05-10

**Notepad++ v8.6.6 bug-fixes & enhancements**

- Update to scintilla 5.5.0 & Lexilla 5.3.2. (Merge [#15042](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15042))
- Fix crash when crossing the 2GB file size threshold. (Fix [#14944](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14944), [#14981](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14981))
- Fix a performance issue due to URL recognition.  (Fix [#13916](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13916))
- Update to nlohman json 3.11.3. (Merge [#15041](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15041))
- Fix multi-edit resists escape after typing issue. (Fix [#14649](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14649))
- Make F3 & Shift-F3 work in Find Replace dialog. (Fix [#2138](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2138))
- Allow Ctrl-TAB to switch tabs in FindReplace, PluginAdmin and UDL dialogs. (Fix [#7932](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7932), [#14975](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14975))
- Add programming language support for Go & Raku(Perl 6). (Fix [#8090](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8090), [#4465](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4465))
- Fix user defined auto-insert not working issue. (Fix [#3171](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3171), [#8063](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8063), [#12547](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12547), [#14831](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14831))
- Enhance GUI: resize checkboxes/radio buttons as text length needs. (Fix [#15006](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15006))
- Enhance GUI: make sizing arrows more coherent in Find dialog. (Fix [#15099](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15099))
- Fix URL enclosed in apostrophes or backtick not working issue. (Fix [#14978](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14978), [#14323](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14323),  [#14212](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14212))
- Fix wrong dropped file view issue. (Fix [#14951](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14951))
- Fix Korean(한)/English(영) key not working regression. (Fix [#14400](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14400), [#14973](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14973))
- Fix the tab labels of some dialogs being cut in Dark mode. (Fix [#11012](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11012))
- Fix close button disappeared issue in Find Replace dialog. (Fix [#14940](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14940))
- Apply dark theme to checkbox buttons on Windows 11. (Fix [#14929](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14929))
- Fix menu bar cluttered in Dark Mode issue. (Fix [#10130](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10130))
- Fix Debug Info minor display regression. (Fix [#14921](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14921))
- Enhance Lua language syntax highlighting. (Fix [#7615](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7615), [#15081](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/15081))
- Improve the function list support for Ada. (Fix [#14908](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14908), [#14687](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14687),  [#14498](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14498))

## 8.6.5 – 2024-03-30

**Notepad++ v8.6.5 bug-fixes & enhancements**

- Fix “Replace All” action not notifying plugins of modification regression by adding NPPN_GLOBALMODIFIED. (Fix [#14767](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14767), see [NPPN_GLOBALMODIFIED how to](https://community.notepad-plus-plus.org/topic/25504/new-nppn_globalmodified-notification))
- Fix plugins not receiving some Scintilla notification types regression. (Fix [issue](https://community.notepad-plus-plus.org/topic/25497/notepad-release-8-6-4/9))
- Fix Shortcut Mapper pontential crash problem. (Implement [#14880](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/14880))
- Fix period backup pontential crash due to the dead lock. (Fix [#14906](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14906))
- Fix NUL characters file corruption after a power outage. (Fix [#6133](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6133), implement [#14860](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/14860))
- Workaround session loss problem due to Dell SupportAssist’s bug. (Fix [#14781](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14781), implement [#14858](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/14858))
- Fix URLs are not detected after a “Replace All” regression. (Fix [#14864](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14864))
- Notify user while saving failure due to hardware problem. (Implement [#14842](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/14842))
- Update to scintilla 5.4.3 (from 5.4.1) & Lexilla 5.3.1. (Implement [#14834](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/14834))
- Support template literal (template strings) in JavaScript & make `back-quoted strings` more readable. (Fix [#3822](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3822))
- Add support for Change History in the text, besides in the margin. Also, make Change History color configurable. (Fix [#12321](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12321), [#13915](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13915), Implement [#14838](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/14838))
- Fix NPPM_RELOADFILE API return wrong result issue. (Fix [issue](https://community.notepad-plus-plus.org/topic/25533/nppm_reloadfile-should-return-true-_only_-on-success/4))
- Enhance Shortcut Mapper filter to find the command items more easily. (Fix #[14743](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14743))
- Prevent typing control characters into document & make it optional. (Fix [#13279](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13279))
- Fix possible no-GUI state when using systray. (Fix [#14777](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14777))
- Make context menu popup location at current text position when invoked via keyboard. (Fix [#14727](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14727))
- Fix Notepad++ blocked when closed minimized or from systray. (Fix [#14718](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14718))
- Fix Mouse Wheel Scrolling in Shortcut Mapper & reduce also the memory use. (Fix [#14895](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14895))
- Fix Python wrong decorator attribute colors & add “ATTRIBUTE” color in styles.xml.model. (Fix [#5894](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5894))

## 8.6.4 – 2024-02-20

**Notepad++ v8.6.4 regression-fix**

- Fix regression that the view cannot be activated by mouse clicking. (Fix [regression](https://community.notepad-plus-plus.org/topic/25490/notepad-release-8-6-3/7?_=1708380779619))

## 8.6.3 – 2024-02-18

**Notepad++ v8.6.3 bug-fixes & enhancements**

- Restore multi-editing option & add “Column To Multi-editing” option on GUI. (Fix [#14645](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14645))
- Make “copy/cut line while no selection” optional. (Fix [#14638](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14638))
- Fix all open files lost after restarting as Admin to save a file. (Fix [#14694](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14694))
- Fix “Replace All” crash & performance issue. (Fix [#14630](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14630))
- Fix calltip crash due to the division by zero. (Fix [#14664](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14664))
- Enhance Function List for Python to support “async def” & colons in argument list. (Fix [#13908](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13908))
- Fix Copy/Cut/Paste issue in Vertical Edge text field in preferences dialog. (Fix [#13874](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13874))
- Fix macro recording twice for some commands. (Fix [#5217](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5217), [#14634](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14634))
- Fix “Open File” command not working with TAB preceded. (Fix [#14543](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14543))
- Add auto-completion keywords for PHP, JavaScript and CSS. (Fix [#14635](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14635), [#14705](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14705))

## 8.6.2 – 2024-01-14

**Notepad++ v8.6.2 fixed regressions**

- Fix Shift-DEL, Ctrl-INS and Shift-INS not working regression. (Fix [#14470](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14470), [#14571](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14571))
- Fix Ctrl+V cannot paste into the text fields of certain plugins regression. (Fix [#14568](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14568))
- Remove option “disableLineCopyCutDelete.xml” (the empty file takes no effect).
- Fix a regression: the position in the previous session is now restored correctly in cloned document. (Fix [#14164](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14164))

## 8.6.1 – 2024-01-05

**Notepad++ v8.6.1 new features & bug-fixes**

- Updated to Scintilla 5.4.1 & Lexilla 5.3.0. (Implement [#14375](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14375))
- Fix a regression: the position in the previous session is now restored correctly in cloned document. (Fix [#14164](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14164))
- Fix a regression: customized extension in Style Configurator is now saved correctly. (Fix [#14437](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14437))
- Add an ability (disableLineCopyCutDelete.xml) to disable line copy/cut/delete when no selection is made and also add back  Shift-DEL & Ctrl-INS shortcuts. (Fix [#14470](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14470), [ref](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14296#issuecomment-1866679990), [ref](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14401#issuecomment-1833326429)))
- Add an ability (noColumnToMultiSelect.xml) to disable column mode to multi-select mode. (Fix [#14464](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14464), [ref](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14296#issuecomment-1848076816))
- Fix deleting in column mode also delete an unexpected EOL. (Fix [#14426](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14426))
- Fix hidden results of long lines for Search results with “Find in…” commands. (Fix [#12023](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12023))
- Enhance Search-results by showing search options for “Find in…” commands. (Fix [#14306](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14306))
- Fix an issue: replacements are no longer duplicated (the 2nd time in cloned document) for “Replace in Opened Docs”. (Fix [#14505](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14505))
- Fix a regression to make F3 & Shift-F3 work again in Incremental Search. (Fix [#14503](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14503))
- Add document tab navigation commands: “First tab” & “Last tab”. (Fix [#14416](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14416))
- Add document tab commands: “Move to Start” & “Move to End” commands. (Fix [#9525](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9525), [#13982](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13982))
- 3 RTL new abilities: RTL per document, RTL per document remembered across the sessions & new attribute editZoneRTL=“no” in RTL localization files. (Fix [#9665](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9665), [#9950](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9950), [#14385](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14385))
- Enhance the “-loadingTime” command line parameter. (Fix [#14472](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14472))
- Enhance the performance: disable undo collection while loading a file. (Fix [#14455](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14455))
- Sort language list in the Preferences dialog. (Fix [#14245](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14245))
- Fix a visual glitch that occurred during multi-paste. (Fix [#14410](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14410))
- Fix confusing memory allocation error message. (Fix [#14418](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14418))
- Fix python wrong decorator attribute color. (Fix [#5894](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5894))
- Fix file status in “other view” is not detected. (Fix [#14225](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14225))
- Fix dropped file being opened in the wrong view. (Fix [#14354](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14354))

## 8.6 – 2023-11-23

**Notepad++ v8.6 new features & bug-fixes**

- Multi-edit is fully supported in Notepad++. (Fix [#14266](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14266), [#8203](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8203))
- Make multi-select background & caret colours customizable. (Fix [#14302](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14302))
- Make session inaccessible files remembered (empty & read-only document as placeholder). (Fix [#12079](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12079), [#12744](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12744), [#13696](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13696))
- Fix missing session invalid error for user session & enhance API NPPM_GETNBSESSIONFILES. (Fix [#14228](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14228))
- Fix network shared files saving regression. (Fix [#14300](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14300))
- Update Scintilla to v5.3.8 & Lexilla to v5.2.8. (Fix [#13442](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13442), [#14188](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14188), [#14288](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14288))
- Fix docking panel crash due to messing up config.xml. (Fix [bug report](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13084#issuecomment-1783787209)
- Fix invalid styler.xml making Notepad++ crash issue. (Fix [#12101](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12101))
- Fix tab-closing crash by middle mouse button (unexpected mouse position). (Fix [#14328](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14328))
- Fix 2 performance issues in Style Configurator. (Fix [#14321](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14321))
- Add 3 line operation (delete, copy & cut) shortcuts. (Fix [#14296](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14296))
- Display extra info in the status bar of Find/Replace dialog to avoid PEBKAC. (Fix [#14307](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14307))
- Fix “Hide lines” command hiding unselected lines issue. (Fix [#14166](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14166))
- Fix silent installer mode when Notepad++ is running issue. (Fix [#10189](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10189), [#10277](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10277), [#22514](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/22514), [#14236](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14236), fix partially [#8514](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8514))
- Fix Updater’s vulnerability (update cURL in WinGUp for fixing CVE-2023-38545). (Fix [WinGUp issue #50](https://github.com/notepad-plus-plus/wingup/issues/50))
- Fix incoherent behaviour of “Duplicate Current Line” menu command. (Fix [#5298](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5298))
- Fix JSON5 not using JSON keywords. (Fix [#14205](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14205))
- Fix empty message showing while cancelling session file saving dialog. (Fix [#14235](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14235))

## 8.5.8 – 2023-10-17

**Notepad++ v8.5.8 bug-fixes and new features**

- Fix “Clear Read-Only Flag” command not working immediately regression. (Fix [#14138](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14138))
- Fix saving files losing Alternate Data Stream issue. (Fix [#1498](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/1498), [#8451](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8451), [#8013](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8013))
- Fix data loss issue due to no room on disk for saving. (Fix [#5664](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5664), [#14089](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14089))
- Add Win10/Win11 Restart-application feature. (Fix [#9722](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9722), [#11721](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11721), [#11934](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11934))
- Fix user created session being modified behaviour on exit. (Implement [part 1](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/85d5f972a8f4507f5e462541cd8b372f059b1fa7), [part 2](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/09499725de6d9dee4ee25de61488428d16dcabd4), [part 3](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/8e43b0adbaed0353a7a97c2ff4e2da3e2dc8efa8))
- Improve document list display performance. (Fix [#13479](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13479), [#12632](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12632))
- Update Scintilla to v5.3.7 & Lexilla to v5.2.7. (Fix [#13991](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13991), [#14062](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14062))
- fix unwanted Afrikaans installer language issue. (Fix [#3844](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3844), [#7574](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7574))
- Fix a crash issue while reading settings from cloud. (Fix [#14131](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14131))
- Fix  security issue CVE-2022-31901. (Fix [#13520](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13520))
- Enhance non-saved search text’s persistence in Find dialog combobox while pressing arrow key. (Fix [#14174](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14174))
- Make auto-checking of Find InSelection configurable (resizable & can be disabled). (Fix [#14108](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14108), [#13677](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13677), [#12639](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12639))
- Perl enhancement: Update Stylers & the keywords for Perl v5.38. (Fix [#14192](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14192))
- Fix “Single Line Uncomment” uncommenting an extra line issue. (Fix [#12829](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12829))
- Fix “Next Bookmark” command not resetting current column issue. (Fix [#14137](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14137))
- Allow menu command Window->Windows to be assigned a shortcut. (Fix [#14179](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14179))
- Fix wrong categories in Shortcuts Mapper. (Fix [#13285](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13285))

## 8.5.7 – 2023-09-08

**Notepad++ v8.5.7 bug-fixes and new features**

- Fix 4 security issues CVE-2023-40031, CVE-2023-40036, CVE-2023-40164 & CVE-2023-40166. (Fix [#14073](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14073))
- Security enhancement: Sign uninstall.exe. (Fix [#14099](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14099))
- Change the slogan in installer. (Fix [#14052](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14052))
- Fix eventual memory leak while reading Utf8-16 files. (Fix [#4120](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4120), [#5806](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5806), [#4443](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4443))
- Fix dragging tab performance issue while Document List is displayed. (Fix [#13479](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13479), [#12632](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12632))
- Add suppress 2GB file warning option for x64. (Fix [#14055](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14055))
- Fix cloned document disassociated issue after Notepad++ being relaunched. (Fix [#10266](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10266))
- Fix session file saving problem if it’s read-only. (Fix [#14024](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14024), [#13894](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13894), [#13859](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13859))
- Fix activating wrong file(s) issue after loading session file. (Fix [#14006](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14006))
- Fix product version value displayed in file’s properties. (Fix [#14010](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/14010), [#11886](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11886), [#11431](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11431))

## 8.5.6 – 2023-08-15

**Notepad++ v8.5.6 bug-fixes and new features**

- Fix plugin crash regression due to CET enhancement. (Fix [regression due to CET](https://community.notepad-plus-plus.org/post/88577))
- Add new API: indicator allocation for plugins. (Fix [#5744](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5744))
- Fix hide lines merging to avoid merging across a visible line. (Fix [#12844](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12844))
- Fix “Clear Change History” issue: cloned document markers are not cleared. (Fix [#13877](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13877))

## 8.5.5 – 2023-08-09

**Notepad++ v8.5.5 bug-fixes and new features**

- Update to Scintilla 5.3.6 and Lexilla 5.2.6 (Implement [#13940](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13940), fix [#4741](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4741),  [#13901](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13901), [#13943](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13943), [#13911](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13911))
- Add change history navigation commands: Go to next/prev change & Clear change history. (Fix [#12248](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12248))
- Fix Change History incorrect display after “Reload from Disk” command. (Fix [#12319](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12319), [#12261](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12261), [#13735](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13735))
- Remember through sessions the directory of “Remember last used directory”. (Fix [#11326](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11326), [#10901](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10901), [#4961](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4961), [#4119](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4119))
- Fix regression of double clicking on find result not going to the document. (Fix [#13636](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13636))
- Fix regression of opening file rejection if file name contains dot at the end. (Fix [#12849](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12849))
- Fix error message of opening file with ‘=’ as end of file name. (Fix [#13344](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13344))
- Fix menu Tools contains 2 SHA-256 item while using localization. (Fix [#13797](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13797))
- Fix SHA-1 hash result wrong length bug while “Treat each line as a separate string” enabled. (Fix [#13812](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13812))
- Add SHA-512 hash features (Fix [#13805](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13805))
- Fix normal.xml for Normal text auto-completion not working issue. (Fix [#12325](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12325))
- Fix Korean IME append file extension issue in save dialog. (Fix [#11582](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11582), [#12225](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12225), [#12366](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12366))
- Make find/replace in files result more accurate while used RegExpr is invalid. (Fix [#13164](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13164))
- Fix Project panel’s inaccurate initialized path in save dialog. (Fix [#13086](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13086))
- Fix wrong syntax highlighting of URLs with quotes in JSON. (Fix [#13522](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13522))
- Fix Clipboard History panel shows corrupted data issue. (Fix [#13817](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13817), [#13844](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13844))
- Improve lines sorting memory consumption. (Fix [#10435](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10435))
- Enhance “Add new document at startup”: add new document only when the session is remembered. (Fix [#13796](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13796))
- Enhance “Convert case to Proper Case” command: fix the error conversion after quote.

## 8.5.4 – 2023-06-18

**Notepad++ v8.5.4 bug-fixes and new features**

- Fix macro recording regression on Unicode character. (Fix [#13757](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13757))
- Fix regression of defective detection for file read-only attribute removal via Explorer. (Fix [#13742](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13742))
- Fix opening multi-files on multi-instance mode regression. (Fix [#36](https://github.com/notepad-plus-plus/nppShell/issues/36), [#13778](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13778))
- Update: Scintilla 5.3.5 Lexilla 5.2.5. (Implement  [#13729](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13729))
- Fix Notepad++ hanging issue running macro to EOF. (Fix [#13342](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13342))
- Fix EOL symbol color/appearence being reset issue while changing encoding. (Fix [#13728](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13728))
- Enable code folding in Assembly source files. (Fix [#13758](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13758), [#9888](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9888))
- Fix document language not remembered through sessions issue. (Fix [#13743](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13743))
- Add SHA-1 hash features. (Fix [#13791](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13791))
- Add “open new blank document in addition on startup” ability. (Fix [#11134](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11134), [#9535](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9535), [#5527](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5527))
- Fix lexer plugin is sorted unconventionally in language menu issue (Fix [#9516](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9516))
- Add message NPPM_DARKMODESUBCLASSANDTHEME to allow plugin to use generic dark mode. (Fix [#13574](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13574))
- Add the ability to close multiple files without saving in Document list. (Fix [#13768](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13768), [#13178](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13178))
- Several GUI Enhancements. (Fix [#13764](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13764), [#10349](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10349), [#8109](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8109), [#13703](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13703), [#13701](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13701), [#13686](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13686), [#13665](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13665), [#13657](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13657), [#13676](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13676), [#13667](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13667), [#13624](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13624), [#13622](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13622))
- Fix error message on uninstallation. (Implement [#13653](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13653))
- Fix tabContextMenu_example.xml not being deleted while uninstallation. (Fix [#13670](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13670))

## 8.5.3 – 2023-05-15

**Notepad++ v8.5.3 bug-fixes and new features**

- Fix session file data loss issue. (Fix [#13514](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13514))
- Fix Explorer context menu “Edit with Notepad++” needs restarting os to appear issue under Win 8⁄10. (Fix [#13](https://github.com/notepad-plus-plus/nppShell/issues/13))
- Fix Explorer context menu “Edit with Notepad++” not installed for multiple users issue. (Fix [#13476](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13476))
- Fix Explorer context menu “Edit with Notepad++” double entries in some applications (Winzip). (Fix [#13499](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13499))
- Make Explorer context menu “Edit with Notepad++” translatable. (Fix [#17](https://github.com/notepad-plus-plus/nppShell/issues/17))
- Add the UTF8 character ability for Run & Macro menu. (Fix [#12670](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12670), [#13221](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13221), [#13488](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13488))
- Add hide/show ability of Control Characters (C0 & C1) and Unicode EOL. (Fix [#8111](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8111))
- Fix Change history margin in black color issue. (Fix [#12764](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12764), [#13593](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13593))
- Improve “Remove consecutive duplicate lines” command performance. (Fix [#5538](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5538), [#12548](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12548))
- Project Workspace “Save a Copy As” confusion issue. (Fix [#13135](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13135))
- Make “Remove consecutive duplicate lines” support more line break. (Fix [#13474](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13474))
- Fix UDL deletion issue. (Fix [#8101](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8101))
- Fix RTL not working on FindInFiles progress window. (Fix [#13458](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13458))
- Fix search results output alignment for large file searches. (Fix [#13481](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13481))
- Several GUI Enhancements. (Fix [#13615](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13615), [#13601](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13601), [#12812](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12812), [#13579](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13579), [#13577](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13577), [#13575](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13575), [#13597](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13597), [#13524](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13524), [#13540](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13540), [#13544](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13544), [#13315](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13315))

## 8.5.2 – 2023-04-06

**Notepad++ v8.5.2 bug-fixes and new features**

- Enhance “Edit with Notepad++” context menu and fix several issues. (Fix [#13399](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13399), [#13410](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13410), [#13425](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13425), [#13438](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13438), [#13440](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13440), [#13446](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13446), [#13457](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13457))
- Make Find/Replace dialog swap/copy button usage more explicit. (Fix [#13368](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13368), [#13021](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13021))
- Fix unexpected caret column jump post brace match. (Fix [#13433](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13433))
- Add hits in-progress increased number to Search Progress dialog. (Fix [#13364](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13364))
- Add HTML Hexadecimal column and more items to ASCII panel. (Fix [#13347](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13347))
- Add ability to do leading spaces with Column Editor. (Fix [#11148](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11148), [#13309](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13309))
- Add programming language support for Hollywood. (Implement [#13417](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13417))
- Fix dock panels visual glitch while finding in search results. (Fix [#13402](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13402), [#13459](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13459))
- Fix Mark dialog’s Copy Marked Text button is not macro-able issue. (Fix [#13405](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13405))
- Dark mode enhancement: make focused combobox more visible. (Fix [#13420](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13420))
- Fix find dialog flicker issue. (Fix [#9536](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9536), [#13381](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13381))
- Enhance Notepad++ icon’s display in system tray. (Fix [#8971](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8971))
- Fix some options in Mark dialog not remembered though the session issue. (Fix [#13277](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13277))

## 8.5.1 – 2023-03-24

**Notepad++ v8.5.1 bug-fixes and new features**

- Use new modern shell “Edit with Notepad++” of Windows 11 instead of hijacking “Pin to Quick access”.(Fix [#13320](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13320), implement [#13330](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13330))
- Update scintilla to 5.3.4 and lexilla to 5.2.4. (Implement [#13338](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13338))
- Add MS Transact-SQL support. (Fix [#5940](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5940), [#7988](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7988), [#11718](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11718), [#12610](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12610), [#13160](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13160))
- Add GDScript language support with autocomplete & functionlist. (Fix [#13329](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13329))
- Fix UDL empty button regression after changing localization. (Fix [#13228](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13228))
- Add ability to copy “Find what” to “Replace with” and vice versa in Find Replace dialog. (Fix [#12122](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12122))
- Fix DocSwitcher RTL problem, and use edit field instead of a small popup value dialog. (Fix [#13244](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13244), [#13248](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13248))
- GUI visual enhancement: Fix whole dialog items blink when a item value changed. (Fix [#13230](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13230))
- Make tray icon context menu translatable. (Fix [#11628](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11628))

## 8.5 – 2023-03-06

**Notepad++ v8.5 bug-fixes and new features**

- Fix notepad replacement opening file name containing white space regression. (Fix [#13032](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13032))
- Fix regression about visual glitch of Find in Files progress window & Document Switcher.(Fix [#13185](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13185), [#13053](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13053))
- Update to Scintilla 5.3.3 and Lexilla 5.2.2. (Implement [#13082](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13082))
- Add new explorer context menu entry “Edit with Notepad++” for WINDOWS 11. (Fix [#10320](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10320), [#10565](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10565), [#4368](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4368), [#8786](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8786), [#10640](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10640), [#10856](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10856), [#10653](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10653), [#7747](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7747), [#6169](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6169), [#92](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/92))
- Add show non-printable characters command. (Fix [#827](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/827), [#4731](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4731), [#8284](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8284))
- Apply tab colors to document list items, and add groups to document list. (Fix [#12155](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12155), [#12689](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12689), [#13026](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13026))
- Add middle mouse click ability to close doc in Document List. (Fix [#12949](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12949))
- Add Begin/End Select in Column Mode command. (Fix [#12833](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12833), [#12832](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12832))
- Add option to make auto-completion list brief. (Fix [#12783](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12783))
- Remove duplicate items in function/word list of Auto-completion. (Fix [#13061](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13061))
- Fix missing items in word autocomplete. (Fix [#13060](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13060))
- Fix autocomplete to sort case insensitive issue. (Fix [#12495](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12495))
- Change behaviour: make Select and Find (Next/Previous) always in normal search mode. (Fix [#3229](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3229))
- Change behaviour: make volatile Find uses least-strict option settings. (Fix [#13145](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13145))
- Change behaviour:  Don’t populate in Find what if a stream selection more than 1024 characters. (Fix [#12603](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12603))
- Fix wrong value set in Preferences->Performance->“Define Large File Size”.(Fix [#13280](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13280))
- Fix untitled document number jumping or repeated problem. (Fix [#8677](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8677), [#11704](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11704), [#13194](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13194))
- Fix dock-able panels not restoring for mono instances when Notepad++ is in the tray. (Fix [#9454](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9454))
- Fix panels not restored from systemtray with “Edit with Notepad++” in admin mode. (Fix [#13041](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13041))
- Fix hit text in search results not being scrolled in the view issue. (Fix [#13129](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13129))
- Add new notification NPPN_EXTERNALLEXERBUFFER for lexer plugin with buffer ID when a new lexer is applied to the buffer in question. (Fix [#12351](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12351))
- Fix Synch H/V Scrolling commands not sync with 2 views. (Fix [#5250](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5250), [#13071](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13071))
- Add several GUI enhancement. (Fix [#11695](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11695), [#13176](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13176), [#13187](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13187), [#13162](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13162))
- Make several GUI items translatable. (Fix [#13175](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13175), [#8020](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8020), [#8858](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8858), [#13088](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/13088), [#8927](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8927), [#10876](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10876), [#9343](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9343), [#8004](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8004))

## 8.4.9 – 2023-01-31

**Notepad++ v8.4.9 bug-fixes and new features**

- Fix saving 4GB+ files file size cutting off issue. (Fix [#12526](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12526))
- Fix v8.4.8 hanging while opening some Pascal files. (Fix [#12822](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12822))
- Add JSON5 support, only JSONC currently (with js comment supported). (Fix [#11676](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11676/), [#11713](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11713))
- Add configuration for panels to ignore ‘-nosession’. (Fix [#9710](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9710))
- Fix Notepad Replacement display ‘Cannot open file “ “’ regression in v8.4.8. (Fix [#12775](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12775))
- Fix Notpad++ hangs while deleting search results results. (Fix [#12555](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12555))
- Fix XML tag-matching not be case-sensitive. (Fix [#10011](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10011))
- Add support selection for “EOL to Space” commands, “TAB and Space conversion” commands & trim operations.(Fix [#12720](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12720), [#12745](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12745), [#12702](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12702), [#12602](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12602), [#12658](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12658))
- Improve Pascal/Delphi function list performance. (Fix [#12693](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12693/), [#12687](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12687), [#12808](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12808))
- Fix exclude functions in comment zones in C++, PHP, JavaScript and Pascal. (Fix [#12759](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12759))
- Use stable sort algorithm instead of standard sort one. (Fix [#12678](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12678))
- Fix doc switcher not using alternate icon sets. (Fix [#12242](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12242))
- Enhance dark mode. (Fix [#12713](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12713/), [#12737](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12737))
- Fix hand cursor on URL too small display under high DPI issue. (Fix [#12772](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12772))
- Fix docking GUI regression for plugin in light mode. (Fix [#12007](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12007))
- Fix cannot undo “Block Uncomment” & “Insert Date/Time” commands in one shot. (Fix [#12830](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12830/), [#12831](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12831))
- Fix sub-menu folder display mess in non-western languages under Macro/Run menu. (Fix [#12670](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12670))

## 8.4.8 – 2022-12-25

**Notepad++ v8.4.8 bug-fixes and new features**

- Update to Scintilla 5.3.2 and Lexilla 5.2.1. (implement [#12624](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12624))
- Dark mode: Add “Follow Windows dark/light mode” feature, and toolbar, tabbar and theme choices are remembered for 2 modes separately. (Fix [#9183](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9183), [#9992](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9992), [#10153](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10153), [#10239](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10239), [#10544](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10544), [#11867](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11867), [#10644](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10644))
- Fix inconsistencies at OS-forced Notepad++ v8.4.8 exit. (Fix [#12541](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12541))
- Make tab context menu customizable. (Fix [#12170](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12170))
- Make Macro & Run menu organizable with submenu by modifying shortcuts.xml. (Fix [#5349](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5349), implement [#12617](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12617))
- Fix crash on Win32 Namespace prefixed file name. (Fix [#12453](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12453))
- Fix delimiter selection crash issue. (Fix [#12384](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12384))
- Improve performance for the “Remove Empty Lines” command. (Fix [#12462](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12462), implement [#12544](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12544))
- Fix theme not working in cloud mode and portable mode issue. (Fix [#6092](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6092/), [#10801](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10801), [#12296](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12296))
- Fix autocomplete/calltip colors not applied when changing themes. (Fix [#12514](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12514))
- Add dark autocompletion icons for dark themes. (Fix [#12549](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12549))
- Fix search result not applying new theme. (Fix [#12588](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12588/))
- Fix sorting failure in zero-length column mode selection. (Fix [#12299](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12299))
- Fix Default Language not working for the 1st empty file with empty session. (Fix [#12586](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12586))
- Enhance “Go to settings” in Style Configurator. (Implement [#12650](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12650), [#12634](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12634))
- Fix themes’ inconsistent behaviour. (Fix [#12642](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12642), [#12508](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12508))
- Fix incorrect plugin architecture reports partially. (Fix partially [#12565](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12565))
- Enhance Properties file: add/improve the syntax folding/highlighting. ([Implementation](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/c0e207328057b9ce321587a053ff1476cbb19562))
- Add vertical scroll bar on all combobox in Find Replace dialog. (Fix [#12459](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12459))
- Function List: Add Pascal/Delphi & NppExec plugin’s scripting, enhance SQL. (Fix [#3664](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3664/), [#12517](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12517), implemnt [#12625](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12625))
- Autocompletion: add PowerShell, fix some entries in PHP, update for Lua.  (Fix [#12492](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12492), implement [#12641](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12641), [#12657](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12657))
- Update CPP & PowerShell keywords. (Fix [#11936](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11936/), [#5004](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5004))
- Fix the tab context menu reload command’s state not synchronized. (Fix [#12579](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12579))

## 8.4.7 – 2022-11-08

**Notepad++ v8.4.7 bug-fixes and new features**

- Fix empty session issue due to forced Windows update restart. (Fix [#9850](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9850), [#12389](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12389), [#5737](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5737), [#4148](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4148), [#2730](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2730)… and [much more](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/12388#issuecomment-1296337508))
- Fix printing with extra background colors issue due to Change History. (Fix [#12281](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12281))
- Update to scintilla 5.3.1 and lexilla 5.2.0. (Implement [#12327](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12327))
- Updated nlohmann json to 3.11.2 and boost to 1.80.0. (Implement [#12271](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12271), [#12273](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12273))
- Make large file restriction configurable. (Fix [#11389](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11389), [#12260](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12260), [#11670](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11670))
- Optimize open/save large files time. ( [Commit](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/a26599794cfd5bc7c6754d240e7563f24b90e4cb))
- Remember Column Editor settings through the sessions. (Implement [#12386](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12386))
- Fix plugin admin search issue. (Fix [#12375](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12375))
- Installer enhancement: prevent arm64 installer from installing on non ARM64 system. (Fix [#12320](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12320))
- Installer enhancement: remember “Don’t use_%APPDATA%” option. (Fix [#12202](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12202))
- Add new API NPPM_GETBOOKMARKID for getting bookmark ID. (Fix [Commit](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/4d5069280900ee249d358bc2b311bdb4b03f30a9))
- Enhance “Go To” dialog: update line/position data dynamically. (Fix [#12284](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12284))
- Fix lines hiding issue. (Fix [#12184](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12184), [#8149](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8149))
- Fix language detected from content not applied if default language is set. (Fix [#11504](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11504))
- Fix long filters get truncated in Find in Files feature. (Fix [#12041](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12041))
- Add ESC Key for aborting “Move to Recycle Bin” confirmation prompt. (Fix [#12117](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12117))

## 8.4.6 – 2022-09-29

**Notepad++ v8.4.6 bug/regression-fixes and new features**

- Add Change History markers for document saved/unsaved/undone modification. (Fix [#12164](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12164), [#12046](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12046))
- Add setting tab color ability. (Fix [#2271](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2271))
- Update to Scintilla 5.3.0 and Lexilla 5.1.9 (Implement [#12045](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12045))
- Fix “Never” button not showing on Updater dialog regression. (Implement [9c86a33](https://github.com/notepad-plus-plus/wingup/commit/9c86a33b2acaf08e2382edfd9ed7aabc6290782e))
- Fix a printing selection regression. (Fix [#11826](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11826), [#12033](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12033), [#11638](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11638))
- Revamp tab context menu: make it less cluttered by adding sub-menu. (Fix [#12147](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12147))
- Fix a security vulnerability. (Fix [#12113](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12113))
- Add dark mode support to Choose Color dialog. (Fix [#12148](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12148))
- Add a page (tab) for incompatible (unloaded) plugins in Plugin Admin. (Fix [#12069](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12069))
- Add Plugin list repository link and its version in PluginAdmin dialog.
- Fix horizontal bar showing issue while resizing document list’s height. (Fix [#12191](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12191))
- Fix NPPN_DARKMODECHANGED wrong return value to plugins. (Fix [#12144](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12144)).

## 8.4.5 – 2022-09-07

**Notepad++ v8.4.5 crash-fixes, bug-fixes & new features**

- Add reduce mode in Find/Replace dialog. (Implement [#11780](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11780))
- Update to Scintilla 5.2.4 and Lexilla 5.1.8. (Implement [#12022](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12022))
- Enhance very long line’s performance. (Fix [#11942](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11942))
- Fix crash on Wine. (Fix [#11941](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11941))
- Fix Notepad++ crash due to calling NPPM_GETLANGUAGENAME with -1 (WPARAM). (Fix [#12009](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/12009))
- Improve performance for “Find in Files” and ““Find all in…”. (Fix [#11878](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11878))
- Add option to turn off selecting text when Field dialog is invoked. (Implement [#11988](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11988))
- Fix drag n drop documents crash between 2 instances. (Fix [#11976](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11976))
- Fix erasing part of content make hanging issue. (Fix [#10193](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10193))
- Add an option for hiding the ＋ ▼ ✕ from the menu bar. (Implement [#11945](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11945))
- Add cycling function hints ability by ALT-UP/DOWN shortcuts. (Implement [#11950](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11950))
- Add carret block after option. (Implement [#11944](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11944))
- Fix detected language not being applied if Default languge is set in Document settings. (Fix [#11504](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11504))
- Fix dark mode visual glichy in explorer panel under Windows 8.1. (Fix [#11898](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11898))

## 8.4.4 – 2022-07-15

**Notepad++ v8.4.4 crash/regression-fixes & new enhancement**

- Fix Find in Files crash & syntax highlighting regression. (Fix [#11910](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11910), [#11883](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11883) & [#11920](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11920))
- Add shortcuts toward the settings of preferences dialog into Styler Configurator. (Implement [#11890](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11890))

## 8.4.3 – 2022-07-08

**Notepad++ v8.4.3 crash/regression-fixes, bug-fixes & new enhancement**

- Add an option which allows to show only 1 entry per found line in search result. (Fix [#2481](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2481), [#1499](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/1499), [#5547](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5547), [#2987](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2987), [#4525](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4525), [#3224](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3224))
- Make EOL (CRLF) display customizable (via Editing section of Preferences dialog). (Fix [#11413](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11413))
- Add 2 more shortcuts “plus” (new file) and “arrow” (drop down list of opened files) buttons on menu bar. (Fix [#11229](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11229))
- Update Lexilla to 5.1.7 & Scintilla to 5.2.3 and use new API for large files. (Implement [#11734](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11734))
- Fix Find in files performance regression since updating Scintilla 5. (Fix [#11814](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11814))
- Add dark mode support for plugins - support dark mode for plugins with docking GUI. (Fix [#11710](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11710), implement [#11767](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11767))
- Fix a crash issue due to opening an empty .NFO file. (Fix [#11820](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11820))
- Fix language fonts regression in Style Configurator (make font definition possible again). (Fix [#11786](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11786))
- Add NPPM_CREATELEXER message for plugins to instantiate lexers. (Fix [#11789](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11789))
- Enhance dark mode (edge colors). (Fix [#11207](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11207), [#11376](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11376))
- Fix “CMD Here” command open Explorer issue. (Fix [#11818](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11818))
- Fix crash issue of “Style Configurator…” command if “stylers.xml” is absent. (Fix [#11812](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11812))
- Fix Selected text changes color issue when editor window loses focus. (Fix [#11743](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11743))
- Skip save all warning dialog if only current editing file is dirty. (Fix [#10995](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10995))
- Fix a small regression in DebugInfo dialog. (Fix [#11752](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11752))

## 8.4.2 – 2022-06-03

**Notepad++ v8.4.2 crash-fixes, bug-fixes & new enhancement**

- Fix crash on “Copy Binary Content” command without selection on edit zone. (Fix [#11639](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11639), [#11671](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11671))
- Fix crashes by re-invoking with command line argument “-udl”. (Fix [#11633](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11633))
- Make toolbar icons customizable. (Fix [#9913](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9913))
- Make fold/unfold current level commands toggleable. (Fix [#11529](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11529), [#9196](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9196))
- Add command line argument for plugin, a related notification and an API. (Fix [#11576](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11576))
- Fix horizontal scrolling with scroll wheel on Logitech MX issue. (Fix [#10490](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10490))
- Enhance dark mode. (Fix [#11642](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11642), [#11693](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11693), [#11683](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11683), [#11530](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11530), [#10159](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10159))
- Add encoding context menu via right/double click on status bar. (Fix [#9998](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9998), [#400](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/400), [#756](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/756))
- Add gui4cli keywords and fix its style IDs in stylers.model.xml.
- Display installed plugin versions in Debug Info dialog. (Fix [#11284](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11284))

## 8.4.1 – 2022-05-11

**Notepad++ v8.4.1 regression-fixes, bug-fixes new enhancement**

- Fix HTML syntax highlighting in PHP files regression. (Fix [#11585](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11585), [#11602](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11602))
- Fix “Reload from disk” loosing syntax highlighting regression. (Fix [#11606](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11606))
- Fix unfocused selected text background color changed regression. (Fix [#11595](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11595))
- Update Scintilla from 5.2.1 to 5.2.2 and Lexilla from 5.1.5 to 5.1.6. (Implement [#11537](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11537))
- Fix multi-part keyword in prefix mode freezes Notepad++ in UDL. (Fix [#11434](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11434))
- Add several dark mode enhancement. (Fix [#11574](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11574), [#11622](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11622), [#10054](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10054), [#11546](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11546), [#11544](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11544))
- Add DarkMode usage detection support for plugins. (Implement [#11546](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11546))
- Add “Framed current line” option beside of “Highlight current line background”. (Implement [#11501](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11501))
- Add file monitoring command line argument [-monitor]. (Implement [#10562](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10562))
- File Dialog enhancement. (Fix [#11630](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11630), [#11517](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11517))
- Add a new format argument/option “ADD_ZERO_PADDING” to NPPM_GETNPPVERSION. (Implement [#11535](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11535))
- Restore auto-completion & calltip default fg/bg colors when no theme is applied. (Fix [#11637](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11637))
- Sort “Search result” to the bottom in language list of Style Configurator. (Fix [#11337](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11337))

## 8.4 – 2022-04-26

**Notepad++ v8.4 new features, enhancement and bug-fixes**

- Update Scintilla from v4.4.6 to v5.2.1 and add Lexilla v5.1.5. (Fix [#10504](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10504))
- Enhance dark mode support (Shortcut Mapper, autocompletion, calltip, Column Editor and Style configurator, Preferences dialog, etc…) (Fix [#11530](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11530), [#11522](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11522), [#11407](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11407), [#11514](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11514), [#11506](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11506), [#11497](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11497))
- Fix lossing characters issue after case-conversion (UPPER/lower). (Fix [#11463](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11463))
- Fix “Sort Lines as Integer” not considering negative number issue. (Fix [#11023](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11023), [#2025](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2025))
- Sort languages alphabetically automatically in Style Configurator. (Fix [#11337](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11337))
- Fix flashing box (autocompletion empty list) appears while typing issue. (Fix [#9433](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9433))
- Scrolling Document List automatically to make the selected tab item visible. (Fix [#11204](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11204))
- Make Find in Files search result line number aligned. (Fix [#11119](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11119))
- Add default A-Z sorting ability in Function list. (Fix [#11446](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11446))
- Add virtual space ability. (Fix [#11443](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11443), [#11444](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11444))
- Fix document being wronly marked as saved bug after converting its encoding. (Fix [#11436](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11436))
- Fix Document list not sync with tab order after sorting. (Fix [#11272](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11272))
- Fix file saving critical bug under Symantec encryption desktop. (Fix [#11339](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11339))
- Fix cropped text in Shortcut mapper’s status area issue. (Fix [#10358](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10358))
- Enhance installer: Remember the chosen language in the previous installation. (Implement [#10582](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10582))
- Improve Find/Replace Dialog layout. (Fix [#11318](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11318))
- Update NSIS & Inno Setup keyword lists.

## 8.3.3 – 2022-03-15

**Notepad++ v8.3.3 regression-fix, bug-fixes and enhancement**

- Fix crash regression on opening a session file. (Fix [#11325](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11325), [#11365](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11365))
- Enhance stability: add new ability (plugin compatibility) for not loading incompatible plugins. (Fix [#11349](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11349). Implement [#11358](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11358), [#11338](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11338), [#11353](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11353))
- Fix deleting the folded line makes folded (hidden) content disappeared. (Fix [#11246](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11246))
- Re-enable ability to center the Find Replace dialog on Notepad++ main window. (Implement [#9201](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9201))
- Fix extension not appended issue while saving with ENTER under Windows 7. (Fix [#11305](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11305), [#11355](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11355))
- Fix preferences dialog “Dark Mode->Customize tone” color pickers RTL alignment issue in dark mode. (Fix [#11343](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11343))
- Fix disabled static texts of Preferences blurry issue in dark mode. (Fix [#10823](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10823), [#11331](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11331))
- Add 4 API for custom auto-indentation and getting current macro status. (Implement [#11253](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11253))
- Add new AutoComplete icon for distinguishing functions from normal keywords. (Implement [#11311](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11311))
- Fix Plugin Admin close issue after typing ENTER. (Fix [#11348](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11348))
- Show current and new version on update dialog. (Implement [#19](https://github.com/notepad-plus-plus/wingup/issues/19))

## 8.3.2 – 2022-02-27

**Notepad++ v8.3.2 regression-fixes, bug-fixes and enhancement**

- Fix incorrect message while double clicking on search result regression. (Fix [#11215](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11215), [#11106](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11106))
- Fix regression: file can’t be saved if it’s set to other charset before. (Fix [#11238](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11238))
- Fix UDL comment config input fields broken regression. (Fix [#11239](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11239))
- Fix UDL dialog crash issue on over 30 created UDL. (Fix [#11257](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11257))
- Add sorting document tab order commands by name, path, type and size under “Window” Menu. (Fix [#10393](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10393))
- Add API NPPM_GETCURRENTLINESTR and variable $(CURRENT_LINESTR) for RunDlg. (Fix [#11216](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11216))
- Support better 2GB+ file (cmdline & session file adaptation). (Fix [#11213](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11213))
- Fix auto-completion sort order problem due to fx icon. (Fix [#11233](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11233))
- Refine auto-saving session on exit behaviour. (Fix [#11249](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11249))
- Enhance performance on exit with certain settings. (Fix [#11219](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11219))
- Fix auto-complete case insensitive not working issue. (Fix [#11187](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11187))
- Fix saving problem (regression) with “Sysnative” alias in x86 binary. (Fix [#11196](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11196))

## 8.3.1 – 2022-02-15

**Notepad++ v8.3.1 regression-fixes, bug-fixes and enhancement**

- Fix XML tag adding or mark deletion crash issue. (Fix [#11128](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11128))
- Fix wrong cursor position on opened file & cmdline ‘-n’ param not working regression. (Fix [#11131](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11131))
- Revert “Enable backup on save (simple) feature by default”.
- Restore auto-completion insert selection default behaviour (now with both ENTER & TAB as expected). (Fix [#11178](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11178))
- Fix Path Completion not working regression. (Fix [#11147](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11147))
- Fix target directory parameter (/D=) ignored by x64 installer regression. (Fix [#11072](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11072))
- Add icons on function items of auto-completion to distinguish from word items. (Implement [#11087](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11087))
- Fix file dialog “Append extension” checkbox not working on empty folder. (Fix [#10436](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10436))
- Fix link part of Dark Mode Customized tone not persistent issue. (Fix [#11095](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11095))
- Fix NPPM_RELOADFILE not working with converted 8.3 DOS file name (from long file name) bug. (Fix [#11106](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11106))

## 8.3 – 2022-02-03

**Notepad++ v8.3 new features and bug-fixes**

- Remove 2GB file open restriction for x64 binary.
- Improve large files (200MB) loading speed and editing/browsing performance.
- Fix Find in Files crash issue.

## 8.2.1 – 2022-01-24

**Notepad++ v8.2.1 new features and bug-fixes**

- Fix regression of loaded session being empty on exit. (Fix [#10986](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10986))
- Add Find/Replace text swap button in Find replace dialog. (Fix [#6010](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6010))
- Add an option for inserting auto-completion selection to fix hitting twice ENTER to go to next line. (Fix [#4799](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4799), [#4631](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4631), [#8389](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8389), [#10915](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10915))
- Fix installer x64 not detected the previous installation location. (Fix [#7946](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7946))
- Add copy name/path commands to DocList and Edit menu. (Fix [#10394](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10394))
- Fix Recent Files List not revised issue after “Save As” command. (Fix [#10946](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10946))
- Fix Windows 11 detected wrongly issue in “Debug information”. (Fix [#11011](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11011))
- Fix “Save As” command cannot be used as “Save” issue. (Fix [#10965](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10965))
- Fix visual glitch regression of fg/bg color disabling. (Fix [#11051](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11051))
- Fix wrong keywords (of preprocessor in C) highlighting in Java. (Fix [#11026](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/11026))

## 8.2 – 2022-01-01

**Notepad++ v8.2 new features and bug-fixes**

- Add exclude folder(s) ability in Find in Files (mouse hover on “Filters” label for getting the example on tool-tip). (Fix [#2433](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2433), [#8350](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8350))
- Fix UTF-8 detected wrongly as TIS-620 encoding issue. (Fix [#10916](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10916), [#940](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/940), [#8755](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8755), [#3588](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3588), [#3188](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3188), [#4932](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4932), [#3172](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3172), [#10492](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10492))
- Add auto save loaded session on exit feature (while “Open session in a new instance” is set in Multi-instance settings). (Fix [#1646](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/1646), [#3241](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3241), [#3574](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3574), [#4228](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4228))
- A comprehensive fix for dockable panels losing background color when switching back Notepad++. (Fix [#2202](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2202), [#2937](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2937), [#5980](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5980), [#8980](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8980), [#9905](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9905), [#10091](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10091))
- Fix memory leak while toggling between Dark/Lite Mode. (Fix [#10957](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10957))
- Fix caret left-right inverse moving in RTL mode issue. (Fix [#8553](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8553), [#7678](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7678), [#9730](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9730))
- Fix Document List icons unchanged issue after switching to dark mode or changing to alternative icons. (Fix [#10740](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10740))
- Fix incorrect folding behaviour in C, C++, Java, JavaScript, TypeScript and Objective-C. (Fix [#4560](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4560))
- Update boost regexp from v1.76 to v1.78. (Implement [#10912](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10912))
- “Rename tab” name field enlargement (from 20 to 63 char!). (Fix [#10961](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10961), [#9849](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9849))
- Apply “crontab” file to the syntax highlighting of bash. (Fix [#3377](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3377))

## 8.1.9.3 – 2021-12-08

**Notepad++ v8.1.9.3 bug-fixes and enhancement**

- Fix regression: detection of backup file restored back problem. (Fix [#10839](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10839))
- Fix saving file and false alert on network drive issues. (Fix [#10751](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10751), [#10688](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10688), [#10753](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10753), [#10757](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10757), [#10751](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10751), [#10787](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10787))
- Fix dockable panels lose background color issue when switching back Notepad++. (Fix [#2202](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2202), [#2937](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2937), [#5980](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5980), [#8980](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8980), [#9905](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9905), [#10091](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10091))
- Fix dirty status persisting issue after reloading file. (Fix [#10796](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10796))
- Add Lua function list capacity. (Implement [#4563](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4563))

## 8.1.9.2 – 2021-11-21

**Notepad++ v8.1.9.2 bug-fixes**

- Fix failure of erasing & saving server logs (of network drive) regression. (Fix [#10794](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10794))
- Fix dark mode not working on Windows 10 21H2. (Fix [#10810](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10810))
- Fix crash in regex search. (Fix [#10773](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10773), [#10803](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10803))
- Fix UDL folding breaking with delimiters issue if UNIX EOL applied. (Fix [#350](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/350), [#2873](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2873), [#3372](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3372), [#5499](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5499))
- Fix UDL generic dark mode via UDL UI not working issue. (Fix [#10781](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10781))
- Fix disabling alternative icons on tab in dark mode issue. (Fix [#10775](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10775))

## 8.1.9.1 – 2021-11-13

**Notepad++ v8.1.9.1 bug-fixes and new enhancement**

- Fix a regression of saving problem. (Fix [#10751](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10751))
- Fix a regression of reloading false alarm from the network drive. (Fix [#10688](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10688), [#10753](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10753), [#10757](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10757))
- Make Function list/Project panel/Folder as Workspace icon display correct under high DPI. ([Implementation](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/d192f58b5b03feba455c6e9f46c3aedce91153aa))
- Make UDL generic dark mode (working for all dark theme) possible via UDL UI. (Implement [#10738](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10738))
- Fix phantom docked panels issue after restoring from systray. (Fix [#10512](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10512))
- Enable backup on save (simple) feature by default (only for the new installation). (Implement [#10725](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10725))

## 8.1.9 – 2021-10-22

**Notepad++ v8.1.9 bug-fixes**

- Fix empty file with non-Unicode encoding cannot be saved issue. (Fix [#10699](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10699))
- Fix language list in Style Configurator not being reloaded issue. (Fix [#9512](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9512))

## 8.1.8 – 2021-10-19

**Notepad++ v8.1.8 bug-fixes**

- Fix config files (XML) saving performance regression. (Fix [#10678](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10678), [#10674](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10674))
- Workaround Microsoft dark mode API bug of Windows 11. (Fix [#10510](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10510))

## 8.1.7 – 2021-10-15

**Notepad++ v8.1.7 bug-fixes**

- Fix empty file not being saved regression. (Fix [#10667](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10667))
- Fix white flash in dark mode on CMD launch with position parameters. (Fix [#10657](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10657))
- Enhance dark themes for some programming languages (JSON, Python & Makefile). (Fix [#10648](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10648))
- Fix “Run macro until the end of file” command skipping the last line issue. (Fix [#10441](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10441))
- Fix tooltip layout and position in RTL mode. (Fix [#10646](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10646))
- Fix docking problem for dockable panel in RTL mode. (Fix [#10641](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10641))

## 8.1.6 – 2021-10-13

**Notepad++ v8.1.6 bug-fixes**

- Fix NUL file-corruption issue after system shutting down brutally. (Fix [#6133](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6133))
- Fix session lost issue after MS update restarting Windows. (Fix [#10402](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10402))
- Make Markdown UDL work in every dark theme. (Fix [#10593](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10593))
- Fix file can be marked as saved even it’s been deleted outside. (Fix [#10401](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10401))
- Fix status bar text display glitchy in dark mode. (Fix [#10564](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10564))
- Fix white flash on Notepad++ startup in dark mode issue. (Fix [#10601](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10601))
- Fix docked window sizing direction problem in RTL mode. (Fix [#10536](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10536))
- Fix floating panel movement issue in RTL mode. (Fix [#10579](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10579))
- Fix Print GUI bug in Preferences dialog. (Fix [#10552](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10552))

## 8.1.5 – 2021-09-27

**Notepad++ v8.1.5 bug-fixes and improvement**

- Make Insert date time customizable. (Fix [#10467](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10467))
- Make date time order reversible for short & long format. (Fix [#10445](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10445))
- Add Insert Date/Time commands shortcut & macro capacities. (Fix [#10567](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10567))
- Fix regression: no error message when locked file could not be saved - Show file locked warning now. (Fix [#9994](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9994))
- Make “Confirm Save All” dialog more clear: use “Always Yes” button instead of “Cancel”. (Fix [#10339](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10339))
- Improve JSON, PHP, PYTHON, CSS, BANNC and VHDL syntax highlighting in dark mode. (Fix [#10502](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10502), [#10425](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10425), [commit](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/c7e1da48ffa048448a0be584e120c638df9246e3))
- Fix inconsistency of Document List context menu. (Fix [#10463](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10463))
- Enable/disable ext column via Document list context menu directly. (Fix [#10468](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10468))
- Add path column in Document list panel. (Fix [#9679](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9679))
- Allow custom color for Document Map. (Fix [#10052](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10052))
- Fix docked/float panels in RTL layout issue. (Fix [#10488](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10488))
- Fix CSS pseudo-elements not recognized issue. Update CSS keywords and add new styles. (Fix [#10425](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10425))
- Fix issue that current directory not been applied after changing current directory option in preferences. (Fix [#10396](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10396))
- Sort Default language combobox of “New Document” section in Preferences. (Fix [#10513](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10513))

## 8.1.4 – 2021-08-25

**Notepad++ v8.1.4 bug-fixes and improvement**

- Fix regression of find/replace and file open performance issue. (Fix [#10398](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10398), [#10296](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10296), [#10260](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10260))
- Make dark mode compatible with Windows 11. (Fix [#10299](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10299))
- Make current existing plugins’ toolbar icons display in both light and dark mode. (Fix [#9959](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9959), [#10388](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10388), [#9809](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9809))
- Support TypeScript language (syntax highlighting, auto-completion & function list). (Implement [#10353](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10353))
- Fix security flaw issue in uninstaller. (Fix [#10191](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10191), [#6165](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6165))
- Add Insert Date Time commands for both short & long format. (Implement [#497](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/497), [#2821](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2821), [#8184](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8184), [#8302](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8302))
- Fix file dialog append extension issue with RTL languages. (Fix [#10397](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10397))
- Fix Find-in-Files “Follow current doc” not working issue when Default Directory is set. (Fix [#8045](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8045))
- Enhance dialogs visual look & feel. (Fix [#10384](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10384))
- Fix LICENSE text display problem in installer. (Fix [#10370](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10370))

## 8.1.3 – 2021-08-13

**Notepad++ v8.1.3 bug-fixes and improvement**

- Dark mode enhancement: 95.427% dialogs are dark-modable. (Implement [#10061](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10061), [#10287](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10287), [#10285](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10285), [#10283](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10283), [#10275](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10275), [#10273](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10273), [#10269](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10269), [#10049](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10049), [#10196](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10196), [#10066](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10066), [#10264](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10264), [#10242](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10242), [#10255](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10255), [#10253](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10253), [#10210](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10210), [#10251](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10251), [#10249](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10249), [#10247](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10247), [#10245](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10245), [#10236](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10236), [#10233](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10233), [#10178](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10178), [#10069](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10069), [#10205](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10205), [#10027](https://github.com/notepad-pl[us-plus/notepad-plus-plus/issues/10027), [#10221](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10221), [#10230](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10230), [#10226](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10226))
- Improve GUI display under high DPI.
- Add Markdown UDL of dark mode in release packages. (Fix [#10196](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10196))
- Fix crash issue when several instances of the save dialogs are shown. (Fix [#10290](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10290))
- Fix save dialog not working on Windows Vista. (Fix [#10238](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10238))
- Add the capacity to switch among Find/Replace/FiF/Mark via their shortcuts. (Implement [#10019](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10019))
- Make Document List Panel togglable via View menu and shortcutable in shortcut mapper. (Implement [#3526](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3526), [#9015](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9015))
- Fix Function list current empty lost issue while Sort/Unsort/Save/Reload. (Fix [#8819](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8819), [#10280](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10280), [#10294](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10294))
- Fix Functions list scrolling to the top on file save issue. (Fix [#9659](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9659))
- Fix wrong path in tooltip of tab in RTL mode. (Fix [#8520](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8520))
- Fix the file drag and drop bug in RTL mode. (Fix [#8730](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8730))
- Add filter capacity in Shortcut mapper by shortcut key combination (Implement [#5616](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5616), [#9316](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9316))
- Add copy file names capacity from Windows dialog. (Implement #[10123](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10123))
- Fix shortcut conflict detection error in Shortcut mapper while filtering. (Fix [#5374](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5374))
- Increase macro, user command and plugin command number capacity. (Fix [#10263](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10263))

## 8.1.2 – 2021-07-19

**Notepad++ v8.1.2 bug-fixes and improvement**

- Make dark mode restartless. (Fix [#10121](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10121))
- Activate dark mode in Windows 11. (Fix [#10136](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10136))
- Make Notepad++ dark mode colors customizable: add 6 more color tone choices. (Implement [#10128](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/10128))
- Add customizing dynamically dark mode colors capacity (Implement [#10145](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/10145))
- Add command line flag -udl=“UDL name” to open a file by applying an existent UDL via its name. (Implement [#10102](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/10102))
- Use always current file directory in File Rename dialog. (Fix [#10095](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10095))
- Fix “Remember last used directory” unexpected behaviour. (Fix [#10115](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10115))
- Fix corrupted encoding text on status bar if shortcut assigned to encode command. (Fix [#10146](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10146))
- Add a Save all confirm dialog. (Fix [#2124](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2124), [#9931](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9931))
- Improve JavaScript auto-completion. (Fix [#9858](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9858))

## 8.1.1 – 2021-07-04

**Notepad++ v8.1.1 bug-fixe and improvement**

- Fix edit zone not being applied to dark mode issue on another user account in the same machine (Fix [#10076](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/10076)).
- Enhance dark mode (make user interface more dark-modable).

## 8.1 – 2021-06-17

**Notepad++ v8.1 regression-fixes and improvements**

- Fix regression of auto-completion performance issue (Fix [#9975](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9975))
- Fix Open dialog with “Save” label for “Open” button (Fix [#9966](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9966))
- Fix Notepad++ crash on dark mode while starting up (Fix [#9961](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9961))
- Improve look & feel in dark mode (Fix [#9982](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9982))
- Adapt Tooltips in dark mode (Fix [#9962](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9962))
- Remove white line under menubar in dark mode (Fix [#9984](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9984))
- Make multiline and vertical tabs work in dark mode (Implement [#10017](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/10017))

## 8 – 2021-06-07

**Notepad++ v8 new features & bug-fixes**

- Add Dark Mode. (Implement [#9183](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9183) & [#7692](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7692))
- ARM64 build is available. (Implement [#5158](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5158))
- One button to build them all - build Notepad++ with Scintilla static lib and Boost RegExpr headers. (Implement [#9594](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/9594))
- Add new Fluent UI icons for toolbar.  (Implement [#9742](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9742))
- Add new feature “Distraction Free Mode” (Menu “View->Distraction Free Mode”).
- Add new API NPPM_ADDTOOLBARICON_FORDARKMODE for dark mode (Implement [#9928](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9928)).
- Add 1 click action (SHIFT-click) on close button to close all tabs in dockable panel (Implement [#8922](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8922).
- Add ability of changing select text foreground color (optional). (Fix [#3397](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3397) & [#1314](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/1314))
- Allow Replace to stop after replacement (optional). (Implement [#4437](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4437))
- Fix append extension feature not working in save dialog. (Fix [#9939](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9939))
- Add ability to reverse line order. (Implement [#9837](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9837))
- Add ability to style only current instance of text. (Fix [#9263](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9263))
- Fix duplicated entries in Auto-Completion pop-up window. (Fix [#9711](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9711))
- Fix Python Function List not showing functions in some circumstance. (Fix [#9844](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/9844))
- Enhance Folder as Workspace performance while adding/removing files in bulk. (Fix [#9203](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9203))
- Add Ada, Fortran, Fortran77 & Haskell in function lists. (Fix [#9698](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9698))
- Improve performance of “Open all” command in Search results. (Fix [#9819](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9819))
- Add “Copy Pathnames” command to Search results context menu. (Fix [#9821](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9821))
- Catch regex search exceptions and show exception message. (Fix [#9565](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9565))
- Add MarkAll Preference settings for case and word. (Fix [#9751](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9751) & [#5148](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5148))
- Fix regression: Handle “Default Directory” setting correctly in Open/Save File Dialog. (Fix [#9767](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9767))
- Fix a special character in UTF16 file crash issue (regression). (Fix [#9797](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9797))
- Add “Append extension” checkbox to Save As dialog. (Implement [#9515](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9515))
- Fix Copy command in Search result is available as there’s no selection. (Fix [#9757](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9757))
- Add padding ability in the edit zone. (Fix [#2323](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2323))
- Make new tab name translatable. (Fix [#2837](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2837))
- Improve character case handling in RegEx. (Fix [#9636](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9636))
- Fix dragged out UDL file is not applied to UDL in the new instance. (Fix [#3451](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3451))
- Add command line parameter for adding specified string to app title bar. (Implement [#9539](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9539))
- Fix Auto-Completion ignoring case issue. (Fix [#3997](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3997), [#4833](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4833) & [#4998](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4998))
- Fix “Match Whole Word” option being enabled in RegEx Search. (Fix [#9766](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9766))
- Fix sort with column key selection that appears after tab characters. (Fix [#9682](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9682))
- Fix “Reload Workspace” menu command not working issue. (Fix [#9350](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9350))
- Fix view file in Edge browser failure issue if name contains spaces. (Fix [#9313](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9313))
- Add ability to avoid accumulating multiple search results. (Fix [#8777](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8777))
- Fix UTF-16 decoding/encoding for code points above U+FFFF. (Fix [#9597](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9597), [#3747](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3747) & [#5754](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5754))
- Fix “Save As” command removing original path from recent files history issue. (Fix [#9673](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9673))
- Fix function List button tool tips mixed up issue. (Fix [#9804](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9804))
- Remove Microsoft Bing from Notepad++ for Search on Internet command, due to its poor reliability. ([Ref](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/06657c82b3b9a1871c483982282f046b1ac7b3be))

## 7.9.5 – 2021-03-23

**Notepad++ v7.9.5 Enhancements & bug-fixes**

- Fix Notepad++ not starting up due to SaveAsAdmin plugin (for installer package). (Fix [#9514](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9514))
- Fix UNC path with quotes handling in folder & file Open/Save dialog. (Fix [#9582](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9582))
- Fix file doesn’t save as extension type on Windows 7. (Fix [#9657](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9657))

## 7.9.4 – 2021-03-15

**Notepad++ v7.9.4 Enhancements & bug-fixes**

- Upgrade Scintilla from v4.2.0 to v4.4.6. (Implement [#9550](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9550))
- Fix DPI scaling broken while dragging Notepad++ into the 2nd monitor regression. (Fix [#9513](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9513), [#9579](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9579))
- Add “Find in Projects” feature. (Implement [#8125](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8125))
- Fix project workspace changes lost on save cancel issue. (Fix [#9605](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9605))
- Fix folder picker not being launched issue because provided directory is invalid. (Fix [#9569](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9569))
- Fix network path (UNC path) not working in file dialog. (Fix [#9527](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9527))
- Fix shortcut name more than 64 characters makes a menu entry empty name issue. (Fix [#9556](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9556))
- Fix extension appending issue in file dialog. (Fix [#9510](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9510))
- Fix file not turning to modified state (with Session Manager plugin) bug after its content being changed. (Fix [#9475](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9475))
- Add an option to mute all sounds in preferences dialog. (Fix [#7950](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7950))
- Make JSON auto-indent for brace. (Fix [#9499](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9499))

## 7.9.3 – 2021-02-15

**Notepad++ v7.9.3 Enhancements & bug-fixes**

- Discontinued support for Windows XP & Windows Server 2003 due to [technical reasons](https://github.com/notepad-plus-plus/notepad-plus-plus/pull/9378). Notepad++ 7.9.2 is the last version to run on Windows XP & Windows Server 2003. ([Ref](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/SUPPORTED_SYSTEM.md))
- Upgrade Notepad++ License: update GPL version from v2 to v3. (Fix [#9425](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9425))
- Fix the regression of copying line data from search results. (Fix [#9334](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9334))
- Fix “Print Line Number” preference is ignored for printing regression. (Fix [#9379](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9379))
- Fix a regression in Chinese Simplified localization. (Fix [#9329](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9329))
- Fix dockable panels not being displayed regression due to multi-instance mode activation. (Fix [#9341](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9341) & [#9363](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9363))
- Make split-lines feature work again with multi-edge rightmost specified edge. (Fix [#8262](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8262))
- Enhance modern style file dialog for allowing UNIX style file path. (Fix [#9374](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9374))
- Use the modern browse folder dialog to get folder path. (Fix [#8513](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8513))
- Improve option for setting save dialog filter to All Types. (Fix [#9325](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9325))
- Add ability to delete entries from combo box history in Find dialog with DELETE key. (Implement [#9366](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9366))
- Fix lost session issue on Windows reboot/shutdown. (Fix [#7839](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7839))
- Add “save Folder as Workspace in session” option in save session dialog. (Implement [#9165](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9165))
- Make value dialog height accurate in any DPI. (Fix [#8443](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8443))
- Fix issue that Switch-To-Panel keyboard shortcuts cannot be used in context menu. (Fix [#9435](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9435))
- Fix a memory leak issue. ([Ref](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/a2ee3e6254c13edc08c4088dc80250079fc16e35))
- Fix blurry display problem on an extended monitor. (Fix [#8115](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8115))
- Fix incompatible plugin not being deleted issue. (Fix [#9377](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9377))
- Synchronize GUP localization file (if available) with Notepad++ in installer.
- Enhance “No update” dialog with the download page link in the Notepad++ updater.
- Fix NPPM_SETLINENUMBERWIDTHMODE API not working issue. (Fix [#9338](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9338))

## 7.9.2 – 2021-01-01

**Notepad++ v7.9.2 Enhancements & bug-fixes**

- Fix regression of auto-Indent. (Fix [#9113](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9113))
- Add custom URI schemes ability. (Fix [#9155](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9155))
- Improve URL parser: fix apostrophe in an URL issue. (Fix [#9031](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9031))
- Add context menu with “Copy link” ability. (Implement [#2435](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2435))
- Add color samples on menu items for styling features. (Fix [#8983](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8983))
- Add “-settingsDir” argument for overriding default settings path. (implement [#4696](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4696))
- Fix crash while exit command issued by plugin. (Fix [#9082](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9082))
- Fix several bugs of PHP parser rule for function list. (Fix [#3321](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3321), [#5045](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5045), [#4627](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4627), [#4606](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4606), [#8855](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8855), [#4208](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4208), [#981](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/981), [#2522](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2522), [#1103](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/1103),  [#4712](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4712), [#3560](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3560), [#5150](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5150), [#4606](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4606))
- Move “Normal Text” to top in Languages Menu. (Implement [#7746](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7746), [#8277](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8277))
- Add new API NPPM_GETSETTINGSONCLOUDPATH for plugins. (Implement [#9168](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9168))
- Add an option for displaying constant line number width. (Implement [#5670](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5670))
- Fix function list is empty with new user profile in the same PC issue. (Fix [#9134](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9134))
- Fix single-quoted string being badly recognized as attribute value in XML. (Fix [#3403](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3403))
- Fix docked panels appear with “-nosession” cmd line parameters. (Fix [#8005](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8005))
- Improve text selection after Replace All In Selection operation. (Fix [#9270](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9270))
- Add the number of total documents on windows dialog’s title bar. (Implement [#8338](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8338))
- Fix scroll to last line problem after main window resizing. (Fix [#9123](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9123))
- Fix Plugin admin display UTF-8 issue in its description. (Fix [#9266](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9266))
- Fix Search result’s text direction (RTL) not always synchronized with main edit zone’s one issue. (Fix [#9241](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9241))
- Fix dockable panels display issue in RTL direction. (Fix [#9241](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9241))
- Fix Search result line number highlighting inaccurate issue. (Fix [#9224](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9224#issuecomment-738864831))
- Make “Line” preceding each line number on Search Results translatable. (Fix [#9224](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9224))
- Fix menu check marks not being removed after closing “Clipboard History” and “Character Panel” panels. (Fix [#9216](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9216))
- Fix command line arguments -p, -n & -c negative value’s undefined behaviour. (Fix [#9146](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9146))
- Add new Margin/Border/Edge sub-page in Preferences. (Implement [#8896](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8896))
- Fix find in files failure issue due to directory path with leading/trailing spaces. (Fix [#9199](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9199))
- Fix folder icon display issue in “Folder as Workspace” after “Expand/Collapse All”. (Fix [#8912](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8912))
- Make “Clipboard History” and “Character Panel” togglable. (Fix [#9094](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9094), [#9078](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9078))
- Fix Find in found results dialog launch failure after macro execution. (Fix [#8199](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8199))
- Disallow Goto dlg offset option from moving to position inside multi-byte char or between CR and LF. (Fix [#9101](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9101), [#9125](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9125))
- Fix “Go to…” dialog wrong Offset value in empty files. (Fix [#9145](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9145))
- Prevent corruption possibility when using -p command line parameter in a UTF file. (Fix [#9142](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9142))
- Improve indent guidelines on non-brace control block languages. (Fix [#9137](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9137))
- Prevent names of untitled tabs from duplication. (Fix [#9119](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9119))
- Add tooltips for Folder as Workspace 3 commands. (Fix [#8325](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8325))
- Fix “SCI_NEWLINE” inside a macro not working issue. (Fix [#5571](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5571))
- Fix bug where search-results won’t open ‘new 1’ file. (Fix [#8461](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8461), [#9098](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9098))
- Fix tab close button remain pushed issue. (Fix [#7750](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7750))
- Enhance ghost typing command line argument feature - using white space directly instead of %20. ([Commit](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/f617325006e7b7f22340b0a49f60a82e3d0392b4))

## 7.9.1 – 2020-11-02

**Notepad++ v7.9.1 Enhancements & bug-fixes**

- Fix NUL file-corruption bug after Windows shutdown brutally (Fix [#6133](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6133)).
- Fix inaccurate URL detection by replacing a new URL parser (Fix [#3912](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3912), [#3353](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3353), [#4643](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4643), [#5029](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/5029), [#6155](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6155), [#7791](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7791), [#8634](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8634))
- Fix RegEx look behind operations and \A and and \b and \z (Fix [#713](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/713), [#1870](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/1870), [#2216](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2216), [#2360](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2360), [#9004](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9004), [#4855](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4855)).
- Split functionList.xml into multifile in “functionList” Folder (Implement [#4896](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4896)).
- Make tray icon work again in administrator mode (Fix [#8528](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8528)).
- Fix dialogs & floating dockable panels don’t minimize to system tray issue (Fix [#9044](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9044), [#8928](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8928)).
- Add alternative icon set for tab bar (Implement [#8068](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8068)).
- Add ability to remove any duplicate lines in a document, keeping the first occurrence (Fix [#8965](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8965)).
- Fix incorrect icon for monitoring status in Document list panel and in Document switcher (Fix [#8783](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8783)).
- Add copy marked text & styled text to clipboard commands to menu (Implement [#8943](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8943), [#6095](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6095)).
- Fix find-all-open-docs not finding all matches in ANSI files (Fix [#8901](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8901)).
- Display long lines better in Find-result panel by increasing its max length to 2048 (Fix [#7723](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7723)).
- Fix double clicking on find result line not working (Fix [#9009](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9009), [#8525](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8525)).
- Fix Find-result rclick-Copy incomplete data bug (Fix [#8801](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8801)).
- Add case insensitive lines sorting (Implement [#4479](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/4479)).
- Add “Open Containing Folder as Workspace” command in main menu and in context menu of tabs (Implement [#3028](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/3028)).
- Enhance Sel info of status bar (Fix [#8524](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8524)).
- Add new option for save type of normal text files in Save dialog (Fix [#8866](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8866)).
- Fix file path truncated issue in save confirmation dialog (Fix [#8812](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8812)).
- Fix auto-Indent not working for PowerShell (Fix [#9049](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/9049)).
- Allow setting of background color for bookmark margin (Fix [#8833](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8833)).
- Fix smart-highlighting not applying to cloned view (Fix [#7910](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/7910)).
- Fix smart highlight issue related to EOF (Fix [#8908](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8908)).
- Fix closing file in 2nd view not removed from Doc Switcher (Fix [#8800](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8800)).
- Add Delete keystroke to remove selected root from Folder as Workspace (Fix [#8960](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8960)).
- Add TAB keystroke in Function List to switch between search field and list (Fix [#8665](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8665)).
- Add ESC keystroke in Function List to switch to edit window (Fix [#8886](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8886)).
- Add ESC keystroke to close Search Results Window (Implement [#2946](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/2946)).
- Fix data-prefixed attributes are not recognized in HTML (Fix [#6200](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/6200)).

## 7.9 – 2020-09-28

**Notepad++ v7.9 Enhancements & bug-fixes**

- Add the ability to open the target file of a Shortcut (*.lnk).
- Enhance side panels behaviour: close a single panel instead of the entire stack.
- Fix Monitoring & document auto-update not scrolling to the end of the file with Word wrap enabled issue.
- Fix mouse cursor flicker while hovering URLs.
- Add back hovered blue underlined URLs.
- Enhance C++, Perl, Python parsers and add VHDL in Function List.
- Improve some ambiguous commands naming in Shortcut Mapper.
- Add an option to prevent right click from canceling selection.
- Add ability to sort lines randomly.
- Fix “Close All BUT this” looses current document data issue.
- Allow user to start making a stream selection and then change to column block (by pressing ALT key).
- Add word wrap option to find results context menu.
- Add keyboard navigation ability to Column Editor.
- Add keyboard shortcut ability to Projects, Folder as Workspace and Function List for switching among these panels.
- Enable project panels toggle from menu.
- Enhance Folder as Workspace to restore latest selected item of last session on Notepad++ startup.
- Fix inaccurate line margin update with word wrap enabled.
- Fix Find previous/next commands not scroll vertically to show match result issue (with word wrap disabled).
- Fix column key sort with col block starting in col1 bug.
- Add confirmation preference for Replace All in All Opened Documents operation.
- Add Escape keypress in functionlist searchbox to clear its text.
- Add RTL capability to localized messageboxes.
- Make (Find) dlgAlwaysVisible a true Preference setting.
- Fix sorting by column key using incorrect key values.
- Add search scope to Find window status bar output.
- Fix false hit result in Find in Finder.
- Prevent redundant line data copy in Finder.

## 7.8.9 – 2020-07-16

**Notepad++ v7.8.9 bug-fixes**

- Fix Line operations (join lines, split lines, remove duplicate lines and sort lines) doing one too many lines issue.
- Fix the regression of jump line failure via command line (-n).
- Fix URL Hovered colour disappears after modifying any Clickable Link Settings regression.
- Fix URL is not clickable in certain stuation while wrapped is enabled.
- Fix “Save” not working in Windows dialog.
- Fix Flickering cursor after double clicking a found line in find results.
- Fix Found line may not be centered by double clicking in find results, if word wrap is on.
- Fix wrong horizontal scroll bar position after restoring Window position.
- Fix Find result window output TAB-width incoherent issue.

## 7.8.8 – 2020-06-28

_Keine Changelog-Liste auf der Seite._

## 7.8.7 – 2020-06-08

_Keine Changelog-Liste auf der Seite._

## 7.8.6 – 2020-04-20

**Notepad++ v7.8.6 bug-fixes & enhancement**

- Add multi-column marker (multi-line edge) feature.
- Add dynamical sorting feature for Folder as Workspace.
- Make MRU tab activate instead of rightmost tab while tab closure (if MRU enabled).
- Fix folding state lost on the next startup issue.
- Make Replace-in-Files confirmation dialog modal to prevent from crashing.
- Add support of smart-indenting for Perl and Rust.
- Make recorded macro (IDC_FINDNEXT & IDC_FINDPREV)retro-compatible up to 7.8.4.

## 7.8.5 – 2020-03-06

**Notepad++ v7.8.5 bug-fixes & enhancement**

- Fix “Monitoring” not detecting all file changes issue.
- Fix auto-updater disabling not working regression.
- Fix Notepad++ doesn’t exit correctly while Windows 10 update restart.
- Make Count command in Find dialog respect Backward-direction and Wrap-around options.
- Make Find dialog remember its position across runs.
- Add the document size column to the Windows Selection dialog.
- Make “View Current File in(browser)” commands macro recordable.
- Add external sound control capability for unsuccessful search (in Find dialog) bell.

## 7.8.4 – 2020-01-30

**Notepad++ v7.8.4 bug-fixes**

- Fix regression of double clicking a found in files result while Word-Wrap is on.
- Fix HashFromDlg title bar localization issue.

## 7.8.3 – 2020-01-16

**Notepad++ v7.8.3 enhancements & bug-fixes**

- Add the “Expand All”, “Fold All” and “Select/Show current editing file” capacity into Folder as Workspace.
- Fix restoring line position issue while document is wrapped.
- Improve Json syntax highlighting.
- Make filling find field of Find dialog with selected word(s) optional.
- Make doSaveOrNot dialog simpler when there’s a single file to save.
- Fix auto-insert {[“”]} imbrication not working issue.
- Make cmd cli (for “Open Containing Folder in cmd”) customizable.
- Prevent from setting Updater’s Proxy as Notepad++ is not in Admin mode.
- Disable file association settings when Notepad++’s no admin right.
- Fix incremental search bar “highlight all” option not conserved bug.
- Enhance SQL syntax highlighting (add 2 more keyword lists).
- Fix too small buffer issue during add text macro playback.
- Fix “Close All Unchanged” not working issue for sub-view.
- Eliminate garbage displaying in Find-result fold margin.

## 7.8.2 – 2019-12-05

**Notepad++ v7.8.2 enhancements & bug-fixes**

- Add key shortcuts in Save or not dialog.
- Add find in files filter excluding ability.
- Add “Open UDL folder” command.
- Fix issue of showing save dialog twice while cloned file is dirty.
- Enhance “Open Explorer” command in Folder as workspace with expected path.
- Fix tab dragging issues.
- Enhance “Close all but This” and “Close all to the left/right” commands while files are dirty.
- Enhance “In Selection” option in Find dialog.
- Fix Notepad++ blocked in notification zone issue.
- Make end-of-line conversion operations macroable.
- Fix “View Current File In” commands disabled problem in some situations.

## 7.8.1 – 2019-10-29

**Notepad++ v7.8.1 enhancements & bug-fixes**

- Fix popup dialog on startup regression regarding notepad replacement issue.
- Make monospaced font in Find dialog optional, disabled by default.
- Add download progress bar while download plugin(s).
- Fix issue for Alt+Tab doesn’t show Notepad++ on Windows 7.

## 7.8 – 2019-10-11

**Notepad++ v7.8 enhancements & bug-fixes**

- Upgrade Scintilla from 4.1.4 to 4.2.0
- Fix non Unicode encoding problem in non-Western language(Chinese or Turkish).
- Add “No to All” and “Yes to All” options in Save dialog.
- Add the command line argument “-openFoldersAsWorkspace” to open folders in “folder as workspace” panel.
Example: notepad++ -openFoldersAsWorkspace c:\src\myProj01 c:\src\myProj02
- Enhance plugin system: allow any plugin to load private DLL files from the plugin folder.
- Fix File-Rename failing when new name is on a different drive.
- Make “Clear all marks”, “Inverse Bookmark”, “Remove Consecutive Duplicate Lines” & “Find All Current Document” to be macro recordable.
- Make “Command Argument Help” MessageBox modal.
- Fix Folder as Workspace crash and “queue overflow” issues.
- Make Combobox font monospace in Find dialog.
- Fix folding in user-defined languages for non-windows line endings.
- Fix crash of Folder as Workspace when too many directory changes happen.
- Fix ‘-nosession’ overwrites config.xml issue.
- Fix the crash due to NPPM_DESTROYSCINTILLAHANDLE message.
- Improve GUI in Find dialog for Find Previous & Find Next buttons.
- Fix Sort Line as Integer regression.
- Add more OS information to debug info.
- Fix tab dragging issues under WINE and ReactOS.
- Fix indent indicators continue to following code blocks for Python.
- Fix Python folding collapse issue.
- Fix crash when sorting “out of range” columns.
- Fix find 2 times for the same occurrence in both original and cloned documents issue.
- Fix command line issues where filenames have multiple white spaces in them.
- Fix Document Peeker constantly changing focus problem.
- Make backward direction checkbox be also on Find dialog’s Mark tab.
- Add 2 new columns for HTML Code in the Character Panel.
- Fix “clear all marks in find dialog also removes bookmarks” issue.
- Enhance supported language (on function list or auto-completion): LISP, BaanC,(PL/)SQL & COBOL.

## 7.7.1 – 2019-06-20

**Notepad++ v7.7.1 enhancements & bug-fixes**

- Fix drag and drop tab regression: dragging tab is switched to another tab issue.
- Fix an input regression: Cyrillic, Turkish and other languages input issue in ANSI mode.
- Fix an ASP regression: VB loses syntax highlighting in ASP document.
- Fix Reload dialog displaying issue during File Monitoring.
- Fix “unhide lines” markers disappears issue.
- Fix Plugin menu is not localized issue if no plugin installed.
- Add “Copy File Name” command in context menu of “Folder as Workspace”.
- Fix crash while sorting lines with numbers longer than 20 digits.
- Enable Scintilla Virtual Space Option change from macro.
- Add Tcl, CMake and AutoIt keywords; add Python and SQL new syntax highlighting categories.

## 7.7 – 2019-05-19

**Notepad++ v7.7 enhancements & bug-fixes**

- Continue Microsoft binary code signing thanks to the offer from DigiCert (again).
- Upgrade Scintilla from v3.56 to v4.14.
- Fix a regression of memory issue while reloading a file.
- Fix cursor flickering problem after double clicking on URL.
- Make Python files default to using spaces instead of tabs.
- Add “Count in selection” option in Find dialog.
- Add Ctrl + R shortcut for “Reload from disk” command.
- Fix ‘\’ display problem in CSS while using themes (Remove Batang font for CSS tags).
- Fix crash while right clicking on DocSwitcher’s column bar.
- Fix all plugins being removed problem while Plugin Admin removes an old plugin (of old system).

## 7.6.6 – 2019-04-04

**Notepad++ v7.6.6 enhancements & bug-fixes**

- Security enhancement: GPG Signature is provided for Notepad++ release.
- Fix a long waiting issue about file auto change detection: enhance “File status Auto-Detection” to avoid switching editing tab off behaviour.
- Fix encoding (language) detection regressions since v7.6.
- Fix a regression: double-clicking on a “find all in current document” result for an unsaved doc prompts to save it.
- Added close all unchanged tabs command.
- Restore deleted “Launch in browser” customized shortcuts in EU-FOSSA bounty program by implementing them in more secure way: Add “View Current
- Retain read only setting state in session.
- Enhancement: after file reload user can still undo.
- Fix a bug in command “Remove Consecutive Duplicate Lines” and make it work with old Macintosh EOL.
- Fix UDL language marker bullet position, if UDL Name exceeds 14 characters, extend UDL names to max 64 characters.
- Enhance external call code to avoid eventual arbitrary commands execution. (EURO-FOSSA)
- Fix crash issue by command “On Selection->Open File” while the number of selected characters is exceed 2048. (EURO-FOSSA)
- Fix crash issue of User Define dialog while deleting a unallocated entry. (EURO-FOSSA)
- Fix crash issue on shortcut command while its length exceed 260. (EURO-FOSSA)
- Add an enhancement on “Open…” command to prevent from the eventual crash. (EURO-FOSSA)
- Fix stack Buffer Overflow in Command::extractArgs. (EURO-FOSSA)

## 7.6.4 – 2019-03-06

**Notepad++ v7.6.4 enhancements & bug-fixes**

- Add Markdown in zip packages and fix Markdown not working in installer package of v7.6.3.
- Switch from certificate verification to hashes verification due to “Notepad++” is rejected by certification authority.
- Enhance User Defined Language System for supporting more than one UDL file. Here is new behaviour.
- Add “Remove Consecutive Duplicate Lines” feature to remove duplicate consecutive lines from whole document.
- Add new shortcut “shift + scroll” for horizontal scrolling.
- Add Stack Overflow as search engine.
- Add the capacity to rename non-existing document’s tab.
- Fixed file open hang issue in old style mode.
- Fix “Find in files” tab translation issue on initial dialog call.
- Fixed macro playback junk characters display issue on Find dialog.
- Ensure each recorded command is playable before playing to avoid exploit in hacking. (EURO-FOSSA)
- Enhance “Search on Internet” command to avoid command hijacked. (EURO-FOSSA)
- Fix buffer overrun in Print dialog. (EURO-FOSSA)
- Load nppPluginList.dll as resource instead of binary for the sake of security. (EURO-FOSSA)
- Check Updater’s integrity before its each launch to prevent from hijacking. (EURO-FOSSA)
- Fix stack buffer overflow in WordStyle dialog. (EURO-FOSSA)
- Fix stack buffer overflow issue on User Define Language dialog. (EURO-FOSSA)
- Prevent eventual DLL hijacking while loading plugins. (EURO-FOSSA)

## 7.6.3 – 2019-01-27

**Notepad++ v7.6.3 enhancements & bug-fixes**

- Add Markdown language (Markdown++), in UDL, included only in installer.
- Move plugins home from %ProgramData% to %ProgramFiles% for the sake of security.
- List plugins in alphabetical order in Plugins Admin dialog.
- Fix loading unexpected dll as plugin issue. (EU-FOSSA)
- Fix stack overflow issue while affecting “ext” field on stylers.xml. (EU-FOSSA)
- Fix stack overflow in XML Parsing. (EU-FOSSA)
- Fix a remote code execution vulnerability via “Open containing folder” command. (EU-FOSSA)
- Fix EXE Hijacking of gup.exe launched by Notepad++. (EU-FOSSA)
- Fix crash issue due to heap overflow in clipboard history panel. (EU-FOSSA)
- Remove run external exe entries for avoiding to execute eventual hijacked binaries. (EU-FOSSA)

## 7.6.2 – 2019-01-01

**Notepad++ v7.6.2 enhancements & bug-fixes**

- Fix Plugins Admin unzip (0 lengh) bug.
- Add generation of SHA-256 hash feature.
- Add Plugins Admin module into portable version (zipped package).
- Add new feature: double click splitter resets panes to equal size.
- Fix the plugin crash issue due to the inexistent plugin conf path.

## 7.5.6 – 2018-03-19

**Notepad++ v7.5.6 enhancements & bug-fixes**

- Fix Plugins Admin unzip (0 lengh) bug.
- Add generation of SHA-256 hash feature.
- Add Plugins Admin module into portable version (zipped package).
- Add new feature: double click splitter resets panes to equal size.
- Fix the plugin crash issue due to the inexistent plugin conf path.

## 7.5.4 – 2018-01-01

**Notepad++ v7.5.4 enhancements & bug-fixes**

- Fix Plugins Admin unzip (0 lengh) bug.
- Add generation of SHA-256 hash feature.
- Add Plugins Admin module into portable version (zipped package).
- Add new feature: double click splitter resets panes to equal size.
- Fix the plugin crash issue due to the inexistent plugin conf path.

## 7.3.3 – 2017-03-08

**Notepad++ v7.3.3 enhancements & bug-fixes**

- Fix CIA Hacking Notepad++ issue ([https://wikileaks.org/ciav7p1/cms/page_26968090.html](https://wikileaks.org/ciav7p1/cms/page_26968090.html)).
- Fix mouse wheel to task list scroll crash bug.
- Fix flickering issue while switching back after modifying or deleting a document from outside.
- Support Motorola S-Record, Intel and Tektronix extended hex file formats.
- Improve multi-line tab: maintaining the selected tab position.
- Fix add char into word char list bug.
- Add Shift+Enter in Find dialog for searching in the opposite direction.
- Fix a regression that delimiter settings is not retained correctly.
- Add clear command button in shortcut mapper.
- Enhancement: file extension supported in Load/Save Session dialog if a session file extension is set.

## 7.0 – 2016-09-21

**Notepad++ v7 enhancements & bug-fixes**

- x64 build available.
- Fix the DLL Hijacking Vulnerability of previous versions (by updating NSIS to v3.0).
- Auto-updater improvement: periodical check can be disable via auto-update prompt dialog.
- Installer enhancement: Check if Notepad++ is running and ask the user to close it before continue.
- Enhancement: add conflict detection to Shortcut Mapper.
- Fix auto-completion on XML comment  and <?xml> tag bug.
- Fix file saving crash which can be reproduced through a specific way to save file.
- Fix a crash issue while UDL’s user keyword list is too long.
- Fix HDPI issues for some components (task list, margins and shortcut mapper).
- Add a new feature(optional) : Close the last document will quit Notepad++.
- Add more Change Case variants (Title Case, Sentence case, iVERT cASE, rANdOm caSe).
- Add Open file & open containing folder commands on selected file/folder name in text content.
- Add Search on Internet command on selected word(s) in text content.
- Add Scroll Tab Bar with mouse wheel capacity.
- Add commands for moving the current file tab Forward/Backward.
- Fix bug of monitoring not working for files under root.
- Ruby is supported by Function List.
- Added new option: Enable scrolling beyond last line.
- Add an option to restore old behaviour (open files in folder) while folder being dropped.

## 6.9 – 2016-02-22

**Notepad++ v6.9 bug-fixes and enhancements**

- Add “Folder as Workspace” feature (How to use: drop any folder in Notepad++).
- Fix Notepad++ hanging issue while user uses touchscreen to activate Notepad++ window.
- HTML auto-close tag enhancement: Prevent <br>, <hr>, <img>, <link> and <meta> from being closed automatically.
- Project enhancement: Allows user defined extension to associate workspace file.
- Make behavior of SHIFT+END and SHIFT+HOME more consistent when word wrapping is enabled.
- Add new API NPPM_SAVEFILE (for plugins) to save any file, not only the focused one.
- Add file extensions for FreePascal/Lazarus pascal, lex (as C).
- Update keywords for C, C++, JavaScript, Python and YAML.

## 6.8.7 – 2015-11-27

**Notepad++ v6.8.7 bug-fixes and enhancements**

- Fix crash while “backups and session snapshots” is activated.
- Restore file extension feature in save dialog.
- Fix crash issue while moving Find In Files progress window.
- Fix tab settings not working in javascript.
- Fix user customized keywords no effect in Javascript.
- Enhance language detection on “Save as”.
- Add back-quoted string support for javascript.
- Move position to center when using “-n” option in command line.
- Installer enhancement: Allow user to keep DSpellCheck plugin.

## 6.7.4 – 2015-01-10

_Keine Changelog-Liste auf der Seite._

## 6.6.6 – 2014-06-13

**Notepad++ v6.6.6 bug-fixes**

- Fix “Settings on cloud - Dropbox” not working problem if the dropbox path has been changed.
- Fix a saving issue in session snapshot and periodic backup feature while backup file is deleted or read-only.

## 6.6.4 – 2014-06-04

**Notepad++ v6.6.4 new feature**

- New feature: Settings on cloud - Dropbox
- Add backup path info for session snapshot & periodic backup feature.

## 6.2.3 – 2012-12-16

**Notepad++ v6.2.3 new features & bug-fixes**

- Fix find “\r\n” bug in RegExpr mode.
- Change “Delete file” command to “Move to Recycle Bin”.
- Add Remove empty lines feature.
- Change document default value from ANSI to UTF8 w/o BOM.
- Enable Word-completion under CJK environment for unicode document.
