# Fonctionnalités

OS Weather calcule côté serveur les conditions atmosphériques locales de l’Overworld et synchronise des snapshots propres aux joueurs vers les clients.

- **47 scénarios climatiques** et un moteur de simulation déterministe.
- **Cellules atmosphériques de 512 blocs** avec interpolation spatiale.
- **Mises à jour autour des zones actives** ; le moteur ne force pas le chargement des chunks Minecraft.
- **Persistance de l’atmosphère** et rattrapage du temps écoulé.
- **États météo** pour pluie, neige, vent, nuages, brouillard, orages, tempêtes de sable et blizzards.
- **Overrides visuels et gameplay** avec priorités et handles de libération explicites.
- **API de providers de dimensions** pour les intégrations d’addons.

Le code et les smoke tests moteur ne constituent pas une validation complète en jeu. Les finitions de rendu, effets spécialisés, shaders/packs de ressources, présentation des éclairs et comportement runtime restent des étapes de sortie. Les commandes vanilla `/weather clear/rain/thunder` sont reliées au mod, sans garantie de compatibilité avec chaque autre mod météo ou graphique. Voir le [statut de sortie](release-status.md).