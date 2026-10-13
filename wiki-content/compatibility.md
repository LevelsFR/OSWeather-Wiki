# Compatibility matrix
**Current project version:** `0.9.0-beta.10.5` · **Public API:** v1

| Minecraft | Loader | Java | Configured baseline | Verified so far | Not yet verified |
|---|---|---:|---|---|---|
| 1.21.1 | Fabric | 21 | Fabric API 0.116.17+1.21.1 | Build/core smoke | Full client, world entry, server |
| 1.21.1 | NeoForge | 21 | NeoForge 21.1.250 | Build/core smoke | Full client, world entry, server |
| 26.2 | Fabric | 25 | Fabric API 0.160.0+26.2 | Build/core smoke | Full client, world entry, server |
| 26.2 | NeoForge | 25 | NeoForge 26.2.0.88 | Build/core smoke | Full client, world entry, server |
| 26.3 | Fabric | 25 | Fabric API 0.160.7+26.3 | Build/core smoke | Full client, world entry, server |
| 26.3 | NeoForge | 25 | NeoForge 26.3.0.16-beta | Build/core smoke | Full client, world entry, server |

## What these statuses mean
- **Build/core smoke:** code compiles and deterministic core checks are documented.
- **Not yet verified:** full Minecraft runtime entry, shader/resource-pack combinations and realistic dedicated-server profiling.
- **Future versions:** Minecraft releases beyond 26.3 are **planned for consideration**, not implemented or supported targets. Other 1.21.x versions are not listed as support targets.

A successful build **is not** a verified runtime compatibility claim. See [release status](release-status.md).
