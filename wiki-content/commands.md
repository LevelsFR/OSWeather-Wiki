# Commands
OS Weather exposes an `/osweather` command family for server administration and inspection.

| Command path | Purpose |
|---|---|
| `/osweather status` | Overview of the current state |
| `/osweather info` | Detailed atmospheric information |
| `/osweather debug` | Debug/diagnostics |
| `/osweather set` | Request a weather override |
| `/osweather clear` | Clear an active override |
| `/osweather reload` | Configuration reload entry point |

**Note:** Exact arguments and permission requirements can differ by build; inspect in-game command suggestions. The prerelease does **not** claim fully implemented hot configuration reload.

## Vanilla commands
Vanilla `/weather clear`, `/weather rain` and `/weather thunder` are bridged to OS Weather overrides, including administrative takeover semantics.

For troubleshooting, include exact command arguments, Minecraft version, loader and mod version in your [bug report](support.md).
