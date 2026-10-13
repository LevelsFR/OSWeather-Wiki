# Compatibility matrix

**Mod:** `0.9.0-beta.10.5` (pre-v1) · **API revision:** `1`  
**Build and core smoke verified:** 2026-10-14 · **Runtime verified:** no

| Minecraft | Loader | Java | Build + 47-scenario core smoke | Client/world/server runtime |
|---|---|---:|---|---|
| 1.21.1 | Fabric | 21 | Pass | Not tested |
| 1.21.1 | NeoForge | 21 | Pass | Not tested |
| 26.2 | Fabric | 25 | Pass | Not tested |
| 26.2 | NeoForge | 25 | Pass | Not tested |
| 26.3 | Fabric | 25 | Pass | Not tested |
| 26.3 | NeoForge | 25 | Pass | Not tested |

The build used Fabric API `0.116.17+1.21.1`, `0.160.0+26.2`, `0.160.7+26.3`; NeoForge `21.1.250`, `26.2.0.88`, `26.3.0.16-beta`, respectively.

A successful compile/smoke check is **not** a claim that the client starts, a world can be joined, or a dedicated server works. Test the exact loader and Minecraft combination before using it on a production world. Other releases are not claimed as supported. See [release status](release-status.md).