# API v1: Weather overrides
Overrides temporarily replace selected weather behavior without rewriting the atmospheric simulation.

## Fields of WeatherOverride
| Field | Type | Meaning |
|---|---|---|
| `weatherId` | String | Namespaced weather identifier |
| `intensity` | float | Intensity, clamped to 0..1 |
| `expiresAtTick` | long | Expiration tick; `-1` means no expiry |
| `priority` | int | Higher priority wins |
| `source` | String | Addon/event owner identifier |
| `visual` | boolean | Affect presentation weather |
| `gameplay` | boolean | Affect gameplay weather |

At least one of `visual` or `gameplay` must be true. Equal-priority overrides select the most recently created override. Use a player UUID to target one player; a `null` UUID targets all players. A player-specific override may win when assigned a higher priority.

## Lifecycle
Call `OSWeather.api().setOverride(playerUuid, override)`, **retain the returned `OverrideHandle`**, then call `releaseOverride(handle)` when the event/addon ends. An indefinite override must still be cleaned up intentionally.

See [integration examples](api-examples.md).
