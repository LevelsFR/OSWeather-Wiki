# Pre-v1 release status
**Documented snapshot:** `0.9.0-beta.10.5`. This is **not a stable v1 release**.

## Implemented and locally validated
- Deterministic pure-Java atmosphere core and persistence
- 47 climate-weighted scenarios; spatial interpolation over 512-block cells
- Active-area simulation without forced chunk loading
- Priority/source-aware overrides and their release handles
- API v1 and dimension-provider registration
- Per-player weather snapshot model and client interpolation baseline
- Six configured build variants with documented compilation and deterministic core smoke checks

## Pending runtime and release gates
- Launch client and enter a world on each of the six targets
- Test dedicated servers and realistic player-load performance
- Verify shader/resource-pack combinations and new rendering APIs
- Finish specialized fog, sandstorm, blizzard, snow rendering and lightning presentation
- Validate remaining renderer polish and hot configuration reload

**Do not interpret compilation and smoke tests as runtime validation.** See the [compatibility matrix](compatibility.md).
