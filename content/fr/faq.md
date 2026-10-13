# Questions fréquentes
## OS Weather est-il open source ?
**Non.** Le mod et son code restent privés, propriétaires et **All Rights Reserved**. Ce dépôt contient la documentation et les signalements publics.

## Est-ce une version stable ?
**Non.** La version documentée est `0.9.0-beta.10.5`, encore candidate avant la v1.

## Pourquoi parle-t-on d’API v1 ?
Le numéro de l’API est **1** et évolue indépendamment du mod, qui n’est pas encore en version **1.0 stable**.

## Minecraft 26.3 est-il totalement validé ?
C’est une cible de compilation avec tests du moteur documentés. **La validation complète en jeu reste à effectuer** comme sur les autres variantes.

## Et le Nether ou l’End ?
Le moteur intégré s’occupe de l’Overworld. Des addons **peuvent implémenter un provider** pour d’autres dimensions, sans garantie de compatibilité déjà testée.

## Cloth Config et Mod Menu sont-ils obligatoires sur Fabric ?
**Non.** Ils servent à afficher les paramètres client dans une interface. Le fichier de configuration fonctionne sans eux. Fabric API reste nécessaire.

## Mon addon peut-il utiliser cette API ?
Les points d’intégration techniques sont décrits. **Une permission juridique de distribuer des intégrations tierces n’a pas encore été explicitement publiée.** Voir les [droits](rights.md).

## Comment signaler un bug ?
Utiliser les [formulaires Issues](https://github.com/LevelsFR/OSWeather-Wiki/issues/new/choose) avec les versions, la reproduction et des logs expurgés.
