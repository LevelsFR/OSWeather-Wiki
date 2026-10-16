# API v1: Integration examples

> These snippets illustrate the documented API signatures. They were written independently, are **not compiled or tested as a drop-in addon**, and are not copied from the private source.

API revision `1` and the stable mod version `1.0` are independent version numbers. API documentation does not grant permission to distribute an integration. No standalone API JAR or Maven coordinates are currently published; an addon needs an authorized compile-time dependency matching the mod build. See [API reference](api-v1.md) and [rights](rights.md).

## Read gameplay weather
~~~java
import com.ourstory.osweather.OSWeather;
import com.ourstory.osweather.api.weather.WeatherContext;
import com.ourstory.osweather.api.weather.AtmosphereSnapshot;

// Obtain playerUuid, x, y, z and gameTick from your addon context.
WeatherContext context = new WeatherContext(
    "minecraft:overworld", playerUuid, x, y, z, gameTick
);
AtmosphereSnapshot weather = OSWeather.api().gameplayWeather(context);
if (weather.isThundering()) {
    // Run your addon's storm-dependent behavior.
}
~~~

## Create and clean up a visual override
~~~java
import com.ourstory.osweather.OSWeather;
import com.ourstory.osweather.api.override.WeatherOverride;
import com.ourstory.osweather.api.override.OverrideHandle;

WeatherOverride event = new WeatherOverride(
    "youraddon:storm", 0.85f, gameTick + 1200L,
    50, "youraddon:event", true, false
);
OverrideHandle handle = OSWeather.api().setOverride(playerUuid, event);
// Later, when your event ends:
OSWeather.api().releaseOverride(handle);
~~~

## Provide weather for another dimension
~~~java
import com.ourstory.osweather.OSWeather;
import com.ourstory.osweather.api.provider.DimensionWeatherProvider;
import com.ourstory.osweather.api.weather.WeatherContext;
import com.ourstory.osweather.api.weather.AtmosphereSnapshot;

DimensionWeatherProvider provider = new DimensionWeatherProvider() {
    public String id() { return "youraddon:weather"; }
    public int priority() { return 10; }
    public boolean supports(String dimensionId) {
        return "youraddon:world".equals(dimensionId);
    }
    public AtmosphereSnapshot query(WeatherContext context) {
        return AtmosphereSnapshot.CLEAR;
    }
};
OSWeather.api().registerDimensionProvider(provider);
~~~

The final provider must return suitable weather data rather than the placeholder `CLEAR` value. Before distribution, verify lifecycle cleanup, dependency behavior and both loaders, and check the [rights statement](rights.md).

## Run an addon in API-only mode

On the server, set this in `config/osweather-server.toml`:

~~~toml
enabled = false
~~~

In stable release `1.0`, this setting stops OS Weather's built-in Overworld simulation and its periodic weather sync. The public API stays available. A registered provider can then answer queries for `minecraft:overworld`; without a provider, the API starts from clear weather, then applies active overrides. With the built-in simulation enabled, OS Weather remains the Overworld provider. An operator can change the setting in the in-game Server tab without restarting. After editing the TOML directly, run `/osweather reload` as an operator.

The API does not automatically render or synchronize an addon's provider data to clients. The addon must query the API and implement any client presentation or gameplay behavior it needs.

### Register an Overworld provider

Call the registration once from your addon's common initialization:

~~~java
import com.ourstory.osweather.OSWeather;

OSWeather.api().registerDimensionProvider(new ExampleOverworldProvider());
~~~

~~~java
import com.ourstory.osweather.api.provider.DimensionWeatherProvider;
import com.ourstory.osweather.api.weather.AtmosphereSnapshot;
import com.ourstory.osweather.api.weather.WeatherContext;

public final class ExampleOverworldProvider implements DimensionWeatherProvider {
    @Override
    public String id() {
        return "youraddon:overworld_weather";
    }

    @Override
    public int priority() {
        return 10;
    }

    @Override
    public boolean supports(String dimensionId) {
        return "minecraft:overworld".equals(dimensionId);
    }

    @Override
    public AtmosphereSnapshot query(WeatherContext context) {
        // Example fixed rain values; replace these with your addon's weather state.
        return new AtmosphereSnapshot(
            "youraddon:rain",
            "youraddon:example_rain",
            16.0f, 0.80f, 1008.0f,
            0.12f, -0.04f,
            0.90f, 0.70f, 0.0f,
            0.05f, 0.0f, 0.0f, 0.80f,
            context.gameTick()
        );
    }
}
~~~

Query the result wherever your addon needs a snapshot:

~~~java
AtmosphereSnapshot weather = OSWeather.api().visualWeather(context);
~~~

Use `gameplayWeather(context)` for gameplay decisions. Visual and gameplay overrides are applied after the provider result. Keep the provider logic safe for the thread and lifecycle from which your addon queries it.
