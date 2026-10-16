# API v1 Reference

**Package:** `com.ourstory.osweather.api` · **API revision:** `1` · **Stable mod release:** `1.0` (V1 stable).

The API revision and mod release version are independent. The stable V1 mod release is `1.0`; the API remains revision `1`. These pages document technical extension points, not a license to distribute addons.

## Main entry points

| Type | Role |
|---|---|
| `OSWeatherApi` | Query visual/gameplay weather, manage overrides and register dimension providers. |
| `WeatherContext` | Dimension, optional player and position/tick context for queries. A null dimension defaults to the Overworld. |
| `AtmosphereSnapshot` | Immutable result containing weather/scenario identifiers and atmospheric values. |
| `WeatherOverride` | Override definition; intensity is clamped and at least one of visual/gameplay must be enabled. |
| `DimensionWeatherProvider` | Public extension interface for weather in another dimension. |

The provider registry is an internal implementation detail. Register providers through `OSWeatherApi`; do not depend on internal classes.

The public API exposes `apiVersion()`, `visualWeather(context)`, `gameplayWeather(context)`, `setOverride(playerUuid, override)`, `releaseOverride(handle)` and `registerDimensionProvider(provider)`. See the dedicated [override](api-overrides.md), [dimension](api-dimensions.md) and [example](api-examples.md) pages.

**Distribution:** no standalone API JAR or Maven coordinates are published. The source repository is private. This reference is not a substitute for an authorized compile-time dependency.
