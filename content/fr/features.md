# Fonctionnalités
## Simulation atmosphérique côté serveur
L’Overworld bénéficie d’une météo locale. Le serveur calcule les conditions ; chaque client reçoit des états synchronisés et réalise des transitions fluides.

- **47 scénarios climatiques** pondérés selon l’environnement.
- **Cellules de 512 × 512 blocs** et interpolation spatiale pour éviter les frontières nettes.
- **Simulation uniquement dans les zones actives**, sans chargement forcé des chunks.
- **Persistance** de l’état atmosphérique lorsque les joueurs reviennent.
- **États calculés** pour la pluie, la neige, le vent, les nuages, le brouillard, les orages, les tempêtes de sable et les blizzards.
- **Overrides** visuels et gameplay indépendants, avec priorités et libération explicite.
- **Providers** pour permettre à des addons de gérer la météo d’autres dimensions.

## Affichage client
La bêta comprend la synchronisation individuelle et des transitions visuelles. **Les finitions du rendu des nuages, les shaders, les effets spécialisés et la validation complète en jeu restent à réaliser.** Voir [statut](release-status.md).

## Compatibilité vanilla
Les commandes vanilla `/weather` sont reliées aux overrides d’OS Weather. Cela ne garantit pas une compatibilité testée avec tous les mods graphiques.
