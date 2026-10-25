# Sources: tools for organising a large personal photo and video library (researched 2026-10-25)

This research is behind the decision to adopt Immich, wrapped in a thin studio bridge, instead of maintaining our own CLIP organiser. Our own script measured 83% category accuracy on a 69-item test set.

**Labels:**
- **[V]**: confirmed in a primary source (official docs, release notes, or the OpenAPI spec).
- **[S]**: from a secondary source.
- **[U]**: unverified.

## Decision

**Primary tool: Immich v3.3.5** (released 21 Oct 2026, AGPL-3.0), self-hosted with Docker Desktop on WSL2.

It is the only option that covers all of the following together:
- Natural-language smart search with a selectable, benchmarked model. In Immich's Crossmodal-3600 recall table, `ViT-SO400M-16-SigLIP2-384__webli` scores 85.99% and `ViT-B-16-SigLIP2__webli` scores 84.86% [V, docs.immich.app/features/searching].
- InsightFace face clustering (buffalo_l) [S].
- Duplicate detection based on CLIP embeddings [S].
- OCR, timeline and map.
- Phone backup.
- Read-only external libraries [V].
- A typed REST API with scoped API keys. For example, `POST /api/search/smart` accepts `query`, `personIds`, `type`, `isFavorite`, `rating` and `tagIds` [V, OpenAPI 3.3.0].

## Rejected or optional alternatives

**Optional:**
- **digiKam 9.0.0** (Mar 2026). It is native on Windows and uses YuNet + SFace faces, YOLOv11 auto-tags and an AI image-quality scanner. It has no natural-language search; its results are queryable through SQLite and XMP. Optional if XMP portability is needed [V].
- **Czkawka/Krokiet 12.0.2** (Sep 2026). A free duplicate and similar-video report. Use it as a report only [V].

**Rejected:**
- **PhotoPrism.** Labels at 224 px, YuNet + SFace faces. Vision LLM features require the paid Plus tier, and the API has no deprecation policy [V/S].
- **LibrePhotos 1.2.0.** Promising, but a small team [S].
- **Ente.** Has no query API because everything is end-to-end encrypted [S].
- **Google Photos.** Since 31 Mar 2025 the Library API only reads media the app uploaded itself [V], and cloud storage is a privacy issue for patients and minors.
- **Windows Photos.** No face grouping in the new app [V].
- **Paid culling tools** (Aftershoot, Narrative Select, Imagen). Paid. No mature open-source culler exists, so we keep our own sharpness and exposure re-rank.
- **Local vision-LLM captioners** (PhotoScribe, A-Eye, exif-ai). Optional later. They write XMP, so use sidecars only.

## Integration facts used by `immich_bridge.py`

**API access** [V, OpenAPI 3.3.0-rc.0, downloaded 2026-10-25]:
- Auth uses the `x-api-key` header.
- Calls used:
  - `GET /api/search/person?name=`
  - `POST /api/search/smart` and `POST /api/search/metadata`
  - `GET /api/assets/{id}` (people, tags, `duplicateId`, `originalPath`)
  - `GET /api/assets/{id}/thumbnail?size=preview`
  - `GET /api/assets/{id}/original`
  - `GET/POST /api/tags` and `PUT /api/tags/{id}/assets`
  - `GET /api/albums`
- First-run setup uses:
  - `POST /api/auth/admin-sign-up` and `/auth/login`
  - `POST /api/api-keys {name, permissions}`
  - `GET/PUT /api/system-config` (`machineLearning.clip.modelName`)
  - `POST /api/libraries {ownerId, importPaths, exclusionPatterns}`
  - `POST /api/libraries/{id}/scan`
  - `PUT /api/jobs/{queue} {command: start, force}`
  - `GET /api/queues` (needs `queue.read`)

**Behaviour to know:**
- Smart search and faces see **one poster frame per video** [S]. For moments inside a clip, use the B-roll multi-frame index.
- Edits made in Immich (names, albums) live in its database, not in the files [V]. Removing an import path drops those assets and their metadata [V].
- Google Drive: Docker can't reliably read the streamed `G:` drive [S]. Use Drive "Mirror files" or a local copy [V, Google help 13401938].

## Found while testing in this repo's sandbox (2026-10-25)

1. **IPv6.** The ML container listens on `[::]` by default and failed to start on a host without IPv6. Setting `IMMICH_HOST: 0.0.0.0` in the override fixes it and is harmless elsewhere.
2. **API key scope.** The studio key needs `queue.read` to report indexing status.
3. **Tags on read-only folders don't persist.** Immich writes tags to XMP sidecars next to the photo. On a read-only mount the write fails, so the tag silently disappears even though `PUT /tags/{id}/assets` returns success. Studio flags and curation therefore use albums and favourites, which are database-only.
4. **Sensitive check calibration.** A single yes/no CLIP prompt pair tagged founder headshots as "patient". Comparing the positive against the best of 7 negatives, with per-kind margins, gave clean results: documents 4/4 plus 1 text-heavy infographic, patients 2/2 with 0 headshots, and minors over-flagged by design.
5. **Sandbox proxy (test only, not in the kit).** The sandbox's TLS-intercepting proxy broke Hugging Face model downloads. We worked around it with host networking and a mounted CA certificate. A normal Windows PC doesn't need this.

## Community MCP servers for Immich (optional; not installed)
- **drolosoft/immich-photo-manager**: a Claude Code plugin with 94 tools, MIT, tested on Immich 3.1 [S]. It includes delete tools, so give it a read-scoped key.
- **barryw/ImmichMCP**: MIT, 49 tools [S].
- **okopok/immich-mcp**: 276 tools generated from the OpenAPI spec [S].

Review any of these before installing.

## Key sources
- Immich:
  - releases: https://github.com/immich-app/immich/releases
  - searching: https://docs.immich.app/features/searching
  - libraries: https://docs.immich.app/features/libraries
  - requirements: https://docs.immich.app/install/requirements
  - ML hardware acceleration: https://docs.immich.app/features/ml-hardware-acceleration
- PhotoPrism AI: https://docs.photoprism.app/user-guide/ai/
- digiKam 9.0.0: https://www.digikam.org/news/2026-03-08-9.0.0_release_announcement/
- Czkawka: https://github.com/qarmin/czkawka/releases
- Google Photos API updates: https://developers.google.com/photos/support/updates
- Drive stream vs mirror: https://support.google.com/drive/answer/13401938
