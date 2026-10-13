# Commandes

Les commandes sont enregistrées sous `/osweather`. Le niveau de permission **2** est requis pour `debug`, `reload`, `set` et `clear`.

| Commande | Comportement réel |
|---|---|
| `/osweather status` | Affiche le résumé météo actuel de l’appelant dans l’Overworld. Nécessite un joueur. |
| `/osweather info` | Alias de `status` ; affiche le même résumé. |
| `/osweather debug` | Même résumé que `status`, protégé par le niveau 2 ; ce n’est pas un rapport de diagnostic distinct. |
| `/osweather set <weather> [player [seconds]]` | Applique un override de commande visuel et gameplay. Cible l’appelant par défaut et dure 600 secondes. Durée : 1 à 86 400 secondes. |
| `/osweather clear [player]` | Libère uniquement l’override créé par `/osweather set` pour l’appelant ou le joueur indiqué. |
| `/osweather reload` | **Ne recharge pas** la configuration ; indique à l’administrateur de redémarrer le serveur après avoir modifié ses paramètres. |

Exemples : `/osweather set rain`, `/osweather set osweather:heavy_snow Alex 300`, `/osweather clear Alex`.

Un identifiant sans namespace est converti en minuscules et préfixé par `osweather:`. L’argument secondes ne peut suivre qu’un argument joueur. Les commandes visant un joueur nécessitent un contexte joueur, sauf si une cible est fournie explicitement.

Les demandes vanilla `/weather clear`, `rain` et `thunder` sont reliées à OS Weather. Cela ne garantit pas la compatibilité avec tous les mods météo tiers. Voir le [support](support.md) pour préparer un rapport de bug.