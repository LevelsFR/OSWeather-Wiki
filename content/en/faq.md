# FAQ

## Is OS Weather a stable release?
The current public build is `1.0-beta`, not a stable final `1.0`. The author confirms that the v1 beta for Minecraft 1.21.1 is validated. See [release status](release-status.md).

## Which Minecraft version and loader does the current file target?
The public CurseForge file is for Minecraft 1.21.1 on NeoForge. Other Minecraft versions and loaders are not covered by this file; check the [compatibility page](compatibility.md).

## Where can I download the mod?
Download the current runtime JAR from [CurseForge](https://www.curseforge.com/minecraft/mc-mods/os-weather). This documentation repository does not host the mod binary.

## Does API revision 1 mean the mod is a stable 1.0?
No. The API revision and mod version are independent. The current mod build is `1.0-beta`.

## Does the mod support dimensions beyond the Overworld?
The built-in simulation owns the Overworld. The API exposes a dimension-provider extension point, but this does not guarantee compatibility with a particular addon or dimension mod.

## Are Cloth Config or Mod Menu required?
No. They are optional configuration-screen integrations where supported. TOML files remain available without them; see [configuration](configuration.md).

## Can I distribute an addon using the API?
The API pages describe technical hooks, not legal permission. Obtain written authorization where needed; see [rights](rights.md).

## Where do I report a bug?
Use the [public issue forms](https://github.com/LevelsFR/OSWeather-Wiki/issues/new/choose) and include redacted logs, exact versions and reproduction steps.
