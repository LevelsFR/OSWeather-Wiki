# API v1 : exemples d’intégration

> Ces extraits illustrent les signatures API documentées. Rédigés indépendamment, ils ne sont **ni compilés ni testés comme addon prêt à installer** et ne sont pas copiés depuis le code privé.

La révision 1 de l’API ne signifie pas que le mod est en version 1.0 et n’autorise pas la distribution d’une intégration. Aucun JAR API autonome ni coordonnées Maven ne sont publiés ; un addon nécessite une dépendance de compilation autorisée correspondant à la build du mod. Voir la [référence API](api-v1.md) et les [droits](rights.md).

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
