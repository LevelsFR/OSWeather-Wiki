# Configuration

OS Weather separates client-only presentation options from server-owned simulation settings. Both files are TOML under the Minecraft `config/` directory.

## Client: `osweather-client.toml`

| Key | Default | Meaning |
|---|---:|---|
| `enhanced_clouds` | `true` | Enables OS Weather's cloud presentation changes. |
| `precipitation` | `true` | Enables the mod's precipitation presentation. |
| `fog` | `true` | Enables weather fog effects. |
| `particles` | `true` | Enables weather particles. |
| `visual_lightning` | `true` | Enables visual lightning presentation. |
| `sounds` | `true` | Enables weather sounds. |
| `cloud_quality` | `2` | Cloud detail: 0 low, 1 medium, 2 high, 3 ultra (clamped to 0–3). |

Client options can be changed in-game when the optional configuration-screen dependencies are installed, or edited directly in the file. On Fabric, Cloth Config provides the screen and optional Mod Menu exposes its entry. NeoForge registers the screen when Cloth Config is available. Neither is required for the mod to load.

## Server: `osweather-server.toml`

| Key | Default | Meaning |
|---|---:|---|
| `enabled` | `true` | Enables the server weather service. |
| `local_weather` | `true` | Uses per-player/local weather behavior. |
| `gameplay_weather` | `true` | Enables gameplay-side weather integration. |
| `real_lightning` | `false` | Allows real lightning only when gameplay weather is enabled and `local_weather=false`; strikes are world-global. |
| `sync_interval_ticks` | `100` | Snapshot interval, clamped to 40–1,200 ticks. |
| `sleep_calming_bias` | `0.10` | Sleep-calming bias, clamped to 0–0.35. |

The server is authoritative. Server-file changes require a server restart; `/osweather reload` only displays that restart notice and does not reload settings. Never post an unredacted live server configuration in a bug report.