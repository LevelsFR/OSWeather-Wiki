# API v1 : exemples d’intégration
> Exemples rédigés à partir des signatures publiques de l’API, **sans copie du code propriétaire**. Ils sont illustratifs et **n’ont pas été compilés ni testés comme addons complets**. Leur publication **ne constitue pas une autorisation juridique de distribuer un addon**.

## Lire la météo gameplay
```java
import com.ourstory.osweather.OSWeather;
import com.ourstory.osweather.api.weather.WeatherContext;
import com.ourstory.osweather.api.weather.AtmosphereSnapshot;

// Récupérer playerUuid, x, y, z et gameTick depuis l'addon.
WeatherContext context = new WeatherContext(
    "minecraft:overworld", playerUuid, x, y, z, gameTick
);
AtmosphereSnapshot weather = OSWeather.api().gameplayWeather(context);
if (weather.isThundering()) {
    // Déclencher la logique orageuse de l'addon.
}
```

## Créer puis libérer un override visuel
```java
import com.ourstory.osweather.OSWeather;
import com.ourstory.osweather.api.override.WeatherOverride;
import com.ourstory.osweather.api.override.OverrideHandle;

WeatherOverride event = new WeatherOverride(
    "youraddon:storm", 0.85f, gameTick + 1200L,
    50, "youraddon:event", true, false
);
OverrideHandle handle = OSWeather.api().setOverride(playerUuid, event);
// Lorsque l'événement se termine :
OSWeather.api().releaseOverride(handle);
```

## Définir la météo d’une autre dimension
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

Remplacer `CLEAR` par un état adapté dans un vrai provider. Vérifier le cycle de vie, les dépendances et les deux loaders. Consulter les [droits](rights.md) avant toute distribution.
