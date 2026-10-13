# Référence API v1
**Namespace :** `com.ourstory.osweather.api` · **Version API :** `1` · **Version du mod :** `0.9.0-beta.10.5`

> Le numéro de l’API évolue indépendamment du mod. Ces signatures décrivent des points d’extension techniques ; **elles ne constituent pas une licence de distribution d’addons**.

## Point d’accès
`com.ourstory.osweather.OSWeather.api()` retourne l’interface `OSWeatherApi` :

| Méthode | Rôle |
|---|---|
| `apiVersion()` | Numéro de l’API |
| `visualWeather(WeatherContext)` | Météo utilisée pour l’affichage |
| `gameplayWeather(WeatherContext)` | Météo utilisée par le gameplay |
| `setOverride(UUID, WeatherOverride)` | Créer un override et son handle |
| `releaseOverride(OverrideHandle)` | Libérer un override |
| `registerDimensionProvider(DimensionWeatherProvider)` | Fournir la météo d’une dimension |

## WeatherContext
Champs : `dimensionId` (String), `playerId` (UUID), `x`, `y`, `z` (double), `gameTick` (long).

## AtmosphereSnapshot
Champs : `weatherId`, `scenarioId`, `temperatureC`, `humidity`, `pressureHpa`, `windX`, `windZ`, `cloudCover`, `precipitation`, `thunder`, `fog`, `sandstorm`, `snow`, `visibility`, `gameTick`.

Helpers : `windSpeed()`, `precipitationType()`, `isRaining()`, `isSnowing()`, `isThundering()`. Types : `NONE`, `RAIN`, `SNOW`.

## Périmètre
Le moteur couvre `minecraft:overworld`. Les autres dimensions passent par des [providers](api-dimensions.md). Utiliser les packages publics `api`, pas les implémentations `internal` ou propres aux loaders.

Voir les [exemples](api-examples.md) et les [overrides](api-overrides.md).
