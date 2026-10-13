# API v1: Integration examples
> These snippets were independently authored from the documented API signatures. They are **illustrative**, not compiled/tested drop-in addons. They are not copied from the proprietary source. Publishing them **does not grant an addon distribution license**.

## Read gameplay weather
```java
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
```

## Create and clean up a visual override
```java
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
```

## Provide weather for another dimension
```java
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
```

The final provider must return suitable weather data rather than the placeholder `CLEAR` value. Before distribution, verify lifecycle cleanup, dependency behavior and both loaders, and check the [rights statement](rights.md).
