# Statut de sortie avant la v1

**Snapshot :** mod `0.9.0-beta.10.5` ; révision de l’API `1`. Le mod **n’est pas une version stable 1.0**.

## Vérifié localement le 14 octobre 2026

- `gradlew assembleAllVersions --no-daemon --max-workers=1` s’est terminé avec succès.
- Les six cibles configurées ont été assemblées : 1.21.1, 26.2 et 26.3 sous Fabric et NeoForge.
- Le `coreSmoke` de chaque cible a réussi sur **47 scénarios**.

## Pas encore vérifié

- Les tâches Gradle `test` ont été ignorées par la tâche agrégée.
- Aucun lancement du client Minecraft, entrée en monde, test multijoueur ou lancement serveur dédié n’a été effectué.
- Le rendu en jeu, les shaders/packs de ressources, le réseau en situation réelle, les performances serveur et l’interface de configuration restent à tester.
- Le code client généré pour 26.3 a émis une note de dépréciation. Son impact runtime n’est pas établi.
- Aucun JAR téléchargeable officiel ni artefact Maven d’API autonome n’est publié depuis ce dépôt documentaire.

Ces résultats prouvent **la compilation et les smoke tests déterministes du moteur seulement**, pas la compatibilité complète en jeu ni la préparation à la publication. Voir la [matrice de compatibilité](compatibility.md).