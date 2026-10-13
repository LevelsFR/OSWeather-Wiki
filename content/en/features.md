# Features
## Server-authoritative atmospheric simulation
The Overworld has an active, local weather model. The server computes weather conditions; clients receive compact snapshots and interpolate transitions.

- **47 climate-weighted scenarios** provide varied conditions constrained by climate.
- **512 × 512-block atmospheric cells**, with spatial blending across cell boundaries.
- **Active-only simulation:** player surroundings evolve without force-loading chunks.
- **Persistence:** atmosphere state can resume when an area becomes active again.
- **Weather effects:** rain, snow, wind, clouds, fog, storms, sandstorms and blizzards are represented by derived state.
- **Overrides:** separate visual and gameplay modifications, priority handling and explicit release handles.
- **Extensions:** providers can serve registered dimensions beyond the Overworld.

## Client presentation
The current beta synchronizes per-player weather and implements transitions and baseline bridges. **Final cloud polish, shaders, dedicated snow/compositor effects, lightning presentation and full runtime validation remain unfinished.** See [release status](release-status.md).

## Vanilla compatibility
Vanilla `/weather` administration requests are bridged to OS Weather overrides. They do not mean all third-party weather or renderer mods have been tested.
