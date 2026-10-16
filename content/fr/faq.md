# FAQ

## OS Weather est-il une version stable ?
Le build public actuel est `1.0-beta`, pas une version finale stable `1.0`. L’auteur confirme que la v1 beta pour Minecraft 1.21.1 est validée. Voir le [statut de sortie](release-status.md).

## Quelle version de Minecraft et quel loader sont ciblés par le fichier actuel ?
Le fichier public CurseForge cible Minecraft 1.21.1 sous NeoForge. Les autres versions de Minecraft et loaders ne sont pas couverts par ce fichier ; voir la [page de compatibilité](compatibility.md).

## Où télécharger le mod ?
Téléchargez le JAR d’exécution actuel sur [CurseForge](https://www.curseforge.com/minecraft/mc-mods/os-weather). Ce dépôt documentaire n’héberge pas le binaire du mod.

## La révision 1 de l’API signifie-t-elle que le mod est une version stable 1.0 ?
Non. La révision de l’API est indépendante de la version du mod. Le build actuel est `1.0-beta`.

## Le mod gère-t-il les dimensions hors Overworld ?
La simulation intégrée gère l’Overworld. L’API expose un point d’extension pour les providers de dimensions, sans garantir la compatibilité avec un addon ou mod de dimension particulier.

## Cloth Config ou Mod Menu sont-ils obligatoires ?
Non. Ce sont des intégrations facultatives pour l’écran de configuration lorsqu’elles sont prises en charge. Les fichiers TOML restent utilisables sans elles ; voir [configuration](configuration.md).

## Puis-je distribuer un addon utilisant l’API ?
Les pages API décrivent des points d’intégration techniques, pas une autorisation juridique. Demandez une autorisation écrite si nécessaire ; voir [droits](rights.md).

## Où signaler un bug ?
Utilisez les [formulaires publics](https://github.com/LevelsFR/OSWeather-Wiki/issues/new/choose) et joignez les versions exactes, des étapes de reproduction et des logs expurgés.
