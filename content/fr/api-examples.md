# API v1 : exemples d’intégration

> Ces extraits illustrent les signatures API documentées. Rédigés indépendamment, ils ne sont **ni compilés ni testés comme addon prêt à installer** et ne sont pas copiés depuis le code privé.

La révision 1 de l’API ne signifie pas que le mod est en version 1.0 et n’autorise pas la distribution d’une intégration. Aucun JAR API autonome ni coordonnées Maven ne sont publiés ; un addon nécessite une dépendance de compilation autorisée correspondant à la build du mod. Voir la [référence API](api-v1.md) et les [droits](rights.md).

## Lire la météo gameplay
~~~java
import com.ourstory.osweather.OSWeather;
import com.ourstory.osweather.api.weather.WeatherContext;
import com.ourstory.osweather.api.weather.AtmosphereSnapshot;

// Récupérer playerUuid, x, y, z et gameTick depuis le contexte de l'addon.
WeatherContext context = new WeatherContext(
    "minecraft:overworld", playerUuid, x, y, z, gameTick
);
AtmosphereSnapshot weather = OSWeather.api().gameplayWeather(context);
if (weather.isThundering()) {
    // Déclencher la logique orageuse de l'addon.
}
~~~

## Créer puis libérer un override visuel
~~~java
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
~~~

## Définir la météo d’une autre dimension
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

Remplacer `CLEAR` par un état adapté dans un vrai provider. Vérifier le cycle de vie, les dépendances et les deux loaders. Consulter les [droits](rights.md) avant toute distribution.

## Utiliser un addon en mode API seule

Sur le serveur, définir cette option dans `config/osweather-server.toml` :

~~~toml
enabled = false
~~~

Redémarrer le serveur après le changement. Dans une build qui inclut le mode API seule, cela arrête la simulation Overworld intégrée et sa synchronisation météo périodique. L’API publique reste disponible. Un provider enregistré peut alors répondre aux requêtes pour `minecraft:overworld`; sans provider, l’API part d’une météo claire puis applique les overrides actifs. Si la simulation intégrée reste activée, OS Weather reste le provider de l’Overworld.

L’API ne rend pas et ne synchronise pas automatiquement les données du provider d’un addon vers les clients. L’addon doit interroger l’API et implémenter lui-même les effets visuels ou gameplay souhaités. Ce mode est disponible uniquement dans les builds qui incluent la modification API seule ; vérifier les notes de la build installée.

### Enregistrer un provider Overworld

Appeler cet enregistrement une fois depuis l’initialisation commune de l’addon :

~~~java
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
        // Exemple de pluie fixe ; remplacer par l’état météo de l’addon.
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

Interroger le résultat lorsque l’addon a besoin d’un snapshot :

~~~java
AtmosphereSnapshot weather = OSWeather.api().visualWeather(context);
~~~

Utiliser `gameplayWeather(context)` pour les décisions gameplay. Les overrides visuels et gameplay sont appliqués après le provider. Adapter le provider au thread et au cycle de vie depuis lesquels l’addon l’interroge.
