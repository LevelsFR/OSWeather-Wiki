# Référence API v1

**Package :** `com.ourstory.osweather.api` · **Révision API :** `1` · **Version stable du mod :** `1.0` (V1 stable).

La révision de l’API et la version de sortie du mod sont indépendantes. La version stable V1 du mod est `1.0` ; l’API reste à la révision `1`. Ces pages décrivent des points d’extension techniques, pas une licence de distribution d’addons.

## Principales entrées

| Type | Rôle |
|---|---|
| `OSWeatherApi` | Interroger la météo visuelle/gameplay, gérer les overrides et enregistrer des providers de dimensions. |
| `WeatherContext` | Contexte de dimension, joueur éventuel, position et tick. Une dimension nulle prend la valeur Overworld. |
| `AtmosphereSnapshot` | Résultat immuable avec identifiants météo/scénario et valeurs atmosphériques. |
| `WeatherOverride` | Définition d’override ; intensité limitée et au moins un mode visuel/gameplay activé. |
| `DimensionWeatherProvider` | Interface publique d’extension pour la météo d’une autre dimension. |

Le registre des providers est un détail d’implémentation interne. Enregistrez les providers avec `OSWeatherApi` ; ne dépendez pas des classes internes.

L’API publique expose `apiVersion()`, `visualWeather(context)`, `gameplayWeather(context)`, `setOverride(playerUuid, override)`, `releaseOverride(handle)` et `registerDimensionProvider(provider)`. Voir les pages [overrides](api-overrides.md), [dimensions](api-dimensions.md) et [exemples](api-examples.md).

**Distribution :** aucun JAR API autonome ni coordonnées Maven ne sont publiés. Le dépôt source reste privé. Cette référence ne remplace pas une dépendance de compilation autorisée.
