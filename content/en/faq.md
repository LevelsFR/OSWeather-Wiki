# FAQ

## Is OS Weather a stable v1?
No. The documented mod is `0.9.0-beta.10.5`, a pre-v1 release. **API revision 1 is not mod version 1.0.**

## What has actually been tested?
On 2026-10-14, all six configured Minecraft/loader targets assembled and each deterministic core smoke check passed 47 scenarios. No client, world-entry, multiplayer or dedicated-server runtime validation was performed. See [release status](release-status.md).

## Is Minecraft 26.3 fully supported?
It is a configured build target that compiled and passed the core smoke check. Runtime support remains unverified.

## Can I download the mod here?
No binary is published by this documentation repository. Install only a JAR officially distributed by the author.

## Does the mod support dimensions beyond the Overworld?
The built-in simulation owns the Overworld. The API exposes a dimension-provider extension point, but this is not evidence that a particular addon or dimension has been tested.

## Are Cloth Config and Mod Menu required?
No. They are optional configuration-screen integrations. TOML files remain available without them; see [configuration](configuration.md).

## Can I distribute an addon using the API?
The API pages describe technical hooks, not legal permission. Terms for distributing third-party integrations have not been expressly published; obtain written authorization where needed. See [rights](rights.md).

## Where do I report a bug?
Use the [public issue forms](https://github.com/LevelsFR/OSWeather-Wiki/issues/new/choose) and include redacted logs, exact versions and reproduction steps.