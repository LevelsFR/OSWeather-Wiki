# API v1 Reference
**Package namespace:** `com.ourstory.osweather.api` · **API version:** `1` · **Documented mod:** `0.9.0-beta.10.5`

> The API version and mod version are independent. The API signatures here describe technical extension points, **not an addon distribution license**.

## Entry point
`com.ourstory.osweather.OSWeather.api()` provides the `OSWeatherApi` interface, which exposes:

| Method | Return / purpose |
|---|---|
| `apiVersion()` | API revision number |
| `visualWeather(WeatherContext)` | Presentation weather snapshot |
| `gameplayWeather(WeatherContext)` | Gameplay/compatibility snapshot |
| `setOverride(UUID, WeatherOverride)` | Create an override and obtain a handle |
| `releaseOverride(OverrideHandle)` | Release an override |
| `registerDimensionProvider(DimensionWeatherProvider)` | Register weather for a dimension |

## WeatherContext
Fields: `dimensionId` (String), `playerId` (UUID), `x`, `y`, `z` (double), `gameTick` (long).

## AtmosphereSnapshot
Read `weatherId`, `scenarioId`, `temperatureC`, `humidity`, `pressureHpa`, `windX`, `windZ`, `cloudCover`, `precipitation`, `thunder`, `fog`, `sandstorm`, `snow`, `visibility` and `gameTick`.

Helpers: `windSpeed()`, `precipitationType()`, `isRaining()`, `isSnowing()`, `isThundering()`. Precipitation types: `NONE`, `RAIN`, `SNOW`.

## Stability and scope
Core OS Weather handles `minecraft:overworld`; extensions for other dimensions use [providers](api-dimensions.md). Rely on public `api` packages, not `internal`, `simulation` or loader-specific implementation packages.

See [examples](api-examples.md) and [overrides](api-overrides.md).
