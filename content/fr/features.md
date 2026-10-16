# Fonctionnalités

OS Weather calcule côté serveur les conditions atmosphériques locales de l’Overworld et synchronise des snapshots propres aux joueurs vers les clients.

- **47 scénarios climatiques pondérés** et un moteur de simulation déterministe.
- **Cellules atmosphériques de 512 blocs** avec interpolation spatiale.
- **Mises à jour autour des zones actives** ; le moteur ne force pas le chargement des chunks Minecraft.
- **Persistance de l’atmosphère** restaurée au chargement du monde ; la simulation ne rattrape pas le temps passé hors ligne.
- **États météo** pour la pluie, la neige, le vent, les nuages, le brouillard, les orages, les tempêtes de sable et les blizzards.
- **Overrides visuels et gameplay** avec priorités et handles de libération explicites.
- **API de providers de dimensions** pour les intégrations d’addons.

L’auteur confirme que la v1 beta actuelle est validée. Les commandes vanilla `/weather clear/rain/thunder` sont reliées au mod, sans garantie de compatibilité avec chaque autre mod météo ou graphique. Voir le [statut de sortie](release-status.md).
