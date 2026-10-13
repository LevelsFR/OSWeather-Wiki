# API v1 : providers de dimensions
Le moteur intégré couvre uniquement `minecraft:overworld`. Les autres dimensions utilisent un registre de providers.

## DimensionWeatherProvider
Implémenter l’interface publique `com.ourstory.osweather.api.provider.DimensionWeatherProvider` :

| Méthode | Fonction |
|---|---|
| `String id()` | Identifiant unique avec namespace |
| `int priority()` | Priorité du provider |
| `boolean supports(String dimensionId)` | Indique si la dimension est gérée |
| `AtmosphereSnapshot query(WeatherContext context)` | Retourne l’état météorologique |

Enregistrer le provider avec `OSWeather.api().registerDimensionProvider(provider)`. Il doit gérer son résultat, ses vérifications et son cycle de vie. Exemples d’extensions possibles : Nether, End, Aether ou dimensions spécifiques à d’autres mods.

**Attention :** cette interface ne garantit pas une compatibilité testée avec un mod de dimension donné. Voir [exemples](api-examples.md).
