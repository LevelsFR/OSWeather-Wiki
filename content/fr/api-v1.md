# Référence API v1

**Package :** `com.ourstory.osweather.api` · **Révision API :** `1` · **Mod documenté :** `0.9.0-beta.10.5` (pré-v1).

La révision de l’API et la version de sortie du mod sont indépendantes. Ces pages décrivent les points d’extension techniques, pas une version stable du mod ni une licence de distribution d’addons.

## Principales entrées

| Type | Rôle |
|---|---|
| `OSWeatherApi` | Interroger la météo visuelle/gameplay, gérer les overrides et enregistrer des providers de dimensions. |
| `WeatherContext` | Contexte de dimension, joueur éventuel, position et tick. Une dimension nulle prend la valeur Overworld. |
| `AtmosphereSnapshot` | Résultat immuable avec identifiants météo/scénario et valeurs atmosphériques. |
| `WeatherOverride` | Définition d’override ; intensité limitée et au moins un mode visuel/gameplay activé. |
| `DimensionProviderRegistry` | Trie les providers par priorité ; une inscription avec le même identifiant remplace la précédente. |

L’API actuelle expose `apiVersion()`, `visualWeather(context)`, `gameplayWeather(context)`, `setOverride(playerUuid, override)`, `releaseOverride(handle)` et `registerDimensionProvider(provider)`. Voir les pages [overrides](api-overrides.md), [dimensions](api-dimensions.md) et [exemples](api-examples.md).

**Distribution :** aucun JAR API autonome ni coordonnées Maven ne sont publiés actuellement. Le dépôt source est privé. Cette référence ne remplace pas une dépendance de compilation autorisée.