# Configuration
OS Weather sépare le rendu local et la simulation contrôlée par le serveur.

| Fichier | Emplacement | Rôle |
|---|---|---|
| `osweather-client.toml` | `config/` côté client | Préférences graphiques et sonores |
| `osweather-server.toml` | `config/` côté serveur | Règles de simulation et gameplay |

## Options client
Les préférences comprennent les nuages et leur qualité, les précipitations, le brouillard, les particules, les éclairs visuels et les sons météo. Certains effets ne sont pas encore finalisés dans cette bêta.

Sur **Fabric**, Cloth Config et Mod Menu, facultatifs, offrent une interface en jeu. Sans eux, modifier directement le fichier client.

## Paramètres serveur
**Le serveur fait autorité.** La configuration locale d’un joueur ne remplace pas les règles météo serveur. Modifier le fichier côté serveur, puis redémarrer si nécessaire. **Le rechargement à chaud n’est pas encore validé comme complet.**

Ne partagez jamais de fichiers de configuration réels contenant des informations privées.
