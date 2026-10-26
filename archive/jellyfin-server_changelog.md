# Changelog: Jellyfin Server

Quelle: https://github.com/jellyfin/jellyfin/releases
Stand: 23.10.2026 06:45

---

## 12.3 – 2026-10-23

# :rocket: Jellyfin Server 12.3

We are pleased to announce the latest stable release of Jellyfin, version 12.3! This minor release brings several bugfixes to improve your Jellyfin experience. As always, please ensure you take a full backup before upgrading!

Discuss this release further [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-12-3).

## Changelog (7)

### 🏗️  Enhancements
* Suppresses useless warnings [PR #18337], by @thedreaddpirate
### 📈 General Changes
* Do not store ratings or gains that are not finite numbers [PR #18267], by @martimarkov
* Fix unbalanced parenthesis in the HalfTopAndBottom image extraction filter [PR #18325], by @cinadr
* Update Microsoft [PR #18418], by @Bond-009
* Treat a year off by one as a tie in TMDb result ranking [PR #18343], by @HaraldNordgren
* Fix crash when a subtitle charset has no .NET encoding [PR #18309], by @p27ZuH6CNAdzr
* Fix crash probing streams without frame size [PR #18243], by @myristate

## 12.2 – 2026-10-05

# :rocket: Jellyfin Server 12.2

We are pleased to announce the latest stable release of Jellyfin, version 12.2! This minor release brings several bugfixes to improve your Jellyfin experience. As always, please ensure you take a full backup before upgrading!

Discuss this release further [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-12-2).

## Changelog (51)

### 📈 General Changes
* Replace custom item display preferences in one transaction [PR #18266], by @martimarkov
* Use hvc1 for Dolby Vision profile 8 [PR #18300], by @theopeuchlestrade
* Make the OwnerId and ExtraType/OwnerId indexes partial so extras lookups keep using them [PR #18276], by @Shadowghost
* Enhance internal search provider for multiple scripts [PR #18223], by @excelsior-dev
* Dispose the database context in DeleteTrickplayDataAsync [PR #18269], by @martimarkov
* Fix orphan ItemValues cleanup after deletion [PR #17892], by @nintwentydo
* Fix off-by-one in the optimistic locking retry backoff [PR #18268], by @martimarkov
* Upgrade ATL to 7.18.0 to fix malformed FLAC hangs [PR #18224], by @ScottishTapWater
* Fix EPUB metadata and covers not loading on Windows [PR #18283], by @chino
* Refuse to start a set-up server whose database is missing or empty [PR #18264], by @martimarkov
* Compare local image dates with a one second tolerance [PR #18278], by @Shadowghost
* Only propagate a changed rating to children that follow it [PR #18280], by @Shadowghost
* Recognize numbered sample and trailer files as extras [PR #18255], by @HaraldNordgren
* Recompute the parental rating score whenever an item is saved [PR #18279], by @Shadowghost
* Compare person names without regard to case in the letter range filters [PR #18265], by @martimarkov
* Fix video quality at low bitrates when reducing bit depth [PR #18261], by @nyanmisaka
* Update episode season name after editing the season name [PR #18253], by @theguymadmax
* Fix segment cleaner deleting segments ahead of playback when remuxing MKV [PR #18186], by @klizas
* Fix user preferences when renaming libraries [PR #18236], by @z0rimo
* Fix item display preferences item [PR #18259], by @martimarkov
* Use XmlReader in encoder preset migration tests [PR #18237], by @maghuro
* Don't advance rewatch Next Up past a barely started episode [PR #18202], by @Shadowghost
* Keep an item's user data rows in agreement [PR #18001], by @Shadowghost
* Stop rebuilding the inherited-tag set per row, and count only the people /Persons can return [PR #18093], by @Shadowghost
* Never treat unresolvable libraries as grounds for deletion [PR #18102], by @Shadowghost
* Don't let a failed shutdown cancel an in-process restart [PR #18063], by @Shadowghost
* Match artist creation lookups using CleanName [PR #18005], by @orut34iop
* Serve graphical subtitles as raw files with range support [PR #18168], by @Shadowghost
* Use MusicBrainz artist name first [PR #18192], by @juxuanu
* Skip statistics on an empty library and refresh them after every scan [PR #18196], by @Shadowghost
* Check media directory write permission before generating trickplays [PR #18161], by @thedreaddpirate
* Reconcile missing episodes by episode, not by number [PR #18090], by @Shadowghost
* Apply stereo downmix filter consistently to progressive audio transcodes [PR #18195], by @Shadowghost
* Fix transcoding settings migration failure caused by null EncoderPreset [PR #18059], by @scr4bble
* Fix more rating systems [PR #18057], by @Shadowghost
* Fix ChangeOwnerIdToGuid migration performance [PR #18073], by @Shadowghost
* Retry MusicBrainz requests when the server is busy [PR #18095], by @Shadowghost
* Fix playlist views [PR #18104], by @Shadowghost
* Scope the music library cover image to that library's artists [PR #18148], by @Shadowghost
* Read the image region when determining TMDb image language in `TmdbUtils` [PR #18150], by @mateusbandeiraa
* Ignore Sample subfolders when resolving movie folders [PR #17964], by @panko
* Don't apply the allowed tags filter to by-name items [PR #18138], by @Shadowghost
* Only regenerate extra names that were generated by the scan [PR #18139], by @Shadowghost
* Skip optimistic expressions when parsing series names [PR #18061], by @panko
* Decode HTML entities in OMDb responses [PR #18096], by @Shadowghost
* Fix the item type name of BaseItemKind.Channel [PR #18132], by @martimarkov
* Log chapter image extraction once per video [PR #18107], by @Jellyfrog
* update tw.json (rating) [PR #18134], by @allexjuang
* Fix typo when parsing codec_tag_string [PR #18164], by @nyanmisaka
* Fix test concurrency [PR #18058], by @Shadowghost
* Fix formatting issue in PlayCommandQueueTests [PR #18079], by @theguymadmax

## 12.1 – 2026-09-15

# :rocket: Jellyfin Server 12.1

We are pleased to announce the latest stable release of Jellyfin, version 12.1! This minor release brings several bugfixes to improve your Jellyfin experience. As always, please ensure you take a full backup before upgrading!

Discuss this release further [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-12-1).

## Changelog (47)

### 📈 General Changes
* Stop resolving items with every field where only stored columns are read [PR #18039], by @Shadowghost
* Fix nested unnumbered season folders collapsing onto the first one [PR #18044], by @Shadowghost
* Release a folder's children once its subtree has been scanned [PR #17884], by @Shadowghost
* Enforce channel mediasource id [PR #18037], by @Shadowghost
* Fix Norwegian ratings [PR #18017], by @theguymadmax
* Stop the library monitor from refreshing against a disposed host [PR #18020], by @Shadowghost
* Don't queue by-name items for playback and reject source requests for them [PR #17999], by @Shadowghost
* Fix forced-only not overriding remembered subtitles [PR #17998], by @Shadowghost
* Fix SyncPlay authentication error handling and limit group member wait time [PR #17938], by @Shadowghost
* Fix /UserViews exhausting memory and reporting random child counts [PR #17881], by @Shadowghost
* Fix device access revocation not logging out existing sessions [PR #18026], by @fmarcac
* Fix database optimization memory use and pre-migration backup integrity [PR #17836], by @Shadowghost
* Stop wrong-type alternate version cleanup from recursing [PR #18030], by @Shadowghost
* Fix incorrect color range during CSC after VK tonemapping [PR #18025], by @nyanmisaka
* Preserve active scans when requesting a background library refresh [PR #18006], by @orut34iop
* Clean up orphaned people when deleting items [PR #17897], by @nintwentydo
* Check Live TV access for a single user instead of enumerating all users [PR #18003], by @Shadowghost
* Fix slashed rating handling [PR #18002], by @Shadowghost
* Skip empty ZIP comments for ComicBookInfo [PR #17971], by @Shadowghost
* Fix EPG issues [PR #17935], by @Shadowghost
* Avoid full people scans and writes for unchanged credits [PR #18004], by @orut34iop
* Clean up invalid data before running migrations [PR #17835], by @Shadowghost
* Restore [JsonIgnore] on AggregateFolder.Children [PR #18011], by @Shadowghost
* Correct SyncPlay sessions that report playback at a stale position [PR #17797], by @fmarcac
* Don't let a torn-down WebSocket take down the request handler [PR #17958], by @Shadowghost
* Fix SimilarItemsManager concurrency [PR #17982], by @Shadowghost
* Delete the full ownership closure when deleting items [PR #17873], by @Shadowghost
* Fix versions of a video still listing separately from their group and preserve manual merges [PR #17842], by @Shadowghost
* Preserve library items when directory enumeration fails [PR #18007], by @orut34iop
* Don't resample or sharpen images Skia isn't actually resizing [PR #17956], by @Shadowghost
* Drop dead item data and fix query ordering and bound parameters [PR #17980], by @Shadowghost
* Stop requesting unused credits when looking up a TMDb person [PR #17973], by @Shadowghost
* Use thumbs for image tmdb image preview [PR #17924], by @enter-a-random-username
* Fix playlist encoding recognition [PR #17930], by @Shadowghost
* Populate missing tags array in Filters2 [PR #17898], by @Shadowghost
* Fix collection creation when the collections library was just added [PR #17950], by @Shadowghost
* Don't record a failed refresh as a completed one [PR #17947], by @Shadowghost
* Fix Italian ratings [PR #17933], by @Shadowghost
* Fix ContainsSubPath check [PR #17929], by @Shadowghost
* Fix trickplay using the wrong video stream [PR #17883], by @crobibero
* Fix metadata provider order needing a restart to apply [PR #17939], by @Shadowghost
* Fix decimal point handling in version names [PR #17931], by @Shadowghost
* Improve SeriesNameRegex [PR #17858], by @Shadowghost
* Report image resolutions for TMDb images when no image size is configured [PR #17859], by @Shadowghost
* Fix transcode throttling not enabling on supported systems (caused by race condition) [PR #17906], by @SimonvBez
* Only group episodes as versions on a confident path parse [PR #17890], by @Shadowghost
* Match parental ratings case-insensitively [PR #17844], by @Jellyfrog

## 12.0 – 2026-09-08

# :rocket: Release notes for 12.0

## Notes on Updating
Before upgrading from an earlier version, a full backup of the data directory is strongly recommended, as this release includes database changes that prevent rolling back without a full restore.

Direct upgrades from 10.10.7 and 10.11.x to 12.0 are supported; intermediate upgrades are not required. Users running releases older than 10.10.7 are strongly encouraged to upgrade to 10.10.7 before migrating to 12.0.

Installed repository plugins (anything not built-in) should also be removed before migrating. Plugins will likely need time to adapt to the new database changes, so re-adding them afterward is the safest approach for testing.

Official plugins compatible with Jellyfin are available through the stable plugin repository. If you have changed to the unstable plugin repository please change it back.
* Go to Dashboard -> Plugins -> Manage Repositories 
* Update the Plugin Repository URL to: https://repo.jellyfin.org/files/plugin/manifest.json

After migrating please perform the following steps.
* Perform a full library scan to restore alternative versions


If you run into issues, please prefix bug reports with "[12.0]".

## Packaging

* Debian Bullseye and Ubuntu Focal packages are no longer built

## Server

* Performance PR implications https://github.com/jellyfin/jellyfin/pull/16062
    * We're running a full path-based check on all library items to clean up left overs. Depending on size this can take some time 
    * Alternative versions of media that were auto resolved (not manually merged) will be removed due to data type issues -> A full library scan will fix this again and is therefore REQUIRED AFTER UPGRADE
    * First scan will take significantly longer than normal and some movies might appear as newly added due to type issues that got fixed on-scan
- Multiple versions for episodes
- Similarity & recommendation providers
- Search providers, letting plugins extend or replace how search results are produced
- SchedulesDirect and EPG refresh fixes
- Fixes to the parental rating system
- Proper data pruning on file replacement/deletion
- Support triple+ digit episode numbers
- Add library-specific BoxSet and Playlist filtering, allowing per-library collection and playlist views
- `CACHEDIR.tag` support
- `Accept-Language` header support
- Add VideoRotation profile condition for Android TVs that do not support rotation metadata
- Parse provider IDs from season and episode folder/file names
- Allow tmdb, tvdb, and imdb as aliases for the tmdbid, tvdbid, and imdbid provider IDs
- Add curly brace and parentheses support for parsing attribute values
- Add NameStartsWith and NameLessThan filters to Person search
- Add new filters for audio and subtitle languages
- Add OriginalLanguage as option to PreferredAudioLanguage
- Add a collection API for Included In feature
- Add support for VobSub subtitle streams
- Add Tmdb missing episode provider

### Breaking and behavior changes

- Legacy route prefixes removed (`/emby/*` and `/mediabrowser/*`). Old third-party clients that rely on them will stop working
- Legacy authorization is now disabled by default, and a migration disables it on existing installs as well
- Removed obsolete API routes: `POST /Users/{userId}/EasyPassword` (the EasyPassword feature is gone), `GET /Items/{itemId}/CriticReviews`, `GET /Environment/NetworkShares`, `POST /System/MediaEncoder/Path`, `GET /LiveTv/Recordings/Groups/{groupId}`, and `GET /QuickConnect/Initiate`
- The global subtitle configuration has been removed, subtitle settings are configured per library
- `.ogg` is no longer treated as a video extension and is audio only, `.aifc` is now recognized as audio, and `.aiff` is no longer treated as an image
- Symlinks are only resolved at playback time
- Sorting by name now uses `SortName` and `CleanName`, and the same cleaning logic is applied to `ForcedSortName`. Library ordering may change compared to 10.11
- Image endpoints no longer upscale beyond the source resolution, so low resolution artwork renders at its real size instead of being enlarged
- Username capitalization can now be changed. Usernames are stored in a normalized column with a unique index, so installs with usernames that differ only by case need to be corrected before upgrading

### Database and performance

- Playlists and collections are now properly relational, using a new `LinkedChildren` table instead of serialized child lists. `OwnerId` and `PrimaryVersionId` are real GUID foreign keys, and `ExtraIds` has been dropped
- Many tuning migrations covering item counts, item names, type and clean name, latest items, image info, and primary version id
- Migration routines clean up existing data on first boot: duplicate music artists and people are merged, orphaned extras and external data are removed, incorrect owner relationships are repaired, and clean names, forced sort names, and series presentation keys are recomputed
- Heavy database tasks no longer run while a library scan is in progress
- Faster queries for Resume, Next Up, rewatching, Latest Items for music, playlists and collections, artist lookup, and item counts
- Item deletion is batched, which fixes "too many SQL variables" failures when deleting large numbers of items
- `jellyfin.db` can now be stored at a custom path

### Operations

- New `--mode` startup flag with `MediaServer`, `MigrateSystem`, and `SeedSystem`, allowing migrations or database seeding to be run without starting the server. This is useful for containerized and orchestrated deployments and for controlled upgrades
- The startup interface has been restyled and now shows version and activity information
- Disabled plugins are no longer re-enabled on restart
- Full system backups skip corrupt keyframe rows instead of failing

### Media and subtitles

- Subtitle writing now goes through SubtitleEdit, which is what avoids the SSA to ASS conversion and loss of styles
- External subtitles can be embedded into MKV when transcoding
- The subtitle extraction timeout is now configurable
- Client-rendered graphical subtitles are allowed during remux
- Fixes for races in concurrent subtitle conversion, cache invalidation when a subtitle is replaced, and ffmpeg hangs during extraction
- New `HlsAudioSeekStrategy` configuration option
- Trickplay: existing files are discovered during a scan, duplicates from interlaced video are fixed, invalid PTS values from containers are normalized, and the cache is cleaned up after a failure

### Live TV

- Live TV no longer returns unreachable "server-local" streaming URLs to clients
- XMLTV background images and episode thumbnails are now imported
- XMLTV guide imports skip programs whose data has not changed, using an ETag computed from the fields the server actually consumes, which makes repeat guide refreshes considerably cheaper. Other listings providers stay on the existing field-by-field update path

### Metadata and providers

- ListenBrainz is now bundled with the server and provides similar artist data with a selectable similarity algorithm
- TVDB provider IDs are supported for movies
- AudioDb artist search
- ReplayGain album gain is parsed
- MusicBrainz lookups are more resilient
- WEB-DL release tags are recognized in file names
- Hyphenated numbers in episode titles are no longer parsed as multi-episode files
- 3D format detection works when the tag is the last token of the path
- Person metadata refreshes are queued instead of blocking the request

## Transcoder

- New upstream version of FFmpeg 8.1
- Optimized CUDA transposing filter performance
- Optimized OCL scaling filter performance
- Optimized OCL tonemapping filter performance on Mali GPU
- Use EOTF from BT 2446 Method B for HLG tonemapping
- Fix potential A/V desync in HLS when transcoding video while remuxing audio
- Avoid SSA to ASS conversion and loss of styles
- Add spec-compliant dvh1 HLS variant for DoVi P5 for compatibility

## Web

* The Modern layout is now the default, the previous layout is now called Legacy
* Updated Music Videos view
* Updated Mixed Media view
* Updated Collections & Playlists view
* Updated Books view
* Add still watching prompt
* Add delay setting for photo slideshow
* Add caching of queries to indexed db for the tanstack query client for improved loading performance
* Add watch feature to log viewer
* Add ```,``` and ```.``` as controls to scrub frame-by-frame
* Add filters for audio and subtitle languages (modern layout only)
* Add Collections and playlist tab to all libraries 
* Add collections to item details page
* Replace libpgs with libbitsub and adds support for vobsub rendering
* Merge cards for crew with multiple roles

### Layout and themes

* All themes now derive from a shared base theme built on CSS variables, including Dark, Light, WMC, Blue Radiance, Apple TV, and Purple Haze. Custom themes may need to be adjusted
* The library toolbar has been merged into the app bar, with a sticky library header and design polish throughout the library
* Custom links can be added to the Modern layout
* The screensaver time setting is now available in the Modern layout

### Libraries and browsing

* Collections and folders tabs for book libraries, and a folder view in the Modern home videos layout
* Default tab options for Home Videos and Photos libraries
* Studio search, and an extended Studios tab
* Play All and Shuffle buttons on the series library. Both are disabled rather than hidden when no items are available
* Improved Upcoming view
* Sorting and filtering on the Activity page
* A Reset Filters button in the filter dropdown
* Folders can be marked as played
* TV show creators are shown on item details
* Similarity providers can be configured per library
* Pagination controls are hidden when paging is disabled

### Playback

* The playback info overlay is more compact and shows more detail
* Chapter names are shown in the OSD slider bubble
* Bitrate detection now runs in web
* Dolby Vision in MKV on webOS 25 and newer
* AV1 fMP4 stream copy on TV clients
* Direct play of anamorphic video on Tizen, and loosened anamorphic restrictions for browser device profiles
* On iOS, background playback continues when the screen is turned off, and audio normalization is disabled to fix pitch and speed issues
* libbitsub updated to v1.11.0 with an HLS offset fix
* The screensaver is suppressed while viewing photos or reading

### TV and remote

* Game controller navigation fixes, and the gamepad repeat rate is no longer tied to framerate
* Keyboard controls work on non-Latin keyboard layouts, with additional fixes for older browsers
* Rewind and FastForward play state commands are handled
* SyncPlay menu update, and the SyncPlay ping is now reported to the server
* Focused and checked checkbox styling in the TV layout

### Under the hood

* WebSockets have been migrated to SDK subscriptions
* The React and TypeScript migration continues with the libraries, Live TV, and networking pages, and the dashboard user pages now use the TS SDK
* TanStack Query now backs user settings and home screen sections, and the query cache is cleared when the server restarts

### Notable fixes

* Blurry card images on high DPI displays, and card image sizes are rounded up
* Duplicate `/socket` connections
* Login loop, connecting to the wrong server when several are configured, and native shell server selection when signing out
* An invalid request for all items on page load
* The Live TV default landing tab
* Holding and dragging on media no longer activates multi-select
* A warning is shown before restoring a version, a warning is shown when starting a backup while a scan is running, and a library scan starts automatically when folders are added to a library

## Security

Server:

* Path validation has been added to the legacy HLS segment endpoints and to the plugin image endpoint, so a requested file must resolve inside the transcode directory
* Path traversal hardening has been extended to the image and plugin endpoints and to username path handling, building on the fixes released in 10.11.x
* The startup wizard can no longer be re-run without authentication on a misconfigured server
* Unsafe plugin package names are rejected by the plugin installer
* Parental filtering is enforced on additional endpoints, playlist visibility has been corrected, non-admin access to additional parts has been fixed, and people are exempt from the allowed tags visibility check

Web:

* Cross-site scripting via person roles
* Auth parameters are encoded when creating API clients
* The login disclaimer only allows common link protocol schemes

## Books

Books have often taken a backseat in favor of video playback in Jellyfin, but this should no longer be the case.
We have started a concerted effort to improve book support across the API and our official clients.
eBook and comic support is still maturing, but the ODPS plugin allows for direct access from a wide range of popular self-hosted programs.
Correspondingly, contributions in any repository are extremely welcome from the wider community.
That includes server improvements, documentation changes, and third-party clients for book playback.
A combination of eBook, comic, and audiobook support is available on the following clients.

Official: Web, iOS, Android, Desktop, Roku, Kodi, JMP
Community: JellyBook, Symfonium, Jellium, Plappa

One notable omission from the server is book series as unique entities, which didn't make the cut for this release.
If you would like to bridge the gap until they are added, feel free to use the [Folio](https://github.com/dkanada/jellyfin-plugin-folio) plugin to display them as collections.
It functions very similar to the [TMDb Box Sets](https://github.com/jellyfin/jellyfin-plugin-tmdbboxsets) plugin but only applies to eBooks.

Another in-flight feature is audiobook chapters, which are only available from the API at present.
Luckily, this means client support is now possible, so you should see them appear in your favorite audiobook client before our next server release.

> NOTE: The Bookshelf plugin has been deprecated and its features have been merged into server or extracted into the ComicVine and GoogleBooks providers.

### Server Changes

* Bookshelf has been split into separate GoogleBooks and ComicVine providers
* Local book parsing has been improved and is available without plugins
    * Book metadata is extracted directly from OPF and ComicInfo files or ComicBookInfo comments
    * External covers are now supported for audiobook files
    * Posters are generated for EPUBs and all supported comic archives
    * Name, index, year, and series are parsed from book filenames
    * Both volume and chapter will be available in the API when present in comic filenames
    * Page counts are extracted from comic archives and PDFs
    * Creator names from OPF data are normalized to a common format
* A new OpenLibrary plugin has been created for metadata and images
* ISBN external IDs and links are supported
* Chapters are now extracted from audiobooks

### Web Changes

* Modern book library layout has been added with view types and paging
* Books display information about their authors and vice versa
* Playback interface has been redesigned and standardized across all book types
* Progress indicator is enabled again for supported eBooks
* Sorting books by index number, release date, etc is now available
* Font size selection has been improved for EPUB files
* Background audiobook playback is working on iOS devices
* Authors, collections, and folders tabs have been added to book libraries, and audiobooks appear under authors
* Fullscreen behavior is unified across all book players, and PDFs support swipe navigation

## Developers

### API Changes

The API no longer allows the use of deprecated authorization mechanisms by default.
Clients and tooling need to migrate if they haven't done so already. See https://github.com/jellyfin/jellyfin/pull/15559 for details.

There have been a number of other changes to the SDK libraries and API as part of an ongoing effort to better document the API for client use.
Please note the following with regards to API support.
A full explanation of our policy for API changes will be added to the developer documentation in the coming months.

- If an endpoint isn't listed in the OpenAPI specification it should not be used by clients.
    - There are certain endpoints that are still exposed for legacy reasons despite being excluded from the OpenAPI spec.
    - These can be removed in any major release without warning
- If an endpoint or parameter is marked as obsolete in the OpenAPI specification it should not be used by clients.
    - Same explanation as above.
- As a general rule, any deprecations will be marked as such for an entire (major) release cycle before the deprecated endpoint or parameter is liable for removal.

Behavior changes clients should be aware of:

- `GetItems` is now asynchronous and applies `recursive` when filters are requested, limited to requests that include `includeItemTypes`. The same query can return a different result set than it did on 10.11
- `ItemByName` responses are restricted and people are deduplicated
- Newly obsolete but still functional, with replacements:
    - `GetTrailers` -> use `GetItems` with `includeItemTypes=Trailer`
    - `GetArtists` and `GetAlbumArtists` -> use `GetPersons`
    - `GetArtistByName` -> use `GetPerson`
    - `GetMusicGenre` -> use `GetGenre`
    - `GetInstantMixFromMusicGenreById` and `GetInstantMixFromMusicGenreByName` -> use `GetInstantMixFromItem`
    - `GetStartupConfiguration`, `UpdateInitialConfiguration`, and `SetRemoteAccess` -> use the configuration endpoints
    - `GetRecordingsSeries`
    - `UserDto.HasPassword` is marked obsolete and no longer provides useful information
- The HLS controllers are hidden from the specification

### Platform

- The server now targets .NET 10. Plugins have to be retargeted and rebuilt
- Swashbuckle has been updated to v10, which changes the generated OpenAPI document, so SDKs need to be regenerated
- jellyfin-web now builds with Node 24 LTS and npm 11

### Plugin changes

- `ISearchEngine` has been replaced by `ISearchManager`, and `SearchEngine` has been replaced by `SearchManager` together with `SqlSearchProvider`
- Removed: `NowPlayingQueueFullItems`, `DtoExtensions.AddClientFields`, `Jellyfin.Extensions.AlphanumericComparator`, the `ISubtitleWriter` family of subtitle writers, and `SubtitleOptions` with `SubtitleConfigurationFactory`
- `ServerConfiguration.EncoderPreset` is no longer nullable
- `IAuthenticationProvider.HasPassword` has been removed
- `IPasswordResetProvider.StartForgotPasswordProcess` takes the entered username and a nullable user
- `IUserManager`: the `Users` and `UsersIds` properties are now the `GetUsers` and `GetUsersIds` methods, and `RenameUser`, `ResetPassword`, and `ChangePassword` take a user id instead of a `User`. `GetFirstUser` has been added
- Several `IItemRepository` members moved to the new services: item saving and deletion and `UpdateInheritedValues` to `IItemPersistenceService`, counts to `IItemCountService`, and Next Up series keys to `INextUpService`
- `IPeopleRepository.GetPeople` and `ILibraryManager.GetPeopleItems` return a `QueryResult`, and `IDtoService.GetBaseItemDtos` and `ILibraryManager.DeleteItemsUnsafeFast` have new signatures
- `IDirectoryService.GetFilePaths` no longer takes a `sort` argument, and the `IPathManager` subtitle and attachment path getters are now nullable

### New plugin APIs

This release adds several extension points that plugins could not hook into before.

- **Search providers.** Plugins can now take part in search itself rather than only in metadata lookup. `ISearchProvider` exposes `Name`, `Type`, `Priority`, and `CanSearch(SearchProviderQuery)`, with `IInternalSearchProvider` for providers that search the local library and `IExternalSearchProvider` for providers that stream `SearchResult` items from a remote service. Providers are registered through `ISearchManager.AddParts` and are consulted in priority order, so a plugin can extend or take over from the built-in `SqlSearchProvider`
- **Similarity and recommendation providers.** `ISimilarItemsProvider` is split inherited by `ILocalSimilarItemsProvider`, `IRemoteSimilarItemsProvider`, and `IBatchLocalSimilarItemsProvider`, each with a generic variant so a provider can declare the item type it handles. Providers are selected and ordered per library through `LibraryOptions.SimilarItemProviders` and `SimilarItemProviderOrder`, and `ISimilarItemsManager` also pulls movie recommendations. The bundled ListenBrainz provider is built on this
- **Comic metadata providers.** `IComicProvider` (`ReadMetadata` and `HasItemChanged`) lets a plugin supply comic metadata alongside the built-in ComicInfo and ComicBookInfo readers
- **Chapters for any item type.** `IChapterManager.SaveChapters` now takes a `BaseItem` rather than a `Video`, and gained a `Supports(BaseItem)` check. This is what makes audiobook chapters possible, and it lets plugins save chapters for non-video items
- **Password resets for unknown users.** `IPasswordResetProvider.StartForgotPasswordProcess` now receives the entered username along with a nullable user, so a provider can handle a request for a username the server does not know or hand the reset off to an external provider
- **Media segment cleanup.** `IMediaSegmentProvider.CleanupExtractedData` is called when an item's data is pruned, so segment providers can remove their own extracted files
- **Schedules Direct.** `ISchedulesDirectService` exposes available countries, service availability, and the image daily limit state, so Live TV plugins no longer need to reimplement them. `ITunerHostManager.DeleteTunerHost` allows removing a tuner
- **Alternate versions and linked children.** Now that linked children are relational, `ILibraryManager` exposes `ResolveAlternateVersion`, `GetLocalAlternateVersionIds`, `GetLinkedAlternateVersions`, `GetItemIdsWithAlternateVersions`, and `UpsertLinkedChild`. Plugins that manipulated version links through serialized item data need to move to these
- **Batch APIs for bulk work.** `IUserDataManager` gained `GetUserDataBatch`, `GetResumeUserData`, `GetResumeUserDataBatch`, and `ResetPlaybackStreamSelections`. `ILibraryManager` gained `GetPeopleByItems`, `GetPeopleNamesByItems`, and `GetNextUpEpisodesBatch`. `IItemCountService` offers batched child and played/total counts
- **Localization.** `ILocalizationManager.GetServerLocalizedString` and `GetLanguageDisplayName` let plugins localize against the server locale
- `ICollectionManager.GetCollectionsContainingItem` backs the Included In feature, and `IPlaylistManager.AddItemToPlaylistAsync` takes a position so items can be inserted at the top of a playlist

`IHasEmbeddedImage` is also new, but it is only for plugins compiled into the server; external plugins should keep declaring their image with `imagePath` in `meta.json`.

### TLS Configuration

In the previous release notes 10.11.0 we announced the deprecation of the built-in TLS certificate handling for this version. This change has been postponed to a future version.

---

Discuss this release further [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-12-0).

## Changelog (460)

### 🔒 Security
* Potential FFmpeg argument injection via unescaped subtitle file path [[GHSA-wwwm-px48-fpvq](https://github.com/jellyfin/jellyfin/security/advisories/GHSA-wwwm-px48-fpvq)]
### 🌟 Highlights
* Implement multiple versions for episodes. [PR #16828], by @Shadowghost
* Disable legacy authorization methods by default [PR #15559], by @nielsvanvelzen
### 🏗️  Enhancements
* Fix movie recommendations [PR #16856], by @Shadowghost
* Have device deletion take list of ids [PR #12834], by @LePips
* Allow tmdb as an alias for tmdbid provider id [PR #16433], by @theguymadmax
* Fix EPG issues [PR #16220], by @Shadowghost
* Add CACHEDIR.tag support [PR #16478], by @Shadowghost
* Remove global subtitle configuration [PR #14957], by @KGT1
* Fix: normalize punctuation when computing CleanName so searches without punctuation match (closes #1674) [PR #14879], by @audrey-inglish
* refactor(StreamInfo): reorganize subtitle URL logic and conditions [PR #13977], by @sususu98
### 📈 General Changes
* Fix Blu-ray multi-angle concat generation [PR #17824], by @Raspberry-Monster
* Expose optimized ItemCounts for byName items [PR #17821], by @Shadowghost
* Only download missing plugin images [PR #17820], by @Shadowghost
* Apply the resize sharpening kernel directly instead of via SKImageFilter [PR #17775], by @slevin-7
* Share played state across alternate versions [PR #17816], by @Shadowghost
* Fix TMDb search result ranking [PR #17819], by @Shadowghost
* Fix TMDb recommendations [PR #17810], by @Shadowghost
* Better handle timeouts on plugin operations [PR #17794], by @Shadowghost
* Don't dispose application singletons after running a code migration [PR #17791], by @Shadowghost
* Enforce dolby vision transfer check [PR #17806], by @gnattu
* Fix items being lost from the refresh queue and bound the directory service caches [PR #17763], by @Shadowghost
* Fix handling of unordered multi-episode NFOs [PR #17805], by @Shadowghost
* Optimize database after migrations [PR #17786], by @Shadowghost
* Bound change batches during a scan; keep ffprobe and image saves from failing [PR #17762], by @Shadowghost
* Fix PGS subtitles for BDMV with TrueHD [PR #17674], by @Oggeb1
* Probe .idx instead of .sub for external VobSub subtitle language detection [PR #17746], by @kfarnung
* Drop SyncPlay requests from sessions that left the group [PR #17799], by @fmarcac
* Fix Live TV HLS playback: bogus audio encoder and unplayable direct played manifests [PR #17768], by @Shadowghost
* Fix crash when SyncPlay shuffle mode is set to sorted twice [PR #17796], by @fmarcac
* Fix SyncPlay active session counter leaking on rejoin [PR #17800], by @fmarcac
* Fix unit mismatch in the SyncPlay resume delay floor [PR #17798], by @fmarcac
* Add comprehensive logging for post scan tasks [PR #17767], by @Shadowghost
* Fix UI stalls caused by large tag and genre sets [PR #17757], by @felixfoertsch
* Bound the TMDb response cache so a library scan cannot fill it without limit [PR #17764], by @Shadowghost
* fix: return fallback gracefully when requested fallback font is missing [PR #17761], by @zerafachris
* Fix people and artist validator creation and deletion handling [PR #17756], by @Shadowghost
* Add progress logging to data migrations [PR #17743], by @Shadowghost
* Enforce reliable processing order in PeopleValidationTask [PR #17750], by @Shadowghost
* Fix recursive handling for LinkedChildren [PR #17752], by @Shadowghost
* Fix ListenBrainz settings and similar item defaults [PR #17748], by @Shadowghost
* Fix item counts on the by-name endpoints [PR #17724], by @Shadowghost
* Enforce permissions on similar items [PR #17729], by @Shadowghost
* Fix formatting and test [PR #17744], by @Shadowghost
* Filter search candidates by user access in a single query [PR #17739], by @Shadowghost
* Support anime provider ids on season folders [PR #17731], by @Shadowghost
* Count a season's episodes by the season they belong to [PR #17735], by @Shadowghost
* Fix ParentId for episodes in virtual seasons [PR #17719], by @theguymadmax
* Persist the refresh stamp so the people task stops redoing its work [PR #17709], by @Shadowghost
* Fix children count on virtual items [PR #17718], by @Shadowghost
* Delete credits nothing maps to and bound item-by-name folder names [PR #17715], by @Shadowghost
* Build a TMDb series cast from the aggregated credits [PR #17716], by @Shadowghost
* Stop deriving user view ids from their localized name [PR #17714], by @Shadowghost
* Fix IsPlayed and IsUnplayed sorting for shows and collections [PR #17713], by @LTe
* Say which image and item failed instead of logging a blank path [PR #17711], by @Shadowghost
* Fix OMDB People handling [PR #17710], by @Shadowghost
* Fix person metadata not being fetched on demand or by the people task [PR #17702], by @Shadowghost
* Fix series merging leaking across libraries and under-counting merged children [PR #17693], by @Shadowghost
* Fix English metadata blocking localized providers ranked below it [PR #17619], by @Shadowghost
* Look up people by item via the credit map instead of a full scan [PR #17700], by @Shadowghost
* Mark breakOnNonKeyFrames as XMLIgnore [PR #17698], by @Shadowghost
* Fall back to the ancestor filter when a view has no top parents [PR #17691], by @Shadowghost
* Safeguard against invalid provider ids [PR #17584], by @Shadowghost
* Optimize query helper memory [PR #17607], by @Shadowghost
* Allow direct play for HDHomeRun Live TV tuners [PR #17682], by @theguymadmax
* Fix latest items for mixed libraries [PR #17678], by @theguymadmax
* Stop user updates from orphaning permission and preference rows [PR #17645], by @Shadowghost
* More resilient MusicBrainz lookup [PR #17670], by @Shadowghost
* Use client-reported position for idle playback cleanup [PR #17631], by @itsb
* Fix GitHub URL typo in CONTRIBUTORS [PR #17659], by @FirmaSpring
* Fix SQLite variable limit in child count batches [PR #17658], by @martin-77
* Prevent orphaned user permissions and preferences [PR #17643], by @m0g3r
* Fix large playlist persistence with WhereOneOrMany [PR #17655], by @martin-77
* Fix other two unit test for localization of Artists in DE [PR #17637], by @IDisposable
* Recognize WEB-DL release tags in video names [PR #17636], by @st7105
* Fix unit test for localization of Artists in DE [PR #17633], by @IDisposable
* Fix FindArtists [PR #17604], by @theguymadmax
* Fix EF core designer drifts [PR #17570], by @Shadowghost
* Fix missing ItemRemoved events and search fallback after access filtering [PR #17579], by @Shadowghost
* Fix PersonTypes not applied when filtering by person [PR #17597], by @theguymadmax
* Fix master build [PR #17599], by @Shadowghost
* Fix assemblies [PR #17582], by @Shadowghost
* Bugfix: #17547 | Batching MediaSourceCount into one call [PR #17576], by @obiwantoby
* fix: bound remote provider pagination [PR #17590], by @TOomaAh
* fix: correct IsAiring negation to exclude airing items [PR #17588], by @TOomaAh
* Stop image endpoints from upscaling beyond the source resolution [PR #17569], by @vavallee
* Cleanup and simplify query helpers [PR #17563], by @Shadowghost
* Add warning that PessimisticLockBehavior is unsafe [PR #17560], by @IDisposable
* Batch people lookups when building item DTOs [PR #17571], by @obiwantoby
* fix(images): disambiguate progress overlay cache keys [PR #17492], by @GOvEy1nw
* Fix by-name endpoints reporting TotalRecordCount=0 next to a populated Items array [PR #17541], by @vdatanet
* Clear metadata provider cache when provider parts are registered [PR #17525], by @rlauuzo
* Delete old related info in bulk as late as possible in UpdateOrInsertItems [PR #17555], by @IDisposable
* Fix disabled plugins being re-enabled on restart [PR #17521], by @Shadowghost
* Fix captured (and discarded) Execute exceptions [PR #17559], by @IDisposable
* Speed up UpdateOrInsertItems for related information [PR #17554], by @IDisposable
* Switch SQLite connection Cache to Private [PR #17558], by @IDisposable
* Fix concurrent ffmpeg segment racing [PR #17536], by @gnattu
* Parse ReplayGain album gain field [PR #17315], by @Florin-Popescu
* Improve People deduplication, fix search and restrict ItemByName responses [PR #17466], by @Shadowghost
* Fix PCM audio transcoding to wav returning HTTP 500 and headerless output [PR #17537], by @vdatanet
* Revert "Refresh Live TV channel icons on every guide update." [PR #17549], by @theguymadmax
* Keep folder extras with the item that owns the folder [PR #17524], by @Shadowghost
* Only treat series and seasons as resumable folders [PR #17523], by @Shadowghost
* Degrade ForceKeepAlive logs to debug [PR #17528], by @Shadowghost
* Fix extras naming and version assignment [PR #17456], by @Shadowghost
* Allow client-rendered graphical subtitles during remux [PR #17512], by @altqx
* Use CleanName when sorting by name [PR #17503], by @theguymadmax
* Fix AdjacentTo being ignored on non-recursive item queries [PR #17486], by @Shadowghost
* Fix video version links being read from stale serialised item data instead of the LinkedChildren table [PR #17482], by @Shadowghost
* Fix Live TV returning unreachable "server-local" streaming URLs to clients. [PR #17298], by @WizardOfYendor1
* Add Tmdb missing episode provider [PR #17147], by @Shadowghost
* Fix storage info lookup for Windows [PR #17500], by @theguymadmax
* Skip SIDX in fMP4 HLS segments [PR #17501], by @alchemyyy
* Fix (Un)Played filter correctness and performance [PR #17463], by @Shadowghost
* Queue person metadata refresh instead of blocking the item request and fix ItemCounts [PR #17460], by @Shadowghost
* Reevaluate pending migrations after each one instead of per stage [PR #17455], by @Shadowghost
* Allow duplicate LinkedChildren for Playlists [PR #17416], by @Shadowghost
* Implement AudioDb artist search [PR #17424], by @Shadowghost
* Fix 3D format detection when the tag is the last token of the path [PR #17310], by @TowyTowy
* Fix missing collection folder posters after initial scans. [PR #16409], by @elio42
* Fix series merging [PR #17417], by @Shadowghost
* Reduce correlated subqueries to improve query performance [PR #17422], by @Shadowghost
* Fix hyphenated numbers in episode titles parsed as multi-episodes [PR #17442], by @Shadowghost
* Fix incorrect year on local trailers [PR #17399], by @Shadowghost
* remove ogg from video extensions since it should only be used for audio [PR #17437], by @dkanada
* Avoid NRE when sorting by user-dependent keys without a user [PR #17395], by @paoloantinori
* Skip ComicInfo parsing if none exists [PR #17423], by @Shadowghost
* Fix play queue index handling in SyncPlay [PR #17234], by @Eneo-org
* Apply cleaning logic on ForcedSortName [PR #17402], by @Shadowghost
* Check the "name" tag for audio/subtitle probe to fix MP4 not showing correctly - Fixes issue #17418 [PR #17419], by @rwebster85
* Drain stderr and stdout concurrently for encoder validation [PR #17430], by @gnattu
* perf: avoid unnecessary list allocation in CheckForIdlePlayback [PR #17411], by @mbastian77
* Match VobSub MKS subtitle profiles by container [PR #17227], by @altqx
* Improve language filters to only fetch language codes that match the requested items/libraries (follow up to #9787) [PR #16980], by @TheMelmacian
* fix: don't throw ArgumentNullException on partial UpdateItem payloads (#17366) [PR #17370], by @zerafachris
* Prevent unauthenticated re-run of the startup wizard on misconfiguration [PR #17369], by @Shadowghost
* Truncate ISO-639-2 language display names at first delimiter [PR #17160], by @854562
* Fix subtitle encoding for local files [PR #17281], by @Shadowghost
* Backport and extend path traversal fixes [PR #17368], by @Shadowghost
* fix: skip corrupt KeyframeData rows during full system backup [PR #17367], by @zerafachris
* Add XML docs to small model enums and remove CS1591 suppressions [PR #17376], by @mbastian77
* Exempt people from the allowed tags visibility check [PR #17377], by @mbastian77
* extract page count from archives and PDFs [PR #17311], by @dkanada
* Feat (fix) - Skip reprocessing program information when importing XMLTV EPG data [PR #16933], by @WizardOfYendor1
* Fix profile image being impossible to clear when its in-memory key is temporary [PR #17282], by @TowyTowy
* Fix: Fetch the correct row matching the most up to date file [PR #17320], by @jordanmichaelrushing
* Fix race condition in concurrent subtitle conversion [PR #17342], by @LTe
* Make RequestHelpers.GetOrderBy generic and reuse it in ActivityLogController [PR #17324], by @damienmeur
* Add additional attribute aliases and improve attribute detection [PR #17254], by @sjakub
* Fix SchedulesDirect image limit recognition [PR #17347], by @Shadowghost
* Sort trailers for TV Shows [PR #17204], by @theguymadmax
* Add TVDB provider ID support for movies [PR #17255], by @theguymadmax
* Fix artists being displayed with albums [PR #17252], by @theguymadmax
* Remove libpostproc check for ffmpeg version validation [PR #17384], by @gnattu
* Fix linked whitespace after image badges in `README.md` [PR #17382], by @kaunkrishna
* normalize common formats for creator names in OPF data [PR #17291], by @dkanada
* Keep authenticated user entity in sync with persisted login timestamps [PR #17302], by @ElianCodes
* Normalize invalid PTS from containers for Trickplay generation [PR #17304], by @nyanmisaka
* Fix Resume query performance [PR #17365], by @Shadowghost
* Add XML docs to small entity interfaces and remove CS1591 suppressions [PR #17375], by @mbastian77
* Fix Swagger UI auth docs (#12990) [PR #16910], by @cha5u5
* Prevent ffmpeg from hanging extracting subtitles [PR #17297], by @IDisposable
* Show production companies under TV Shows' Studios [PR #17246], by @Rant423
* Fix potential garbled text in FFmpeg logs on Windows [PR #17288], by @nyanmisaka
* Remove PlaybackPositionTicks from MediaSourceInfo [PR #17327], by @Shadowghost
* Fix format negotiation in hybrid SW decode and CUDA tonemap pipeline [PR #17334], by @nyanmisaka
* Fix Identify returning wrong images [PR #17151], by @theguymadmax
* Update season and episode SeriesName when renaming a series [PR #17326], by @theguymadmax
* Remove episode image override hack [PR #17280], by @Shadowghost
* Fix path transversal exposure in Plugins [PR #17191], by @IDisposable
* Revert setting default BaseItemKind for CollectionType [PR #17348], by @theguymadmax
* Add XML docs to small channel types and remove CS1591 suppressions [PR #17343], by @mbastian77
* Add XML docs to small session model types and remove CS1591 suppressions [PR #17344], by @mbastian77
* Add XML docs to small DLNA model types and remove CS1591 suppressions [PR #17340], by @mbastian77
* Add XML docs to provider lookup info types and remove CS1591 suppressions [PR #17339], by @mbastian77
* Add XML docs to DeviceId and remove CS1591 suppression [PR #17338], by @mbastian77
* Limit similar items to user accessible libraries [PR #17337], by @Shadowghost
* Fix max login attempts [PR #17274], by @theguymadmax
* Add Novel job mapping to the Writing department [PR #17248], by @theguymadmax
* Allow SeriesName to be editable from Item Metadata (books) [PR #17250], by @jordanmichaelrushing
* Fix additional parts for non-admins [PR #17266], by @Shadowghost
* Fix incorrect protocol used for subtitle charset detection [PR #17306], by @theguymadmax
* Check numeric rating value after splitting country code [PR #17273], by @theguymadmax
* support external images for audiobooks [PR #17287], by @dkanada
* Fix Greece parental ratings [PR #17268], by @theguymadmax
* Fix actor images not displayed until clicked [PR #16668], by @johnpc
* Don't throw on logout if session does not exist [PR #17228], by @Shadowghost
* Use InvariantCulture when parsing machine-generated dates [PR #17238], by @iderex
* Fixes for multi version handling [PR #17044], by @Shadowghost
* Fix parental rating lookup for multi-rating entries [PR #17239], by @theguymadmax
* Fix ghost entries when deleting library paths [PR #17231], by @theguymadmax
* Allow changing capitalization of usernames [PR #17229], by @Bond-009
* Fix folder view [PR #17222], by @theguymadmax
* Close sessions for lost WebSockets to prevent zombie SyncPlay groups [PR #17079], by @Eneo-org
* Fix Swedish rating [PR #17209], by @theguymadmax
* Fix NullReferenceException in GetStreamingState for closed live streams [PR #17206], by @zachhide
* Use Enumerable.LeftJoin for activity log user query [PR #17175], by @obrenoalvim
* Rework bitrate reporting [PR #17170], by @Shadowghost
* Fix Book collections speed issues [PR #15954], by @IDisposable
* Batch duplicate-cleanup deletes in merge migrations [PR #17162], by @Shadowghost
* Remove orphaned people [PR #17140], by @theguymadmax
* Reject unsafe plugin package names in installer [PR #17013], by @dfederm
* Use Convert.ToHexStringLower for Schedules Direct password hash [PR #17174], by @obrenoalvim
* Live TV: re-fetch channel icons on guide refresh [PR #16914], by @danieltutuianu
* Revamp startup UI for visual style and usability [PR #17154], by @joshuaboniface
* Fix localization lookup [PR #17187], by @Shadowghost
* Fix embedded lyrics not updating on replace all refresh [PR #17134], by @theguymadmax
* Fix Live TV tuner not releasing [PR #17178], by @theguymadmax
* Don't run heavy DB tasks while scan is running [PR #17182], by @Shadowghost
* Fix local Comic book plugin registration [PR #17188], by @Shadowghost
* Fix too many SQL variables in DeleteItem for large batch deletes [PR #17153], by @joshuaboniface
* Fix Identify returning wrong results [PR #17146], by @theguymadmax
* Fix audio sample rate forced to 48 kHz for non-Opus codecs [PR #17090], by @moontwister
* Deprecate the redundant /Trailers endpoint [PR #17094], by @moontwister
* Skip parsing root-level folders in SeriesResolver [PR #17116], by @theguymadmax
* Fixed "Deleting media that is still being watched in SyncPlay results in errors" [PR #14935], by @pokreman06
* Fix series year lost during name parsing [PR #17112], by @theguymadmax
* Fix episode air date offset after initial scan [PR #17121], by @theguymadmax
* Follow native interoperability best practices [PR #17099], by @Bond-009
* improve book resolution from filename [PR #17087], by @dkanada
* Extend TranscodingReason reporting [PR #17106], by @Shadowghost
* Always apply recursive when filters are requested [PR #17088], by @Shadowghost
* Fetch TV Shows creators from TMDB [PR #17107], by @Rant423
* Replace usage of SharpCompress [PR #17089], by @Bond-009
* Fix AlbumIds filtering by Name instead of by Id [PR #17085], by @matt-teahan
* Add support for background images and episode thumbnails from XMLTV [PR #17077], by @SheaSmith
* Fix AudioDb album description not displayed for English (mirror of #16606) [PR #17081], by @Gadnief
* Fix duplicate key collision [PR #17083], by @theguymadmax
* Assign correct season info to new episodes [PR #17051], by @ivanjx
* Fix CleanName and CleanValue refresh [PR #17064], by @Shadowghost
* Fix duplicate trickplay images for interlaced videos [PR #17058], by @nyanmisaka
* migrate local comic providers to server codebase [PR #16444], by @dkanada
* Add code assistance section to PR template [PR #17054], by @nielsvanvelzen
* Prefer local alternate versions when deduplicating linked children [PR #17042], by @Shadowghost
* Media source handling fixes [PR #17041], by @Shadowghost
* Refresh live TV channel image when remapped (alt #7843) (fixes #7834) [PR #10841], by @Bond-009
* Implement search providers [PR #16121], by @Shadowghost
* fix(dto): prefer PlaylistsFolder primary image for playlists tiles [PR #16520], by @beateixeira04
* Fix xUnit1051 in UserManagerLockHelperTests [PR #17043], by @Shadowghost
* Update issue template version to 10.11.11 [PR #17035], by @theguymadmax
* Discover existing trickplay files on scan [PR #16945], by @Shadowghost
* Fix external data pruning on item deletion [PR #16941], by @Shadowghost
* Fix subtitle replacement not invalidating cache [PR #17028], by @Shadowghost
* Fix playlist visibility [PR #17025], by @Shadowghost
* Enforce parental filtering on additional endpoints [PR #17019], by @Shadowghost
* Prefer subtitle extension over codec [PR #16998], by @Bond-009
* Improve Merge Conflict Labeler [PR #17018], by @Bond-009
* Fix season unknown for flat TV structures [PR #16995], by @theguymadmax
* Make EncoderPreset non nullable [PR #17007], by @nyanmisaka
* Only default recursive to true if we have includeItemTypes [PR #16999], by @Shadowghost
* Extract attachments in one ffmpeg command when dumping [PR #16915], by @Shadowghost
* Fix incorrect list capacity [PR #16996], by @theguymadmax
* Trim tags [PR #16994], by @theguymadmax
* Fix recently added episode links and posters [PR #16967], by @Shadowghost
* Write subtitles using SubtitleEdit [PR #16805], by @Bond-009
* Re-disable legacy authorization methods by default [PR #16992], by @theguymadmax
* Only resolve symlinks on playback [PR #16965], by @Shadowghost
* Fix folders being identified as seasons in mixed libraries [PR #16259], by @theguymadmax
* Fix Schedules Direct API Error Codes [PR #16920], by @arazilsongweaver
* Fix similarity [PR #16942], by @Shadowghost
* Fix inaccessible artist when they exist in multiple libraries [PR #16977], by @theguymadmax
* Add support for VobSub subtitle streams [PR #16552], by @altqx
* Compare old file byte-by-byte to new stream [PR #16936], by @IDisposable
* Remove NowPlayingQueueFullItems from session DTOs [PR #16976], by @PCEWLKR
* Use ConfigureAwait(false) in CollectionController [PR #16953], by @PCEWLKR
* Fix CA2007 warnings in InstallationManager [PR #16946], by @jonesy827
* Add a collection API for `Included In` feature [PR #15516], by @XSAM
* Add new viewtypes options [PR #16177], by @theguymadmax
* Fix Merge Conflict Labeler #2 [PR #16963], by @Bond-009
* Fix A/V desync when resuming HLS with video transcode + audio copy [PR #16580], by @LTe
* Improve OriginalLanguage normalization and inheritance [PR #16829], by @Lampan-git
* Update issue template version to 10.11.10 [PR #16927], by @theguymadmax
* Fix inconsistent extradata generated by hevc_vaapi on AMD driver [PR #16913], by @nyanmisaka
* Backport: Fix/user manager collation [PR #16919], by @Bond-009
* fix: suppress repeated PriorityClass warning in MediaEncoder [PR #16872], by @psavarmattas
* Update issue template version to 10.11.9 [PR #16897], by @theguymadmax
* Add support for filtering playlists by parentId [PR #16893], by @Shadowghost
* Fix Merge Conflict Labeler [PR #16892], by @Bond-009
* Add CI format check [PR #15250], by @jakobkukla
* Reorder Migrations and fix failing migration [PR #16861], by @JPVenson
* Add support for filtering boxsets by parentId [PR #16882], by @Shadowghost
* Modernize version display in UI [PR #16862], by @JPVenson
* Fix integrated provider images [PR #16855], by @Shadowghost
* Use --batch --yes for installing jellyfin keyring in devcontainer [PR #16878], by @IDisposable
* Embed external subtitles into MKV when transcoding [PR #16448], by @LTe
* fix: write livetv recording NFO dateadded as UTC [PR #16863], by @tayfun-akguc
* Misc fixes [PR #16837], by @Shadowghost
* fix: add null check for non-existent program in GetProgram [PR #16858], by @BrunoSync
* Fix CA1819 warnings in ChannelFeatures by using IReadOnlyList [PR #16853], by @jtvhd6
* Set max rating for splashscreen to 13 [PR #16852], by @theguymadmax
* New filters for audio and subtitle languages [PR #9787], by @TheMelmacian
* Implement similarity providers [PR #15970], by @Shadowghost
* Add Accept-Language header support and cleanup translations [PR #16488], by @Shadowghost
* Update log for user session related concurrency update fails [PR #16835], by @JPVenson
* return music artists from person endpoints [PR #16721], by @dkanada
* Reference correct .NET version in README [PR #16831], by @Bond-009
* consolidate OpenAPI categories and deprecate startup routes [PR #16757], by @dkanada
* Safeguard against invalid GUIDs [PR #16813], by @Shadowghost
* Use SortName when sorting by name [PR #16804], by @Shadowghost
* Suppress CA2213 false positive on ApplicationHost._pluginManager (#2149) [PR #16792], by @Crystora
* Print warning on invalid Subnets in Network/Proxy configuration [PR #16793], by @Shadowghost
* Add videoRotation profile condition [PR #16803], by @nyanmisaka
* Fix artist duplicates [PR #16807], by @Shadowghost
* IOException with STRM HTTP URLs [PR #16290], by @benbenmoss
* Fix Segment Provider Configuration [PR #16798], by @Shadowghost
* Fix CA1051 and CA1815 warnings, Change public fields to auto properties [PR #14847], by @tjwalkr3
* Add OriginalLanguage as option to PreferredAudioLanguage [PR #12579], by @Lampan-git
* Switch to new version scheme [PR #16758], by @Shadowghost
* fix person type exclusion in api response [PR #16784], by @dkanada
* Fix MusicBrainz test. [PR #16789], by @IDisposable
* Parse provider IDs from season and episode folder/file names [PR #16472], by @IDisposable
* Fix Canadian rating and fallback to unrated if we have a CountryCode but no matching rating [PR #16328], by @Shadowghost
* Fix live stream consumer leak on negative PositionTicks [PR #16321], by @WizardOfYendor1
* Add startup mode to migrate or seed the database on cmd [PR #16319], by @JPVenson
* Remove DigitalOcean from sponsors section [PR #16788], by @theguymadmax
* Ignore season directories with no video for TV Shows [PR #16611], by @LmanTW
* Fix #16308: Community ratings not updating after changing .nfo file. [PR #16466], by @PERSONALPANCHIWIRIS
* Fix unique people response for query if no item ID is supplied [PR #16783], by @Shadowghost
* Fix subtitle save path [PR #16779], by @Shadowghost
* Move MusicBrainz Query client to plugin instance [PR #16780], by @Shadowghost
* Fix UserManager after EFcore refactor (backport #15368) [PR #16782], by @JPVenson
* Add the filename to exceptions in DeserializeFromFile() [PR #16246], by @lcorbasson
* Add different Slovak and Czech translation of Season for parsing [PR #16646], by @Biosias
* Remove unnecessary ToList calls in TrickplayManager [PR #16322], by @poytiis
* Fix rewatch query [PR #16778], by @Shadowghost
* Speed-up LatestItems for Music [PR #16756], by @Shadowghost
* Guard against null-overwrite of saved audio/subtitle track selections [PR #16769], by @llaforest
* Fix use of thread-unsafe List<T>.Sort() [PR #16777], by @gabeluci
* Keep legacy authorization enabled [PR #16754], by @nielsvanvelzen
* Fix dummy chapter handling for videos with a single chapter or short duration. [PR #16695], by @ExpctING
* Honor episode NFO season during metadata merge [PR #16702], by @itz4blitz
* Fix keyframe duration overshoot breaking playback [PR #16704], by @dyld-w
* Implement ignore rule caching [PR #16166], by @Shadowghost
* Fix Playlist and Boxset query, save and count performance [PR #16761], by @Shadowghost
* fix person TotalRecordCount when limit is applied [PR #16616], by @dkanada
* Fix triple digit episode number handling [PR #16475], by @Shadowghost
* Fix FFProbeVideoInfo downloading subtitles without considering internal streams [PR #16747], by @MBR-0001
* Query Performance Improvements [PR #16062], by @Shadowghost
* feat/audiobook_chapters [PR #16518], by @sevenrats
* Avoid SSA to ASS conversion and loss of styles [PR #16744], by @nyanmisaka
* fix: use symmetric 15s default for skip forward/backward lengths [PR #16739], by @tcsenpai
* hide HLS controllers and deprecate unused endpoints [PR #16715], by @dkanada
* Fix IPv6 prefixes not recognized as proxy [PR #16672], by @dwandw
* improve openapi endpoint categorization [PR #16698], by @dkanada
* Fix watched status resetting on re-watch [PR #15762], by @MSalman5230
* Upgrade to xunit v3 [PR #16666], by @Shadowghost
* fix: add image/jpg to MIME type extension lookup [PR #16658], by @jskoetsier
* Remove all JF contributors from Emby list [PR #16694], by @Bond-009
* Skip libraries without enabled subtitle providers in SubtitleScheduledTask [PR #16649], by @MBR-0001
* Include item path in provider error log messages [PR #16667], by @johnpc
* Enable jellyfin.db customized path [PR #15355], by @twsouthwick
* Update to Jellyfin.XmlTv 10.12.0-pre1 [PR #16659], by @Bond-009
* Set XmlTvProgram.IsLive [PR #8890], by @SenorSmartyPants
* Move rename command permission check to script [PR #11231], by @felix920506
* Added Tanzania countries.json [PR #14406], by @ewkonzo
* Don't allow library name with leading or trailing space [PR #13491], by @gnattu
* fix: retain subtitles spanning HLS segment boundaries [PR #16594], by @LiHRaM
* chore(ci): Add permissions grant [PR #13443], by @jsoref
* Fix artist metadata not being fetched on initial library scan [PR #16606], by @theguymadmax
* Fix in-process restart [PR #16482], by @Shadowghost
* add NameStartsWith and NameLessThan filters to Person search [PR #16619], by @dkanada
* Respect EnableSubtitleExtraction setting in subtitle delivery [PR #16380], by @LTe
* Fix language display for ISO 639-2-only codes (e.g. mul, und, mis, zxx) [PR #16567], by @shocklateboy92
* Fix HDR tonemapping for BDMV content [PR #16609], by @ddemarco5
* Fix FolderStorageInfo to show parent filesystem [PR #16456], by @joshuaboniface
* Don't spam debug log with items without rating [PR #16342], by @Bond-009
* Backport security fixes [PR #16577], by @Bond-009
* Update issue template version to 10.11.8 [PR #16573], by @theguymadmax
* Fix BoxSet parentId being ignored in item queries [PR #16490], by @theguymadmax
* Reverse check for track changed [PR #16501], by @bilbofroggins
* Add AlbumNormalizationGain field to BaseItemDto [PR #14745], by @HeroBrine1st
* add StartIndex and ParentId to person search [PR #16397], by @dkanada
* edit openapi files in place with sed [PR #16569], by @dkanada
* fix invalid workflow on openapi report job [PR #16561], by @dkanada
* Fix parental ratings not working on music albums [PR #16553], by @theguymadmax
* Fix UDP Auto-Discovery returning IPv6 for cross-subnet IPv4 requests [PR #15902], by @ZeusCraft10
* fix openapi report and publish workflows [PR #16556], by @dkanada
* Update issue template version to 10.11.7 [PR #16530], by @theguymadmax
* Add callback for segment data pruning to IMediaSegmentProvider [PR #16419], by @Shadowghost
* remove nested directory for openapi workflows [PR #16524], by @dkanada
* Cleanup trickplay cache dir on failure [PR #16365], by @Shadowghost
* Only set IsAvc for video streams [PR #16507], by @Bond-009
* split openapi workflows between pull request and merge [PR #16463], by @dkanada
* recognize underscore and dot separators for multi-version grouping [PR #16465], by @upscaylman
* fix: cap GetVideoBitrateParamValue at 400 Mbps [PR #16467], by @scheilch
* Add ignore patterns for Hungarian sample files [PR #16238], by @furdiburd
* More robust date handling in Library DB migration [PR #16474], by @Shadowghost
* Fix attachment extraction of files without video or audio stream [PR #16312], by @Shadowghost
* Add spec-compliant dvh1 HLS variant for Dolby Vision Profile 5 [PR #16362], by @NoFear0411
* Fix filename truncation when bracketed tags appear mid-filename [PR #16222], by @tyage
* fix crashes on devices that don't support ipv6 [PR #15841], by @JanzenJohn
* Fix int32 overflow in QSV rate-control parameter computation [PR #16376], by @scheilch
* Recognize ".m4b", ".m4a", ".aac", ".flac", ".mp3", and ".opus" as an audio-book formats [PR #15377], by @lousando
* include external IDs and URLs for book providers [PR #15593], by @dkanada
* Fix remote image language priority to prefer English over no-language [PR #16368], by @redinsch
* Respect library country code for parental ratings [PR #16388], by @theguymadmax
* Use generic Enum overloads to resolve CA2263 warnings [PR #16395], by @jaxx2104
* Return BadRequest when an invalid set of filters is given [PR #16398], by @Bond-009
* Fix ItemValues Type checks [PR #16160], by @Shadowghost
* Add missing ProducesResponseType(401) to QuickConnectController.InitiateQuickConnect [PR #16331], by @JuanCalderon-17
* Fix near-1:1 SAR values falsely flagged as anamorphic [PR #16318], by @NoFear0411
* Use artist images for music library thumbnail [PR #16240], by @theguymadmax
* AIFF support: add .aifc as audio file type, remove .aiff as image file type [PR #16274], by @ghost
* Update JetBrains logo link in README.md [PR #16323], by @anthonylavado
* Revise note on hosting web client for development [PR #16281], by @JPVenson
* Fix malformed query string in StreamInfo.ToUrl() causing 500 error via proxies [PR #16255], by @cosu
* Upgrade Swashbuckle to v10 [PR #16256], by @Shadowghost
* Mitigate pull_request_target privilege escalation [PR #16263], by @andrewrabert
* Fix episodes appearing in Season Unknown incorrectly and prevent unnecessary virtual season creation [PR #16236], by @theguymadmax
* TmdbSeriesProvider: Set ProductionYear field [PR #16144], by @DerMaddis
* Add moveToTop option to IPlaylistManager.AddItemToPlaylistAsync [PR #15138], by @kevgrig
* Fix: Add 'Kairon; IRSE!' to artist whitelist [PR #14709], by @loop95
* Fix container and updated [PR #16202], by @JPVenson
* Trim names and roles for people [PR #16181], by @theguymadmax
* Skip validation for empty landing preferences [PR #16178], by @theguymadmax
* Add curly brace and parentheses support for parsing attribute values [PR #14927], by @nileshp87
* Fix TMDB language handling: support full ISO 639-1 + ISO 3166-1 codes (e.g. zh-CN, zh-TW) [PR #16151], by @Daydreamer-riri
* Fix: Resolve CA1849 synchronous IO in EpubImageProvider [PR #16124], by @Gladtbam
* Remove some deprecated API members [PR #16110], by @nielsvanvelzen
* SessionManager: Log when playback is started [PR #15908], by @jpds
* extract local metadata from OPF and EPUB files [PR #15604], by @dkanada
* fix: prevent premature disposal of HTTP subtitle streams [PR #14809], by @lostb1t
* Update issue template version to 10.11.6 [PR #16059], by @theguymadmax
* Fix typos in XML documentation comments [PR #15997], by @vignesh1507
* Fix zh-CN subtitle language display [PR #15947], by @ZeusCraft10
* Update to .NET 10.0 [PR #15475], by @Bond-009
* Refactor HLS transcode seeking [PR #15926], by @abitofevrything
* fix: Handle unknown item types gracefully in DeserializeBaseItem [PR #15956], by @ZeusCraft10
* Add TrueHD and DTS codes string for HLS [PR #15959], by @nyanmisaka
* Fix KeyNotFoundException in CryptographyProvider when iterations parameter is missing [PR #15958], by @ZeusCraft10
* Fix API diff workflow [PR #15888], by @Shadowghost
* Optimize `StringHelper.FirstToUpper()` [PR #15916], by @stevenaw
* Upgrade Swashbuckle and fix OpenAPI spec [PR #15886], by @Shadowghost
* Fixed issue with ABI Compatability - Difference not completing [PR #15924], by @PeachesMLG
* Fix GET MetadataEditor ContentTypeOptions for mixed content [PR #15797], by @Smeagolworms4
* Add myself to CONTRIBUTORS.md [PR #15831], by @allmazz
* Fixed Multi Sort in New ActivityManager [PR #15820], by @bjorntp
* Update issue template version to 10.11.5 [PR #15798], by @theguymadmax
* Library: Async the SaveImages function [PR #15718], by @luigi311
* parse more information from book filenames [PR #15655], by @dkanada
* Optimize GetUniqueFlags<T>() [PR #15774], by @stevenaw
* Remove legacy API route middleware [PR #15669], by @nielsvanvelzen
* Proper pinning of SkiaSharp to prevent accidental updates [PR #15736], by @MarkCiliaVincenti
* avoid Take(0) when Limit == 0 [PR #14608], by @ghost
* Fix typo in CheckOrCreateMarker exception [PR #15341], by @Xinerki
* Add ability to sort and filter activity log entries [PR #15583], by @crobibero
* Locking cleaning [PR #15713], by @MarkCiliaVincenti
* Fix episodes showing up on recently added shows [PR #15433], by @theguymadmax
* Add subtitle extraction timeout configuration option [PR #15538], by @KarkaLT
* Add CPU to issue template [PR #15704], by @theguymadmax
* Remove special client behavior for API response fields [PR #15638], by @nielsvanvelzen
* Add milliseconds to default console output format [PR #15227], by @kevgrig
* Fix TV Series parsing containing only numbers. [PR #14824], by @CodyEngel
* Add support for more embedded metadata tags [PR #15437], by @allmazz
* Deprecate HasPassword property on UserDto [PR #14950], by @nielsvanvelzen
* Add version to StartupUI [PR #15246], by @JPVenson
* Add all 10.11 versions to issue template [PR #15565], by @anthonylavado
* Update Jellyfin Server version in issue template [PR #15398], by @dpieski
* Update CODEOWNERS to capture bump_version [PR #15236], by @joshuaboniface

## 10.11.11 – 2026-06-06

# :rocket: Jellyfin Server 10.11.11

We are pleased to announce the latest stable release of Jellyfin, version 10.11.11! This minor release brings several bugfixes to improve your Jellyfin experience. As always, please ensure you take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-11-11).

## Changelog (1)

### 📈 General Changes
* Add lockhelper for UserManager [PR #16944], by @JPVenson

## 10.11.10 – 2026-05-24

# :rocket: Jellyfin Server 10.11.10

We are pleased to announce the latest stable release of Jellyfin, version 10.11.10! This minor release brings several bugfixes to improve your Jellyfin experience. As always, please ensure you take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-11-10).

## Changelog (2)

### 🔒 Security
* Fix GHSA-f47c-m7gr-q92j, by @Shadowghost
* Fix GHSA-jg92-mrxq-vv75, by @Shadowghost
* Fix GHSA-wwwm-px48-fpvq, by @Shadowghost

### 📈 General Changes
* Fix stale UserData cache [PR #15048], by @theguymadmax
* Fix/user manager collation [PR #16906], by @JPVenson

## 10.11.9 – 2026-05-21

# :rocket: Jellyfin Server 10.11.9

We are pleased to announce the latest stable release of Jellyfin, version 10.11.9! This minor release brings several bugfixes to improve your Jellyfin experience. As always, please ensure you take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-11-9).

## Changelog (5)

### 📈 General Changes
* Fix rate control in av1_amf encoder [PR #16819], by @nyanmisaka
* Fix UserManager after EFcore refactor [PR #15368], by @JPVenson
* Update log for user session related concurrency update fails [PR #16845], by @JPVenson
* Allow HDR10 for VPP tonemapping [PR #16718], by @gnattu
* Use strict QSV CPB size for less powerful H.264 decoder [PR #16743], by @nyanmisaka

## 10.11.8 – 2026-04-05

# :rocket: Jellyfin Server 10.11.8

We are pleased to announce the latest stable release of Jellyfin, version 10.11.8! This minor release brings several bugfixes to improve your Jellyfin experience. As always, please ensure you take a full backup before upgrading!

**Note**: This release fixes several regressions from 10.11.7, with the goal to get people onto an updated release due to the forthcoming (t-minus 9 days) release of the GHSAs/CVEs that were fixed in 10.11.7. Please upgrade to this release as soon as you can.

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-11-8).

## Changelog (3)

### 📈 General Changes
* Handle folders without associated library in FixLibrarySubtitleDownloadLanguages [PR #16540], by @Shadowghost
* Fix subtitle saving [PR #16539], by @MBR-0001
* Fix querying media with language filters [PR #16538], by @MBR-0001

## 10.11.7 – 2026-03-31

# :rocket: Jellyfin Server 10.11.7

We are pleased to announce the latest stable release of Jellyfin, version 10.11.7! This minor release brings several bugfixes to improve your Jellyfin experience. As always, please ensure you take a full backup before upgrading!

**WARNING**: This release contains several **extremely important security fixes**. These vulnerabilities will be disclosed in **14 days** as per our security policy. Users of **all versions prior to 10.11.7 are advised to upgrade immediately**.

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-11-7).

## Changelog (29)

### :lock: Security
* Fix for GHSA-j2hf-x4q5-47j3, by @Shadowghost 
* Fix for GHSA-8fw7-f233-ffr8, by @Shadowghost 
* Fix for GHSA-v2jv-54xj-h76w, by @Shadowghost 
* Fix for GHSA-jh22-fw8w-2v9x, by @Shadowghost 

### 📈 General Changes
* Fix CA1810 build error [PR #16522], by @Bond-009
* Fix Null was not checked before using the H264 profile [PR #16519], by @nyanmisaka
* Remove -copyts and add -flush_packets 1 to subtitle extraction [PR #16440], by @Molier
* Fix lint issue [PR #16514], by @theguymadmax
* Fix nullref ex in font handling [PR #16369], by @Bond-009
* Fix restore backup metadata location [PR #16425], by @theguymadmax
* Fix NFO saver using wrong provider ID for collectionnumber [PR #16449], by @theguymadmax
* Fix readrate options in FFmpeg 8.1 [PR #16423], by @nyanmisaka
* Apply analyzeduration and probesize for subtitle streams to improve codec parameter detection [PR #16293], by @IceStormNG
* Fix filter detection in FFmpeg 8.1 [PR #16392], by @nyanmisaka
* Fix subtitle extraction caching empty files [PR #16257], by @lowbit
* Fix hls segment length adjustment for remuxed content [PR #16341], by @crimsonspecter
* Fix broken library subtitle download settings [PR #16204], by @MBR-0001
* Checkpoint WAL before moving library.db in migration [PR #16253], by @theguymadmax
* Fix nullref in Season.GetEpisodes when the season is detached from a series [PR #16150], by @dfederm
* Reattach user data after item removal during library scan [PR #16227], by @dfederm
* Deduplicate provider IDs during MigrateLibraryDb migration [PR #16226], by @dfederm
* Skip image checks for empty folders [PR #16231], by @theguymadmax
* Fix TMDB image URLs missing size parameter [PR #16116], by @saltpi
* Fix random sort returning duplicate items [PR #16098], by @theguymadmax
* Fix SessionInfoWebSocketListener not using SessionInfoDto [PR #16109], by @nielsvanvelzen
* Fix HLS playlist generation for transcodes with fractional framerate [PR #16053], by @IceStormNG
* Rehydrate cached UserData after reattachment [PR #16071], by @MarcoCoreDuo
* Fix TMDB crew department mapping [PR #16066], by @theguymadmax
* Revert hidden directory ignore pattern [PR #16077], by @theguymadmax

## 10.11.6 – 2026-01-19

# :rocket: Jellyfin Server 10.11.6

We are pleased to announce the latest stable release of Jellyfin, version 10.11.6! This minor release brings several bugfixes to improve your Jellyfin experience. As always, please ensure you take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-11-6).

## Changelog (20)

### 📈 General Changes
* Prioritize better matches on search [PR #15983], by @Shadowghost
* Fix artist display order [PR #15816], by @theguymadmax
* Restore weekly refresh for library folder images [PR #16046], by @theguymadmax
* Be more strict about PersonType assignment [PR #15872], by @Shadowghost
* Fix birthplace not saving correctly [PR #16020], by @theguymadmax
* Trim music artist names [PR #15808], by @theguymadmax
* Add mblink creation logic to library update endpoint. [PR #15965], by @Collin-Swish
* Fix watched state not kept on Media replace/rename [PR #15899], by @MarcoCoreDuo
* Skip hidden directories and .ignore paths in library monitoring [PR #16029], by @theguymadmax
* Revert "always sort season by index number" [PR #15950], by @theguymadmax
* Fix crash when plugin repository has an invalid URL [PR #15961], by @theguymadmax
* Fix tag inheritance for Continue Watching queries [PR #15931], by @theguymadmax
* Fix playlist item de-duplication [PR #15858], by @Collin-Swish
* Prefer US rating on fallback [PR #15793], by @Shadowghost
* Fix missing H.264 and AV1 SDR fallbacks in HLS playlist [PR #15833], by @nyanmisaka
* add CultureDto cache [PR #15826], by @cvium
* Fix the use of HWA in unsupported H.264 Hi422P/Hi444PP [PR #15819], by @nyanmisaka
* Enforce more strict webm check [PR #15807], by @gnattu
* Fix video lacking SAR and DAR are marked as anamorphic [PR #15834], by @nyanmisaka
* Use hvc1 codectag for Dolby Vision 8.4 [PR #15835], by @gnattu

## 10.11.5 – 2025-12-15

# :rocket: Jellyfin Server 10.11.5

We are pleased to announce the latest stable release of Jellyfin, version 10.11.5! This minor release brings several bugfixes to improve your Jellyfin experience. As always, please ensure you take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-11-5).

## Changelog (17)

### 📈 General Changes
* Fix unnecessary database JOINs in ApplyNavigations [PR #15666], by @andrewrabert
* Skip invalid ignore rules [PR #15746], by @Shadowghost
* Fix backdrop images being deleted when stored with media [PR #15766], by @theguymadmax
* Fix NullReferenceException in ApplyOrder method [PR #15768], by @theguymadmax
* Fix AV1 decoding hang regression on RK3588 [PR #15776], by @nyanmisaka
* Fix collections display order [PR #15767], by @theguymadmax
* Fix parental rating filtering with sub-scores [PR #15786], by @theguymadmax
* Fix case sensitivity edge case [PR #15752], by @Collin-Swish
* Fix trickplay images using wrong item on alternate versions [PR #15757], by @theguymadmax
* Fix blocking in async context in LimitedConcurrencyLibraryScheduler [PR #15662], by @SapientGuardian
* Use original name for MusicAritist matching [PR #15689], by @gnattu
* Backport dependencies [PR #15723], by @Shadowghost
* Fix symlinked file size [PR #15681], by @ivanjx
* Fix ItemAdded event triggering when updating metadata [PR #15680], by @theguymadmax
* Fix: Add .ts fallback for video streams to prevent crash [PR #15690], by @martenumberto
* Fix stack overflow during scan (#15000) [PR #15698], by @myzhysz
* Fix the empty output of trickplay on RK3576 [PR #15670], by @nyanmisaka

## 10.11.4 – 2025-12-01

# :rocket: Jellyfin Server 10.11.4

We are pleased to announce the latest stable release of Jellyfin, version 10.11.4! This minor release brings several bugfixes to improve your Jellyfin experience. As always, please ensure you take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-11-4).

## Changelog (10)

### 📈 General Changes
* Fix ResolveLinkTarget crashing on exFAT drives [PR #15568], by @theguymadmax
* Cache OpenApi document generation [PR #15672], by @crobibero
* Revert "Localization/iso6392.txt: change pob and pop" [PR #15555], by @MBR-0001
* Add hidden file check in BdInfoDirectoryInfo.cs. [PR #15582], by @QuintonQu
* Fix isMovie filter logic [PR #15594], by @theguymadmax
* Fix locked fields not saving [PR #15564], by @theguymadmax
* Save item to database before providers run to prevent FK errors [PR #15563], by @theguymadmax
* Prevent copying HDR streams when only SDR is supported [PR #15556], by @gnattu
* Fix NullReferenceException in filesystem path comparison [PR #15548], by @theguymadmax
* Restrict first video frame probing to file protocol [PR #15557], by @gnattu

## 10.11.3 – 2025-11-16

# :rocket: Jellyfin Server 10.11.3

We are pleased to announce the latest stable release of Jellyfin, version 10.11.3! This minor release brings several bugfixes to improve your Jellyfin experience. As always, please ensure you take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-11-3).

## Changelog (25)

### 📈 General Changes
* Fix series DateLastMediaAdded not updating when new episodes are added [PR #15472], by @theguymadmax
* Fix movie titles using folder name when NFO saver is enabled [PR #15529], by @theguymadmax
* Fix tmdbid not detected in single movie folder [PR #14955], by @theguymadmax
* Fix font extraction for certain transcoding settings [PR #15502], by @Iksas
* Fix playlist DateCreated and DateLastMediaAdded not being set [PR #15508], by @theguymadmax
* Add 1 minute tolerance for NFO change detection [PR #15514], by @theguymadmax
* Remove InheritedTags and update tag filtering logic [PR #15493], by @theguymadmax
* Fix .ignore handling for directories [PR #15501], by @theguymadmax
* Fix gitignore-style not working properly on windows. [PR #15487], by @CBPJ
* Improve season folder parsing [PR #15404], by @theguymadmax
* Don't error out when searching for marker files fails [PR #15466], by @Bond-009
* Fix NullReferenceException in GetPathProtocol when path is null [PR #15462], by @theguymadmax
* Resolve symlinks for static media source infos [PR #15263], by @revam
* Check if target exists before trying to follow it [PR #15468], by @Bond-009
* Fix collection grouping in mixed libraries [PR #15373], by @theguymadmax
* Fix AncestorIds not migrating [PR #15446], by @theguymadmax
* Fix System.NullReferenceException when people's role is null (10.11.z) [PR #15441], by @IceStormNG
* Invalidate parent folder's cache on deletion/creation [PR #15423], by @theguymadmax
* Fix name filters to use only SortName [PR #15381], by @theguymadmax
* Don't enforce a minimum amount of free space for the tmp and log dirs [PR #15390], by @Bond-009
* Fixed missing sort argument [PR #15413], by @JPVenson
* Fix item count display for collapsed items [PR #15380], by @theguymadmax
* Update branding in Swagger page [PR #15422], by @nielsvanvelzen
* Fix search terms using diacritics [PR #15435], by @theguymadmax
* feat(sqlite): add timeout config [PR #15369], by @evanreichard

## 10.11.2 – 2025-11-03

# :rocket: Jellyfin Server 10.11.2

We are pleased to announce the latest stable release of Jellyfin, version 10.11.2! This minor release brings several bugfixes to improve your Jellyfin experience. As always, please ensure you take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-11-2).

## Changelog (6)

### 🔒 Security
* Update password reset to always return the same response structure [PR #15254], by @thornbill
### 📈 General Changes
* Fix legacy migration file checks [PR #15322], by @crobibero
* Update file size when refreshing metadata [PR #15325], by @vinnyspb
* Skip too large extracted season numbers [PR #15326], by @Shadowghost
* fix: in optimistic locking, key off table is locked [PR #15328], by @evanreichard
* Ignore initial delay in audio-only containers [PR #15247], by @nyanmisaka

## 10.11.1 – 2025-10-27

# :rocket: Jellyfin Server 10.11.1

We are pleased to announce the latest stable release of Jellyfin, version 10.11.1!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-11-1).

## Changelog (26)

### 📈 General Changes
* Improve symlink handling [PR #15209], by @Shadowghost
* Fix pagination and sorting for folders [PR #15187], by @Shadowghost
* Update dependency z440.atl.core to 7.6.0 [PR #15225], by @Bond-009
* Add season number fallback for OMDB and TMDB plugins [PR #15113], by @ivanjx
* Skip invalid database migration [PR #15212], by @crobibero
* Skip directory entry when restoring from backup [PR #15196], by @crobibero
* Skip extracted files in migration if bad timestamp or no access [PR #15220], by @JJBlue
* Normalize paths in database queries [PR #15217], by @theguymadmax
* Only save chapters that are within the runtime of the video file [PR #15176], by @CeruleanRed
* Filter plugins by id instead of name [PR #15197], by @crobibero
* Play selected song first with instant mix [PR #15133], by @theguymadmax
* Fix Has(Imdb/Tmdb/Tvdb)Id checks [PR #15126], by @MBR-0001
* Skip extracted files in migration if bad timestamp or no access [PR #15112], by @Shadowghost
* Clean up BackupService [PR #15170], by @crobibero
* Initialize transcode marker during startup [PR #15194], by @crobibero
* Make priority class setting more robust [PR #15177], by @gnattu
* Lower required tmp dir size to 512MiB [PR #15098], by @Bond-009
* Fix XmlOutputFormatter [PR #15164], by @crobibero
* Make season paths case-insensitive [PR #15102], by @theguymadmax
* Fix LiveTV images not saving to database [PR #15083], by @theguymadmax
* Speed-up trickplay migration [PR #15054], by @Shadowghost
* Optimize WhereReferencedItemMultipleTypes filtering [PR #15087], by @theguymadmax
* Fix videos with cropping metadata are probed as anamorphic [PR #15144], by @nyanmisaka
* Reject stream copy of HDR10+ video if the client does not support HDR10 [PR #15072], by @nyanmisaka
* Log the message more clear when network manager is not ready [PR #15055], by @gnattu
* Skip invalid keyframe cache data [PR #15032], by @Shadowghost

## 10.11.0 – 2025-10-20

# :rocket: Jellyfin Server 10.11.0

We are pleased to announce the latest stable release of Jellyfin, version 10.11.0!

This major release brings many new features, improvements, and bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

**WARNING**: There are **very important release notes** to review before upgrading! Please find all the details in [our blog post on the release](https://jellyfin.org/posts/jellyfin-release-10.11.0).

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-11-0).

## Changelog (396)

### 🌟 Highlights
* Add Full system backup feature [PR #13945], by @JPVenson
* Add .gitignore style ignoring [PR #13906], by @Shadowghost
* Add Api and startup check for sufficient storage capacity [PR #13888], by @JPVenson
* Added Setup overlay app to communicate status of startup [PR #12880], by @JPVenson
* Remove the ability to auto port forward [PR #13222], by @Bond-009
* Refactor library.db into jellyfin.db and EFCore [PR #12798], by @JPVenson
### 🏗️  Enhancements
* add xmbc nfo uniqueid type norminalisation [PR #14965], by @KGT1
* Fix CA1051 warning, Change public field to auto-property [PR #14827], by @tjwalkr3
* Offload 1080p+ subtitle scaling to RKRGA [PR #14179], by @nyanmisaka
* Enable OpenCL deinterlacer for AMF on Windows when available [PR #14144], by @nyanmisaka
* Use VBR and MBBRC in QSV encoders for better quality [PR #14079], by @nyanmisaka
* Fix the transparency issue of ASS subtitle rendering in HWA [PR #14024], by @nyanmisaka
* Add DoVi Profile 5 support for Rockchip RKMPP [PR #13911], by @nyanmisaka
* Add ServerName to startup configuration [PR #13901], by @thornbill
* Add missing public properties to SystemInfo response [PR #13822], by @thornbill
* Reduce allocations, simplifed code, faster implementation, included tests - StreamInfo.ToUrl [PR #9369], by @Shadowghost
* Fix only returning one item from /Item/Latest api. [PR #12492], by @scampower3
### 📈 General Changes
* Validate encoder path when saving [PR #14996], by @crobibero
* Handle es-419 in TMDb [PR #14946], by @Lampan-git
* Use TryAdd instead of Add when registering custom OpenAPI responses [PR #14997], by @crobibero
* Fix contributing artist query [PR #14991], by @theguymadmax
* Fix exception when saving user data to NFO files [PR #14993], by @theguymadmax
* Remove chapters on file change [PR #14984], by @Shadowghost
* Fix LUFS detection deadlock per issue #13697 [PR #14960], by @karm235
* Prevent PlaylistsFolder deletion during library removal [PR #14978], by @theguymadmax
* Skip creating Person entities for Artist and AlbumArtist types [PR #14971], by @theguymadmax
* Fix artist external Url [PR #14969], by @theguymadmax
* apply sort on ItemValue query [PR #14976], by @JPVenson
* Fix collections folder duplication [PR #14925], by @theguymadmax
* Improve performance on people query [PR #14963], by @theguymadmax
* Clean up missing image references [PR #14962], by @theguymadmax
* Truncate password reset file on open for writing [PR #14948], by @Bond-009
* Handle xx as TMDb no language for backdrops [PR #14941], by @crobibero
* Fix libraries not loading after startup wizard, Change AddVirtualFolder to validate folders [PR #14942], by @tjwalkr3
* Limit decoder thread count on AMD AMF to save VRAM [PR #14943], by @nyanmisaka
* fix: get total count after grouping [PR #14931], by @lostb1t
* Fix mka-style tagging key [PR #14936], by @gnattu
* Readd wildcard search [PR #14934], by @JPVenson
* Fix BoxSet sorting [PR #14919], by @theguymadmax
* Add check for processing recursive data structures [PR #14897], by @JPVenson
* Fix parental ratings [PR #14909], by @theguymadmax
* Add tag filtering and random sorting to GetSimilarItems [PR #14918], by @theguymadmax
* Add explicit reference check to migration [PR #14887], by @JPVenson
* Fix AddProperParentChildRelationBaseItemWithCascade migration deleting all items [PR #14890], by @nielsvanvelzen
* Only include custom code analysis for debug builds [PR #14883], by @crobibero
* Fixing the UFID field value giving a warning and not being correctly processed [PR #14851], by @teblam
* Restore NFO/import ordering by using ListOrder instead of SortOrder [PR #14873], by @theguymadmax
* Expose ExtractAllExtractableSubtitles [PR #14876], by @Shadowghost
* Add Jellyfin.CodeAnalysis project to abi diff [PR #14875], by @JPVenson
* Fix people deduplication lookup [PR #14864], by @JPVenson
* Fixes FK on unconnected base items [PR #14863], by @JPVenson
* Rollback to last working skiasharp version [PR #14862], by @gnattu
* Add Check for ItemValues [PR #14860], by @JPVenson
* Apply filter server side [PR #14856], by @JPVenson
* Fix people SortOrder [PR #14852], by @theguymadmax
* Include ListOrder on Import [PR #14854], by @JPVenson
* Add People Dedup and multiple progress fixes [PR #14848], by @JPVenson
* Fix collections one-off [PR #14814], by @theguymadmax
* Fix ordering where exists [PR #14843], by @JPVenson
* Add schema to 503 headers [PR #14840], by @crobibero
* Fix Image loading [PR #14842], by @JPVenson
* Fix groupings not applied [PR #14826], by @JPVenson
* fix: add back missing behavior for HasAnyProviderId [PR #14831], by @revam
* Attach before updating/deleting to avoid DbUpdateConcurrencyException [PR #14746], by @evan314159
* Skip removed images when updating images [PR #14823], by @Shadowghost
* Revert limit hack [PR #14820], by @JPVenson
* Make migration handle parent cleanup [PR #14817], by @JPVenson
* Fix root folder not being saved to Db if nessesary [PR #14819], by @JPVenson
* Fix playlist move from smaller to larger index [PR #14794], by @kgarner7
* #14751 Only migrate providerids that match assumption [PR #14810], by @JPVenson
* Temp/options and isplayed [PR #14795], by @JPVenson
* Fix sync disposal of async-created IAsyncDisposable objects [PR #14755], by @evan314159
* Add ec3 to audio file extensions [PR #14799], by @Shadowghost
* Reenable common PRAGMA setters [PR #14791], by @JPVenson
* Fix IsPlayed [PR #14786], by @crobibero
* Allow non-admin users to subscribe to their own Sessions [PR #13767], by @KGT1
* Fix duplicate media entries when sorting [PR #14404], by @theguymadmax
* Avoid constant arrays as arguments [PR #14784], by @Bond-009
* Various cleanups [PR #14785], by @Bond-009
* Fix several Stackoverflows [PR #14783], by @JPVenson
* Add fast path to check for empty ignore files [PR #14782], by @Bond-009
* Never replace BoxSet LinkedChildren on update [PR #14723], by @Shadowghost
* Change Spanish variants order in iso6392.txt to make Castillian the "default" version [PR #14777], by @a-collado
* Improve optimistic locking behavior [PR #14779], by @JPVenson
* Reenable pooling [PR #14778], by @JPVenson
* Add 1-second tolerance to resume playback completion check [PR #14774], by @theguymadmax
* Sort trailers before teasers [PR #14715], by @theguymadmax
* Seal Emby.Naming.Video.StackResolver.StackMetadata to silence a compiler warning [PR #14764], by @varoonp123
* Don't use ffprobe frame options on audio probe [PR #14773], by @Shadowghost
* Additional debug logging for SQLite connections [PR #14753], by @evan314159
* Skip non-media folders in movie resolver [PR #14724], by @theguymadmax
* Preserve 3D format on metadata refresh [PR #14742], by @theguymadmax
* Refactor Display preference manager [PR #14056], by @JPVenson
* Fix latest items grouping by collection type [PR #14736], by @theguymadmax
* Add more robust error handling for AudioNormalizationTask [PR #14728], by @Bond-009
* AudioNormalizationTask db progress saving [PR #14550], by @shanepowell
* Update .Net Core to .Net [PR #14718], by @ShalokShalom
* Correct Album Artists merge logic [PR #14655], by @evan314159
* fix ProbeProvider.HasChanged: if file date OR file size changed [PR #14674], by @evan314159
* Normalizer cleanup [PR #14711], by @IDisposable
* Use existing userData when filtering by IsPlayed [PR #14703], by @crobibero
* Fix GetSimilarItems to exclude the searched for item Id [PR #14686], by @evan314159
* Run background ffmpeg tasks as ProcessPriorityClass.BelowNormal [PR #14651], by @evan314159
* Delay initialization of singleton services during migration CoreInitialisation stage [PR #14653], by @evan314159
* Fix AlbumArtistIds filter to use correct ItemValueType [PR #14641], by @evan314159
* Change Spanish; Latin language code according to BCP 47 specification [PR #14639], by @a-collado
* Fix anamorphic video detection (#14640) [PR #14648], by @GeneMarks
* Fix GetBaseItemDto to return related item counts via SQL count [PR #14634], by @crobibero
* Refactor query from EXISTS to JOIN to avoid API timeouts with large libraries [PR #14557], by @evan314159
* Always save images [PR #14600], by @Shadowghost
* Revert "Merge pull request #13604 from Jxiced/master" [PR #14593], by @Bond-009
* Enhanced HTTP Range request support for. strm file [PR #14021], by @sususu98
* Extract subtitles of MKS aux files if they're extractable. [PR #12718], by @IceStormNG
* Further refinement of BCP 47 language labeling support [PR #14410], by @dyphire
* Improve extra rule resolution and file handling [PR #14540], by @TokerX
* Prevent whitespaces in username during wizard setup [PR #13604], by @Jxiced
* Don't fail image saving on missing BaseItem [PR #14567], by @Shadowghost
* Add extra movflags to fMP4 to take initial audio delay into account [PR #14553], by @nyanmisaka
* Add fallback for keyframe-only trickplay extraction [PR #14467], by @jkhsjdhjs
* Preserve interpunct (·) [PR #14543], by @theguymadmax
* Also migrate IsFolder [PR #14554], by @JPVenson
* fix file modification date comparisons [PR #14503], by @evan314159
* Add progress reporting to AudioNormalizationTask. [PR #14306], by @shanepowell
* Fix allow and block queries [PR #14482], by @theguymadmax
* Ignore directory if empty .ignore file is present [PR #14536], by @piyushrungta25
* Update DateLastSaved after running metadata savers [PR #14531], by @Shadowghost
* Fix trickplay extraction ffmpeg error-handling [PR #14493], by @jkhsjdhjs
* Fix issue with EncodedRecorder streams not showing up under "Active Recordings" [PR #14357], by @theshoeshiner
* Supress transaction [PR #14514], by @JPVenson
* Fix Serbian ISO 639-2 codes [PR #14476], by @theguymadmax
* Clean up and fix backup/restore [PR #14489], by @crobibero
* Use RequestHelpers.GetSession in SessionWebSocketListener [PR #14494], by @nielsvanvelzen
* improve userdata migration [PR #14488], by @JPVenson
* Delete old migrations on restore [PR #14486], by @JPVenson
* ﻿Drawing: make SkiaEncoder more robust when reading image dimensions [PR #14481], by @queukat
* Ensure UserData stays unique on delete [PR #14475], by @sundermann
* Fix refreshing the library cannot delete old attachments [PR #14461], by @nyanmisaka
* Allow loading of Database options for DB provider [PR #14466], by @JPVenson
* vob file support [PR #14471], by @Fjox
* Add SerilogExpressions reference [PR #14438], by @JPVenson
* Added advanced parallel process calculation [PR #14437], by @JPVenson
* Use IDatabaseCreator instead of relying on History repository [PR #14465], by @JPVenson
* Only save images when changed [PR #14425], by @JPVenson
* Only enable VAAPI MJPEG encoder on Intel iHD driver [PR #14433], by @nyanmisaka
* Fix PeopleHelper.AddPerson Exceptions due to bad meta-data extracts. [PR #14309], by @shanepowell
* Fix seasons random (#13224) [PR #14335], by @maxime-en
* Prefer ALBUMARTISTS to ALBUMARTIST when PreferNonstandardArtistsTag set [PR #14413], by @evan314159
* Revert invalid Portuguese translations [PR #14414], by @thornbill
* Fix compiler warning for CodeMigration.cs [PR #14390], by @gnattu
* Fix modification checks and make sure to use UTC [PR #14347], by @Shadowghost
* Fix typo in 503 response for API [PR #14377], by @arch1eOS
* Fix -fps_mode option being applied on input [PR #14379], by @nyanmisaka
* Improve cast and crew handling [PR #14370], by @theguymadmax
* Add migration to migrate disconnected UserData too [PR #14339], by @JPVenson
* Fix issue with syncplay group incorrectly playing content on creation [PR #14360], by @Mason-Weigand
* Adapt LrcLyricParser to new LrcParser version [PR #14263], by @Maxr1998
* Fix missing music genre metadata [PR #14332], by @theguymadmax
* Make keyframe extraction task cancellable [PR #14368], by @Shadowghost
* Cleanup Migration [PR #14341], by @Shadowghost
* Skip missing images when creating collages [PR #14344], by @Shadowghost
* fix(devcontainer): correct apt-packages path [PR #14235], by @spellr
* Don't check dynamic metadata removal for static HDR formats [PR #14322], by @gnattu
* Fix QSV "static surface pool size exceeded" on Windows [PR #14330], by @nyanmisaka
* Add act as a stacking option for music albums [PR #14333], by @theguymadmax
* Use dto instead of db object when returning trickplay [PR #14328], by @crobibero
* Use square root scaling for high framerate videos' bitrate requirements [PR #14314], by @gnattu
* Fix startup logger, startup health check [PR #14327], by @crobibero
* Use proper scheduler that honors the parallel task limit [PR #14281], by @JPVenson
* Always set update action when item does not exist [PR #14304], by @JPVenson
* Only remove image file if it exists [PR #14302], by @Shadowghost
* Add explicit check for placeholder ID [PR #14298], by @JPVenson
* Remove appsettings.json loading component from startup server [PR #14275], by @JPVenson
* Fix People Issues [PR #14284], by @Shadowghost
* Properly handle file access issues in some cases [PR #14272], by @Shadowghost
* Fix UserData cleanup task and queries [PR #14280], by @JPVenson
* Fix schema name on backup [PR #14269], by @JPVenson
* Fix existing media segments not being handled on scan [PR #14218], by @ThunderClapLP
* chore/typo [PR #14264], by @IDisposable
* fix(collection): Do not lock newly created collections [PR #14259], by @darioackermann
* fix(Session): don't query DB if queue hasn't changed [PR #14244], by @Skaytacium
* Feature/persistent watch data [PR #14262], by @JPVenson
* Pin Skiasharp version to 3.116.1 [PR #14255], by @gnattu
* Fix ExcludeItemId, ExcludeProviderIds and HasAnyProviderId filter [PR #14249], by @JPVenson
* Ignore null key virtual folders [PR #14253], by @JPVenson
* util forward headers on startup api [PR #14246], by @JPVenson
* Rework startup topic handling and reenable output to logging framework [PR #14243], by @JPVenson
* Use filename for single videos (non-movie/null collections) in MovieResolver [PR #14162], by @theguymadmax
* Don't attempt to do metadata removal for dovi without fallback [PR #14240], by @gnattu
* Only show log in Local network [PR #14241], by @JPVenson
* Fix search for missing metadata overriding existing metadata [PR #12908], by @scampower3
* Add year parameter to TMDB series cache key [PR #14209], by @theguymadmax
* always sort season by index number [PR #13307], by @qiqian
* Fix source directory for setup template [PR #14228], by @JPVenson
* Fix race condition in SessionManager.GetSessionInfo [PR #14131], by @moalhaddar
* Fix broken chapter image placeholders when no image is present [PR #14230], by @theguymadmax
* Update issue report.yml [PR #14099], by @felix920506
* Fix metadata not refreshing in negative UTC timezones [PR #14225], by @theguymadmax
* Fix DirectoryNotFoundException for backdrop folders in trickplay [PR #14223], by @theguymadmax
* Add support for delete from playlist call with api key [PR #14154], by @sharinganthief
* Add cache-control: no-cache to index.html if selfhosted [PR #14222], by @JPVenson
* Feature/version check in library migration [PR #14105], by @JPVenson
* Migrate all known old migrations even when not applied in migration.xml [PR #14217], by @JPVenson
* Allow custom plugin provided database providers to be loaded [PR #14171], by @JPVenson
* Add declarative backups for migrations [PR #14135], by @JPVenson
* Update XmlTv tests to use UTC date formats [PR #14163], by @telans
* Fix missing logging of connections by disallowed IPs [PR #14011], by @lf-
* Prune trickplay data on regenerate and scan [PR #14085], by @Shadowghost
* Add ExcludeItemIds filtering to UserViewBuilder.Filter [PR #14203], by @shanepowell
* Fix server not auto restarting [PR #14215], by @JPVenson
* Backup MigrationHistory as well [PR #14136], by @JPVenson
* Add multiple options for internal locking [PR #14047], by @JPVenson
* Fix unittests [PR #14202], by @shanepowell
* Localization/iso6392.txt: Correct the Portuguese entries [PR #14030], by @baka0815
* Add partition helper [PR #14039], by @JPVenson
* Round RemoteImage CommunityRating to nearest tenths when sorting [PR #13145], by @SenorSmartyPants
* Add SVG to transparent image types [PR #14160], by @theguymadmax
* Make name sorting case-insensitive [PR #14153], by @theguymadmax
* Ensure subfolders are processed in folders containing one video file [PR #14140], by @theguymadmax
* Fix collection behavior when sorting by rating or runtime [PR #14148], by @theguymadmax
* Fix ArgumentNullException when downloading season logos [PR #14141], by @theguymadmax
* Terminate at null char for audio tags [PR #14100], by @gnattu
* Fix ArgumentNullException in TmdbExternalUrlProvider [PR #14130], by @theguymadmax
* Translate query by AncestorIds correctly [PR #14094], by @allesmi
* Fix extracted data cleanup in cleanup post scan task [PR #14083], by @Shadowghost
* added different countries parental ratings [PR #14069], by @SoumyadipAuddy
* Fix Blu-ray metadata: preserve external streams and language metadata [PR #14077], by @theguymadmax
* Reject invalid replaygain tag value [PR #14082], by @gnattu
* Cleanup external item data cleanup [PR #14072], by @Shadowghost
* Only consider migrations that have key set for migration.xml migration [PR #14061], by @JPVenson
* Add tests for ManagedFileSystem.MoveDirectory [PR #14065], by @Bond-009
* Fix cross filesystem dir moving [PR #14063], by @gnattu
* fix #14034 Readd Context provider on Initialise [PR #14040], by @JPVenson
* Cleanup file related code [PR #14023], by @Bond-009
* Recognize file changes and remove data on change [PR #13839], by @Shadowghost
* Add albumart as recognized filename for music artwork [PR #14048], by @theguymadmax
* Added parental ratings for Indian content [PR #14050], by @SoumyadipAuddy
* Cleanup Tasks and Validators [PR #14028], by @Shadowghost
* Add "part" as possible album prefix for stacking [PR #14022], by @harry-hart
* Fix trickplay directory path construction [PR #14036], by @theguymadmax
* Fix startup logger log file order [PR #14044], by @theguymadmax
* Add new nuget packages to abi diff [PR #14016], by @crobibero
* Fix image extractor with more strict ffmpeg requirement [PR #14013], by @gnattu
* Unified migration handling [PR #13950], by @JPVenson
* Fix distinction queries [PR #14007], by @Shadowghost
* Fix ItemValue query [PR #13939], by @JPVenson
* Don't pass through timestamp for image extractor [PR #13999], by @gnattu
* Optimize migrations [PR #13855], by @Shadowghost
* improved performance of save operations [PR #13889], by @JPVenson
* Create directory before checking for size [PR #13962], by @JPVenson
* Check for path overlaps [PR #12832], by @JPVenson
* Rework chapter management [PR #13847], by @Shadowghost
* Fix IsInMixedFolder not being set for Extras [PR #13536], by @tkloy24
* Only run merge conflict labler action on pull requests [PR #13378], by @felix920506
* Deprecate OnPlaybackXXX API operations in favor of ReportPlaybackXXX [PR #13993], by @nielsvanvelzen
* Remove 10.11.z EFcore migration warnings [PR #13972], by @ferferga
* Fix OverflowException when scanning media with a very short duration [PR #13949], by @Bond-009
* Return SyncPlay group info after creation, add GET group endpoint [PR #13935], by @nielsvanvelzen
* Add port awareness to startup server [PR #13913], by @JPVenson
* Fix SyncPlay WebSocket OpenAPI schemas [PR #13946], by @nielsvanvelzen
* Improve video resolution filtering and classification logic [PR #13332], by @theguymadmax
* Fix thumbnail extraction of mpegts videos in FFmpeg 7.1+ [PR #13942], by @nyanmisaka
* Fix Genre cleanup [PR #13916], by @Shadowghost
* Safeguard against null value trimming in tag results [PR #13908], by @Shadowghost
* Remove the hashed password from startup users response [PR #13904], by @thornbill
* Add polish age ratings [PR #13851], by @relains
* Add Genre cleanup and fix cleanup filter queries [PR #13891], by @Shadowghost
* Only reselect audio streams when user preference is respected [PR #13832], by @gnattu
* Fix negated IP addresses without subnet mask not being parsed correctly [PR #13854], by @mapret
* Fix InheritedParentalRatingSubValue not set [PR #13880], by @JPVenson
* Use Guid for parentPrimaryImageItemId [PR #13874], by @nielsvanvelzen
* Fix seeking beyond EOF again [PR #13871], by @nyanmisaka
* Translate the ISO-639-2/B codes to ISO-639-2/T. [PR #13068], by @baka0815
* Fix the migration as the new constraint now uses Value as unique key [PR #13867], by @JPVenson
* Add API support for ELRC word-based lyrics [PR #12941], by @AlexDalas
* Fix backup not written to correct directory [PR #13853], by @JPVenson
* Fix Genre type [PR #13862], by @Shadowghost
* Send Album Artist and Artist in seperate variables when doing a lyrics search [PR #13852], by @scampower3
* Fix ancestors [PR #13827], by @Shadowghost
* Fix indices and update of ItemValues [PR #13843], by @Shadowghost
* Use subdirectories to organize extracted data [PR #13838], by @Shadowghost
* Make ReadInputAtNativeFramerate configurable for M3U tuner [PR #13773], by @timminator
* Fix ArgumentNullException on playlist creation [PR #13837], by @Bond-009
* Cleanup extracted files [PR #13760], by @Shadowghost
* Only remove keyframe cache dir if it exists [PR #13834], by @Shadowghost
* Trim library names [PR #13828], by @JPVenson
* Import Keyframes into database [PR #13771], by @Shadowghost
* Improve dynamic HDR metadata handling [PR #13277], by @gnattu
* allow admin users to get Splashscreen even when it's disabled [PR #13825], by @KGT1
* Cleanup ItemFields [PR #13818], by @Shadowghost
* Preserve SplashscreenLocation when updating branding config [PR #13756], by @KGT1
* Add Dolby Vision tests for Tizen [PR #12670], by @dmitrylyzo
* Reduce Skia conversions [PR #5366], by @ferferga
* Fix Tmdb external URL generation [PR #13817], by @Shadowghost
* Explicitly set default value for enums used in API models [PR #13821], by @gnattu
* Use pattern matching for null checks [PR #13793], by @Bond-009
* Rework parental ratings [PR #12615], by @Shadowghost
* Fix playlist order [PR #13730], by @quyet-v
* Fix MoveTrickplayFiles migration [PR #13807], by @Shadowghost
* Fix StreamInfo.ToUrl [PR #13808], by @Shadowghost
* Library.db migration impovements [PR #13809], by @JPVenson
* Enable VideoToolbox AV1 decode [PR #13194], by @gnattu
* Fix cleanup of wrong table in migration [PR #13796], by @JPVenson
* feat: allow grouping shows into collections [PR #13236], by @jheuel
* Fix build and tests [PR #13790], by @crobibero
* Add profile condition to limit the number of streams [PR #13583], by @dmitrylyzo
* Fix for Issue #12142: Fix ExtraRuleResolver filtering out top level folders [PR #12170], by @mcmcelro
* Implement limiting caches [PR #13605], by @crobibero
* Improve SkiaEncoder's font handling [PR #13231], by @gnattu
* Add channel queries to series [PR #13356], by @Kevinjil
* Fix Sort by Year Bug (#12101) [PR #13733], by @jjwarrenSEP
* Fix consumer count off by one when closing a browser tab with a livestream that is transcoding [PR #13220], by @timminator
* Fix validation of VAAPI/QSV render node path [PR #13786], by @nyanmisaka
* Include UnratedType in LibraryDb migration query [PR #13783], by @theguymadmax
* Add eac3 as an audio name format [PR #13784], by @theguymadmax
* Add override for migration if library.old aready exists [PR #13779], by @JPVenson
* Extract container, video and audio compatibility checks [PR #12678], by @dmitrylyzo
* Feature/backup on migration [PR #13754], by @JPVenson
* Change the order of the iso6392.txt file [PR #13314], by @baka0815
* Fix Cleanup task not awaiting async methods [PR #13769], by @JPVenson
* [Feature] Database code refactor [PR #13589], by @JPVenson
* Add OpenAPI spec for #12880 [PR #13764], by @JPVenson
* Add ability to provide search pattern to GetFiles [PR #13691], by @NooNameR
* Include PeopleBaseItemMap in GetPeople to inlcude Role and SortOrder [PR #13616], by @Lampan-git
* Disable flaky tests [PR #13765], by @JPVenson
* Add missing singleton [PR #13761], by @Shadowghost
* Fix Invalid Item Queries [PR #13757], by @JPVenson
* Rework season folder parsing [PR #11748], by @Shadowghost
* Remove all DB data on item removal, delete internal trickplay files [PR #13753], by @Shadowghost
* Rename Islamic Republic of Pakistan to Pakistan [PR #13752], by @adiled
* 2x faster library.db migration, reduced memory pressure [PR #13749], by @ferferga
* Fix IMDb URL for People [PR #13724], by @theguymadmax
* Fix OnPlaybackStopped task erroring out when closing a browser tab with a livestream that is transcoding [PR #13226], by @timminator
* Fix subtitle selection to respect preferred language for forced subtitles [PR #13098], by @timminator
* Add fast-path to getting just the SeriesPresentationUniqueKey for NextUp [PR #13687], by @crobibero
* Add start index to /Programs/Recommended endpoint [PR #13696], by @Bond-009
* Fix subnet contains check [PR #13493], by @gnattu
* Fix build and tests [PR #13718], by @Shadowghost
* Migrate to IExternalUrlProvider [PR #13175], by @Shadowghost
* Include CleanName in LibraryDb migration query [PR #13690], by @theguymadmax
* Sort embedded collections in Nfo files [PR #9560], by @IDisposable
* Extract trickplay files into own subdirectory [PR #13406], by @Shadowghost
* Include SortName in LibraryDb migration query [PR #13675], by @te9c
* Fix possible NullReferenceException in playlist warning [PR #13643], by @l2dy
* Don't use RETURNING clause with EFCore [PR #13492], by @gnattu
* Better exception message when folders or folder items are missing [PR #13632], by @IDisposable
* Remove deprecated GetWakeOnLanInfo endpoint [PR #13606], by @nielsvanvelzen
* Revert nullability of MediaStream.IsHearingImpaired [PR #13573], by @crobibero
* Add support for reading and storing Recording MBIDs from file metadata [PR #12173], by @lyarenei
* Don't allow usernames to have leading or trailing spaces [PR #13556], by @Jxiced
* Change BaseItemEntity ChannelId to nullable Guid [PR #13553], by @crobibero
* Disallow incremental updates to JellyfinDbModelSnapshot [PR #13564], by @crobibero
* Make the JsonConverters for delimited arrays more generic [PR #13396], by @Bond-009
* Write only for query columns to EFCore db [PR #13542], by @gnattu
* Fix the issue where the external audio track always defaults. [PR #13132], by @choyakawa
* Simulate old GetItemValueNames behavior [PR #13539], by @gnattu
* Rename CreateOrUpdateItems back to CreateItems [PR #13527], by @Bond-009
* Fix Search results are case-sensitive for people [PR #13516], by @tkloy24
* Handle empty image lists gracefully in SplashscreenPostScanTask [PR #13498], by @gnattu
* Remove check-backport CI action [PR #13523], by @joshuaboniface
* Enable nullable for AuthorizationInfo [PR #13485], by @Bond-009
* Order MediaStream query by StreamIndex [PR #13506], by @gnattu
* Make StartDate/EndDate nullable [PR #13494], by @gnattu
* Fix build after backports due to EFCore change [PR #13488], by @Bond-009
* Removing CollectionFolders from cache when they are deleted on disk. [PR #13315], by @sinterdev
* Fix source typo [PR #13453], by @luzpaz
* Always await instead of directly returning Task [PR #12925], by @Bond-009
* Remove useless checks and dead code [PR #13405], by @Bond-009
* chore(ci): Let CI fail independently on each platform [PR #13446], by @jsoref
* Fix spelling [PR #13444], by @jsoref
* Fix typos [PR #13438], by @luzpaz
* Use MediaTypeNames where possible [PR #13440], by @Bond-009
* Fix various typos [PR #13436], by @luzpaz
* Fix spelling [PR #11103], by @jsoref
* improve documentation for ContainerHelper class [PR #13360], by @reuterma24
* Add ability to remove a ChannelMapping [PR #12970], by @Giermann
* Add option to disable deprecated legacy authorization options [PR #13306], by @nielsvanvelzen
* Fix .gzip handling and URL redirection for XML TV guide parsing [PR #13319], by @theguymadmax
* Prefer ApiKey over api_key in generated URL's [PR #13342], by @nielsvanvelzen
* Migrate rulesets to .editorconf [PR #13195], by @Shadowghost
* move to new System.Threading.Lock type for better performance [PR #13213], by @Ich1goSan
* Determine tv image type by extension if content-type is unavailable [PR #13076], by @theguymadmax
* Removed RemoveOldPlugins configuration flag [PR #13102], by @RealGreenDragon
* Implement TaskTriggerInfoType enum [PR #12783], by @LePips
* Move TV-PG ratings to be in line with PG rating. [PR #12867], by @Dessyreqt
* Added test for ListsingsManager.DeleteListingsProvider(). [PR #12793], by @kennethcochran
* Updated DevContainer to Bookworm Debian [PR #13037], by @JPVenson
* Fix typo in guide info endpoint comment [PR #13117], by @1hitsong
* make playlist creation private by default [PR #12853], by @dkanada
* Fix typo in LibraryOptions [PR #13097], by @nielsvanvelzen
* Fixed segment providers never presented to UI [PR #13060], by @JPVenson
* Add dotnet9 to abi compat workflow [PR #13046], by @crobibero
* Update projects to .NET 9 [PR #13023], by @Bond-009
* Add EpisodeExpression for anime file names [PR #12778], by @TonyBotongChu
* Added + in username regex validator, Test + in username, issue #10414 [PR #12819], by @SethPattee
* Auto update issue template version on new release [PR #12893], by @HadrienPatte
* Update issue template version from 10.9.11 to 10.10.0 [PR #12882], by @HadrienPatte

## 10.10.7 – 2025-04-05

# :rocket: Jellyfin Server 10.10.7

We are pleased to announce the latest stable release of Jellyfin, version 10.10.7!

This minor release brings several bugfixes and security fixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-10-7).

## Important Notes

* Configurations behind a reverse proxy that did not explicitly configure trusted proxies will not work after this release. This was never a supported configuration, so please ensure you correct your configuration before upgrading. See [the updated docs here](https://jellyfin.org/docs/general/networking/#known-proxies) for more information.

## Changelog (12)

### 🔒 Security
* Fix validation of API parameters to FFmpeg [[GHSA-2c3c-r7gp-q32m](https://github.com/jellyfin/jellyfin/security/advisories/GHSA-2c3c-r7gp-q32m)], by @Shadowghost
* Fix trusting forward headers if none are configured [[GHSA-qcmf-gmhm-rfv9](https://github.com/jellyfin/jellyfin/security/advisories/GHSA-qcmf-gmhm-rfv9)], by @JPVenson

**Note**: GHSAs will be published seven (7) days after this release.

### 📈 General Changes
* Fix regression where "Search for missing metadata" not handling cast having multiple roles [PR #13720], by @Lampan-git
* Clone fallback audio tags instead of use ATL.Track.set [PR #13694], by @gnattu
* Backport 10.11 API enum changes [PR #13835], by @nielsvanvelzen
* Support more rating formats [PR #13639], by @IDisposable
* Fix stackoverflow in MediaSourceCount [PR #12907], by @JPVenson
* Upgrade LrcParser to 2025.228.1 [PR #13659], by @congerh
* Include Role and SortOrder in MergePeople to fix "Search for missing metadata" [PR #13618], by @Lampan-git
* Delete children from cache on parent delete [PR #13601], by @Bond-009
* Fix overwrite of PremierDate with a year-only value [PR #13598], by @IDisposable
* Wait for ffmpeg to exit on Windows before we try deleting the concat file [PR #13593], by @Bond-009
* Fix 4K filtering when grouping movies into collections [PR #13594], by @theguymadmax
* Remove empty ParentIndexNumber workaround [PR #13611], by @Shadowghost
* Update dependency z440.atl.core to 6.20.0 [PR #13845], by @Shadowghost

## 10.10.6 – 2025-02-16

# :rocket: Jellyfin Server 10.10.6

We are pleased to announce the latest stable release of Jellyfin, version 10.10.6!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-10-6).

## Release Notes

* Crashes on Apple silicon [Issue #13379] should be fixed by the bump to .NET framework version 8.0.13 in this release

## Changelog (12)

### 📈 General Changes
* Update dependency z440.atl.core to 6.16.0 [PR #13526], by @crobibero
* Fix subnet contains check [PR #13489], by @gnattu
* Fix image encoding concurrency limit [PR #13532], by @gnattu
* Fix SchedulesDirect image prefetching [PR #13469], by @Shadowghost
* Skip allowed tags check for parents of an item [PR #12721], by @elfalem
* Fix LiveTV Guide Backdrop image not updating [PR #13504], by @IDisposable
* Correctly handle audio number tag fallbacks [PR #13490], by @gnattu
* Allow api key to subscribe to admin websockets [PR #13499], by @crobibero
* Fix rating mistake in us.csv [PR #13487], by @Bond-009
* Fall back to calculating mime type from path when needed [PR #13439], by @Bond-009
* Fix interface ordering again [PR #13448], by @Shadowghost
* Fixed Websocket not locking state correctly [PR #13459], by @JPVenson

## 10.10.5 – 2025-01-25

# :rocket: Jellyfin Server 10.10.5

We are pleased to announce the latest stable release of Jellyfin, version 10.10.5!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-10-5).

## Changelog (9)

### 📈 General Changes
* Add check to prevent downgrade from future EFCore refactor [PR #13103], by @JPVenson
* Open files with FileShare.Read for BlurHash calculations [PR #13425], by @Bond-009
* Don't select audio stream and codec explicitly for copy when bitrate exceeds limit [PR #13423], by @gnattu
* Fix parallel use of not thread-safe SubtitleFormat instance [PR #13384], by @alltilla
* Use WriteThrough for ImageSaver [PR #13411], by @gnattu
* Catch IOExceptions for GetFileSystemMetadata [PR #13390], by @gnattu
* Fix rating levels [PR #13388], by @Shadowghost
* Fix: handling of <set> elements in NfoParser [PR #13092], by @TheMelmacian
* Fix interface selection [PR #13382], by @Shadowghost

## 10.10.4 – 2025-01-22

# :rocket: Jellyfin Server 10.10.4

We are pleased to announce the latest stable release of Jellyfin, version 10.10.4!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-10-4).

## Changelog (20)

### 📈 General Changes
* Never treat matroska as webm for audio playback [PR #13345], by @gnattu
* Don't generate trickplay for backdrops [PR #13183], by @gnattu
* Use nv15 as intermediate format for 2-pass rkrga scaling [PR #13313], by @gnattu
* Fix DTS in HLS [PR #13288], by @Shadowghost
* Transcode to audio codec satisfied other conditions when copy check failed. [PR #13209], by @gnattu
* Fix missing episode removal [PR #13218], by @Shadowghost
* Fix NFO ID parsing [PR #13167], by @Shadowghost
* Always do tone-mapping for HDR transcoding when software pipeline is used [PR #13151], by @nyanmisaka
* Fix EPG image caching [PR #13227], by @Shadowghost
* Don't use custom params on ultrafast x265 preset [PR #13262], by @gnattu
* Backport ATL update 6.11 to 10.10 [PR #13280], by @gnattu
* Don't fall back to ffprobe results for multi-value audio tags [PR #13182], by @gnattu
* Backport ATL update to 10.10 [PR #13180], by @gnattu
* Properly check LAN IP in HasRemoteAccess [PR #13187], by @gnattu
* Fix possible infinite loops in incomplete MKV files [PR #13188], by @Bond-009
* Check if the video has an audio track before codec fallback [PR #13169], by @gnattu
* Fallback to lossy audio codec for bitrate limit [PR #13127], by @gnattu
* Fix missing ConfigureAwait [PR #13139], by @gnattu
* Only do DoVi remux when the client supports profiles without fallbacks [PR #13113], by @gnattu
* Enable RemoveOldPlugins by default (10.10.z backport) [PR #13106], by @RealGreenDragon

## 10.10.3 – 2024-11-19

# :rocket: Jellyfin Server 10.10.3

We are pleased to announce the latest stable release of Jellyfin, version 10.10.3!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-10-3).

## Changelog (2)

### 📈 General Changes
* Exclude file system based library playlists from migration [PR #13059], by @Shadowghost
* Downgrade minimum sdk version [PR #13063], by @crobibero

## 10.10.2 – 2024-11-16

# :rocket: Jellyfin Server 10.10.2

We are pleased to announce the latest stable release of Jellyfin, version 10.10.2!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-10-2).

## Changelog (15)

### 🏗️  Enhancements
* Added query filter to disregard disabled Providers [PR #12916], by @JPVenson
### 📈 General Changes
* Respect cancellation token/HTTP request aborts correctly in `SymlinkFollowingPhysicalFileResultExecutor` [PR #13033], by @goknsh
* Update dependencies [PR #13038], by @Bond-009
* Fix playlists [PR #12934], by @Shadowghost
* Fix missing procamp vaapi filter [PR #13026], by @nyanmisaka
* Only set first MusicBrainz ID for audio tags [PR #13003], by @gnattu
* Always cleanup trickplay temp for ffmpeg failures [PR #13030], by @gnattu
* Use invariant culture for tonemap options [PR #12991], by @gnattu
* Fix InvariantCulture in VPP tonemap options [PR #12989], by @nyanmisaka
* Fix trickplay images never being replaced [PR #12955], by @gnattu
* Fix height of imported trickplay tiles [PR #12964], by @nyanmisaka
* Always consider null char as delimiter for ID3v2 [PR #12962], by @gnattu
* Fix pixel format in HEVC RExt SDR transcoding [PR #12973], by @nyanmisaka
* Fix json array string writer in JsonDelimitedArrayConverter [PR #12949], by @gnattu
* Add a small tolerance value to remux fps check [PR #12947], by @gnattu

## Packaging (1)

* Ignore proxy settings during healthcheck [PR #47](https://github.com/jellyfin/jellyfin-packaging/pull/47), by @agentsas

## 10.10.1 – 2024-11-03

# :rocket: Jellyfin Server 10.10.1

We are pleased to announce the latest stable release of Jellyfin, version 10.10.1!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-10-1).

## Changelog (5)

### 📈 General Changes
* Set AudioCodec when building stream [PR #12931], by @gnattu
* Remove DynamicImageResponse local image after saved to metadata folder [PR #12940], by @gnattu
* Fixed possible NullReferenceException in SessionManager [PR #12915], by @JPVenson
* Don't try to prune images for virtual episodes. [PR #12909], by @revam
* Fix TMDB import failing when no IMDB ID is set for a movie [PR #12891], by @benedikt257

## 10.10.0 – 2024-10-26

# :rocket: Jellyfin Server 10.10.0

We are pleased to announce the latest stable release of Jellyfin, version 10.10.0!

This major release brings many new features, improvements, and bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-10-0).

## Changelog (189)

### 🔒 Security
* Fix OpenAPI workflow [PR #11733], by @nielsvanvelzen
### 🌟 Highlights
* Feature/media segments plugin api [PR #12359], by @JPVenson
* Add media segments API [PR #12345], by @JPVenson
* Enable Dolby AC-4 decoder [PR #11486], by @gnattu
* Use real temp dir instead of cache dir for temp files [PR #12226], by @Bond-009
* Add software tonemap filter support [PR #12270], by @gnattu
### 🏗️  Enhancements
* Enable Rockchip MJPEG encoder for Trickplay [PR #12610], by @nyanmisaka
* Add SUPPLEMENTAL-CODECS for Dolby Vision video with fallbacks [PR #12605], by @gnattu
* Enable the new BWDIF CUDA deint filter when available [PR #12590], by @nyanmisaka
* Add native VPP tonemap for QSV on Windows [PR #12592], by @nyanmisaka
* Add subtitle parser errors to log if available [PR #12479], by @pret0rian
* Tune x264/5 encoding params for realtime playback [PR #12540], by @nyanmisaka
* Prevent server from starting if the ffmpeg path is invalid [PR #12463], by @gnattu
* Fix the broken video orientation (+-90/180) [PR #11250], by @nyanmisaka
* Add better audio VBR settings [PR #11492], by @gnattu
* Add audio remux to UniversalAudioController [PR #11399], by @gnattu
* Enable hardware Trickplay processing pipeline for VideoToolbox [PR #11510], by @gnattu
* Add remuxing support for VP9 [PR #11489], by @gnattu
* Add option to extract keyframe only during trickplay image generation [PR #11511], by @gnattu
* Support filter by index number in ItemsController [PR #12027], by @nielsvanvelzen
* Prefer profile over codec for display title [PR #11772], by @Bond-009
### 📈 General Changes
* Fix check for format option in scale_cuda filter [PR #12874], by @nyanmisaka
* Added Unittest to check for unapplied model changes [PR #12854], by @JPVenson
* Add catch to remove cached user if creation fails [PR #12574], by @JPVenson
* Infer more audio codec from containers [PR #12837], by @gnattu
* Fix seeking beyond EOF in HWA transcoding [PR #12847], by @nyanmisaka
* Don't check remote sources for trickplay [PR #12824], by @gnattu
* Ensure Skia images are always disposed [PR #12786], by @JPVenson
* NetworkManager: Use MemberNotNull attribute [PR #12777], by @fice-t
* StartupHelper: fix app paths when SpecialFolder does not yet exists. [PR #12790], by @tmds
* Clean up logging in MediaSegmentManager [PR #12776], by @crobibero
* Extract DoVi thumbnail at 4000nit [PR #12771], by @gnattu
* Fix allow inputContainer to be null for Live TV [PR #12770], by @joshjryan
* Clean up deprecated -vsync option [PR #12765], by @nyanmisaka
* Fix full range in SW decoder & HW encoder for Trickplay [PR #12763], by @nyanmisaka
* Fix RKMPP-DRM-OpenCL mapping [PR #12758], by @nyanmisaka
* Disable ATL's internal ID3v2.2/3 splitting [PR #12751], by @gnattu
* Improve Trickplay image quality using HQ scaler on intel [PR #12759], by @nyanmisaka
* Add perf tradeoff mode to image extractor [PR #12744], by @gnattu
* Do not consider tags in search [PR #12741], by @Shadowghost
* Handle full range output in tonemap filter for Trickplay [PR #12746], by @nyanmisaka
* Workaround ATL tag parsing [PR #12705], by @gnattu
* Pre-fill ParentIndexNumber to preserve it between scans [PR #12739], by @Shadowghost
* Add missing migration for SegmentProviderId [PR #12735], by @Shadowghost
* Fix vpp tonemap pixfmt regression [PR #12733], by @nyanmisaka
* Fix the invalid libplacebo filter option [PR #12732], by @nyanmisaka
* Add endpoint for getting playlists by id [PR #12697], by @Shadowghost
* Ensure user's own playlists are accessible regardless of allowed tags [PR #12700], by @elfalem
* Fix get sessions with api key [PR #12696], by @gnattu
* Only move trickplay file should not be saved with media to metadata dir [PR #12704], by @gnattu
* Sanitize CustomTagDelimiters server side [PR #12698], by @gnattu
* Fix MJPEG hwenc may be incorrectly enabled on AMDGPU [PR #12695], by @nyanmisaka
* Tweak Trickplay migration for speed [PR #12643], by @crobibero
* Fix libx264/libx265 auto preset [PR #12692], by @gnattu
* Fix intel Xe kernel driver cannot be used with QSV [PR #12691], by @nyanmisaka
* Escape quotes in the subtitle path [PR #12690], by @dmitrylyzo
* Allow Playlists access for users with allowed tags configured [PR #12686], by @elfalem
* Fix GetTrickplayTileImage operation name [PR #12681], by @nielsvanvelzen
* Fix incorrect input range for certain hw JPEG encoders [PR #12683], by @nyanmisaka
* Fix media segment operation name [PR #12682], by @nielsvanvelzen
* Fix the diff between requested and actual resolution in RKMPP [PR #12680], by @nyanmisaka
* Fix DeviceProfile.Id should be nullable [PR #12679], by @nielsvanvelzen
* Better bitrate and resolution normalization [PR #12644], by @gnattu
* Let HLS Controller decide if subtitle should be burn in [PR #12676], by @gnattu
* Fix metadata merge for BoxSets [PR #12583], by @Shadowghost
* Fix RKMPP 2pass scaling in Trickplay [PR #12675], by @nyanmisaka
* Enable key-frame only decoding for RKMPP trickplay [PR #12673], by @nyanmisaka
* Add more DTOs to API [PR #12587], by @Shadowghost
* Enable HEVC RExt HW decoding for 4:2:2/4:4:4 content [PR #12664], by @nyanmisaka
* Watch library directories with perm errors [PR #10684], by @bhowe34
* Don't expose hwaccel type for non-admin [PR #12663], by @gnattu
* Only sort item by width when they have the same path [PR #12626], by @gnattu
* Sort by version name before resolution sorting [PR #12621], by @gnattu
* Fix subtitle dar comparison when number not exact [PR #12660], by @gnattu
* Optimizations & Simplifications - Removed multiple from String.Split to Span [PR #9374], by @Shadowghost
* Test StreamBuilder more precisely & improve the transcode reason [PR #12639], by @gnattu
* Fix some PGSSUB burn-in perf regressions [PR #12655], by @nyanmisaka
* Don't resolve trickplay folder during media scanning [PR #12652], by @gnattu
* Remove redundant newline to fix CI [PR #12636], by @gnattu
* Only remove images in metadata folder by default [PR #12631], by @gnattu
* Don't extract chapter images if chapters are <1s long on average [PR #11832], by @Bond-009
* Add option to always burn in subtitles if transcoding is triggered [PR #12430], by @gnattu
* Enable BWDIF VideoToolbox deint filter when available [PR #12634], by @gnattu
* Fix QSV presets may be empty [PR #12633], by @nyanmisaka
* Use subtitle cache when burning subtitles in [PR #12627], by @oxixes
* feat(i18n): able to finetune transliterator [PR #12378], by @BLumia
* cli: add option to disable network change detection [PR #11253], by @gnattu
* Add audio ranking for transcoding profiles [PR #12546], by @dmitrylyzo
* Use enums for encoding options [PR #12561], by @Shadowghost
* Extract condition from Where clause to eliminate extra filtering [PR #12614], by @dmitrylyzo
* Update issue template version from 10.9.10 to 10.9.11 [PR #12613], by @TimGels
* Fix trickplay migration [PR #12608], by @gnattu
* Add non-standard multi-value audio tag support [PR #12385], by @gnattu
* Fix FormattingStreamWriter type [PR #12607], by @gnattu
* Make Live TV compatibility profiles customizable [PR #12529], by @gnattu
* Enhance Trickplay [PR #11883], by @Shadowghost
* Remove left-over network path references [PR #12446], by @nielsvanvelzen
* Backport #12562 and #12521 [PR #12602], by @gnattu
* Enable tone-mapping and HLS remuxing for DoVi Profile 10 in AV1 [PR #12604], by @nyanmisaka
* Add support DoVi Profile 10 [PR #11559], by @llutic
* Add MediaStream.ReferenceFrameRate for problematic video files [PR #12603], by @gnattu
* Cleanup tasks [PR #12578], by @Shadowghost
* Add SubContainer support to CodecProfile [PR #12420], by @gnattu
* Increase password hash iterations [PR #12552], by @Bond-009
* Remove passwordSha1 param from AuthenticateUser function [PR #12545], by @Bond-009
* Clean up UserDataManager [PR #12547], by @Bond-009
* Remove BOM from UTF-8 files [PR #12548], by @Bond-009
* Only run on pull_request_target, use jellyfin-bot [PR #12599], by @crobibero
* ABI Diff action - use Github Token [PR #12594], by @crobibero
* Add ABI compat workflow [PR #11132], by @crobibero
* Use frozen collections in MimeTypes.cs [PR #10826], by @goremykin
* Adapting AMD VAAPI-Vulkan pipeline to FFmpeg 7.0 [PR #12577], by @nyanmisaka
* Update QSV device args  to use the renderNodePath [PR #12384], by @evanjarrett
* Allow SW encoders to use VideoToolbox HW filters [PR #12576], by @gnattu
* Enable software tonemap for dolby vision [PR #12571], by @gnattu
* Update issue template version from 10.9.9 to 10.9.10 [PR #12559], by @TimGels
* Upgrade LRCParser to 2024.0728.2 [PR #12543], by @Shadowghost
* Add LiveTvController tests [PR #12549], by @Bond-009
* Add PluginsController tests [PR #12551], by @Bond-009
* Improve error message when image extraction times out [PR #12533], by @Bond-009
* Add new tonemap mode options [PR #12534], by @gnattu
* Use Apple reccomended values for HLS CODECS [PR #12532], by @Bond-009
* Reduce calls to GetUserById [PR #11665], by @Bond-009
* Fix noautorotate cli for videotoolbox [PR #12530], by @gnattu
* Adjust filters to adapt FFmpeg 7.0 [PR #12524], by @nyanmisaka
* Fix SA1508 in LyricScheduledTask [PR #12507], by @gnattu
* Allow svg for local images [PR #12454], by @theguymadmax
* Add support for ItemSortBy values in BoxSet [PR #12457], by @lostb1t
* Add lyrics library options, add download scheduled task [PR #12397], by @crobibero
* Pass Series Display Order information to SeasonInfo [PR #12498], by @scampower3
* chore: update BaseSqliteRepository.cs [PR #12471], by @eltociear
* Update XmlTvListingsProvider.cs to fix the record series button missing on many programs [PR #12398], by @bpauquette
* Update PluginPageInfo.cs summary. [PR #12464], by @dredstone1
* Update the default repository URL for the StudioImages plugin [PR #12375], by @tobias-varden
* Update README.md [PR #12435], by @aaronjrodrigues
* Fix VideoToolbox Hi10P [PR #12429], by @gnattu
* Remove unused encoders [PR #12428], by @gnattu
* Updated issue Jellyfin version [PR #12394], by @TimGels
* Fix missing service registration for MediaSegments [PR #12392], by @JPVenson
* Update VideoToolbox pipeline for jellyfin-ffmpeg7 [PR #12380], by @gnattu
* Enable more analyser rules as errors [PR #12369], by @Bond-009
* Add AC-4 downmix algorithm [PR #12354], by @gnattu
* Fix: parsing of xbmc style multi episode nfo files [PR #12268], by @TheMelmacian
* Add RFC7845 downmix algorithm [PR #12300], by @gnattu
* Migrate to z440.atl from TagLib-Sharp [PR #11879], by @gnattu
* Enable nullable for DtoService and DtoOptions [PR #11432], by @Bond-009
* Enable nullable for UserItemData [PR #11390], by @Bond-009
* Enable nullability for QueryResult [PR #12355], by @crobibero
* Display DOVI title in DisplayTitle when available [PR #12353], by @gnattu
* Add TrySetProviderId extension [PR #12295], by @Bond-009
* Fix up getting livetv programs api docs [PR #12327], by @crobibero
* Check MaxAudioChannels for directAudioStream candidates [PR #12319], by @gnattu
* Don't buffer content in GetStaticRemoteStreamResult [PR #12309], by @Bond-009
* Fix comment in PhotoProvider [PR #12323], by @tobias-varden
* Update issue report.yml to use 10.9.8 version [PR #12332], by @TimGels
* Fix BDMV stream indexes [PR #12310], by @Bond-009
* Fix AC-4 Sample rate check [PR #12299], by @gnattu
* Changed `GetThemeMedia` to support SortBy/Order options [PR #12167], by @ItsAllAboutTheCode
* Move external url listing to provider for plugin use [PR #12279], by @crobibero
* Fix (another) ArgumentNullException while scanning music [PR #12294], by @Bond-009
* Fix ArgumentNullException while scanning music [PR #12292], by @Bond-009
* Use complete paths in BD info [PR #12201], by @Bond-009
* Don't include new internal MediaStream properties in api spec [PR #12288], by @crobibero
* Run DeleteTranscodeFileTask on startup [PR #12239], by @Bond-009
* Allow streaming of raw PGS subtitles without transcoding [PR #12056], by @Arcus92
* Add check for ProviderIds to prevent '=' from appearing in keys, also support '=' in the values. [PR #12274], by @EraYaN
* Refactor bug report issue template [PR #11135], by @TimGels
* Improve LibraryManager.Sort when using "Random" order [PR #12165], by @ItsAllAboutTheCode
* Add unit tests for PremiereDateComparer [PR #12251], by @honestlywhoknows
* Add messages to LiveTvConflict exception [PR #12185], by @crobibero
* Don't expect `BaseItem` to be a movie/video file. [PR #11204], by @revam
* Enable H.264 Hi10P hardware decode for Apple Silicon on macOS >=14.6 [PR #12124], by @gnattu
* Improve empty list check [PR #12022], by @l2dy
* Replace async void with async Task in tests [PR #12012], by @Bond-009
* Fix build [PR #11993], by @Bond-009
* Revert "Allow collection sort by Release Date Descending" [PR #11971], by @Bond-009
* Remove old connection count props [PR #11972], by @Bond-009
* Update shields in README [PR #11973], by @Bond-009
* Add regression tests for update library endpoint [PR #11877], by @Bond-009
* Allow collection sort by Release Date Descending [PR #11615], by @piratefin
* README Typo Fixes [PR #11782], by @Jason-Barratt
* Fix OpenAPI workflow summary [PR #11780], by @nielsvanvelzen
* Fix OpenAPI workflow some more [PR #11779], by @nielsvanvelzen
* Improve OpenAPI diff workflow [PR #11769], by @nielsvanvelzen
* Only log item id in trickplay warning [PR #11711], by @Bond-009
* Fix reference to deprecated package [PR #11530], by @crobibero
* Add OpenAPI spec generator for stable releases [PR #11603], by @joshuaboniface
* Disable nuget warning in Jellyfin.Extensions [PR #11536], by @crobibero
* Update version in issue template [PR #11400], by @felix920506

## 10.9.11 – 2024-09-07

# :rocket: Jellyfin Server 10.9.11

We are pleased to announce the latest stable release of Jellyfin, version 10.9.11!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-9-11).

## Changelog (6)

### 📈 General Changes
* Fix subtitle and attachment extraction when input path contains quotes [PR #12575], by @dmitrylyzo
* Use filtered codecs to build appliedConditions [PR #12562], by @nyanmisaka
* Fix alt version name generation [PR #12558], by @Bond-009
* Create and use FormattingStreamWriter [PR #12550], by @Bond-009
* Fix CodecProfiles and video encoder profiles [PR #12521], by @nyanmisaka
* Don't apply chapter image settings to music [PR #12531], by @gnattu

## 10.9.10 – 2024-08-25

# :rocket: Jellyfin Server 10.9.10

We are pleased to announce the latest stable release of Jellyfin, version 10.9.10!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-9-10).

## Changelog (9)

### 📈 General Changes
* Include AVIF extension for support images [PR #12415], by @ikelos
* Apply all codec conditions [PR #12499], by @dmitrylyzo
* Revert "NextUp query respects Limit" [PR #12414], by @fredrik-eriksson 
* Set Content-Disposition header to attachment for image endpoints [PR #12490], by @nielsvanvelzen
* Fix bitstream filter not applied to videos in TS container [PR #12493], by @nyanmisaka
* Fix the record series button missing on many programs (port of #12398) [PR #12481], by @Bond-009
* Don't force non-virtual when all episodes in season are isMissing=true [PR #12425], by @scampower3
* Check attachment path for null before use [PR #12443], by @gnattu
* Fix SA1201 issue [PR #12390], by @justinkb

## 10.9.9 – 2024-08-05

# :rocket: Jellyfin Server 10.9.9

We are pleased to announce the latest stable release of Jellyfin, version 10.9.9!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-9-9).

## Changelog (3)

### 📈 General Changes
* Fix creating virtual seasons (again) [PR #12356], by @nielsvanvelzen
* Update Serilog deps [PR #12368], by @Bond-009
* Implement Device Cache to replace EFCoreSecondLevelCacheInterceptor [PR #11901], by @gnattu

## 10.9.8 – 2024-07-21

# :rocket: Jellyfin Server 10.9.8

We are pleased to announce the latest stable release of Jellyfin, version 10.9.8!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-9-8).

## Changelog (3)

### 📈 General Changes
* Properly escape paths in concat file for BDMV [PR #12296], by @Bond-009
* Fix localization of audio title [PR #12278], by @Bond-009
* Fix season handling ("Season Unknown" / unneccesary empty seasons) [PR #12240], by @nielsvanvelzen

## 10.9.7 – 2024-06-25

# :rocket: Jellyfin Server 10.9.7

We are pleased to announce the latest stable release of Jellyfin, version 10.9.7!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-9-7).

## Changelog (23)

### 📈 General Changes
* Fix HDR detection for 4K Blu-Ray BDMVs [PR #12166], by @Bond-009
* Log album name and id in normalization task [PR #11911], by @Bond-009
* Try to add extracted lyrics during scanning [PR #12126], by @gnattu
* Fix season backdrops [PR #12055], by @Shadowghost
* Rewrite PlaylistItemsProvider as ILocalMetadataProvider [PR #12053], by @Shadowghost
* Fix empty image folder removal for legacy locations [PR #12025], by @Shadowghost
* Fix season handling [PR #12050], by @Shadowghost
* Only cleanup children on specific exceptions [PR #12134], by @Shadowghost
* Remove incomplete mediatype restriction from playlists [PR #12024], by @Shadowghost
* Fix MicroDVD being recognized as DVDSUB subtitles [PR #12149], by @nyanmisaka
* Fix Cleanup Task metadata saving [PR #12123], by @Shadowghost
* Fix the Australian PG rating [PR #12043], by @oddstr13
* Map IPv6 mapped IPv4 addresses back to IPv4 before running checks [PR #12094], by @Shadowghost
* Do not override <year> if <releasedate> is set [PR #12120], by @Shadowghost
* Make m2ts extension case-insensitive [PR #12065], by @Rivenlalala
* Overwrite supported codecs for livetv [PR #12017], by @gnattu
* Check hearing impared flags with equality instead of contains [PR #12026], by @Bond-009
* Fix local episode image thumb recognition [PR #12039], by @Shadowghost
* Fix video embedded image detection [PR #12031], by @nyanmisaka
* Fix replace all and respect metadata settings [PR #12028], by @Shadowghost
* Fix Music Brainz release group query [PR #12073], by @Shadowghost
* Fix mpeg-ts detection [PR #12046], by @gnattu
* Do not fail user deletion if we have no playlist folder [PR #12037], by @Shadowghost

## 10.9.6 – 2024-06-06

# :rocket: Jellyfin Server 10.9.6

We are pleased to announce the latest stable release of Jellyfin, version 10.9.6!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-9-6).

## Changelog (4)

### 📈 General Changes
* Fix fallback artist when taglib fails [PR #11989], by @gnattu
* Do not stop validation if folder was removed [PR #11959], by @Shadowghost
* Use only 1 write connection/DB [PR #11986], by @Bond-009
* Set ProductionLocations instead of Tags [PR #11984], by @Shadowghost

## 10.9.5 – 2024-06-05

# :rocket: Jellyfin Server 10.9.5

We are pleased to announce the latest stable release of Jellyfin, version 10.9.5!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-9-5).

## Changelog (12)

### 📈 General Changes
* Fallback to local dir when saving to media dir fails [PR #11978], by @Shadowghost
* Fix Library renaming [PR #11963], by @gnattu
* Fix identify over NFO and replace all when NFO saving enabled [PR #11921], by @Shadowghost
* Create readonly DB connections when possible [PR #11969], by @Bond-009
* Fix local image saving [PR #11934], by @Shadowghost
* Fix dateadded and movie NFO recognition [PR #11935], by @Shadowghost
* Increase lyrics migration batch size to 5000 [PR #11943], by @Shadowghost
* Export trailer URLs in new format [PR #11958], by @Shadowghost
* Do not delete file locations for virtual episodes and seasons [PR #11954], by @Shadowghost
* NextUp query respects Limit [PR #11956], by @cptn-x
* Only set season path if season folder parsing was successful [PR #11920], by @Shadowghost
* Check trailer distinction by URL [PR #11933], by @Shadowghost

## 10.9.4 – 2024-06-01

# :rocket: Jellyfin Server 10.9.4

We are pleased to announce the latest stable release of Jellyfin, version 10.9.4!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-9-4).

## Changelog (15)

### 🔒 Security
* Fix FirstTimeSetupHandler allowing public access [PR #11873], by @thornbill
### 📈 General Changes
* Add Env Var to disable second level cache [PR #11823], by @gnattu
* Fix replace logic [PR #11743], by @Shadowghost
* Mark Audio as RequiresDeserialization and backfill data [PR #11762], by @Shadowghost
* Move NFO series season name parsing to own local provider [PR #11719], by @Shadowghost
* Audio normalization: parse ffmpeg output line by line [PR #11910], by @Bond-009
* Relax remuxing requirement for LiveTV [PR #11851], by @gnattu
* Fix multi-part album folder being detected as artist folder [PR #11886], by @gnattu
* Use music metadata from ffprobe when TagLib fails [PR #11859], by @gnattu
* Return missing episodes for series when no user defined [PR #11806], by @Shadowghost
* Fix missing episodes query for seasons [PR #11882], by @Shadowghost
* Escape tmpConcatPath for DVD and BD folder [PR #11894], by @gnattu
* Don't check if admin has access to library when updating [PR #11876], by @Bond-009
* Fix ffprobe -user_agent parameter [PR #11857], by @gnattu
* Upgrade dependencies [PR #11867], by @Shadowghost

## 10.9.3 – 2024-05-27

# :rocket: Jellyfin Server 10.9.3

We are pleased to announce the latest stable release of Jellyfin, version 10.9.3!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-9-3).

## Changelog (19)

### 📈 General Changes
* Extract media attachment one by one if the filename appears to be a path [PR #11812], by @gnattu
* Filter invalid IPs on external interface matching [PR #11766], by @gnattu
* Use SharedStream for LiveTV more restrictively [PR #11805], by @gnattu
* Fix the IOSurf error in QSV transcoding [PR #11830], by @nyanmisaka
* Improve reliability of HasChanged check [PR #11792], by @Shadowghost
* Trickplay: kill ffmpeg when task is cancelled [PR #11790], by @NotSaifA
* Force more compatible transcoding profile for LiveTV [PR #11801], by @gnattu
* Exclude virtual items from DateLastMediaAdded calculation [PR #11804], by @Shadowghost
* Add Canceled to ended state [PR #11808], by @Shadowghost
* Recalculate trickplay image height for anamorphic videos [PR #11798], by @gnattu
* Fix BD/DVD folder chapter image extraction [PR #11754], by @Shadowghost
* Mark SearchHint.MatchedTerm as nullable [PR #11802], by @crobibero
* Disable VA-VK interop on not supported kernel versions [PR #11799], by @nyanmisaka
* Retain order blu-ray segments [PR #11781], by @Bond-009
* Override too small trickplay image interval [PR #11788], by @gnattu
* Apply audio boost when downmixing regardless of downmixalgo [PR #11774], by @Bond-009
* Fix VideoToolbox H264 constrained profile option [PR #11713], by @gnattu
* Do not run trickplay on scan if disabled [PR #11739], by @Shadowghost
* Don't require user when getting current session [PR #11738], by @crobibero

## 10.9.2 – 2024-05-17

# :rocket: Jellyfin Server 10.9.2

We are pleased to announce the latest stable release of Jellyfin, version 10.9.2!

This minor release brings several bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-9-2).

## Changelog (19)

### 🔒 Security
* Fix FirstTimeSetupPolicy allowing guest access [PR #11651], by @thornbill
### 🏗️  Enhancements
* Fix series status parsing [PR #11648], by @Shadowghost
### 📈 General Changes
* Fix season names [PR #11647], by @Shadowghost
* Secure local playlist path handling [PR #11680], by @Shadowghost
* Prevent double iterating over all seasons [PR #11700], by @Shadowghost
* Fix network binding [PR #11671], by @Shadowghost
* Workaround ffmpeg keyframe seeking for external subtitles [PR #11689], by @gnattu
* Use MediaType instead of ToString and add text/ as disallowed mimetypes [PR #11699], by @cvium
* Fix not binding to SQL parameters [PR #11698], by @Bond-009
* Fix local playlist scanning [PR #11673], by @Shadowghost
* Restore caching for UserManager [PR #11670], by @gnattu
* Properly dispose dbContext in MigrateUserDb [PR #11677], by @Bond-009
* Fix quality parameter for vaapi_mjpeg [PR #11675], by @gnattu
* Always fallback for failed HEAD request [PR #11668], by @gnattu
* Don't generate TrickPlay images for files that don't exist [PR #11653], by @Bond-009
* Allow empty user id when getting device list [PR #11633], by @crobibero
* Fix missing filename for timer [PR #11629], by @gnattu
* Handle exception for unexpected audio file YEAR tag values [PR #11621], by @nfmccrina
* Fix network config [PR #11587], by @gnattu

## 10.9.1 – 2024-05-13

# :rocket: Jellyfin Server 10.9.1

We are pleased to announce the latest stable release of Jellyfin, version 10.9.1!

This minor release brings several bugfixes to improve your Jellyfin experience. In particular it fixes a few glaring bugs that had mass impact with 10.9.0. We recommend everyone on 10.9.0 upgrade to 10.9.1 now.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-9-1).

## Changelog (5)

### 🏗️  Enhancements
* Default to processor count concurrent scan instead of 2 * processor count [PR #11569], by @crobibero
* Change "try" to "attempt" english translation [PR #11578], by @TimGels
### 📈 General Changes
* Fix absolute path checking on windows [PR #11570], by @gnattu
* Add metrics collector to disposable parts [PR #11539], by @crobibero
* Fix migration with special Rating [PR #11541], by @crobibero

## 10.9.0 – 2024-05-11

# :rocket: Jellyfin Server 10.9.0

We are pleased to announce the latest stable release of Jellyfin, version 10.9.0!

This major release brings many new features, improvements, and bugfixes to improve your Jellyfin experience.

As always, please ensure you stop your Jellyfin server and take a full backup before upgrading!

You can find more details about and discuss this release [on our forums](https://forum.jellyfin.org/t-new-jellyfin-server-web-release-10-9-0).

## Changelog (743)

### 🔒 Security
* Require elevation for plugin related endpoints [PR #11436], by @nielsvanvelzen
* fix: forward port patch for GHSA-866x-wj5j-2vf4 [PR #11228], by @gnattu
* Fix library access [PR #8732], by @thornbill
### 🌟 Highlights
* feat: Fully support hardware filters on Apple VideoToolbox [PR #11014], by @gnattu
* Add full HWA transcoding pipeline for Rockchip RKMPP [PR #10748], by @nyanmisaka
* Move DLNA to Plugin (Part 2) [PR #10558], by @barronpm
* Update to .NET 8 [PR #10463], by @Bond-009
* Trickplay preview images [PR #9554], by @nicknsy
* Add AV1 hardware and software encoding [PR #9907], by @nyanmisaka
* Add support for ffmpeg's segment deletion for HLS [PR #8744], by @DomiStyle
* refactor: admin users must have a non-empty password [PR #9821], by @cvium
* chore: deprecate EasyPassword as it isn't very secure [PR #9820], by @cvium
* Audio normalization [PR #9222], by @TelepathicWalrus
* Add "Allowed Tags" to Parental Controls [PR #9139], by @Jpuc1143
* Add Lyrics API Endpoint [PR #8381], by @1hitsong
* Add hearing impaired subtitle stream indicator [PR #7379], by @1337joe
### 🏗️  Enhancements
* Add playlist ACL endpoints [PR #11220], by @Shadowghost
* Use enum for BaseItemDto.ExtraType [PR #11261], by @nielsvanvelzen
* Support "extra" folder for extras content [PR #11249], by @nielsvanvelzen
* Fix the fragile segment deletion [PR #11161], by @nyanmisaka
* Enable nullable for more files [PR #11149], by @Bond-009
* Catch delete encoded media file exceptions [PR #11165], by @vessd
* Add ability to enable/disable libraries [PR #11037], by @btopherjohnson
* Add LSR/CITY to artist whitelist [PR #11160], by @1337joe
* Add MediaStreamProtocol enum [PR #10153], by @nielsvanvelzen
* Move userId in API from route to optional query parameter [PR #11074], by @crobibero
* Always make userId query parameter optional [PR #11024], by @nielsvanvelzen
* Make userId optional in GetProgramsDto [PR #11028], by @nielsvanvelzen
* Fix the preproc filters for dvbsub burn-in [PR #11034], by @nyanmisaka
* Add EqualsAny for VideoCodecTag condition [PR #10965], by @nyanmisaka
* Correct VIDEO-RANGE field for HLG content [PR #10968], by @nyanmisaka
* AsyncKeyedLock migration [PR #10801], by @MarkCiliaVincenti
* Extract all subtitle streams simultaneously [PR #10884], by @alltilla
* Feature/ghcs ffmpegversion [PR #10888], by @JPVenson
* Fixed some issues in PGSSUB and ASS subtitle burn-in [PR #10924], by @nyanmisaka
* Remove UserManager Cache [PR #10781], by @barronpm
* Remove some unused client capabilities and sync code [PR #10812], by @nielsvanvelzen
* Use -noauto{scale,rotate} for disabling auto filters [PR #10810], by @nyanmisaka
* Make TMDb api key configurable, fix missing/wrong image urls [PR #10737], by @1337joe
* Update /Device endpoint to return CustomName [PR #10422], by @scampower3
* Use `eof_action=pass` when overlaying subtitles [PR #10710], by @jkhsjdhjs
* Move Jellyfin.Networking [PR #10660], by @barronpm
* Fix Nullability for INetworkManager.GetBindAddress [PR #10659], by @barronpm
* Make "activeWithinSeconds" independent from "controllableByUserId" parameter [PR #10649], by @felix920506
* Fix A53 CC SEI breaking H26x_VAAPI hardware encode [PR #10275], by @nyanmisaka
* Add option to include resumable items in next up requests [PR #10200], by @thornbill
* Remove one session per device id limitation [PR #10197], by @thornbill
* Fix AV1 NVENC encoder profile option [PR #10199], by @nyanmisaka
* Fix AV1 playback in LiveTV [PR #10183], by @nyanmisaka
* Fix MJPEG video is recognized as embedded image [PR #10173], by @nyanmisaka
* Fix the issue that audio bsf only takes effect for remuxing [PR #10172], by @nyanmisaka
* Expand AMD VA-API Vulkan filtering support to Polaris/gfx8 [PR #10074], by @nyanmisaka
* Only disable the global_header for AMD HEVC encoder [PR #10045], by @nyanmisaka
* Add support for lyric provider plugins [PR #9920], by @nielsvanvelzen
* Rearrage the Amd vaapi-vulkan pipeline for synchronization [PR #9882], by @nyanmisaka
* Use default files to remove index.html from url [PR #9776], by @thornbill
* Fix vaapi-vulkan subtitle tearing issue [PR #9584], by @nyanmisaka
* Adapt Vulkan filtering to 6.0 [PR #9429], by @nyanmisaka
* Improve the Vulkan based subtitle burn-in performance [PR #9402], by @nyanmisaka
* Remove unused notification endpoints [PR #8952], by @nielsvanvelzen
* Authentication API deprecations [PR #8927], by @nielsvanvelzen
* Remove unused ImageByName API [PR #8928], by @nielsvanvelzen
* Add admin login to QuickConnect API [PR #8734], by @nielsvanvelzen
* Add SeriesStatus.Unreleased [PR #8661], by @nielsvanvelzen
* Enable Quick Connect by default [PR #7624], by @nielsvanvelzen
* Add new priority level to ResolverPriority for plugins [PR #7519], by @nielsvanvelzen
### 📈 General Changes
* Use actual item removal count for library change determination [PR #11526], by @gnattu
* Default to not extract lyrics [PR #11523], by @gnattu
* Let AutoDiscoveryHost bind to all addresses [PR #11504], by @gnattu
* Always set cast receivers during migration [PR #11516], by @crobibero
* Add Not Implemented response check to m3u tuner HEAD request [PR #11496], by @davidfdezalcoba
* Allow explicitly set userId for RequestHelpers.GetSession [PR #11505], by @gnattu
* Fix broken hardware encoder and filter for trickplay [PR #11506], by @gnattu
* Workarounds TV tuners rejecting HEAD method [PR #11495], by @gnattu
* Clean up synchronization [PR #11458], by @MarkCiliaVincenti
* Playlist fixes [PR #11487], by @Shadowghost
* Don't close inactive session on default [PR #11491], by @gnattu
* Fix external LRC files being incorrectly overwritten during the initial scan [PR #11480], by @gnattu
* Fix subtitle saving if file already exists [PR #11310], by @Shadowghost
* Validate Collection Folders on adding and removal [PR #11444], by @gnattu
* Fix missing season Index [PR #11472], by @gnattu
* Always attempt to get User if a user id is provided [PR #11471], by @crobibero
* More efficient array creation [PR #11468], by @Bond-009
* Fix incomplete tag query for whitelist tags [PR #11416], by @gnattu
* Improve audio normalization [PR #11457], by @Bond-009
* Use more accurate rounding in GetFixedOutputSize [PR #11435], by @gnattu
* Properly await Task.Delay() [PR #11361], by @Bond-009
* Fix multiple intro providers and remove unneeded ToLists [PR #11431], by @Bond-009
* Use StringSplitOptions.TrimEntries where possible [PR #11421], by @Bond-009
* Always scan ReplayGain tag [PR #11418], by @Bond-009
* Fix task CleanupCollectionAndPlaylistPathsTask removing valid paths [PR #11410], by @jmqm
* Don't run ffprobe a second time for music file [PR #11419], by @Bond-009
* Only apply custom downmix to 5.1 audios [PR #11401], by @gnattu
* fix: don't apply whitelist tags to libraries [PR #11377], by @gnattu
* Maintaining track order when a new playlist is created from an existing playlist [PR #11371], by @nickyg91
* Fix InvalidCastException in ItemUpdateController [PR #11398], by @nielsvanvelzen
* Limit sessions per user [PR #11370], by @crobibero
* ci: Ensure lock directory exists [PR #11383], by @joshuaboniface
* Fix WebSocket disconnecting when exception is thrown during processing [PR #11395], by @nielsvanvelzen
* ci: Add flock to openapi spec upload [PR #11381], by @joshuaboniface
* #11289 Fixed cleanup task not checking for folders [PR #11311], by @JPVenson
* fix: explicitly allow remove root when performing library removal [PR #11352], by @gnattu
* Changes SessionWebSocketListener to (re)use a timer [PR #11358], by @Bond-009
* Enable nullable for LibraryManager [PR #11191], by @Bond-009
* Support age in LocalizationManager.GetRatingLevel [PR #11367], by @nielsvanvelzen
* fix: bind auto-discovery to multicast ip on macOS [PR #11368], by @gnattu
* fix: don't extract external sub [PR #11373], by @gnattu
* Write JSON directly to logfile [PR #11360], by @Bond-009
* fix: fallback to artist if album artist not provided [PR #11357], by @crobibero
* fix: use new serializer cache per IXmlSerializer [PR #11356], by @crobibero
* Validate item access [PR #11171], by @crobibero
* fix: fix off-by-one error in `GetAttributeValue` [PR #11351], by @revam
* Don't decode animated images [PR #11109], by @crobibero
* Only update if actively refreshing [PR #11341], by @crobibero
* Fix track MBID in audio metadata [PR #11301], by @lyarenei
* Enable more warnings as errors [PR #11288], by @Bond-009
* Don't throw if file was already removed [PR #11286], by @Shadowghost
* Allow ApiKey to authorize against the FirstTimeSetupOrElevated policy [PR #11338], by @crobibero
* Add support for out-of-spec but existent, Dolby Vision Profile 8 CCid 6 media. [PR #11334], by @GeorgeH005
* Add index for lastPlayedDate [PR #11342], by @crobibero
* Fix policy for GetRemoteSubtitles [PR #11321], by @nielsvanvelzen
* Fix disabled libraries being returned in MediaFolders api [PR #11236], by @thornbill
* Fix some spelling mistakes [PR #11287], by @Shadowghost
* Add jacket to the list of music images [PR #11314], by @Tina-otoge
* Fix apple audio codecs [PR #11315], by @gnattu
* fix: rtsp live stream ffprobe timeout [PR #11279], by @chencaidy
* fix: av1 codecs string [PR #11280], by @gnattu
* Lowercase CollectionTypeOptions to match legacy experience [PR #11272], by @crobibero
* Fix FindExtras overwriting current extra type [PR #11260], by @nielsvanvelzen
* Remove SessionInfo.FullNowPlayingItem from API responses [PR #11268], by @nielsvanvelzen
* fix metadata refresh for artists [PR #11257], by @sibbi77
* Catch exceptions in auto discovery [PR #11252], by @crobibero
* fix: don't do empty hwupload for VT [PR #11235], by @gnattu
* fix: use a reentrant lock when accessing active connections [PR #11256], by @cvium
* fix: add image count check to splash screen generation [PR #11245], by @revam
* Add i18n for TaskCleanCollectionsAndPlaylists [PR #11248], by @crobibero
* fix: unset qmin and qmax for vt [PR #11246], by @gnattu
* fix: disable api endpoint for ffmpeg path for security [PR #11225], by @gnattu
* Fix the broken codecs shifting [PR #11243], by @nyanmisaka
* Fix compiler warnings for Emby.Server.Implementations [PR #9641], by @Daaiid
* fix: move trickplay specific option into TrickplayOptions [PR #11229], by @gnattu
* Fix default values missing in ClientCapabilities(Dto) [PR #11232], by @nielsvanvelzen
* Adds rename command to commands.yml [PR #11178], by @felix920506
* fix: prefer cli ffmpeg path over config file [PR #11219], by @gnattu
* Fix OpenAPI workflow publishing pull request artifact as unstable specification [PR #11224], by @nielsvanvelzen
* Handle OpenAPI spec uploads properly [PR #11215], by @joshuaboniface
* fix: remove legacy codecs for VideoToolbox [PR #11217], by @gnattu
* Add openapi.json upload to new repo server [PR #11214], by @joshuaboniface
* Check all tags for allow/block [PR #11206], by @crobibero
* Fix sar->dar typo in #11185 [PR #11210], by @nyanmisaka
* fix: use Metal tonemap instead of OpenCL [PR #11198], by @gnattu
* fix: map encoder preset to quality setting for VideoToolbox [PR #11205], by @gnattu
* Fix codec vs ActualOutputVideoCodec [PR #11203], by @nyanmisaka
* Add new VideoRangeTypes to fully support DoVi on webOS [PR #10469], by @viktory36
* Add default auth policy to generated openapi spec [PR #11181], by @crobibero
* fix: use a more recent UA for M3U Tuner [PR #11199], by @gnattu
* feat(i18n): transliterate item name before sorting and filtering [PR #11172], by @BLumia
* fix: make sure the dimension is divisible by two for zscale [PR #11185], by @gnattu
* Convert bump_version to bumper only [PR #11184], by @joshuaboniface
* refactor: use Channels as queueing mechanism for periodic websocket messages [PR #11092], by @cvium
* fix: skip library folders that are inaccessible or empty [PR #9291], by @cvium
* Restore bump_version script [PR #11177], by @crobibero
* Remove legacy build utilities [PR #11162], by @crobibero
* Fixes  'replace missing metadata' overwrites existing metadata that does exist [PR #11136], by @scampower3
* IIS Hosting [PR #11120], by @kimboslice99
* Add lyric files to supported extensions [PR #11163], by @robert-hamilton36
* Add a github action to automatically precheck new issues for problems [PR #11154], by @felix920506
* Fix parsing of audio PremiereDate property [PR #11155], by @sel10ut
* Change parsing logic of audio track title [PR #11156], by @sel10ut
* chore: remove repetitive words [PR #11159], by @standstaff
* Don't attempt to calculate blurhash for svg [PR #11127], by @crobibero
* Added logging for where config logs and cache directories are stored [PR #11124], by @PeachesMLG
* Specify file as concat when extracting attachments [PR #11129], by @crobibero
* Lowercase MediaStreamProtocol for backwards compatibility [PR #11126], by @crobibero
* Cleanup PhotoProvider.cs using new .NET 8 features [PR #11119], by @PeachesMLG
* Remove Azure pipelines CI [PR #11121], by @joshuaboniface
* Add migration for new plugin repo [PR #11100], by @crobibero
* Extract and cache all media attachments in bulk [PR #11029], by @alltilla
* Precache livetv program images [PR #11083], by @crobibero
* Add support for converting from svg to other image types [PR #11077], by @crobibero
* Save embedded lyrics when probing audio [PR #11081], by @crobibero
* Always use ffmpeg codec for bluray [PR #11079], by @crobibero
* Collect candidate audio streams if no audio index is specified [PR #11046], by @dmitrylyzo
* Return backdrops with text as thumb for tmdb [PR #11078], by @crobibero
* fix replace missing metadata for music [PR #10691], by @bhowe34
* Rename route parameters that are id to be more descriptive [PR #11068], by @crobibero
* Store lyrics in the database as media streams [PR #9951], by @crobibero
* Remove "Media Playback" option from new issues [PR #11033], by @felix920506
* LiveTV MediaSourceProvider refactor [PR #11054], by @barronpm
* Do not dispose the ffmpeg process [PR #11064], by @Shadowghost
* Add item id to download activity [PR #11055], by @crobibero
* LiveTV Recordings Refactor [PR #11045], by @barronpm
* Add PlaybackOrder to Session state [PR #10934], by @dkacperski97
* Add IListingsManager Service [PR #10981], by @barronpm
* Add missing MIME types for comicbook formats [PR #11010], by @rluetzner
* Fix tiles playlist not using relative paths [PR #11000], by @nicknsy
* BDMV fixes [PR #10990], by @Shadowghost
* Make the bitrate of the fallback stream the same as the original [PR #9121], by @dmitrylyzo
* Add icon for Jellyfin Windows build [PR #10997], by @nyanmisaka
* Fix tests: discard webm from test mkvs if there is an unsupported codec [PR #10999], by @dmitrylyzo
* Escape subtitle extraction input path [PR #10992], by @felix920506
* Correct m4b mimetype [PR #10980], by @felix920506
* Discard WebM if there is an unsupported codec [PR #10772], by @dmitrylyzo
* Replace IServerEntryPoint with IHostedService [PR #10976], by @barronpm
* Update issue report.yml [PR #10946], by @felix920506
* SchedulesDirect fix [PR #10847], by @barronpm
* Fix some incompatible API deprecations [PR #10973], by @nielsvanvelzen
* Progress cleanup [PR #10969], by @barronpm
* Fix InvalidOperationException if log file not found [PR #10956], by @beakerandjake
* Update README to include default web client urls [PR #10949], by @beakerandjake
* Live TV DI [PR #10951], by @barronpm
* Fix NFO parser to be able to read corrct STRM URL format [PR #10870], by @MaVdbussche
* Add IGuideManager service [PR #10878], by @barronpm
* Fix long live tv load times, Fixes #10761 [PR #10881], by @TelepathicWalrus
* Fix action building [PR #10899], by @Gauvino
* Use NuGetAuthenticate@1 [PR #10882], by @crobibero
* Refactor Dockerfile and build [PR #10603], by @Gauvino
* Use helper function to compare guid [PR #10825], by @crobibero
* Add ITunerHostManager service and minor LiveTv cleanup [PR #10858], by @barronpm
* Fixed disposable not being called [PR #10613], by @JPVenson
* Fix incorrect path check in CleanupCollectionAndPlaylistPathsTask [PR #10876], by @Bond-009
* Move Live TV code to Jellyfin.LiveTv [PR #10838], by @barronpm
* Remove DLNA-specific DeviceProfile code [PR #10850], by @barronpm
* Respond with Service Unavailable if not in correct network [PR #10822], by @crobibero
* Specify DateTimeKind when pulling a DateTime out of the database [PR #10823], by @crobibero
* Detect audio spatial format [PR #9996], by @mohd-akram
* Fix NU1507 to allow only nuget.org via nuget.config [PR #10396], by @DaveSenn
* Add option to use replaygain tags for audio [PR #10566], by @TelepathicWalrus
* Feature/enable gh codespaces [PR #10324], by @JPVenson
* Auto Discovery Cleanup [PR #10793], by @barronpm
* Fix More Live TV Warnings [PR #10818], by @barronpm
* Fix broken code coverage [PR #10788], by @Bond-009
* Add ITranscodeManager [PR #10758], by @barronpm
* Fix Somalia's display name [PR #10765], by @st3v3nmw
* Fix StreamBuilder tests [PR #10757], by @dmitrylyzo
* Fix some warnings in LiveTV [PR #10682], by @barronpm
* Quote bash paths to prevent word splitting [PR #10672], by @Erotemic
* Convert CollectionType to use lowercase enum names [PR #10702], by @crobibero
* Fully specify github action versions [PR #10738], by @1337joe
* Remove OpenAPI artifact upload from test workflow [PR #10736], by @nielsvanvelzen
* Add new API endpoint to view/update Item UserData [PR #10573], by @arabcoders
* Remove unused DLNA models [PR #10685], by @barronpm
* Fix: Plugin Installed Alerts missing from Admin Dashboard #10620 [PR #10625], by @ilovepilav
* Allow persons on books [PR #10371], by @Pithaya
* Query Improvements [PR #10617], by @barronpm
* LibraryChangedNotifier Cleanup [PR #10592], by @barronpm
* Use new .NET 8 features [PR #10591], by @Bond-009
* Fix action building [PR #10590], by @Gauvino
* Move DLNA to Plugin (Part 1 (Part 2)) [PR #10574], by @barronpm
* Move DLNA to Plugin (Part 1) [PR #10557], by @barronpm
* Convert string MediaType to enum MediaType [PR #9762], by @crobibero
* Validate AuthenticationProviderId and PasswordResetProviderId [PR #10553], by @Chris-Codes-It
* Add GH Workflow for CI Tests [PR #10392], by @DavidFair
* Convert CollectionType, SpecialFolderType to enum [PR #9764], by @crobibero
* Convert ItemSortBy to enum [PR #9765], by @crobibero
* Revert SkiaSharp upgrade, fix library scan crashes [PR #10544], by @justin-sleep
* Update link to Jellyfin website [PR #10501], by @methbkts
* Combine Title and Overview for multi-episodes files for the TMDB provider [PR #10078], by @scampower3
* Add IDisposableAnalyzers to more projects [PR #10531], by @Bond-009
* Update SkiaSharp to v2.88.6 [PR #10513], by @Bond-009
* Correct docstring for /Upcoming [PR #10519], by @s-t-e-v-e-n-k
* Forward user_agent config to ffprobe [PR #10448], by @vincent
* Don't remove all tokens if invalid header is provided [PR #10490], by @crobibero
* #10333 Fix for stale PRs check: increase operations, process ascending [PR #10473], by @jacobslusser
* refactor: cache the resize image filter [PR #10472], by @cvium
* chore(deps): use Svg.Skia instead of the deprecated SkiaSharp.Svg [PR #10471], by @cvium
* Add auto close of an inactive session after X minutes [PR #10357], by @herby2212
* add EnableSubtitleManagement permission [PR #10410], by @Ch1nkara
* Fix mismatch between intel VAAPI UMD/KMD in rare cases [PR #10451], by @nyanmisaka
* #10333 Increases operations per run of GitHub 'stale' action [PR #10447], by @jacobslusser
* chore(deps): downgrade IDisposableAnalyzers to 4.0.4 [PR #10457], by @cvium
* add IAsyncDisposable to DisplayPreferencesManager [PR #10455], by @cvium
* Fix fuzz projects [PR #10416], by @Bond-009
* Fix a few resharper warnings and appy a few its suggestions [PR #10366], by @goremykin
* Customizable Cast Receiver [PR #10270], by @crobibero
* Multiple Stream changes [PR #10390], by @Bond-009
* Dlna cleanup [PR #10391], by @barronpm
* Enable CodeAnalysisTreatWarningsAsErrors for MediaBrowser.Common [PR #10389], by @Bond-009
* StreamingHelpers.GetOutputFileExtension should never return null [PR #10387], by @Bond-009
* Empty Guids shouldn't make it into the refresh queue [PR #10379], by @Bond-009
* Deprecate CanLaunchWebBrowser [PR #10381], by @Bond-009
* Refactor URI overrides [PR #10051], by @Shadowghost
* Fix HLS playback of m4a files with mjpeg stream [PR #10069], by @lonebyte
* XML Parsing Cleanup [PR #10352], by @barronpm
* Use Process.WaitForExitAsync added in .NET 5 [PR #10378], by @Bond-009
* Fix using movie.nfo first when <filename>.nfo also exists [PR #10339], by @leovan
* Jellyfin.Drawing minor improvements [PR #10347], by @Bond-009
* Add SystemManager service [PR #10337], by @barronpm
* Combine Title and Overview for multi-episodes files for NFO file [PR #10080], by @scampower3
* Use CryptoStream to convert stream from base64 [PR #10346], by @Bond-009
* Fix multiple FLAC HTTP Live Streaming issues [PR #10067], by @lonebyte
* Don't create non existent persons in LibraryManager.GetPerson [PR #10345], by @Bond-009
* Use Authorization header in integration tests [PR #10336], by @Bond-009
* Reduce string allocations [PR #10348], by @Bond-009
* Add support for transcode audio file to PCM format [PR #10321], by @feilongfl
* Fix/probesize [PR #10255], by @thomasjohansen
* Add full version tag for renovate [PR #10370], by @1337joe
* Fixed probesize argument passing to FFmpeg [PR #10135], by @0x25CBFC4F
* Fix JELLYFIN_FFMPEG_OPT is not enabled in fedora ExecStart [PR #10330], by @nyanmisaka
* #10333 Updates issue stale action to fix issues with not running [PR #10334], by @jacobslusser
* Minor cleanup [PR #10331], by @barronpm
* Add book related values to the PersonKind enum [PR #10325], by @Pithaya
* PhotoResolver: change how generated images are detected [PR #10222], by @Bond-009
* Add shebang to jellyfin.init [PR #10318], by @MartinWilkerson
* Allow repeated same tv guide channels on M3U tuner [PR #10323], by @hagaygo
* Use IHostLifetime for Shutdown/Restart [PR #10261], by @barronpm
* Ignore .zfs folder [PR #10219], by @Bond-009
* Add We;Na to artist split whitelist [PR #10329], by @1337joe
* Fix sed failing on Docker builds for CentOS/Fedora [PR #10285], by @DavidFair
* fix: use TryGetString to avoid crashing, fixes #10306 [PR #10308], by @cvium
* Update node versions [PR #10305], by @thornbill
* CollectionFolder: replace Dictionary + locks with ConcurrentDictionary [PR #10276], by @Bond-009
* Make startup script more portable [PR #10212], by @brianjmurrell
* Add missing LocalAccessOrRequiresElevationHandler [PR #10268], by @crobibero
* Downgrade SkiaSharp to prevent segfault [PR #10264], by @Bond-009
* Start adding IDisposableAnalyzers to projects [PR #10266], by @Bond-009
* Fully specify version tags for renovate [PR #10263], by @1337joe
* Downgrade SkiaSharp.NativeAssets.Linux to prevent segfault [PR #10257], by @Bond-009
* Extend collections cleanup task to include playlists too [PR #10234], by @Shadowghost
* Minor LibraryMonitor improvements [PR #10218], by @Bond-009
* fix: open the connection when using SqliteConnection directly [PR #10230], by @cvium
* Run collect script on failures [PR #10217], by @thornbill
* add auto-bump_version workflow [PR #6209], by @h1dden-da3m0n
* Avoid shell expansion issues [PR #10211], by @brianjmurrell
* Update Swashbuckle.AspNetCore.ReDoc to 6.5.0 [PR #10210], by @Bond-009
* Add program directories to JELLYFIN_ARGS for sysvinit compatibility [PR #10039], by @hugueslarrive
* Add a small Bash script to launch Jellyfin, instead of a symlink. [PR #10169], by @gandihar
* Enable nullable for more files [PR #10056], by @Bond-009
* Add global.json to specify dotnet version [PR #10207], by @crobibero
* Removed nesting levels through block-scoped `using` statement [PR #10025], by @Lehonti
* Fix typo in NetworkConfiguration.cs [PR #10190], by @eltociear
* Add new Spain content rating ERI [PR #10165], by @danimart1991
* refactor: use Microsoft.Data.Sqlite instead of SQLitePCL.pretty [PR #10138], by @cvium
* Use the correct trancode path [PR #10158], by @Bond-009
* Fix a few multiple enumerations [PR #10154], by @goremykin
* Enable nullable for more files and add tests [PR #10141], by @Bond-009
* Reduce log spam on failed logins [PR #10137], by @Bond-009
* Fix debian/ubuntu arm64 build error,runtime argument missing [PR #10139], by @FantasyGmm
* Reduce the amount of allocations in GetWhereClauses [PR #10114], by @Bond-009
* fix: accessing Standard* of a Process requires manually disposing them afterwards [PR #10125], by @cvium
* refactor: use ConcurrentDictionary when IMemoryCache isn't needed [PR #10122], by @cvium
* Album gain [PR #10085], by @TelepathicWalrus
* Fix French parental rating system [PR #10117], by @Elu43
* Add Slovak parental ratings [PR #10120], by @sambartik
* Fixes metadata refresh problems with NFO files [PR #10090], by @scampower3
* Fix subtitle encoder if webvtt is requested [PR #9669], by @sleepycatcoding
* Add parsing for dates with spaces [PR #10053], by @christianlegge
* Fix error in test preventing Moq update (#10096) [PR #10097], by @Bond-009
* Fix the probing of m4a metadata with missing composer [PR #10062], by @lonebyte
* Add support for more remote subtitle info [PR #10035], by @MBR-0001
* Fix album art extraction for multi-disc music albums [PR #10029], by @tallbl0nde
* Various improvements [PR #9875], by @Shadowghost
* Fix the is-local check when resetting the password [PR #10060], by @lonebyte
* Fix Jellyfin.Networking.Tests [PR #10055], by @Bond-009
* Add ability to upload (and save) SDH subtitles [PR #10036], by @MBR-0001
* Fix format normalizer for multiple input formats [PR #10049], by @Shadowghost
* Fix Australian parental rating system [PR #10006], by @Shadowghost
* Change: Add TinyMediaManager compatibility for german parental rating [PR #9992], by @Blackskyliner
* fix: set memorystream position after copying [PR #10022], by @cvium
* fix #9983 MigrateNetworkConfiguration error [PR #9987], by @Sky-High
* Extract networking constants [PR #9958], by @Shadowghost
* Use RegexGenerator where possible [PR #9799], by @Bond-009
* Augment tag searching to consider individual ItemValues instead of the delimited tags field [PR #8914], by @bradbeattie
* Rewrite NetworkManager and incorporate various fixes from open PRs [PR #8147], by @Shadowghost
* Fix sending websocket messages [PR #9948], by @crobibero
* Add a way to handle more invalid characters when sanitizing a filename [PR #9219], by @ProfessionalismIsMyMiddleName
* Disable real time monitoring by default [PR #9447], by @Bond-009
* Fix Websocket OpenApi [PR #9935], by @crobibero
* Added CleanupCollection task [PR #9231], by @JPVenson
* Migrate VideoRange and VideoRangeType to Enum [PR #9890], by @Shadowghost
* Do HEAD request to get content type instead of checking for extension [PR #8823], by @Bond-009
* Fixed RTL text not beeing rendered properly on Lib images [PR #9612], by @JPVenson
* chore(ci): add labels to docker images [PR #9210], by @candrews
* Don't ignore parentId for playlists [PR #9909], by @Bond-009
* Add default value to OpenAPI specification for UserPolicy.EnableCollectionManagement [PR #9933], by @nielsvanvelzen
* Update stylecop.analyzers to v1.2.0-beta.507 [PR #9915], by @Bond-009
* Reduce bottlenecks scan code [PR #9863], by @Bond-009
* Move hardcoded LibraryUpdateDuration to ServerConfiguration. [PR #9894], by @fhriley
* Use intermediate env for openapi workflow [PR #9906], by @crobibero
* Fix #9642 backport [PR #9902], by @nyanmisaka
* Add all websocket messages to generated openapi spec [PR #9682], by @crobibero
* Whitelist plugin dlls [PR #9564], by @AmbulantRex
* Implement NFO named season parsing [PR #8203], by @Shadowghost
* Fix InvalidOpEx while trying to read HttpResponseContent 2x [PR #9861], by @Bond-009
* Make LUFS property nullable in BaseItemDto [PR #9858], by @nielsvanvelzen
* Mock configuration to get SqliteCacheSizeKey during test [PR #9857], by @crobibero
* Increase journal_size_limit Defaults [PR #9667], by @Silvenga
* Source SQLite cache_size from an Environment Variable [PR #9666], by @Silvenga
* Fix TotalRecordCount calculation [PR #9818], by @Shadowghost
* Check for Imdb id for series [PR #9803], by @Bond-009
* Set removed and added tags recursively [PR #9771], by @Shadowghost
* Fix readonlyspan usage [PR #9775], by @crobibero
* Rescue malformed Xml response in DLNA PlayTo [PR #9759], by @seaeagle1
* Fix playlists library and migration [PR #9770], by @Shadowghost
* Fix access to playlists not created by a user [PR #9746], by @Shadowghost
* Happy Eyeballs (IP6 fallback to IP4) implementation of http client. [PR #8598], by @Neuheit
* Fix local JPG primary image for video being overwritten by screen grabber [PR #9552], by @SenorSmartyPants
* Remove ExtendedFileSystemInfo [PR #9749], by @Bond-009
* Fix MigrateRatingLevels [PR #9461], by @Shadowghost
* Fix pull request #9485 - scaleFactor limitation to 1 [PR #9738], by @olanwe
* Fix FirstTimeSetupHandler not failing on invalid user if not in setup mode [PR #9747], by @Shadowghost
* Whitelist Smith/Kotzen [PR #9729], by @1337joe
* sql connection pool [PR #9643], by @Bond-009
* Add artist to artist split whitelist [PR #9705], by @fuchsmich
* Add artist to artist split whitelist [PR #9659], by @pogmommy
* fix: dead link [PR #9626], by @brettpetch
* Fix null parental rating comparison [PR #9618], by @bradbeattie
* Update issue template to help HWA debugging [PR #9645], by @nyanmisaka
* Properly dispose prepared statements [PR #9635], by @Bond-009
* #7626 Added handling for common FormatExceptions with Skia loading sv… [PR #9581], by @JPVenson
* Fix analyzers warnings and suggestions [PR #9607], by @goremykin
* Augment similarity with person matches [PR #9613], by @bradbeattie
* Use minby and maxby [PR #9583], by @goremykin
* Implement check to hide all libraries when user has no access [PR #9536], by @elmuffo
* Fix migration for MusicBrainz [PR #9559], by @IDisposable
* Add action to close PRs with merge conflicts [PR #9561], by @thornbill
* Don't add .spc audio files (#9034) [PR #9545], by @Bond-009
* Fix item deletion with api key (#7610) [PR #9541], by @Bond-009
* Fix playlist creation and removal [PR #9466], by @Shadowghost
* Add merge conflict comment [PR #9529], by @thornbill
* Convert Person.Type to use PersonKind enum [PR #9487], by @crobibero
* Fix audio VBR calculation [PR #9522], by @knackebrot
* Extras: Clean filename and process NFOs [PR #9403], by @SenorSmartyPants
* Multiple HLS codec and bitrate fixes [PR #9388], by @Shadowghost
* Don't overwrite NFO images [PR #9452], by @SenorSmartyPants
* Fix pre-existing chapter images not being deleted [PR #9103], by @DarrenRuane
* Fix file stacking [PR #9496], by @mammo0
* Fix #9378 [PR #9505], by @Bond-009
* Update workflow actions to specify full version [PR #9502], by @1337joe
* Reduce usage of GetAwaiter().GetResult() [PR #9418], by @Bond-009
* Extend country code rating matching [PR #9460], by @Shadowghost
* Add config option to disable dummy chapter generation [PR #9410], by @Shadowghost
* Fall back to using "logo" attrib if "tvg-logo" is mssing in M3U-tuner [PR #9475], by @gitteric
* Add manual web builds [PR #9468], by @thornbill
* Save TVChannel Height if set [PR #8777], by @SenorSmartyPants
* Enable nullable for more files [PR #9449], by @Bond-009
* Fix DVD and BD folder playback [PR #9254], by @Shadowghost
* Audiobook grouping fixes [PR #9446], by @1337joe
* Ignore avg critic rating Rotten Tomatoes [PR #9448], by @Bond-009
* Allow webp for local images [PR #9454], by @Bond-009
* Reduce log spam [PR #9417], by @Bond-009
* Allocate fewer Lists [PR #9416], by @Bond-009
* Add SeasonProviderIds to EpisodeInfo [PR #9407], by @nalsai
* Fix auth endpoints using api key [PR #9408], by @crobibero
* Enable nullable for more files [PR #9397], by @Bond-009
* Catch Exception when disposing connection [PR #9326], by @ipitio
* Simplify audio transcode channel lookup [PR #9389], by @crobibero
* Enable nullable for more files [PR #9381], by @Bond-009
* Copy IsAutomated option when making MetadataRefreshOptions copy. [PR #9385], by @nicknsy
* Overhaul content rating handling [PR #8526], by @Shadowghost
* Fix #7516 [PR #9365], by @Bond-009
* Various fixes [PR #9361], by @Shadowghost
* Improve alternate ordering [PR #9336], by @Bond-009
* Optimize tryparse [PR #9356], by @Bond-009
* Various MusicBrainz fixes [PR #9352], by @Shadowghost
* Change transcoderChannelLimit default to 8 [PR #9266], by @holow29
* Enable nullable for more files [PR #9322], by @Bond-009
* Add rule and tests to fix  #9341 [PR #9343], by @Lenart12
* Fix MusicBrainz default server [PR #9349], by @Shadowghost
* Reduce string allocations by regex [PR #9337], by @Bond-009
* Fix use after dispose [PR #9340], by @Bond-009
* Validate requested user id [PR #8812], by @crobibero
* Verify ContentType of uploaded images [PR #9061], by @Bond-009
* Make exact match primary video [PR #9319], by @Bond-009
* Fix NRE in DisposeAsyncCore [PR #9320], by @MBR-0001
* Fix LocalAccessOrRequiresElevationHandler [PR #9315], by @Shadowghost
* Backport #9130 [PR #9160], by @Shadowghost
* Enable nullable for more files [PR #9310], by @Bond-009
* Fix #9300 [PR #9312], by @Bond-009
* Add permissions for collection management [PR #8887], by @Shadowghost
* Fix locked item metadata updates [PR #9306], by @1337joe
* refactor: simplify authz [PR #9282], by @cvium
* Fix error in XmlTvListingsProviderTests [PR #9302], by @Bond-009
* Always run code analyzers for tests projects [PR #9304], by @Bond-009
* Return NotFound when itemId isn't found [PR #9253], by @Bond-009
* LiveTV fixes [PR #9297], by @crobibero
* Remove .npmrc and nuget.config files [PR #9284], by @Bond-009
* Implement hardware filters for videotoolbox, use Apple AAC encoder when available [PR #7807], by @gnattu
* Use one AssemblyLoadContext per plugin [PR #9115], by @barronpm
* Fix backdrop image fetching to prioritize non-language images [PR #8982], by @bradbeattie
* Specify required movflags when encoding M4A audio [PR #9249], by @jmshrv
* Fix transcoded audio not playing [PR #9263], by @TelepathicWalrus
* Simplify CreateApplicationPaths [PR #9171], by @Bond-009
* fix: swap to `jellyfin-ffmpeg5` [PR #9256], by @brettpetch
* Migrate Jellyfin.Api to scoped namespace [PR #9215], by @Shadowghost
* Use Directory.Packages.props [PR #9135], by @zcsizmadia
* ApplicationHost cleanup [PR #9191], by @barronpm
* fix: require current password when admin changes their own password [PR #9238], by @cvium
* Fix audio codec not being used in UniversalAudio [PR #9192], by @jmshrv
* fix: don't allow exceptions to propagate from Refresh progress event handlers [PR #9228], by @cvium
* Improve ffprobe json parsing and don't log error for Codec Type attachment [PR #9227], by @Bond-009
* Add 404 response to MarkPlayedItem/MarkUnplayedItem [PR #9211], by @chrisb92
* Remove Emby.Notifications [PR #9147], by @barronpm
* Remove ability to add a played indicator to images [PR #9186], by @crobibero
* Add Phantom/Ghost to normalizer whitelist [PR #9180], by @lstrojny
* Remove restart.sh dependencies from packaging [PR #9164], by @ykgmfq
* Save modified userData after parsing an nfo [PR #9176], by @ProfessionalismIsMyMiddleName
* Simplify AlphanumericComparator [PR #9170], by @Bond-009
* Remove OS information from System Info [PR #9175], by @barronpm
* Remove CustomHeaderNames [PR #9143], by @barronpm
* Fix PGS position issue in Vulkan pipeline [PR #9146], by @nyanmisaka
* Minor improvements [PR #9156], by @Bond-009
* Fix debug builds [PR #9154], by @Bond-009
* Revert 'Fix interlace check for H.264 MBAFF coded MP4 files' (#6222) [PR #9126], by @Bond-009
* Change log level for bind address usage to debug [PR #9066], by @barronpm
* Remove DvdLib [PR #9068], by @barronpm
* Increase stale bot operations per run [PR #9133], by @Shadowghost
* Fix packaging to remove `restart.sh` script [PR #9124], by @Shadowghost
* EF Core Cleanup [PR #9108], by @barronpm
* Refactor Startup + Enable in-process restarting [PR #9100], by @barronpm
* Allow limiting parallel image encodings to reduce memory usage [PR #8783], by @hannesbraun
* Fine tune DB settings [PR #9044], by @Bond-009
* Fix client supported image formats [PR #9071], by @teobaranga
* Update test dependencies [PR #9094], by @barronpm
* Migrate to IHost [PR #9078], by @barronpm
* Fix all warnings in MediaBrowser.MediaEncoding [PR #9073], by @Bond-009
* Use file-scoped namespaces in Drawing projects [PR #9065], by @barronpm
* Add stereo downmix algorithm selection. [PR #9001], by @Shadowghost
* Fix all warnings in Jellyfin.Server.Implementations and MediaBrowser.Providers [PR #9070], by @Bond-009
* Rename Emby.Drawing and move to src [PR #9054], by @barronpm
* Move Jellyfin.Drawing.Skia to src [PR #9064], by @barronpm
* Add Chinese Bilingual language [PR #7623], by @MBR-0001
* Add dts to list of audio codecs which require ffmpeg strict -2 [PR #9029], by @DavidFair
* Fix recursive children lookup of folders [PR #8678], by @EgorBakanov
* Fixing similar parental rating calculation [PR #8959], by @bradbeattie
* Deduplicate media stream ordering code [PR #9014], by @Bond-009
* Use EventManager for AuthenticationSuccess, AuthenticationFailure [PR #8960], by @crobibero
* Fix all warnings in Jellyfin.Api [PR #9003], by @Bond-009
* Add jellyfin to the render and video groups for HWA [PR #9006], by @nyanmisaka
* Use nfo provided remote images on initial scan [PR #8995], by @daullmer
* DVR: Add options to disable NFO and image saving [PR #8775], by @SenorSmartyPants
* Give stale action write permission for issues [PR #8990], by @Bond-009
* Checkout common ancestor for comparison in OpenAPI workflow [PR #8985], by @nielsvanvelzen
* Add support for .sup subtitle [PR #8808], by @crobibero
* Use custom database healthcheck [PR #8973], by @crobibero
* Fix `multi` cleaning [PR #8978], by @Xavier-Do
* Cleanup and refactor streambuilder [PR #7494], by @Shadowghost
* Fix image searching to prioritize explicit language match if searching in English [PR #8946], by @bradbeattie
* Use Diacritics.NET [PR #8964], by @Bond-009
* Correct path to installation guide [PR #8948], by @mason-mcglothlin
* Use DistinctBy introduced in .NET 6 [PR #8922], by @Bond-009
* Adding "creation_time" as a tag lookup for FFProbe for premiere date [PR #8884], by @bradvolen
* Correct systemd dynamic directory [PR #8924], by @joshuaboniface
* Use Order() introduced in .NET 7 [PR #8923], by @Bond-009
* Default to no bitrate limit if no maxBitrate is set [PR #8850], by @Shadowghost
* Improve DB perf for everyone not using debug logging [PR #8827], by @Bond-009
* Use static methods StopWatch where it makes sense [PR #8898], by @Bond-009
* Fix debug builds [PR #8909], by @Bond-009
* Change log level for slow HTTP responses from WRN TO DBG [PR #8826], by @Bond-009
* Fix Windows FFmpeg download link [PR #8901], by @Shadowghost
* Add option to allow extras to use embedded titles [PR #7767], by @1337joe
* Augment search to consider tags [PR #8842], by @bradbeattie
* Fix fedora and centos nightly [PR #8875], by @Bond-009
* Fix nightly builds [PR #8870], by @Bond-009
* Remove dependency on OptimizedPriorityQueue [PR #8868], by @Bond-009
* Fix to make sure that UDF streams are opened with Share.Read (#8276) [PR #8867], by @stanionascu
* Always log when starting ffprobe [PR #8866], by @Bond-009
* Check HTTP status code before writing response to file [PR #8863], by @Bond-009
* feat: macOS arm64 build support [PR #8515], by @gnattu
* Use is and is not when comparing with null [PR #8511], by @Bond-009
* Add support for avif and webp for photos [PR #8857], by @f5xs-0000a
* Target .NET 7 [PR #8547], by @Bond-009
* Fix build [PR #8859], by @Bond-009
* Fix some warnings and only disable TreatWarningsAsErrors for CodeAnalysis [PR #8709], by @Bond-009
* Add support for OPUS and fixes for FLAC case issue in HLS [PR #8546], by @nyanmisaka
* Allow non-ASCII in downloaded filenames [PR #8825], by @potatodiet
* Add MusicBrainz server validation and fallback [PR #8833], by @Shadowghost
* Harden GitHub Workflows security [PR #8664], by @sashashura
* Add delay_moov flag for progressive mp4 transcoding [PR #8836], by @thornbill
* The -autoscale option was added in FFmpeg 4.4 [PR #8813], by @Bond-009
* Fix CI [PR #8824], by @Bond-009
* Offset API Played Indicator to correct position [PR #8819], by @photonconvergence
* Minor search update - full word titles matches first [PR #8757], by @SteveTheGrey
* Chapter Image settings(back-end): [PR #8137], by @negulici-r-barnabas
* Investigate some TODO comments [PR #8790], by @Bond-009
* Fix last CA1305 error [PR #8806], by @Bond-009
* Add missing format providers (fix CA1305 errors) [PR #8745], by @Terrance
* Providermanager cleanup [PR #7039], by @1337joe
* DVR: Prefer HD channels then earliest showing when handling duplicate showings. [PR #8768], by @SenorSmartyPants
* Sort external files when scanning [PR #8695], by @JeWe37
* Don't cancel DVR recordings when adjusting settings [PR #8752], by @SenorSmartyPants
* Don't auto-update if plugin is pending restart [PR #8727], by @crobibero
* Add xmldocs for TMDb provider, correct provider spelling [PR #7602], by @Shadowghost
* Change LocalizationOption for Traditional Chinese [PR #8737], by @TheBlueKingLP
* Fix integration tests [PR #8742], by @Bond-009
* remove JellyfinDbProvider and add second level caching [PR #8601], by @cvium
* Fix secondary audio [PR #8666], by @dmitrylyzo
* Add support for "Digital Media" album splits [PR #8713], by @trentks
* HDHomeRun - Fix incorrect starting offset of buffer span in CheckTunerAvailability. [PR #8726], by @swedishborgie
* Add regression test for #8696 [PR #8698], by @Bond-009
* Don't throw exception if program.Title is null [PR #8696], by @crobibero
* Fix URI creation in redirection middleware [PR #8551], by @Shadowghost
* Fix double assignment [PR #8670], by @jvitkauskas
* Clean up some unnecessary ToLists and deprecated function [PR #8618], by @j-griffiths
* Fix extra type differentiation [PR #8638], by @photonconvergence
* Fix Docker healthcheck output [PR #8529], by @jjlin
* Revert dependency updates to Azure Pipelines [PR #8627], by @crobibero
* Migrate MusicBrainz plugin to MetaBrainz.MusicBrainz [PR #7603], by @Shadowghost
* Prevent host lookup on GetSmartUrl for HTTP requests (master) [PR #8603], by @Shadowghost
* Rewrite BaseItem.ModifySortChunks [PR #8540], by @Bond-009
* Skip missing symlink instead of breaking out of directory scan [PR #8521], by @1337joe
* Add Vulkan filtering support for AMD VAAPI (Vega/gfx9+) [PR #7708], by @nyanmisaka
* Fix some things that slipped through the cracks [PR #8541], by @Bond-009
* Fix subtitle selection behaviour [PR #8472], by @j-griffiths
* Use System.IO.Compression instead of SharpCompress for gzips [PR #7840], by @adrez99
* Add extras with "Other" as a label [PR #8520], by @anthonylavado
* Skip generic shows from duplicate removal actions [PR #8370], by @abpei
* Update embedded image names to match docs [PR #8522], by @1337joe
* Remove r3 from clean strings [PR #8027], by @Bond-009
* Extend music parsing [PR #7514], by @Shadowghost
* Fix hearing impaired localization lookup [PR #8512], by @1337joe
* Update fuzzing projects to .net6 [PR #8510], by @Bond-009
* Redirect natively if no baseurl is set [PR #8408], by @Shadowghost
* Fix DLNA UpdateProfile test [PR #6751], by @Bond-009
* Use ArgumentNullException.ThrowIfNull helper method [PR #8503], by @Bond-009
* Fixed a few compiler warnings (#2149) [PR #8505], by @JJS
* fix: use HttpContext and ClaimsPrincipal instead of IAuthorizationContext [PR #8500], by @cvium
* Added handling of streams of type "data" [PR #8483], by @crobibero
* Remove redundant using directives [PR #8469], by @hannesbraun
* Remove LGTM badge [PR #8410], by @Bond-009
* Remove libraspberrypi0 package from arm Dockerfile [PR #8402], by @Bond-009
* Use record for AudioBookFilePathParserResult [PR #8409], by @Bond-009
* Fix special features not being sorted [PR #8401], by @ZachPhelan
* Fix HTML for badges in README [PR #8407], by @hannesbraun
* Add Sweden, Finland and Norway content rating [PR #7846], by @hogenf
* Drop transitional package apt-transport-https [PR #5950], by @ypid
* Pass referer parameter to ffmpeg [PR #8144], by @joseph39
* Add more artists to '/' separator whitelist [PR #8386], by @justjakka
* Don't allow throwing System.Exception [PR #8378], by @Bond-009
* Require properly typed ActionResult<T> [PR #8382], by @crobibero
* Add A/T/O/S to '/' separator whitelist [PR #8384], by @justjakka
* Make Password Reset case sensitive [PR #8377], by @Bond-009
* Fixes for FFProbe Keyframe extraction [PR #8335], by @eglia
* Minor cleanup [PR #8250], by @Bond-009
* Simplify UniversalAudioController code, remove redundant null checks [PR #8359], by @nielsvanvelzen
* Fix musl publish command [PR #8376], by @crobibero
* Fix musl build permissions [PR #8375], by @crobibero
* Use Guid type for UserConfiguration fields [PR #8325], by @nielsvanvelzen
* Add musl-linux-arm64 support [PR #8112], by @JinYi-Tsinghua
* Fix QuickConnect operation names [PR #8360], by @nielsvanvelzen
* JELLYFIN_NOWEBAPP_OPT is now --nowebclient [PR #8313], by @brianjmurrell
* Fix regression in DlnaHttpClient [PR #8300], by @Bond-009
* Rework SsdpHttpClient [PR #7433], by @Bond-009
* Fix various typos [PR #8267], by @luzpaz
* Make IgnoreDts configurable for M3U tuner [PR #7903], by @knackebrot
* don't require a user id for items api call using api key [PR #7965], by @jasongdove
* Fix operation name in SearchController and correct nullability for SearchHint [PR #8279], by @nielsvanvelzen
* fix: single video folder during photos lib scan [PR #7845], by @utkuozdemir
* Increase (really) timeout for subtitle extraction to 30min [PR #8259], by @RealGreenDragon
* Use guid for adjacentTo API parameter [PR #8261], by @nielsvanvelzen
* Jellyfin 10.9.0 [PR #8118], by @crobibero
* Use guid for seriesId API parameter [PR #8262], by @nielsvanvelzen
* Move transcodes to be under CachePath [PR #8107], by @candrews
* Add escape hatch for Series merging [PR #8008], by @revam
* Fix yuvj420p pixel format hardware decoding [PR #8001], by @nyanmisaka
* Fix the broken transcoding throttler [PR #7994], by @nyanmisaka
* Catch external streams exceptions [PR #7988], by @nyanmisaka
* Upgrade to dotnet 6.0.6, update remaining dependencies [PR #7984], by @crobibero
* Override the VAAPI driver env if i965 device is known [PR #7975], by @nyanmisaka
* Fix HWA decoders are not applied to BluRay folders [PR #7968], by @nyanmisaka
* Fix subtitle encoder if subrip is requested [PR #7960], by @Shadowghost
* Fix output extension if user has no transcoding permission [PR #7955], by @nyanmisaka
* Add DoVi side data parsing [PR #7964], by @nyanmisaka
* fix: use proper bind address for DLNA location url (#7953) [PR #7954], by @cvium
* Brighter VPP tone-mapping on Intel [PR #7950], by @nyanmisaka
* Add VideoRangeType to video conditions [PR #7947], by @nyanmisaka
* feat: partially handle SVG files and remove exceptions from blurhash and dimensions [PR #7946], by @cvium
* Fix the int overflow issue and the wrong map index of external audio [PR #7941], by @nyanmisaka
* Fix recommendations [PR #7940], by @Shadowghost
* Move service hardening options to override config [PR #7887], by @joshuaboniface
* Rework Fedora build [PR #7614], by @mihawk90
* Fix splashscreen [PR #7895], by @crobibero
* Enable XmlReaderSettings.Async, fixes #7929 [PR #7934], by @Bond-009
* Remove MPEG4 hwaccel from AMF [PR #7925], by @nyanmisaka
* Improve AMF tonemap speed when using sw decoding [PR #7924], by @nyanmisaka
* fix: read configuration during Invoke instead of during construction [PR #7913], by @cvium
* fix: only use keyframes when remuxing video [PR #7911], by @cvium
* Switch to FirstOrDefault extension [PR #7894], by @crobibero
* fix: tv shows do not support multi edition [PR #7892], by @cvium
* Prevent 400 error when using navigation buttons. [PR #7885], by @iwalton3
* fix: respect the image refresh options when parsing remote images from NFO [PR #7873], by @cvium
* Add tests for preferred audio language selection [PR #7682], by @1337joe
* chore: disable DLNA by default [PR #7868], by @cvium
* Don't add `MigrationOptions` to the api spec [PR #7867], by @crobibero
* chore: enable on demand keyframe extraction for mkv [PR #7854], by @cvium
* Fix Dolby Vision profile 5 and 8 to SDR HW tone-mapping [PR #7828], by @nyanmisaka
* Fix the PNG image decoding issue in Skia [PR #7852], by @nyanmisaka
* Backport all dependency updates [PR #7842], by @crobibero
* IAsyncDisposable is one big pitfall [PR #7810], by @Bond-009
* Exclude streams with mismatched types in external files [PR #7802], by @nyanmisaka
* Fix closing livetv stream on session end [PR #7781], by @crobibero
* Conditionally include platform specific Skia assets [PR #7792], by @crobibero
* Clear TranscodingInfo if play method changed [PR #7785], by @dmitrylyzo
* Enable SupportsTranscoding if device has transcoding profiles [PR #7784], by @crobibero
* Support searching with tv program filters [PR #7780], by @1337joe
* Manually describe Version for openapi [PR #7775], by @crobibero
* Fix to allow for episode numbering over 999 in certain scenarios [PR #7741], by @LewkyB
* Fix the mismatched resolution in sw PGS burn-in [PR #7736], by @nyanmisaka
* Don't let permission denied kill library scans [PR #7724], by @jtcasper
* Populate authentication info with server details if using API key [PR #7774], by @crobibero
* Update to dotnet 6.0.5 [PR #7766], by @crobibero
* fix: disable "Automatically add to collection" by default [PR #7749], by @cvium
* Update TMDbLib to 1.9.2 [PR #7723], by @crobibero
* Fix the disordered color in Dolby Vision remuxing on Safari [PR #7718], by @nyanmisaka
* Fix the issue that HEVC transcoding can't be disabled [PR #7712], by @nyanmisaka
* Respect limited opus sampling rates when building trancoding command [PR #7716], by @Shadowghost
* Fix streambuilder reasons for direct playback checks [PR #7699], by @Shadowghost
* Don't migrate auth token if user doesn't exist [PR #7693], by @crobibero
* Fixes diacritics regression #7484 #7450 #7560 [PR #7604], by @Jellifi007
* Fix DVR error: too long filename [PR #7544], by @jaantaponen
* Fix Matrix badge link to space instead of community [PR #7744], by @n-peugnet
* Properly handle stream addition and removal for strm use cases [PR #7529], by @Shadowghost
* Prefer MetadataProvider enum as provider id key over arbitrary strings [PR #7654], by @Shadowghost
* Add libssl3 as an alternative dependency for Ubuntu 22.04 LTS [PR #7648], by @nyanmisaka
* Fix H264 level on safari fmp4 [PR #7643], by @nyanmisaka
* Fix quick connect tests [PR #7638], by @1337joe
* Only delete xmltv cache file if exist [PR #7625], by @crobibero
* Correct LocalTrailerCount in API [PR #7634], by @neilsb
* Fix xmltv caching part 2 [PR #7592], by @1337joe
* Add missing properties to PlaybackStart, PlaybackStop [PR #7605], by @crobibero
* Update Jellyfin.XmlTv to 10.8.0 [PR #7591], by @1337joe
* Fix the wrong external audio map index if text subtitle exists [PR #7580], by @nyanmisaka
* Update to dotnet 6.0.4 [PR #7590], by @crobibero
* Remove mp2 from video file extensions [PR #7578], by @Shadowghost
* Require elevation to save list of plugin repositories [PR #7569], by @crobibero
* Fix NamedConfiguration API Generation [PR #7561], by @DMouse10462
* Fix xmltv caching [PR #7567], by @cvium
* Write UTC Date to .nfo files [PR #7543], by @daullmer
* Fix StreamBuilder [PR #7537], by @dmitrylyzo
* Add fallback for image downloads with bad reported MediaType [PR #7521], by @1337joe
* Optimize GetMD5 function [PR #7575], by @Bond-009
* Fix PGS burn-in on certain iGPU such as Iris Plus 655 [PR #7557], by @nyanmisaka
* fix: remove (incorrect) negation of bool expression [PR #7551], by @cvium
* fix: use IPAddress.IsLoopback instead of custom [PR #7549], by @cvium
* Fix album index sorts [PR #7548], by @1337joe
* Make recording stop at scheduled stop time [PR #7542], by @1337joe
* Remove video file from file list before processing external files [PR #7527], by @Shadowghost
* Fix media path saving to wrong library when name duplicated [PR #7525], by @1337joe
* Allow media without streams to playback [PR #7523], by @crobibero
* Fix StudioImageProvider [PR #7507], by @crobibero
* Catch checksum mismatch when updating plugins [PR #7512], by @crobibero
* Safely get/set User permission/preference [PR #7506], by @crobibero
* Add 10.8.0 to issue template [PR #7513], by @1337joe

## 10.8.13 – 2023-11-29

# Jellyfin 10.8.13

Stable hotfix release for 10.8.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* **NOTICE:** The customizable FFmpeg binary path in the WebUI/API has been REMOVED for security reasons. Please see [the corresponding blog post here](https://jellyfin.org/posts/jellyfin-security-and-you) for further details.

This bugfix release contains two GHSA security fixes; the details of these vulnerabilities **will be released publicly on December 5th 2023**. Please ensure you update your systems as soon as possible. Credit to @Kwstubbs (of GitHub Security Labs), @FredericLinn, and @mawalu for finding these.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/29

### [jellyfin](https://github.com/jellyfin/jellyfin) [3]

Note: Dependabot & Renovate automatic PRs are excluded from this list.

 * #10625 [@ilovepilav] Fix: Plugin Installed Alerts missing from Admin Dashboard #10620
 * [GHSA-rr9h-w522-cvmr](https://github.com/jellyfin/jellyfin/security/advisories/GHSA-rr9h-w522-cvmr) [@joshuaboniface] Remove the functionality of /System/MediaEncoder/Path
 * [GHSA-866x-wj5j-2vf4](https://github.com/jellyfin/jellyfin/security/advisories/GHSA-866x-wj5j-2vf4) [@crobibero] Validate codec and container

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [3]

Note: Dependabot & Renovate automatic PRs are excluded from this list.

 * jellyfin/jellyfin-web#5019 [@joshuaboniface] Set FFmpeg path disabled
 * jellyfin/jellyfin-web#4993 [@rafma0] Remove FLAC Audio in Video Support for Tizen (Backport #4938)
 * jellyfin/jellyfin-web#4992 [@rafma0] Fix jittering in emby-checkbox (Backport #4929)

## 10.8.12 – 2023-11-05

# Jellyfin 10.8.12

Stable hotfix release for 10.8.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

N/A

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/29

### [jellyfin](https://github.com/jellyfin/jellyfin) [5]

Note: Dependabot & Renovate automatic PRs are excluded from this list.

 * #10528 [@nyanmisaka] Fix mismatched intel VAAPI UMD/KMD - Backport #10451
 * ~~#10514 [@Bond-009] Update SkiaSharp (v2.88.6) and BlurHashSharp (v1.3.1)~~ Reverted due to SEGV on access
 * #10487 [@thornbill] Fix scaleFactor limit - Backport #9738
 * #10454 [@Shadowghost]  Add MALLOC_TRIM_THRESHOLD_ to default ENV
 * #10406 [@thornbill] Fix playlist listings

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [6]

Note: Dependabot & Renovate automatic PRs are excluded from this list.

 * jellyfin/jellyfin-web#4912 [@dmitrylyzo] Fix imports
 * jellyfin/jellyfin-web#4893 [@thornbill] Change Subtitle Sync slider to go from -300 to 300 - Backport  jellyfin/jellyfin-web#4754
 * jellyfin/jellyfin-web#4892 [@thornbill] Fix language/subtitle switcher when using gamepad - Backport  jellyfin/jellyfin-web#4860
 * jellyfin/jellyfin-web#4837 [@dmitrylyzo] Fix playing empty item set
 * jellyfin/jellyfin-web#4813 [@dmitrylyzo] Handle pressing Enter to finish keyboard dragging of slider (Backport  jellyfin/jellyfin-web#4805)
 * jellyfin/jellyfin-web#4797 [@Mauroq] Remove H264 10bit support on Samsung TV (Tizen)

## 10.8.11 – 2023-09-24

# Jellyfin 10.8.11

Stable hotfix release for 10.8.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

N/A

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/29

### [jellyfin](https://github.com/jellyfin/jellyfin) [6]

Note: Dependabot automatic PRs are excluded from this list.

 * #9952 [@Bond-009] Backport fix for #9503
 * #9928 [@nyanmisaka] Disable global_header on AMD VA-API encoder
 * #9916 [@Bond-009] Don't ignore parentId for playlists (backport #9909)
 * #9723 [@dmitrylyzo] Fix multiple codec checking in CodecProfiles conditions
 * #10265 [@Shadowghost] Backport #10173
 * #10151 [@nyanmisaka] Fix performance loss of QSV HDR tone-mapping on Windows

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [14]

Note: Dependabot automatic PRs are excluded from this list.

 * jellyfin/jellyfin-web#4758 [@dmitrylyzo] Fix slider step
 * jellyfin/jellyfin-web#4757 [@dmitrylyzo] Remove Dolby Vision support on Samsung TV (Tizen)
 * jellyfin/jellyfin-web#4709 [@thornbill] Fix scheduled task time limit key
 * jellyfin/jellyfin-web#4688 [@dmitrylyzo] Disable ALAC on MacOS in non-Safari browsers
 * jellyfin/jellyfin-web#4685 [@hurani] Backport pull request #4171 to release 10.8.z
 * jellyfin/jellyfin-web#4657 [@thornbill] Fix xss in custom subtitles element
 * jellyfin/jellyfin-web#4654 [@joshuaboniface] Add confirmation for 3rd party repos
 * jellyfin/jellyfin-web#4632 [@dmitrylyzo] Improve keyboard control
 * jellyfin/jellyfin-web#4628 [@dmitrylyzo] Fix initial state of volume slider
 * jellyfin/jellyfin-web#4627 [@dmitrylyzo] Fix overlap of slider bubble
 * jellyfin/jellyfin-web#4591 [@thornbill] Fix QuickConnect code not displaying in Spanish
 * jellyfin/jellyfin-web#4589 [@thornbill] Fix xss in api key page
 * jellyfin/jellyfin-web#4561 [@dmitrylyzo] Fix bottom video controls don't auto-hide
 * jellyfin/jellyfin-web#4553 [@dmitrylyzo] Unhide PlayNextEpisodeAutomatically on TV

## 10.8.10 – 2023-04-23

# Jellyfin 10.8.10

Stable hotfix release for 10.8.z release branch.

## New Features and Major Improvements

* CRITICAL SECURITY ADVISORY: [GHSA-9p5f-5x8v-x65m](https://github.com/jellyfin/jellyfin/security/advisories/GHSA-9p5f-5x8v-x65m) and [GHSA-89hp-h43h-r5pq](https://github.com/jellyfin/jellyfin-web/security/advisories/GHSA-89hp-h43h-r5pq) can be combined to allow remote code execution for *any authenticated Jellyfin user including non-admin users*. While the particular execution mechanism of the former dates to the 10.8.0 release, the latter was present for all Jellyfin releases before this point. It is thus absolutely critical for all Jellyfin administrators, regardless of version, to upgrade to this version if they allow any untrusted users and/or expose their instance to the Internet.

## Release Notes

N/A

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/29

### [jellyfin](https://github.com/jellyfin/jellyfin) [12]

Note: Dependabot automatic PRs are excluded from this list.

 * [GHSA-9p5f-5x8v-x65m](https://github.com/jellyfin/jellyfin/security/advisories/GHSA-9p5f-5x8v-x65m) [@daullmer] Throw exception on path traversal in WriteDocumentAsync
 * #9671 [@nyanmisaka] Fix the canvas size for DVBSUB and DVDSUB subtitles
 * #9642 [@nyanmisaka] Fix the brightness of VPP tonemap and add the tonemap mode
 * #9538 [@TheTyrius] Fix nvenc preset order
 * #9430 [@nyanmisaka] Fix Live TV hardware decoding
 * #9422 [@nyanmisaka] Fix stream map when using filter_complex with unlabeled output
 * #9411 [@nyanmisaka] Fix codec checking in CodecProfiles conditions
 * #9409 [@Shadowghost] Multiple HLS codec and bitrate fixes (10.8.z)
 * #9391 [@nyanmisaka] Fix H.264 baseline hwaccel and enable enhanced Nvdec by default
 * #9355 [@nyanmisaka] Some VAAPI VPP and OpenCL fixes
 * #9351 [@Shadowghost] Fix EqualsAny condition check for int and double

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [11]

Note: Dependabot automatic PRs are excluded from this list.

 * [GHSA-89hp-h43h-r5pq](https://github.com/jellyfin/jellyfin-web/security/advisories/GHSA-89hp-h43h-r5pq) [@iwalton3] Escape device id in raw HTML
 * jellyfin/jellyfin-web#4492 [@nyanmisaka] Add the tonemap mode options
 * jellyfin/jellyfin-web#4487 [@thornbill] Fix dead documentation link
 * jellyfin/jellyfin-web#4395 [@thornbill] Fix installed plugin version html
 * jellyfin/jellyfin-web#4385 [@nyanmisaka] Drop progressive transcoding in web client
 * jellyfin/jellyfin-web#4362 [@dmitrylyzo] Fix subtitle offset reset when seeking progressive stream
 * jellyfin/jellyfin-web#4356 [@dmitrylyzo] Babelify @jellyfin/libass-wasm
 * jellyfin/jellyfin-web#4330 [@dmitrylyzo] Fix navigation for some types of INPUT
 * jellyfin/jellyfin-web#4312 [@dmitrylyzo] Backport PR #4150 to 10.8.z branch
 * jellyfin/jellyfin-web#4310 [@jsayol] Backport PR #4147 to 10.8.z branch

## 10.8.9 – 2023-01-22

# Jellyfin 10.8.9

Stable hotfix release for 10.8.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

N/A

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/29

### [jellyfin](https://github.com/jellyfin/jellyfin) [10]

Note: Dependabot automatic PRs are excluded from this list.

 * #9145 [@nyanmisaka] Fix PGS position issue in sw decoding #8602
 * #9130 [@Shadowghost] Fix API access permissions for LiveTV and downloads
 * #9112 [@nyanmisaka] Backport the ffmpeg link fix (#8901) to 10.8.z
 * #9092 [@dmitrylyzo] Don't add additional entries if HEVC encoding is disabled                                                                                                                                                               
 * #9060 [@thornbill] Disable splash screen image by default
 * #9051 [@dmitrylyzo] Fix transcode reasons
 * #9050 [@nyanmisaka] Update workaround for i915 hang in linux 5.18 to 6.1.3
 * #9049 [@Shadowghost] Add more codecs requiring ffmpeg strict -2
 * #9020 [@Bond-009] Backport 8726: Fix incorrect starting offset of buffer span in CheckTunerAvailability
 * #9009 [@dmitrylyzo] Fix secondary audio

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [9]

Note: Dependabot automatic PRs are excluded from this list.

 * jellyfin/jellyfin-web#4288 [@dmitrylyzo] Fix loading Spanish (Latin America) (es-419)
 * jellyfin/jellyfin-web#4274 [@dmitrylyzo] Fix back action on Hisense TV
 * jellyfin/jellyfin-web#4269 [@thornbill] Fix XSS vulnerability in plugin repo pages
 * jellyfin/jellyfin-web#4267 [@dmitrylyzo] Fix AudioContext limit exceeded
 * jellyfin/jellyfin-web#4263 [@dmitrylyzo] Fix change audio track
 * jellyfin/jellyfin-web#4243 [@dmitrylyzo] Fix HTML escaping in MediaSession and on remote page
 * jellyfin/jellyfin-web#4240 [@dmitrylyzo] Fix detection of SecondaryAudio support
 * jellyfin/jellyfin-web#4238 [@thornbill] Fix XSS vulnerability in router
 * jellyfin/jellyfin-web#4182 [@nyanmisaka] Fix the progressive mp4 transcoding profile

## 10.8.8 – 2022-11-29

# Jellyfin 10.8.8

Stable hotfix release for 10.8.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

N/A

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/29

### [jellyfin](https://github.com/jellyfin/jellyfin) [1]

Note: Dependabot automatic PRs are excluded from this list.

 * #8753 [@thornbill] Fix items access backport

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [2]

Note: Dependabot automatic PRs are excluded from this list.

 * jellyfin/jellyfin-web#4172 [@thornbill] Fix item details banner image alignment
 * jellyfin/jellyfin-web#4166 [@dmitrylyzo] Fix keyboard navigation for INPUT and TEXTAREA

## 10.8.7 – 2022-11-01

# Jellyfin 10.8.7

Stable hotfix release for 10.8.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

N/A

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/29

### [jellyfin](https://github.com/jellyfin/jellyfin) [3]                                                               
                                                                                                                       
Note: Dependabot automatic PRs are excluded from this list.      
                                                                                                                       
 * #8667 [@daullmer] Enable OMDB plot for non-English languages as fallback
 * #8662 [@cvium] fix: use a combination of ParentIndexNumber and IndexNumber to determine next up episodes
 * #8649 [@nielsvanvelzen] Un-revert "Merge pull request #8298 from lomion0815/fix-data-stream"
                                                                                                                       
### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [0] 
                                                                                                                       
Note: Dependabot automatic PRs are excluded from this list.             
                                                                                                                       
N/A

## 10.8.6 – 2022-10-29

# Jellyfin 10.8.6

Stable hotfix release for 10.8.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

N/A

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/29

### [jellyfin](https://github.com/jellyfin/jellyfin) [12]

Note: Dependabot automatic PRs are excluded from this list.

 * #8620 [@nyanmisaka] Fix the DG2 HDR TM tearing issue on Windows
 * #8611 [@nielsvanvelzen] Fix TranscodeReasons type in OpenAPI output
 * #8609 [@anthonylavado] Use Token for SchedulesDirect Images and Image Index
 * #8608 [@cvium] Add index for DateCreated on ActivityLogs
 * #8600 [@Shadowghost] Prevent host lookup on GetSmartUrl for HTTP requests
 * #8523 [@Gylesie] Fallback only to the current time when marking item as watched
 * #8517 [@cvium] Backport #8335 to release-10.8.z
 * #8516 [@cvium] fix: kill ffprobe if keyframe parsing fails
 * #8501 [@cvium] fix: set MinIndexNumber for the next up query
 * #8499 [@cvium] chore: add Basque to the list of localization options
 * #8480 [@thornbill] Revert "Merge pull request #8298 from lomion0815/fix-data-stream"
 * #8411 [@Maxr1998] Allow direct play even if no audio stream is available

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [7]

Note: Dependabot automatic PRs are excluded from this list.

 * jellyfin/jellyfin-web#4117 [@thornbill] Backport PR #4094 to 10.8 release
 * jellyfin/jellyfin-web#4089 [@dmitrylyzo] Fix double escape HTML
 * jellyfin/jellyfin-web#4069 [@peterspenler] Fix images sometimes not un-blurring
 * jellyfin/jellyfin-web#4047 [@thornbill]  Change settings menu item name to "Euskara"
 * jellyfin/jellyfin-web#4039 [@thornbill] Fix card cropping on item details page
 * jellyfin/jellyfin-web#4005 [@dmitrylyzo] Fix locale with suffix
 * jellyfin/jellyfin-web#4004 [@cvium] chore: add Basque display language option

## 10.8.5 – 2022-09-25

# Jellyfin 10.8.5

Stable hotfix release for 10.8.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

N/A

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/29

### [jellyfin](https://github.com/jellyfin/jellyfin) [10]

Note: Dependabot & Renovate automatic PRs are excluded from this list.

 * #8433 [@crobibero] Update to dotnet 6.0.9
 * #8399 [@cvium] Respect visibility for people items (rebased)
 * #8348 [@cvium] Revert "Revert "refactor: use season number and episode number for NextUp ordering instead of SortName""
 * #8327 [@RealGreenDragon] Increased (really) subtitle extraction timeout to 30 min (10.8.z back-port)
 * #8321 [@strugee] Fix systemd not breaking whitespace in env vars
 * #8298 [@lomion0815] Added handling of streams of type "data"
 * #8280 [@thornbill] Fix ffmpeg analyze duration env var taking priority over media source
 * #8214 [@nielsvanvelzen] Make userId truly optional in UniversalAudioController
 * #8213 [@nyanmisaka] Fix high single thread usage in throttler
 * #8189 [@lukefor] Fix GetItems IndexOutOfRangeException when IDs do not exist

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [4]

Note: Dependabot & Renovate automatic PRs are excluded from this list.

 * jellyfin/jellyfin-web#3878 [@thornbill] Fix sdk imports to improve build size
 * jellyfin/jellyfin-web#3877 [@Callum17] Fix itemcontextmenu fails to update for items with no image metadata
 * jellyfin/jellyfin-web#3849 [@dmitrylyzo] Fix unexpected cursor hiding
 * jellyfin/jellyfin-web#3848 [@dmitrylyzo] Fix idle function call

## 10.8.4 – 2022-08-14

# Jellyfin 10.8.4

Stable hotfix release for 10.8.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

N/A

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/29

### [jellyfin](https://github.com/jellyfin/jellyfin) [6]

Note: Dependabot automatic PRs are excluded from this list.

 * #8257 [@joshuaboniface] Use separate args for dotnet publish commands
 * #8234 [@crobibero] update to dotnet 6.0.8
 * #8219 [@nyanmisaka] Move Fedora service hardening options to override config
 * #8212 [@SenorSmartyPants] Add resolution text for 384 sized video
 * #8209 [@Shadowghost] Fix series query including missing episodes when it should not
 * #8182 [@Shadowghost] Extract external subs from container before determining characterset

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [1]

Note: Dependabot automatic PRs are excluded from this list.

 * jellyfin/jellyfin-web#3789 [@thornbill] Fix XSS in card aria labels

## 10.8.3 – 2022-08-02

# Jellyfin 10.8.3

Stable hotfix release for 10.8.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* This version is identical to 10.8.2 except that PR #8087 has been reverted. This PR seemed to cause numerous issues when launching the homescreen or playing media as reported in #8198. The change will land again (with fixes to avoid the regression) in 10.8.4.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/29

### [jellyfin](https://github.com/jellyfin/jellyfin) [1]

Note: Dependabot automatic PRs are excluded from this list.

 * REVERT #8087 [@cvium] feat: make subtitleeditparser generic

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [0]

Note: Dependabot automatic PRs are excluded from this list.

## 10.8.2 – 2022-08-01

# Jellyfin 10.8.2

Stable hotfix release for 10.8.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

N/A

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/29

### [jellyfin](https://github.com/jellyfin/jellyfin) [16]

Note: Dependabot automatic PRs are excluded from this list.

 * #8191 [@cvium] fix: remove Virtual episodes when their physical counterpart exists
 * #8174 [@nyanmisaka] Disable auto inserted SW scaler for HW decoders
 * #8167 [@crobibero] Add back library scan from library manager
 * #8166 [@joseph39] Bind @userid only when it's in the statement
 * #8163 [@daullmer] Don't refresh playlists on album refresh
 * #8152 [@thornbill] Fix support for rtsp streams over tcp
 * #8127 [@nyanmisaka] Workaround for linux 5.18+ i915 hang at cost of performance
 * #8115 [@crobibero] Update to dotnet 6.0.7
 * #8104 [@Shadowghost] Add resolution text output for more resolutions
 * #8092 [@Andy2244] Change allow higher opus, vorbis transcode bitrates
 * #8087 [@cvium] feat: make subtitleeditparser generic
 * #8078 [@Andy2244] fix copy&paste error for requestedRangeTypes preventing stream copy
 * #8061 [@nyanmisaka] Fix intel dx11-ocl interop taking too long to initialize on windows
 * #8038 [@Shadowghost] Remove mount and unmount permissions for jellyfin group from sudoers
 * #8013 [@daullmer] Fix password change during parental control schedule
 * #7732 [@LewkyB] Fix to make web sockets close gracefully on server shutdown

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [7]

Note: Dependabot automatic PRs are excluded from this list.

 * jellyfin/jellyfin-web#3781 [@yahuli] Fix TypeError
 * jellyfin/jellyfin-web#3778 [@nielsvanvelzen] Add title and filename to download request in item details
 * jellyfin/jellyfin-web#3775 [@daullmer] Fix user specific remote access
 * jellyfin/jellyfin-web#3760 [@nielsvanvelzen] Fix saving log settings not working
 * jellyfin/jellyfin-web#3751 [@nielsvanvelzen] Fix splash screen checkbox always unchecked
 * jellyfin/jellyfin-web#3730 [@SenorSmartyPants] CardBuilder: Test episode number in addition to episode name
 * jellyfin/jellyfin-web#3729 [@SenorSmartyPants] Save series images under season, when browsing parent images for season

## 10.8.1 – 2022-06-27

# Jellyfin 10.8.1

Stable hotfix release for 10.8.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

N/A

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/29

### [jellyfin](https://github.com/jellyfin/jellyfin) [29]

Note: Dependabot automatic PRs are excluded from this list.

 * #8001 [@nyanmisaka] Fix yuvj420p pixel format hardware decoding
 * #7994 [@nyanmisaka] Fix the broken transcoding throttler
 * #7988 [@nyanmisaka] Catch external streams exceptions
 * #7985 [@crobibero] Revert "refactor: use season number and episode number for NextUp ordering instead of SortName"
 * #7984 [@crobibero] Upgrade to dotnet 6.0.6, update remaining dependencies
 * #7975 [@nyanmisaka] Override the VAAPI driver env if i965 device is known
 * #7968 [@nyanmisaka] Fix HWA decoders are not applied to BluRay folders
 * #7964 [@nyanmisaka] Add DoVi side data parsing
 * #7961 [@cvium] refactor: use season number and episode number for NextUp ordering instead of SortName
 * #7960 [@Shadowghost] Fix subtitle encoder if subrip is requested
 * #7955 [@nyanmisaka] Fix output extension if user has no transcoding permission
 * #7954 [@cvium] fix: use proper bind address for DLNA location url (#7953)
 * #7950 [@nyanmisaka] Brighter VPP tone-mapping on Intel
 * #7947 [@nyanmisaka] Add VideoRangeType to video conditions
 * #7946 [@cvium] feat: partially handle SVG files and remove exceptions from blurhash and dimensions
 * #7941 [@nyanmisaka] Fix the int overflow issue and the wrong map index of external audio
 * #7940 [@Shadowghost] Fix recommendations
 * #7939 [@1337joe] Track selector fix
 * #7934 [@Bond-009] Enable XmlReaderSettings.Async, fixes #7929
 * #7925 [@nyanmisaka] Remove MPEG4 hwaccel from AMF
 * #7924 [@nyanmisaka] Improve AMF tonemap speed when using sw decoding
 * #7913 [@cvium] fix: read configuration during Invoke instead of during construction
 * #7911 [@cvium] fix: only use keyframes when remuxing video
 * #7894 [@crobibero] Switch to FirstOrDefault extension
 * #7892 [@cvium] fix: tv shows do not support multi edition
 * #7887 [@joshuaboniface] Move service hardening options to override config
 * #7885 [@iwalton3] Prevent 400 error when using navigation buttons.
 * #7873 [@cvium] fix: respect the image refresh options when parsing remote images from NFO
 * #7614 [@mihawk90] Rework Fedora build

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [13]

Note: Dependabot automatic PRs are excluded from this list.

 * jellyfin/jellyfin-web#3724 [@samcon] Fix resume not working on LG WebOS
 * jellyfin/jellyfin-web#3722 [@nyanmisaka] Fix 6ch audio is disabled on AC3 supported browsers
 * jellyfin/jellyfin-web#3721 [@Shadowghost] Fix stream selection remembering
 * jellyfin/jellyfin-web#3720 [@Shadowghost] Fix device logos for various clients
 * jellyfin/jellyfin-web#3719 [@nyanmisaka] Expose DoVi metadata and VideoRangeType
 * jellyfin/jellyfin-web#3717 [@dmitrylyzo] Add maximum allowed video resolution selector
 * jellyfin/jellyfin-web#3716 [@Orhideous] Recognize MIME for transcoded audio in streams
 * jellyfin/jellyfin-web#3714 [@nyanmisaka] Expose VPP TM brightness/contrast gain options
 * jellyfin/jellyfin-web#3713 [@nyanmisaka] Add VideoRangeType condition for web client
 * jellyfin/jellyfin-web#3704 [@zhuangzhuang] Fix empty  avatar when upload same profile image
 * jellyfin/jellyfin-web#3701 [@nyanmisaka] Remove MPEG4 hwaccel from AMF
 * jellyfin/jellyfin-web#3694 [@crobibero] Add the ability to enable/disable the splashscreen
 * jellyfin/jellyfin-web#3571 [@mihawk90] Cleanup and standardise Fedora build (web)

## 10.8.0 – 2022-06-11

# Jellyfin 10.8.0

We're pleased to announce that 10.8.0 is now stable after over a year of effort. Congratulations to everyone who has participated.

GitHub project for release: https://github.com/orgs/jellyfin/projects/29

Binary assets: https://repo.jellyfin.org/releases/server

There is a lot in here, so please see the blog post here for a list of the big features and changes: https://jellyfin.org/posts/jellyfin-10-8-0/

## Full Changelog since 10.7.z

### [jellyfin](https://github.com/jellyfin/jellyfin) [662]

Note: Dependabot automatic PRs are excluded from this list.

 * #7868 [@cvium] chore: disable DLNA by default
 * #7867 [@crobibero] Don't add `MigrationOptions` to the api spec
 * #7854 [@cvium] chore: enable on demand keyframe extraction for mkv
 * #7852 [@nyanmisaka] Fix the PNG image decoding issue in Skia
 * #7842 [@crobibero] Backport all dependency updates
 * #7828 [@nyanmisaka] Fix Dolby Vision profile 5 and 8 to SDR HW tone-mapping
 * #7810 [@Bond-009] IAsyncDisposable is one big pitfall
 * #7802 [@nyanmisaka] Exclude streams with mismatched types in external files
 * #7792 [@crobibero] Conditionally include platform specific Skia assets
 * #7785 [@dmitrylyzo] Clear TranscodingInfo if play method changed
 * #7784 [@crobibero] Enable SupportsTranscoding if device has transcoding profiles
 * #7781 [@crobibero] Fix closing livetv stream on session end
 * #7780 [@1337joe] Support searching with tv program filters
 * #7775 [@crobibero] Manually describe Version for openapi
 * #7774 [@crobibero] Populate authentication info with server details if using API key
 * #7766 [@crobibero] Update to dotnet 6.0.5
 * #7749 [@cvium] fix: disable "Automatically add to collection" by default
 * #7741 [@LewkyB] Fix to allow for episode numbering over 999 in certain scenarios
 * #7736 [@nyanmisaka] Fix the mismatched resolution in sw PGS burn-in
 * #7724 [@jtcasper] Don't let permission denied kill library scans
 * #7723 [@crobibero] Update TMDbLib to 1.9.2
 * #7718 [@nyanmisaka] Fix the disordered color in Dolby Vision remuxing on Safari
 * #7716 [@Shadowghost] Respect limited opus sampling rates when building trancoding command
 * #7712 [@nyanmisaka] Fix the issue that HEVC transcoding can't be disabled
 * #7699 [@Shadowghost] Fix streambuilder reasons for direct playback checks
 * #7693 [@crobibero] Don't migrate auth token if user doesn't exist
 * #7654 [@Shadowghost] Prefer MetadataProvider enum as provider id key over arbitrary strings
 * #7648 [@nyanmisaka] Add libssl3 as an alternative dependency for Ubuntu 22.04 LTS
 * #7643 [@nyanmisaka] Fix H264 level on safari fmp4
 * #7638 [@1337joe] Fix quick connect tests
 * #7634 [@neilsb] Correct LocalTrailerCount in API
 * #7625 [@crobibero] Only delete xmltv cache file if exist
 * #7624 [@nielsvanvelzen] Enable Quick Connect by default
 * #7605 [@crobibero] Add missing properties to PlaybackStart, PlaybackStop
 * #7604 [@Jellifi007] Fixes diacritics regression #7484 #7450 #7560
 * #7592 [@1337joe] Fix xmltv caching part 2
 * #7591 [@1337joe] Update Jellyfin.XmlTv to 10.8.0
 * #7590 [@crobibero] Update to dotnet 6.0.4
 * #7580 [@nyanmisaka] Fix the wrong external audio map index if text subtitle exists
 * #7578 [@Shadowghost] Remove mp2 from video file extensions
 * #7569 [@crobibero] Require elevation to save list of plugin repositories
 * #7567 [@cvium] Fix xmltv caching
 * #7561 [@DMouse10462] Fix NamedConfiguration API Generation
 * #7557 [@nyanmisaka] Fix PGS burn-in on certain iGPU such as Iris Plus 655
 * #7551 [@cvium] fix: remove (incorrect) negation of bool expression
 * #7549 [@cvium] fix: use IPAddress.IsLoopback instead of custom
 * #7548 [@1337joe] Fix album index sorts
 * #7544 [@jaantaponen] Fix DVR error: too long filename
 * #7543 [@daullmer] Write UTC Date to .nfo files
 ** #7542 [@1337joe] Make recording stop at scheduled stop time
 * #7537 [@dmitrylyzo] Fix StreamBuilder
 * #7529 [@Shadowghost] Properly handle stream addition and removal for strm use cases
 * #7527 [@Shadowghost] Remove video file from file list before processing external files
 * #7525 [@1337joe] Fix media path saving to wrong library when name duplicated
 * #7523 [@crobibero] Allow media without streams to playback 
 * #7521 [@1337joe] Add fallback for image downloads with bad reported MediaType
 * #7519 [@nielsvanvelzen] Add new priority level to ResolverPriority for plugins
 * #7512 [@crobibero] Catch checksum mismatch when updating plugins
 * #7507 [@crobibero] Fix StudioImageProvider
 * #7506 [@crobibero] Safely get/set User permission/preference
 * #7496 [@crobibero] Fix TranscodeReasons property name
 * #7495 [@crobibero] Fix chmod entrypoint
 * #7493 [@Shadowghost] Fix DLNA DirectPlay
 * #7492 [@crobibero] Don't allow unknown sort-by
 * #7488 [@crobibero] Fix OpenAPI spec generation for TranscodeReason
 * #7487 [@InvoxiPlayGames] Change DLNA description requests to obey profiles, format UUID correctly
 * #7483 [@nyanmisaka] Improve fps for cuda tonemap in sw decoding
 * #7477 [@crobibero] Use requested bitrate for direct play calculations
 * #7476 [@crobibero] tmdb - update available series end status
 * #7474 [@nielsvanvelzen] Add missing authorization attributes
 * #7468 [@jakobkukla] Fix supportsTranscoding not reflecting user permissions sometimes
 * #7466 [@nyanmisaka] Prefer Cuvid to Nvdec by default for better performance
 * #7449 [@crobibero] Revert using Math.Clamp
 * #7448 [@nielsvanvelzen] Restrict item refreshing to administrators
 * #7445 [@Bond-009] BaseItem: remove unused functions
 * #7444 [@Bond-009] Add tests for BaseUrl normalization
 * #7443 [@whiteowl3] allow strm probe to succeed
 * #7441 [@1337joe] Add label for external audio/sub tracks
 * #7440 [@1337joe] Match external sub/audio stream adding logic
 * #7437 [@Nalsai] Add extracting attachments from external subs
 * #7435 [@nyanmisaka] Fix the fMP4 HLS audio sync issue on Safari
 * #7434 [@crobibero] Update to dotnet 6.0.3
 * #7432 [@Bond-009] SocketFactory: Remove redundant code
 * #7431 [@Bond-009] UdpServerEntryPoint: Fix typo
 * #7425 [@Bond-009] Remove none existing Australian rating
 * #7411 [@crobibero] Revert "chore: Add a read only connection for routes like Shows/NextUp"
 * #7410 [@MinecraftPlaye] Let the UI show which DTS profile is in use
 * #7406 [@crobibero] Fix build
 * #7405 [@StollD] Readd .strm as an allowed extension for videos
 * #7404 [@nyanmisaka] Remove the deprecated OMX and MMAL HWA
 * #7403 [@1337joe] Fix external file check for shorter names
 * #7397 [@nyanmisaka] Set the name of intel vaapi driver explicitly
 * #7396 [@thornbill] Update artwork repository urls
 * #7394 [@1337joe] Strip out external file fuzzy name matching
 * #7388 [@GermanCoding] Hide ISO 639-2 special codes in display titles
 * #7387 [@nyanmisaka] Lowering the VRAM usage on NVDEC decoder
 * #7386 [@nyanmisaka] Fix the path to the extracted fonts on Windows
 * #7383 [@thornbill] Include played and unplayed results in the same next up request
 * #7382 [@crobibero] Allow KeyframeExtractor to be localized
 * #7381 [@crobibero] Fix migration of DateTime to EF
 * #7380 [@crobibero] Add JsonConstructor to GeneralCommand
 * #7378 [@thornbill] Add resume book as default home section
 * #7376 [@GermanCoding] Remove superfluous "SoundHandler" from audio stream names
 * #7375 [@nyanmisaka] Update presets for NVENC encoder
 * #7374 [@nyanmisaka] Update intel compute runtime to 22.08.22549
 * #7370 [@crobibero] Only add internal files if the internal metadata path exists
 * #7369 [@Bond-009] Remove obsolete code for premium plugins
 * #7366 [@1337joe] Add post filtering for theme song and video
 * #7363 [@1337joe] Parse the unused chapter id field from ffmpeg output as a long
 * #7349 [@1337joe] Merge MediaInfoResolver subclass tests
 * #7346 [@Bond-009] Optimize Guid comparisons
 * #7338 [@mueslimak3r] fix HLS transcoding on android tv -- dont use -noaccurate_seek for hls transcode
 * #7333 [@eyezak] [Bugfix] Provile bitStreamArgs for HLS fMP4
 * #7332 [@eyezak] [Bugfix] Report transcoding complete
 * #7326 [@Bond-009] Remove some dead code
 * #7325 [@eyezak] Rework StreamBuilder to avoid unnecessary transcoding
 * #7324 [@Maxr1998] Implement Comparers for (Parent)IndexNumber
 * #7322 [@Bond-009] Clean up SqliteItemRepository
 * #7321 [@Bond-009] Fix some warnings
 * #7300 [@cvium] Change KeepReading to StopReading and use bytes read as an indicator
 * #7291 [@aolszowka] Fix h264_v4l2m2m acceleration in Raspberry Pi 4
 * #7290 [@crobibero] Update to dotnet 6.0.2
 * #7286 [@daullmer] NFO: fix thumb tags without aspect
 * #7275 [@Nalsai] Add extracting attachments for ffmpeg to burn subtitles with correct fonts
 * #7257 [@Shadowghost] Add some more artists to artist split whitelist
 * #7255 [@Shadowghost] Refactor and extend external subtitle and audio handling
 * #7245 [@h1dden-da3m0n] add stale issue check workflow
 * #7241 [@Bond-009] Flush to disk async where possible
 * #7240 [@jaysonsantos] chore: Add a read only connection for routes like Shows/NextUp
 * #7239 [@nielsvanvelzen] Use Guid for BaseItemDto parent ids
 * #7238 [@1337joe] Make ffprobe metadata merge consistent with MetadataService.MergeData
 * #7236 [@Bond-009] Always create TaskCompletionSource<T> with TaskCreationOptions.RunContinuationsAsynchronously
 * #7235 [@Bond-009] Ban the usage of Task.Result
 * #7234 [@nielsvanvelzen] Use Guid for BaseItemPerson.Id
 * #7233 [@Bond-009] Fix some warnings
 * #7225 [@crobibero] Properly populate QueryResult
 * #7221 [@SenorSmartyPants] UserView Thumbnail fixes
 * #7219 [@1337joe] Add TMDb logo handling
 * #7217 [@SenorSmartyPants] Generate cover image for music video type libraries.
 * #7203 [@1337joe] Fix resolving local alternates
 * #7202 [@knackebrot] Add option to change unix socket permissions
 * #7198 [@dmitrylyzo] Add TranscodingProfile conditions
 * #7197 [@dmitrylyzo] Fix maximum video resolution for dynamic HLS controller
 * #7186 [@1337joe] Order extra rules so directory takes precedence over naming
 * #7185 [@dmitrylyzo] Fix SA1642 warning
 * #7176 [@dmitrylyzo] Fix trailers duplication
 * #7175 [@dmitrylyzo] Ignore JSON serialization for special features of movie.
 * #7172 [@SenorSmartyPants] Config option to import season name from TMDB
 * #7141 [@nyanmisaka] Seek the external audio stream
 * #7138 [@nyanmisaka] Fix the wrong logic in HEVC VP9 10bit hwdec boxes
 * #7137 [@SenorSmartyPants] Remove special HTTP HEAD processing
 * #7136 [@1337joe] Fix stuck show library scans
 * #7134 [@adavier] Implement Trakt Episode Links
 * #7132 [@Bond-009] Update README.md
 * #7131 [@Bond-009] Fix warning SA1414 and CA1849
 * #7129 [@crobibero] VideoStream null handle
 * #7121 [@Bond-009] Error on SA1316
 * #7118 [@crobibero] Add null check for audio stream
 * #7115 [@joshuaboniface] Remove bump-version junk
 * #7112 [@stanionascu] Fix #7100 - when opening invalid UDF images
 * #7109 [@crobibero] Use provided SortOrder
 * #7107 [@Bond-009] Speed up Jellyfin.Naming.Tests
 * #7105 [@1337joe] Respect lock state when updating season 0 name
 * #7101 [@Bond-009] Remove incorrect mime type image/jpg
 * #7095 [@crobibero] Don't apply transformations to .gif 
 * #7093 [@ilaborde] Remove unnecessary ToList in DlnaManager
 * #7092 [@crobibero] Reverse all order-by
 * #7080 [@crobibero] Allow ApiKey query parameter for authentication
 * #7078 [@1337joe] Improve metadata merge for identify
 * #7076 [@crobibero] Add ability to search by -
 * #7075 [@crobibero] Fix orderby query
 * #7070 [@thornbill] Fix Fedora build version
 * #7059 [@crobibero] Fix device ordering
 * #7058 [@cvium] Use dedicated resolvers for extras
 * #7055 [@crobibero] Fix analysis issues
 * #7054 [@matthew-jones-uk] Add DisableEmbeddedSubtitles setting
 * #7052 [@crobibero] Add image/jpg to extension lookup
 * #7049 [@crobibero] Remove warnings
 * #7048 [@Bond-009] Update StyleCop
 * #7047 [@Bond-009] Fix build
 * #7044 [@1337joe] Fix trailers v2
 * #7042 [@crobibero] Fix build from PR merging
 * #7038 [@Bond-009] Fix option to disable server discovery
 * #7035 [@cvium] Force a remux/transcode with external audio files
 * #7034 [@cvium] Catch HttpRequestException when saving images from local provider
 * #7029 [@cvium] Use our own Contains extension
 * #7028 [@cvium] Fix extras folders
 * #7021 [@cvium] Use == instead of Object.Equals to avoid closure allocation
 * #7020 [@cvium] Use static lambdas
 * #7018 [@Bond-009] Remove unreachable branches from JsonConverters
 * #7017 [@crobibero] Fix query param spelling
 * #7015 [@Bond-009] Use System.IO.Compression instead of SharpCompress for zips
 * #7013 [@1337joe] Increment library name number instead of appending
 * #7012 [@nnnlog] Remove ProtectClock for hardware encoding
 * #7006 [@crobibero] Fix BaseItemKind Querying
 * #7005 [@1337joe] Deprecate LibraryOptions.EnableInternetProviders
 * #7004 [@Bond-009] General cleanup
 * #7002 [@crobibero] Update to dotnet 6.0.1
 * #7000 [@brianjmurrell] Fix build on EL7
 * #6998 [@1337joe] Fix crash on missing server config file
 * #6994 [@Tedyst] Fixed crash in MigrationRunner by checking migration for file existance
 * #6985 [@joshuaboniface] Improve and unharden systemd units for LXC and Fedora
 * #6980 [@brianjmurrell] Update RPM build for Ci autoversion packages
 * #6979 [@crobibero] Use BaseItemKind where possible
 * #6978 [@Bond-009] Add tests for ProbeResultNormalizer.GetFrameRate
 * #6977 [@Bond-009] Use correct jpeg MIME type
 * #6976 [@Bond-009] Don't check floats for equality
 * #6965 [@bendardenne] Add artist to '/' split whitelist
 * #6956 [@cvium] Refactor extras and movie multi-part parsing
 * #6953 [@matthiasdv] Add more hardening to systemd service
 * #6941 [@holahmeds] Use MimeTypes package to determine MIME type
 * #6936 [@cvium] Reduce allocations
 * #6934 [@nyanmisaka] HWA pipeline refactor, AMD/Intel/Nvidia full hardware filtering support, AV1 hwdec
 * #6929 [@Bond-009] Use JsonContent where possible
 * #6927 [@1337joe] Use SSL for tmdb images
 * #6923 [@cvium] Don't query series twice
 * #6920 [@marius-luca-87] Add an option for dropping specific subtitle formats using the DLNA SubtitleProfile
 * #6915 [@1337joe] Subtitle filename parsing fix
 * #6914 [@marius-luca-87] Take into account the streams dlnaheaders query parameter set by the DidlBuilder NormalizeDlnaMediaUrl function
 * #6912 [@crobibero] Add additional provider id parsing to file name
 * #6907 [@marius-luca-87] - enable seek function when direct streaming over DLNA
 * #6902 [@cvium] Migrate network configuration safely
 * #6900 [@ianjazz246] Use local time for RecordingHelperTests
 * #6898 [@jonas-resch] Add support for external audio files
 * #6890 [@crobibero] Fix creating DLNA profiles
 * #6879 [@crobibero] Remove ClientLog endpoints
 * #6874 [@1337joe] Expose TMDb image scale options to user
 * #6873 [@crobibero] Add ability to exclude active sessions from resumable items
 * #6871 [@cvium] Only force scheme and port when HTTPS is disallowed
 * #6870 [@cvium] Refactor omdb providers and fix issues
 * #6869 [@cvium] Small optimization to child count field
 * #6867 [@yresquirol] Related media according to genre
 * #6866 [@Bond-009] Remove task cancellation hacks
 * #6862 [@1337joe] Query media streams by type instead of filtering
 * #6860 [@cvium] Read past empty elements
 * #6857 [@Bond-009] Fix some warnings
 * #6856 [@cvium] Remove unused dependencies
 * #6854 [@1337joe] Add setter for CustomPrefs
 * #6852 [@Bond-009] Fix some warnings
 * #6851 [@cvium] Remove ILibraryManager as a dependency in resolvers etc.
 * #6850 [@PetrusZ] Add Collection Validator, create collection based on nfo
 * #6849 [@1337joe] Actually check server disabled metadata providers
 * #6848 [@marius-luca-87] Ensure the proper StartTimeTicks variable is forwarded to the AddDlnaHeaders function
 * #6845 [@marius-luca-87] Flush the XmlWriter before calling the StringBuilder ToString() method
 * #6841 [@joshuaboniface] Send SourceBranch to collect-server.azure.sh
 * #6838 [@crobibero] Add nullable dictionary openapi mapping
 * #6837 [@crobibero] Don't throw exception on unauthenticated requests
 * #6836 [@cvium] Very light cleanup in applicationhost
 * #6831 [@1337joe] Image provider cleanup
 * #6830 [@crobibero] Fix filtering images without dimensions
 * #6829 [@crobibero] Remove Obsolete attribute on enum
 * #6823 [@crobibero] Fix nullability on DisplayPreferencesDto
 * #6822 [@NickSica] Fix Ombi auth through Jellyfin
 * #6819 [@cvium] Try to use Width and Height from ImageInfo to determine aspect ratio
 * #6818 [@Bond-009] Replace PBKDF2-SHA1 with PBKDF2-SHA512
 * #6816 [@Bond-009] Fix some warnings
 * #6814 [@thornbill] Fix yaml format issue in issue template
 * #6813 [@Bond-009] Fix some warnings
 * #6808 [@cvium] Simplify and reduce LOC in ControlHandler
 * #6806 [@crobibero] Update to full dotnet 6
 * #6795 [@LinFor] Fix DLNA on older Samsung TVs
 * #6794 [@Bond-009] Remove some dead code
 * #6793 [@Bond-009] Add some docs and tests
 * #6792 [@Bond-009] Fix UnauthorizedAccessException in GetDrives
 * #6791 [@cvium] Load all types when checking plugin DLLs
 * #6784 [@nielsvanvelzen] Fix OpenAPI workflow fork cloning
 * #6783 [@1337joe] Deprecate ImageType.Screenshot and ItemFields.Screenshot
 * #6782 [@nielsvanvelzen] Fix OpenAPI workflow not working with pull requests from forks
 * #6781 [@1337joe] Add MaxCastMembers to TMDb Plugin Settings
 * #6778 [@jvoisin] Add a bit of hardening to the systemd service
 * #6777 [@ThibaultNocchi] Fix WebVTT region to spec
 * #6774 [@cvium] Make sure ReadToDescendant was successful before continuing
 * #6769 [@Bond-009] Remove unused IHasScreenshots interface
 * #6766 [@Bond-009] Minor improvements
 * #6765 [@zehnerGIT] Make tags import from TMDB configurable
 * #6764 [@zehnerGIT] Prevent log spam in StreamBuilder.cs
 * #6763 [@1337joe] Clean up duplicate TmdbImageProvider code
 * #6762 [@WWWesten] Add missing localization options
 * #6761 [@Bond-009] Streamline startup code
 * #6752 [@1337joe] Add Tests, Fix metadata refresh deletes backgrounds
 * #6748 [@ptalmeida] Add pt-pt as culture, fix localization typo
 * #6745 [@crobibero] Use correct id when finding existing dlna profile
 * #6740 [@zirdum] Corrected Unraid template link
 * #6737 [@Bond-009] Enable nullable for MediaBrowser.Providers
 * #6735 [@Bond-009] Enable nullable for more files
 * #6718 [@MBR-0001] Add IsAutomated property to SubtitleSearchRequest
 * #6695 [@crobibero] Update to dotnet6.rc2
 * #6689 [@1337joe] Expand video attached image extraction to support multiple images/types
 * #6681 [@dmitrylyzo] Add more sorting to Latest
 * #6680 [@MarcelCoding] Add Docker Healthcheck
 * #6678 [@Bond-009] Use new Random.Shared instead of creating new instances
 * #6677 [@Bond-009] Remove duplicate Fisher–Yates shuffle impl
 * #6676 [@Bond-009] Use static crypto rng
 * #6673 [@cvium] Return the path to the pinfile in forgot password
 * #6670 [@lyarenei] Update artist split whitelist
 * #6667 [@Bond-009] Fix the last few warnings
 * #6666 [@Bond-009] Fix issue #6123
 * #6665 [@Bond-009] Improve test coverage for QuickConnectManager
 * #6664 [@cvium] Queue refresh after subtitle upload and minor fixes
 * #6663 [@crobibero] Reference dotnet6-rc1 packages
 * #6656 [@daullmer] Change .vscode/launch.json to use .NET 6
 * #6651 [@KonH] Fix part of common warnings
 * #6649 [@barronpm] Fix Warnings in Emby.Server.Implementations (Part 2)
 * #6648 [@barronpm] Fix warnings in Emby.Server.Implementations (Part 1)
 * #6646 [@1337joe] Add test data and unit test for mp4 metadata probe
 * #6644 [@Bond-009] Enable nullable for ItemDataProvider
 * #6641 [@Bond-009] Use ConvertFrom with invariant culture instead of current culture
 * #6639 [@1337joe] Add mp4 track title fallback
 * #6631 [@GodTamIt] Update README for .NET version
 * #6629 [@crobibero] Disable DOTNET_SYSTEM_GLOBALIZATION_INVARIANT in docker images
 * #6627 [@Bond-009] Add regression test for #6560
 * #6618 [@crobibero] Create output directory when extracting archive files
 * #6616 [@crobibero] Remove all instances of en-US culture
 * #6614 [@Bond-009] Fix some warnings
 * #6613 [@Bond-009] Use RandomAccess instead of a FileStream where it makes sense
 * #6612 [@Bond-009] Remove sync FileStream hack
 * #6611 [@Bond-009] Fix user DB migration
 * #6600 [@cvium] Add first draft of keyframe extraction for Matroska
 * #6597 [@Bond-009] Add regression test for  #5323
 * #6596 [@crobibero] Add Jellyfin.Extensions to nuget package publish
 * #6593 [@Bond-009] ItemImageProvider: improve HTTP error handling
 * #6592 [@Bond-009] SsdpHttpClient: Ensure successful status code before reading response
 * #6590 [@Bond-009] Target net6.0
 * #6589 [@Bond-009] Validate ffmpeg path
 * #6588 [@Bond-009] Fix issue #6587
 * #6584 [@Bond-009] Specify DateTimeStyles when possible
 * #6582 [@Bond-009] Allow shutdown while starting WebHost
 * #6580 [@Artiume] Update Docker Image
 * #6571 [@Dixin] Fix extra folder name and type mapping.
 * #6569 [@crobibero] Update to dotnet 5.0.10
 * #6567 [@Bond-009] Reduce allocations
 * #6564 [@Bond-009] Fix Azure CI
 * #6563 [@Bond-009] Fix SubtitleEncoder and add regression tests
 * #6558 [@dmitrylyzo] Respond on request when ffmpeg fails
 * #6556 [@nielsvanvelzen] Use standard Authorization header in OpenAPI specification
 * #6553 [@ankenyr] Comparing PremiereDate when episode comparison would otherwise be equal.
 * #6551 [@MrChip53] Add ListingProviderInfo Id to XMLTV cache file name
 * #6546 [@ianjazz246] Use TheoryData instead of IEnumerable
 * #6544 [@cvium] Don't set ffmpeg path from null to its Display value
 * #6541 [@cvium] Read file length for symlinks,
 * #6538 [@cvium] Kill ProgressiveFileCopier and seek to end for ongoing livetv
 * #6535 [@Bond-009] Add tests for DlnaController
 * #6534 [@Bond-009] Fix some warnings
 * #6531 [@GodTamIt] Fix images "not loading" after manual identification
 * #6528 [@oledfish] Add "Production" and "TV" episode orders to the metadata editor.
 * #6526 [@Bond-009] Fix log message
 * #6523 [@cvium] Fix disposed exception when ffmpeg exits early in GetLiveHlsStream
 * #6522 [@ferferga] EFCore improvements and cleanups
 * #6521 [@ferferga] Fix Dockerfile typos
 * #6515 [@Maeur1] Update Intel Compute Runtime Resources
 * #6507 [@Artiume] Convert Issue Template to YAML
 * #6506 [@Artiume] Request FFmpeg version
 * #6502 [@crobibero] Add Jellyfin.Extensions to package publish
 * #6501 [@crobibero] Enable nullable for SchedulesDirect // Add Tests for SchedulesDirect
 * #6499 [@Bond-009] Fix some warnings
 * #6498 [@Bond-009] Fix InvalidOperationException when serializing MediaPathInfo
 * #6497 [@Bond-009] Add SqliteItemRepository.ItemImageInfoFromValueString as a fuzzing target
 * #6495 [@qsniyg] Allow zero activity log retention days
 * #6494 [@Bond-009] Clean up VideoImageProvider
 * #6492 [@Bond-009] Ignore Omnisharp crash logs
 * #6491 [@Bond-009] Fix build
 * #6486 [@fredriklindberg] Support forwarded headers for api url
 * #6485 [@markshark05] Update M3U Channel Name Precedence
 * #6475 [@crobibero] Remove more and more warnings
 * #6474 [@Bond-009] Add tests for LibraryStructureController
 * #6473 [@Bond-009] Enable nullable for more files
 * #6457 [@Izumiko] Add 'includeAdult' option for TheMovieDb
 * #6456 [@GodTamIt] Disambiguate vpx to vp8 or vp9
 * #6446 [@Deathspike] Fix embedded subtitles taking priority over external ones
 * #6445 [@cvium] Add timeout to ProgressiveFileStream
 * #6444 [@cvium] Use ProgressiveFileStream for LiveRecordings endpoint
 * #6436 [@daullmer] Add Splashscreen api endpoint
 * #6434 [@crobibero] Update Dockerfile to use debian:bullseye-slim
 * #6430 [@Bond-009] Minor improvements
 * #6429 [@crobibero] Update to dotnet 5.0.9
 * #6428 [@Bond-009] Fix PasswordHash tests
 * #6427 [@winterqt] Disable UseAppHost in portable deployment
 * #6425 [@boolemancer] Fix explicit stream selection in MediaEncoder.ExtractImageInternal
 * #6423 [@richlander] Fix warnings in MediaBrowser.Controller
 * #6422 [@daullmer] Add support for NFO fanart tag
 * #6414 [@richlander] Fix warnings in MediaBrowser.Controller/MediaEncoding directory
 * #6412 [@richlander] Fix warnings in MediaBrowser.Controller/Session
 * #6404 [@crobibero] Fix redirect logic if request path is exactly the base url
 * #6403 [@ankenyr] Adding tests for AiredEpisodeOrderComparer.
 * #6402 [@anthonylavado] Add sponsor links
 * #6397 [@MrChip53] Properly stream M3U file over http
 * #6394 [@h1dden-da3m0n] ci: change OS packaging images to be quiet
 * #6392 [@Bond-009] ApiServiceCollectionExtensions.AddProxyAddresses: Add more tests
 * #6388 [@Bond-009] Minor improvements
 * #6386 [@richlander] Fix warnings in MediaBrowser.Controller/LiveTv
 * #6383 [@sushilicious] Made default parser a tiny bit more robust
 * #6381 [@Bond-009] Enable nullable for DlnaManager
 * #6379 [@getupbuzz] Optimize episode parser
 * #6377 [@richlander] Optimize Dockerfiles
 * #6358 [@MrTimscampi] Enable people for audio files and add music probing test
 * #6355 [@Bond-009] EnsureLibraryFolder: Minor optimization
 * #6354 [@Bond-009] Enable nullable in more files
 * #6346 [@richlander] Fix warnings in MediaBrowser.Controller/Drawing
 * #6344 [@richlander] Update to .NET SDK 5.0.302
 * #6342 [@richlander] Fix warnings in MediaBrowser.Controller/Library
 * #6339 [@richlander] Fix partial set of MediaBrowser.Controller/Entities warnings
 * #6338 [@richlander] Fix warnings for MediaBrowser.Controller/Providers directory
 * #6336 [@richlander] Fix warning in MediaBrowser.Controllers/Channels
 * #6335 [@richlander] Fix MediaBrowsers.Providers analysis issues
 * #6329 [@Bond-009] Add tests for GetResolutionText
 * #6328 [@Bond-009] Improve episode parser
 * #6327 [@nyanmisaka] Add support for cuda tonemap and overlay
 * #6326 [@crobibero] Update to dotnet 5.0.8
 * #6308 [@nielsvanvelzen] Add OpenAPI workflow
 * #6304 [@Bond-009] Add h265 to CleanStrings
 * #6303 [@Artiume] update bug report to ask for hwaccel
 * #6300 [@thornbill] Update stalebot configuration
 * #6298 [@crobibero] Remove /MusicGenres/{id}/InstantMix endpoint
 * #6297 [@Bond-009] Fix episode parser
 * #6296 [@Bond-009] Improve platform checks
 * #6290 [@Bond-009] Remove old "has update available" code
 * #6289 [@Bond-009] Fix some warnings
 * #6283 [@natedawg] Fix spelling of artist K/DA in splitting whitelist
 * #6281 [@crobibero] Reduce warnings in MediaBrowser.Controller
 * #6280 [@MrTimscampi] Add more artist names to the splitting whitelist
 * #6279 [@Bond-009] Add tests for Playback/BitrateTest endpoint
 * #6276 [@crobibero] BitrateTest: Use ASP validation, increase maximum size.
 * #6268 [@Bond-009] Add test for RobotsRedirectionMiddleware
 * #6267 [@Bond-009] Minor fixes
 * #6262 [@MrTimscampi] Prefer original date when getting premiere date from ffprobe
 * #6258 [@gnuyent] Add hardware encoding status to playback data
 * #6257 [@MrTimscampi] Use artist backdrop for generated library image
 * #6256 [@MrTimscampi] Refactor GetResolutionText
 * #6240 [@Bond-009] Add tests for QuickConnectManager
 * #6239 [@jvoisin] Add a LGTM.com badge
 * #6236 [@Bond-009] Fix QuickConnect
 * #6233 [@Bond-009] MediaBrowser.Providers: Remove some warnings
 * #6222 [@orryverducci] Fix interlace check for H.264 MBAFF coded MP4 files
 * #6210 [@bellegarde-c] debian: Add maxcpucount option to override_dh_auto_build. Fix #5234
 * #6208 [@h1dden-da3m0n] disable project automation workflows in forks
 * #6204 [@Bond-009] Move non-jellyfin extensions to separate project
 * #6201 [@barronpm] Migrate Authentication DB to EF Core
 * #6200 [@nielsvanvelzen] Refactor Quick Connect
 * #6197 [@MrTimscampi] Document SubtitleDeliveryMethod
 * #6191 [@crobibero] Update to dotnet 5.0.7
 * #6183 [@stanionascu] Better detection of the ISO DVD/BD types
 * #6180 [@crobibero] Ignore Test Controllers
 * #6177 [@Bond-009] Use async FileStreams where it makes sense
 * #6176 [@nielsvanvelzen] Require userId in getItems and getTrailers endpoints
 * #6174 [@Bond-009] Remove our own RemoveDiacritcs string extension in favor of Diacritics.Net
 * #6173 [@Bond-009] Add test for ReadOnlySpan.Count extension
 * #6172 [@Bond-009] Remove useless nullable directives
 * #6165 [@Bond-009] Fix duplicate keys causing an exception
 * #6163 [@Bond-009] Fix index out of range and add reg tests
 * #6162 [@crobibero] Redirect to default if root is requested
 * #6156 [@Bond-009] Minor fixes
 * #6150 [@Bond-009] Add property based testing
 * #6137 [@ferferga] Refactor Github Actions
 * #6133 [@ferferga] Pull request target
 * #6121 [@Bond-009] Fix some warnings
 * #6117 [@LinFor] Add OriginalTitle to ItemLookupInfo
 * #6116 [@Maxr1998] Fix broken link in CONTRIBUTORS and add myself
 * #6115 [@Maxr1998] Refactor ProbeResultNormalizer
 * #6102 [@LinFor] Don't prefer OMDB rating over all other providers
 * #6096 [@cvium] Remove some unnecessary allocations
 * #6094 [@crobibero] Add sorting to /Artists/AlbumArtists
 * #6090 [@cvium] Bump SQLitePCL.pretty.netstandard to 3.0.1
 * #6089 [@BaronGreenback] Set UserRootFolder.IsRoot to true
 * #6086 [@Bond-009] Remove dead code
 * #6084 [@Bond-009] Enable nullable reference types for MediaBrowser.MediaEncoding
 * #6083 [@Bond-009] Enable nullable reference types for Emby.Server.Implementations
 * #6075 [@MrTimscampi] Properly detect Dolby Vision files derived from AV1, AVC and HEVC
 * #6074 [@Bond-009] Enable nullable for InternalItemsQuery
 * #6072 [@crobibero] Update to Dotnet 5.0.6 (Fixed)
 * #6071 [@BaronGreenback] Make DLNA folders to work as expected.
 * #6058 [@ferferga] Add FullNowPlayingQueue property to sessions endpoint
 * #6054 [@cvium] Reduce some allocations
 * #6051 [@Bond-009] Add tests for Recordinghelper
 * #6050 [@Bond-009] Fully disable stupid rules
 * #6047 [@crobibero] Update to Dotnet 5.0.6
 * #6042 [@crobibero] Reduce warnings in MediaBrowser.Controller (Part 2)
 * #6037 [@ferferga] Replace GH_TOKEN with JF_BOT_TOKEN
 * #6033 [@daullmer] Call TMDb Person API with metadata language
 * #6031 [@ferferga] Run SQLite query planner optimization at shutdown/restart
 * #6027 [@fredriklindberg] Improve series matching
 * #6026 [@daullmer] Use TMDb parental rating building from movies for shows
 * #6025 [@daullmer] Test LocalizationManager
 * #6013 [@Bond-009] Minor improvements
 * #6010 [@crobibero] Mooooove the label commenter config
 * #6009 [@nielsvanvelzen] Disable automation CI on issues
 * #6005 [@Bond-009] Enable nullable reference types for Emby.Dlna
 * #6000 [@Bond-009] Enable nullable reference types for MediaBrowser.Controller
 * #5999 [@Bond-009] Add support for legacy HDhomerun DUAl
 * #5997 [@JKI12] Fixes for Book Progress
 * #5995 [@tuky] Respect configured JELLYFIN_USER in Debian's postinst
 * #5990 [@BaronGreenback] Enable querystring to be encoded
 * #5988 [@Bond-009] Add fuzzing infrastructure
 * #5985 [@Bond-009] Minor improvements
 * #5984 [@Bond-009] Add regression test for ContainerProfile.ContainsContainer
 * #5982 [@Bond-009] Enable nullable reference types for MediaBrowser.Common
 * #5980 [@Maxr1998] Fix direct play for DirectPlayProfiles without any codecs set
 * #5979 [@daullmer] Add support for fanart aspect in thumb tag
 * #5975 [@thornbill] Fix web build in dockerfiles
 * #5973 [@crobibero] Kill the CI
 * #5956 [@BaronGreenback] Minor optimization.
 * #5955 [@Bond-009] Don't run integration tests in parallel
 * #5954 [@Bond-009] Add tests for SqliteItemRepository.(De)SerializeProviderIds
 * #5952 [@Bond-009] Add tests for SqliteItemRepository.(De)SerializeImages
 * #5946 [@Bond-009] TmdbUtils: Use ordinal string compare
 * #5945 [@Bond-009] Fix scanning
 * #5944 [@shortspider] Add ResumeBook Section
 * #5941 [@Maxr1998] Improve documentation for DeviceProfile
 * #5938 [@cvium] Reduce some allocations with the magic of spans etc.
 * #5934 [@Bond-009] SqliteItemRepository: Parse ChannelId directly from utf-8 data
 * #5929 [@crobibero] Add ability to sort on Genre, MusicGenre, Artist
 * #5918 [@crobibero] Add endpoint to log client events
 * #5905 [@BaronGreenback] Fix for Livetv and DLNA when bind interfaces specified.
 * #5894 [@brianjmurrell] Allow to bind to priveleged ports (i.e. 80/443)
 * #5893 [@Bond-009] SqliteItemRepository: remove redundant operations
 * #5892 [@crobibero] Mark password property as obsolete
 * #5891 [@Bond-009] ManagedFileSystem: Rewrite GetValidFilename and more improvements
 * #5890 [@Bond-009] Reduce string allocations/fs lookups in resolve code
 * #5889 [@Bond-009] Remove unused/duplicate services
 * #5887 [@Bond-009] Improve perf of db save and query
 * #5886 [@Artiume] Request all the logs
 * #5877 [@Bond-009] EncodingHelper: Fix circular dependency
 * #5876 [@Bond-009] DeepCopy: Throw ArgumentNullException if one of the args is null
 * #5867 [@Bond-009] ProviderManager: fix discard and 2 warnings
 * #5866 [@Bond-009] Switch from HttpClientHandler to SocketsHttpHandler
 * #5864 [@DeeJayBro] Fix ArgumentOutOfRangeException when getting PostedPlaybackInfo
 * #5843 [@BaronGreenback] Code Clean up: Remove unused using directives
 * #5842 [@BaronGreenback] Code Clean up: Group Methods
 * #5836 [@BaronGreenback] Code Clean up: "value assigned is not used in any execution path"
 * #5828 [@jackrvan] Add NextUpCutoffDate to NextUpQuery
 * #5807 [@Bond-009] Remove throttle in refresh code
 * #5806 [@Bond-009] Fix possible ArgumentNullException
 * #5803 [@crobibero] Properly redirect healthcheck endpoint if using BaseUrl
 * #5794 [@richlander] Remove coupling to distro
 * #5792 [@Bond-009] Fix possible ArgumentNullException
 * #5784 [@Bond-009] Fix random failing of tests
 * #5779 [@joshuaboniface] Add label commenter workflow
 * #5768 [@Bond-009] Add test for handling dangling symlinks
 * #5767 [@cvium] Do not touch "old" local artwork unless saving locally
 * #5766 [@cvium] Use sync Serialize when writing scheduled tasks to disk
 * #5763 [@Bond-009] Minor improvements to IPObjects
 * #5762 [@BaronGreenback] Fix network test on dns failure
 * #5759 [@Bond-009] Fix LogUnmatchedProfile formatting
 * #5755 [@BaronGreenback] Auth: Network Access Policy
 * #5744 [@mohd-akram] Add support for TMDB series absolute and DVD order
 * #5738 [@cvium] Resolve name from episode folder
 * #5731 [@Bond-009] Add tests for UserController
 * #5730 [@thornbill] Disable HEVC encoding by default
 * #5729 [@crobibero] Update to dotnet 5.0.5
 * #5721 [@Bond-009] Add code to test authenticated endpoints
 * #5713 [@Bond-009] Add tests for unauthenticated websocket access
 * #5708 [@Bond-009] Enable NetAnalyzers for more projects
 * #5707 [@ferferga] (jellyfin-web): Switch to npm
 * #5699 [@Bond-009] Add test for ProbeResultNormalizer.GetMediaInfo
 * #5697 [@Bond-009] Simplify the way we choose our ffmpeg
 * #5696 [@Maxr1998] Improve metadata probing to better support music videos
 * #5691 [@Bond-009] Fix possible nullref
 * #5685 [@Bond-009] Remove useless null check
 * #5681 [@BaronGreenback] Various DLNA Optimizations
 * #5676 [@Bond-009] Remove useless code
 * #5675 [@Bond-009] Add tests for CopyToExtensions
 * #5659 [@ssenart] [DLNA] [NextTrack] [Gapless] Fix 5644 and 5294
 * #5648 [@OancaAndrei] Fix session references in SyncPlay
 * #5637 [@dmitrylyzo] Check appropriate profile type
 * #5623 [@barronpm] EF Core Cleanup 2
 * #5614 [@Bond-009] Fix possible null ref exception
 * #5612 [@Bond-009] Rewrite PasswordHash.Parse to work with ReadOnlySpans
 * #5606 [@lmnotran] Delay starting service until after network is online
 * #5602 [@daullmer] Don't convert from IPAddress to string to IPAddress
 * #5598 [@cvium] change HLS endpoint defaults to false
 * #5586 [@nyanmisaka] Disable auto rotation for some HWA methods
 * #5580 [@Bond-009] Add StartupControllerTests
 * #5579 [@cocool97] Add 'group-title' channel parsing
 * #5561 [@barronpm] Fix duplicate permissions
 * #5522 [@Bond-009] Fix integration test project
 * #5520 [@Bond-009] Rewrite Rewrite HdHomerunManager.ParseReturnMessage and add tests
 * #5490 [@thornbill] Remove forum badge
 * #5467 [@daullmer] Nfo id parsing fixes
 * #5422 [@Bond-009] FxCop -> Net Analyzers (part 2)
 * #5417 [@Bond-009] Add code analysis attributes where appropriate
 * #5395 [@barronpm] Jellyfin.Data Cleanup Part 1
 * #5384 [@Larvitar] Do not apply search results on seasons
 * #5382 [@crobibero] Add JsonVersionConverter and tests
 * #5380 [@Bond-009] 100% branch coverage for DashboardController
 * #5362 [@crobibero] Fix case-sensitive json parsing
 * #5359 [@cvium] Do nothing in timer callback when device locator is disposed
 * #5354 [@shortspider] Update README to include ffmpeg
 * #5338 [@Bond-009] Remove tests that are upstreamed
 * #5336 [@Bond-009] Split integration tests from unit tests
 * #5321 [@daullmer] Add nfo thumb tag support
 * #5317 [@Bond-009] MaybeNullWhen(false) -> NotNullWhen(true)
 * #5314 [@barronpm] Remove unused entity
 * #5307 [@barronpm] Switch to Using Declarations in MediaBrowser.Providers
 * #5299 [@Bond-009] Improve branch coverage
 * #5291 [@Bond-009] Add tests for DashboardController
 * #5285 [@Bond-009] Update deps Jellyfin.Model.Tests
 * #5277 [@Bond-009] Add Jellyfin.Model.Tests project to the solution
 * #5276 [@Bond-009] Minor improvements
 * #5273 [@Bond-009] Enable TreatWarningsAsErrors for MediaBrowser.Model
 * #5253 [@Bond-009] Fix broken test
 * #5243 [@crobibero] Bump Swashbuckle.AspNetCore to 6.0.5
 * #5242 [@Bond-009] Properly forward cancellationTokens
 * #5235 [@daullmer] Add more nfo tests
 * #5228 [@lbenini] Fix BaseItemKind conversion for PlaylistsFolder
 * #5226 [@Bond-009] 100% branch coverage for Emby.Naming
 * #5223 [@Bond-009] Minor improvements
 * #5222 [@Bond-009] Don't enable case-insensitivity for json by default
 * #5220 [@Bond-009] Rewrite packet writing code for HdHomerun
 * #5218 [@dkanada] rename the solution file
 * #5213 [@Bond-009] Add tests for RequestHelpers.GetItemTypeStrings
 * #5209 [@crobibero] Create BaseItemKind enum
 * #5194 [@daullmer] Add nfo parsing for watched, playcount and lastplayed
 * #5193 [@daullmer] Add test for generic nfo provider id parsing
 * #5190 [@Bond-009] Add regression test for PluginManager.SaveManifest
 * #5189 [@Bond-009] Remove last usage of \d
 * #5174 [@barronpm] Clean up UserManager.AuthenticateUser
 * #5166 [@netpok] Get episode range end from XBMC compatible nfo
 * #5159 [@daullmer] Remove unused files
 * #5142 [@M0ssTee] Replaced /d with [0-9], see issue #2923
 * #5112 [@Bond-009] Add test for ShuffleExtensions
 * #5097 [@Bond-009] Remove useless abstraction and clean up formatting
 * #5092 [@OancaAndrei] Clear playlist in SyncPlay group
 * #5088 [@daullmer] Fix nfo saving during UserDataSaved event
 * #5085 [@daullmer] Process actor type in nfo files
 * #5084 [@daullmer] Don't write tagline in <outline> in nfo files
 * #5074 [@Bond-009] 100% branch coverage for Jellyfin.Naming
 * #5068 [@daullmer] Add additional tests for nfo parsing
 * #5043 [@senritsu] adjust episode path expression to allow digits in series names
 * #5012 [@Bond-009] Improve WebSocket Message Deserialization
 * #5010 [@BaronGreenback] Removal of IPluginConfigurationPage
 * #5009 [@MrTimscampi] Move studios image providers to plugin
 * #5007 [@Bond-009] Open FileStream with FileMode.Create instead of FileMode.OpenOrCreate
 * #5006 [@Bond-009] Use JsonSerializer.SerializeToUtf8Bytes when doing a round trip
 * #5005 [@Bond-009] JsonSerializer deserialize from bytes where possible
 * #4994 [@Bond-009] Add tests for artist nfo
 * #4992 [@Bond-009] Add tests for series nfo
 * #4989 [@Bond-009] Add tests for NFO parsers
 * #4988 [@Bond-009] Remove CropWhitespace function
 * #4986 [@Bond-009] Use new ReadAllLines extensions
 * #4984 [@Bond-009] Use SubtitleEdit to parse subtitles
 * #4981 [@daullmer] Add .nfo ratings tag
 * #4945 [@obradovichv] Fix string culture specificity
 * #4943 [@crobibero] Fix OMDb converter
 * #4899 [@Bond-009] Cover all branches in JsonNullableGuidConverter
 * #4878 [@Bond-009] Add tests for srt parser
 * #4877 [@Bond-009] Add tests for ass parser
 * #4857 [@crobibero] Fix dependencies
 * #4853 [@daullmer] Use System.Text.Json instead of ServiceStack.Text
 * #4849 [@crobibero] Remove unused dependencies 
 * #4799 [@tommasodotNET] Authorization header parsing
 * #4775 [@barronpm] Enable Nullable for Jellyfin.Server.Implementations
 * #4766 [@barronpm] Convert DeleteUser to async
 * #4754 [@Bond-009] Migrate from FxCop analyzers to .NET analyzers
 * #4731 [@Sylk] Modified ReadMe with updated command line command
 * #4720 [@MrTimscampi] Add overloaded constructor for ActivityLog levels
 * #4665 [@anthonylavado] Fix the NPM publish scope to public
 * #4664 [@joshuaboniface] Make me codeowner of the .ci dir
 * #4663 [@joshuaboniface] Bump version to 10.8.0 for next release
 * #4615 [@strugee] Improve restart.sh
 * #4005 [@cromefire] Add additional opts for systemd / upstart

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [326

Note: Dependabot automatic PRs are excluded from this 

 * jellyfin/jellyfin-web#3668 [@dmitrylyzo] Show ettings button even if transcoding isn't supported
 * jellyfin/jellyfin-web#3667 [@dmitrylyzo] Enable Lint job on release branches
 * jellyfin/jellyfin-web#3664 [@dmitrylyzo] Bump @jellyfin/libass-wasm from 4.1.0 to 4.1.1
 * jellyfin/jellyfin-web#3662 [@1337joe] Support searching for tv programs
 * jellyfin/jellyfin-web#3658 [@thornbill] Add workaround for channel card images
 * jellyfin/jellyfin-web#3657 [@dmitrylyzo] Remove play button highlighting
 * jellyfin/jellyfin-web#3647 [@1337joe] Disable "Automatically add to collection" by default
 * jellyfin/jellyfin-web#3644 [@dmitrylyzo] Migrate to @jellyfin/libass-wasm@4.1.0
 * jellyfin/jellyfin-web#3643 [@dmitrylyzo] Resolve worker URLs
 * jellyfin/jellyfin-web#3642 [@taku0] Change CSS font-family by language preference
 * jellyfin/jellyfin-web#3639 [@rhld16] Add missing languages
 * jellyfin/jellyfin-web#3637 [@MinecraftPlaye] Add WebP to the page detection list for comics
 * jellyfin/jellyfin-web#3635 [@dmitrylyzo] Fix SSA/ASS missing font
 * jellyfin/jellyfin-web#3628 [@thornbill] Fix artists album lists
 * jellyfin/jellyfin-web#3622 [@thornbill] Restore external links on mobile
 * jellyfin/jellyfin-web#3618 [@thornbill] Fix backdrop being used on large screens in mobile layout
 * jellyfin/jellyfin-web#3617 [@thornbill] Fix iPadOS icon
 * jellyfin/jellyfin-web#3616 [@thornbill] Revert some poor translations
 * jellyfin/jellyfin-web#3614 [@dmitrylyzo] Check undefined streamInfo.url
 * jellyfin/jellyfin-web#3604 [@thornbill] Fix custom element creation
 * jellyfin/jellyfin-web#3601 [@thornbill] Fix XSS in repositories list
 * jellyfin/jellyfin-web#3597 [@nielsvanvelzen] Use text input in Quick Connect page
 * jellyfin/jellyfin-web#3577 [@thornbill] Fix SD filter state
 * jellyfin/jellyfin-web#3547 [@thornbill] Fix touch events in epub player
 * jellyfin/jellyfin-web#3543 [@Shadowghost] Restore sort order and fix strm usecase
 * jellyfin/jellyfin-web#3535 [@dmitrylyzo] Fix 'resume' when clicking on item details poster
 * jellyfin/jellyfin-web#3527 [@thornbill] Fix rewatching next up status
 * jellyfin/jellyfin-web#3525 [@whiteowl3] Correct Typo
 * jellyfin/jellyfin-web#3519 [@dmitrylyzo] Escape HTML
 * jellyfin/jellyfin-web#3505 [@dmitrylyzo] Fix HTML escaping
 * jellyfin/jellyfin-web#3503 [@felixoswald] Fix birth location link
 * jellyfin/jellyfin-web#3502 [@dmitrylyzo] Fix webOS OPUS support
 * jellyfin/jellyfin-web#3501 [@dmitrylyzo] Fix old streamInfo on stream change
 * jellyfin/jellyfin-web#3500 [@dmitrylyzo] Some fixes for theme song/video
 * jellyfin/jellyfin-web#3498 [@thornbill] Restore missing MessageUnauthorizedUser error message
 * jellyfin/jellyfin-web#3496 [@renovate[bot]] Update development dependencies
 * jellyfin/jellyfin-web#3495 [@thornbill] Fix any type warning
 * jellyfin/jellyfin-web#3493 [@thornbill] Add default-case-last rule and fix issues
 * jellyfin/jellyfin-web#3492 [@renovate[bot]] Update dependency @types/react to v17.0.40
 * jellyfin/jellyfin-web#3490 [@h1dden-da3m0n] add dev-deps label to renovate dev-deps PRs
 * jellyfin/jellyfin-web#3489 [@thornbill] Add headings to display settings screen
 * jellyfin/jellyfin-web#3488 [@renovate[bot]] Update dependency cssnano to v5.1.1
 * jellyfin/jellyfin-web#3482 [@nyanmisaka] Remove the deprecated OMX HWA
 * jellyfin/jellyfin-web#3481 [@Maxr1998] Sort album tracks by (Parent)IndexNumber, then SortName
 * jellyfin/jellyfin-web#3480 [@thornbill] Fix more accessibility issues
 * jellyfin/jellyfin-web#3478 [@thornbill] Fix click on item details poster playing wrong item
 * jellyfin/jellyfin-web#3477 [@renovate[bot]] Update development dependencies
 * jellyfin/jellyfin-web#3476 [@renovate[bot]] Update development dependencies
 * jellyfin/jellyfin-web#3475 [@renovate[bot]] Update dependency cssnano to v5.1.0
 * jellyfin/jellyfin-web#3474 [@renovate[bot]] Update CI dependencies (major)
 * jellyfin/jellyfin-web#3473 [@thornbill] Move rewatching in next up to display option and remove home section
 * jellyfin/jellyfin-web#3472 [@thornbill] Add google cast unsupported message and update translations
 * jellyfin/jellyfin-web#3471 [@thornbill] Fix remaining any type warnings
 * jellyfin/jellyfin-web#3467 [@dmitrylyzo] Return Promise from SyncPlay playRequest
 * jellyfin/jellyfin-web#3466 [@dmitrylyzo] Fix HTMLMediaElement.play no Promise
 * jellyfin/jellyfin-web#3465 [@dmitrylyzo] Show slideshow OSD on click
 * jellyfin/jellyfin-web#3464 [@thornbill] Fix minor issues with card padder icons
 * jellyfin/jellyfin-web#3463 [@dmitrylyzo] Add more accessibility
 * jellyfin/jellyfin-web#3461 [@dmitrylyzo] Fix page reload on return
 * jellyfin/jellyfin-web#3460 [@thornbill] Fix remote control translation
 * jellyfin/jellyfin-web#3459 [@dmitrylyzo] Add aria-hidden to button icons
 * jellyfin/jellyfin-web#3458 [@dmitrylyzo] Alter the title of the state buttons
 * jellyfin/jellyfin-web#3457 [@renovate[bot]] Update actions/setup-node action to v3
 * jellyfin/jellyfin-web#3456 [@dmitrylyzo] Few refactors of remotecontrol
 * jellyfin/jellyfin-web#3453 [@dmitrylyzo] Add copy buttons to Media Info
 * jellyfin/jellyfin-web#3452 [@thornbill] Update mixed library label
 * jellyfin/jellyfin-web#3451 [@thornbill] Move rewatching to separate home screen section
 * jellyfin/jellyfin-web#3449 [@dmitrylyzo] Unhide some options on TVs
 * jellyfin/jellyfin-web#3448 [@dmitrylyzo] Add card padder icon for items with an image
 * jellyfin/jellyfin-web#3445 [@dmitrylyzo] Fix nowplayingbar not displaying when restoring the view
 * jellyfin/jellyfin-web#3444 [@dmitrylyzo] Fix playing theme song when using parent links
 * jellyfin/jellyfin-web#3443 [@dmitrylyzo] Fix Play/Resume focus jump
 * jellyfin/jellyfin-web#3438 [@thornbill] Update renovate configuration
 * jellyfin/jellyfin-web#3435 [@renovate[bot]] Update development dependencies
 * jellyfin/jellyfin-web#3434 [@renovate[bot]] Update dependency postcss-preset-env to v7.4.1
 * jellyfin/jellyfin-web#3433 [@dmitrylyzo] [TypeScript] Disable implicit any
 * jellyfin/jellyfin-web#3432 [@1337joe] Fix show sort by date played
 * jellyfin/jellyfin-web#3431 [@dmitrylyzo] Check OPUS support on webOS
 * jellyfin/jellyfin-web#3427 [@dmitrylyzo] Reload backdrop on restore
 * jellyfin/jellyfin-web#3426 [@thornbill] Fix new lint errors
 * jellyfin/jellyfin-web#3424 [@renovate[bot]] Update dependency follow-redirects to 1.14.8 [SECURITY]
 * jellyfin/jellyfin-web#3420 [@dmitrylyzo] Display physical dimensions of player
 * jellyfin/jellyfin-web#3415 [@dmitrylyzo] Fix focus on Home tab
 * jellyfin/jellyfin-web#3412 [@dmitrylyzo] Reduce the size of the icon in the ListView
 * jellyfin/jellyfin-web#3411 [@dmitrylyzo] Allow navigation to the parent show/season/album
 * jellyfin/jellyfin-web#3409 [@thornbill] Fix pagination on live tv pages
 * jellyfin/jellyfin-web#3408 [@renovate[bot]] Update development dependencies
 * jellyfin/jellyfin-web#3406 [@renovate[bot]] Update dependency postcss [SECURITY]
 * jellyfin/jellyfin-web#3405 [@renovate[bot]] Update development dependencies (major)
 * jellyfin/jellyfin-web#3403 [@renovate[bot]] Update actions/checkout action to v2.4.0
 * jellyfin/jellyfin-web#3402 [@renovate[bot]] Pin dependencies
 * jellyfin/jellyfin-web#3399 [@renovate[bot]] Update dependency nanoid to 3.1.31 [SECURITY]
 * jellyfin/jellyfin-web#3398 [@renovate[bot]] Update dependency marked to 4.0.10 [SECURITY]
 * jellyfin/jellyfin-web#3395 [@renovate[bot]] Update dependency follow-redirects to 1.14.7 [SECURITY]
 * jellyfin/jellyfin-web#3394 [@renovate[bot]] Update dependency browserslist to 4.16.5 [SECURITY]
 * jellyfin/jellyfin-web#3385 [@dmitrylyzo] Fix themes
 * jellyfin/jellyfin-web#3380 [@dmitrylyzo] Enable AV1 codec on webOS 5+ FHD
 * jellyfin/jellyfin-web#3379 [@Shadowghost] Add external, forced and default attributes to subtitle and audio mediainfo
 * jellyfin/jellyfin-web#3377 [@thornbill] Fix issue where wrong plugin could be disabled
 * jellyfin/jellyfin-web#3376 [@SenorSmartyPants] Add option to season image downloader to pick from series images
 * jellyfin/jellyfin-web#3374 [@dmitrylyzo] Handle resolved play promise
 * jellyfin/jellyfin-web#3373 [@dmitrylyzo] Fix theme song playback when switching items with different themes
 * jellyfin/jellyfin-web#3369 [@dmitrylyzo] Escape HTML
 * jellyfin/jellyfin-web#3367 [@SenorSmartyPants] Display rewatching list in Next up section on home page
 * jellyfin/jellyfin-web#3364 [@h1dden-da3m0n] add stale issue check workflow
 * jellyfin/jellyfin-web#3361 [@MinecraftPlaye] Only use comic pages for internal calculations and ignore metadata files
 * jellyfin/jellyfin-web#3360 [@dmitrylyzo] Show AlphaPicker if there is SortName
 * jellyfin/jellyfin-web#3359 [@dmitrylyzo] Fix page layouts for webOS
 * jellyfin/jellyfin-web#3357 [@SenorSmartyPants] Display MediaSourceCount for all media Types
 * jellyfin/jellyfin-web#3356 [@SenorSmartyPants] Special Features: Display extraType as secondaryText on card
 * jellyfin/jellyfin-web#3355 [@dmitrylyzo] Add Markdown to Login Disclaimer
 * jellyfin/jellyfin-web#3354 [@dmitrylyzo] Fix Light theme text color
 * jellyfin/jellyfin-web#3353 [@dmitrylyzo] Cleanup
 * jellyfin/jellyfin-web#3351 [@dmitrylyzo] Fix starting of book player with a blank page
 * jellyfin/jellyfin-web#3350 [@MinecraftPlaye]  Update the resume button after stopping
 * jellyfin/jellyfin-web#3349 [@MinecraftPlaye] Save reading progress for pdfs for each page
 * jellyfin/jellyfin-web#3348 [@thornbill] Fix unstyled emby-select field when rendered with React
 * jellyfin/jellyfin-web#3347 [@dmitrylyzo] Stack toasts
 * jellyfin/jellyfin-web#3344 [@knackebrot] Try to determine the number of speakers before falling back to hardcoded values
 * jellyfin/jellyfin-web#3343 [@dmitrylyzo] Limit transcoding profiles with maximum resolution
 * jellyfin/jellyfin-web#3342 [@dmitrylyzo] Fix LiveTV Channels paging and autofocus
 * jellyfin/jellyfin-web#3341 [@dmitrylyzo] Add paging to listview
 * jellyfin/jellyfin-web#3340 [@dmitrylyzo] Fix auto focus on Play/Resume
 * jellyfin/jellyfin-web#3336 [@SenorSmartyPants] Display series level extras on tv series page.
 * jellyfin/jellyfin-web#3335 [@dmitrylyzo] Fix Blurhash worker on webOS 1.2
 * jellyfin/jellyfin-web#3334 [@dmitrylyzo] Fix trailer playback when no local trailers are available
 * jellyfin/jellyfin-web#3324 [@thornbill] Add plugin repository help link
 * jellyfin/jellyfin-web#3323 [@thornbill] Fix image urls
 * jellyfin/jellyfin-web#3322 [@thornbill] Add channels link to home page section
 * jellyfin/jellyfin-web#3319 [@SenorSmartyPants] Add episode details to live TV DVR schedule
 * jellyfin/jellyfin-web#3318 [@iainsaxonhome] Added Quit App to main menu
 * jellyfin/jellyfin-web#3317 [@SenorSmartyPants] Make Live TV Guide scrollbar visible.
 * jellyfin/jellyfin-web#3315 [@1337joe] Expose collection generation options for mixed libraries
 * jellyfin/jellyfin-web#3313 [@thornbill] Fix eslint polyfills for typescript files
 * jellyfin/jellyfin-web#3302 [@marius-luca-87] Avoid requesting mjpeg attachements during ass subtitle playback
 * jellyfin/jellyfin-web#3297 [@thornbill] Update babel packages
 * jellyfin/jellyfin-web#3296 [@marius-luca-87] Add "Select All" action to multiSelect
 * jellyfin/jellyfin-web#3281 [@joshuaboniface] Remove bump-version junk
 * jellyfin/jellyfin-web#3271 [@thornbill] Fix number option in alphapicker
 * jellyfin/jellyfin-web#3270 [@thornbill] Add Apple device icon
 * jellyfin/jellyfin-web#3269 [@thornbill] Bump jellyfin-apiclient to v1.10.0
 * jellyfin/jellyfin-web#3251 [@thornbill] Allow for unlimited photos in playbackmanager
 * jellyfin/jellyfin-web#3250 [@thornbill] Make movies and shows in genre list random
 * jellyfin/jellyfin-web#3247 [@thornbill] Remove network device option from add library dialog
 * jellyfin/jellyfin-web#3246 [@thornbill] Fix Fedora and CentOS builds
 * jellyfin/jellyfin-web#3244 [@thornbill] Add eslint rule for empty functions
 * jellyfin/jellyfin-web#3242 [@crobibero] Add missing strings for TranscodeReason
 * jellyfin/jellyfin-web#3241 [@matthew-jones-uk] Add DisableEmbeddedSubtitles support in editor
 * jellyfin/jellyfin-web#3237 [@Piccar] Added hovereffect on listItems for all themes
 * jellyfin/jellyfin-web#3231 [@emilrowland] fix: Oculus browser is no longer marked as TV
 * jellyfin/jellyfin-web#3230 [@SenorSmartyPants] Fix #369 : Episode Details Premiere date
 * jellyfin/jellyfin-web#3226 [@brianjmurrell] Run bump_version in make srpm
 * jellyfin/jellyfin-web#3209 [@dmitrylyzo] Handle command 'Back'
 * jellyfin/jellyfin-web#3208 [@nyanmisaka] Remove unused server check for cinema mode option
 * jellyfin/jellyfin-web#3206 [@nyanmisaka] Update HWA settings to adapt the server code changes
 * jellyfin/jellyfin-web#3197 [@ianjazz246] Sort genres by SortName instead of Random
 * jellyfin/jellyfin-web#3184 [@WWWesten] Add missing font option for subtitles
 * jellyfin/jellyfin-web#3181 [@PetrusZ] Add AutoCollection option to libraryoptionseditor
 * jellyfin/jellyfin-web#3180 [@brianjmurrell] Remove chown -R root:root from specfile
 * jellyfin/jellyfin-web#3172 [@joshuaboniface] Send SourceBranch to collect-server.azure.sh
 * jellyfin/jellyfin-web#3171 [@WWWesten] Update displaySettings.template.html
 * jellyfin/jellyfin-web#3161 [@thornbill] Rollback hls.js to 0.14
 * jellyfin/jellyfin-web#3160 [@thornbill] Fix list view item encoding
 * jellyfin/jellyfin-web#3149 [@grafixeyehero] Fix live tv default tab
 * jellyfin/jellyfin-web#3147 [@dmitrylyzo] Fix re-emptying image
 * jellyfin/jellyfin-web#3146 [@dmitrylyzo] Fix plugin image URL
 * jellyfin/jellyfin-web#3144 [@ferferga] Decode blurhash in a WebWorker
 * jellyfin/jellyfin-web#3143 [@WWWesten] Update Library Settings
 * jellyfin/jellyfin-web#3142 [@WWWesten] Update en-us.json for subtitlesettings component
 * jellyfin/jellyfin-web#3128 [@WWWesten] Add missing localization key for Media Info
 * jellyfin/jellyfin-web#3116 [@jomp16] Save playback speed rate, and restore when playing a video again
 * jellyfin/jellyfin-web#3115 [@dmitrylyzo] Fix regression after PR #3046
 * jellyfin/jellyfin-web#3114 [@dmitrylyzo] Remove language normalization - use original language
 * jellyfin/jellyfin-web#3113 [@Jellifi007] Fix H264 52 Level available but not detected Fixes #3090
 * jellyfin/jellyfin-web#3092 [@thornbill] Use single color for loading indicator
 * jellyfin/jellyfin-web#3091 [@thornbill] Fix dialog style conflict
 * jellyfin/jellyfin-web#3073 [@grafixeyehero] Convert userPasswordPage & UserImagePage to react
 * jellyfin/jellyfin-web#3072 [@grafixeyehero] Convert userParentalControlPage to react
 * jellyfin/jellyfin-web#3071 [@grafixeyehero] Convert userLibraryAccessPage to react
 * jellyfin/jellyfin-web#3070 [@grafixeyehero] Convert edit user page to react
 * jellyfin/jellyfin-web#3069 [@dmitrylyzo] Make dialog buttons smaller on TV
 * jellyfin/jellyfin-web#3049 [@cvium] Set 'Scan for new and updated files' as the default refresh option
 * jellyfin/jellyfin-web#3046 [@dmitrylyzo] Fix playback error stop
 * jellyfin/jellyfin-web#3044 [@thornbill] Fix repository url link not opening as external
 * jellyfin/jellyfin-web#3042 [@cvium] set sane defaults for the hidden SSDP and UDP config values
 * jellyfin/jellyfin-web#3034 [@MinecraftPlaye] Save the progress when reading a Comic Book Archive
 * jellyfin/jellyfin-web#3033 [@daullmer] Check permission in multiselect for refresh option in menu
 * jellyfin/jellyfin-web#3031 [@dmitrylyzo] Use custom modals on webOS and Tizen 2.x
 * jellyfin/jellyfin-web#3028 [@dmitrylyzo] Resolve show promise
 * jellyfin/jellyfin-web#3027 [@dmitrylyzo] Use "web" target in the serve mode only
 * jellyfin/jellyfin-web#3026 [@grafixeyehero] convert NewUserPage to react
 * jellyfin/jellyfin-web#3025 [@grafixeyehero] convert UserProfilesPage to react
 * jellyfin/jellyfin-web#3024 [@dmitrylyzo] Fix JavascriptSubtitlesOctopus dispose
 * jellyfin/jellyfin-web#3022 [@dmitrylyzo] Update JavascriptSubtitlesOctopus
 * jellyfin/jellyfin-web#3021 [@thornbill] Move the selected player name next to cast icon
 * jellyfin/jellyfin-web#3020 [@thornbill] Fix remote fullscreen event handler
 * jellyfin/jellyfin-web#3019 [@thornbill] Enable multiserver in development environments
 * jellyfin/jellyfin-web#3018 [@thornbill] Fix audio player overlapping on small screens
 * jellyfin/jellyfin-web#3017 [@thornbill] Fix header centering on large mobile devices
 * jellyfin/jellyfin-web#3016 [@thornbill] Remove unused sass mixins
 * jellyfin/jellyfin-web#3004 [@4censord] build.sh: Allow docker build on non debian systems
 * jellyfin/jellyfin-web#3002 [@thornbill] Add theme color support
 * jellyfin/jellyfin-web#3001 [@thornbill] Update apiclient
 * jellyfin/jellyfin-web#2975 [@dmitrylyzo] Fix server candidates on apps
 * jellyfin/jellyfin-web#2971 [@dmitrylyzo] Fix webOS DTS audio support
 * jellyfin/jellyfin-web#2952 [@dmitrylyzo] Fix video UI for LiveTV
 * jellyfin/jellyfin-web#2950 [@dmitrylyzo] Use the same duration format
 * jellyfin/jellyfin-web#2948 [@thornbill] Restore missing placeholder error message
 * jellyfin/jellyfin-web#2947 [@SegiH] Move "Remove" option in card menu item in Dashboard->Library to the last item
 * jellyfin/jellyfin-web#2946 [@thornbill] Disable sync correction by default on mobile
 * jellyfin/jellyfin-web#2945 [@thornbill] Fix media indicator color
 * jellyfin/jellyfin-web#2944 [@SegiH] Show playlist item count
 * jellyfin/jellyfin-web#2943 [@thornbill] Fix play all and shuffle buttons
 * jellyfin/jellyfin-web#2941 [@dmitrylyzo] Slideshow autoplay
 * jellyfin/jellyfin-web#2940 [@thornbill] Fix direct play logic when direct stream is disabled
 * jellyfin/jellyfin-web#2939 [@thornbill] Log warning instead of error when dictionary has not loaded
 * jellyfin/jellyfin-web#2937 [@oledfish] Add "Production" and "TV" episode orders to the metadata editor.
 * jellyfin/jellyfin-web#2936 [@OancaAndrei] Update ApiClient instance used by SyncPlay
 * jellyfin/jellyfin-web#2934 [@joshuaboniface] Update bump_version to new NPM method
 * jellyfin/jellyfin-web#2917 [@dmitrylyzo] Dialog history and actionSheet resolving
 * jellyfin/jellyfin-web#2914 [@dmitrylyzo] Show error if player not found
 * jellyfin/jellyfin-web#2913 [@thornbill] Reorder item details sections
 * jellyfin/jellyfin-web#2912 [@thornbill] Disable warnings in webpack dev server overlay
 * jellyfin/jellyfin-web#2910 [@crobibero] Fix QuickConnect for 10.8
 * jellyfin/jellyfin-web#2908 [@dmitrylyzo] Fix theme song player
 * jellyfin/jellyfin-web#2907 [@ferferga] Add rebase command
 * jellyfin/jellyfin-web#2889 [@dmitrylyzo] Fix dialog history
 * jellyfin/jellyfin-web#2887 [@dmitrylyzo] Babel blurhash
 * jellyfin/jellyfin-web#2872 [@GodTamIt] Send vp8 and vp9 over vpx as transcode profiles
 * jellyfin/jellyfin-web#2860 [@Pfuenzle] Removed Tag filter limit of 50
 * jellyfin/jellyfin-web#2859 [@thornbill] Redesign item details screen for mobile
 * jellyfin/jellyfin-web#2858 [@thornbill] Fix build warnings
 * jellyfin/jellyfin-web#2857 [@njsmith] Allow web player to buffer ahead a reasonable amount of data
 * jellyfin/jellyfin-web#2853 [@thornbill] Update workbox
 * jellyfin/jellyfin-web#2837 [@keegandahm] Made volume slider exponential rather than linear
 * jellyfin/jellyfin-web#2835 [@nielsvanvelzen] Add "jellyfin" to output file names
 * jellyfin/jellyfin-web#2829 [@thornbill] Fix continue watching card shapes
 * jellyfin/jellyfin-web#2821 [@thornbill] Update merge conflict action trigger
 * jellyfin/jellyfin-web#2801 [@MrTimscampi] Person types and translations
 * jellyfin/jellyfin-web#2799 [@daullmer] Fix TV item details UX
 * jellyfin/jellyfin-web#2794 [@nyanmisaka] Add BT.2390 EETF to tonemap algorithms
 * jellyfin/jellyfin-web#2790 [@thornbill] Fix webpack config for bundle caching
 * jellyfin/jellyfin-web#2789 [@thornbill] Update stalebot configuration
 * jellyfin/jellyfin-web#2786 [@MrTimscampi] Improve people pages and metadata editor
 * jellyfin/jellyfin-web#2785 [@MrTimscampi] Allow markdown for plugin changelogs
 * jellyfin/jellyfin-web#2784 [@thornbill] Fix ATV 0.11 using wrong icon
 * jellyfin/jellyfin-web#2781 [@imchasingshadows] bugfix/web0s-fullscreen
 * jellyfin/jellyfin-web#2778 [@HazilMohamed] fix endsAt time when playback speed changes
 * jellyfin/jellyfin-web#2777 [@MrTimscampi] Translate the transcode reasons
 * jellyfin/jellyfin-web#2776 [@gnuyent] Add hardware encoding status to playback data
 * jellyfin/jellyfin-web#2758 [@thornbill] Use album artist for listing artist albums
 * jellyfin/jellyfin-web#2753 [@jackrvan] Add setting for max days for a show to appear in next up list
 * jellyfin/jellyfin-web#2749 [@nielsvanvelzen] Use new Quick Connect enabled endpoint
 * jellyfin/jellyfin-web#2748 [@nielsvanvelzen] Remove activate feature from Quick Connect page
 * jellyfin/jellyfin-web#2747 [@nielsvanvelzen] Move Quick Connect toggle to General page in dashboard
 * jellyfin/jellyfin-web#2743 [@thornbill] Remove html from syncplay toast messages
 * jellyfin/jellyfin-web#2742 [@thornbill] Update dependencies
 * jellyfin/jellyfin-web#2740 [@MrTimscampi] Replace newlines in plugin changelogs with the proper HTML tag
 * jellyfin/jellyfin-web#2736 [@thornbill] Fix invalid import path
 * jellyfin/jellyfin-web#2722 [@MrTimscampi] Add TypeScript support for React components
 * jellyfin/jellyfin-web#2707 [@grafixeyehero] Access module 
 * jellyfin/jellyfin-web#2706 [@thornbill] Update icon used for syncplay
 * jellyfin/jellyfin-web#2705 [@thornbill] Add support for custom menu links in config.json
 * jellyfin/jellyfin-web#2704 [@thornbill] Fix continue reading card shape
 * jellyfin/jellyfin-web#2703 [@thornbill] Add error logging for missing translation keys
 * jellyfin/jellyfin-web#2698 [@thornbill] Fix live reload
 * jellyfin/jellyfin-web#2683 [@thornbill] Add react support
 * jellyfin/jellyfin-web#2681 [@thornbill] Cleanup toasts
 * jellyfin/jellyfin-web#2680 [@anthonylavado] Update IRC Links to Libera Chat
 * jellyfin/jellyfin-web#2670 [@viggy96] Add next/previous chapter buttons to video player
 * jellyfin/jellyfin-web#2668 [@dmitrylyzo] Fix back on load [Tizen 2.x]
 * jellyfin/jellyfin-web#2664 [@dmitrylyzo] Remove trying app URL as server URL
 * jellyfin/jellyfin-web#2663 [@JKI12] Fixes resuming of books
 * jellyfin/jellyfin-web#2660 [@grafixeyehero] Fix browser history for dialog
 * jellyfin/jellyfin-web#2646 [@shortspider] Prevent Buttons from Sitting Over Text
 * jellyfin/jellyfin-web#2630 [@dmitrylyzo] Fix home screen settings
 * jellyfin/jellyfin-web#2627 [@BrianCArnold] Added ability to burn in all subtitles, including SRT.
 * jellyfin/jellyfin-web#2626 [@shortspider] Add Fullscreen Ability to Books
 * jellyfin/jellyfin-web#2625 [@dmitrylyzo] Cleanup: maintabsmanager
 * jellyfin/jellyfin-web#2622 [@dmitrylyzo] Fix tabs scrolling in Tizen
 * jellyfin/jellyfin-web#2621 [@iwalton3] Add subtitle/audio auto-set feature.
 * jellyfin/jellyfin-web#2618 [@iwalton3] Allow client custom css and disabling global server custom css.
 * jellyfin/jellyfin-web#2613 [@dmitrylyzo] ScrollManager: fix parent search
 * jellyfin/jellyfin-web#2612 [@dmitrylyzo] Fix navigation in paging block
 * jellyfin/jellyfin-web#2610 [@shortspider] Add a Continue Reading Section
 * jellyfin/jellyfin-web#2599 [@omeryagmurlu] Use episode images in the "Next Up" section
 * jellyfin/jellyfin-web#2594 [@ferferga] chore(ci): replace with actions-label-merge-conflict
 * jellyfin/jellyfin-web#2583 [@daullmer] Add configuration for slow response logging
 * jellyfin/jellyfin-web#2581 [@dmitrylyzo] Add LogIn/LogOut event handlers to NativeShell
 * jellyfin/jellyfin-web#2569 [@ferferga] chore(npm): fix CI after switch to npm
 * jellyfin/jellyfin-web#2559 [@thornbill] Remove commented code
 * jellyfin/jellyfin-web#2557 [@iwalton3] NativeShell enhancements for Jellyfin Media Player
 * jellyfin/jellyfin-web#2539 [@BrianCArnold] Changed calculation for media info run time to render hours
 * jellyfin/jellyfin-web#2534 [@jackrvan] Improve behaviour of space bar pausing/playing video
 * jellyfin/jellyfin-web#2533 [@dmitrylyzo] Make play button bigger
 * jellyfin/jellyfin-web#2532 [@dmitrylyzo] Add controls page to the user settings
 * jellyfin/jellyfin-web#2523 [@ferferga] Run merge conflict check on PR rebase/commit
 * jellyfin/jellyfin-web#2518 [@dkanada] pull fedora changes into master branch
 * jellyfin/jellyfin-web#2516 [@tonyfinn] Show current group members in syncplay group dialog
 * jellyfin/jellyfin-web#2506 [@thornbill] Remove forum badge
 * jellyfin/jellyfin-web#2499 [@thornbill] Fix dialog helper not resolving
 * jellyfin/jellyfin-web#2497 [@PrplHaz4] KnownProxies now supports hostnames too
 * jellyfin/jellyfin-web#2491 [@dkanada] use better icon for manage library button
 * jellyfin/jellyfin-web#2485 [@dmitrylyzo] Fix webpack globbing in hidden folder
 * jellyfin/jellyfin-web#2476 [@ferferga] Switch to npm
 * jellyfin/jellyfin-web#2472 [@dkanada] add border radius to several card elements
 * jellyfin/jellyfin-web#2467 [@albeeeert] Add padding to prevent music controls from clipping
 * jellyfin/jellyfin-web#2466 [@eudes] Use absolute path in CopyPlugin config
 * jellyfin/jellyfin-web#2464 [@dmitrylyzo] Tune some styles on now playing page
 * jellyfin/jellyfin-web#2456 [@dmitrylyzo] Add Webpack publicPath
 * jellyfin/jellyfin-web#2445 [@dkanada] reduce dependabot update frequency
 * jellyfin/jellyfin-web#2428 [@acvigue] Fix: prevent some backdrops from showing on homepage
 * jellyfin/jellyfin-web#2379 [@dkanada] fix some unhandled promises and refactor some code
 * jellyfin/jellyfin-web#2355 [@thornbill] Fix warnings
 * jellyfin/jellyfin-web#2354 [@thornbill] Move to sass everywhere
 * jellyfin/jellyfin-web#2352 [@JKI12] Change to expose keyboard shortcuts for chapter navigation
 * jellyfin/jellyfin-web#2342 [@OancaAndrei] Clear playlist in SyncPlay group
 * jellyfin/jellyfin-web#2310 [@nielsvanvelzen] Use OpenStreetMap instead of Google Maps
 * jellyfin/jellyfin-web#2281 [@Camc314] Update fontsource to 4.0.1
 * jellyfin/jellyfin-web#2266 [@dkanada] remove touch controls from video player
 * jellyfin/jellyfin-web#2264 [@Artiume] Remove games references
 * jellyfin/jellyfin-web#2261 [@Artiume] Dependencies update
 * jellyfin/jellyfin-web#2221 [@thornbill] Add lint rule for array callback returns
 * jellyfin/jellyfin-web#2212 [@thornbill] Use package version
 * jellyfin/jellyfin-web#2204 [@OancaAndrei] Add basic SyncPlay settings
 * jellyfin/jellyfin-web#2176 [@joshuaboniface] Bump version to 10.8.0 for next release

## 10.7.7 – 2021-09-06

# Jellyfin 10.7.7

Stable hotfix release for 10.7.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

N/A

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/27

### [jellyfin](https://github.com/jellyfin/jellyfin) [2]

 * #6512 [@thornbill] Preferences fix
 * #6274 [@thornbill] Restore max width and height params

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [1]

 * jellyfin/jellyfin-web#2759 [@thornbill] Fix serviceworker paths

## 10.7.6 – 2021-06-18

# Jellyfin 10.7.6

Stable hotfix release for 10.7.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [All] Fix DLNA/SSDP flooding bug

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/27

### [jellyfin](https://github.com/jellyfin/jellyfin) [7]

 * #6175 [@nielsvanvelzen] Fix routeMediaSourceId route parameter in SubtitleController GetSubtitle
 * #6131 [@BaronGreenback] Fix network flooding issue
 * #6053 [@nyanmisaka] Fix the 'No decoder surfaces left' error on Cuda
 * #6043 [@peterspenler] Reorder requested audio channels checks
 * #6038 [@crobibero] Don't logout if deviceId is null
 * #6022 [@cvium] Revert remuxing permission changes from #5859
 * #5987 [@Bond-009] PathExtensions: Fix index out of bounds in TryReplaceSubPath

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [7]

 * jellyfin/jellyfin-web#2678 [@grafixeyehero] Access Loading globally
 * jellyfin/jellyfin-web#2676 [@thornbill] Fix xss via displaymessage
 * jellyfin/jellyfin-web#2675 [@thornbill] Fix sharing url
 * jellyfin/jellyfin-web#2673 [@dmitrylyzo] Fix ServiceWorker URL
 * jellyfin/jellyfin-web#2672 [@nyanmisaka] Remove OPUS from supported HLS audio formats
 * jellyfin/jellyfin-web#2665 [@dmitrylyzo] Add connection response handling
 * jellyfin/jellyfin-web#2475 [@dmitrylyzo] Fix wizard in multi-server app

## 10.7.5 – 2021-05-05

# Jellyfin 10.7.5

Stable hotfix release for 10.7.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [All] Fix broken profiles from 10.7.4

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/27

### [jellyfin](https://github.com/jellyfin/jellyfin) [0]

 * ~#5943 [@Maxr1998] Nullability handling for device profile classes~ REVERT

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [0]

## 10.7.4 – 2021-05-05

# Jellyfin 10.7.4

Stable hotfix release for 10.7.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [All] Fix broken playback and tests in 10.7.3

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/27

### [jellyfin](https://github.com/jellyfin/jellyfin) [3]

 * #5970 [@crobibero] Fix Linux Tests
 * #5969 [@crobibero] Remove Required attributes
 * #5968 [@crobibero] Remove legacy apiclient generation

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [0]

## 10.7.3 – 2021-05-05

# Jellyfin 10.7.3

Stable hotfix release for 10.7.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [All] Small bugfixes
* [All] Security advisory https://github.com/jellyfin/jellyfin/security/advisories/GHSA-rgjw-4fwc-9v96: Remove dangerous endpoints that allow unauthenticated enumeration and access to private HTTP resources.  **NOTE**: This is an API-breaking change. The major security risk outweights the issue of changing the endpoints. These were used only when fetching remote images.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/27

### [jellyfin](https://github.com/jellyfin/jellyfin) [18]

 * [SECURITY GHSA-rgjw-4fwc-9v96] [@joshuaboniface] Remove /Images/Remote API endpoint
 * #5943 [@Maxr1998] Nullability handling for device profile classes
 * #5937 [@Maxr1998] Remove extraneous 'stream' parameter
 * #5904 [@cvium] add UpdatePeopleAsync and add people to both tables
 * #5903 [@iwalton3] Leave SyncPlay group on session disconnect.
 * #5881 [@cvium] Add tvrage and imdb ids for episodes
 * #5878 [@Artiume] Fix Audiobook Resume
 * #5873 [@cvium] Check for empty string when migrating displaypreferences
 * #5870 [@cvium] Fix TMDb Person Provider
 * #5863 [@cvium] use IF NOT EXISTS in migration
 * #5861 [@BaronGreenback] Change profile matching to match what the web interface says.
 * #5860 [@cvium] Fix notification disabled users list
 * #5859 [@cvium] Respect user settings for transcode and remux
 * #5852 [@cvium] Add Person to TypedBaseItems if it's new
 * #5848 [@sgmoore] Fix ArgumentOutOfRangeException scanning AudioBooks
 * #5826 [@BaronGreenback] PlayTo Fix: Use external ip not internal interface
 * #5808 [@cvium] Optimize the way items are grouped into collections

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [12]

 * jellyfin/jellyfin-web#2657 [@thornbill] Bump jellyfin-apiclient to 1.8.0
 * jellyfin/jellyfin-web#2648 [@thornbill] Fix alpine python package
 * jellyfin/jellyfin-web#2647 [@thornbill] Fix mov support in Safari
 * jellyfin/jellyfin-web#2645 [@joshuaboniface] Remove image proxying through API
 * jellyfin/jellyfin-web#2624 [@dmitrylyzo] webOS: fix Favorites tab
 * jellyfin/jellyfin-web#2620 [@dmitrylyzo] Hide AlphaPicker on Search page for real TVs
 * jellyfin/jellyfin-web#2619 [@dmitrylyzo] Fix video filters hiding
 * jellyfin/jellyfin-web#2617 [@iwalton3] Set scrollbar width in TV mode.
 * jellyfin/jellyfin-web#2616 [@dmitrylyzo] Fix view style selection dialog (ES6 migration)
 * jellyfin/jellyfin-web#2604 [@Artiume] Update Audiobook Resume Help
 * jellyfin/jellyfin-web#2593 [@oddstr13] Ensure that fillHeight gets set on image requests
 * jellyfin/jellyfin-web#2519 [@dmitrylyzo] Add HEVC in TS for Tizen and webOS

## 10.7.2 – 2021-04-11

# Jellyfin 10.7.2

Stable hotfix release for 10.7.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [All] Small bugfixes

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/27

### [jellyfin](https://github.com/jellyfin/jellyfin) [31]

 * #5782 [@cvium] Fix 10.7.2 nullable
 * #5769 [@cvium] Enable Workstation GC mode
 * #5764 [@cvium] Do not check permissions for Folders collectiontype
 * #5750 [@iwalton3] Fix setting audio stream in PlaybackInfo for jellyfin-web.
 * #5748 [@cvium] Set mediatype to Audio for playlists in a music library
 * #5747 [@cvium] Catch IOException and include stack trace when saving images
 * #5746 [@cvium] don't die on dangling symlinks
 * #5736 [@cvium] fetching images should not kill the scanner
 * #5734 [@cvium] move IsPlayed to outerquery
 * #5725 [@BrianCArnold] Fixed issue with determining if a directory was a directory or file
 * #5717 [@cvium] make custompref value nullable
 * #5712 [@BaronGreenback] Keep plugin state after update.
 * #5702 [@cvium] add simple auth handling to websocketmanager
 * #5693 [@Maxr1998] Probe result tweaks
 * #5688 [@crobibero] Add SessionDiscoveryInfo to generated api-docs
 * #5672 [@cvium] ensure only valid images are saved in ItemImageProvider
 * #5671 [@cvium] set original title in tmdbmovieprovider
 * #5661 [@ferferga] Return Major.Minor.Build instead of Major.Minor.Build.Revision for OpenAPI
 * #5634 [@cvium] make directoryservice cache case sensitive
 * #5631 [@BrianCArnold] Fix SessionController.SendMessageCommand Body Binding
 * #5629 [@lmaonator] Fix stream selection having no effect when casting to jellyfin-mpv-shim
 * #5624 [@crobibero] Allow subtitle format to be set from query parameter.
 * #5621 [@cvium] enable range processing for download endpoints
 * #5620 [@MrTimscampi] Ignore ffmpeg input format for ISO files and fix input path protocol for ISOs
 * #5613 [@accek] Improve responses to HEAD /audio/<id>/stream for Samsung DLNA renderers
 * #5600 [@cvium] Fix hls defaults for 10.7
 * #5596 [@BaronGreenback] Implemented DLNA exception handling
 * #5556 [@oddstr13] Add «resize to fill box» alternative for image endpoints
 * #5495 [@BaronGreenback] Fix remote access whitelist
 * #5416 [@BaronGreenback] Fix for multiple ip addresses on an interface which are in the same subnet.
 * #5385 [@Bond-009] Use XDocument.LoadAsync instead of XDocument.Parse
 * #5258 [@Smith00101010] Include specials in the calculation for the "Next Up" episode

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [9]

 * jellyfin/jellyfin-web#2586 [@joshuaboniface] Fix 10.7.2 Fedora docker
 * jellyfin/jellyfin-web#2585 [@nielsvanvelzen] Fix 10.7.2 lockfile
 * jellyfin/jellyfin-web#2576 [@dmitrylyzo] Fix ES6 migration
 * jellyfin/jellyfin-web#2575 [@cvium] Revert "fix: redirect to login if stored credentials are invalid"
 * jellyfin/jellyfin-web#2572 [@Ullmie02] Fix music videos on artist and album page
 * jellyfin/jellyfin-web#2552 [@cvium] add 'unknown' as an input command
 * jellyfin/jellyfin-web#2536 [@cvium] fix: redirect to login if stored credentials are invalid
 * jellyfin/jellyfin-web#2530 [@ssenart] [2529] [RegressionFix] [Dlna] Album shuffle button does not shuffle any more since 10.6.4.                                                                                                           
 * jellyfin/jellyfin-web#2524 [@crobibero] Build from fedora-33
 * jellyfin/jellyfin-web#2514 [@oddstr13] Add support for fillWidth and fillHeight
 * jellyfin/jellyfin-web#2509 [@MrTimscampi] Disable first episodes in Next Up home section

## 10.7.1 – 2021-03-21

# Jellyfin 10.7.1

Stable hotfix release for 10.7.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [All] Small bugfixes
* [Fedora] Fix broken builds and package issues
* [All/Windows] Fix several security issues as mention in https://github.com/jellyfin/jellyfin/security/advisories/GHSA-wg4c-c9g9-rxhx

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/27

### [jellyfin](https://github.com/jellyfin/jellyfin) [22]

 * [SECURITY GHSL-2021-050](https://github.com/jellyfin/jellyfin/security/advisories/GHSA-wg4c-c9g9-rxhx) [@EraYan] Fix issues 1 through 5 from GHSL-2021-050
 * #5559 [@cvium] Clean the entity name for non-words before searching
 * #5550 [@cvium] revert underscore as a multiversion separator
 * #5532 [@cvium] do not resolve episode-like files if they are in extras folders
 * #5518 [@crobibero] Add missing InstantMix endpoints
 * #5515 [@cvium] fix refresh endpoint
 * #5512 [@crobibero] Set openapi version to server version
 * #5510 [@BaronGreenback] Fix: Streaming crashing due to no deviceProfileId match.
 * #5504 [@crobibero] Add JsonStringConverter
 * #5500 [@crobibero] Fix third party integration
 * #5480 [@crobibero] Add SessionMessageType to generated openapi spec
 * #5476 [@EraYaN] Remove BuildPackage dependency for PublishNuget in CI
 * #5475 [@BaronGreenback] Null pointer fix in DLNA when its disabled.
 * #5461 [@cvium] fix multiversion eligibility check for complex folder names
 * #5457 [@cvium] Use distinct for AllArtists to avoid double refreshing
 * #5447 [@joshuaboniface] Remove Microsoft repo from install step
 * #5444 [@Ullmie02] Use FileShare.Read to fix HdHomeRun
 * #5431 [@cvium] Use imdbid as fallback in movie provider
 * #5428 [@cvium] Default to the searchinfo year, fallback to parsed year
 * #5403 [@BaronGreenback] Various DLNA Device Profile fixes
 * #5324 [@danieladov] Fix duplicated movies when group movies into collections is enabled

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [4]

 * jellyfin/jellyfin-web#2503 [@thornbill] Fix default values for invalid config.json files
 * jellyfin/jellyfin-web#2502 [@brianjmurrell] Add BR: nodejs for Fedora 33 and up
 * jellyfin/jellyfin-web#2498 [@thornbill] Add close button to comics player
 * jellyfin/jellyfin-web#2496 [@thornbill] Allow logos without backdrops enabled

## 10.7.0 – 2021-03-08

# Jellyfin 10.7.0

Stable release for 10.7.0

GitHub project for release: https://github.com/orgs/jellyfin/projects/27

Binary assets: https://repo.jellyfin.org/releases/server

## User-facing Features

* SyncPlay for TV shows and Music
* Significantly improved web performance due to ES6 upgrades, Webpack, and assets served with gzip compression
* Migration of further databases to new EFCore database framework
* Redesigned OSD and Up Next dialog
* New PDF reader functionality
* New Comics (cbz/cbr) reader functionality
* New HDR thumbnails extraction functionality
* New HDR Tone mapping functionality with Nvidia NVENC, AMD AMF and Intel VAAPI (additional configuration is required)
* HEVC remuxing or transcoding over fMP4 on supported Apple devices (disabled by default)
* Allow custom fonts to be used for ASS/SSA subtitle rendering
* New default library image style (generated on library scans)
* New QuickConnect functionality for (disabled by default)
* Support for limiting the number of user sessions
* Support for uploading subtitles
* Improved networking backend
* Upgrade to .NET SDK 5.0 for improved performance in the backend
* Fix issues with reboot script on Linux with Systemd
* Various fixes for iOS Safari and Edge Chromium browsers
* Various transcoding improvements
* Various bugfixes and minor improvements
* Various code cleanup
* Updated and improved plugin management interface, prevents bugs when upgrading as well as improve functionality
* Fixes some bugs with DLNA

## Release Notes

* [Debian/Ubuntu] Please note that when upgrading from <10.7.0, you will be prompted for changes to the file "/usr/share/jellyfin/web/config.json". **You should select "Y" for this ("install the package maintainer's version")** unless you have modified this file yourself.
* [ALL] Non-reversable database changes. **Ensure you back up before upgrading.**
* [ALL] TVDB support has been *removed* from the core server. If TVDB metadata was enabled on a library, this will be disabled. TVDB support can now be obtained through a separate plugin available in the official Plugin Catalog.
* [ALL] If you use a reverse proxy with X-Forwarded-For, and have a static proxy IP, consider setting this option in the Networking admin tab for more reliable parsing.

## Client/Plugin (API/ABI) Developer Notes

* We have migrated from ServiceStack to ASP.NET. Web API endpoints no longer accept HTTP Form requests; everything must be `application/json`. NOTE: Plugins that implement endpoints will also have to migrate.
* Plugins must now target `net5.0`.
* `IHttpClient` removal: Now inject `IHttpClientFactory` instead.
* `HttpException` removal: Now catch `HttpResponseException` instead.
* Services can be registered to the DI pipeline.

Please see the [Jellyfin Development Matrix channel](https://matrix.to/#/#jellyfin-dev:matrix.org) for questions or further details on these changes.

## Known Bugs/Tracker for 10.7.1 hotfix

Bugs which are already known and being worked on are listed in this issue: https://github.com/jellyfin/jellyfin-meta/issues/1

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/27

### [jellyfin](https://github.com/jellyfin/jellyfin) [599]

 * #5409 [@ikomhoog] Changed string.Length == 0 to string.IsNullOrEmpty in case of null
 * #5407 [@Bond-009] Fix casing CollectionType
 * #5406 [@cvium] do not throw ArgumentNullException in TryCleanString
 * #5402 [@Ullmie02] Use FileShare.None when creating files
 * #5383 [@cvium] do not pick a linked item as primary when merging versions
 * #5381 [@cvium] make sure network path substitution matches correctly
 * #5377 [@cvium] Do not use language or imagelanguages when searching for images with TMDb
 * #5375 [@crobibero] Specify defaults or set query parameter to nullable
 * #5356 [@cvium] return false when providerid is null or empty
 * #5345 [@BaronGreenback] Dual IP4 / IP6 server fails on non-windows platforms
 * #5342 [@BaronGreenback] Corrected logging message
 * #5339 [@Bond-009] Revert breaking change to HasProviderId
 * #5315 [@BaronGreenback] Fix for environment variable JELLYFIN_PublishedServerUrl being ignored.
 * #5312 [@BaronGreenback] Fix for #5280
 * #5301 [@Bond-009] Fix unchecked input
 * #5290 [@Bond-009] Fix possible null ref exception
 * #5278 [@BaronGreenback] Fix for #5168
 * #5275 [@BaronGreenback] Fixes #5148
 * #5274 [@BaronGreenback] Fix for #5254
 * #5270 [@Bond-009] TMDB: Also search with IMDB or TVDB Id if specified
 * #5263 [@Bond-009] TMDB: Include year in search
 * #5255 [@cvium] Validate the new username when renaming
 * #5251 [@crobibero] Fix vpp null reference
 * #5250 [@barronpm] Fix user renaming logic
 * #5230 [@orryverducci] Fix double rate deinterlacing for some TS files
 * #5217 [@dkanada] handle plugin manifests automatically
 * #5216 [@dkanada] remove deprecated settings from server config
 * #5208 [@crobibero] Add image file accept to openapi
 * #5207 [@matthin] Default to English metadata during the setup wizard.
 * #5200 [@crobibero] Update to dotnet 5.0.3
 * #5188 [@cvium] Exclude BOM when writing meta.json plugin manifest
 * #5181 [@BaronGreenback] Fixed IPHost.TryParse
 * #5171 [@Ullmie02] Fix forgot password pin request
 * #5154 [@crobibero] Don't skip hidden / system files when enumerating
 * #5117 [@nyanmisaka] Make FRAME-RATE field culture invariant
 * #5111 [@Larvitar] Remove season name from metadata result
 * #5107 [@nyanmisaka] Fix for NVDEC decoder and improvements for VAAPI tonemap
 * #5106 [@BaronGreenback] Fixes zero byte nfo files.
 * #5105 [@crobibero] Add null check for ImageTags
 * #5099 [@crobibero] Fix openapi nullable properties
 * #5095 [@Bond-009] Fix GetOrderBy and add tests
 * #5091 [@crobibero] Use ArrayModelBinder for sortBy and sortOrder
 * #5090 [@Ullmie02] Catch TypeLoadException during plugin load
 * #5073 [@BaronGreenback] Fix for 4933: Alternative ffmpeg fix
 * #5069 [@crobibero] Add ability to mark query parameter as obsolete
 * #5064 [@BaronGreenback] Plugin bug fixes
 * #5062 [@crobibero] Fix delete log task
 * #5031 [@crobibero] Update to dotnet 5.0.2
 * #5027 [@crobibero] Add parameter to disable sending first episode as next up
 * #5025 [@BaronGreenback] Fix DLNA PlayTo encoding issue
 * #5004 [@dkanada] remove unused notification type
 * #4997 [@crobibero] Require elevated auth to upload subtitles
 * #4980 [@Ullmie02] Add additional chinese languages
 * #4978 [@BaronGreenback] Fixes for multiple proxies
 * #4976 [@BaronGreenback] Fixed DLNA Server on RC2
 * #4970 [@BaronGreenback] Change split character
 * #4968 [@ianjazz246] Fix library with music directly under artist folder
 * #4962 [@thornbill] Fix capitalization of Playstate message
 * #4961 [@crobibero] Fix potential null reference
 * #4956 [@jceresini] Fix rpm package dependencies
 * #4936 [@crobibero] Fix inverted SkipWhile
 * #4935 [@ConfusedPolarBear] Remove used quick connect tokens
 * #4920 [@crobibero] Attach correct Blurhash to BaseItemPerson
 * #4911 [@Ullmie02] Change stable ci nuget build command
 * #4906 [@Spacetech] Ignore inaccessible files & folders during library scans
 * #4905 [@BaronGreenback] Null exception fix
 * #4902 [@BaronGreenback] Fixed loopback subnet
 * #4891 [@Artiume] Split resume function for Audiobooks
 * #4890 [@nielsvanvelzen] Fix search hint endpoint error
 * #4884 [@crobibero] Add JsonConverter for Nullable Guids
 * #4874 [@MrTimscampi] Enable TMDB and OMDB by default
 * #4872 [@BaronGreenback] Removed workaround code as web is now fixed.
 * #4863 [@nyanmisaka] Fix boxes in library name backdrop
 * #4861 [@crobibero] Fix null reference when logging
 * #4860 [@nyanmisaka] Avoid transcoding to 3ch audio for HLS streaming
 * #4859 [@Ullmie02] Don't build unstable Nuget packages on tags
 * #4856 [@nyanmisaka] Fix some profiles for H264 AMF encoder
 * #4855 [@crobibero] Initialize JsonSerializerOptions statically
 * #4852 [@ryanpetris] SchedulesDirect no longer refreshes channels properly
 * #4850 [@BaronGreenback] Null reference fix
 * #4847 [@crobibero] Fix another key collision in MigrateDisplayPreferencesDatabase
 * #4842 [@crobibero] Add JsonDateTimeConverter
 * #4836 [@crobibero] Return dashboardTheme when requesting DisplayPreferences
 * #4833 [@Ullmie02] Fix similar items endpoint for movies and TV
 * #4828 [@joshuaboniface] Add static Linux builds for arm and musl
 * #4824 [@crobibero] Add request parameters to OpenLiveStreamDto
 * #4821 [@BaronGreenback] Fix: Disable dlna server API responses if dlna is disabled.
 * #4819 [@crobibero] Set filename when downloading file
 * #4816 [@nyanmisaka] Fix some video profiles for Android client
 * #4807 [@nyanmisaka] Correct DLNA audio codecs for PS3 and PS4
 * #4803 [@ryanpetris] Fix Live TV Recording Scheduling
 * #4794 [@cvium] Convert from base64 when saving item images
 * #4792 [@cvium] Add missing seasons during AfterMetadataRefresh
 * #4789 [@crobibero] Fix get provider id extension
 * #4781 [@crobibero] Use request body for mapping xml channels
 * #4774 [@nyanmisaka] Fine tune some tone mapping params
 * #4773 [@Artiume] Remove opf extension for book types
 * #4771 [@crobibero] Use typed UserManager GetPreference
 * #4769 [@crobibero] Check correct fetcher list for provider name
 * #4767 [@nyanmisaka] Fix SSL certificate cannot be saved
 * #4762 [@crobibero] Fix openapi file schema
 * #4761 [@crobibero] Convert CreatePlaylist to use query params instead of body
 * #4758 [@nyanmisaka] Fix landing screen options
 * #4757 [@cvium] Remove ImageFetcherPostScanTask
 * #4756 [@crobibero] Fix inverted condition when authenticating with an ApiKey
 * #4753 [@crobibero] Update to dotnet 5.0.1
 * #4751 [@nyanmisaka] Use larger batch size on mpegts to avoid corrupted thumbnails
 * #4750 [@crobibero] Fix blueberry
 * #4749 [@crobibero] Serialize GUID without dashes
 * #4743 [@crobibero] Actually use library options when filtering metadata providers
 * #4741 [@Bond-009] Add tests for HdHomerunHost.GetLineup
 * #4738 [@Bond-009] Add tests for HdHomerunHost.GetModelInfo
 * #4737 [@crobibero] Add missing EnsureSuccessStatusCode
 * #4736 [@nyanmisaka] Fix custom library order
 * #4735 [@crobibero] Fix JsonConverter recursion
 * #4733 [@crobibero] Fix potential null reference in OMDB
 * #4730 [@crobibero] Don't serialize empty GUID to null
 * #4729 [@BaronGreenback] Disable DLNA when HTTPS is required
 * #4726 [@BaronGreenback] Fix - Access Denied on using certificates in windows as user.
 * #4724 [@BaronGreenback] Fix null reference error in Dlna PlayTo
 * #4722 [@crobibero] Fix API forbidden response
 * #4716 [@OancaAndrei] Update authorization policies for SyncPlay
 * #4715 [@crobibero] Add number to bool json converter
 * #4713 [@crobibero] Redirect robots.txt if hosting web content
 * #4711 [@barronpm] Add required attributes to parameters
 * #4710 [@OancaAndrei] Restore sessions in SyncPlay groups upon reconnection
 * #4709 [@BaronGreenback] Improved plugin management functionality
 * #4706 [@cvium] Only apply series image aspect ratio if episode/season has no primary image
 * #4701 [@crobibero] Don't return plugin versions that target newer Jellyfin version
 * #4699 [@crobibero] Fix CustomItemDisplayPreferences unique key collision in the migration
 * #4678 [@BaronGreenback] Change logging level and message in NetworkManager
 * #4675 [@BaronGreenback] Ability to use DNS names in KnownProxies
 * #4672 [@cvium] Fix MergeVersions endpoint
 * #4671 [@cvium] Clear KnownNetworks and KnownProxies if none are configured explicitly
 * #4669 [@MrTimscampi] Fix NPM command in CI
 * #4667 [@joshuaboniface] Remove obsolete erroring command
 * #4662 [@joshuaboniface] Fix bad do in bump_version
 * #4661 [@Bond-009] Remove spammy debug line
 * #4660 [@crobibero] Add support for web serving .mem files
 * #4653 [@crobibero] Optimize FavoritePersons query
 * #4652 [@crobibero] Add support for custom item display preferences
 * #4651 [@crobibero] Remove IIsoMounter and IsoMounter
 * #4648 [@nyanmisaka] Optimize load plugin logs
 * #4647 [@rhamzeh] fix: add Palestine to supported countries
 * #4645 [@crobibero] Move OpenApiSecurityScheme to OperationFilter
 * #4644 [@Bond-009] Minor improvements
 * #4643 [@crobibero] Fix null reference when getting filters of an empty library
 * #4638 [@crobibero] Don't die if folder doesn't have id
 * #4636 [@BaronGreenback] [Fix for 10.7] Missed a config move
 * #4633 [@crobibero] Use Guid as API parameter type where possible
 * #4632 [@crobibero] Fix MusicBrainz request Accept header
 * #4630 [@Bond-009] Add tests for GetUuid
 * #4629 [@crobibero] Provide NoResult instead of Fail in CustomAuthenticationHandler
 * #4628 [@MrTimscampi] Prevent GetUpNext from returning episodes in progress
 * #4626 [@nyanmisaka] Do not extract audio stream bitrate info for videos from formatInfo
 * #4625 [@crobibero] Fix OpenApi generation for BlurHash
 * #4623 [@dependabot[bot]] Bump Moq from 4.15.1 to 4.15.2
 * #4622 [@dependabot[bot]] Bump prometheus-net.DotNetRuntime from 3.4.0 to 3.4.1
 * #4621 [@dependabot[bot]] Bump ServiceStack.Text.Core from 5.10.0 to 5.10.2
 * #4620 [@nyanmisaka] Fix transcoding reasons report
 * #4613 [@BaronGreenback] [Fix] NotificationType was never set in dlna event manager
 * #4610 [@nyanmisaka] Extract tone mapped thumbnails for HDR videos
 * #4609 [@Bond-009] Add more tests for JsonGuidConverter
 * #4608 [@dkanada] Remove deprecated flag to disable music plugins
 * #4607 [@nyanmisaka] Fix the I-frame image extraction filter string
 * #4605 [@hawken93] Allow JsonGuidConverter to read null
 * #4597 [@nyanmisaka] Add NEO OpenCL runtime for Intel Tone mapping
 * #4595 [@MrTimscampi] Don't return first episodes in next up
 * #4594 [@nyanmisaka] Remove one redundant 'hwaccel vaapi' string
 * #4591 [@Bond-009] Clean up SchedulesDirect
 * #4589 [@ConfusedPolarBear] [Fix] Test query value
 * #4588 [@Bond-009] Remove Hex class as the BCL has one now
 * #4582 [@crobibero] Use proper Named HttpClient for MusicBrainz requests
 * #4580 [@crobibero] Specify default DateTimeKind from EFCore
 * #4575 [@crobibero] Don't throw null reference if ContentType is null.
 * #4574 [@joshuaboniface] Revert "Enable jellyfin.service unit on Fedora fresh install"
 * #4570 [@nyanmisaka] Add Tonemapping for Intel VAAPI
 * #4568 [@crobibero] Serialize Guid.Empty to null
 * #4563 [@crobibero] Fix sending PlaybackInfo
 * #4562 [@crobibero] Don't send activity event if notification type is null
 * #4557 [@crobibero] Fix namespace and add attribute for ClientCapabilitiesDto
 * #4554 [@joshuaboniface] Run explicit service start if restart failed
 * #4553 [@joshuaboniface] Enable jellyfin.service unit on Fedora fresh install
 * #4551 [@crobibero] Only trim file name if folder name is shorter
 * #4550 [@crobibero] Handle invalid plugins
 * #4548 [@orryverducci] Revert "Fix frame rate probing for interlaced MKV files"
 * #4545 [@BaronGreenback] [Fix] Null Pointer in TmdbMovieProvider
 * #4544 [@BaronGreenback] [Fix] Config option read from wrong place.
 * #4539 [@crobibero] Add NullableEnumModelBinder and NullableEnumModelBinderProvider
 * #4538 [@mario-campos] Implement CodeQL Static Analysis
 * #4537 [@crobibero] Convert ClientCapabilities to a Dto with JsonConverters
 * #4534 [@Bond-009] Remove UTF8 bom from some files
 * #4533 [@Bond-009] Fix nullref
 * #4526 [@crobibero] Fix marking item as played
 * #4525 [@crobibero] Set DeleteTranscodeFileTask to trigger every 24h
 * #4524 [@crobibero] Use sdk 5.x
 * #4523 [@crobibero] Set sdk version to 5.0
 * #4522 [@BaronGreenback] Set plugin version to that specified in the manifest
 * #4519 [@crobibero] Write DateTimes in ISO8601 format for backwards compatibility.
 * #4518 [@crobibero] Fix live tv hls playback
 * #4517 [@BaronGreenback] [Fix] Fixed Plugin versioning in browser notifications
 * #4516 [@oddstr13] Fix plugin old version cleanup
 * #4515 [@barronpm] Clean up DeviceManager and Don't Store Capabilities on Disk
 * #4514 [@Artiume] Update FFmpeg log
 * #4513 [@BaronGreenback] Multi-repository plugins
 * #4510 [@crobibero] Set default request accept headers
 * #4509 [@crobibero] Fix null reference when saving plugin configuration
 * #4507 [@BaronGreenback] Corrects spelling in comments
 * #4504 [@crobibero] Fix Environment authorization policy
 * #4503 [@Bond-009] Pass cancellation where possible
 * #4502 [@crobibero] Use ALL the decompression methods
 * #4501 [@ferferga] Don't scale extracted images and ffmpeg improvements
 * #4500 [@oddstr13] Use .NET 5.0 in Nuget pipeline
 * #4499 [@crobibero] Reduce RequestHelpers.Split usage and remove RequestHelpers.GetGuids
 * #4497 [@crobibero] Fix docker and centos builds
 * #4494 [@nyanmisaka] Add video range info to the title
 * #4493 [@crobibero] Fix dockerfiles
 * #4492 [@Artiume] update dotnet 5.0 buster image
 * #4490 [@dependabot[bot]] Bump Mono.Nat from 3.0.0 to 3.0.1
 * #4489 [@dependabot[bot]] Bump PlaylistsNET from 1.1.2 to 1.1.3
 * #4488 [@dependabot[bot]] Bump Moq from 4.14.7 to 4.15.1
 * #4487 [@crobibero] Upgrade all netcore3.1 to net5.0
 * #4486 [@crobibero] Remove api client generator errors
 * #4485 [@crobibero] Update user cache after updating user.
 * #4480 [@crobibero] Remove custom HttpException
 * #4478 [@Bond-009] Don't allocate single char arrays when possible
 * #4477 [@nyanmisaka] Fix return type for GetAttachment
 * #4476 [@crobibero] Fix plugin update exception
 * #4475 [@crobibero] Fix api client ci condition
 * #4474 [@crobibero] Convert array property to IReadOnlyList
 * #4473 [@crobibero] Don't throw exception when converting values using binder or JsonConv…
 * #4469 [@cvium] Change OPTIONS to POST and call SaveConfiguration in SetRepositories
 * #4468 [@cvium] Semi-revert removal of Name for /Similar in openapi
 * #4466 [@kayila] Fix #4465 by adding the missing extras folders.
 * #4463 [@crobibero] Skip migration if user doesn't exist
 * #4460 [@yodatak] Bump dependencies to Fedora 33
 * #4458 [@crobibero] Upgrade to Net5
 * #4456 [@martinek-stepan] Emby.Naming - nullable & code coverage
 * #4452 [@crobibero] Add ModelBinder to ImageType
 * #4450 [@cvium] Remove duplicate /Similar endpoints
 * #4448 [@crobibero] Don't throw exception if name is null
 * #4447 [@dependabot[bot]] Bump Serilog.Sinks.Graylog from 2.2.1 to 2.2.2
 * #4446 [@dependabot[bot]] Bump Microsoft.NET.Test.Sdk from 16.7.1 to 16.8.0
 * #4444 [@crobibero] Remove unstable npm ci task
 * #4443 [@cvium] Remove OriginalAuthenticationInfo and add IsAuthenticated property
 * #4440 [@neilsb] Perform hashing of Password for Schedules Direct on server
 * #4437 [@crobibero] Add missing dlna attributes.
 * #4434 [@BaronGreenback] Fixes #4423 - Fixes DLNA in unstable; 
 * #4432 [@nyanmisaka] Add initial support for HEVC over FMP4-HLS
 * #4428 [@crobibero] Add x-jellyfin-version to openapi spec
 * #4427 [@joshuaboniface] Reverse order of sudo and nohup
 * #4426 [@joshuaboniface] Remove spurious argument to nohup
 * #4425 [@joshuaboniface] Restore missing targetFolder
 * #4424 [@Bond-009] Minor perf improvements
 * #4422 [@crobibero] Add /Users/Me endpoint
 * #4420 [@cvium] Fix Persons, Genres and Studios endpoints
 * #4416 [@dkanada] Disable compatibility checks until they work again
 * #4413 [@cvium] Rename itemIds to ids
 * #4412 [@cvium] Save new display preferences
 * #4411 [@crobibero] Fix endpoint authorization requirements
 * #4410 [@crobibero] Set UserAgent when getting M3u playlist
 * #4409 [@crobibero] Fix API separators
 * #4408 [@crobibero] Dependency catch up
 * #4406 [@joshuaboniface] Remove jellyfin-ffmpeg dep from server package
 * #4405 [@nyanmisaka] Fix AAC direct streaming
 * #4403 [@Bond-009] Http1AndHttp2 is the default, no need to explicitly enable it
 * #4401 [@nyanmisaka] Respect music quality settings when transcoding
 * #4395 [@barronpm] Convert some code in UserManager to async
 * #4393 [@crobibero] Support IReadOnlyList in CommaDelimitedArrayModelBinder
 * #4392 [@crobibero] Fix LiveTV TS playback
 * #4391 [@crobibero] Support IReadOnlyList for JsonCommaDelimitedArrayConverter
 * #4388 [@crobibero] Add missing slashes in ffmpeg argument.
 * #4384 [@nyanmisaka] Fix HLS music playback on iOS
 * #4378 [@barronpm] Fix possible null reference exception
 * #4377 [@barronpm] Add caching to users
 * #4375 [@crobibero] Fix setting duplicate keys from auth header
 * #4371 [@cvium] Fix GET ScheduledTasks return value
 * #4369 [@orryverducci] Fix frame rate probing for interlaced MKV files
 * #4361 [@ssenart] Add FLAC and define the corresponding target sample rate
 * #4350 [@crobibero] Fix .npmrc
 * #4347 [@dependabot[bot]] Bump Moq from 4.14.6 to 4.14.7
 * #4346 [@dependabot[bot]] Bump prometheus-net from 3.6.0 to 4.0.0
 * #4342 [@crobibero] Add BaseItemManager
 * #4341 [@Bond-009] Minor improvements
 * #4339 [@BaronGreenback] Making default Plugin configurations accessible when developing. 
 * #4331 [@crobibero] Add npmAuthenticate task
 * #4330 [@crobibero] Fix ApiKey authentication
 * #4328 [@crobibero] Remove CommaDelimitedArrayModelBinderProvider
 * #4326 [@crobibero] Automatically clean activity log database
 * #4324 [@crobibero] Update to dotnet 3.1.9
 * #4317 [@Bond-009] Fix AudioBookListResolver test coverage
 * #4315 [@Jan-PieterBaert] Fix some warnings
 * #4312 [@crobibero] Add comma delimited string to array json converter
 * #4309 [@nielsvanvelzen] Make StartupWizardCompleted nullable in PublicSystemInfo
 * #4306 [@crobibero] Remove references to legacy scripts
 * #4305 [@crobibero] Convert image type string to enum.
 * #4304 [@crobibero] Convert exclude location type string to enum.
 * #4303 [@crobibero] Convert filters string to enum.
 * #4302 [@crobibero] Convert field string to enum.
 * #4301 [@crobibero] Fix comma delimited array model binder
 * #4300 [@crobibero] Fix ci npm install order
 * #4299 [@crobibero] Fix api client CI
 * #4298 [@crobibero] Remove TheTVDB plugin from server source.
 * #4292 [@crobibero] Add missing general commands
 * #4286 [@Bond-009] Minor improvements to tmdb code
 * #4285 [@cvium] Fix IWebSocketListener service registration
 * #4284 [@cvium] Fix playbackstart not triggering in the new eventmanager
 * #4281 [@crobibero] Fix registry name and link
 * #4279 [@joshuaboniface] Make MaxActiveSessions not nullable
 * #4277 [@dependabot[bot]] Bump Moq from 4.14.5 to 4.14.6
 * #4276 [@cvium] SecurityException should return 403
 * #4275 [@anthonylavado] Fix Transcode Cleanup Schedule
 * #4274 [@barronpm] Rewrite Activity Log Backend
 * #4273 [@joshuaboniface] Fix RPM spec again
 * #4271 [@joshuaboniface] Improve handling of apiclient generator
 * #4269 [@joshuaboniface] Add user max sessions options
 * #4268 [@Bond-009] Improve GroupInfo class
 * #4267 [@cvium] Disable invalid auth provider
 * #4266 [@Maxr1998] Log stream type and codec for missing direct play profile
 * #4265 [@KonH] Remove unnecessary null checks in some places
 * #4264 [@Camc314] Add missing properties to typescript axios generator
 * #4263 [@cvium] Defer image pre-fetching until the end of a refresh/scan
 * #4262 [@anthonylavado] Remove Windows legacy files
 * #4261 [@Spacetech] Make MusicBrainzAlbumProvider thread safe and fix retry logic
 * #4260 [@crobibero] Allow server to return .data files
 * #4259 [@ConfusedPolarBear] Accept ImageFormat as API parameter
 * #4257 [@Bond-009] Add tests for deserializing guids
 * #4255 [@crobibero] Generate document file for openapi spec in CI
 * #4254 [@BaronGreenback] Fix for #4241: Plugin config initialisation.
 * #4253 [@BaronGreenback] DI in plugins
 * #4252 [@skyfrk] Convert supportedCommands strings to enums
 * #4249 [@EraYaN] Publish OpenAPI spec for master and tagged releases
 * #4248 [@crobibero] Manually register models used in websocket messages.
 * #4247 [@crobibero] Update all on-disk plugins
 * #4243 [@jlechem] Removing string we don't use anymore.
 * #4242 [@Spacetech] Increase library scan and metadata refresh speed
 * #4236 [@ConfusedPolarBear] Fix some warnings
 * #4233 [@dependabot[bot]] Bump Mono.Nat from 2.0.2 to 3.0.0
 * #4232 [@dependabot[bot]] Bump TvDbSharper from 3.2.1 to 3.2.2
 * #4231 [@dependabot[bot]] Bump Serilog.Sinks.Graylog from 2.1.3 to 2.2.1
 * #4230 [@dependabot[bot]] Bump BlurHashSharp.SkiaSharp from 1.1.0 to 1.1.1
 * #4229 [@dependabot[bot]] Bump BlurHashSharp from 1.1.0 to 1.1.1
 * #4228 [@dependabot[bot]] Bump IPNetwork2 from 2.5.224 to 2.5.226
 * #4227 [@dependabot[bot]] Bump Swashbuckle.AspNetCore.ReDoc from 5.5.1 to 5.6.3
 * #4226 [@dependabot[bot]] Bump Swashbuckle.AspNetCore from 5.5.1 to 5.6.3
 * #4225 [@Spacetech] Check response status code before saving images
 * #4222 [@Spacetech] Use ConcurrentDictionary's in DirectoryService
 * #4221 [@Spacetech] Fix InvalidOperationException in TvdbSeriesProvider.MapSeriesToResult
 * #4220 [@Spacetech] Fix invalid operation exception in TvdbEpisodeImageProvider.GetImages
 * #4219 [@Spacetech] Increase initial scan speed for music libraries
 * #4217 [@crobibero] Properly handle null structs in json
 * #4213 [@cvium] Add ProgressiveFileStream
 * #4212 [@BaronGreenback] Null Pointer fix: BaseControlHandler.cs
 * #4211 [@BaronGreenback] Null Pointer Fix : PlayToController.cs
 * #4210 [@nielsvanvelzen] Use enum for WebSocket message types
 * #4209 [@cvium] Add Dto to ForgotPassword
 * #4208 [@cvium] Fix Identify by renaming route parameter to match function argument
 * #4207 [@joshuaboniface] Revamp the main README
 * #4205 [@cvium] Fix aspect ratio calculation sometimes returning 0 or 1
 * #4204 [@cvium] Add series image aspect ratio when ep/season is missing an image
 * #4202 [@cvium] Migrate the TMDb providers to the TMDbLib library
 * #4200 [@ryanpetris] HDHomeRun: Preemptively throw a LiveTvConflictException
 * #4199 [@ryanpetris] Fix stream performance when opening/closing new streams.
 * #4194 [@nvllsvm] Optimize images
 * #4192 [@nielsvanvelzen] Use GeneralCommandType enum in GeneralCommand
 * #4189 [@Bond-009] Minor improvements
 * #4187 [@BaronGreenback] Fix for #4184 when no FFMPEG path set.
 * #4186 [@BaronGreenback] Fixes #4185 : FFMPeg version match exception.
 * #4183 [@Ullmie02] Fix TMDB Season Images
 * #4182 [@ryanpetris] Fix HD Home Run streaming
 * #4178 [@hoanghuy309] Update LocalizationManager.cs
 * #4177 [@cvium] Remove dummy season and missing episode provider
 * #4176 [@MrTimscampi] Update SkiaSharp.NativeAssets.Linux to 2.80.2
 * #4173 [@BaronGreenback] Unstable: Various controller fixes.
 * #4171 [@nyanmisaka] Add tonemapping for AMD AMF
 * #4170 [@BaronGreenback] Plugin versioning - amended for plugins without meta.json
 * #4169 [@stanionascu] Playback (direct-stream/transcode) of BDISO/BDAV containers
 * #4164 [@spooksbit] Removed browser auto-launch functionality
 * #4163 [@Bond-009] Minor improvements
 * #4162 [@BaronGreenback] Fix for #4161: BaseUrl in DLNA
 * #4156 [@androiddevnotes] Fix typos
 * #4145 [@dependabot[bot]] Bump SkiaSharp from 2.80.1 to 2.80.2
 * #4142 [@olsh] Fix parameters validation in ImageProcessor.GetCachePath
 * #4139 [@BaronGreenback] DLNA MediaRegistrar - static and commented.
 * #4138 [@BaronGreenback] DLNA ContentManager - static and commented.
 * #4137 [@BaronGreenback] DLNA ConnectionManager - static and commented.
 * #4136 [@BaronGreenback] DLNA Classes - No code change, just added commenting to classes. 
 * #4128 [@derchu] Update content rating from thetvdb
 * #4126 [@crobibero] update to dotnet 3.1.8
 * #4125 [@BaronGreenback] Networking 2 (Cumulative PR) - Swapping over to new NetworkManager 
 * #4121 [@cvium] Normalize application paths
 * #4118 [@SegiH] Change default value for allow duplicates in playlist option to False
 * #4116 [@cvium] Add Known Proxies to system configuration
 * #4114 [@crobibero] Add new files to rpm build
 * #4108 [@Bond-009] Minor performance improvements to item saving
 * #4106 [@Keridos] some testing for AudioBook
 * #4103 [@Bond-009] Fix some warnings
 * #4102 [@cvium] Skip startup message for /system/ping
 * #4096 [@crobibero] Fix catching authentication exception
 * #4094 [@crobibero] Fix redirection
 * #4093 [@crobibero] Fix api routes
 * #4092 [@crobibero] Add missing FromRoute, Required attribute
 * #4084 [@BaronGreenback] Unstable: PlayTo corruption url fix
 * #4082 [@cromefire] More expressive names for the VideoStream API
 * #4079 [@dependabot[bot]] Bump SQLitePCLRaw.bundle_e_sqlite3 from 2.0.3 to 2.0.4
 * #4078 [@Bond-009] Minor improvements
 * #4077 [@BaronGreenback] Simplified Code: Removed code which was never used.
 * #4076 [@Bond-009] Fix some warnings
 * #4075 [@BaronGreenback] Simplified Code: Removed code which was never used.
 * #4074 [@cvium] Fix null exception in tmdb episode provider
 * #4073 [@Bond-009] Fix ObjectDisposedException
 * #4071 [@Bond-009] Fix sln file
 * #4070 [@crobibero] Add ci task to publish api client
 * #4069 [@crobibero] Make all FromRoute required
 * #4068 [@barronpm] Fix Plugin Events and Clean Up InstallationManager.cs
 * #4067 [@barronpm] DisplayPreferences fixes
 * #4065 [@BaronGreenback] Bug Fix : DLNA Server advertising
 * #4063 [@BaronGreenback] Our of Memory fix when streaming large files
 * #4062 [@BaronGreenback] Fix for #4059
 * #4061 [@BaronGreenback] Fix for #4060
 * #4057 [@crobibero] Add flag for startup completed
 * #4055 [@Ullmie02] Enable HTTP Range Processing (Fix seeking)
 * #4054 [@lmaonator] Fix TVDB plugin not handling absolute display order
 * #4053 [@thornbill] Fix aac mime-type
 * #4051 [@crobibero] Replace swagger logo with jellyfin logo
 * #4048 [@crobibero] Remove GenerateDocumentationFile
 * #4047 [@crobibero] Use efcore library for health check
 * #4046 [@EraYaN] Enable code coverage and upload OpenAPI spec.
 * #4045 [@crobibero] Add db health check
 * #4043 [@cvium] Split HttpListenerHost into middlewares
 * #4042 [@EraYaN] Fixes for CI Nuget package pushing and CI triggers
 * #4041 [@EraYaN] Add the item path to the ItemLookupInfo class
 * #4039 [@cvium] Remove ServiceStack and related stuff
 * #4037 [@crobibero] Set openapi schema type to file where possible
 * #4035 [@crobibero] Fix apidoc routes with base url
 * #4034 [@barronpm] Fix all warnings in Jellyfin.Data
 * #4033 [@crobibero] Readd nullable number converters
 * #4031 [@Bond-009] Fix some warnings
 * #4030 [@crobibero] Remove IHttpClient
 * #4028 [@crobibero] Properly verify cache duration
 * #4027 [@cvium] Fix model binding in UpdateLibraryOptions
 * #4026 [@dependabot[bot]] Bump prometheus-net.DotNetRuntime from 3.3.1 to 3.4.0
 * #4024 [@dependabot[bot]] Bump IPNetwork2 from 2.5.211 to 2.5.224
 * #4022 [@Bond-009] Fix incorrect usage of ArrayPool
 * #4018 [@barronpm] Library Entity Cleanup
 * #4013 [@crobibero] Allow CORS domains to be configured
 * #4010 [@cromefire] Fix wrong OpenAPI auth header value
 * #4008 [@crobibero] Include xml docs when publishing
 * #4002 [@crobibero] Fix partial library and channel access
 * #4001 [@brianjmurrell] Add an empty %files section to main package
 * #3999 [@PrplHaz4] [Permissions] Fix for individual channel plugins #2858
 * #3988 [@crobibero] Use proper SPDX Identifier
 * #3984 [@crobibero] Use Prerelease System.Text.Json
 * #3983 [@Bond-009] Fix incorrect adding of user agent
 * #3977 [@barronpm] Make LibraryController.GetDownload async
 * #3976 [@nyanmisaka] Expose max_muxing_queue_size to user
 * #3975 [@nyanmisaka] Increase the max muxing queue size for ffmpeg
 * #3961 [@crobibero] Ignore null json values
 * #3959 [@Bond-009] Enable TreatWarningsAsErrors for Emby.Data in Release
 * #3958 [@Bond-009] Enable TreatWarningsAsErrors for MediaBrowser.Controller in Release
 * #3955 [@Bond-009] Make some methods async
 * #3954 [@Ullmie02] Use backdrop with library name as library thumbnail
 * #3953 [@crobibero] bump DotNet.Glob
 * #3951 [@crobibero] Add nullable int32, int64 json converters
 * #3950 [@crobibero] Fix dlna play to
 * #3947 [@Bond-009] Fix all warnings in Emby.Dlna
 * #3946 [@crobibero] Clean up output formatters
 * #3943 [@Bond-009] Simplify FFmpeg detection code
 * #3942 [@Ullmie02] Reduce warnings in Emby.Dlna
 * #3941 [@crobibero] Conver all remaining form request to body
 * #3939 [@Bond-009] Make MediaBrowser.MediaEncoding warnings free
 * #3938 [@crobibero] Fix conflicting audio routes
 * #3935 [@crobibero] Add Default Http Client
 * #3932 [@crobibero] Add support for custom api-doc css
 * #3928 [@Mygod] Add 1440p to the mix
 * #3925 [@crobibero] Remove IHttpClient from Providers
 * #3910 [@barronpm] Event Rewrite (Part 1)
 * #3908 [@crobibero] Use proper mediatypename
 * #3907 [@crobibero] Fix DLNA Routes
 * #3903 [@crobibero] Add xml output formatter
 * #3899 [@crobibero] Install specific plugin version if requested
 * #3898 [@crobibero] Return int64 in json as number
 * #3895 [@crobibero] Remove IHttpClient from Jellyfin.Api
 * #3894 [@barronpm] Remove ListHelper.cs
 * #3892 [@barronpm] Minor fixes to LiveTvMediaSourceProvider
 * #3891 [@barronpm] Remove unused methods in IDtoService
 * #3889 [@Ullmie02] Build Unstable NuGet packages
 * #3886 [@crobibero] bump deps
 * #3880 [@DirtyRacer1337] Fix year parsing
 * #3879 [@cvium] Populate ThemeVideoIds and ThemeSongIds
 * #3877 [@orryverducci] Deinterlacing improvements
 * #3874 [@danieladov] Fix MergeVersions()
 * #3872 [@crobibero] Fix setting user policy
 * #3871 [@Ullmie02] Allow plugins to define their own api endpoints
 * #3868 [@dependabot[bot]] Bump ServiceStack.Text.Core from 5.9.0 to 5.9.2
 * #3867 [@dependabot[bot]] Bump TvDbSharper from 3.2.0 to 3.2.1
 * #3866 [@dependabot[bot]] Bump Microsoft.NET.Test.Sdk from 16.6.1 to 16.7.0
 * #3865 [@dependabot[bot]] Bump Swashbuckle.AspNetCore.ReDoc from 5.3.3 to 5.5.1
 * #3863 [@EraYaN] Add nohup and continueOnError to the Collect Artifacts task
 * #3861 [@crobibero] API Fixes
 * #3860 [@cvium] Fix collages
 * #3859 [@crobibero] Fix Requirement assigned to Handler
 * #3858 [@cvium] Fix startup wizard redirect
 * #3854 [@danieladov] Fix Split versions
 * #3851 [@barronpm] Clean up LibraryChangedNotifier.
 * #3849 [@barronpm] Make DisplayPreferencesManager Scoped
 * #3846 [@YouKnowBlom] Avoid including stray commas in HLS codecs field
 * #3841 [@Bond-009] Fix warnings
 * #3840 [@barronpm] Fix MemoryCache Usage.
 * #3838 [@Bond-009] MemoryStream optimizations
 * #3837 [@cvium] Fix BaseItems not being cached in-memory
 * #3836 [@cvium] Remove rate limit from TMDb provider
 * #3835 [@cvium] Throw HttpException when tvdb sends us crap data
 * #3834 [@cvium] Make external ids nullable in TMDb
 * #3831 [@joshuaboniface] Bump to .NET Core SDK 3.1.302
 * #3824 [@barronpm] Clean up TunerHost Classes
 * #3822 [@EraYaN] Merge the args and commands item for the artifact collection
 * #3820 [@Bond-009] Fix some warnings
 * #3816 [@cvium] Change OnRefreshStart and OnRefreshComplete logging levels to debug
 * #3812 [@barronpm] Merge API Migration into master
 * #3810 [@AlfHou] Fix README links and note about setup wizard
 * #3809 [@Bond-009] Minor improvements
 * #3806 [@dkanada] Disable compatibility checks for now
 * #3805 [@dependabot[bot]] Bump Mono.Nat from 2.0.1 to 2.0.2
 * #3804 [@dependabot[bot]] Bump Serilog.AspNetCore from 3.2.0 to 3.4.0
 * #3803 [@dependabot[bot]] Bump sharpcompress from 0.25.1 to 0.26.0
 * #3802 [@dependabot[bot]] Bump PlaylistsNET from 1.0.6 to 1.1.2
 * #3801 [@michael9dk] Update README.md (fix broken links)
 * #3795 [@anthonylavado] Update to newer Jellyfin.XMLTV
 * #3792 [@cvium] TMDb: Change Budget and Revenue to long to avoid overflow
 * #3790 [@cvium] Remove some unnecessary string allocations
 * #3784 [@barronpm] Minor fixes to ActivityManager
 * #3782 [@Bond-009] Minor fixes for websocket code
 * #3774 [@EraYaN] Add a much shorter timeout to the CollectArtifacts job
 * #3772 [@EraYaN] Updated SkiaSharp to 2.80.1 and replace resize code to fix bad quality
 * #3769 [@dkanada] Remove useless order step for intros
 * #3761 [@cvium] Fix DI memory leak
 * #3760 [@thornbill] Fix inverted logic for LAN IP detection
 * #3759 [@AlfHou] Change 'nowebcontent' flag to 'nowebclient' flag in readme
 * #3757 [@cvium] Update BlurHashSharp and set max size to 128x128
 * #3747 [@barronpm] Use Memory Cache
 * #3740 [@Bond-009] Optimize Substring and StringBuilder usage
 * #3728 [@nyanmisaka] adjust priority in outputSizeParam cutter
 * #3727 [@K900] Fix #3624
 * #3725 [@joshuaboniface] Flip quoting in variable set command
 * #3724 [@joshuaboniface] Bump master version to 10.7.0 for next release
 * #3723 [@joshuaboniface] Get and tag with the actual release version in CI
 * #3720 [@joshuaboniface] Fix bump_version so it works properly
 * #3711 [@yrjyrj123] Fix the problem that hardware decoding cannot be used on macOS.
 * #3704 [@oddstr13] Don't ignore dot directories or movies/episodes with sample in their name.
 * #3703 [@oddstr13] Allow space in username
 * #3699 [@oddstr13] Fix embedded subtitles
 * #3690 [@MichaIng] Fix left /usr/bin/jellyfin symlink on removal and typo
 * #3684 [@Bond-009] Fix warnings
 * #3683 [@nyanmisaka] Allows to provide multiple fallback fonts for client to render subtitles
 * #3679 [@barronpm] Use System.Text.Json in DefaultPasswordResetProvider
 * #3678 [@barronpm] Remove Unused Dependencies.
 * #3677 [@barronpm] Fixed compilation error on master.
 * #3675 [@ferferga] fix typo in debian's config file
 * #3671 [@Bond-009]  Make UNIX socket configurable 
 * #3666 [@barronpm] Use System.Text.Json in LiveTvManager
 * #3665 [@barronpm] Use interfaces in app host constructors
 * #3664 [@Bond-009] Make CreateUser async
 * #3663 [@crobibero] Add missing usings to UserManager
 * #3660 [@crobibero] Force plugin config location
 * #3659 [@Bond-009] Optimize StringBuilder.Append calls
 * #3657 [@Bond-009] Review usage of string.Substring (part 1)
 * #3649 [@thornbill] Skip image processing for live tv sources
 * #3646 [@barronpm] Make IncrementInvalidLoginAttemptCount async.
 * #3642 [@crobibero] Try adding plugin repository again
 * #3634 [@crobibero] fix built in plugin js
 * #3632 [@azlm8t] tvdb: Log path on lookup errors
 * #3620 [@BaronGreenback] Fix for #3607 and #3515
 * #3616 [@crobibero] Allow migration to optionally run on fresh install
 * #3615 [@nyanmisaka] Fix QSV device creation on Comet Lake
 * #3613 [@Bond-009] Replace \d with [0-9] in ffmpeg detection and scan code
 * #3609 [@Bond-009] Fix warnings
 * #3604 [@joshuaboniface] Fix bad Debuntu dependencies
 * #3602 [@crobibero] Fix username case change
 * #3598 [@barronpm] Clean up ProviderManager.cs
 * #3597 [@barronpm] Jellyfin.Drawing.Skia Cleanup
 * #3595 [@Bond-009] Improve DescriptionXmlBuilder
 * #3578 [@barronpm] Migrate Display Preferences to EF Core
 * #3577 [@crobibero] Specify plugin repo on plugin installation
 * #3576 [@HelloWorld017] Fix SAMI UTF-16 Encoding Bug
 * #3552 [@BaronGreenback] Fixes #3551 (Notifications Serialization error)
 * #3532 [@Ullmie02] Add support for binding to Unix socket
 * #3521 [@sachk] Fix support for mixed-protocol subtitles
 * #3508 [@BaronGreenback] Part 1: nullable Emby.DLNA
 * #3442 [@nyanmisaka] Tonemapping function relying on OpenCL filter and NVENC HEVC decoder
 * #3401 [@BaronGreenback] Fix for windows plug-in upgrades issue: #1623 
 * #3366 [@barronpm] Remove UserManager.AddParts
 * #3216 [@rotvel] Try harder at detecting ffmpeg version and enable the validation
 * #3196 [@ferferga] Remove "download images in advance" option
 * #3194 [@OancaAndrei] SyncPlay for TV series (and Music)
 * #3086 [@redSpoutnik] Add Post subtitle in API
 * #3053 [@rigtorp] Add additional resolver tests
 * #2888 [@ConfusedPolarBear] Add quick connect (login without typing password)
 * #2788 [@ThatNerdyPikachu] Use embedded title for other track types

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [474]

 * jellyfin/jellyfin-web#2482 [@cvium] don't use Locations as an indicator for AddLibrary
 * jellyfin/jellyfin-web#2473 [@thornbill] Add hash to bundle urls for cache busting
 * jellyfin/jellyfin-web#2470 [@pgeorgi] browser.js: Avoid misdetecting Chrome OS as OS X
 * jellyfin/jellyfin-web#2461 [@thornbill] Remove iOS bandwidth limit
 * jellyfin/jellyfin-web#2443 [@dmitrylyzo] Fix attachment delivery urls
 * jellyfin/jellyfin-web#2442 [@dkanada] minor improvements to plugin pages
 * jellyfin/jellyfin-web#2417 [@MrLemur] Change babel.config.js sourceType to unamiguous
 * jellyfin/jellyfin-web#2378 [@dkanada] update style for active sessions
 * jellyfin/jellyfin-web#2375 [@ferferga] fix: message appearing after adding repositories
 * jellyfin/jellyfin-web#2374 [@cvium] reject play access validation promise
 * jellyfin/jellyfin-web#2358 [@Alcatraz077] Allows Search On Tizen
 * jellyfin/jellyfin-web#2357 [@thornbill] Fix epub player height
 * jellyfin/jellyfin-web#2356 [@ferferga] fix: notched devices area not covered
 * jellyfin/jellyfin-web#2353 [@thornbill] Fix scaling in comics player
 * jellyfin/jellyfin-web#2350 [@nyanmisaka] Options for enhanced NVDEC and VPP tonemap
 * jellyfin/jellyfin-web#2344 [@ferferga] refactor: remove unused imports
 * jellyfin/jellyfin-web#2343 [@dkanada] fix image alignment on plugin cards
 * jellyfin/jellyfin-web#2327 [@MrChip53] Edit admin dashboard menu for plugins
 * jellyfin/jellyfin-web#2323 [@jarnedemeulemeester] Fix replay icon not getting replaced with play_arrow icon
 * jellyfin/jellyfin-web#2318 [@thornbill] Fix removed ButtonDelete key
 * jellyfin/jellyfin-web#2313 [@dmitrylyzo] Fix browser detection: Safari vs Tizen
 * jellyfin/jellyfin-web#2312 [@jarnedemeulemeester] Use local version of Noto Sans if available
 * jellyfin/jellyfin-web#2311 [@nielsvanvelzen] Disable multi download option
 * jellyfin/jellyfin-web#2309 [@ferferga] fix(card): white flashing images
 * jellyfin/jellyfin-web#2306 [@thornbill] Fix tiny card icons
 * jellyfin/jellyfin-web#2293 [@thornbill] Fix latest tab links for tv and music
 * jellyfin/jellyfin-web#2290 [@MrTimscampi] Add Chromecast error messages to the locales
 * jellyfin/jellyfin-web#2288 [@joshuaboniface] Bump API client to 1.6.0
 * jellyfin/jellyfin-web#2286 [@Artiume] Split Audiobook Resume
 * jellyfin/jellyfin-web#2283 [@thornbill] Allow decimal entry for bitrate on mobile
 * jellyfin/jellyfin-web#2280 [@Artiume] Add missing Languages to Web
 * jellyfin/jellyfin-web#2269 [@dkanada] Fix issue with double click fullscreen
 * jellyfin/jellyfin-web#2265 [@MrTimscampi] Sort items by premiere date on the details page
 * jellyfin/jellyfin-web#2263 [@MrTimscampi] Fix OSD gradients not letting pointer events through
 * jellyfin/jellyfin-web#2260 [@thornbill] Fix chevron centering on home section titles
 * jellyfin/jellyfin-web#2258 [@thornbill] Restore the dashboard theme option
 * jellyfin/jellyfin-web#2247 [@thornbill] Always allow stopping via the action menu
 * jellyfin/jellyfin-web#2246 [@thornbill] Fix layout issues on mobile item details
 * jellyfin/jellyfin-web#2244 [@Artiume] Fix Continue Listening
 * jellyfin/jellyfin-web#2242 [@thornbill] Replace bash prepare script with node version
 * jellyfin/jellyfin-web#2240 [@thornbill] Remove duplicate try/catch
 * jellyfin/jellyfin-web#2239 [@thornbill] Disable browser hack rule for sass files
 * jellyfin/jellyfin-web#2238 [@thornbill] Fix restart button being shown when unsupported
 * jellyfin/jellyfin-web#2237 [@thornbill] Fix layout of plugin cards
 * jellyfin/jellyfin-web#2236 [@thornbill] Fix touch support in epub reader
 * jellyfin/jellyfin-web#2234 [@thornbill] Use Noto Sans from Fontsource
 * jellyfin/jellyfin-web#2225 [@BaronGreenback] Plugin manager changes
 * jellyfin/jellyfin-web#2224 [@Delgan]  Fix possible HLSError (BufferFullError) on Firefox
 * jellyfin/jellyfin-web#2222 [@nyanmisaka] Modify some tone mapping related strings
 * jellyfin/jellyfin-web#2220 [@dependabot[bot]] Bump ini from 1.3.5 to 1.3.7
 * jellyfin/jellyfin-web#2219 [@crobibero] Set Content-Type header when creating a playlist
 * jellyfin/jellyfin-web#2218 [@thornbill] Fix style issues on dashboard page
 * jellyfin/jellyfin-web#2217 [@nyanmisaka] Landing screen options clean up
 * jellyfin/jellyfin-web#2216 [@dmitrylyzo] Fix canPlay for Live TV
 * jellyfin/jellyfin-web#2215 [@dmitrylyzo] Fix multiplication of event listeners on Live TV pages
 * jellyfin/jellyfin-web#2214 [@dmitrylyzo] Fix LiveTV group anchors
 * jellyfin/jellyfin-web#2213 [@thornbill] Fix sonarqube bugs
 * jellyfin/jellyfin-web#2211 [@thornbill] Fix invalid dlna profile path
 * jellyfin/jellyfin-web#2210 [@nyanmisaka] Set the step of subtitle offset slider to 0.1
 * jellyfin/jellyfin-web#2202 [@thornbill] Remove reference to sharing help element
 * jellyfin/jellyfin-web#2195 [@OancaAndrei] Fix SyncPlay switching to next item in queue
 * jellyfin/jellyfin-web#2188 [@dmitrylyzo] Fix anchor click action and plugin configuration page URL
 * jellyfin/jellyfin-web#2186 [@Maxr1998] Fix plugin loader for function definitions in window
 * jellyfin/jellyfin-web#2183 [@dmitrylyzo] SyncPlay, don't use bad ApiClient
 * jellyfin/jellyfin-web#2181 [@MrTimscampi] Remove non-existing UserData field from requests
 * jellyfin/jellyfin-web#2177 [@anthonylavado] Update the API Client version
 * jellyfin/jellyfin-web#2175 [@thornbill] Fix invalid guide link
 * jellyfin/jellyfin-web#2174 [@thornbill] Fix comics player
 * jellyfin/jellyfin-web#2173 [@Maxr1998] Simplify hiding menu items based on supported features
 * jellyfin/jellyfin-web#2172 [@Maxr1998] Fix local bind address using wrong config value
 * jellyfin/jellyfin-web#2171 [@nyanmisaka] Fix the issue where the bitrate option is always Auto
 * jellyfin/jellyfin-web#2165 [@Maxr1998] Fix select server item in drawer menu
 * jellyfin/jellyfin-web#2164 [@thornbill] Fix more link issues
 * jellyfin/jellyfin-web#2163 [@thornbill] Prevent default submit event on add plugin repo form
 * jellyfin/jellyfin-web#2162 [@h1dden-da3m0n] update(ci): dependabot config from v1 to v2
 * jellyfin/jellyfin-web#2161 [@thornbill] Add item path to card data to support canPlay check
 * jellyfin/jellyfin-web#2160 [@thornbill] Fix multiple hashes added to route
 * jellyfin/jellyfin-web#2159 [@thornbill] Plugin manager improvements
 * jellyfin/jellyfin-web#2158 [@thornbill] Fix opening links with middle click or open in new tab
 * jellyfin/jellyfin-web#2156 [@thornbill] Prevent merge conflicts action from running on forks
 * jellyfin/jellyfin-web#2155 [@thornbill] Improve QuickConnect ux
 * jellyfin/jellyfin-web#2153 [@thornbill] Add github action to label PRs with merge conflicts
 * jellyfin/jellyfin-web#2152 [@thornbill] Add config option to include cookies in playback requests
 * jellyfin/jellyfin-web#2150 [@thornbill] Fix plugin initialization for dynamic imports
 * jellyfin/jellyfin-web#2149 [@thornbill] Make disabled rules trigger warnings
 * jellyfin/jellyfin-web#2148 [@nyanmisaka] Fix the BufferFullError on Chromium based browsers
 * jellyfin/jellyfin-web#2147 [@dependabot-preview[bot]] Bump expose-loader from 1.0.1 to 1.0.3
 * jellyfin/jellyfin-web#2146 [@dependabot-preview[bot]] Bump @babel/core from 7.12.7 to 7.12.9
 * jellyfin/jellyfin-web#2145 [@dependabot-preview[bot]] Bump core-js from 3.7.0 to 3.8.0
 * jellyfin/jellyfin-web#2144 [@dependabot-preview[bot]] Bump babel-loader from 8.2.1 to 8.2.2
 * jellyfin/jellyfin-web#2143 [@dependabot-preview[bot]] Bump webpack from 5.6.0 to 5.9.0
 * jellyfin/jellyfin-web#2142 [@thornbill] Reenable no unresolved import rule and fix playlist imports
 * jellyfin/jellyfin-web#2141 [@thornbill] Add api key to remote image urls
 * jellyfin/jellyfin-web#2140 [@thornbill] Fix use of global ApiClient in authenticate middleware
 * jellyfin/jellyfin-web#2139 [@nielsvanvelzen] Support async plugin loading from window
 * jellyfin/jellyfin-web#2138 [@nyanmisaka] Fix the overlap in iOS music view and the hidden nowPlayingBar
 * jellyfin/jellyfin-web#2137 [@nielsvanvelzen] Pass plugin name to pluginManager.loadPlugin
 * jellyfin/jellyfin-web#2135 [@nyanmisaka] Do not use AC3 for audio transcoding if AAC and MP3 are supported
 * jellyfin/jellyfin-web#2131 [@dmitrylyzo] Fix babel support for legacy browsers
 * jellyfin/jellyfin-web#2130 [@hawken93] fix login autocomplete
 * jellyfin/jellyfin-web#2129 [@dmitrylyzo] Prevent doubleclick on buttons from bubbling to video for fullscreen (alternative)
 * jellyfin/jellyfin-web#2128 [@nyanmisaka] Fix the inconsistent header button size in dashboard
 * jellyfin/jellyfin-web#2127 [@thornbill] Remove standalone.js and broken navigation
 * jellyfin/jellyfin-web#2126 [@thornbill] Fix arabic import from date-fns
 * jellyfin/jellyfin-web#2124 [@thornbill] Add stylelint for sass files
 * jellyfin/jellyfin-web#2122 [@thornbill] Use static imports for html templates
 * jellyfin/jellyfin-web#2121 [@thornbill] Fix fetcher settings html import
 * jellyfin/jellyfin-web#2120 [@thornbill] Revert change to base font size
 * jellyfin/jellyfin-web#2119 [@nyanmisaka] Show tonemap options for VAAPI
 * jellyfin/jellyfin-web#2118 [@hawken93] simplify server address candidates
 * jellyfin/jellyfin-web#2117 [@thornbill] Add linters to github actions
 * jellyfin/jellyfin-web#2116 [@thornbill] Disable chromecast in unsupported browsers
 * jellyfin/jellyfin-web#2111 [@dkanada] fix possible issue with server detection
 * jellyfin/jellyfin-web#2110 [@dependabot-preview[bot]] Bump @babel/preset-env from 7.12.1 to 7.12.7
 * jellyfin/jellyfin-web#2109 [@dependabot-preview[bot]] Bump stylelint from 13.7.2 to 13.8.0
 * jellyfin/jellyfin-web#2108 [@dependabot-preview[bot]] Bump copy-webpack-plugin from 6.3.0 to 6.3.2
 * jellyfin/jellyfin-web#2107 [@dependabot-preview[bot]] Bump sass-loader from 10.0.5 to 10.1.0
 * jellyfin/jellyfin-web#2106 [@dependabot-preview[bot]] Bump eslint from 7.13.0 to 7.14.0
 * jellyfin/jellyfin-web#2105 [@dependabot-preview[bot]] Bump @babel/core from 7.12.3 to 7.12.7
 * jellyfin/jellyfin-web#2104 [@thornbill] Remove unused files and dependencies
 * jellyfin/jellyfin-web#2103 [@BaronGreenback] [Fix] Removed SeriesInfo attribute.
 * jellyfin/jellyfin-web#2101 [@oddstr13] Take baseurl into account, use original url, not LocalAddress
 * jellyfin/jellyfin-web#2100 [@BaronGreenback] [RC Fix] Hide some network options until next release
 * jellyfin/jellyfin-web#2098 [@thornbill] Fix missing jellyfin-noto resources
 * jellyfin/jellyfin-web#2097 [@thornbill] Fix standalone crash due to missing apiclient
 * jellyfin/jellyfin-web#2096 [@mario-campos] Implement CodeQL Static Analysis
 * jellyfin/jellyfin-web#2095 [@thornbill] Fix epub player issues
 * jellyfin/jellyfin-web#2094 [@nyanmisaka] Fix Airplay in Safari
 * jellyfin/jellyfin-web#2093 [@thornbill] Fix pdfjs import
 * jellyfin/jellyfin-web#2092 [@hawken93] restore Assets
 * jellyfin/jellyfin-web#2086 [@thornbill] Fix missing index.html in prod build
 * jellyfin/jellyfin-web#2085 [@hawken93] Just return original server address in chromecastHelper
 * jellyfin/jellyfin-web#2083 [@BaronGreenback] Multi-repository plugin modification
 * jellyfin/jellyfin-web#2080 [@thornbill] Add prepare script to allow CI to skip build
 * jellyfin/jellyfin-web#2079 [@joshuaboniface] Revert "pull fonts from official repository"
 * jellyfin/jellyfin-web#2078 [@nyanmisaka] Tweak OSD duration display for narrow screen
 * jellyfin/jellyfin-web#2077 [@nyanmisaka] Add descriptions for Remux
 * jellyfin/jellyfin-web#2076 [@dependabot-preview[bot]] Bump babel-loader from 8.1.0 to 8.2.1
 * jellyfin/jellyfin-web#2075 [@dependabot-preview[bot]] Bump webpack-stream from 6.1.0 to 6.1.1
 * jellyfin/jellyfin-web#2072 [@dependabot-preview[bot]] Bump gulp-sourcemaps from 2.6.5 to 3.0.0
 * jellyfin/jellyfin-web#2071 [@joshuaboniface] Add Debian conffiles with config.json
 * jellyfin/jellyfin-web#2069 [@Artiume] Show Remux as a Playback Method
 * jellyfin/jellyfin-web#2064 [@nyanmisaka] Add initial profile for HEVC over FMP4-HLS
 * jellyfin/jellyfin-web#2061 [@cvium] Remove advanced toggle for library editor
 * jellyfin/jellyfin-web#2054 [@dependabot-preview[bot]] Bump webpack from 5.3.2 to 5.4.0
 * jellyfin/jellyfin-web#2053 [@dependabot-preview[bot]] Bump core-js from 3.6.5 to 3.7.0
 * jellyfin/jellyfin-web#2052 [@dependabot-preview[bot]] Bump eslint from 7.12.1 to 7.13.0
 * jellyfin/jellyfin-web#2051 [@dependabot-preview[bot]] Bump query-string from 6.13.6 to 6.13.7
 * jellyfin/jellyfin-web#2050 [@dependabot-preview[bot]] Bump whatwg-fetch from 3.4.1 to 3.5.0
 * jellyfin/jellyfin-web#2049 [@dependabot-preview[bot]] Bump css-loader from 5.0.0 to 5.0.1
 * jellyfin/jellyfin-web#2044 [@neilsb] Fix Schedules Direct Listings
 * jellyfin/jellyfin-web#2041 [@Artiume] Sort Show Genres by Random
 * jellyfin/jellyfin-web#2040 [@Artiume] Sort Movies Genres by Random
 * jellyfin/jellyfin-web#2039 [@ThibaultNocchi] Photos fullscreen button + hiding exit and arrows buttons on autoplay
 * jellyfin/jellyfin-web#2038 [@cvium] Create 1 lazyloader observer per collection type
 * jellyfin/jellyfin-web#2037 [@dependabot-preview[bot]] Bump node-sass from 4.14.1 to 5.0.0
 * jellyfin/jellyfin-web#2036 [@dependabot-preview[bot]] Bump gulp-terser from 1.4.0 to 1.4.1
 * jellyfin/jellyfin-web#2035 [@dependabot-preview[bot]] Bump eslint from 7.12.0 to 7.12.1
 * jellyfin/jellyfin-web#2034 [@dependabot-preview[bot]] Bump swiper from 6.3.4 to 6.3.5
 * jellyfin/jellyfin-web#2032 [@dependabot-preview[bot]] Bump webpack from 5.2.0 to 5.3.2
 * jellyfin/jellyfin-web#2031 [@dependabot-preview[bot]] Bump pdfjs-dist from 2.4.456 to 2.5.207
 * jellyfin/jellyfin-web#2030 [@dependabot-preview[bot]] Bump file-loader from 6.1.1 to 6.2.0
 * jellyfin/jellyfin-web#2029 [@cvium] Fix collectionEditor creation in movies
 * jellyfin/jellyfin-web#2028 [@danieladov] Hide progress bar when playing theme media
 * jellyfin/jellyfin-web#2027 [@dmitrylyzo] Remove custom hover style
 * jellyfin/jellyfin-web#2026 [@nyanmisaka] Adjust the default audio codec to AAC for HLS streaming
 * jellyfin/jellyfin-web#2025 [@dmitrylyzo] No external link for TV
 * jellyfin/jellyfin-web#2021 [@minobp] Add loading Japanese json files
 * jellyfin/jellyfin-web#2018 [@dkanada] Remove broken features from user settings
 * jellyfin/jellyfin-web#2017 [@dependabot-preview[bot]] Bump webpack from 5.0.0 to 5.2.0
 * jellyfin/jellyfin-web#2016 [@dependabot-preview[bot]] Bump headroom.js from 0.11.0 to 0.12.0
 * jellyfin/jellyfin-web#2015 [@dependabot-preview[bot]] Bump hls.js from 0.14.15 to 0.14.16
 * jellyfin/jellyfin-web#2014 [@dependabot-preview[bot]] Bump eslint from 7.11.0 to 7.12.0
 * jellyfin/jellyfin-web#2013 [@dependabot-preview[bot]] Bump confusing-browser-globals from 1.0.9 to 1.0.10
 * jellyfin/jellyfin-web#2012 [@dependabot-preview[bot]] Bump swiper from 6.3.3 to 6.3.4
 * jellyfin/jellyfin-web#2011 [@dependabot-preview[bot]] Bump howler from 2.2.0 to 2.2.1
 * jellyfin/jellyfin-web#2010 [@dkanada] pull fonts from official repository
 * jellyfin/jellyfin-web#2004 [@dependabot-preview[bot]] Bump css-loader from 4.3.0 to 5.0.0
 * jellyfin/jellyfin-web#2003 [@dependabot-preview[bot]] Bump @babel/eslint-parser from 7.11.5 to 7.12.1
 * jellyfin/jellyfin-web#2002 [@dependabot-preview[bot]] Bump browser-sync from 2.26.12 to 2.26.13
 * jellyfin/jellyfin-web#2001 [@dependabot-preview[bot]] Bump @babel/eslint-plugin from 7.11.5 to 7.12.1
 * jellyfin/jellyfin-web#2000 [@dependabot-preview[bot]] Bump @babel/preset-env from 7.11.5 to 7.12.1
 * jellyfin/jellyfin-web#1999 [@dependabot-preview[bot]] Bump @babel/plugin-proposal-private-methods from 7.10.4 to 7.12.1
 * jellyfin/jellyfin-web#1998 [@dependabot-preview[bot]] Bump @babel/core from 7.11.6 to 7.12.3
 * jellyfin/jellyfin-web#1997 [@dependabot-preview[bot]] Bump @babel/polyfill from 7.11.5 to 7.12.1
 * jellyfin/jellyfin-web#1996 [@dependabot-preview[bot]] Bump @babel/plugin-transform-modules-amd from 7.10.5 to 7.12.1
 * jellyfin/jellyfin-web#1995 [@dependabot-preview[bot]] Bump query-string from 6.13.5 to 6.13.6
 * jellyfin/jellyfin-web#1994 [@vitorsemeano] Migration to ES6
 * jellyfin/jellyfin-web#1993 [@sparky8251] Removed excess quality options to make menu more manageable
 * jellyfin/jellyfin-web#1987 [@dependabot-preview[bot]] Bump eslint from 7.10.0 to 7.11.0
 * jellyfin/jellyfin-web#1986 [@dependabot-preview[bot]] Bump file-loader from 6.1.0 to 6.1.1
 * jellyfin/jellyfin-web#1985 [@dependabot-preview[bot]] Bump style-loader from 1.3.0 to 2.0.0
 * jellyfin/jellyfin-web#1984 [@dependabot-preview[bot]] Bump swiper from 6.3.2 to 6.3.3
 * jellyfin/jellyfin-web#1982 [@dependabot-preview[bot]] Bump hls.js from 0.14.13 to 0.14.15
 * jellyfin/jellyfin-web#1981 [@dependabot-preview[bot]] Bump webpack from 4.44.2 to 5.0.0
 * jellyfin/jellyfin-web#1980 [@dkanada] Minor UX improvements
 * jellyfin/jellyfin-web#1979 [@BaronGreenback] Dashboard change to Network page to support new NetworkManager
 * jellyfin/jellyfin-web#1975 [@dkanada] Manual changes for no-var eslint rule
 * jellyfin/jellyfin-web#1974 [@dkanada] Run eslint to fix most var instances
 * jellyfin/jellyfin-web#1970 [@dependabot-preview[bot]] Bump style-loader from 1.2.1 to 1.3.0
 * jellyfin/jellyfin-web#1968 [@dependabot-preview[bot]] Bump query-string from 6.13.4 to 6.13.5
 * jellyfin/jellyfin-web#1966 [@joshuaboniface] Implement frontend component of max user sessions
 * jellyfin/jellyfin-web#1963 [@dependabot-preview[bot]] Bump stylelint from 13.7.1 to 13.7.2
 * jellyfin/jellyfin-web#1962 [@dependabot-preview[bot]] Bump eslint-plugin-import from 2.22.0 to 2.22.1
 * jellyfin/jellyfin-web#1961 [@dependabot-preview[bot]] Bump del from 5.1.0 to 6.0.0
 * jellyfin/jellyfin-web#1960 [@dependabot-preview[bot]] Bump hls.js from 0.14.12 to 0.14.13
 * jellyfin/jellyfin-web#1959 [@dependabot-preview[bot]] Bump jellyfin-apiclient from 1.4.1 to 1.4.2
 * jellyfin/jellyfin-web#1958 [@dependabot-preview[bot]] Bump query-string from 6.13.2 to 6.13.4
 * jellyfin/jellyfin-web#1957 [@dependabot-preview[bot]] Bump eslint from 7.9.0 to 7.10.0
 * jellyfin/jellyfin-web#1956 [@dependabot-preview[bot]] Bump swiper from 6.2.0 to 6.3.2
 * jellyfin/jellyfin-web#1955 [@dmitrylyzo] Fix ES6 import - browser
 * jellyfin/jellyfin-web#1954 [@dmitrylyzo] Fix subtitles display on Tizen 2.x
 * jellyfin/jellyfin-web#1953 [@dmitrylyzo] Fix 'file:' fetching (bundled apps)
 * jellyfin/jellyfin-web#1951 [@dmitrylyzo] Fix theme video (animated backdrops)
 * jellyfin/jellyfin-web#1949 [@dmitrylyzo] Retranslate UI instead of recreating it
 * jellyfin/jellyfin-web#1948 [@fffrankieh] Fix Enter key in Edit Metadata dialog
 * jellyfin/jellyfin-web#1946 [@cvium] Fix PIN request and reset route
 * jellyfin/jellyfin-web#1945 [@OancaAndrei] SyncPlay for TV series (and Music)
 * jellyfin/jellyfin-web#1942 [@nvllsvm] Optimize images
 * jellyfin/jellyfin-web#1941 [@dependabot-preview[bot]] Bump webpack from 4.44.1 to 4.44.2
 * jellyfin/jellyfin-web#1940 [@dependabot-preview[bot]] Bump html-webpack-plugin from 4.4.1 to 4.5.0
 * jellyfin/jellyfin-web#1938 [@dependabot-preview[bot]] Bump sortablejs from 1.10.2 to 1.12.0
 * jellyfin/jellyfin-web#1934 [@cvium] Remove missing ep checkbox in library options
 * jellyfin/jellyfin-web#1933 [@nyanmisaka] Update strings for tonemapping on AMD AMF
 * jellyfin/jellyfin-web#1929 [@dependabot-preview[bot]] Bump css-loader from 4.2.2 to 4.3.0
 * jellyfin/jellyfin-web#1928 [@dependabot-preview[bot]] Bump hls.js from 0.14.11 to 0.14.12
 * jellyfin/jellyfin-web#1927 [@dependabot-preview[bot]] Bump stylelint from 13.7.0 to 13.7.1
 * jellyfin/jellyfin-web#1926 [@dependabot-preview[bot]] Bump query-string from 6.13.1 to 6.13.2
 * jellyfin/jellyfin-web#1924 [@dependabot-preview[bot]] Bump eslint from 7.8.1 to 7.9.0
 * jellyfin/jellyfin-web#1923 [@dependabot-preview[bot]] [Security] Bump bl from 1.2.2 to 1.2.3
 * jellyfin/jellyfin-web#1920 [@dkanada] Prefer const rule for ESLint
 * jellyfin/jellyfin-web#1918 [@dkanada] Fix startup wizard redirect and standalone mode
 * jellyfin/jellyfin-web#1917 [@cvium] Add known proxies config option
 * jellyfin/jellyfin-web#1916 [@mcarlton00] Make alpha picker return only selected letters
 * jellyfin/jellyfin-web#1914 [@dependabot-preview[bot]] Bump swiper from 6.1.1 to 6.2.0
 * jellyfin/jellyfin-web#1913 [@dependabot-preview[bot]] Bump whatwg-fetch from 3.4.0 to 3.4.1
 * jellyfin/jellyfin-web#1912 [@dependabot-preview[bot]] Bump @babel/core from 7.11.5 to 7.11.6
 * jellyfin/jellyfin-web#1911 [@dependabot-preview[bot]] Bump material-design-icons-iconfont from 6.0.1 to 6.1.0
 * jellyfin/jellyfin-web#1909 [@iwalton3] Add Auto Cast Feature 
 * jellyfin/jellyfin-web#1905 [@brianjmurrell] Add BR: git for all distros
 * jellyfin/jellyfin-web#1904 [@cvium] Fix task filter for the scan task button
 * jellyfin/jellyfin-web#1903 [@dmitrylyzo] Return permanent scrollbar
 * jellyfin/jellyfin-web#1902 [@dependabot-preview[bot]] Bump eslint from 7.8.0 to 7.8.1
 * jellyfin/jellyfin-web#1900 [@dependabot-preview[bot]] Bump webpack-stream from 6.0.0 to 6.1.0
 * jellyfin/jellyfin-web#1899 [@dkanada] Allow plugin config changes on standalone
 * jellyfin/jellyfin-web#1898 [@Camc314] Update dependabot frequency to weekly
 * jellyfin/jellyfin-web#1897 [@Camc314] Fix Message Appearing on Page Reload
 * jellyfin/jellyfin-web#1896 [@dkanada] Fix a common error message and update some strings
 * jellyfin/jellyfin-web#1894 [@dmitrylyzo] Fix webOS 1.2
 * jellyfin/jellyfin-web#1893 [@thornbill] Fix old iOS devices that do not support AC-3
 * jellyfin/jellyfin-web#1892 [@dependabot-preview[bot]] Bump eslint from 7.7.0 to 7.8.0
 * jellyfin/jellyfin-web#1891 [@dependabot-preview[bot]] Bump hls.js from 0.14.10 to 0.14.11
 * jellyfin/jellyfin-web#1889 [@dependabot-preview[bot]] Bump @babel/preset-env from 7.11.0 to 7.11.5
 * jellyfin/jellyfin-web#1888 [@dependabot-preview[bot]] Bump @babel/core from 7.11.4 to 7.11.5
 * jellyfin/jellyfin-web#1887 [@dkanada] Add basic pdf reader
 * jellyfin/jellyfin-web#1886 [@dependabot-preview[bot]] Bump @babel/polyfill from 7.10.4 to 7.11.5
 * jellyfin/jellyfin-web#1885 [@dependabot-preview[bot]] Bump @babel/eslint-parser from 7.11.4 to 7.11.5
 * jellyfin/jellyfin-web#1884 [@dependabot-preview[bot]] Bump @babel/eslint-plugin from 7.11.3 to 7.11.5
 * jellyfin/jellyfin-web#1883 [@Camc314] Hide alphaPicker when not sorting alphabetically
 * jellyfin/jellyfin-web#1882 [@Camc314] Fix accessing subtitles and playback data actionsheets
 * jellyfin/jellyfin-web#1880 [@thornbill] Fix iPad detection
 * jellyfin/jellyfin-web#1877 [@dependabot-preview[bot]] Bump date-fns from 2.16.0 to 2.16.1
 * jellyfin/jellyfin-web#1875 [@dependabot-preview[bot]] Bump stylelint from 13.6.1 to 13.7.0
 * jellyfin/jellyfin-web#1874 [@dependabot-preview[bot]] Bump file-loader from 6.0.0 to 6.1.0
 * jellyfin/jellyfin-web#1873 [@thornbill] Fix iOS PiP support detection
 * jellyfin/jellyfin-web#1871 [@ThibaultNocchi] Fixed header tooltips not being translated to the user language
 * jellyfin/jellyfin-web#1870 [@Camc314] Unclutter listview for small screens
 * jellyfin/jellyfin-web#1868 [@cvium] Add application/json as content type for JSON requests
 * jellyfin/jellyfin-web#1867 [@Camc314] Fix hovering CSS changes on mobile
 * jellyfin/jellyfin-web#1863 [@dependabot-preview[bot]] Bump html-webpack-plugin from 4.4.0 to 4.4.1
 * jellyfin/jellyfin-web#1862 [@dependabot-preview[bot]] Bump material-design-icons-iconfont from 5.0.1 to 6.0.1
 * jellyfin/jellyfin-web#1861 [@dependabot-preview[bot]] Bump html-webpack-plugin from 4.3.0 to 4.4.0
 * jellyfin/jellyfin-web#1859 [@MrTimscampi] Use connectionManager global
 * jellyfin/jellyfin-web#1856 [@MrTimscampi] Remove withCredentials from xhrSetup in hls.js
 * jellyfin/jellyfin-web#1855 [@MrTimscampi] Fix bad global restriction
 * jellyfin/jellyfin-web#1853 [@dependabot-preview[bot]] Bump webpack-stream from 5.2.1 to 6.0.0
 * jellyfin/jellyfin-web#1851 [@dependabot-preview[bot]] Bump date-fns from 2.15.0 to 2.16.0
 * jellyfin/jellyfin-web#1849 [@brianjmurrell] Add BuildRequires: git to Fedora specfile
 * jellyfin/jellyfin-web#1847 [@dependabot-preview[bot]] Bump hls.js from 0.14.9 to 0.14.10
 * jellyfin/jellyfin-web#1845 [@MrTimscampi] Various TV-related fixes
 * jellyfin/jellyfin-web#1844 [@Camc314] Fix broken item details actionMenu for TV Shows
 * jellyfin/jellyfin-web#1843 [@dkanada] Prevent the use of confusing globals
 * jellyfin/jellyfin-web#1842 [@nyanmisaka] Expose max_muxing_queue_size to user
 * jellyfin/jellyfin-web#1841 [@dependabot-preview[bot]] Bump css-loader from 4.2.1 to 4.2.2
 * jellyfin/jellyfin-web#1839 [@dkanada] Remove translations with duplicate values
 * jellyfin/jellyfin-web#1837 [@dependabot-preview[bot]] Bump gulp-terser from 1.3.2 to 1.4.0
 * jellyfin/jellyfin-web#1832 [@MrTimscampi] Fix cards without title
 * jellyfin/jellyfin-web#1831 [@dependabot-preview[bot]] Bump @babel/core from 7.11.1 to 7.11.4
 * jellyfin/jellyfin-web#1830 [@dependabot-preview[bot]] Bump @babel/eslint-parser from 7.11.3 to 7.11.4
 * jellyfin/jellyfin-web#1829 [@thornbill] Make fallback text on cards less tiny
 * jellyfin/jellyfin-web#1827 [@thornbill] Fix TV channel logo size
 * jellyfin/jellyfin-web#1825 [@MrTimscampi] Redesign OSD and Up Next dialog
 * jellyfin/jellyfin-web#1823 [@thornbill] Set background color on blurhash image load
 * jellyfin/jellyfin-web#1822 [@dependabot-preview[bot]] Bump hls.js from 0.14.8 to 0.14.9
 * jellyfin/jellyfin-web#1820 [@thornbill] Remove horizontal margins on guide
 * jellyfin/jellyfin-web#1819 [@MrTimscampi] Fix tabs always focusing the active tab in TV layout
 * jellyfin/jellyfin-web#1817 [@welpher] Update zh-cn.json
 * jellyfin/jellyfin-web#1814 [@danieladov] Fix download/edit metadata of specific version
 * jellyfin/jellyfin-web#1813 [@dkanada] Update some translation strings
 * jellyfin/jellyfin-web#1812 [@iwalton3] Show seek buttons when playing video on mobile.
 * jellyfin/jellyfin-web#1811 [@iwalton3] Fix syncplay menu.
 * jellyfin/jellyfin-web#1810 [@iwalton3] Change all instances of currentTime to be in ms.
 * jellyfin/jellyfin-web#1809 [@dependabot-preview[bot]] Bump eslint from 7.6.0 to 7.7.0
 * jellyfin/jellyfin-web#1808 [@jomp16] Support for faster playback rates.
 * jellyfin/jellyfin-web#1806 [@matjaz321] Bug fix for: Cannot exit unavailable/private trailers
 * jellyfin/jellyfin-web#1804 [@dkanada] Remove some duplicate strings
 * jellyfin/jellyfin-web#1802 [@dmitrylyzo] Reorder CSS loading
 * jellyfin/jellyfin-web#1801 [@MrTimscampi] Use JSON when POSTing data
 * jellyfin/jellyfin-web#1799 [@matjaz321] Hitting space to check/uncheck checkboxes doesn't work on firefox
 * jellyfin/jellyfin-web#1798 [@orryverducci] Add new deinterlacing options
 * jellyfin/jellyfin-web#1796 [@dkanada] Fix some odd strings and remove duplicate values
 * jellyfin/jellyfin-web#1795 [@MrTimscampi] Fix themes not loading unless signed in
 * jellyfin/jellyfin-web#1794 [@bugfixin] Remove extraneous pageContainer element from videoOSD
 * jellyfin/jellyfin-web#1792 [@dependabot-preview[bot]] Bump @babel/eslint-parser from 7.11.0 to 7.11.3
 * jellyfin/jellyfin-web#1791 [@dependabot-preview[bot]] Bump @babel/eslint-plugin from 7.11.0 to 7.11.3
 * jellyfin/jellyfin-web#1789 [@MrTimscampi] Move Dashboard to a new module
 * jellyfin/jellyfin-web#1787 [@MrTimscampi] Move HTML files to the proper locations
 * jellyfin/jellyfin-web#1785 [@dependabot-preview[bot]] Bump hls.js from 0.14.7 to 0.14.8
 * jellyfin/jellyfin-web#1784 [@dependabot-preview[bot]] Bump whatwg-fetch from 3.3.1 to 3.4.0
 * jellyfin/jellyfin-web#1783 [@thornbill] Hide download button for books when not supported
 * jellyfin/jellyfin-web#1781 [@Camc314] Migration of chromecastPlayer to ES6 Modules and remove a few final requires
 * jellyfin/jellyfin-web#1780 [@Camc314] Migration of tunerPicker and userdatabuttons to ES6 modules
 * jellyfin/jellyfin-web#1779 [@Camc314] Migration of experimentalWarnings and sessionPlayer to ES6 modules
 * jellyfin/jellyfin-web#1778 [@Camc314] Migration of logoScreenSaver and playAccessValidation to ES6 module
 * jellyfin/jellyfin-web#1776 [@MrTimscampi] Remove focus-prevent-scroll, migrate gamepadtokey and chromecastHelper to ES6
 * jellyfin/jellyfin-web#1775 [@dependabot-preview[bot]] Bump css-loader from 4.2.0 to 4.2.1
 * jellyfin/jellyfin-web#1774 [@MrTimscampi] Migrate navdrawer and scroller to ES6
 * jellyfin/jellyfin-web#1771 [@Camc314] Migration of themeMediaPLayer, viewSettings and notification to ES6 modules
 * jellyfin/jellyfin-web#1769 [@Camc314] Migration of subtitleeditor and subtitlesync to ES6 modules
 * jellyfin/jellyfin-web#1768 [@Camc314] Migration of sortmenu and slideshow to ES6 modules
 * jellyfin/jellyfin-web#1765 [@Camc314] Add default to fix master (chromecastPlayer)
 * jellyfin/jellyfin-web#1763 [@thornbill] Add start script as alias for serve
 * jellyfin/jellyfin-web#1762 [@Camc314] Migration of recordinghelper and seriesrecordingeditor to ES6 modules
 * jellyfin/jellyfin-web#1761 [@Camc314] Migration of recordingeditor and recordingfields to ES6 modules
 * jellyfin/jellyfin-web#1760 [@dependabot-preview[bot]] Bump gulp-terser from 1.3.0 to 1.3.2
 * jellyfin/jellyfin-web#1759 [@Camc314] Migration of guide and guide-settings to ES6 modules
 * jellyfin/jellyfin-web#1758 [@dependabot-preview[bot]] Bump @babel/core from 7.11.0 to 7.11.1
 * jellyfin/jellyfin-web#1757 [@matjaz321] Migrated itembydetailpage to es6 moduel
 * jellyfin/jellyfin-web#1756 [@matjaz321] Migrated castSenderApi.js to es6 module
 * jellyfin/jellyfin-web#1753 [@dependabot-preview[bot]] Bump whatwg-fetch from 3.2.0 to 3.3.1
 * jellyfin/jellyfin-web#1751 [@Camc314] Migration of layoutManager and itemsrefresher to ES6 modules
 * jellyfin/jellyfin-web#1750 [@Camc314] Migration of recordingbutton and recordingcreator to ES6 modules
 * jellyfin/jellyfin-web#1749 [@Camc314] Migration of livetvguide and livetvcomponents to ES6 modules
 * jellyfin/jellyfin-web#1748 [@dmitrylyzo] Fix old Edge loading
 * jellyfin/jellyfin-web#1747 [@Camc314] Migration of htmlAudioPlayer to ES6 module
 * jellyfin/jellyfin-web#1745 [@matjaz321] Migrated livetvchannels to es6 module
 * jellyfin/jellyfin-web#1744 [@matjaz321] Migrated livetvrecordings.js to es6 module
 * jellyfin/jellyfin-web#1743 [@matjaz321] Migrated livetvschedule.js to ES6 module
 * jellyfin/jellyfin-web#1742 [@dkanada] Remove unused strings from source
 * jellyfin/jellyfin-web#1740 [@Camc314] Fix broken playback
 * jellyfin/jellyfin-web#1738 [@Xantios] Move focusManager to ES6
 * jellyfin/jellyfin-web#1737 [@Supergamer1337] Added overlay and play functionality.
 * jellyfin/jellyfin-web#1736 [@Camc314] Migration of xmltv and schedulesdirect to ES6 modules
 * jellyfin/jellyfin-web#1734 [@dmitrylyzo] Fix injecting of view with embedded script
 * jellyfin/jellyfin-web#1733 [@Camc314] Migration of viewManager to ES6 module
 * jellyfin/jellyfin-web#1732 [@dependabot-preview[bot]] Bump gulp-terser from 1.2.1 to 1.3.0
 * jellyfin/jellyfin-web#1731 [@dmitrylyzo] Fix usage of ES6 import hacks
 * jellyfin/jellyfin-web#1730 [@Camc314] Remove Aliasing this in Music
 * jellyfin/jellyfin-web#1728 [@mattstrayer] Migrated FilterMenu to es6 module
 * jellyfin/jellyfin-web#1726 [@matjaz321] Migrated livetvseriestimer to es6 module
 * jellyfin/jellyfin-web#1725 [@matjaz321] Migrated livetvsuggested.js to es6 module
 * jellyfin/jellyfin-web#1724 [@matjaz321] Migrated `livetvguideprovider.js` to es6 module
 * jellyfin/jellyfin-web#1723 [@MrTimscampi] Update Swiper to 6.1.1
 * jellyfin/jellyfin-web#1722 [@MrTimscampi] Update ESLint to 7.6.0
 * jellyfin/jellyfin-web#1719 [@Camc314] Migration of remotecontrol to ES6 module
 * jellyfin/jellyfin-web#1718 [@MrTimscampi] Migrate routes.js and mouseManager to ES6
 * jellyfin/jellyfin-web#1716 [@MrTimscampi] Migrate PluginManager and PackageManager to ES6
 * jellyfin/jellyfin-web#1715 [@dependabot-preview[bot]] Bump css-loader from 4.1.1 to 4.2.0
 * jellyfin/jellyfin-web#1713 [@matjaz321] Migrated `/controllers/livetvsettings.js` to es6 module
 * jellyfin/jellyfin-web#1712 [@dkanada] Standardize key prefixes for translations
 * jellyfin/jellyfin-web#1711 [@dkanada] Remove strings that only exist in translations
 * jellyfin/jellyfin-web#1710 [@MrTimscampi] Remove image size hack
 * jellyfin/jellyfin-web#1709 [@dkanada] Rename chromecast flavors
 * jellyfin/jellyfin-web#1708 [@cyrusboadway] Consider Meta Key (⌘/⊞) as a modifier
 * jellyfin/jellyfin-web#1707 [@Camc314] Migration of playbackmanager to ES6 module
 * jellyfin/jellyfin-web#1706 [@MrTimscampi] Migrate to new babel-eslint package
 * jellyfin/jellyfin-web#1705 [@dependabot-preview[bot]] Bump @babel/preset-env from 7.10.4 to 7.11.0
 * jellyfin/jellyfin-web#1704 [@dependabot-preview[bot]] Bump @babel/core from 7.10.5 to 7.11.0
 * jellyfin/jellyfin-web#1703 [@dependabot-preview[bot]] Bump autoprefixer from 9.8.5 to 9.8.6
 * jellyfin/jellyfin-web#1702 [@dependabot-preview[bot]] Bump hls.js from 0.14.6 to 0.14.7
 * jellyfin/jellyfin-web#1701 [@MrTimscampi] Use emblem when loading on mobile
 * jellyfin/jellyfin-web#1700 [@matjaz321] Migrated livetvstatus.js to es6 module
 * jellyfin/jellyfin-web#1699 [@MrTimscampi] Remove redundant variable assignments
 * jellyfin/jellyfin-web#1697 [@cyrusboadway] Skip number key navigation when key is modified with alt/ctrl
 * jellyfin/jellyfin-web#1695 [@dependabot-preview[bot]] Bump css-loader from 4.0.0 to 4.1.1
 * jellyfin/jellyfin-web#1694 [@dependabot-preview[bot]] Bump webpack from 4.44.0 to 4.44.1
 * jellyfin/jellyfin-web#1693 [@Camc314] Migration of playqueuemanager to ES6 module
 * jellyfin/jellyfin-web#1692 [@Camc314] Migration of refresh dialog to ES6 module
 * jellyfin/jellyfin-web#1691 [@dependabot-preview[bot]] [Security] Bump elliptic from 6.5.2 to 6.5.3
 * jellyfin/jellyfin-web#1689 [@matjaz321] Migration of `livetvtuner.js` to es6
 * jellyfin/jellyfin-web#1688 [@Supergamer1337] Made cursor hide on OSD hide.
 * jellyfin/jellyfin-web#1686 [@Larvitar] Fix issue with nowplaying page when item.Album or item.Artists are null.
 * jellyfin/jellyfin-web#1684 [@thornbill] Fix fullscreen video in iOS Safari
 * jellyfin/jellyfin-web#1681 [@dkanada] Add paging in book player with touch events
 * jellyfin/jellyfin-web#1680 [@KucharczykL] Add tooltips for Skip to previous/next buttons
 * jellyfin/jellyfin-web#1679 [@Camc314] Migration of loading and favoriteitems to ES6 modules
 * jellyfin/jellyfin-web#1678 [@dkanada] Fix banner height and use primary image as fallback
 * jellyfin/jellyfin-web#1677 [@Maxr1998] Improve NativeShell integration
 * jellyfin/jellyfin-web#1676 [@Camc314] Migration of home, tabbedview and libraryMenu to ES6 modules
 * jellyfin/jellyfin-web#1675 [@Camc314] Migration of list and screensavermanager to ES6 modules
 * jellyfin/jellyfin-web#1674 [@michael9dk] Update README.md (add Node.js in dependencies)
 * jellyfin/jellyfin-web#1672 [@MrTimscampi] Adjust target browsers
 * jellyfin/jellyfin-web#1669 [@joshuaboniface] Flip quoting in variable set command
 * jellyfin/jellyfin-web#1668 [@joshuaboniface] Bump master version to 10.7.0 for next release
 * jellyfin/jellyfin-web#1667 [@joshuaboniface] Get and tag with actual release version in CI
 * jellyfin/jellyfin-web#1666 [@dependabot-preview[bot]] Bump hls.js from 0.14.5 to 0.14.6
 * jellyfin/jellyfin-web#1665 [@joshuaboniface] Fix bump_version so it works properly
 * jellyfin/jellyfin-web#1664 [@dmitrylyzo] Fix typo in package.json
 * jellyfin/jellyfin-web#1663 [@Camc314] Migration of libraryBrowser and multiDownload to ES6 modules
 * jellyfin/jellyfin-web#1662 [@dmitrylyzo] Add h264 codec profile for TS container
 * jellyfin/jellyfin-web#1661 [@Camc314] Fix removing scheduled tasks
 * jellyfin/jellyfin-web#1660 [@nyanmisaka] Fix mkv directplay on Edge chromium
 * jellyfin/jellyfin-web#1657 [@dmitrylyzo] Fix file download
 * jellyfin/jellyfin-web#1656 [@dmitrylyzo] Fix CircleOfDeath on plugin install
 * jellyfin/jellyfin-web#1655 [@Camc314] Migration of imageEditor and imageDownloader to ES6 modules
 * jellyfin/jellyfin-web#1654 [@Camc314] Migration of toast and upnextdialog to ES6 modules
 * jellyfin/jellyfin-web#1653 [@MrTimscampi]  Migrate shell, serverNotifications and scrollHelper to ES6 + remove searchtab 
 * jellyfin/jellyfin-web#1652 [@MrTimscampi] Migrate add, installed, available plugin pages to ES6
 * jellyfin/jellyfin-web#1651 [@dependabot-preview[bot]] Bump browser-sync from 2.26.10 to 2.26.12
 * jellyfin/jellyfin-web#1650 [@Camc314] Migration of favorites, homeTab and editItemMetadata to ES6 modules
 * jellyfin/jellyfin-web#1649 [@Camc314] Migration of notification and notifications to ES6 modules
 * jellyfin/jellyfin-web#1647 [@dkanada] Move wizard and user preference routes to nested folders
 * jellyfin/jellyfin-web#1645 [@MrTimscampi] Migrate appRouter to ES6
 * jellyfin/jellyfin-web#1644 [@dmitrylyzo] Fix layout of login and selectserver pages
 * jellyfin/jellyfin-web#1643 [@dependabot-preview[bot]] Bump css-loader from 3.6.0 to 4.0.0
 * jellyfin/jellyfin-web#1641 [@dmitrylyzo] Fix event source for inputManager in case of multiple open dialogs
 * jellyfin/jellyfin-web#1638 [@dependabot-preview[bot]] Bump webpack from 4.43.0 to 4.44.0
 * jellyfin/jellyfin-web#1637 [@dkanada] Remove legacy jquery extensions
 * jellyfin/jellyfin-web#1636 [@nyanmisaka] Add options to use multiple custom fonts for subtitle rendering
 * jellyfin/jellyfin-web#1635 [@dependabot-preview[bot]] Bump hls.js from 0.14.3 to 0.14.5
 * jellyfin/jellyfin-web#1634 [@MrTimscampi] Merge the ES6 feature branch back into master
 * jellyfin/jellyfin-web#1633 [@dependabot-preview[bot]] Bump gulp-terser from 1.2.0 to 1.2.1
 * jellyfin/jellyfin-web#1632 [@dmitrylyzo] Remove debug leftovers
 * jellyfin/jellyfin-web#1630 [@grafixeyehero] remove unused morebutton and editimage
 * jellyfin/jellyfin-web#1628 [@dmitrylyzo] Use NodeList instead of HTMLCollection
 * jellyfin/jellyfin-web#1627 [@rom4nik] Fix required track count for subtitle selector to appear
 * jellyfin/jellyfin-web#1625 [@MrTimscampi] Add version check for SyncPlay
 * jellyfin/jellyfin-web#1624 [@MrTimscampi] Update apiclient to 1.4.1
 * jellyfin/jellyfin-web#1620 [@MrTimscampi] Restore More button in metadata editor
 * jellyfin/jellyfin-web#1612 [@Maxr1998] Add support for seeking with milliseconds
 * jellyfin/jellyfin-web#1609 [@dependabot-preview[bot]] Bump date-fns from 2.14.0 to 2.15.0
 * jellyfin/jellyfin-web#1608 [@dependabot-preview[bot]] Bump browser-sync from 2.26.7 to 2.26.10
 * jellyfin/jellyfin-web#1606 [@dependabot-preview[bot]] Bump @babel/core from 7.10.4 to 7.10.5
 * jellyfin/jellyfin-web#1604 [@dependabot-preview[bot]] Bump @babel/plugin-transform-modules-amd from 7.10.4 to 7.10.5
 * jellyfin/jellyfin-web#1603 [@dependabot-preview[bot]] Bump hls.js from 0.14.0 to 0.14.3
 * jellyfin/jellyfin-web#1600 [@Camc314] Migration of itemDetails/index, browser and itemHelper to ES6 module
 * jellyfin/jellyfin-web#1599 [@MrTimscampi] Remove dead code
 * jellyfin/jellyfin-web#1598 [@MrTimscampi] Overhaul issue templates
 * jellyfin/jellyfin-web#1595 [@dkanada] Fix issue with sync menu and excessive logging
 * jellyfin/jellyfin-web#1594 [@MrTimscampi] Redesign login and selectserver pages
 * jellyfin/jellyfin-web#1593 [@MrTimscampi] Replace trigger and handle with handleCommand
 * jellyfin/jellyfin-web#1584 [@Camc314] Migration of nowplaying and videoosd to ES6 modules
 * jellyfin/jellyfin-web#1577 [@MrTimscampi] Migrate appHost, qualityOptions, bundle and appLoader to es6
 * jellyfin/jellyfin-web#1554 [@Camc314] Migration of music to ES6 modules
 * jellyfin/jellyfin-web#1553 [@Camc314] Migration of Movies to ES6 Modules
 * jellyfin/jellyfin-web#1552 [@masterkoppa] Add basic support for bulk deleting all devices
 * jellyfin/jellyfin-web#1542 [@dmitrylyzo] Fix OSD lock
 * jellyfin/jellyfin-web#1502 [@dkanada] Pull themes and plugins from web config
 * jellyfin/jellyfin-web#1499 [@grafixeyehero] Move tvlatest tab to suggestions section
 * jellyfin/jellyfin-web#1487 [@nyanmisaka] Tonemapping function dashboard options
 * jellyfin/jellyfin-web#1484 [@ferferga] Remove legacy loading
 * jellyfin/jellyfin-web#1408 [@dmitrylyzo] Fix subtitle line spacing and add position
 * jellyfin/jellyfin-web#1374 [@itegulov] Adapt book plugin for mobile devices
 * jellyfin/jellyfin-web#1333 [@MrTimscampi] Kill Yoda
 * jellyfin/jellyfin-web#1325 [@MrTimscampi] Add barebones comic book reader
 * jellyfin/jellyfin-web#1316 [@ferferga] Remove download images in advance from library options
 * jellyfin/jellyfin-web#1308 [@bendardenne] Revisit showing track artists in album view
 * jellyfin/jellyfin-web#1237 [@DesertCookie] Sort multi-version movie dropdown menu
 * jellyfin/jellyfin-web#1236 [@GuilhermeHideki] Convert files to SCSS
 * jellyfin/jellyfin-web#1212 [@redSpoutnik] Feature: manually add subtitle
 * jellyfin/jellyfin-web#1191 [@MrTimscampi] Remove block padding and disallow it
 * jellyfin/jellyfin-web#1175 [@GuilhermeHideki] Add folder for common SCSS code
 * jellyfin/jellyfin-web#1096 [@ConfusedPolarBear] Add quick connect (login without typing password)
 * jellyfin/jellyfin-web#1091 [@cromefire] Migrated HtmlVideoPlayer

## 10.6.4 – 2020-08-30

# Jellyfin 10.6.4

Stable hotfix release for 10.6.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [all] Small bugfixes
* [fedora/centos] Fix broken metapackages and dependencies

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/28

### [jellyfin](https://github.com/jellyfin/jellyfin) [2]

 * #4001 [@brianjmurrell] Add an empty %files section to main package
 * #3953 [@crobibero] bump DotNet.Glob

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [4]

 * jellyfin/jellyfin-web#1849 [@brianjmurrell] Add BuildRequires: git to Fedora specfile
 * jellyfin/jellyfin-web#1823 [@thornbill] Set background color on blurhash image load
 * jellyfin/jellyfin-web#1820 [@thornbill] Remove horizontal margins on guide
 * jellyfin/jellyfin-web#1818 [@dmitrylyzo] Fix non-ES6 import [10.6.z]

## 10.6.3 – 2020-08-17

# Jellyfin 10.6.3

Stable hotfix release for 10.6.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [packages] Bump the version of the .NET SDK in use to fix numerous bugs.
* [all] QOL improvements in WebUI.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/28

### [jellyfin](https://github.com/jellyfin/jellyfin) [1]

 * #3831 [@joshuaboniface] Bump to .NET Core SDK 3.1.302

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [4]

 * jellyfin/jellyfin-web#1799 [@matjaz321] Hitting space to check/uncheck checkboxes doesn't work on firefox
 * jellyfin/jellyfin-web#1794 [@bugfixin] Remove extraneous pageContainer element from videoOSD
 * jellyfin/jellyfin-web#1748 [@dmitrylyzo] Fix old Edge loading
 * jellyfin/jellyfin-web#1542 [@dmitrylyzo] Fix OSD lock

## 10.6.2 – 2020-08-03

# Jellyfin 10.6.2

Stable hotfix release for 10.6.z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [all] Various server and UI bugfixes.
* [all] Memory usage issues should be fixed.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/28

### [jellyfin](https://github.com/jellyfin/jellyfin) [11]

 * #3795 [@anthonylavado] Update to newer Jellyfin.XMLTV
 * #3792 [@cvium] TMDb: Change Budget and Revenue to long to avoid overflow
 * #3790 [@cvium] Remove some unnecessary string allocations
 * #3761 [@cvium] Fix DI memory leak
 * #3760 [@thornbill] Fix inverted logic for LAN IP detection
 * #3757 [@cvium] Update BlurHashSharp and set max size to 128x128
 * #3728 [@nyanmisaka] adjust priority in outputSizeParam cutter
 * #3727 [@K900] Fix #3624
 * #3725 [@joshuaboniface] Flip quoting in variable set command
 * #3723 [@joshuaboniface] Get and tag with the actual release version in CI
 * #3720 [@joshuaboniface] Fix bump_version so it works properly

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [11]

 * jellyfin/jellyfin-web#1734 [@dmitrylyzo] Fix injecting of view with embedded script
 * jellyfin/jellyfin-web#1701 [@MrTimscampi] Use emblem when loading on mobile
 * jellyfin/jellyfin-web#1686 [@Larvitar] Fix issue with nowplaying page when item.Album or item.Artists are null.
 * jellyfin/jellyfin-web#1684 [@thornbill] Fix fullscreen video in iOS Safari
 * jellyfin/jellyfin-web#1681 [@dkanada] Add paging in book player with touch events
 * jellyfin/jellyfin-web#1678 [@dkanada] Fix banner height and use primary image as fallback
 * jellyfin/jellyfin-web#1672 [@MrTimscampi] Adjust target browsers
 * jellyfin/jellyfin-web#1669 [@joshuaboniface] Flip quoting in variable set command
 * jellyfin/jellyfin-web#1667 [@joshuaboniface] Get and tag with actual release version in CI
 * jellyfin/jellyfin-web#1665 [@joshuaboniface] Fix bump_version so it works properly
 * jellyfin/jellyfin-web#1656 [@dmitrylyzo] Fix CircleOfDeath on plugin install

## 10.6.1 – 2020-07-27

# Jellyfin 10.6.1

Stable hotfix release for 10.6.1 release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [all] Various server and UI bugfixes.
* [all] Memory usage may be improved somewhat from 10.6.0, however we believe the leak is still present and is still being investigated. If you run out of RAM, restarting your server every few days (or library scans) might be a quick fix.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/28

### [jellyfin](https://github.com/jellyfin/jellyfin) [18]

 * #3711 [@yrjyrj123] Fix the problem that hardware decoding cannot be used on macOS.
 * #3704 [@oddstr13] Don't ignore dot directories or movies/episodes with sample in their name.
 * #3703 [@oddstr13] Allow space in username
 * #3699 [@oddstr13] Fix embedded subtitles
 * #3675 [@ferferga] fix typo in debian's config file
 * #3663 [@crobibero] Add missing usings to UserManager
 * #3660 [@crobibero] Force plugin config location
 * #3649 [@thornbill] Skip image processing for live tv sources
 * #3642 [@crobibero] Try adding plugin repository again
 * #3634 [@crobibero] fix built in plugin js
 * #3620 [@BaronGreenback] Fix for #3607 and #3515
 * #3616 [@crobibero] Allow migration to optionally run on fresh install
 * #3615 [@nyanmisaka] Fix QSV device creation on Comet Lake
 * #3604 [@joshuaboniface] Fix bad Debuntu dependencies
 * #3602 [@crobibero] Fix username case change
 * #3576 [@HelloWorld017] Fix SAMI UTF-16 Encoding Bug
 * #3552 [@BaronGreenback] Fixes #3551 (Notifications Serialization error)
 * #3521 [@sachk] Fix support for mixed-protocol subtitles

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [11]

 * jellyfin/jellyfin-web#1662 [@dmitrylyzo] Add h264 codec profile for TS container
 * jellyfin/jellyfin-web#1660 [@nyanmisaka] Fix mkv directplay on Edge chromium
 * jellyfin/jellyfin-web#1641 [@dmitrylyzo] Fix event source for inputManager in case of multiple open dialogs
 * jellyfin/jellyfin-web#1632 [@dmitrylyzo] Remove debug leftovers
 * jellyfin/jellyfin-web#1628 [@dmitrylyzo] Use NodeList instead of HTMLCollection
 * jellyfin/jellyfin-web#1627 [@rom4nik] Fix required track count for subtitle selector to appear
 * jellyfin/jellyfin-web#1625 [@MrTimscampi] Add version check for SyncPlay
 * jellyfin/jellyfin-web#1624 [@MrTimscampi] Update apiclient to 1.4.1
 * jellyfin/jellyfin-web#1620 [@MrTimscampi] Restore More button in metadata editor
 * jellyfin/jellyfin-web#1612 [@Maxr1998] Add support for seeking with milliseconds
 * jellyfin/jellyfin-web#1595 [@dkanada] Fix issue with sync menu and excessive logging

## 10.6.0 – 2020-07-19

# Jellyfin 10.6.0

Stable release for 10.6.0

Blog post explaining changes: https://jellyfin.org/posts/jellyfin-10-6-0/

GitHub project for release: https://github.com/orgs/jellyfin/projects/17

Binary assets: https://repo.jellyfin.org/releases/server

## Release Notes

* [ALL] Memory usage may be higher in 10.6.0 compared to previous versions. We have had several, but not many, reports of high memory usage in unstable 10.6.0 builds, most often caused by frequent library scanning. The current consensus is that this is due to the garbage collection in C# not being agressive enough. There are future plans to investigate and address this further in a general way, but the situation right now does not seem serious enough to block a stable release. If it does become evident that this is a major issue, a fix will be prioritized for a 10.6.1 release.

* [ALL] This release introduces the first of several major database schema changes as we move to EF Core, specifically to the User and Activity databases. UPON UPGRADING YOUR INSTANCE TO 10.6.0, YOU WILL NOT BE ABLE TO DOWNGRADE TO 10.5.5 OR EARLIER WITHOUT RENAMING AND EDITING MUTIPLE FILES IN MUTIPLE PLACES. **Make a backup of your instance before upgrading so downgrades can be a smooth and simple process.**

* [ALL] This release features a simultaneous release of jellyfin-ffmpeg v4.3.1. You should upgrade both at the same time for maximum compatibility, performance, and stabiity. However...

* [Debian/Ubuntu `amd64` `.deb`s] The updated jellyfin-ffmpeg v4.3.1 was not built on the following older releases due to an build failure of an additional included amd64-only dependency. Users of these releases will continue to use jellyfin-ffmpeg v4.2.3. This should be fine unless you wish to use QSV, which was buggy in v4.2.3; if you do, we recommend upgrading to a newer operating system version for your Jellyfin instance or switching to Docker-based installs in order to take full advantage of jellyfin-ffmpeg v4.3.1.
      - Debian Stretch (9.x)
      - Ubuntu Xenial (16.04)

* [Debian/Ubuntu Repository] ~The seamless apt upgrade seems to have been more troublesome than anticipated. If your upgrade fails, immediately run `apt -f install` with no other options and this should correct the situation. If not, try running `apt install jellyfin-server` instead.~ Fixed by package version `10.6.0-2` of `jellyfin-server` and `jellyfin`.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/26

### [jellyfin](https://github.com/jellyfin/jellyfin) [283]

 * #3596 [@joshuaboniface] Fix typo in CI configuration
 * #3593 [@joshuaboniface] Add NuGet publish step to tag CI
 * #3591 [@crobibero] Remove profile image before setting new
 * #3590 [@crobibero] Fix tvdb actors url
 * #3587 [@crobibero] fix UserManager UpdatePolicy
 * #3586 [@barronpm] Remove obsolete network path code
 * #3585 [@Ken-g6] 2354 fix soft link sizes
 * #3582 [@barronpm] Update .NET Core to 3.1.6
 * #3581 [@crobibero] Increase delete logging
 * #3579 [@crobibero] Add UserId filter to ActivityLog Entries endpoint
 * #3575 [@nyanmisaka] Bump the minimun required jellyfin-ffmpeg version
 * #3573 [@crobibero] Catch HttpRequestException when requesting plugins
 * #3570 [@crobibero] Add EnumeratorCancellation attribute
 * #3569 [@nyanmisaka] Fix QSV subtitle burn-in on windows and P010 detect
 * #3566 [@cvium] TVDB: Fetch image keytypes before querying images
 * #3563 [@cvium] Only fetch Next Up for episodes that have been fully matched
 * #3562 [@rotvel] Fix audio file transcoding.
 * #3557 [@crobibero] Fix update user
 * #3555 [@cvium] Fix disposed database context
 * #3553 [@joshuaboniface] Explicitly add what Azure used to do implicitly
 * #3549 [@neilsb] Prevent failure to bind to Auto Discover port being a fatal error
 * #3545 [@dependabot[bot]] Bump AutoFixture from 4.12.0 to 4.13.0
 * #3541 [@dkanada] Keep playstate during syncplay group creation
 * #3539 [@barronpm] Fix EF Core Memory Leak
 * #3535 [@crobibero] Fix syncplay function name
 * #3533 [@barronpm] Make User Authentication Case-insensitive and remove EF Core Log spam
 * #3522 [@crobibero] Clean syncplay endpoint names
 * #3519 [@joshuaboniface] Add conditionals to root YAML definition
 * #3516 [@dependabot[bot]] Bump Moq from 4.14.4 to 4.14.5
 * #3513 [@barronpm] Fix TypeLoadException during plugin load
 * #3505 [@Bond-009] Minor fixes
 * #3502 [@barronpm] Use Array.Empty
 * #3500 [@nyanmisaka] Add FFmpeg 4.3 detection and solve the green line on QSV HWA
 * #3495 [@anthonylavado] Use newer Jellyfin.XmlTv for Guide Fixes
 * #3480 [@neilsb] Respect FFMpeg path passed via Environment Variable
 * #3478 [@crobibero] bump autofixture
 * #3477 [@dependabot[bot]] Bump Swashbuckle.AspNetCore from 5.5.0 to 5.5.1
 * #3475 [@dependabot[bot]] Bump AutoFixture from 4.11.0 to 4.12.0
 * #3473 [@dependabot[bot]] Bump Moq from 4.14.3 to 4.14.4
 * #3465 [@BaronGreenback] 10.6.0.0 Null Pointer fix
 * #3461 [@Bond-009] Add support for ReadOnlySpan<char> in IgnorePatterns
 * #3456 [@crobibero] Add more ignorepatterns and tests
 * #3455 [@dkanada] Use constructor to set optimal config values
 * #3445 [@crobibero] catch skia errors when getting image dimensions
 * #3444 [@dkanada] Fix azure badge
 * #3439 [@cvium] Never ignore application folders
 * #3437 [@barronpm] Fix User Deletion
 * #3435 [@crobibero] revert missing session fields
 * #3431 [@BaronGreenback] Fix for #3404
 * #3425 [@crobibero] Revert ILoggerFactory usage in BaseItem.cs
 * #3423 [@crobibero] Remove EasyPassword from Authentication providers
 * #3418 [@Bond-009] Minor changes
 * #3417 [@dependabot[bot]] Bump Moq from 4.14.1 to 4.14.3
 * #3416 [@dependabot[bot]] Bump prometheus-net.AspNetCore from 3.5.0 to 3.6.0
 * #3415 [@dependabot[bot]] Bump Swashbuckle.AspNetCore from 5.4.1 to 5.5.0
 * #3414 [@dependabot[bot]] Bump prometheus-net from 3.5.0 to 3.6.0
 * #3411 [@neilsb] Prevent system plugins from being uninstalled
 * #3409 [@Bond-009] Fix scan crashed
 * #3407 [@telans] .gitignore: ignore jellyfin-web symlink & .vscode: dotnet telemetry optout
 * #3394 [@Ullmie02] Fix startup wizard in 10.6
 * #3390 [@telans] Multiple warning fixes
 * #3386 [@joshuaboniface]  Add Azure DevOps package builds
 * #3380 [@Bond-009] Enable TreatWarningsAsErrors in Release for MediaBrowser.Providers
 * #3378 [@crobibero] [SyncPlay] Remove (unused) SessionId route parameter
 * #3360 [@Bond-009] Fix Task that ignores cancellation request
 * #3358 [@crobibero] Enable BlurHash for People
 * #3353 [@Bond-009] Remove code for handling single hyphen arguments
 * #3351 [@dependabot[bot]] Bump IPNetwork2 from 2.4.0.126 to 2.5.211
 * #3350 [@dependabot[bot]] Bump sharpcompress from 0.25.0 to 0.25.1
 * #3349 [@dependabot[bot]] Bump Serilog.Sinks.Graylog from 2.1.2 to 2.1.3
 * #3348 [@dependabot[bot]] Bump CommandLineParser from 2.7.82 to 2.8.0
 * #3347 [@dependabot[bot]] Bump Swashbuckle.AspNetCore from 5.0.0 to 5.4.1
 * #3346 [@dependabot[bot]] Bump coverlet.collector from 1.2.1 to 1.3.0
 * #3344 [@dependabot[bot]] Bump PlaylistsNET from 1.0.4 to 1.0.6
 * #3343 [@telans] Add full stop at end of comments (SA1629)
 * #3342 [@BaronGreenback] Fix for [DLNA] Many log messages from Media Renderers trying to see old events
 * #3341 [@telans] Add newlines after closing braces (SA1513/SA1516)
 * #3336 [@telans] Fix trivial SA1005, SA1111, SA1508, SA1510 warnings
 * #3334 [@crobibero] Remove warnings from MediaBrowser.LocalMetadata
 * #3329 [@telans] Enable code analyzers for tests
 * #3316 [@aled] Fix server error when user enters a password, but none is set.
 * #3315 [@crobibero] Add MessageId to websocket message, fix ws exception
 * #3313 [@crobibero] Update to .NET Core 3.1.5
 * #3309 [@dependabot[bot]] Bump ServiceStack.Text.Core from 5.8.0 to 5.9.0
 * #3301 [@dependabot[bot]] Bump Moq from 4.13.1 to 4.14.1
 * #3298 [@dependabot[bot]] Bump SQLitePCLRaw.bundle_e_sqlite3 from 2.0.2 to 2.0.3
 * #3295 [@dependabot[bot]] Bump SkiaSharp from 1.68.1 to 1.68.3
 * #3294 [@dependabot[bot]] Bump Microsoft.NET.Test.Sdk from 16.5.0 to 16.6.1
 * #3293 [@dependabot[bot]] Bump System.Text.Encoding.CodePages from 4.7.0 to 4.7.1
 * #3292 [@dependabot[bot]] Bump SkiaSharp.NativeAssets.Linux from 1.68.1 to 1.68.3
 * #3291 [@cvium] Use the "legacy" AuthenticationException in AuthService
 * #3289 [@rigtorp] Clarify comment and log actual search string in TMDB search provider
 * #3284 [@EraYaN] Install compatibility tool from nuget instead of pulling a github release
 * #3282 [@aled] Fix a small number of compile warnings
 * #3270 [@KristupasSavickas] reduce log spam when generating blurhashes
 * #3268 [@crobibero] Force configuration paths to not be ignored.
 * #3267 [@pusta] CONTRIBUTORS.md - Updated jellyfin-server-windows to compile against .Net Core 3.1
 * #3262 [@dkanada] Disable sonarcloud until secrets are working
 * #3259 [@crobibero] Add omdb config as embedded resource
 * #3258 [@aled] Fix a small number of compile warnings
 * #3255 [@itegulov] Make books resumable
 * #3254 [@crobibero] Use typed logger where possible
 * #3252 [@YouKnowBlom] Fix incorrect HLS master playlist fields
 * #3250 [@shayaantx] Ignore languages with null ids when fetching images from tvdb
 * #3248 [@crobibero] Add dependabot
 * #3245 [@dkanada] Fix some issues with the CI
 * #3244 [@dkanada] Initial implementation for custom plugin repositories
 * #3237 [@Bond-009] Enable TreatWarningsAsErrors for more projects
 * #3236 [@Bond-009] Enable StyleCop for MediaBrowser.Common
 * #3235 [@Bond-009] Fix build
 * #3222 [@barronpm] Fix Activity Log Migrations for Very Old Databases
 * #3214 [@danieladov] Order ids to merge to avoid stack overflow
 * #3208 [@dkanada] More work for core plugins
 * #3203 [@Bond-009] Enable TreatWarningsAsErrors for Jellyfin.Server.Implementations in Release mode
 * #3192 [@dkanada] Fix issue with audio transcoding
 * #3187 [@joshuaboniface] Revert "Fix emby/user/public API leaking sensitive data"
 * #3185 [@Ullmie02] Don't Send Exception Messages (Old API)
 * #3180 [@xumix] Refactor copy codec checks
 * #3179 [@Bond-009] Fix some 'bugs' flagged by sonarcloud
 * #3174 [@dkanada] Remove uses of fnchecked from plugins
 * #3173 [@joshuaboniface] Add -k to keyserver curl command
 * #3164 [@dkanada] Fix a few issues with the plugin manifest
 * #3158 [@Artiume] Update Library Service
 * #3149 [@Artiume] Add .edl Mimetype
 * #3148 [@barronpm] Migrate User DB to EF Core
 * #3144 [@Artiume] Add lost+found to ignore list
 * #3138 [@mark-monteiro] Reduce Excessive Logging From DeveloperExceptionPageMiddleware
 * #3137 [@mark-monteiro] Correctly Support Translating External Ids
 * #3134 [@mark-monteiro] Update to .NET Core 3.1.4
 * #3133 [@kesslern] Fix 500 error causing first-time setup wizard to hang
 * #3118 [@barronpm] Fix regressions introduced by #3098
 * #3117 [@JustAMan] Fixes collections (and probably some extras support, too)
 * #3116 [@Artiume] Update Books Resolver File Types and add .opf Mime Type
 * #3115 [@MrTimscampi] Parse color transfer and color primaries from ffprobe, and fix video range
 * #3113 [@Artiume] Fix Progressive and Interlaced Stream capitalization
 * #3105 [@aled] Fix compile warnings in Jellyfin.Naming.Tests
 * #3099 [@rigtorp] Use glob patterns to ignore files
 * #3098 [@barronpm] Remove Support for Injecting ILogger Directly
 * #3089 [@MrTimscampi] Add more information to TmdbSeriesProvider
 * #3085 [@MrTimscampi] Add positionning cues to WebVTT writer
 * #3084 [@fhriley] Fix #3083: Set the Access-Control-Allow-Origin header to the request …
 * #3072 [@JustAMan] Re-raise the exception that caused LiveTV stream to not open
 * #3071 [@rigtorp] Make tvdb name normalizer unicode aware
 * #3066 [@Artiume] Remove ogg video mimetype
 * #3056 [@rigtorp] Reduce number of TMDB lookups if filenames have punctuation chars
 * #3050 [@Artiume] Update MimeTypes.cs
 * #3049 [@mark-monteiro] Fix editorconfig Settings
 * #3046 [@puschie286] allow bd tag in file names
 * #3043 [@puschie286] Jellyfin.Server as startup project
 * #3038 [@barronpm] Clean up generated code
 * #3037 [@ConfusedPolarBear] Fix CORS header not being added to exceptions
 * #3035 [@mark-monteiro] Do not double dispose item repository resources
 * #3033 [@neilsb] Allow override of address published by auto discovery
 * #3024 [@Bond-009] Remove ListHelper extensions
 * #3020 [@rigtorp] Fix container image build by installing python
 * #3007 [@BaronGreenback] Fix for #2986
 * #2995 [@JustAMan] Now parse date in header correctly as being in UTC
 * #2992 [@rotvel] Try harder to find ffmpeg in app directory. 
 * #2990 [@mark-monteiro] Create Missing Data Folders
 * #2985 [@sparky8251] Add Prometheus exporters
 * #2970 [@barronpm] Migrate Activity Database to Entity Framework Core
 * #2969 [@BaronGreenback] http in development mode crashed -
 * #2966 [@dkanada] Remove several deprecated utilities in the web package
 * #2960 [@ZadenRB] Adds annotation for content-type of ASP.NET Web API endpoints
 * #2950 [@Bond-009] Fix VideoResolver and tests
 * #2949 [@Bond-009] Enable TreatWarningsAsErrors for DvdLib
 * #2945 [@mark-monteiro] Add Integration Tests For BrandingService
 * #2943 [@mark-monteiro] Respect AutoRunWebApp and NoAutoRunWebApp settings when HostWebClient is false
 * #2940 [@balu92] Fix missing colons
 * #2936 [@anthonylavado] Remove JsonIgnore from the DateLastSaved property of BaseItem
 * #2920 [@Bond-009] Add some simple tests
 * #2917 [@Bond-009] Improved tests
 * #2916 [@Bond-009] Minor improvements
 * #2915 [@randrey] Fix imdbid regex
 * #2910 [@randrey] Additional mime types for DLNA (VLC)
 * #2906 [@randrey] Fix InvalidOperationException while browsing via DLNA client.
 * #2904 [@Bond-009] Use System.Buffers in RangeRequestWriter
 * #2903 [@randrey] Fix DLNA clients displaying wrong album art.
 * #2900 [@mark-monteiro] Use dependency injection to construct migration routines
 * #2880 [@Bond-009] Remove dead function
 * #2874 [@barronpm] Emby.Server.Implementations code cleanup and warning fixes (Part 1)
 * #2864 [@JustAMan] Make Last-Modified and If-Modified-Since headers follow the spec
 * #2862 [@mark-monteiro] Bump Mono.Nat from 2.0.0 to 2.0.1
 * #2861 [@mark-monteiro] Fix Auth Response Codes
 * #2855 [@Delgan] Improve movie resolver if space precedes the year
 * #2849 [@lyonzy] Handle null outputFileExtension in GetOutputFilePath
 * #2848 [@ZadenRB] Fix casing of JSON in Jellyfin API
 * #2846 [@dkanada] Remove requirement to build web during server builds
 * #2837 [@Bond-009] Minor IAsyncDisposable improvements
 * #2834 [@mark-monteiro] Add nuget.config file
 * #2830 [@Bond-009] DvdLib: remove dependency on MediaBrowser.Model
 * #2829 [@Bond-009] Fix some warnings
 * #2825 [@mark-monteiro] Fix misformed xml doc comment
 * #2821 [@nyanmisaka] Fix MPEG4 broken on VAAPI
 * #2817 [@ferferga] Remove unnecessary space in hardware decoders argument for ffmpeg
 * #2816 [@joshuaboniface] Revert "Specify a minimum version for jellyfin-ffmpeg dependency in .deb dependencies"
 * #2813 [@nyanmisaka] Switch to jellyfin-ffmpeg with integrated driver in docker build
 * #2809 [@nyanmisaka] Add more separate hardware decoding toggles, support videotoolbox
 * #2804 [@dtparr] Add Unit Tests for the Extras Directories
 * #2799 [@dkanada] Remove old windows job from pipeline
 * #2798 [@JustAMan] Make localhost LiveTV restreams always use plain HTTP port
 * #2797 [@mark-monteiro] Add MediaBrowser.WebDashboard\jellyfin-web to .gitignore
 * #2796 [@JustAMan] Make codec check in profile examine profile type first
 * #2794 [@mark-monteiro] Bump System.Text.Json from 4.7.0 to 4.7.1
 * #2793 [@mark-monteiro] Remove Ix.NET
 * #2792 [@mark-monteiro] Bump sharpcompress from 0.24.0 to 0.25.0
 * #2791 [@mark-monteiro] Bump coverlet.collector from 1.2.0 to 1.2.1
 * #2785 [@nyanmisaka] Fix MPEG4 packback error regression on vaapi
 * #2783 [@JustAMan] Add logging of URL being processed when logging an error
 * #2782 [@JustAMan] Fix support for attachments with baseURL set
 * #2779 [@KristupasSavickas] Fix ffmpeg path on ARM docker image
 * #2775 [@mark-monteiro] Port Forwarding Improvements
 * #2774 [@mark-monteiro] Simplify HTTPS Properties
 * #2772 [@barronpm] MediaBrowser.Api code cleanup
 * #2771 [@Bond-009] Enable nullabe reference types for Emby.Drawing and Jellyfin.Drawing.Skia
 * #2769 [@mark-monteiro] Make Plugin Repo URL Configurable
 * #2767 [@Bond-009] Enable nullabe reference types for MediaBrowser.Model
 * #2765 [@mark-monteiro] Register And Construct Services Correctly Using DI Framework
 * #2758 [@Bond-009] Remove PluginInstalled
 * #2755 [@Bond-009] Clean up SqliteItemRepository
 * #2749 [@hauntingEcho] Specify a minimum version for jellyfin-ffmpeg dependency in .deb dependencies
 * #2746 [@dafo90] Authentication request log with IP
 * #2745 [@Artiume] Force Audio Transcoding for LiveTV Transcoding
 * #2742 [@Bond-009] Enable Microsoft.CodeAnalysis.FxCopAnalyzers for Jellyfin.Common
 * #2741 [@Bond-009] Fix some warnings
 * #2740 [@JustAMan] Fix GetLocalApiUrl for cases with https enabled
 * #2735 [@mark-monteiro] Bump Microsoft.NET.Test.Sdk from 16.4.0 to 16.5.0
 * #2733 [@OancaAndrei] Add syncplay feature
 * #2731 [@Bond-009] Minor improvements
 * #2730 [@Bond-009] Try to not crash on unsupported plugin load
 * #2723 [@jairbubbles] Update Jellyfin.SkiaSharp.NativeAssets.LinuxArm to version 1.68.1
 * #2721 [@PrplHaz4] Separate Channels permissions from All Libraries
 * #2720 [@dkanada] Fix custom musicbrainz servers
 * #2715 [@nyanmisaka] Prefer to use libfdk_aac encoder for better audio quality when it is available
 * #2712 [@joshuaboniface] Revert #2146 ordering change
 * #2708 [@ox0spy] Dockerfile: support for non-ASCII characters
 * #2696 [@mark-monteiro] Display Extras With Unknown Types
 * #2680 [@mark-monteiro] Remove CommonProcess and ProcessFactory
 * #2678 [@ferferga] Translate Scheduled Tasks
 * #2676 [@GranPC] Implement Blurhash generation for images
 * #2674 [@JustAMan] Make variables binding correspond with column names
 * #2669 [@mark-monteiro] Update .NET Core to 3.1.3
 * #2668 [@mark-monteiro] Fix ApplicationHost Dispose() method
 * #2667 [@crobibero] Fix warnings in Emby.Naming
 * #2660 [@Bond-009] Minor style fixes
 * #2657 [@villagra] Add netstandard2.0 as TargetFramework
 * #2656 [@joshuaboniface] Improve builds
 * #2655 [@lfoust] Fix FormatException when mapping TVDB series
 * #2653 [@iwalton3] Fix embedded mkv subtitles.
 * #2645 [@sparky8251] Add RSS feed badges to README
 * #2642 [@mark-monteiro] Add missing null check when retrieving extras
 * #2639 [@alset333] Change DeinterlaceMethod's "bobandweave" to "yadif" or "yadif_bob", and set default value
 * #2638 [@mark-monteiro] Update .NET Core to 3.1.2
 * #2637 [@mark-monteiro] Do not instantiate IService instances unecessarily at startup
 * #2636 [@mark-monteiro] Use ASP.NET Core HTTPS Development Certificate
 * #2635 [@mark-monteiro] Use ASP Development Exception Page
 * #2634 [@mark-monteiro] Enable HTTP/2 support
 * #2631 [@mark-monteiro] Fix Client Build Scripts
 * #2621 [@mark-monteiro] Log 'JELLYFIN_' environment variables at application start
 * #2620 [@mark-monteiro] Add Development Documentation To README
 * #2617 [@Shawmon] add wasm mimetype
 * #2607 [@joshuaboniface] Correct BuildRequires and NodeJS for Fedora/CentOS
 * #2606 [@Artiume] Update docker dependencies for Gulp
 * #2603 [@mark-monteiro] Fix Azure Pipelines Build
 * #2601 [@mark-monteiro] Support Running Server Without Web Content
 * #2582 [@Bond-009] Fix subtitles
 * #2573 [@YouKnowBlom] Add codecs, resolution and frame-rate fields to HLS master playlist
 * #2566 [@mark-monteiro] Feature Request Issue Template
 * #2559 [@whooo] Add descriptive TV episode titles for DLNA browsing
 * #2549 [@dkanada] Refactor some provider classes
 * #2541 [@joshuaboniface] Fix curl for Jellyfin GPG key
 * #2506 [@mark-monteiro] Inject loggers with context using ILogger<T>
 * #2503 [@nyanmisaka] Fix various bugs in HWA subtitle burn-in
 * #2502 [@JustAMan] Adds BaseItem.Equals method that compares items by their Id
 * #2497 [@mark-monteiro] Check for duplicates when adding items to a playlist
 * #2492 [@Polpetta] Fix emby/user/public API leaking sensitive data
 * #2480 [@mark-monteiro] Support Injecting IConfiguration
 * #2478 [@JustAMan] Fix ordering of search results
 * #2466 [@dkanada] Update plugin classes for nightly builds
 * #2449 [@Bond-009] Fix some warnings
 * #2447 [@Bond-009] Add analyzers to MediaBrowser.Providers and minor improvements
 * #2293 [@EraYaN] Add new EF Core data model (v2)
 * #2162 [@Bond-009] Rewrite WebSocket handling code
 * #2154 [@dkanada] Add image provider for artists

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [310]

 * jellyfin/jellyfin-web#1579 [@dependabot[bot]] Bump lodash from 4.17.15 to 4.17.19
 * jellyfin/jellyfin-web#1578 [@dmitrylyzo] Change volume slider event
 * jellyfin/jellyfin-web#1575 [@thornbill] Remove iOS footer hack
 * jellyfin/jellyfin-web#1574 [@thornbill] Fix lighter header/footer background color
 * jellyfin/jellyfin-web#1573 [@MrTimscampi] Minor fixes
 * jellyfin/jellyfin-web#1571 [@ferferga] Remove repeated fav icon in remotecontrol in desktop layout
 * jellyfin/jellyfin-web#1563 [@joshuaboniface] Explicitly add what Azure used to do implicitly
 * jellyfin/jellyfin-web#1559 [@dependabot-preview[bot]] Bump whatwg-fetch from 3.1.0 to 3.2.0
 * jellyfin/jellyfin-web#1557 [@dependabot-preview[bot]] Bump autoprefixer from 9.8.4 to 9.8.5
 * jellyfin/jellyfin-web#1551 [@dkanada] Fix some style issues on item details and now playing
 * jellyfin/jellyfin-web#1544 [@Camc314] Dashboard Styling Bug fixes (add library text cut off, css textbox, and too long last seen text)
 * jellyfin/jellyfin-web#1541 [@Camc314] Migration of display, home, playback and subtitles to ES6 modules and small fixes
 * jellyfin/jellyfin-web#1534 [@MrTimscampi] Use new SyncPlay API client
 * jellyfin/jellyfin-web#1532 [@Camc314] Further fixes for purplehaze and AppleTV
 * jellyfin/jellyfin-web#1531 [@MrTimscampi] Adjust text selection rules and add provider name to identification results
 * jellyfin/jellyfin-web#1528 [@dependabot-preview[bot]] Bump hls.js from 0.13.2 to 0.14.0
 * jellyfin/jellyfin-web#1521 [@dependabot-preview[bot]] Bump intersection-observer from 0.10.0 to 0.11.0
 * jellyfin/jellyfin-web#1519 [@Camc314] Fixing Border radius and light theme improvements
 * jellyfin/jellyfin-web#1516 [@MrTimscampi] Update deps
 * jellyfin/jellyfin-web#1510 [@MrTimscampi] Fix back button not stopping video playback
 * jellyfin/jellyfin-web#1509 [@MrTimscampi] Remove blurhash from listView
 * jellyfin/jellyfin-web#1506 [@ferferga] Add missing placeholder icons
 * jellyfin/jellyfin-web#1504 [@MrTimscampi] Prevent text selection
 * jellyfin/jellyfin-web#1498 [@MrTimscampi] Improve blurhash performance
 * jellyfin/jellyfin-web#1497 [@MrTimscampi] Add defered appLoader and splash screen
 * jellyfin/jellyfin-web#1496 [@dmitrylyzo] Rearrange keydown event handling
 * jellyfin/jellyfin-web#1495 [@dmitrylyzo] Fix Firefox subtitle offset
 * jellyfin/jellyfin-web#1494 [@dmitrylyzo] Friendly SubtitleSync
 * jellyfin/jellyfin-web#1488 [@dkanada] Fix redirect issue on video player
 * jellyfin/jellyfin-web#1485 [@ferferga] Add missing tooltip for TV layout
 * jellyfin/jellyfin-web#1477 [@dmitrylyzo] Hide hamburger button on TV
 * jellyfin/jellyfin-web#1475 [@crobibero] remove sessionId parameter from api calls
 * jellyfin/jellyfin-web#1473 [@dependabot-preview[bot]] Bump @babel/preset-env from 7.10.2 to 7.10.3
 * jellyfin/jellyfin-web#1472 [@dependabot-preview[bot]] Bump swiper from 5.4.3 to 5.4.5
 * jellyfin/jellyfin-web#1471 [@dependabot-preview[bot]] Bump stylelint from 13.6.0 to 13.6.1
 * jellyfin/jellyfin-web#1470 [@dependabot-preview[bot]] Bump jstree from 3.3.9 to 3.3.10
 * jellyfin/jellyfin-web#1468 [@dependabot-preview[bot]] Bump @babel/core from 7.10.2 to 7.10.3
 * jellyfin/jellyfin-web#1467 [@dependabot-preview[bot]] Bump fast-text-encoding from 1.0.2 to 1.0.3
 * jellyfin/jellyfin-web#1466 [@dependabot-preview[bot]] Bump autoprefixer from 9.8.0 to 9.8.2
 * jellyfin/jellyfin-web#1465 [@dependabot-preview[bot]] Bump shaka-player from 2.5.13 to 3.0.1
 * jellyfin/jellyfin-web#1464 [@neilsb] Prevent removal of system plugins
 * jellyfin/jellyfin-web#1463 [@MrTimscampi] Fix latest section portrait cards not being portrait in all cases
 * jellyfin/jellyfin-web#1462 [@KGT1] ActionHandler 'seekto' for Media Notification Seekbar
 * jellyfin/jellyfin-web#1461 [@MrTimscampi] Fix issue with IntersectionObserver root margin
 * jellyfin/jellyfin-web#1452 [@MrTimscampi] Use parent poster for items with children
 * jellyfin/jellyfin-web#1448 [@joshuaboniface] Make the portable web archive and dir consistent
 * jellyfin/jellyfin-web#1445 [@ferferga] Add tooltips for header icons
 * jellyfin/jellyfin-web#1444 [@grafixeyehero] Remove unused  loadingDialog & serverRestartDialog
 * jellyfin/jellyfin-web#1442 [@Delgan]  Fix media info dialog visually refreshing library page in background 
 * jellyfin/jellyfin-web#1441 [@grafixeyehero] Fix context Event Listener for metadataEditor
 * jellyfin/jellyfin-web#1439 [@Delgan] Fix broken image uploader due to missing '#dropImageText' element
 * jellyfin/jellyfin-web#1437 [@ferferga] CSS fixes when resizing library browser
 * jellyfin/jellyfin-web#1432 [@dmitrylyzo] Don't start time sync if not in SyncPlay mode
 * jellyfin/jellyfin-web#1430 [@ferferga] Player hotfixes and improvements
 * jellyfin/jellyfin-web#1427 [@ferferga] Remove leftover from #1046
 * jellyfin/jellyfin-web#1416 [@joshuaboniface] Ensure collection step depends on build steps
 * jellyfin/jellyfin-web#1414 [@dependabot-preview[bot]] Bump query-string from 6.13.0 to 6.13.1
 * jellyfin/jellyfin-web#1413 [@dependabot-preview[bot]] Bump eslint-plugin-import from 2.21.1 to 2.21.2
 * jellyfin/jellyfin-web#1412 [@dependabot-preview[bot]] Bump shaka-player from 2.5.12 to 2.5.13
 * jellyfin/jellyfin-web#1411 [@dependabot-preview[bot]] Bump swiper from 5.4.2 to 5.4.3
 * jellyfin/jellyfin-web#1410 [@dependabot-preview[bot]] Bump css-loader from 3.5.3 to 3.6.0
 * jellyfin/jellyfin-web#1409 [@Camc314] Fix "Drop image here, or click to browse" persistent Visual
 * jellyfin/jellyfin-web#1406 [@Delgan] Avoid async rendering of MediaSources tracks to prevent content jump
 * jellyfin/jellyfin-web#1405 [@Camc314] Fix Movie Progress Bar Width
 * jellyfin/jellyfin-web#1401 [@MrTimscampi] Remove standalone mode
 * jellyfin/jellyfin-web#1399 [@dkanada] Add packaging step on azure and refactor pipelines
 * jellyfin/jellyfin-web#1398 [@thornbill] Restore menu options in mobile view
 * jellyfin/jellyfin-web#1393 [@dkanada] Initial work for repository configuration
 * jellyfin/jellyfin-web#1392 [@grafixeyehero] Fix typo and remove unused legacy dashboard
 * jellyfin/jellyfin-web#1391 [@MrTimscampi] Use explicit codec checks for DTS and VC-1
 * jellyfin/jellyfin-web#1386 [@ferferga] Fix episodes listing after blurhash
 * jellyfin/jellyfin-web#1383 [@dependabot-preview[bot]] Bump query-string from 6.12.1 to 6.13.0
 * jellyfin/jellyfin-web#1382 [@dependabot-preview[bot]] Bump swiper from 5.4.1 to 5.4.2
 * jellyfin/jellyfin-web#1379 [@dependabot-preview[bot]] Bump eslint-plugin-import from 2.20.2 to 2.21.1
 * jellyfin/jellyfin-web#1378 [@dependabot-preview[bot]] Bump stylelint from 13.5.0 to 13.6.0
 * jellyfin/jellyfin-web#1377 [@dependabot-preview[bot]] Bump jellyfin-apiclient from 1.2.1 to 1.2.2
 * jellyfin/jellyfin-web#1376 [@dependabot-preview[bot]] Bump stylelint-order from 4.0.0 to 4.1.0
 * jellyfin/jellyfin-web#1375 [@dependabot-preview[bot]] Bump gulp-cli from 2.2.1 to 2.3.0
 * jellyfin/jellyfin-web#1373 [@crobibero] Fix all jQuery checked.
 * jellyfin/jellyfin-web#1371 [@crobibero] Fix plugin display without config page
 * jellyfin/jellyfin-web#1369 [@MrTimscampi] Small browser profile fixes
 * jellyfin/jellyfin-web#1368 [@itegulov] Make book player restore location on resume
 * jellyfin/jellyfin-web#1367 [@dkanada] Add support for es6 controllers and migrate logs controller
 * jellyfin/jellyfin-web#1366 [@dkanada] Update casing for some files and add placeholder elements
 * jellyfin/jellyfin-web#1360 [@MrTimscampi] Remove the 500 item limitation on photo playback
 * jellyfin/jellyfin-web#1357 [@ferferga] Change key name from EnableFastImageFadeIn to EnableFasterAnimations
 * jellyfin/jellyfin-web#1355 [@MrTimscampi] Make the default card colors look less like rainbow vomit
 * jellyfin/jellyfin-web#1354 [@MrTimscampi] Fix baseUrl for web config file
 * jellyfin/jellyfin-web#1353 [@grafixeyehero] Migration accessSchedule to ES6 modules
 * jellyfin/jellyfin-web#1352 [@grafixeyehero] Migrate chaptercardbuilder and peoplecardbuilder to es6 modules
 * jellyfin/jellyfin-web#1347 [@Brissot] Fixing Chrome's Unnecessary AV1 Transcode and Combined WebM Profiles
 * jellyfin/jellyfin-web#1345 [@dmitrylyzo] Babel epubjs (WebOS 1.2)
 * jellyfin/jellyfin-web#1344 [@Artiume] Change Default for OptionAutomaticallyGroupSeries
 * jellyfin/jellyfin-web#1342 [@dmitrylyzo] Fix userSettings.chromecastVersion call
 * jellyfin/jellyfin-web#1341 [@MrTimscampi] Fix traceback in SyncPlay when casting to Google Cast
 * jellyfin/jellyfin-web#1339 [@dependabot-preview[bot]] Bump @babel/core from 7.10.1 to 7.10.2
 * jellyfin/jellyfin-web#1338 [@dependabot-preview[bot]] Bump eslint-plugin-eslint-comments from 3.1.2 to 3.2.0
 * jellyfin/jellyfin-web#1337 [@dependabot-preview[bot]] Bump shaka-player from 2.5.11 to 2.5.12
 * jellyfin/jellyfin-web#1336 [@dependabot-preview[bot]] Bump @babel/preset-env from 7.10.1 to 7.10.2
 * jellyfin/jellyfin-web#1331 [@MrTimscampi] Remove non-standalone mode
 * jellyfin/jellyfin-web#1328 [@MrTimscampi] Add format checking to EPUB player
 * jellyfin/jellyfin-web#1327 [@Camc314] Fix Page jumps when entering custom css
 * jellyfin/jellyfin-web#1322 [@MrTimscampi] Update API client and dependencies
 * jellyfin/jellyfin-web#1321 [@MrTimscampi] Lint and build improvements
 * jellyfin/jellyfin-web#1317 [@MrTimscampi] Update apiclient
 * jellyfin/jellyfin-web#1315 [@dmitrylyzo] Fix ability to change settings of another user
 * jellyfin/jellyfin-web#1311 [@dmitrylyzo] Enable babel for date-fns
 * jellyfin/jellyfin-web#1310 [@Artiume] Add Genres to Home Screen
 * jellyfin/jellyfin-web#1309 [@bendardenne] Transfer whole playlist when transferring playback
 * jellyfin/jellyfin-web#1307 [@anthonylavado] Include explicit yarn version
 * jellyfin/jellyfin-web#1305 [@Camc314] Edit Image Cropped Fix #1207
 * jellyfin/jellyfin-web#1304 [@dkanada] Update apiclient to fix some issues
 * jellyfin/jellyfin-web#1302 [@dependabot-preview[bot]] Bump swiper from 5.4.0 to 5.4.1
 * jellyfin/jellyfin-web#1301 [@dependabot-preview[bot]] Bump gulp-cli from 2.2.0 to 2.2.1
 * jellyfin/jellyfin-web#1299 [@dependabot-preview[bot]] Bump date-fns from 2.13.0 to 2.14.0
 * jellyfin/jellyfin-web#1298 [@dependabot-preview[bot]] Bump stylelint from 13.4.0 to 13.5.0
 * jellyfin/jellyfin-web#1296 [@Camc314] Minor changes to Apple TV theme
 * jellyfin/jellyfin-web#1294 [@dkanada] Remove legacy jquery function from source
 * jellyfin/jellyfin-web#1293 [@mark-monteiro] Support restarting the server on all platforms
 * jellyfin/jellyfin-web#1291 [@dkanada] Fix an issue with plugin installation
 * jellyfin/jellyfin-web#1288 [@dkanada] Add display preference for details banner and update some defaults
 * jellyfin/jellyfin-web#1286 [@ferferga] Implement blurhash (follow-up of #987 but from scratch)
 * jellyfin/jellyfin-web#1284 [@Delgan] Migrate components/playback functions to ES6 modules
 * jellyfin/jellyfin-web#1283 [@thornbill] Make the share url link to the actual item instead of github
 * jellyfin/jellyfin-web#1282 [@Artiume] Move Network paths to be next to Optional Path
 * jellyfin/jellyfin-web#1280 [@dmitrylyzo] Fix dependency loop
 * jellyfin/jellyfin-web#1279 [@dmitrylyzo] Fix actionSheet
 * jellyfin/jellyfin-web#1277 [@ferferga] Fix #1141 linting
 * jellyfin/jellyfin-web#1276 [@KucharczykL] Add en-us strings for DVR.
 * jellyfin/jellyfin-web#1275 [@KucharczykL] Make DVR heading translatable.
 * jellyfin/jellyfin-web#1273 [@ferferga] Fix scrollHelper reference
 * jellyfin/jellyfin-web#1272 [@Artiume] Toggle off uPnP Port Forwarding as Default for Startup Wizard
 * jellyfin/jellyfin-web#1269 [@dkanada] Convert photo player to class
 * jellyfin/jellyfin-web#1266 [@MrTimscampi] Move plugins to a dedicated directory
 * jellyfin/jellyfin-web#1263 [@itegulov] Implement minimalistic EPUB reader
 * jellyfin/jellyfin-web#1262 [@dependabot-preview[bot]] Bump howler from 2.1.3 to 2.2.0
 * jellyfin/jellyfin-web#1261 [@dependabot-preview[bot]] Bump stylelint from 13.3.3 to 13.4.0
 * jellyfin/jellyfin-web#1259 [@dependabot-preview[bot]] Bump swiper from 5.3.8 to 5.4.0
 * jellyfin/jellyfin-web#1257 [@dependabot-preview[bot]] Bump autoprefixer from 9.7.6 to 9.8.0
 * jellyfin/jellyfin-web#1253 [@MrTimscampi] Force spacing around operators
 * jellyfin/jellyfin-web#1251 [@adavier] Fix Quality Settings for Aspect Ratios less than 16:9 (1.77)
 * jellyfin/jellyfin-web#1246 [@dkanada] Clean up the translation files
 * jellyfin/jellyfin-web#1243 [@dkanada] Refactor a bunch of filenames and folders
 * jellyfin/jellyfin-web#1242 [@dkanada] Implement select menu for chromecast version
 * jellyfin/jellyfin-web#1239 [@ferferga] Revert 9a47428 changes, so IPs are allowed
 * jellyfin/jellyfin-web#1238 [@ferferga] Remove imageFetcher
 * jellyfin/jellyfin-web#1232 [@MrTimscampi] Fix more sonarqube bugs
 * jellyfin/jellyfin-web#1231 [@Artiume] Fix Progressive Stream 'P' capitalization
 * jellyfin/jellyfin-web#1229 [@ferferga] Keep scrollbar always present to avoid UI clipping
 * jellyfin/jellyfin-web#1223 [@dkanada] Fix wizard route and config load error
 * jellyfin/jellyfin-web#1222 [@MrTimscampi] Make dialogs more bearable
 * jellyfin/jellyfin-web#1221 [@dependabot-preview[bot]] Bump date-fns from 2.12.0 to 2.13.0
 * jellyfin/jellyfin-web#1219 [@dependabot-preview[bot]] Bump webpack-dev-server from 3.10.3 to 3.11.0
 * jellyfin/jellyfin-web#1218 [@dependabot-preview[bot]] Bump jquery from 3.5.0 to 3.5.1
 * jellyfin/jellyfin-web#1217 [@dependabot-preview[bot]] Bump shaka-player from 2.5.10 to 2.5.11
 * jellyfin/jellyfin-web#1213 [@MrTimscampi] Hide the previous page when loading videoOsd
 * jellyfin/jellyfin-web#1211 [@fhriley] Fix #1210: Add credentials to XHR requests
 * jellyfin/jellyfin-web#1208 [@twinkybot] Per default a new user has no access to any library
 * jellyfin/jellyfin-web#1206 [@MrTimscampi] Fix some issues with details page and small redesign
 * jellyfin/jellyfin-web#1205 [@dmitrylyzo] Fix slider thumb on WebOS 2
 * jellyfin/jellyfin-web#1204 [@dmitrylyzo] Fix slideshow (Safari, WebOS 2)
 * jellyfin/jellyfin-web#1203 [@dmitrylyzo] Fix browserslist for autoprefixer
 * jellyfin/jellyfin-web#1200 [@dmitrylyzo] Babel apiclient and fix reference name
 * jellyfin/jellyfin-web#1198 [@ferferga] Switch player backdrops to poster attribute of the video element
 * jellyfin/jellyfin-web#1196 [@MrTimscampi] Remove leftover API client file
 * jellyfin/jellyfin-web#1192 [@dmitrylyzo] Use root build config
 * jellyfin/jellyfin-web#1188 [@dependabot-preview[bot]] Bump core-js from 3.6.4 to 3.6.5
 * jellyfin/jellyfin-web#1187 [@dependabot-preview[bot]] Bump stylelint from 13.2.1 to 13.3.3
 * jellyfin/jellyfin-web#1186 [@dependabot-preview[bot]] Bump date-fns from 2.11.1 to 2.12.0
 * jellyfin/jellyfin-web#1185 [@dependabot-preview[bot]] Bump @babel/core from 7.9.0 to 7.9.6
 * jellyfin/jellyfin-web#1184 [@dependabot-preview[bot]] Bump page from 1.11.5 to 1.11.6
 * jellyfin/jellyfin-web#1183 [@dependabot-preview[bot]] Bump @babel/plugin-transform-modules-amd from 7.9.0 to 7.9.6
 * jellyfin/jellyfin-web#1182 [@dependabot-preview[bot]] Bump html-webpack-plugin from 4.0.2 to 4.3.0
 * jellyfin/jellyfin-web#1181 [@dependabot-preview[bot]] Bump intersection-observer from 0.7.0 to 0.10.0
 * jellyfin/jellyfin-web#1177 [@dmitrylyzo] Fix backdrop screensaver: autoplay and hide
 * jellyfin/jellyfin-web#1173 [@sarab97] Migrate deleteHelper, actionSheet, indicators and playMenu to ES6
 * jellyfin/jellyfin-web#1171 [@MrTimscampi] Enable a simple color placeholder for loading cards
 * jellyfin/jellyfin-web#1168 [@sarab97] fixed aspect ratio display issue of photo
 * jellyfin/jellyfin-web#1167 [@Brissot] Added AV1 Codec Profile to Avoid Transcode
 * jellyfin/jellyfin-web#1166 [@sarab97] Download button fix on photos slideshow
 * jellyfin/jellyfin-web#1165 [@MrTimscampi] Add dependabot config
 * jellyfin/jellyfin-web#1162 [@MrTimscampi] Remove the small logo in OSD and details page
 * jellyfin/jellyfin-web#1159 [@dependabot[bot]] Bump jquery from 3.4.1 to 3.5.0
 * jellyfin/jellyfin-web#1156 [@ferferga] Change EOL of dfnshelper from CRLF to LF
 * jellyfin/jellyfin-web#1155 [@ferferga] Vertical menu
 * jellyfin/jellyfin-web#1150 [@nielsvanvelzen] Remove limit of 50 for tag filter
 * jellyfin/jellyfin-web#1146 [@JustAMan] Fix some issues blocking WebOS 1.2 / 2.0
 * jellyfin/jellyfin-web#1145 [@MrTimscampi] Add a CODEOWNERS file
 * jellyfin/jellyfin-web#1144 [@JustAMan] Fix .ASS offset when seeking a progressive stream
 * jellyfin/jellyfin-web#1142 [@sarab97] fix playlist translation for en language
 * jellyfin/jellyfin-web#1141 [@cromefire] Register plugins with promises
 * jellyfin/jellyfin-web#1140 [@mark-monteiro] Clean up network settings page
 * jellyfin/jellyfin-web#1137 [@MrTimscampi] Update path to moved modules in ES6 modules
 * jellyfin/jellyfin-web#1135 [@MrTimscampi] Fix an issue with Screenfull on iOS
 * jellyfin/jellyfin-web#1134 [@MrTimscampi] Use posters for latest TV shows
 * jellyfin/jellyfin-web#1131 [@dmitrylyzo] Icons for WebOS 2
 * jellyfin/jellyfin-web#1130 [@dmitrylyzo] Fix keyboard navigation on remotecontrol page
 * jellyfin/jellyfin-web#1129 [@MrTimscampi] Convert ESLint config to JavaScript, lint all files and re-add autoprefixer
 * jellyfin/jellyfin-web#1127 [@Delgan] Fix pointer missing in "create new lib" link
 * jellyfin/jellyfin-web#1126 [@MrTimscampi] Check appSettings for undefined
 * jellyfin/jellyfin-web#1125 [@dmitrylyzo] Fix event subscription on remotecontrol page
 * jellyfin/jellyfin-web#1124 [@MrTimscampi] Use TV layout by default on PS4
 * jellyfin/jellyfin-web#1123 [@MrTimscampi] Move headroom to bundle
 * jellyfin/jellyfin-web#1122 [@MrTimscampi] Only inject appLoader if using standalone mode
 * jellyfin/jellyfin-web#1121 [@dkanada] Update more route locations
 * jellyfin/jellyfin-web#1119 [@JustAMan] Add check for funky Promise faced on WebOS 2
 * jellyfin/jellyfin-web#1116 [@samuel9554] [Feature Request] Zoom In on Photos
 * jellyfin/jellyfin-web#1114 [@redSpoutnik] Fix SubtitleSync-TextField behavior
 * jellyfin/jellyfin-web#1113 [@MrTimscampi] Add title and year to posters in TV genres view
 * jellyfin/jellyfin-web#1109 [@YouKnowBlom] Change Chromecast player name to Google Cast
 * jellyfin/jellyfin-web#1108 [@nielsvanvelzen] Add Android icon for Android TV in devices page
 * jellyfin/jellyfin-web#1106 [@dmitrylyzo] Fix inputManager trigger
 * jellyfin/jellyfin-web#1105 [@thornbill] Restore user menu on mobile
 * jellyfin/jellyfin-web#1104 [@dmitrylyzo] Fix reference to undefined variable
 * jellyfin/jellyfin-web#1103 [@MrTimscampi] Fix accidentally deleted CSS in details page
 * jellyfin/jellyfin-web#1100 [@dmitrylyzo] Add scheduled playback progress report
 * jellyfin/jellyfin-web#1099 [@Delgan] Fix dropdown not properly aligned for long subtitles
 * jellyfin/jellyfin-web#1095 [@JustAMan] Fix .ass subtitles not starting on mobile
 * jellyfin/jellyfin-web#1093 [@MrTimscampi] Fix some mobile navigation issues
 * jellyfin/jellyfin-web#1092 [@MrTimscampi] Use screenfull to handle fullscreen switching
 * jellyfin/jellyfin-web#1089 [@cromefire] Migrating backdropscreensaver, filterdialog and fetchhelper to ES6
 * jellyfin/jellyfin-web#1088 [@MrTimscampi] Update and cleanup MediaSessions
 * jellyfin/jellyfin-web#1084 [@MrTimscampi] Fix more Sonarqube issues
 * jellyfin/jellyfin-web#1083 [@mark-monteiro] Handle 401 & 403 Server Responses Correctly
 * jellyfin/jellyfin-web#1076 [@MrTimscampi] Finish moving elements
 * jellyfin/jellyfin-web#1074 [@dmitrylyzo] Move delayed volume update to playbackManager
 * jellyfin/jellyfin-web#1072 [@ferferga] Move "hide watched media" checkbox
 * jellyfin/jellyfin-web#1071 [@dkanada] Zip the built files before publish
 * jellyfin/jellyfin-web#1070 [@redSpoutnik] Set subtitle-sync for SubtitlesOctopus
 * jellyfin/jellyfin-web#1069 [@MrTimscampi] Force the use of single quotes
 * jellyfin/jellyfin-web#1068 [@dkanada] Pass title and filename to native shell
 * jellyfin/jellyfin-web#1065 [@MrTimscampi] Add unloading capability to the image loader
 * jellyfin/jellyfin-web#1063 [@dkanada] Update plugin pages for new manifest properties
 * jellyfin/jellyfin-web#1056 [@samuel9554] Revamp player (nowplaying.html, remotecontrol.js)
 * jellyfin/jellyfin-web#1053 [@MrTimscampi] Use development mode for dev server
 * jellyfin/jellyfin-web#1049 [@JustAMan] Fix newline breaks in SRT subtitles shown in Firefox
 * jellyfin/jellyfin-web#1048 [@JustAMan] Use patched octopus that works on Cordova
 * jellyfin/jellyfin-web#1047 [@ZadenRB] Fix inconsistent value in drop down list on library page
 * jellyfin/jellyfin-web#1046 [@nyanmisaka] Add more separate hardware decoding toggles
 * jellyfin/jellyfin-web#1042 [@ZadenRB] Remove suffix for duration of tasks on scheduled tasks page
 * jellyfin/jellyfin-web#1040 [@JustAMan] Fix native hls resume
 * jellyfin/jellyfin-web#1039 [@MrTimscampi] Sonarqube bug fixin' - Part 1: Phantom Bugs
 * jellyfin/jellyfin-web#1034 [@rexbron] Set autocaptialize to 'off' on the login username form
 * jellyfin/jellyfin-web#1032 [@MrTimscampi] Fix semicolons and throw error in ESLint if missing
 * jellyfin/jellyfin-web#1029 [@ferferga] Globalize shouldn't require ConnectionManager
 * jellyfin/jellyfin-web#1028 [@ZadenRB] Fixed alignment of subsections on item details page
 * jellyfin/jellyfin-web#1026 [@dmitrylyzo] Babel query-string to support older browsers
 * jellyfin/jellyfin-web#1024 [@MrTimscampi] Throw linting errors if using non-polyfilled APIs
 * jellyfin/jellyfin-web#1022 [@ferferga] Fix mobile layout for itemdetails
 * jellyfin/jellyfin-web#1020 [@JustAMan] Fix attachment delivery urls
 * jellyfin/jellyfin-web#1016 [@MrTimscampi] Touch up ESLint config
 * jellyfin/jellyfin-web#1015 [@dkanada] Convert all config files to ES6 and remove unused controller
 * jellyfin/jellyfin-web#1014 [@MrTimscampi] Remove duplicate implementations of parentWithClass()
 * jellyfin/jellyfin-web#1011 [@OancaAndrei] Add syncplay feature
 * jellyfin/jellyfin-web#1007 [@MrTimscampi] Remove API Client from the tree
 * jellyfin/jellyfin-web#1005 [@JustAMan] Switch to new version of JavascriptSubtitlesOctopus, enable new options
 * jellyfin/jellyfin-web#1004 [@ferferga] Don't use Globalize globally
 * jellyfin/jellyfin-web#1003 [@MrTimscampi] Fix admin drawer logo showing up everywhere
 * jellyfin/jellyfin-web#1000 [@Nazar78] Support H264 Level 52 (Tizen 5.0)
 * jellyfin/jellyfin-web#999 [@dmitrylyzo] ES6 migration: autoFocuser, dom, scrollManager
 * jellyfin/jellyfin-web#996 [@MrTimscampi] Update CI to use NodeJS 12.x
 * jellyfin/jellyfin-web#992 [@dmitrylyzo] Fix dom addEventListener/removeEventListener
 * jellyfin/jellyfin-web#991 [@Stampede10343] Migrate some easy components to ES6
 * jellyfin/jellyfin-web#989 [@dmitrylyzo] Fix subtitle settings in Tizen
 * jellyfin/jellyfin-web#985 [@dmitrylyzo] Add browser lazy-sync
 * jellyfin/jellyfin-web#984 [@MrTimscampi] Fix Browsersync JavaScript reload error
 * jellyfin/jellyfin-web#983 [@MrTimscampi] Make the page limit configurable
 * jellyfin/jellyfin-web#979 [@dmitrylyzo] Fix view restoring
 * jellyfin/jellyfin-web#978 [@joshuaboniface] Improve and split builds
 * jellyfin/jellyfin-web#975 [@Nickbert7] Fix cast sender api path
 * jellyfin/jellyfin-web#971 [@lfoust] Display specific types for ExternalIds
 * jellyfin/jellyfin-web#970 [@MrTimscampi] Clean up the menus on mobile
 * jellyfin/jellyfin-web#969 [@dmitrylyzo] Fix XviD playback on Tizen
 * jellyfin/jellyfin-web#968 [@alset333] Add controls for DeinterlaceMethod
 * jellyfin/jellyfin-web#967 [@MrTimscampi] Refactor slideshow.js
 * jellyfin/jellyfin-web#963 [@MrTimscampi] Don't scale logo on details page
 * jellyfin/jellyfin-web#962 [@dkanada] Add method to open client settings
 * jellyfin/jellyfin-web#960 [@ferferga] Translate missing items - Part 1
 * jellyfin/jellyfin-web#958 [@MrTimscampi] Show missing indicator in ListView
 * jellyfin/jellyfin-web#955 [@thornbill] Fix schedules direct buttons being hidden by default
 * jellyfin/jellyfin-web#953 [@dkanada] Remove tar from published artifacts
 * jellyfin/jellyfin-web#952 [@dkanada] Publish web releases on azure
 * jellyfin/jellyfin-web#951 [@dtparr] Correct the url in the wizardstart.html to remove the administrator folder
 * jellyfin/jellyfin-web#950 [@MrTimscampi] Fix CI on PRs
 * jellyfin/jellyfin-web#949 [@MrTimscampi] Improve details page informations and selects
 * jellyfin/jellyfin-web#948 [@MrTimscampi] Fix artist details ribbon
 * jellyfin/jellyfin-web#943 [@dependabot[bot]] Bump acorn from 6.2.1 to 6.4.1
 * jellyfin/jellyfin-web#939 [@Artiume] Fix Dashboard OS for German
 * jellyfin/jellyfin-web#938 [@dkanada] Remove query string from source
 * jellyfin/jellyfin-web#937 [@dmitrylyzo] Fix radio style
 * jellyfin/jellyfin-web#936 [@macr] Fix "Copy Stream URL" for iOS.
 * jellyfin/jellyfin-web#932 [@MrTimscampi] Show hamburger menu on mobile and fix title padding
 * jellyfin/jellyfin-web#931 [@dmitrylyzo] Fix radiobutton and checkbox
 * jellyfin/jellyfin-web#929 [@mark-monteiro] Fix Network Settings Page
 * jellyfin/jellyfin-web#926 [@ThibaultNocchi] Fixed broken links described by #925
 * jellyfin/jellyfin-web#920 [@dmitrylyzo] Fix slideshow 2
 * jellyfin/jellyfin-web#919 [@dmitrylyzo] Fix icons doubling and WebOS support
 * jellyfin/jellyfin-web#908 [@masterkoppa] Make item detail overview expandable (Fix #888)
 * jellyfin/jellyfin-web#907 [@MrTimscampi] Improve image loading speed and sizes
 * jellyfin/jellyfin-web#904 [@dmitrylyzo] Clear player data after stop
 * jellyfin/jellyfin-web#872 [@Artiume] Update ISO playback warning
 * jellyfin/jellyfin-web#871 [@grafixeyehero] Move page.js to node
 * jellyfin/jellyfin-web#869 [@MrTimscampi] Start conversion of modules to ES6
 * jellyfin/jellyfin-web#862 [@MrTimscampi] Use Gulp to build the client
 * jellyfin/jellyfin-web#839 [@mijofa] Added extra playback keybindings
 * jellyfin/jellyfin-web#837 [@h1nk] Close dialogs when container background is right clicked
 * jellyfin/jellyfin-web#821 [@viaregio] #2407: Prefer embedded MP4-metadata for episode and season numbers
 * jellyfin/jellyfin-web#817 [@dkanada] Add basic web client configuration
 * jellyfin/jellyfin-web#780 [@MrTimscampi] Move confirm, prompt and chromecast modules definitions outside of site.js
 * jellyfin/jellyfin-web#715 [@MrTimscampi] Remove libjass

## 10.5.5 – 2020-04-26

# Jellyfin 10.5.5

Stable hotfix release for 10.5.Z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [all] Various server and UI bugfixes.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/26

### [jellyfin](https://github.com/jellyfin/jellyfin) [17]

 * #2990 [@mark-monteiro] Create Missing Data Folders
 * #2940 [@balu92] Fix missing colons
 * #2936 [@anthonylavado] Remove JsonIgnore from the DateLastSaved property of BaseItem
 * #2935 [@anthonylavado] Revert "Fix eTags DateLastSaved"
 * #2928 [@anthonylavado] Fix eTags DateLastSaved
 * #2915 [@randrey] Fix imdbid regex
 * #2910 [@randrey] Additional mime types for DLNA (VLC)
 * #2906 [@randrey] Fix InvalidOperationException while browsing via DLNA client.
 * #2903 [@randrey] Fix DLNA clients displaying wrong album art.
 * #2868 [@JustAMan] Fix passing web branch
 * #2864 [@JustAMan] Make Last-Modified and If-Modified-Since headers follow the spec
 * #2849 [@lyonzy] Handle null outputFileExtension in GetOutputFilePath
 * #2848 [@ZadenRB] Fix casing of JSON in Jellyfin API
 * #2834 [@mark-monteiro] Add nuget.config file
 * #2813 [@nyanmisaka] Switch to jellyfin-ffmpeg with integrated driver in docker build
 * #2798 [@JustAMan] Make localhost LiveTV restreams always use plain HTTP port
 * #2745 [@Artiume] Force Audio Transcoding for LiveTV Transcoding

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [11]

 * jellyfin/jellyfin-web#872 [@Artiume] Update ISO playback warning
 * jellyfin/jellyfin-web#1113 [@MrTimscampi] Add title and year to posters in TV genres view
 * jellyfin/jellyfin-web#1111 [@dmitrylyzo] Change template string to generic one to support older browsers
 * jellyfin/jellyfin-web#1109 [@YouKnowBlom] Change Chromecast player name to Google Cast
 * jellyfin/jellyfin-web#1108 [@nielsvanvelzen] Add Android icon for Android TV in devices page
 * jellyfin/jellyfin-web#1105 [@thornbill] Restore user menu on mobile
 * jellyfin/jellyfin-web#1104 [@dmitrylyzo] Fix reference to undefined variable
 * jellyfin/jellyfin-web#1095 [@JustAMan] Fix .ass subtitles not starting on mobile
 * jellyfin/jellyfin-web#1093 [@MrTimscampi] Fix some mobile navigation issues
 * jellyfin/jellyfin-web#1074 [@dmitrylyzo] Move delayed volume update to playbackManager
 * jellyfin/jellyfin-web#1022 [@ferferga] Fix mobile layout for itemdetails

## 10.5.4 – 2020-04-13

# Jellyfin 10.5.4

Stable hotfix release for 10.5.Z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [all] Various server and UI bugfixes.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/24

### [jellyfin](https://github.com/jellyfin/jellyfin) [9]

 * #2847 [@mark-monteiro] Fix compilation error in HttpListenerHost
 * #2821 [@nyanmisaka] Fix MPEG4 broken on VAAPI
 * #2796 [@JustAMan] Make codec check in profile examine profile type first
 * #2785 [@nyanmisaka] Fix MPEG4 packback error regression on vaapi
 * #2783 [@JustAMan] Add logging of URL being processed when logging an error
 * #2782 [@JustAMan] Fix support for attachments with baseURL set
 * #2779 [@KristupasSavickas] Fix ffmpeg path on ARM docker image
 * #2758 [@Bond-009] Remove PluginInstalled
 * #2721 [@PrplHaz4] Separate Channels permissions from All Libraries
 * #2715 [@nyanmisaka] Prefer to use libfdk_aac encoder for better audio quality when it is available

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [8]

 * jellyfin/jellyfin-web#963 [@MrTimscampi] Don't scale logo on details page
 * jellyfin/jellyfin-web#1072 [@ferferga] Move "hide watched media" checkbox
 * jellyfin/jellyfin-web#1070 [@redSpoutnik] Set subtitle-sync for SubtitlesOctopus
 * jellyfin/jellyfin-web#1068 [@dkanada] Pass title and filename to native shell
 * jellyfin/jellyfin-web#1049 [@JustAMan] Fix newline breaks in SRT subtitles shown in Firefox
 * jellyfin/jellyfin-web#1048 [@JustAMan] Use patched octopus that works on Cordova
 * jellyfin/jellyfin-web#1047 [@ZadenRB] Fix inconsistent value in drop down list on library page
 * jellyfin/jellyfin-web#1040 [@JustAMan] Fix native hls resume

## 10.5.3 – 2020-04-05

# Jellyfin 10.5.3

Stable hotfix release for 10.5.Z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [all] Various server and UI bugfixes.
* [various] Fix build issues (manually) that caused Master branch web to be put into 10.5.2 for some packages.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/23

### [jellyfin](https://github.com/jellyfin/jellyfin) [11]

 * #2740 [@JustAMan] Fix GetLocalApiUrl for cases with https enabled
 * #2730 [@Bond-009] Try to not crash on unsupported plugin load
 * #2723 [@jairbubbles] Update Jellyfin.SkiaSharp.NativeAssets.LinuxArm to version 1.68.1
 * #2720 [@dkanada] Fix custom musicbrainz servers
 * #2712 [@joshuaboniface] Revert #2146 ordering change
 * #2674 [@JustAMan] Make variables binding correspond with column names
 * #2668 [@mark-monteiro] Fix ApplicationHost Dispose() method
 * #2655 [@lfoust] Fix FormatException when mapping TVDB series
 * #2653 [@iwalton3] Fix embedded mkv subtitles.
 * #2559 [@whooo] Add descriptive TV episode titles for DLNA browsing
 * #2503 [@nyanmisaka] Fix various bugs in HWA subtitle burn-in

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [8]

 * jellyfin/jellyfin-web#970 [@MrTimscampi] Clean up the menus on mobile
 * jellyfin/jellyfin-web#937 [@dmitrylyzo] Fix radio style
 * jellyfin/jellyfin-web#1028 [@ZadenRB] Fixed alignment of subsections on item details page
 * jellyfin/jellyfin-web#1020 [@JustAMan] Fix attachment delivery urls
 * jellyfin/jellyfin-web#1018 [@MrTimscampi] Backport changes to Octopus
 * jellyfin/jellyfin-web#1005 [@JustAMan] Switch to new version of JavascriptSubtitlesOctopus, enable new options
 * jellyfin/jellyfin-web#1003 [@MrTimscampi] Fix admin drawer logo showing up everywhere
 * jellyfin/jellyfin-web#1000 [@Nazar78] Support H264 Level 52 (Tizen 5.0)

## 10.5.2 – 2020-03-22

# Jellyfin 10.5.2

Stable hotfix release for 10.5.Z release branch.

NOTE: As [10.5.1](https://github.com/jellyfin/jellyfin/releases/tag/v10.5.1) was never technically released, includes all updates and release notes from there as well.

## New Features and Major Improvements

N/A

## Release Notes

* [all] Various server and UI bugfixes.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/22

### [jellyfin](https://github.com/jellyfin/jellyfin) [4]

 * #2642 [@mark-monteiro] Add missing null check when retrieving extras
 * #2622 [@Artiume] Fix Release 10.5.z
 * #2617 [@Shawmon] add wasm mimetype
 * #2478 [@JustAMan] Fix ordering of search results

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [9]

 * jellyfin/jellyfin-web#969 [@dmitrylyzo] Fix XviD playback on Tizen
 * jellyfin/jellyfin-web#958 [@MrTimscampi] Show missing indicator in ListView
 * jellyfin/jellyfin-web#955 [@thornbill] Fix schedules direct buttons being hidden by default
 * jellyfin/jellyfin-web#951 [@dtparr] Correct the url in the wizardstart.html to remove the administrator folder
 * jellyfin/jellyfin-web#932 [@MrTimscampi] Show hamburger menu on mobile and fix title padding
 * jellyfin/jellyfin-web#931 [@dmitrylyzo] Fix radiobutton and checkbox
 * jellyfin/jellyfin-web#919 [@dmitrylyzo] Fix icons doubling and WebOS support
 * jellyfin/jellyfin-web#907 [@MrTimscampi] Improve image loading speed and sizes
 * jellyfin/jellyfin-web#904 [@dmitrylyzo] Clear player data after stop

## 10.5.1 – 2020-03-16

# Jellyfin 10.5.1

NOTICE: THIS RELEASE HAS BEEN PULLED.

> We've had to pull 10.5.1 due to some unfixable build failures. Only Debian and Ubuntu package users would be affected. If you happened to upgrade to 10.5.1 on these platforms, it should work, but we've removed the offending version from the repos. A 10.5.2 will arrive in a week or two.

Stable hotfix release for 10.5.Z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [all] General UI improvements and bugfixes.
* [all] Fixes issues with subtitle burning and rendering.
* [CentOS/Fedora] Fix CentOS and Fedora builds (hopefully).

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/21

### [jellyfin](https://github.com/jellyfin/jellyfin) [3]

 * #2607 [@joshuaboniface] Correct BuildRequires and NodeJS for Fedora/CentOS
 * #2582 [@Bond-009] Fix subtitles
 * #2541 [@joshuaboniface] Fix curl for Jellyfin GPG key

### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [6]

 * jellyfin/jellyfin-web#948 [@MrTimscampi] Fix artist details ribbon
 * jellyfin/jellyfin-web#943 [@dependabot[bot]] Bump acorn from 6.2.1 to 6.4.1
 * jellyfin/jellyfin-web#936 [@macr] Fix "Copy Stream URL" for iOS.
 * jellyfin/jellyfin-web#929 [@mark-monteiro] Fix Network Settings Page
 * jellyfin/jellyfin-web#926 [@ThibaultNocchi] Fixed broken links described by #925
 * jellyfin/jellyfin-web#920 [@dmitrylyzo] Fix slideshow 2

## 10.5.0 – 2020-03-08

# Jellyfin 10.5.0

After a lot of work over several months, we're pleased to offer Jellyfin 10.5.0.

## New Features and Major Improvements

* Moved from .NET Core 2.2 to 3.1 for improved performance and backend features
* Major performance and responsiveness improvements to both the web client and the server
* New design for the item details view in the web client
* New animations in the web client
* Improve compatibility with legacy browsers in the web client
* Improved SSA/ASS subtitles support in the web client
* Added keyboard navigation to the TV layout in the web client
* Added full hardware-acceleration encoding and decoding support for Raspberry Pi
* Added support for embedded attachments in media files [#1838]
* Fixed Play To order for playlists

## Important Release Notes

* [ALL] A migration will be automatically applied to logging.json to change some default options to reduce log spam. Users should continue to modify their logging configuration in `logging.json` if desired, while the defaults will be held in `logging.default.json`; the default file should NOT be modified, as it may be overwritten again at a later date.
* [ALL] ASS subtitle support only works properly with subtitles that are not heavily animated. If you are seeing lag when rendering ASS subtitless, you should burn them in by changing User Settings -> Subtitles -> Burn Subtitles -> All complex formats. Note that this will increase CPU usage.
* [CentOS] Due (yet again) to random build failures, there will not be a 10.5.0 release for CentOS. Once the bugs are fixed, it will be released for 10.5.1. Fedora (31) is OK.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/20

### [jellyfin](https://github.com/jellyfin/jellyfin) [186]                                                                                                                                                                                     
                                                                                                               
 * #2536 [@dkanada] Migrate AudioDB to use plugin interface                                  
 * #2535 [@mark-monteiro] Create Logging Configuration Heirarchy                                
 * #2534 [@joshuaboniface] Set EnableHttps disabled by default                                                                                                                                                                               
 * #2532 [@MrTimscampi] Add baseURL to attachments API url                                                    
 * #2524 [@ferferga] Replaces NSIS uninstaller icon so it's more visible                                  
 * #2523 [@JustAMan] Improve migrations so they are more maintainable                          
 * #2515 [@JustAMan] Implement ability to run migration routines when updating Jellyfin        
 * #2513 [@Bond-009] Improve alpha numeric sorting                                             
 * #2512 [@Artiume] Update Fedora build container version                                
 * #2508 [@joshuaboniface] Update contributors list                                            
 * #2501 [@JustAMan] Default transcoding throttling to false for new installs                                                                                                                                                                 
 * #2500 [@mark-monteiro] Register Logging Services Correctly                                
 * #2491 [@mark-monteiro] Fix Playlist Deletion                                                             
 * #2483 [@xosdy] Fix download file with non-ASCII filename                                     
 * #2476 [@JustAMan] Bring back sorting when needed to fix PlayTo                            
 * #2474 [@JustAMan] Simplify AlphanumericComparer, reduce code duplication                                    
 * #2472 [@Narfinger] moves shows tests to Theory and InlineData format                        
 * #2448 [@Narfinger] adds names from the episodenumber tests to path tests                                    
 * #2444 [@Narfinger] converted tests to inlinedata                 
 * #2442 [@Bond-009] Switch remux and direct stream                                
 * #2436 [@dkanada] Add config options for MusicBrainz                             
 * #2434 [@Bond-009] Fix photo serialization                                 
 * #2429 [@Bond-009] Fix episode parsing                                                     
 * #2427 [@Bond-009] Minor improvements                                                                       
 * #2421 [@viaregio] #2407: Prefer episode and season numbers from the embedded MP4-metadata           
 * #2405 [@nvllsvm] Fix arm32 built on amd64 host                                      
 * #2400 [@Bond-009] Another baseurl related fix                          
 * #2398 [@Artiume] Update dockerfile to install git for new dependency
 * #2394 [@mark-monteiro] Add Some XML Documentation              
 * #2393 [@DMouse10462] Fix Fedora build                        
 * #2384 [@Bond-009] Fix some warnings in Emby.Server.Implementations
 * #2382 [@dkanada] Refactor some API services                   
 * #2381 [@sebPomme] Fix quick start guide url in readme                                  
 * #2379 [@joshuaboniface] Use NodeJS 10.X for NPM builds       
 * #2374 [@Bond-009] Fix some warnings in MediaBrowser.Controller   
 * #2373 [@Bond-009] Fix some warnings in MediaBrowser.Model           
 * #2368 [@nyanmisaka] Fix framerate info not showing when mediasource is in H264 format.
 * #2367 [@Artiume] fix SSL issue in arm and arm64                            
 * #2365 [@mcarlton00] Add root certificates to docker image                               
 * #2363 [@dkanada] Add session view endpoint                             
 * #2362 [@dkanada] Improve scan progress and fix a few bugs            
 * #2359 [@Bond-009] Allow changing capitalization of usernames    
 * #2358 [@Bond-009] Enable TreatWarningsAsErrors and Nullable for test projects
 * #2357 [@Bond-009] Fix warnings                               
 * #2349 [@Bond-009] Update deps                                
 * #2347 [@Matt07211] Fix broken webserver caused by dotnet publish. Temp Fix for #2255
 * #2343 [@Bond-009] Fix spacing logs                                                         
 * #2338 [@ferferga] Removed old 'automatic restart after update' features        
 * #2337 [@ThreeFive-O] Add transcoding framerate info                    
 * #2332 [@pR0Ps] Fix another issue with DLNA responses not properly paginating
 * #2331 [@nyanmisaka] fix an issue that could not correctly determine 'IsSecondaryAudio' in some cases.
 * #2326 [@Bond-009] Improvements to dlna server           
 * #2325 [@Bond-009] Clean up Emby.Naming                                                                      
 * #2321 [@Bond-009] Simplify image processing by removing image enhancers                   
 * #2304 [@pR0Ps] Fix pagination for DLNA root folder list                                      
 * #2299 [@dkanada] Fix a few more tests for music and episodes                                                                                                                                                                              
 * #2297 [@Bond-009] Kestrel doesn't like sync IO operations                                                  
 * #2295 [@shemanaev] Enable path mapping in `PlaybackInfo` endpoint                                      
 * #2291 [@Bond-009] Fix warnings in SessionManager                                            
 * #2290 [@anthonylavado] Update SQLitePCL to new version                                      
 * #2289 [@Bond-009] Add back support for DVDs copied as folders                               
 * #2288 [@Bond-009] Add brackets around thread id                                       
 * #2287 [@nyanmisaka] New upstream ffmpeg version 4.2.1 for windows nightly channel           
 * #2283 [@EraYaN] Change NSIS log verbosity and use lesser but faster compression.                                                                                                                                                           
 * #2275 [@Artiume] Explicitly ask for ffmpeg logs                                           
 * #2272 [@Bond-009] Add thread ID and source to logging                                                    
 * #2269 [@EraYaN] Split CI YAML files and update code coverage collection                      
 * #2268 [@dkanada] Fix tests for absolute paths                                             
 * #2266 [@Bond-009] Try to fix nullreff                                                                       
 * #2264 [@Bond-009] Clean up server discovery code                                            
 * #2258 [@geilername] Enable Throttling when transcoding without Hardware-Acceleration                        
 * #2257 [@Bond-009] Fix a couple of tests                          
 * #2254 [@Bond-009] Fix regex for movies released after 2019                      
 * #2251 [@nyanmisaka] add support for AMD AMF hardware encoding on Windows & Linux
 * #2249 [@Narfinger] fixes dockerfile building on recent linux installations
 * #2248 [@EraYaN] Fix the VSTest runner                                                     
 * #2247 [@Bond-009] Remove StringHelper functions                                                            
 * #2245 [@BnMcG] Add a test to prevent a regression of absolute path generation behaviour             
 * #2242 [@Bond-009] Remove FileSystem.GetStream                                       
 * #2240 [@anthonylavado] Re-order the path statement to avoid file issues
 * #2230 [@dkanada] Fix dependency issue for CI                        
 * #2222 [@sachk] Update the build script to use .NET core SDK 3.1
 * #2221 [@Bond-009] Fix baseurl (again)                        
 * #2220 [@Bond-009] Replace unicode char with its integer value     
 * #2219 [@Bond-009] Fix JSON subtitle writer                    
 * #2216 [@gnattu] Let HLS fallback to mpegts in case device reports unsupported container
 * #2208 [@Bond-009] Fix a couple of TODOs                      
 * #2206 [@Bond-009] Delete user config dir on user deletion        
 * #2185 [@Bond-009] Fix exceptions while scanning                     
 * #2184 [@WiiPlayer2] Remove explicit configuration of "global_header" flag             
 * #2181 [@BnMcG] Test Jellyfin.Api authentication handling                   
 * #2176 [@Bond-009] Enable nullable reference types for Emby.Photos and Emby.Notifications
 * #2170 [@Bond-009] Minor changes to MediaInfoService                    
 * #2165 [@Ullmie02] Add Tmdb as a Provider for Season Images           
 * #2160 [@Artiume] Force Transcoding LiveTV                       
 * #2155 [@mark-monteiro] Jellyfin.Drawing.Skia Warnings and Analyzers          
 * #2153 [@dkanada] Fix playlist deletion and a few warning fixes
 * #2152 [@dkanada] Track progress for any item that supports the feature
 * #2150 [@Bond-009] Enable TreatWarningsAsErrors for some projects                    
 * #2146 [@cromefire] Fix invalid username handling                                           
 * #2144 [@neilsb] Add Excluded Tags to SQLite query using parameters             
 * #2142 [@Bond-009] Add improved error message for #2141                 
 * #2138 [@mark-monteiro] Fix Tvdb Provider Episode Search                     
 * #2136 [@Bond-009] More warnings (removed)                                                            
 * #2134 [@Bond-009] Fix comparison between different types
 * #2133 [@Bond-009] Fix typo                                                                                  
 * #2118 [@chaosinnovator] Add StartIndex result to /Items API query                         
 * #2109 [@Bond-009] Fix plugin installation and correct api behaviour                          
 * #2107 [@Bond-009] Move to .Net Core 3.1                                                                                                                                                                                                   
 * #2106 [@Bond-009] Fix ubuntu x64 docker build                                                              
 * #2105 [@Bond-009] Add back all old emby tests                                                          
 * #2104 [@cvium] Simplify regex to avoid catastrophic backtracking                            
 * #2102 [@Bond-009] Add installed plugins to bug reports                                      
 * #2099 [@cryptobank] Fix VAAPI encoding on 10-bit hevc. Update QSV encoding and scaling to...
 * #2098 [@Bond-009] Fix GetTranscodePath function and cache path update logline         
 * #2097 [@Bond-009] Remove unused fields and properties                                       
 * #2096 [@Bond-009] Clean up Emby.Server.Implementations/LiveTv/EmbyTV/EmbyTV.cs                                                                                                                                                             
 * #2089 [@escabe] Fix #2088                                                                 
 * #2082 [@excelite] added required nuget package to enable serilog based centralized logging in gelf format
 * #2073 [@Bond-009] Minor improvements to network code                                         
 * #2071 [@excelite] add filesize limit for logfiles and a maximum logfile count             
 * #2062 [@Bond-009] Use .Net Core 3.0 in all docker images                                                    
 * #2058 [@ferferga] Add full Raspberry Pi hardware accelerated decoding support               
 * #2055 [@Bond-009] Fix master build                                                                          
 * #2054 [@Bond-009] dlna GetPathValue                              
 * #2052 [@EraYaN] Add tag building support to Windows Web build.                  
 * #2050 [@Bond-009] Fix possible nullref when updating packages                   
 * #2049 [@dkanada] Update readme                                            
 * #2045 [@Bond-009] Fix baseurl issues part 2                                               
 * #2041 [@Bond-009] Fix more warnings                                                                        
 * #2040 [@Bond-009] Validate https certificates                                                       
 * #2039 [@Bond-009] Fix always false condition                                        
 * #2034 [@Bond-009] Fix easy password                                    
 * #2020 [@Bond-009] Add support for multi segment base urls           
 * #2019 [@Bond-009] Remove leading / from baseurl                
 * #2016 [@joshuaboniface] Update stalebot timings and message  
 * #2008 [@Bond-009] Fix GetPathValue function                       
 * #1992 [@Bond-009] Fix naming tests                            
 * #1991 [@Bond-009] Don't append transcodes to transcoding temp path                     
 * #1977 [@Bond-009] Update deps                                
 * #1973 [@EraYaN] Fix the last of the docs warnings                
 * #1970 [@Bond-009]  Use Mono.Nat Nuget package                       
 * #1969 [@anthonylavado] Add an exemption for the confirmed label                       
 * #1968 [@Bond-009] Disable CA1720: Identifiers should not contain type names
 * #1967 [@Bond-009] Fix some warnings                                                     
 * #1965 [@Bond-009] Deserialize with the correct type (and warning fixes)
 * #1954 [@LogicalPhallacy] Use mirror for NSSM                         
 * #1949 [@stevehayles] Update to Dockerfile                       
 * #1942 [@Bond-009] Enable nullable reference types for Jellyfin.Server        
 * #1941 [@Bond-009] Make probesize and analyzeduration configurable and simplify circular dependencies
 * #1937 [@justinfenn] use exec form for Dockerfile entrypoint           
 * #1934 [@dkanada] Minor changes to transcode cleanup scheduled task                  
 * #1933 [@cvium] Reload logging.json on changes                                              
 * #1931 [@grafixeyehero] update persons service                                  
 * #1930 [@grafixeyehero] update vsc workspace launch for net core 3      
 * #1929 [@Narfinger] Fix parsing of certain names and adds a default season if no season was found
 * #1926 [@Bond-009] Add clearer exceptions, warnings and docs                                          
 * #1925 [@joshuaboniface] Integrate web build into Debuntu package build steps
 * #1923 [@Bond-009] Don't shuffle some types by default                                                       
 * #1922 [@Bond-009] Use the correct dotnet runtime in Docker images                         
 * #1918 [@nvllsvm] Docker fixes                                                                
 * #1915 [@Bond-009] Rewrite hex encoder/decoder                                                                                                                                                                                             
 * #1909 [@KerryRJ] Fix System.NullReferenceException when playing Dvds copied to HDD                         
 * #1904 [@JustAMan] Switch ffmpeg to hls muxer (from segment) to fix premature stop on non-patched ffmpeg
 * #1903 [@anthonylavado] Update NSIS Installer                                                
 * #1898 [@Bond-009] Fix Json serialization error                                              
 * #1891 [@stanionascu] Upgrade BDInfo plugin to UHD/Atmos/DTS:X support                       
 * #1887 [@joshuaboniface] Bump version to 10.5.0 for next stable release                
 * #1884 [@Bond-009] Move to netcore3.0                                                        
 * #1872 [@thornbill] Update translate badge in README                                                                                                                                                                                        
 * #1871 [@Bond-009] Enable `TreatWarningsAsErrors` for MediaBrowser.Common and Emby.Photos  
 * #1870 [@JustAMan] Fix exception when handling error, log errors better                                   
 * #1866 [@Bond-009] Change slow query time logging to debug                                    
 * #1864 [@Bond-009] Improve IInstallationManager interface                                  
 * #1863 [@joshuaboniface] Fix inconsistent BaseUrl behavior                                                   
 * #1862 [@joshuaboniface] Fix bump_version for submodule removal                              
 * #1861 [@joshuaboniface] Use NVM to install nodejs v8 and yarn for CentOS                                    
 * #1859 [@joshuaboniface] Fix COPR build and Fedora packaging      
 * #1855 [@Bond-009] Minor style fixes                                             
 * #1854 [@Bond-009] Use System.Text.Json api for databases                        
 * #1853 [@Bond-009] Log startup time                                        
 * #1852 [@Bond-009] Fix some more warnings                                                  
 * #1840 [@Bond-009] Ignore warning CA1308 and SA1108                                                         
 * #1838 [@Unhelpful] Add support for embedded attachments in media files                              
 * #1789 [@Bond-009] Update deps and add MultiThreading analyzer                       
 * #1503 [@cvium] Move StartupWizard to ASP.NET Web Api                   
                                                                       
### [jellyfin-web](https://github.com/jellyfin/jellyfin-web) [167]
                                                                
 * jellyfin/jellyfin-web#877 [@JustAMan] Stop checkbox showing a checkmark when unchecked 
 * jellyfin/jellyfin-web#875 [@JustAMan] Make card buttons be positioned properly     
 * jellyfin/jellyfin-web#874 [@MrTimscampi] Use forked version of JavascriptSubtitlesOctopus                   
 * jellyfin/jellyfin-web#866 [@sorinyo2004] Fix hover buttons layout on portraitCard 
 * jellyfin/jellyfin-web#860 [@thornbill] Fix browsers that do not support Promises      
 * jellyfin/jellyfin-web#856 [@thornbill] Add eslint:recommended to eslint config           
 * jellyfin/jellyfin-web#854 [@dmitrylyzo] Fix variable reference                                             
 * jellyfin/jellyfin-web#849 [@dkanada] Catch some errors and remove unused method                 
 * jellyfin/jellyfin-web#846 [@dmitrylyzo] Fix slideshow                                                        
 * jellyfin/jellyfin-web#845 [@thornbill] Remove es6 env until babel is added                  
 * jellyfin/jellyfin-web#844 [@thornbill] Fix horizontal scrolling on emby-scrollers         
 * jellyfin/jellyfin-web#843 [@grafixeyehero] Webos icon fix                            
 * jellyfin/jellyfin-web#838 [@h1nk] Add missing final newlines                                      
 * jellyfin/jellyfin-web#834 [@YouKnowBlom] Fix webOS support in videoosd.js and homesection.js                             
 * jellyfin/jellyfin-web#831 [@nyanmisaka] Mark h264 high10 as unsupported on mobile browsers 
 * jellyfin/jellyfin-web#828 [@Nickbert7] Fix dashboard padding                                             
 * jellyfin/jellyfin-web#819 [@dmitrylyzo] Disable scrollManager on emby-scroller in "native mode"                 
 * jellyfin/jellyfin-web#818 [@dmitrylyzo] Fix cropping of scaled card (TV layout)                     
 * jellyfin/jellyfin-web#816 [@MrTimscampi] Make the console quieter by default                
 * jellyfin/jellyfin-web#814 [@MrTimscampi] Fix icons on WebOS 4                                                        
 * jellyfin/jellyfin-web#813 [@MrTimscampi] Add more icon types                                                              
 * jellyfin/jellyfin-web#812 [@dmitrylyzo] Enhance volume slider
 * jellyfin/jellyfin-web#811 [@grafixeyehero] Fix nowplaying  for tv mode                                                           
 * jellyfin/jellyfin-web#797 [@dkanada] Fix some minor style issues                                               
 * jellyfin/jellyfin-web#788 [@nyanmisaka] Fix detail page title on mobile layout                                    
 * jellyfin/jellyfin-web#787 [@YouKnowBlom] Add delay on play/pause to prevent hiccup when entering/exiting fullscreen                                                                                                                                            
 * jellyfin/jellyfin-web#786 [@dmitrylyzo] Fix slider positioning on click and (try to) make it look the same in different browsers
 * jellyfin/jellyfin-web#785 [@MrTimscampi] Update Rotten Tomatoes icons                                                       
 * jellyfin/jellyfin-web#784 [@nyanmisaka] Fix device icons for Safari and Android browsers                         
 * jellyfin/jellyfin-web#783 [@MrTimscampi] Update dependencies                                                     
 * jellyfin/jellyfin-web#781 [@MrTimscampi] Tweak poster size on home screen                                        
 * jellyfin/jellyfin-web#779 [@MrTimscampi] Fix action icons in lists wrapping to multiple lines              
 * jellyfin/jellyfin-web#778 [@MrTimscampi] Force ratings to 1 decimal place                                        
 * jellyfin/jellyfin-web#775 [@joshuaboniface] Alter hardware acceleration message                                                                                                                                                                                 
 * jellyfin/jellyfin-web#773 [@dkanada] Minor theme changes and tweak session cards on dashboard                  
 * jellyfin/jellyfin-web#772 [@dmitrylyzo] Fix logoscreensaver image path                                                        
 * jellyfin/jellyfin-web#770 [@dmitrylyzo] Disable keyboard navigation for non-TV                                    
 * jellyfin/jellyfin-web#769 [@dannymichel] Fix detail page                                                       
 * jellyfin/jellyfin-web#767 [@nyanmisaka] Fix encoder preset option not working                                                    
 * jellyfin/jellyfin-web#764 [@thornbill] Fix device images on main dashboard page                                  
 * jellyfin/jellyfin-web#763 [@thornbill] Fix custom css precedence                                                                 
 * jellyfin/jellyfin-web#762 [@MrTimscampi] Adjust details page ribbon margins and colors
 * jellyfin/jellyfin-web#760 [@nyanmisaka] Add some translations for playback info                      
 * jellyfin/jellyfin-web#759 [@dannymichel] Fix logo page margin                                        
 * jellyfin/jellyfin-web#758 [@dannymichel] Fix padding in header                                 
 * jellyfin/jellyfin-web#755 [@dmitrylyzo] Add server select support for NativeShell                              
 * jellyfin/jellyfin-web#754 [@ThibaultNocchi] Clipboard API & fallback method to copy stream URL                                  
 * jellyfin/jellyfin-web#751 [@ThibaultNocchi] Checks if stream URL is successfully copied and displays an appropriate toast
 * jellyfin/jellyfin-web#747 [@MrTimscampi] Add placeholder image to detail pages and more placeholder icons
 * jellyfin/jellyfin-web#746 [@ferferga] Load gamepadtokey.js only when is necessary           
 * jellyfin/jellyfin-web#744 [@grafixeyehero] Fix usersettings for PR #726                  
 * jellyfin/jellyfin-web#740 [@MrTimscampi] Enable imageLoader fade-in effect          
 * jellyfin/jellyfin-web#739 [@thornbill] Add title attributes to card title buttons 
 * jellyfin/jellyfin-web#738 [@ferferga] Switched OS media controls                       
 * jellyfin/jellyfin-web#737 [@MrTimscampi] Miscellaneous CSS fixes                   
 * jellyfin/jellyfin-web#736 [@ferferga] Remove "Automatically update this server" checkbox                    
 * jellyfin/jellyfin-web#735 [@ferferga] Change font family                          
 * jellyfin/jellyfin-web#734 [@dmitrylyzo] Fix compatibility for older browsers (webOS 3)
 * jellyfin/jellyfin-web#730 [@ManfredRichthofen] Remove red login border on firefox        
 * jellyfin/jellyfin-web#728 [@dlahoti] sort items to play in the correct order when sending to Chromecast    
 * jellyfin/jellyfin-web#726 [@dkanada] Remove useless autoplay script and add folder for settings 
 * jellyfin/jellyfin-web#725 [@dkanada] Fix some missing resource issues                                        
 * jellyfin/jellyfin-web#724 [@nyanmisaka] Update and fix some canPlayType                     
 * jellyfin/jellyfin-web#722 [@grafixeyehero] Deminify part 4                                
 * jellyfin/jellyfin-web#721 [@grafixeyehero] Fix alphaPicker padding                   
 * jellyfin/jellyfin-web#720 [@dmitrylyzo] Add app exit on "Go back"                                 
 * jellyfin/jellyfin-web#719 [@samuel9554] Add titles in movie tabs genres moviegenres.js                                   
 * jellyfin/jellyfin-web#716 [@Bond-009] Safari supports AC-3                                 
 * jellyfin/jellyfin-web#714 [@MrTimscampi] Use dist versions in bundle.js                                  
 * jellyfin/jellyfin-web#713 [@dkanada] Add a folder for useful scripts                                            
 * jellyfin/jellyfin-web#712 [@dkanada] Move all documentation links to subdomain                      
 * jellyfin/jellyfin-web#711 [@dkanada] Fix xmltv strings and remove broken tv guide sources   
 * jellyfin/jellyfin-web#710 [@dkanada] Fix some issues with theme resources                                            
 * jellyfin/jellyfin-web#709 [@MrTimscampi] Add CSS linting and enforce style                                                
 * jellyfin/jellyfin-web#708 [@MrTimscampi] Move material icons to external package
 * jellyfin/jellyfin-web#704 [@grafixeyehero] Fix scroll for movie recommendation                                                   
 * jellyfin/jellyfin-web#702 [@dmitrylyzo] Add playback control from TV remote                                    
 * jellyfin/jellyfin-web#701 [@dmitrylyzo] Fix filter dialog size for TV                                             
 * jellyfin/jellyfin-web#699 [@dmitrylyzo] Fix headerLeft justify-content (WebOS 3/4, Tizen 4)                                                                                                                                                                    
 * jellyfin/jellyfin-web#698 [@twinkybot] Help Link in the admin area for Users points to 404 on github                            
 * jellyfin/jellyfin-web#694 [@grafixeyehero] Item detail page layout improvements continued form #611                         
 * jellyfin/jellyfin-web#688 [@grafixeyehero] Fix respect user option backdrop image                                
 * jellyfin/jellyfin-web#683 [@dkanada] Minor playback improvements and a few icon and string fixes                 
 * jellyfin/jellyfin-web#680 [@MrTimscampi] Use scrollManager for TV layout in all browser and improve scroll feel  
 * jellyfin/jellyfin-web#676 [@MrTimscampi] Revert vendor prefix removal                                      
 * jellyfin/jellyfin-web#673 [@dkanada] Add android icon and fix issue with kodi icon                               
 * jellyfin/jellyfin-web#672 [@MrTimscampi] Hide Cast button on TV layout                                                                                                                                                                                          
 * jellyfin/jellyfin-web#670 [@dkanada] Fix issue with previous merge commit                                      
 * jellyfin/jellyfin-web#667 [@Nickbert7] Update remotecontrol layout                                                            
 * jellyfin/jellyfin-web#664 [@WX9yMOXWId] Properly load modules before loading view                                 
 * jellyfin/jellyfin-web#663 [@MrTimscampi] Enable headroom only on mobile                                        
 * jellyfin/jellyfin-web#660 [@Larvitar]  Display year in "Collection" and "More like this"                                         
 * jellyfin/jellyfin-web#655 [@MrTimscampi] Remove vendor prefixes in CSS                                           
 * jellyfin/jellyfin-web#654 [@MrTimscampi] Add autoprefix to postcss                                                               
 * jellyfin/jellyfin-web#651 [@Larvitar] Fix for commit d111e8c                          
 * jellyfin/jellyfin-web#650 [@MrTimscampi] Align the page title with other text and icons in the header
 * jellyfin/jellyfin-web#649 [@XVicarious] Allow WEBP Uploading                                         
 * jellyfin/jellyfin-web#645 [@mcarlton00] Rework device icons + add Kodi icon                    
 * jellyfin/jellyfin-web#641 [@Larvitar] If item EndYear is the same as ProductionYear only display ProductionYear
 * jellyfin/jellyfin-web#640 [@YouKnowBlom] Add a warning to user wizard reflecting the importance of usernames                    
 * jellyfin/jellyfin-web#639 [@dmitrylyzo] Fix require of 'export default'                                                  
 * jellyfin/jellyfin-web#635 [@dkanada] Some general refactoring for assets                                 
 * jellyfin/jellyfin-web#634 [@dkanada] Move more controllers to a sane directory structure    
 * jellyfin/jellyfin-web#633 [@Artiume] Correct URL Link, discuss new networking page       
 * jellyfin/jellyfin-web#631 [@Artiume] Fix User Link                                  
 * jellyfin/jellyfin-web#630 [@Artiume] Fixed Jellyfin Link                          
 * jellyfin/jellyfin-web#628 [@Artiume] Fix DLNA Link                                     
 * jellyfin/jellyfin-web#627 [@s0urcelab] add missing string and translation          
 * jellyfin/jellyfin-web#626 [@dkanada] Fix context menu margin and user preference buttons                    
 * jellyfin/jellyfin-web#624 [@redSpoutnik] Fix subtitle sync firefox                
 * jellyfin/jellyfin-web#619 [@DaveChild] Fix for card image scaling problem             
 * jellyfin/jellyfin-web#618 [@Wunax] Fix a bug that hides children elements in the videoosd
 * jellyfin/jellyfin-web#617 [@dmitrylyzo] Fix variable definition place                                      
 * jellyfin/jellyfin-web#615 [@AndreCarvalho] Add option to randomly sort music albums             
 * jellyfin/jellyfin-web#613 [@redSpoutnik] reset subtitle offset on next episode play                          
 * jellyfin/jellyfin-web#612 [@grafixeyehero] Fix Scroll arrows missing when searching         
 * jellyfin/jellyfin-web#611 [@grafixeyehero] Item detail page layout improvements           
 * jellyfin/jellyfin-web#610 [@YouKnowBlom] Fix existing library folder path returning undefined
 * jellyfin/jellyfin-web#605 [@ringmatter] Add support for local webpack devserver development       
 * jellyfin/jellyfin-web#604 [@grafixeyehero] Fix collection padding in TV layout                                           
 * jellyfin/jellyfin-web#601 [@grafixeyehero] Fix webcomponents-lite bundling                 
 * jellyfin/jellyfin-web#600 [@Wunax] Fix can't connect to server if enableAutoLogin is false               
 * jellyfin/jellyfin-web#597 [@dkanada] Minor changes to improve Firefox support                                   
 * jellyfin/jellyfin-web#596 [@Wunax] Fix input field user avatar in a wrong position                  
 * jellyfin/jellyfin-web#594 [@grafixeyehero] Fix some issues with the backdrop image          
 * jellyfin/jellyfin-web#593 [@dkanada] Update readme                                                                   
 * jellyfin/jellyfin-web#592 [@grafixeyehero] Add Screen saver                                                               
 * jellyfin/jellyfin-web#584 [@Nickbert7] Enable remote control navigation
 * jellyfin/jellyfin-web#583 [@Wunax] Fixed set aspect ratio option in the player                                 
 * jellyfin/jellyfin-web#582 [@grafixeyehero] Replacing all Unicode icon                                                         
 * jellyfin/jellyfin-web#580 [@grafixeyehero] Update apphost appVersion to 10.5.0                                    
 * jellyfin/jellyfin-web#578 [@ryan-hartzell] Add autocomplete attributes to login fields                         
 * jellyfin/jellyfin-web#577 [@dmitrylyzo] Fix iOS platform detection #572                                                          
 * jellyfin/jellyfin-web#576 [@anthonylavado] Remove the leading /web/ from the manifest to avoid PWA titles        
 * jellyfin/jellyfin-web#573 [@dkanada] Align scroller items with heading                                                           
 * jellyfin/jellyfin-web#571 [@dkanada] Fix select server redirect and remove more dependencies
 * jellyfin/jellyfin-web#568 [@grafixeyehero] update Icon for medialibrarypage, userprofile, device, multiselect and installedplugins
 * jellyfin/jellyfin-web#567 [@anthonylavado] Add label to exclude issue from Stale                     
 * jellyfin/jellyfin-web#566 [@dmitrylyzo] Make navigation and playback control TV-friendly       
 * jellyfin/jellyfin-web#565 [@dmitrylyzo] Add appropriate focuscontainer classes to menus                        
 * jellyfin/jellyfin-web#564 [@dmitrylyzo] Fix focus of library order item after change                                            
 * jellyfin/jellyfin-web#563 [@dmitrylyzo] Add autofocus on page load                                                       
 * jellyfin/jellyfin-web#554 [@ThatNerdyPikachu] Actually make DatePlayed use a colon on ItemDetails        
 * jellyfin/jellyfin-web#551 [@dkanada] Remove dashboard icon from header                      
 * jellyfin/jellyfin-web#550 [@grafixeyehero] Fix Metadata Manager Live TV Loading..        
 * jellyfin/jellyfin-web#549 [@grafixeyehero] Move bower_components libraries from source control to npm
 * jellyfin/jellyfin-web#548 [@grafixeyehero] Add favorite people section to favorite tab
 * jellyfin/jellyfin-web#547 [@Unhelpful] Use JavascriptSubtitlesOctopus to render ASS subtitles with embedded fonts.
 * jellyfin/jellyfin-web#545 [@ferferga] Improved appearance of images and artworks - Part 3
 * jellyfin/jellyfin-web#544 [@dmitrylyzo] Add ScrollManager to control scrolling on focus                     
 * jellyfin/jellyfin-web#542 [@grafixeyehero] Improve wizard finish page redirect    
 * jellyfin/jellyfin-web#541 [@bilde2910] Update CONTRIBUTORS.md                         
 * jellyfin/jellyfin-web#540 [@grafixeyehero] Add file path to itemidentifier               
 * jellyfin/jellyfin-web#534 [@dmitrylyzo] Set "Resume" action on season item on TV                           
 * jellyfin/jellyfin-web#533 [@dmitrylyzo] Tizen: Remove tab activation by focus                   
 * jellyfin/jellyfin-web#524 [@grafixeyehero] Fix minor style on home section Live TV                           
 * jellyfin/jellyfin-web#523 [@grafixeyehero] Add icon on item context menu                    
 * jellyfin/jellyfin-web#521 [@dkanada] Fix save button in now playing controller            
 * jellyfin/jellyfin-web#520 [@grafixeyehero] Cleanup connect.emby.media                        
 * jellyfin/jellyfin-web#519 [@dhartung] Fix subtitle display from previous file in queue            
 * jellyfin/jellyfin-web#513 [@thornbill] Revert Swiper to fix initialization error                                         
 * jellyfin/jellyfin-web#511 [@grafixeyehero] Deminify part 3                                 
 * jellyfin/jellyfin-web#510 [@thornbill] Add translate badge to README                                     
 * jellyfin/jellyfin-web#507 [@redSpoutnik] Fix subtitle sync                                                      
 * jellyfin/jellyfin-web#506 [@grafixeyehero] Deminify                                                 
 * jellyfin/jellyfin-web#496 [@NathanPickard] Removed Other from TV Guide data providers       
 * jellyfin/jellyfin-web#491 [@dkanada] Bundle flvjs and shaka and move all libs to one folder

## 10.4.3 – 2019-12-06

# Jellyfin 10.4.3

Stable hotfix release for 10.4.Z release branch.

## New Features and Major Improvements

N/A

## Release Notes

* [all] General UI improvements and bugfixes.
* [all] Fixes the various scanning bugs that were seen and, based on testing, introduced in #1992 and #1929. These should be fixed by #2104.
* [all] Logging auto-rotation now cleans itself with a 100MB filesize limit as well. Should prevent logs filling up excessively especially when in DEBUG mode.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/19

### [Jellyfin](https://github.com/jellyfin/jellyfin)

 * #2104  Simplify regex to avoid catastrophic backtracking
 * #2071  Add filesize limit for logfiles and a maximum logfile count
 * #2054  Fix dlna GetPathValue

### [Jellyfin Web](https://github.com/jellyfin/jellyfin-web)

 * jellyfin/jellyfin-web#613  Reset subtitle offset on next episode play
 * jellyfin/jellyfin-web#612  Fix Scroll arrows missing when searching
 * jellyfin/jellyfin-web#610  Fix existing library folder path returning undefined
 * jellyfin/jellyfin-web#604  Fix collection padding in TV layout
 * jellyfin/jellyfin-web#596  Fix input field user avatar in a wrong position
 * jellyfin/jellyfin-web#594  Fix some issues with the backdrop image

## 10.4.2 – 2019-11-24

# Jellyfin 10.4.2

Stable hotfix release for 10.4.Z release branch.

## New Features and Major Improvements

N/A

## Important Release Notes

* [all] There are some image format improvements in jellyfin/jellyfin-web#545 that might interest some users who requested these changes.
* [all] There are further minor fixes to the Base URL to prevent some issues saving settings. There are no administrator changes required for this.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/18

### [Jellyfin](https://github.com/jellyfin/jellyfin)

 * #2045  Fix baseurl issues part 2
 * #2039  Fix always false condition
 * #2034  Fix easy password
 * #2019  Remove leading / from baseurl
 * #2008  Fix GetPathValue function
 * #1992  Fix naming tests
 * #1929  Fix parsing of certain names and adds a default season if no season was found

### [Jellyfin Web](https://github.com/jellyfin/jellyfin-web)

 * jellyfin/jellyfin-web#583  Fixed set aspect ratio option in the player
 * jellyfin/jellyfin-web#578  Add autocomplete attributes to login fields
 * jellyfin/jellyfin-web#576  Remove the leading /web/ from the manifest to avoid PWA titles
 * jellyfin/jellyfin-web#545  Improved appearance of images and artworks - Part 3

## 10.4.1 – 2019-11-03

# Jellyfin 10.4.1

Stable hotfix release for 10.4.Z release branch.

## New Features and Major Improvements

N/A

## Important Release Notes

* [all] The way the base URL was configured in 10.4.0 did not work properly, causing API-related issues including failing to save settings. This has been fixed in this release and this functionality is now implemented in the conventional way (all API endpoints and pages are now under the base URL, including redirects from the root). However, *this fix results in a change to the way Jellyfin is accessed when upgraded from 10.4.0 due to a change in the default value*. See below for a more detailed explanation and workaround/correction. We apologize for the inconvenience of this.
* [centos] CentOS packages should be available again after failing in the 10.4.0 release.
* [fedora] COPR support should be available again after failing in the 10.4.0 release.
* [windows] The NSSM installer has been tweaked further, including integrating a tray icon for Jellyfin when not running as a service. This should help users who do not wish to use a service-based install due to the limitations outlined in the 10.4.0 release notes.
* [ubuntu] Ubuntu Xenial is not compatible with Jellyfin 10.4.0 or 10.4.1 `.deb` due to SSL version incompatibilities. The recommended workarounds are: (a) backporting libssl1.1 from Bionic to Xenial, (b) using Docker, (c) upgrading to Ubuntu Bionic (or newer).

## Base URL change

The original implementation of this functionality in 10.4.0 added `/jellyfin` as the default base URL, but due to the changes in #1863, this will now be taken as an absolute base URL for the instance, which is was not before. This means that **all Jellyfin instances upgraded from 10.4.0 to 10.4.1 will now default to the path http://myserver:8096/jellyfin/** instead of the expected path http://myserver:8096/. Clients including Android and AndroidTV *require* this base URL to match with the entered URL (i.e. the `/jellyfin` component must be present in the configured URL). **The workaround to this is to remove the base URL value immediately after installing 10.4.1 if you're upgrading from 10.4.0.** Note that direct upgrades from versions previous to 10.4.0, to 10.4.1, do not require any workarounds and the new default value is populated with the empty value as expected.

Of course, you're also free to retain this new base URL if you wish - just ensure you update the connection URL in any clients you use to include it, and ensure your reverse proxy configuration handles this (our defaults from the documentation will).

We debated including this workaround as part of a post-install migration within packages, but felt that this would cause too many complications and require too much work across 10+ different packaging formats, and as such server administrators must perform this mitigation themselves if they do not wish to use the `/jellyfin` base URL. We apologize for this inconvenience. The steps to perform this are as follows (**NOTE**: You can do this *before* upgrading to 10.4.1 as well):

#### From the WebUI
1. Don't try to use Jellyfin at the new base URL; head straight to the admin dashboard. The default `/` URL should redirect you automatically to the new base URL, though note that this may cache the redirect in your browser.
1. Go to "Networking" on the left sidebar, under the "Advanced" menu heading.
1. Scroll down to "Base URL:".
1. Remove the text from this field, i.e. `/jellyfin`, and click "Save".
1. Restart the server.
1. Close any active sessions; they will no longer be valid. You may also need to clear your cache history for the site if the redirect was saved.
1. Visit Jellyfin at your original URL again.

#### From the CLI
1. Stop the Jellyfin process.
1. Find and open `system.xml` in the Jellyfin configuration directory (e.g. `/etc/jellyfin/system.xml` on Debuntu).
1. Find the entry `<BaseUrl>`.
1. Replace the entire line, i.e. `<BaseUrl>/jellyfin</BaseUrl>`, with `<BaseUrl/>`.
1. Start the Jellyfin process.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/16

### [Jellyfin](https://github.com/jellyfin/jellyfin)

 * #1954  Use mirror for NSSM
 * #1933  Reload logging.json on changes
 * #1909  Fix System.NullReferenceException when playing Dvds copied to HDD
 * #1904  Switch ffmpeg to hls muxer (from segment) to fix premature stop on non-patched ffmpeg
 * #1903  Update NSIS Installer
 * #1898  Fix Json serialization error
 * #1870  Fix exception when handling error, log errors better
 * #1866  Change slow query time logging to debug
 * #1863  Fix inconsistent BaseUrl behavior
 * #1862  Fix bump_version for submodule removal 
 * #1861  Use NVM to install nodejs v8 and yarn for CentOS
 * #1859  Fix COPR build and Fedora packaging

### [Jellyfin Web](https://github.com/jellyfin/jellyfin-web)

 * jellyfin/jellyfin-web#550  Fix Metadata Manager Live TV Loading
 * jellyfin/jellyfin-web#542  Improve wizard finish page redirect
 * jellyfin/jellyfin-web#540  Add file path to itemidentifier
 * jellyfin/jellyfin-web#524  Fix minor style on home section Live TV
 * jellyfin/jellyfin-web#523  Add icon on item context menu
 * jellyfin/jellyfin-web#521  Fix save button in now playing controller
 * jellyfin/jellyfin-web#519  Fix subtitle display from previous file in queue
 * jellyfin/jellyfin-web#513  Revert Swiper to fix initialization error
 * jellyfin/jellyfin-web#507  Fix subtitle sync

## 10.4.0 – 2019-10-07

# Jellyfin 10.4.0

After a lot of work over several months, we're pleased to offer Jellyfin 10.4.0.

## New Features and Major Improvements

 * Speed! WebUI responsiveness has been greatly improved, resulting in a much snappier experience with the WebUI.
 * Tons and tons of backend improvements to help stability and increase speed.
 * General improvements to various areas of the WebUI, including hover animations, icon improvements, scroller fixes, and other general fixes.
 * Configurable base URL functionality [Feature Request [#37](https://features.jellyfin.org/posts/37)].
 * New web layout option to help future webOS clients, including keyboard navigation support.
 * Removal of most bundled libraries from the WebUI to streamline performance.
 * Keyboard shortcut support in the video player.
 * Unhid the Activity page in the Dashboard for eventual improvement.
 * Reorganization of the Dashboard menus, including separating out most of the former "Advanced" menu.
 * Manual subtitle synchronization support [Feature Request [#178](https://features.jellyfin.org/posts/178)].
 * FFmpeg >4.0 support; jellyfin-ffmpeg upgraded to 4.2.1; warnings for unsupported versions in the logs [Feature Request [#203](https://features.jellyfin.org/posts/203)].
 * Proper installer for Windows users [Feature Request [#83](https://features.jellyfin.org/posts/83)].
 * Full hardware acceleration support for VAAPI, NVEnv/NVDec, and OMX [Feature Request [#75](https://features.jellyfin.org/posts/75)].
 * "Purple Haze" theme added as an in-built option.
 * New plugin: Bookshelf, for managing eBooks [Feature Request [#43](https://features.jellyfin.org/posts/43)].
 * New plugin: FanArt, removed from core server.

## Important Release Notes

 * [All] As always, ensure you back up your Jellyfin data and configuration directories, with Jellyfin stopped, before upgrading. This is very important in case you want to roll back to a previous stable release.
 * [All] Some plugins have updated versions to work with 10.4.0; if any installed plugins are missing after upgrading, re-install them from the catalog.
 * [All] FanArt support has been moved to a plugin.
 * [Kodi Integration] Due to recent updates, if syncing fails, you may need to kick off a manual full sync, after which normal syncs will work again.
 * [Windows] For 10.4.0, the default Windows data directory has moved from `%AppDataLocal%\Jellyfin` to `%ProgramData%\Jellyfin\Server`. Move/copy your data to this new location before upgrading.
 * [Windows] Ensure you remove any previously-installed `zip`-based installs, or you may get duplicate Windows Service entries.
 * [Windows] Startup shortcuts are not present for non-service installs and must be created manually.
 * [Windows] Service installs require correct permissions; keep this in mind if you get permission errors accessing media or configurations.
 * [Windows] Service installs won't have access to network shares unless your computer is in an Active Directory domain by default; you must change the service login to a named account manually and provide credentials to any network shares for this to work, or do not install Jellyfin as a service.
 * [Windows] The installer also does not take care of any firewall rules for you, make sure to add the appropiate Windows Firewall rules.

## FFmpeg

Jellyfin 10.4.0 is complemented by `jellyfin-ffmpeg` 4.2.1 on the following platfoms:

 * Debian (stretch, buster; amd64, arm64, armhf)
 * Ubuntu (xenial, bionic, cosmic, dapper; amd64, arm64, armhf)
 * Docker

And by a build based on the current master (N-95234-g35a63a9127, https://github.com/FFmpeg/FFmpeg/commit/a1e5c35a6e43ef8722017b070c124e72d628c0cd) for Windows.

On these platforms, our FFmpeg includes a patch to help aleviate premature skips near the end of videos (#1694). We hope this is a stopgap until our patch is accepted upstream, or a fix found within Jellyfin.

For now, other platforms may still experience this bug as their FFmpeg is not patched.

Please ensure you upgrade `jellyfin-ffmpeg` as well as `jellyfin` for 10.4.0 for optimal performance. Older versions will however still work fine.

## Changelog

GitHub Project: https://github.com/orgs/jellyfin/projects/8

### [Jellyfin](https://github.com/jellyfin/jellyfin)

 * #1846  Switch to custom patched build for ffmpeg for the Windows installer
 * #1845  Correct missing mesa-va-drivers package
 * #1844  Fix missing image on seasons without posters
 * #1841  Update Docs to docs.jellyfin.org URL
 * #1829  Fix SchedulesDirect authentication
 * #1825  Revert "Fix premature stop when streaming"
 * #1822  Update README for new docs location
 * #1820  Properly build DLL for porable
 * #1819  Ignore exception when attempting to kill ffmpeg that has exited
 * #1818  Fix SourceBranch -> SourceBranchName in git clone for Web UI
 * #1817  Change PRAGMA mode from WAL to TRUNCATE
 * #1815  Fix tests
 * #1814  Fix ffmpeg version check for unknown versions
 * #1812  Avoid editing preferences without user interaction
 * #1811  Configure Kestrel listener to use configured IPs
 * #1809  Recursively zip Windows packages
 * #1808  Change Win32 AMF flag to d3d11va
 * #1805  Fix plugin installation
 * #1804  Add tests for EncoderValidator and add support for ffmpeg 4.2
 * #1803  Don't log revision number
 * #1802  Fix premature stop when streaming
 * #1801  Do explicit dotnet publish in Dockerfiles
 * #1798  Fix SetImage to avoid out of range exception
 * #1793  Clean up and update builds to use new jellyfin-web
 * #1791  Remove submodule and add clone and build to CI for web UI
 * #1788  Include libssl-dev dep in Ubuntu build containers
 * #1785  Add mediabrowser route back for now
 * #1777  Add escapes for path quotes in the NSIS Installer
 * #1775  Fix multiple mistakes and warnings
 * #1773  Remove WAN DDNS
 * #1772  Hide new users from public API by default
 * #1770  Remove WAN IP Detection
 * #1768  Set log level to debug for HTTP range requests
 * #1765  Add submodule update to CI build.
 * #1764  Fix publish CI YAML parse error
 * #1763  Add two manually triggered pipelines for publishing artifacts.
 * #1752  Improve Skia error handling
 * #1751  Reset invalid login counter on successfull login
 * #1746  Docker - Build jellyfin-web
 * #1744  Rewrite `ItemDataProvider` to be more robust
 * #1735  Update deps
 * #1731  Fix culture problem on Windows for segment_time_delta argument.
 * #1727  Add mesa-va-drivers to main Dockerfile for AMD VAAPI transcoding
 * #1723  Possible fix for MrMC
 * #1709  Fix crash due to missing userRootFolder data
 * #1708  Fix translate link
 * #1707  Fix default build arg
 * #1704  Fix replace multiple spaces
 * #1702  Fix more warnings
 * #1700  Restore flac mime type
 * #1699  Bump version to 10.4.0
 * #1696  Add VSTest support to CI
 * #1695  Make Docker ffmpeg version configurable
 * #1693  Update Debian build to Buster and LibSSL 1.1
 * #1692  NSIS improvements
 * #1691  Enable VAAPI decoding without hardware encoding
 * #1687  Move IsoMounter to plugin
 * #1686  More warning fixes
 * #1685  Fix invalid arg for
 * #1683  Move the transcode path and other small fixes
 * #1680  Fix q6fn dlna seek for direct play
 * #1678  Fix ArgumentOutOfRangeException in ParseTimeSeekHeader
 * #1677  Remove legacy auth code
 * #1676  Fix login
 * #1665  Fix warnings, improve performance
 * #1659  Fix segment_time_delta value for ffmpeg 4.1
 * #1656  Fix firewall-cmd: Error: INVALID_SERVICE: 'jellyfin' not among existing services
 * #1651  Fix local trailers playback
 * #1650  Upgrade SQLitePCL to v2
 * #1646  Return DB lock immediately
 * #1645  Fix UserNotFoundError
 * #1644  Fix possible hidden exceptions
 * #1643  Fix some documentation warnings for MediaBrowser.XbmcMetadata
 * #1642  Speed up BaseItem deserialization
 * #1641  Tmdb cleanup and re-add Writer and Producer
 * #1636  Add analysers to Emby.IsoMounting and enable TreatWarningsAsErrors
 * #1634  Fix build on .Net Core 2.x
 * #1633  Attempt to fix #1391
 * #1632  Improve LocalizationManager
 * #1631  Fix build for .Net Core 2.x
 * #1629  Fix tvdb guest stars with multiple roles
 * #1628  Always fetch episode id as EpisodeInfo does not contain it
 * #1625  Fix instant crash.
 * #1624  Fix possible Nullref
 * #1622  Add a task to clean up transcode cache
 * #1614  Document all public/internal members of Emby.Drawing
 * #1613  Update deps + document startup project
 * #1612  Fix warnings
 * #1608  Add link to feature request hub to readme
 * #1605  Fix Docker build
 * #1602  Update the Stale-bot config
 * #1597  Set log level to debug for HTTP range requests
 * #1593  Docker - make web version more configurable
 * #1590  Adds null check on studio/network name
 * #1588  Add base url option to server configuration
 * #1584  Check checksum for plugin downloads
 * #1583  Add Fider to README
 * #1582  Include library via NuGet instead of via source
 * #1581  Use System.Net abstractions instead of raw socket
 * #1580  Ignore Ipv6 link-local addresses
 * #1579  Fix #1388 and #1472
 * #1578  Replace custom code with Asp.Net Core code
 * #1574  Add the --azure-pipelines switch to the compat checker
 * #1573  Use a dictionary to look up mimetypes
 * #1572  Remove the issue template for feature requests.
 * #1568  Add DLNA headers if requested by the client
 * #1562  Don't copy the complete response stream
 * #1555  Add Stale app configuration starting point
 * #1541  Override the Debian installinit name
 * #1540  Fixed SMI Encoding Bug
 * #1536  Fix broken symlinks in deployment
 * #1534  Use dash or underscore on mv command
 * #1524  Remove IpAddressInfo and IpEndPointInfo classes
 * #1521  Clean up livestreaming code
 * #1519  Fix merge errors
 * #1518  Update the GitHub token to a Grant Auth token
 * #1517  Update the GitHub connection name to use the GitHub App token
 * #1516  Move VACUUM command to fix merge error
 * #1513  Fix style issues
 * #1511  Add NSIS installer build support
 * #1505  Qualified Namespace of pscredential
 * #1500  Add optional password field on user creation
 * #1499  Log IP address on failed login attempt
 * #1484  Update TVDB provider to search based on series display order
 * #1463  Update deps
 * #1462  Improvements to InstallationManager
 * #1457  Stop path substitution in SubtitleEncoder - Fix #1446
 * #1454  Simplify file serving code
 * #1453  Improve main code flow
 * #1452  Improvements to UserManager
 * #1451  Create Media Playback issue template
 * #1448  Use the username for the user config path
 * #1440  Change UsCulture to InvariantCulture
 * #1433  Add support for encoding with libx265 and hevc_nvenc
 * #1427  Move fanart image provider to plugin
 * #1397  Streamline authentication proccess
 * #1369  Enable Exynos MFC encoder and fix transcoding bitrate control
 * #1368  Only return useful drives
 * #1367  Ignore casing photo extensions
 * #1366  Fix more warnings
 * #1363  Update getting-help link in README
 * #1293  Fix query time logging
 * #1274  Prevent null reference when request content type is x-www-form-urlencoded
 * #1247  Adjust detection of 'sample' in filenames to use regex boundaries
 * #1245  Remove unused event
 * #1229  Cleaning WebSocketSharp continued
 * #1225  Fix help message to indicate the right output folder
 * #1224  Fix missing Unraid cache mount and name capitalization
 * #1218  Disable dotnet_compat part of pipeline
 * #1212  Clean `WebSocketSharpRequest.PathInfo`
 * #1211  Update Unraid Docker icon
 * #1210  Fix README documentation link
 * #1182  Speed up DeepCopy
 * #1176  Remove unused dependency for Emby.Naming
 
### [Jellyfin Web](https://github.com/jellyfin/jellyfin-web)

 * jellyfin/jellyfin-web#503  Fix some minor issues with the dashboard page
 * jellyfin/jellyfin-web#502  Update Docs to docs.jellyfin.org URL
 * jellyfin/jellyfin-web#501  Resolves missing policy error on user creation
 * jellyfin/jellyfin-web#500  Restore prepare script
 * jellyfin/jellyfin-web#498  Fix issues with scrollbutton visibility
 * jellyfin/jellyfin-web#497  Update documentation links
 * jellyfin/jellyfin-web#492  Add webpack-dev-server
 * jellyfin/jellyfin-web#490  Add jQuery to global scope
 * jellyfin/jellyfin-web#484  Revert "Allow card text to continue through line breaks"
 * jellyfin/jellyfin-web#481  Fix missing jQuery in medialibraryeditor
 * jellyfin/jellyfin-web#479  Improve the user settings interface
 * jellyfin/jellyfin-web#478  Fix video osd header styles
 * jellyfin/jellyfin-web#477  Fix mediainfo display on tv mode
 * jellyfin/jellyfin-web#474  add 700ms timer for 'mousemove' and 'touchmove' volume listeners
 * jellyfin/jellyfin-web#472  Remove WAN domain name options
 * jellyfin/jellyfin-web#470  Azure pipelines
 * jellyfin/jellyfin-web#468  Fix Duplicate loading animation
 * jellyfin/jellyfin-web#466  Fix toggle on tv layout mode
 * jellyfin/jellyfin-web#464  update apphost appVersion to 10.4.0
 * jellyfin/jellyfin-web#463  Changed to non-blocking subtitles
 * jellyfin/jellyfin-web#462  Add style for metadata sidebar Icon folder
 * jellyfin/jellyfin-web#461  Fix: Not all players support xxxSubtitleOffset
 * jellyfin/jellyfin-web#460  Added toast notification when copy-stream is executed
 * jellyfin/jellyfin-web#459  Added more details to itemdetails page
 * jellyfin/jellyfin-web#458  Refactor several files and methods
 * jellyfin/jellyfin-web#456  Require hls.js from npm
 * jellyfin/jellyfin-web#455  Allow fldSelectLoginProvider for admins
 * jellyfin/jellyfin-web#451  Improve button style when focused
 * jellyfin/jellyfin-web#450  Disable animations in editor sidebar
 * jellyfin/jellyfin-web#449  Don't hide play all and shuffle buttons on mobile
 * jellyfin/jellyfin-web#448  fix AutoRunWebApp checkbox on dashboardgeneral
 * jellyfin/jellyfin-web#446  Dashboard layout improvements
 * jellyfin/jellyfin-web#444  Minor update for media info
 * jellyfin/jellyfin-web#443  Fixed blurred My Media images
 * jellyfin/jellyfin-web#441  Improve image quality on detail page
 * jellyfin/jellyfin-web#439  Add media file size to Playback Data
 * jellyfin/jellyfin-web#436  Always have last sort of movies be by production year
 * jellyfin/jellyfin-web#435  Change primary highlight for delete confirmation dialog
 * jellyfin/jellyfin-web#434  Add string for LabelFolder
 * jellyfin/jellyfin-web#433  Quick fix Now playing bar controls
 * jellyfin/jellyfin-web#432  Add icon to metadata editor side bar
 * jellyfin/jellyfin-web#430  Fix layout issues for device cards on dashboard
 * jellyfin/jellyfin-web#429  Add prepare script for git installs
 * jellyfin/jellyfin-web#428  Fix preload background color
 * jellyfin/jellyfin-web#427  Add sorting for music albums in an artist's details page
 * jellyfin/jellyfin-web#425  Bump eslint-utils from 1.4.0 to 1.4.2
 * jellyfin/jellyfin-web#424  Add a "Copy Stream URL" button in the dropdown menu, for easy Direct Play in VLC
 * jellyfin/jellyfin-web#422  Use same css rules for section tabs
 * jellyfin/jellyfin-web#418  if collection has no playable items hide play and shuffle btns
 * jellyfin/jellyfin-web#417  add favorite books section to favorite tab
 * jellyfin/jellyfin-web#415  Fix redirect on wizardfinishpage
 * jellyfin/jellyfin-web#414  Resolve deviceId promise properly during apphost init
 * jellyfin/jellyfin-web#413  Fix card layout on home for books
 * jellyfin/jellyfin-web#412  Move transcoding page to playback settings and improve strings
 * jellyfin/jellyfin-web#411  Clean up unused filter audio language
 * jellyfin/jellyfin-web#410  Disable Group versions for non admin
 * jellyfin/jellyfin-web#408  Reflect changes made to main repo's stale bot config.
 * jellyfin/jellyfin-web#406  Enable blurred footer in chrome
 * jellyfin/jellyfin-web#405  Upgrade dependencies
 * jellyfin/jellyfin-web#403  Fix text overlap on now playing bar
 * jellyfin/jellyfin-web#402  Selectively hide manual login button
 * jellyfin/jellyfin-web#400  Add base url option to web client
 * jellyfin/jellyfin-web#399  Delete enhancement-request.md and feature-request.md
 * jellyfin/jellyfin-web#398  Add stale app config.
 * jellyfin/jellyfin-web#397  Allow card text to continue through line breaks
 * jellyfin/jellyfin-web#396  Move download action to major button for books (itemdetailspage)
 * jellyfin/jellyfin-web#388  Enable display mode setting
 * jellyfin/jellyfin-web#386  Change media info display
 * jellyfin/jellyfin-web#382  Fix homesection 'On now' display elements
 * jellyfin/jellyfin-web#381  Fix homesection programs button to go to correct page
 * jellyfin/jellyfin-web#380  Fix to enable tuner edit again
 * jellyfin/jellyfin-web#379  Add an ImageHelper class to consolidate frequently used icons
 * jellyfin/jellyfin-web#378  Add optional password field on user creation
 * jellyfin/jellyfin-web#377  Fix log issue from jellyfin/jellyfin-web#365
 * jellyfin/jellyfin-web#376  Fix adminDrawerLogo
 * jellyfin/jellyfin-web#375  Fix querySelector for Save metadata and images as hidden files
 * jellyfin/jellyfin-web#372  Add 'Series' button to Live TV menu off homesection
 * jellyfin/jellyfin-web#366  Minor fixes for section headers
 * jellyfin/jellyfin-web#365  Fix repeated automatic attempts to cast to a device
 * jellyfin/jellyfin-web#360  Small tweaks to the server settings
 * jellyfin/jellyfin-web#356  Fix certain elements getting incorrectly centered on firefox
 * jellyfin/jellyfin-web#353  Add proper styling to DlnaProfile and ScheduledTask pages
 * jellyfin/jellyfin-web#350  Move fanart provider to plugin
 * jellyfin/jellyfin-web#348  Fix firefox dropdown
 * jellyfin/jellyfin-web#343  Bundle npm dependencies using webpack
 * jellyfin/jellyfin-web#342  Add span class to fix a margin issue with some icons
 * jellyfin/jellyfin-web#339  Add editorconfig
 * jellyfin/jellyfin-web#337  Correction and translation of texts or words in spanish
 * jellyfin/jellyfin-web#336  Update purple haze theme and fix some unstyled elements
 * jellyfin/jellyfin-web#335  Always show options menu next to mouse
 * jellyfin/jellyfin-web#330  Merge current translations
 * jellyfin/jellyfin-web#327  Changes checkboxes focus appearance
 * jellyfin/jellyfin-web#326  Fix icon
 * jellyfin/jellyfin-web#325  Add some missing strings and remove gradients from themes
 * jellyfin/jellyfin-web#324  Change warning icons on dashboard to a bell instead of "pvr"
 * jellyfin/jellyfin-web#322  Fix secondery title position and show year on tv show ui
 * jellyfin/jellyfin-web#318  Add a response on icon hover and other style fixes
 * jellyfin/jellyfin-web#315  Move buttons to top right for custom scroll element
 * jellyfin/jellyfin-web#314  Initial support for keyboard navigation (for webOS remote etc.)
 * jellyfin/jellyfin-web#313  Improve the library page and dialog UX
 * jellyfin/jellyfin-web#312  Always show the start task button except on errors
 * jellyfin/jellyfin-web#307  Redirect when loading video player fails
 * jellyfin/jellyfin-web#300  Fix dashboard column & update purple haze
 * jellyfin/jellyfin-web#299  remove networking information from the dashboard
 * jellyfin/jellyfin-web#295  Add a round progress bar to purple haze theme
 * jellyfin/jellyfin-web#294  change cast & crew view to horizontal scroller
 * jellyfin/jellyfin-web#292  Fix some issues with the user preference page
 * jellyfin/jellyfin-web#278  New keyboard shortcuts
 * jellyfin/jellyfin-web#276  Fix text overflow not displaying ellipsis in cards
 * jellyfin/jellyfin-web#275  Add double click to fullscreen
 * jellyfin/jellyfin-web#272  Remove option to enable debug logging
 * jellyfin/jellyfin-web#271  Remove similar themes with accent changes
 * jellyfin/jellyfin-web#266  fix rounded progress bars
 * jellyfin/jellyfin-web#265  Update links for most of the old documentation
 * jellyfin/jellyfin-web#264  Fix Thumb rendering without thumbnails
 * jellyfin/jellyfin-web#251  Adding new Purple haze themes with rounded layout
 * jellyfin/jellyfin-web#241  Fix logout session storage
 * jellyfin/jellyfin-web#238  Remove unusable assets and update a string reference to connect
 * jellyfin/jellyfin-web#232  Replace more web archive buttons with new documentation
 * jellyfin/jellyfin-web#230  Remove unnecessary overflowY changes
 * jellyfin/jellyfin-web#229  Fix "Password Reset by PIN" page
 * jellyfin/jellyfin-web#224  Conversion to webpack - part5 - module resolution, data-require cleaned
 * jellyfin/jellyfin-web#220  Add subtitle synchronization on HTML video player

## 10.3.7 – 2019-07-24

10.3.7 hotfix release.

## Release Notes

* Fixes the regressions caused in the 10.3.6 release.

## Major Features

N/A

## Changelog

### jellyfin

#1537  Properly set content type
#1538  Try to fix XmlTvListingsProvider
#1552  Disable buffering in HttpClient as it causes big requests to timeout

### jellyfin-web

jellyfin/jellyfin-web#393  Fix to enable tuner edit again

## 10.3.6 – 2019-07-06

10.3.6 hotfix release.

## Release Notes

* Fixes the coexistence of Emby and Jellyfin apps on Android via jellyfin-web. All existing Jellyfin sessions will be ended and relogin will be required.
* Fixes some issues with TVDB and with segfaults from Skia, and with EnabledFolders.

## Major Features

N/A

## Changelog

### jellyfin

#1394  Check if an item is a child of an EnabledFolder
#1455  Vacuum databases at startup 
#1473  Apply deprecation web request on 10.3.z
#1478  Wait for the async authentication to finish when the JTW token expires
#1485  Fix skia segfault
#1495  Add nicer restart script
#1514  Fixes issues with HttpClientManager

### jellyfin-web

jellyfin/jellyfin-web#361  Allow Jellyfin and Emby to coexist on the same domain
jellyfin/jellyfin-web#364  Change channel mapper to sort list

## 10.3.5 – 2019-06-10

10.3.5 hotfix release.

## Release Notes

Fixes two bugs with the (pulled) 10.3.4 release, including a major security bug.

**NOTE:** This release fixes #1445 in a way that no workarounds are required. If an external auth provider fails or is removed, users who were entirely dependent on that auth provider now fail-closed (preventing login and logging an error) rather than fail-open. The password of the default auth provider for that user can still be reset in this case allowing access to the accounts in the failed state, if needed, by going through the usual password reset process and setting a password for the default auth provider. *Also note* that when in the failed state, *saving* a user config will reenable the default auth provider for the user, since this is selected by default; if doing this, ensure you set a password for the user immediately, otherwise do not attempt to modify users in this state via the admin dashboard before correcting the underlying issue; future releases may improve how this is handled visually on the user configuration page, but in this release it is implicit.

## Major Features

N/A

## Changelog

### jellyfin

#1443  Update arm* Dockerfiles for latest multiarch
#1447  Implement InvalidAuthProvider

### jellyfin-web

N/A

## 10.3.4 – 2019-06-07

10.3.4 hotfix release.

## Release Notes

Fixes several bugs with the 10.3.3 release.

**STOP**: This release is currently pulled due to #1445 - if you use the LDAP authentication plugin, do not upgrade.

## Major Features

N/A

## Changelog

### jellyfin

#1437  Fix issue #1436: media folders appear empty unless user has all libraries access
#1406  Format the PIN when updating it
#1426  Fix inverted comparison in the tvdb token refresh logic

### jellyfin-web

jellyfin/jellyfin-web#304  Fixed Progressive Web App for Android and iOS
jellyfin/jellyfin-web#333  Fix back button in PWA 
jellyfin/jellyfin-web#340  Fix context in querySelector
jellyfin/jellyfin-web#354  Add thumbnail fix to release

## 10.3.3 – 2019-05-18

10.3.3 hotfix release.

## Release Notes

Fixes several bugs with the 10.3.2 release.

* Problems with collections are fixed only for new collections; see #1338 for full details.

## Major Features

N/A

## Changelog

### jellyfin

#1294 Fix non-ascii filename downloads
#1306 Move artifact chown inside docker to avoid sudo
#1338 Enforce a specific folder structure for Extras to avoid misidentification
#1372 Fix broken pin in 10.3.z
#1380 Improve Photo rendering in DLNA

### jellyfin-web

jellyfin/jellyfin-web#304 Fixed Progressive Web App for Android and iOS
jellyfin/jellyfin-web#309 Various fixes for webOS 3.3
jellyfin/jellyfin-web#316 Correct the naming of iPad and iPhone
jellyfin/jellyfin-web#323 Resolve some android seeking issues

## 10.3.2 – 2019-05-01

10.3.2 hotfix release.

## Release Notes

Fixes several bugs from the 10.3.1 release.

## Major Features

N/A

## Changelog

### jellyfin

#1287  Re-add content length, semi revert of changes in #1010
#1296  Fix #1234
#1305  Fix passwordless authentication with non-json content-types
#1310  Remove unreachable code from BaseProgressiveStreamingService
#1324  Add arm64 packaging for Debuntu
#1327  Support libssl1.1 for Ubuntu Disco
#1332  Make the TvdbEpisodeProvider class Public
#1333  Fix incorrect hasPassword flag when easy pin set
#1334  Iterate over IEnumerable before disposing
#1335  Limit amount of ffmpeg processes extracting images at once

### jellyfin-web

jellyfin/jellyfin-web#270  Adds recording button back to view
jellyfin/jellyfin-web#277  Fix a broken Live TV page
jellyfin/jellyfin-web#287  Remove extraneous padding from sliders
jellyfin/jellyfin-web#290  Remove outdated Firefox check for slider bubble
jellyfin/jellyfin-web#291  Correct 404 on autoPlayDetect.js
jellyfin/jellyfin-web#296  Fix "Password Reset by PIN" page

## 10.3.1 – 2019-04-22

10.3.1 hotfix release.

## Release Notes

Fixes several bugs from the 10.3.0 release.

## Major Features

N/A

## Changelog

### jellyfin

#1258 Handle exception when loading unsupported assembly [allows server to continue starting even with invalid plugins]
#1264 Fix comparison for empty password migration [fixes empty passwords not being accepted]

### jellyfin-web

jellyfin/jellyfin-web#257 Load fallback culture before login [fixes missing strings on login page]
jellyfin/jellyfin-web#258 Fix server name input type [makes clients handle the URL path a little more gracefully]

## 10.3.0 – 2019-04-19

10.3.0 release.

## Release Notes

* This release makes non-backwards-compatible changes to the `users.db` database (#870). Ensure you take a backup of this database (with Jellyfin stopped) before upgrading if you wish to revert back to an earlier release.

* This release requires Windows users move the data directory from `%APPDATA%\jellyfin` to `%LOCALAPPDATA%\jellyfin` (#851). This is automatic with `install-jellyfin.ps1`. Based on RC testing this shouldn't cause any long-term problems.

* The 3rd-party API no longer accepts pre-hashed passwords for authentication; the clients MUST send a plaintext password, and this MUST be encrypted via HTTPS to avoid password leakage. Administrators who do not use HTTPS already (either in-app or via [reverse proxy](https://jellyfin.readthedocs.io/en/latest/administrator-docs/reverse-proxy/)) are **strongly encouraged** to do so.

* Plugins installed with Jellyfin 10.2.Z might not upgrade properly due to a bug in the plugin management system that has now been corrected. If you encounter errors while upgrading a plugin, the easiest solution is to remove the plugin first, then re-add it. To preserve configuration as well, delete the plugin directory on the filesystem (e.g. in Debuntu/Fedora under `/var/lib/jellyfin/plugins`) the reinstall the newer version.

* Users of **Yatse** should remove then re-add their Jellyfin server as the new Jellyfin type or authentication may fail.

* OpenSubtitles support has been moved to a plugin.

## Major features

* Uses the Kestrel web server instead of the previous homebrew web server.
* The insecure authentication system has been revamped to store passwords more securely and enable future external authentication.
* Individual user passwords can be reset without affecting other users.
* A mostly-Webpack-compatible WebUI.
* More translations.
* Numerous bugfixes around both the front- and back-end.

## Changelog

### jellyfin

#735 Readability changes
#776 Update tvdb provider to v2 api
#785 Remove useless abstraction around XmlReaderSettings
#800 Add CentOS and update rpm spec for the cachedir option
#801 Move to Microsoft.Extensions.DependencyInjection
#829 Removed some unused fields
#830 Removed remaining self-update code
#844 Reworked FFmpeg path discovery and always display to user
#847 Make websockets code async
#848 Minor changes to reduce allocations
#849 Less string allocations
#851 Simplify code to get data dir
#862 Add dotnet-compat ABI testing and Debug configuration building to drone-CI
#870 Better default authentication
#885 More warning fixes                 
#887 Replace primitive injection with IConfiguration
#889 Fix uncaught xml error
#891 Reduce the amount of db calls during the post scan event
#898 Switch to Roslyn naming rules in EditorConfig
#900 Implement proper FFmpeg version checking
#902 COPR auto building
#907 Fix assembly visibility                 
#913 Reduce log spam
#914 Separate HttpPostedFile into it's own file
#915 Remove IEncryptionManager
#930 checking user-permission in GetQueryResult
#934 Don't require a restart for 75% of plugins
#936 Fixed the assemblynames for compatibility check in drone.
#939 Clean up and rename obsolete deployment platforms
#947 Add Azure Pipelines YAML
#950 Replace OptimizedPriorityQueue source with NuGet reference
#952 Populate video extras again
#955 Avoid exceptions due to folder and file not found                                                                 
#959 Reduce string allocations at startup
#962 Fix Path
#977 Always set ffmpeg flag +genpts when video stream is being copied
#978 Fix DLNA for multiple interfaces on linux
#981 Close the response stream after fetching temp files
#984 Update kz.csv
#986 Backmerge submodule updating strategy
#996 Reduce the amount of exceptions thrown
#999 Check that ffmpeg log target isn't disposed before writing to it
#1000 Don't close the socket response multiple times
#1003 Use stopwatch for more accurate measurements and reduce log spam
#1007 Log time in a standardized way
#1009 Implement SxxExx EpisodeNum Processing
#1010 Remove System.Net and port to Kestrel
#1011 Don't try to order the response the same as the request
#1018 Fix rmvb video can not play under DLNA
#1020 Do not allow new users to delete content by default
#1021 Fail on warnings for Jellyfin.Server
#1028 Simplify rating loading
#1032 Correct the list of series types
#1043 Update image overlays to use Jellyfin blue
#1051 Build improvements for wrapping infrastructure
#1058 Cleanup/simplification
#1059 Remove EnvironmentInfo
#1060 Remove redundant class AssemblyInfo
#1061 Remove dead code
#1062 Fix the 2 new warnings
#1063 Update to renamed DownloadGitHubRelease task (Microsoft/azure-pipelines-tasks#9481)
#1064 Remove file added in #996
#1065 Don't set status code if response is closed
#1067 Add urlprefixes during init
#1069 Quick nullref fix
#1071 Fix error
#1072 Remove New File Header
#1075 Remove mirror images from library thumbnail
#1077 Make MusicBrainz base url configurable
#1081 Disable HTTPS in Kestrel if Certificate is null
#1089 Update translations
#1090 Set DisplayTitle for subtitles
#1091 Do not use the nuget packages for comparison, but the last master build
#1092 Add configurable webdir option
#1093 Use better path configuration for packages
#1094 Skip processing of images that don't exist
#1095 Add AppConfig to the DI service collection
#1096 Remove open subtitles from the server
#1098 Fix build by removing non existent namespace
#1100 Finalise removal of --ffprobe switch
#1103 Improvements around streams
#1104 Disable the Drone CI ABI check
#1105 Only delay making MusicBrainz request if necessary
#1106 More warning fixes
#1110 Adjusted the Product Name so the User Agent is correct/better
#1114 Only remove /var/lib/apt/lists/* in Dockerfile
#1115 Clean apt lists in arm Dockerfiles
#1116 Fix exception caused by #1096
#1117 Check before flushing ffmpeg log
#1119 MusicBrainz 503 Retry Strategy
#1120 Quick fix for auth bug
#1121 Update username regex to string literal with escaped -
#1127 Add configurable user lockout
#1136 Require access type to be included in bug report
#1137 Fix default value for Expires header
#1139 Update init scripts for compatibility with Devuan
#1140 Add Doxygen config
#1149 Adds per user password reset
#1151 Use public ports and advertise DNS if available for WAN address
#1153 Check if disposed first
#1157 Simplify/remove/clean code
#1166 Fix exception on startup
#1169 Use new libexecdir location for jellyfin-ffmpeg
#1170 Correct bad quote characters
#1171 Add Ubuntu armhf build
#1172 Minor improvements to release build setup                                                                                                                                                                                                
#1178 Updates windows installer default lib location
#1188 Fix problems with plugin installation
#1189 Update local path to include the jellyfin dir
#1190 Update Dockerfiles
#1195 Optimize images with image_optim
#1199 Use TLS 1.2 to download NSSM
#1209 Override username with AuthenticationProvider
#1221 Make Jellyfin search its base dir for ffmpeg
#1239 Clean up UDP responders, and move ProductName to Public endpoint
#1242 Fix metadata path save
#1244 Hotfix authapi

### jellyfin-web

jellyfin/jellyfin-web#128 Always show FFmpeg path in Transcoding page
jellyfin/jellyfin-web#144 Add top offset and bottom offset margins in emby-scrollbuttons
jellyfin/jellyfin-web#153 Make types more consistent
jellyfin/jellyfin-web#159 remove some deprecated plugin code
jellyfin/jellyfin-web#162 Convertion to webpack - part1 - npm and dynamic module resolution for site.js
jellyfin/jellyfin-web#166 Better progressive playback controls of bottom pages
jellyfin/jellyfin-web#168 Lots of changes to the server configuration pages
jellyfin/jellyfin-web#170 Updated translations
jellyfin/jellyfin-web#171 Sort item results in the same order as requested
jellyfin/jellyfin-web#172 Add web path as config option
jellyfin/jellyfin-web#175 Update the translation help link
jellyfin/jellyfin-web#177 Conversion to webpack - part2 - emby-webcomponents into components and module naming resolution
jellyfin/jellyfin-web#178 Remove unused localization strings (updated)
jellyfin/jellyfin-web#180 Apply typo fix for apphost
jellyfin/jellyfin-web#181 Correct syntax error in networkPath
jellyfin/jellyfin-web#187 Add CI for eslint
jellyfin/jellyfin-web#188 Conversion to webpack - part3 - routes isolation, module resolution, refactoring appStorage
jellyfin/jellyfin-web#189 Fix require apiInput
jellyfin/jellyfin-web#190 Add setting to support configurable user lockout
jellyfin/jellyfin-web#195 Remove no to nb
jellyfin/jellyfin-web#196 Return inner promise in createConnectionManager
jellyfin/jellyfin-web#197 Cleanup cordova modules - webpack fix
jellyfin/jellyfin-web#202 Remove sync and registration services
jellyfin/jellyfin-web#203 Remove all unused strings from translation files
jellyfin/jellyfin-web#204 Fix CI
jellyfin/jellyfin-web#205 Move assets and third party libs out of components and update some strings
jellyfin/jellyfin-web#206 Conversion to webpack - part4 - module resolution, appStorage refactor, minor cleanup
jellyfin/jellyfin-web#211 Adds web options to support better password resets
jellyfin/jellyfin-web#214 Fix Direct Playback broken in Chrome 73
jellyfin/jellyfin-web#216 Remove sync menu from multiselect
jellyfin/jellyfin-web#217 Re-add missing strings
jellyfin/jellyfin-web#218 Solve random dark pane over video playing in fullscreen mode
jellyfin/jellyfin-web#219 Change Chromecast volume instead while casting
jellyfin/jellyfin-web#221 Fix local chromecast play behind reverse proxy
jellyfin/jellyfin-web#222 Remember device volume/mute on Chromecast playback stop
jellyfin/jellyfin-web#223 When playing on Chromecast make volume buttons change chromecast volume
jellyfin/jellyfin-web#225 Fix restart button API call
jellyfin/jellyfin-web#226 Optimize images with image_optim
jellyfin/jellyfin-web#227 Update add server input type
jellyfin/jellyfin-web#231 Improve the plugin catalog and related controllers
jellyfin/jellyfin-web#235 Add check for multiserver on login page
jellyfin/jellyfin-web#237 Avoid element overlap with music controls
jellyfin/jellyfin-web#244 Fix a deminification issue with the plugin page
jellyfin/jellyfin-web#245 Add Missing strings "HeaderFavorite..."
jellyfin/jellyfin-web#247 Update the name in Manifest.json
jellyfin/jellyfin-web#249 Correct edititemmetadata.js script location
jellyfin/jellyfin-web#253 Readd missing strings

## 10.2.2 – 2019-03-01

Hotfix release from `10.2.1`.

#### Changelog (`jellyfin`)

* #968 Release 10.2.z copr autobuild
* #964 Install the dotnet runtime package in Fedora build
* #979 Build Package releases without debug turned on
* #990 Fix slow local image validation
* #991 Fix the ffmpeg compatibility
* #992 Add Debian armhf (Raspberry Pi) build plus crossbuild
* #998 Set EnableRaisingEvents to true for processes that require it
* #1017 Set ffmpeg+ffprobe paths in Docker container

#### Changelog (`jellyfin-web`)

* #152 Go back on Media stop
* #156 Fix volume slider not working on nowplayingbar

## 10.2.1 – 2019-02-21

Hotfix release from `10.2.0`.

#### Changelog

* #920 Fix cachedir missing from Docker container
* #924 Use the movie name instead of folder name
* #933 Semi-revert to prefer old movie grouping behaviour
* #948 Revert movie matching (supersedes #933, #924, #739)
* #960 Use jellyfin/ffmpeg image

## 10.2.0 – 2019-02-16

Jellyfin Server release 10.2.0.

#### Changelog

  * #452 Use EF Core for Activity database                                                                                                                                                                                                     
  * #535 Clean up streambuilder
  * #655 Support trying local branches in submodule
  * #656 Do some logging in MediaInfoService
  * #657 Remove conditions that are always true/false
  * #661 Fix NullRef from progress report
  * #663 Use TagLibSharp Nuget package
  * #664 Revert "Fix segment_time_delta for ffmpeg 4.1"
  * #666 Add cross-platform build for arm64
  * #668 Return Audio objects from MusicAlbum.Tracks
  * #671 Set EnableRaisingEvents correctly
  * #672 Remove unconditional caching, modified since header and use ETags
  * #677 Fix arm32 Docker
  * #681 Fix Windows build script errors + pin ffmpeg to 4.0
  * #686 Disable some StyleCop warnings
  * #687 Fix some analyzer warnings
  * #689 Fix RPM package build for fedora
  * #702 Fix debug build on windows
  * #706 Make another docker layer reusable
  * #709 Fix always null expressions
  * #710 Fix a spelling mistake
  * #711 Remove remnants of system events
  * #713 Fix empty statement in DidlBuilder.cs
  * #716 Remove more compile time warnings
  * #721 Change image dimentions from double to int
  * #723 Minor improvements to db code
  * #724 Move Skia back into it's own project
  * #726 Clean up IFileSystem wrappers around stdlib.
  * #727 Change default aspect ratio to 2/3 from 0
  * #728 Use ffmpeg from jrottenberg/ffmpeg
  * #732 Reworked LocalizationManager to load data async
  * #733 Remove unused function
  * #734 Fix more analyzer warnings
  * #736 Start startup tasks async
  * #737 Add AssemblyInfo for Jellyfin.Drawing.Skia
  * #739 Change multi version logic for movies
  * #740 Remove code for pre-installed plugins & properly check if file exists
  * #756 Make cache dir configurable
  * #757 Fix default aspect ratio
  * #758 Add password field to initial setup
  * #764 Remove dead code, made some functions properly async
  * #769 Fix conditions where the ! was swallowed in #726
  * #774 reimplement support for plugin repository
  * #782 Remove commented file MediaBrowser.LocalMetadata.Savers.PersonXmlSaver
  * #783 Update builds to use #749 and #756
  * #788 Fix more warnings
  * #794 Remove MoreLINQ
  * #797 Fix all warnings
  * #798 Cleanup around the api endpoints
  * #800 Add CentOS and update rpm spec for the cachedir option
  * #802 Fix build error
  * #804 Handle new option parser properly
  * #805 Add weblate translation status to README
  * #807 Fix restart script in OS packages
  * #810 Fix loading of rating files
  * #812 Fix up the explicit docs links in the README
  * #819 Some small changes in Device.cs and DidlBuilder.cs
  * #822 Complete rename ImageSize -> ImageDimensions
  * #824 Improved Docker pkgbuild
  * #831 Move some arrays to generics
  * #833 Add await to GetCountries in LocalizationService
  * #834 Add donation badge and reorganize badges
  * #838 Quick style fix
  * #840 Fix more warnings
  * #841 Fix OC badge to all and add forum badge
  * #842 Use VAAPI-enabled ffmpeg
  * #852 Use SQLitePCL.pretty.netstandard on NuGet
  * #853 Fix poor handling of cache directories
  * #864: Add support for ZIP plugin archives
  * #868: Fix audio streaming via BaseProgressiveStreamingService
  * #869: Remove DLL support and require all packages/plugins to be zip archives
  * #872: Fix potential NullReferenceException
  * #890: Drop ETag and use Last-Modified header
  * #892: Add jellyfin-ffmpeg and versioning to package deps
  * #899: DLNA: Fix race condition leading to missing device names
  * #901: Properly dispose HttpWebResponse when the request failed to avoid 'too many open files'
  * #909: Fix docker arm builds
  * #910: Enhance Dockerfiles
  * #911: Checkout submodules in Docker Hub hook

## 10.1.0 – 2019-01-25

Release 10.1.0 for `jellyfin`.

## Changelog

* #335: Build scripts and build system consolidation.        
* #424: add jellyfin-web as submodule                         
* #455: Cleanup some small things                              
* #458: Clean up several minor issues and add TODOs      
* #506: Removing tabs and trailing whitespace                     
* #508: Update internal versioning and user agents.
* #516: Remove useless properties from IEnvironmentInfo                              
* #520: Fix potential bug where aspect ratio would be incorrectly calculated
* #534: Add linux-arm and linux-arm64 native NuGet dependency.
* #540: Update Emby API keys to our own            
* #541: Change ItemId to Guid in ProviderManager   
* #556: Fix "Password Reset by PIN" page                             
* #562: Fix error with uppercase photo extension and fix typo in a log line
* #563: Update dev from master                               
* #566: Avoid printing stacktrace when bind to port 1900 fails
* #567: Shutdown gracefully when recieving a termination signal
* #571: Add more NuGet metadata properties               
* #575: Reformat all C# server code to conform with code standards
* #576: Add code analysers for debug builds               
* #580: Fix Docker build   
* #582: Replace custom image parser with Skia                              
* #587: Add nuget info to Emby.Naming
* #589: Ensure config and log folders exist
* #596: Fix indentation for xml files
* #598: Remove MediaBrowser.Text for license violations and hackiness
* #606: Slim down docker image
* #613: Update MediaEncoding
* #616: Add Swagger documentation
* #619: Really slim down Docker container
* #621: Minor improvements to library scan code
* #622: Add unified build script and bump_version script
* #623: Replaced injections of ILogger with ILoggerFactory
* #625: Update taglib-sharp
* #626: Fix extra type name in parameter, add out keyword
* #627: Use string for ApplicationVersion
* #628: Update Product Name (User-Agent)
* #629: Fix subtitle converter misinterpreting 0 valued endTimeTicks
* #631: Cleanup ImageProcessor and SkiaEncoder
* #634: Replace our TVDB key with @drakus72's which is V1
* #636: Allow subtitle extraction and conversion in direct streaming
* #637: Remove unused font
* #638: Removed XmlTv testfiles and nuget install
* #646: Fix infinite loop bug on subtitle.m3u8 request
* #655: Support trying local branches in submodule
* #661: Fix NullRef from progress report
* #666: Add cross-platform build for arm64
* #677: Fix arm32 build

Includes [release 10.1.0](https://github.com/jellyfin/jellyfin-web/releases/tag/v10.1.0) of [jellyfin-web](https://github.com/jellyfin/jellyfin-web).

## 10.0.1 – 2019-01-25

Hotfix release correcting regressions and obvious bugs from `10.0.0`.

Release tagged `10.0.1`. Debian build `10.0.1-1`.

## Changelog

#487: Support `*.log` files in browser log viewer
#488: Fix odd formatting in MimeType.cs
#512: Fix CONTRIBUTORS.md formatting    
#501: Fix regression in integer divisions in latest movies category
#498: Change contributing link in settings to readthedocs.io        
#493: Remove unused values.txt resource                           
#491: Fix userprofile.js crash
#519: Fix the DecodeJfif function to get proper image sizes
#486: Add NuGet package info to plugin projects
#523: Bump version for 10.0.1

## 10.0.0 – 2019-01-25

### Changelog based on referenced [pull requests](https://github.com/jellyfin/jellyfin/pull/419#issue-242422198)

* Rebranding completed - new colors, new logo, fixed links.
* Extensive code cleanup, should probably have some minor performance improvements. Also lots of warnings got fixed.
* Switched to Serilog for logging, now logs should be more readable and less of a bottleneck (they're written asyncronously now). Logging is now configurable and goes to proper `/var/log/jellyfin` for Debian packages.
* Removed lots of remaining phoning home (includes check for update and for news) which cluttered logs with errors. Reduced verbosity of default ffmpeg logging.
* Fixed support for clients requesting AAC to be downsampled to stereo from 5.1, needed to support some Chromecast use cases.
* Fixed XmlTv access error, removed Premiere nag in XmlTv access.
* Re-enabled UDP auto-discovery of Jellyfin server by clients that support that on LAN; added proper license for the project used for this auto-discovery.
* Fixed library access and device list access by a non-admin user if admin user previously didn't visit the pages.
* Stopped downloading fonts during runtime.
* Default theme is set to dark for admin pages and first setup.
* Fixed some DLNA casting issues.
* Docker images now bundle `ffmpeg 4.0.3` and are made smaller and faster to rebuild.
* Dropped ImageMagick and Drawing.Net in favor of leaving only Skia for image processing. **Note**: so far no Skia dotnet bindings exist for ARM.
* Language files were cleaned of unused strings; Danish translation was improved.
* SMB support in application was removed - Jellyfin won't load files over SMB protocol, one should properly mount a share using OS mechanism instead.
* Removed Connect in UI as it requires centralized service which Jellyfin doesn't intend to implement.
* Debian source tarballs are made smaller.
* Documentation moved to https://jellyfin.readthedocs.io/en/latest/

(Thanks to @JustAMan for compiling this [changelog](https://github.com/jellyfin/jellyfin/pull/419#issuecomment-452701091).)

## 10.0.2 – 2019-01-25

Hotfix release correcting regressions and obvious bugs from `10.0.1`.

Release tagged `10.0.2`. Debian build `10.0.2-1`.

## Changelog

jellyfin/jellyfin-web#23: Update Chromecast app ID [via direct commit]
#540: Update Emby API keys to our own
#541: Change ItemId to Guid in ProviderManager
#566: Avoid printing stacktrace when bind to port 1900 fails
