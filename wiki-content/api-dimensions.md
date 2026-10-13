# API v1: Dimension weather providers
OS Weather's built-in simulation owns only `minecraft:overworld`. External dimensions are deliberately served through a provider registry.

## DimensionWeatherProvider
Implement the public interface `com.ourstory.osweather.api.provider.DimensionWeatherProvider`:

| Method | Meaning |
|---|---|
| `String id()` | Unique namespaced provider ID |
| `int priority()` | Provider priority |
| `boolean supports(String dimensionId)` | Whether the provider handles the requested dimension |
| `AtmosphereSnapshot query(WeatherContext context)` | Weather snapshot for the request |

Register with `OSWeather.api().registerDimensionProvider(provider)`. Your provider is responsible for its result, validation and lifecycle. Suitable uses include modded Nether, End, Aether or other addon-specific worlds.

This describes an API interface, not verified compatibility with any particular third-party dimension mod. See [examples](api-examples.md).
