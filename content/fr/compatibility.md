# Matrice de compatibilité

**Mod :** `0.9.0-beta.10.5` (avant la v1) · **Révision API :** `1`  
**Compilation et smoke test moteur vérifiés :** 2026-10-14 · **Runtime vérifié :** non

| Minecraft | Loader | Java | Compilation + smoke test (47 scénarios) | Client/monde/serveur en jeu |
|---|---|---:|---|---|
| 1.21.1 | Fabric | 21 | Réussi | Non testé |
| 1.21.1 | NeoForge | 21 | Réussi | Non testé |
| 26.2 | Fabric | 25 | Réussi | Non testé |
| 26.2 | NeoForge | 25 | Réussi | Non testé |
| 26.3 | Fabric | 25 | Réussi | Non testé |
| 26.3 | NeoForge | 25 | Réussi | Non testé |

Le build utilisait Fabric API `0.116.17+1.21.1`, `0.160.0+26.2`, `0.160.7+26.3` ; et NeoForge `21.1.250`, `26.2.0.88`, `26.3.0.16-beta`, respectivement.

La compilation et les smoke tests **ne prouvent pas** que le client démarre, qu’un monde s’ouvre ou qu’un serveur dédié fonctionne. Testez la combinaison exacte de Minecraft et du loader avant de l’utiliser sur un monde important. Les autres versions ne sont pas déclarées compatibles. Voir le [statut de sortie](release-status.md).