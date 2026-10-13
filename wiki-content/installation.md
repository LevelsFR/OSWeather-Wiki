# Installation
> **Pre-release notice:** documentation covers `0.9.0-beta.10.5`. The six target variants are configured and compile in the project; **runtime launch/world-entry validation remains pending**. Do not assume a public binary exists until the author distributes one.

## Requirements
| Minecraft | Loader | Java |
|---|---|---|
| 1.21.1 | Fabric or NeoForge | 21 |
| 26.2 | Fabric or NeoForge | 25 |
| 26.3 | Fabric or NeoForge | 25 |

### Steps
1. Obtain the **official distributed OS Weather JAR** for your Minecraft version and loader.
2. Install the matching Fabric or NeoForge loader.
3. **Fabric:** install Fabric API matching the target Minecraft release.
4. Place the correct OS Weather JAR into the instance/server `mods` directory.
5. Launch and inspect the log for load failures. For multiplayer, use a matching server installation where required.

### Configuration
Client settings use `config/osweather-client.toml`; server-side simulation settings use `config/osweather-server.toml`. Edit server settings on the server. On Fabric, **Cloth Config + Mod Menu are optional** for the client settings screen; the file configuration remains available without them.

Consult [compatibility](compatibility.md) before reporting a loader failure. **Never install a sources JAR** as the runtime mod.
