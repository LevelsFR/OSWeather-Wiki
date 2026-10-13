# Installation

> **Pre-release:** the documented build is `0.9.0-beta.10.5`, not a stable v1. This documentation repository does not publish mod binaries. Use only a JAR officially supplied by the author.

| Minecraft | Loader | Java | Build/core smoke | In-game runtime |
|---|---|---:|---|---|
| 1.21.1 | Fabric or NeoForge | 21 | Pass | Not tested |
| 26.2 | Fabric or NeoForge | 25 | Pass | Not tested |
| 26.3 | Fabric or NeoForge | 25 | Pass | Not tested |

The build and smoke results were last verified on 2026-10-14. A successful build does not guarantee that the game starts or a world loads.

## Install

1. Obtain the official runtime JAR matching both Minecraft and the loader.
2. Install the matching Fabric or NeoForge loader.
3. On Fabric, install Fabric API for the same Minecraft version.
4. Put the runtime JAR in the instance's `mods/` directory.
5. For multiplayer, use a matching mod build on the server and clients where required.

Client settings are in `config/osweather-client.toml`; server simulation settings are in `config/osweather-server.toml` on the server. Cloth Config/Mod Menu are optional UI integrations. Never install a sources JAR as the mod. See [compatibility](compatibility.md) and [configuration](configuration.md).