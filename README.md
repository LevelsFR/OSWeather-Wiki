# OS Weather | Official Public Documentation

**OS Weather** is a server-authoritative local atmospheric weather simulation for Minecraft, developed by **LevelsFR**.

> This is the public documentation and issue-tracker repository, not the mod source repository. The mod and source code remain private and proprietary: **All Rights Reserved**.

**Documented mod build:** `0.9.0-beta.10.5` (**pre-v1**) · **API revision:** `1` · **Mod ID:** `osweather`

## Documentation

The bilingual [OS Weather Wiki site](https://levelsfr.github.io/OSWeather-Wiki/) is published with GitHub Pages.

- [Installation](content/en/installation.md) · [Compatibility matrix](content/en/compatibility.md)
- [Features](content/en/features.md) · [Commands](content/en/commands.md) · [Configuration](content/en/configuration.md)
- [API v1](content/en/api-v1.md) · [Integration examples](content/en/api-examples.md) · [Overrides](content/en/api-overrides.md) · [Dimension providers](content/en/api-dimensions.md)
- [Release validation status](content/en/release-status.md) · [FAQ](content/en/faq.md) · [Support](content/en/support.md)
- [Français](content/fr/index.md)

The six configured variants (Minecraft 1.21.1, 26.2 and 26.3 on Fabric and NeoForge) compile and pass 47 deterministic core smoke scenarios each. **Client launch, world entry and dedicated-server runtime are not yet validated**, so this is not a stable V1 release and no runtime compatibility guarantee is made.

## Support

Report bugs and request features through [GitHub Issues](https://github.com/LevelsFR/OSWeather-Wiki/issues/new/choose). Include the exact Minecraft, loader and mod versions, reproduction steps and **redacted** logs. Never post tokens, private server addresses, personal information or sensitive configuration.

## Proprietary software and API

Publishing API signatures and examples does **not** grant a software or addon-distribution license. No standalone Maven API artifact is published, and third-party addon distribution terms have not been expressly approved. Read [Rights and API permissions](RIGHTS.md).

## Private-source boundary

This repository does not contain mod source, private build files, secrets, runtime binaries or private logs. `LevelsFR/OSWeather` remains private. The public [Pages site](https://levelsfr.github.io/OSWeather-Wiki/) is the canonical documentation; the native GitHub Wiki is separate.