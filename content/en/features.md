# Features

OS Weather computes local atmospheric conditions for the Overworld on the server and synchronizes player-specific snapshots to clients.

- **47 climate-weighted scenarios** and a deterministic simulation core.
- **512-block atmospheric cells** with spatial interpolation.
- **Active-area updates**; the simulation does not force-load Minecraft chunks.
- **Persisted atmosphere state** restored when the world loads; the simulation does not catch up while the world is offline.
- **Weather state** for rain, snow, wind, clouds, fog, storms, sandstorms and blizzards.
- **Visual/gameplay overrides** with priority and explicit release handles.
- **Dimension-provider API** for addon integrations.

The author confirms that OS Weather is ready for the stable V1 release (`1.0`). Vanilla `/weather clear/rain/thunder` is bridged, but compatibility with every other weather or rendering mod is not claimed. See [release status](release-status.md).
