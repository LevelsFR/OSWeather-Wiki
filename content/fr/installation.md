# Installation
> **Attention, préversion :** cette documentation couvre `0.9.0-beta.10.5`. Les six variantes sont configurées et compilables, mais **leur lancement et leur entrée en monde ne sont pas encore entièrement validés**. La disponibilité d’un JAR public n’est pas présumée.

## Prérequis
| Minecraft | Loader | Java |
|---|---|---|
| 1.21.1 | Fabric ou NeoForge | 21 |
| 26.2 | Fabric ou NeoForge | 25 |
| 26.3 | Fabric ou NeoForge | 25 |

### Étapes
1. Récupérer le **JAR officiel distribué** correspondant à Minecraft et au loader.
2. Installer la bonne version de Fabric ou NeoForge.
3. **Fabric :** installer Fabric API compatible.
4. Placer le JAR OS Weather dans le dossier `mods` du client ou du serveur.
5. Lancer le jeu et consulter les logs si le chargement échoue. En multijoueur, installer aussi le mod côté serveur lorsque nécessaire.

### Paramètres
Les paramètres client se trouvent dans `config/osweather-client.toml`. Les paramètres de simulation serveur sont dans `config/osweather-server.toml`, à modifier **sur le serveur**. Sous Fabric, **Cloth Config et Mod Menu sont facultatifs** pour disposer d’une interface de configuration.

Voir [compatibilité](compatibility.md). **Ne pas installer de JAR de sources** à la place du mod.
