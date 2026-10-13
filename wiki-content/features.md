# Features

OS Weather computes local atmospheric conditions for the Overworld on the server and synchronizes player-specific snapshots to clients.

- **47 climate-weighted scenarios** and a deterministic simulation core.
- **512-block atmospheric cells** with spatial interpolation.
- **Active-area updates**; the simulation does not force-load Minecraft chunks.
- **Persisted atmosphere state** and fast-forward handling for elapsed time.
- **Weather state** for rain, snow, wind, clouds, fog, storms, sandstorms and blizzards.
- **Visual/gameplay overrides** with priority and explicit release handles.
- **Dimension-provider API** for addon integrations.

The code and core smoke checks are not full in-game validation. Cloud/rendering polish, specialized effects, shader/resource-pack combinations, lightning presentation and runtime behavior remain release checks. Vanilla `/weather clear/rain/thunder` is bridged, but compatibility with every other weather/rendering mod is not claimed. See [release status](release-status.md).