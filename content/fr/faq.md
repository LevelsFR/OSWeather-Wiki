# FAQ

## OS Weather est-il une v1 stable ?
Non. Le mod documenté est en version pré-v1 `0.9.0-beta.10.5`. **La révision 1 de l’API ne signifie pas que le mod est en version 1.0.**

## Qu’est-ce qui a réellement été testé ?
Le 14 octobre 2026, les six cibles Minecraft/loader configurées ont été assemblées et chaque smoke test déterministe du moteur a réussi sur 47 scénarios. Aucun runtime client, entrée en monde, multijoueur ou serveur dédié n’a été validé. Voir le [statut de sortie](release-status.md).

## Minecraft 26.3 est-il entièrement pris en charge ?
C’est une cible de build configurée qui compile et réussit le smoke test moteur. Le fonctionnement en jeu reste à vérifier.

## Peut-on télécharger le mod ici ?
Non. Ce dépôt documentaire ne publie aucun binaire. N’installez qu’un JAR distribué officiellement par l’auteur.

## Le mod gère-t-il les dimensions hors Overworld ?
La simulation intégrée gère l’Overworld. L’API expose un point d’extension pour les providers de dimensions, mais cela ne prouve pas qu’un addon ou une dimension particulière ait été testé.

## Cloth Config et Mod Menu sont-ils obligatoires ?
Non. Ce sont des intégrations facultatives pour l’écran de configuration. Les fichiers TOML restent utilisables sans eux ; voir [configuration](configuration.md).

## Puis-je distribuer un addon utilisant l’API ?
Les pages API décrivent des points d’intégration techniques, pas une autorisation juridique. Les conditions de distribution d’intégrations tierces ne sont pas encore publiées explicitement ; demandez une autorisation écrite si nécessaire. Voir [droits](rights.md).

## Où signaler un bug ?
Utilisez les [formulaires publics](https://github.com/LevelsFR/OSWeather-Wiki/issues/new/choose) et joignez les versions exactes, des étapes de reproduction et des logs expurgés.