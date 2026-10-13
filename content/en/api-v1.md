# API v1 Reference

**Package:** `com.ourstory.osweather.api` · **API revision:** `1` · **Documented mod:** `0.9.0-beta.10.5` (pre-v1).

The API revision and mod release version are independent. These pages document technical extension points, not a stable mod release or a license to distribute addons.

## Main entry points

| Type | Role |
|---|---|
| `OSWeatherApi` | Query visual/gameplay weather, manage overrides and register dimension providers. |
| `WeatherContext` | Dimension, optional player and position/tick context for queries. A null dimension defaults to the Overworld. |
| `AtmosphereSnapshot` | Immutable result containing weather/scenario identifiers and atmospheric values. |
| `WeatherOverride` | Override definition; intensity is clamped and at least one of visual/gameplay must be enabled. |
| `DimensionProviderRegistry` | Orders providers by priority; registering the same provider id replaces its prior entry. |

The current API exposes `apiVersion()`, `visualWeather(context)`, `gameplayWeather(context)`, `setOverride(playerUuid, override)`, `releaseOverride(handle)` and `registerDimensionProvider(provider)`. See the dedicated [override](api-overrides.md), [dimension](api-dimensions.md) and [example](api-examples.md) pages.

**Distribution:** no standalone API JAR or Maven coordinates are currently published. The source repository is private. The API reference is not a substitute for an authorized compile-time dependency.