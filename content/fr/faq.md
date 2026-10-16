# FAQ

## La sortie stable V1 est-elle prête ?
Oui. L’auteur confirme qu’OS Weather est prêt pour la version stable `1.0`. CurseForge ne liste actuellement que l’ancienne beta pour Minecraft 1.21.1 sous NeoForge ; voir le [statut de sortie](release-status.md) pour distinguer la préparation de la release de la disponibilité des fichiers.

## Quelles versions de Minecraft et quels loaders sont pris en charge par la V1 stable ?
La matrice V1 stable couvre Minecraft 1.21.1, 26.2.x et 26.3.x sous Fabric et NeoForge. CurseForge indique les JAR stables effectivement publiés ; voir la [page de compatibilité](compatibility.md).

## Où télécharger le mod ?
Téléchargez le JAR d’exécution stable `1.0` correspondant à votre version de Minecraft et à votre loader sur [CurseForge](https://www.curseforge.com/minecraft/mc-mods/os-weather). Si le fichier stable pour votre cible n’y est pas listé, il n’est pas encore disponible. Ce dépôt documentaire n’héberge pas le binaire du mod.

## La révision 1 de l’API est-elle le même numéro que la version 1.0 du mod ?
Non. La révision API et la version du mod sont indépendantes. La version stable du mod est `1.0` et l’API est à la révision `1`.

## Le mod gère-t-il les dimensions hors Overworld ?
La simulation intégrée gère l’Overworld. L’API expose un point d’extension pour les providers de dimensions, sans garantir la compatibilité avec un addon ou mod de dimension particulier.

## Cloth Config ou Mod Menu sont-ils obligatoires ?
Non. Ce sont des intégrations facultatives pour l’écran de configuration lorsqu’elles sont prises en charge. Les fichiers TOML restent utilisables sans elles ; voir [configuration](configuration.md).

## Puis-je distribuer un addon utilisant l’API ?
Les pages API décrivent des points d’intégration techniques, pas une autorisation juridique. Demandez une autorisation écrite si nécessaire ; voir [droits](rights.md).

## Où signaler un bug ?
Utilisez les [formulaires publics](https://github.com/LevelsFR/OSWeather-Wiki/issues/new/choose) et joignez les versions exactes, des étapes de reproduction et des logs expurgés.
