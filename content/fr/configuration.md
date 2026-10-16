# Configuration

OS Weather sépare les options de rendu propres au client des paramètres de simulation contrôlés par le serveur. Les deux fichiers TOML se trouvent dans le dossier Minecraft `config/`.

## Client : `osweather-client.toml`

| Clé | Défaut | Rôle |
|---|---:|---|
| `enhanced_clouds` | `true` | Active les changements d’affichage des nuages d’OS Weather. |
| `precipitation` | `true` | Active l’affichage des précipitations du mod. |
| `fog` | `true` | Active les effets de brouillard météo. |
| `particles` | `true` | Active les particules météo. |
| `visual_lightning` | `true` | Active l’affichage visuel des éclairs. |
| `sounds` | `true` | Active les sons météo. |
| `cloud_quality` | `2` | Détail des nuages : 0 faible, 1 moyen, 2 élevé, 3 ultra (limité à 0–3). |

Les options client sont modifiables en jeu si les dépendances facultatives de l’écran de configuration sont installées, ou directement dans le fichier. Sous Fabric, Cloth Config fournit l’écran et Mod Menu, facultatif, son entrée. NeoForge enregistre l’écran lorsque Cloth Config est présent. Aucun de ces mods n’est nécessaire au chargement d’OS Weather. En étant connecté à un serveur OS Weather, un OP peut aussi utiliser la catégorie Serveur dans l’écran Cloth Config.

## Serveur : `osweather-server.toml`

| Clé | Défaut | Rôle |
|---|---:|---|
| `enabled` | `true` | Active la simulation Overworld intégrée et sa synchronisation périodique aux clients. Mettre `false` pour les désactiver tout en conservant l’API publique pour les providers et overrides d’addons. Le mode API seule est inclus dans la sortie stable `1.0`. |
| `local_weather` | `true` | Utilise le comportement météo local/par joueur. |
| `gameplay_weather` | `true` | Active l’intégration météo gameplay. |
| `real_lightning` | `false` | Autorise les éclairs réels uniquement si le gameplay météo est activé et `local_weather=false` ; les impacts sont globaux au monde. |
| `sync_interval_ticks` | `100` | Intervalle des snapshots, limité à 40–1 200 ticks. |
| `sleep_calming_bias` | `0.10` | Biais d’apaisement pendant le sommeil, limité à 0–0,35. |

Le serveur fait autorité. Les réglages effectués en jeu par un OP sont enregistrés sur le serveur et appliqués immédiatement sans redémarrage. Après une modification directe de `osweather-server.toml`, un OP peut lancer `/osweather reload` pour charger et appliquer les changements. Ne publiez jamais une configuration serveur active sans en avoir masqué les informations privées.
