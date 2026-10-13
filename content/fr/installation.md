# Installation

> **Préversion :** la build documentée est `0.9.0-beta.10.5`, pas une v1 stable. Ce dépôt documentaire ne publie aucun binaire du mod. Utilisez uniquement un JAR officiellement transmis par l’auteur.

| Minecraft | Loader | Java | Build/smoke moteur | Runtime en jeu |
|---|---|---:|---|---|
| 1.21.1 | Fabric ou NeoForge | 21 | Réussi | Non testé |
| 26.2 | Fabric ou NeoForge | 25 | Réussi | Non testé |
| 26.3 | Fabric ou NeoForge | 25 | Réussi | Non testé |

La compilation et les smoke tests ont été vérifiés pour la dernière fois le 14 octobre 2026. Une compilation réussie ne garantit pas le démarrage du jeu ni le chargement d’un monde.

## Installation

1. Obtenir le JAR runtime officiel correspondant à la version de Minecraft et au loader.
2. Installer la version correspondante de Fabric ou NeoForge.
3. Sous Fabric, installer Fabric API pour la même version de Minecraft.
4. Placer le JAR runtime dans le dossier `mods/` de l’instance.
5. En multijoueur, utiliser une build correspondante sur le serveur et les clients lorsque nécessaire.

Les paramètres client sont dans `config/osweather-client.toml` ; ceux de la simulation serveur dans le `config/osweather-server.toml` du serveur. Cloth Config/Mod Menu sont des intégrations UI facultatives. N’installez jamais un JAR de sources comme mod. Voir [compatibilité](compatibility.md) et [configuration](configuration.md).