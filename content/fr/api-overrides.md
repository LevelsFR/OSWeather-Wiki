# API v1 : overrides météo
Les overrides remplacent temporairement certains comportements météo sans modifier la simulation atmosphérique.

## Champs de WeatherOverride
| Champ | Type | Rôle |
|---|---|---|
| `weatherId` | String | Identifiant météo avec namespace |
| `intensity` | float | Intensité, limitée à 0..1 |
| `expiresAtTick` | long | Tick d’expiration ; `-1` sans expiration |
| `priority` | int | La priorité la plus forte gagne |
| `source` | String | Identifiant de l’addon ou de l’événement |
| `visual` | boolean | Affecte l’affichage |
| `gameplay` | boolean | Affecte le gameplay |

Au moins un indicateur `visual` ou `gameplay` doit être `true`. À priorité égale, l’override créé le plus récemment l’emporte. Un UUID cible un joueur ; `null` cible tous les joueurs. Une priorité supérieure permet à un override individuel de prendre le dessus.

## Cycle de vie
Appeler `OSWeather.api().setOverride(playerUuid, override)`, **conserver son `OverrideHandle`**, puis appeler `releaseOverride(handle)` lorsque l’effet se termine.

Voir les [exemples](api-examples.md).
