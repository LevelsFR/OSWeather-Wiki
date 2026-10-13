# Pre-v1 release status

**Snapshot:** mod `0.9.0-beta.10.5`; API revision `1`. The mod is **not a stable 1.0 release**.

## Verified locally on 2026-10-14

- `gradlew assembleAllVersions --no-daemon --max-workers=1` completed successfully.
- All six configured targets assembled: 1.21.1, 26.2 and 26.3 on Fabric and NeoForge.
- Each target's `coreSmoke` passed **47 scenarios**.

## Not verified

- Gradle `test` tasks were skipped by the aggregate build.
- No Minecraft client launch, world entry, multiplayer session or dedicated-server launch was performed.
- Rendering, shader/resource-pack interactions, networking under real play, server performance and config UI still need runtime checks.
- The build emitted a non-fatal `LevelRenderer.render` remapping diagnostic and a 26.3 generated-client deprecation note. Their in-game impact has not been established.
- No official downloadable JAR or standalone Maven API artifact is published from this documentation repository.

These results establish **build and deterministic core-smoke status only**, not full gameplay compatibility or release readiness. See the [compatibility matrix](compatibility.md).