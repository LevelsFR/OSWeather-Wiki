# Installation

> The stable OS Weather V1 release is version `1.0`. Install only a stable `1.0` file matching your Minecraft version and loader. The CurseForge page does not yet list stable packages for the full target matrix; verify that the matching stable file is available before downloading.

## Install the mod

1. [Download the stable OS Weather 1.0 file from CurseForge](https://www.curseforge.com/minecraft/mc-mods/os-weather) that matches your Minecraft version and loader.
2. Install the matching Minecraft and loader target. Use Java 21 for Minecraft 1.21.1 and Java 25 for 26.2.x/26.3.x.
3. Put the runtime JAR in the instance's `mods/` directory.
4. For multiplayer, install the matching release on the server and on the clients that join.

Do not use a source JAR. Each Minecraft/loader combination requires its matching runtime JAR; see the [compatibility matrix](compatibility.md) and the CurseForge files page.

Client settings are stored in `config/osweather-client.toml`. Server simulation settings are in `config/osweather-server.toml` on the server. The optional configuration screen is not required; see [configuration](configuration.md) and [compatibility](compatibility.md).
