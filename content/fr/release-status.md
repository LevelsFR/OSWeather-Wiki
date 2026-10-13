# Statut avant la v1
**Version documentée :** `0.9.0-beta.10.5`. Il ne s’agit **pas d’une v1 stable**.

## Implémenté et vérifié localement
- Moteur atmosphérique Java déterministe avec persistance
- 47 scénarios climatiques et interpolation sur des cellules de 512 blocs
- Simulation active sans forcer le chargement des chunks
- Overrides avec priorités, provenance et handles de libération
- API v1 et registre de providers pour d’autres dimensions
- Modèle de snapshots météo par joueur et base des transitions client
- Six variantes configurées, avec compilation et smoke tests déterministes documentés

## À vérifier avant une v1 publique
- Lancement et entrée en monde sur les six variantes
- Tests sur serveur dédié avec plusieurs joueurs et mesure des performances
- Shaders, packs de ressources et nouvelles API de rendu
- Finitions brouillard, sable, blizzard, neige et effets d’éclairs
- Finitions graphiques et rechargement à chaud de la configuration

**Une compilation et des tests unitaires ne prouvent pas la stabilité en jeu.** Voir [compatibilité](compatibility.md).
