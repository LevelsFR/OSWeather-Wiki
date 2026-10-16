# FAQ

## What is the current release?
OS Weather is the stable V1 release, version `1.0`. The CurseForge page does not yet show stable packages for every supported target; see [release status](release-status.md) for file availability.

## Which Minecraft versions and loaders does stable V1 support?
The stable V1 target matrix covers Minecraft 1.21.1, 26.2.x and 26.3.x on both Fabric and NeoForge. CurseForge determines which stable JARs have actually been uploaded; see the [compatibility page](compatibility.md).

## Where can I download the mod?
Download the stable `1.0` runtime JAR matching your Minecraft version and loader from [CurseForge](https://www.curseforge.com/minecraft/mc-mods/os-weather). If the stable file for your target is not listed yet, it is not available to download. This documentation repository does not host the mod binary.

## Is API revision 1 the same version number as mod 1.0?
No. API revision and mod version are independent. The stable mod release is `1.0`, and the API revision is `1`.

## Does the mod support dimensions beyond the Overworld?
The built-in simulation owns the Overworld. The API exposes a dimension-provider extension point, but this does not guarantee compatibility with a particular addon or dimension mod.

## Are Cloth Config or Mod Menu required?
No. They are optional configuration-screen integrations where supported. TOML files remain available without them; see [configuration](configuration.md).

## Can server settings be changed without restarting?
Yes. An operator can use the in-game Server settings tab. If the server TOML file is edited directly, an operator can run `/osweather reload` to apply the changes immediately.

## Can I distribute an addon using the API?
The API pages describe technical hooks, not legal permission. Obtain written authorization where needed; see [rights](rights.md).

## Where do I report a bug?
Use the [public issue forms](https://github.com/LevelsFR/OSWeather-Wiki/issues/new/choose) and include redacted logs, exact versions and reproduction steps.
