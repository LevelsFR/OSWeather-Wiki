# Configuration
OS Weather separates local client presentation from server-owned simulation.

| File | Location | Responsibility |
|---|---|---|
| `osweather-client.toml` | `config/` on the client | Visual and audio preferences |
| `osweather-server.toml` | `config/` on the server | Simulation/gameplay weather settings |

## Client controls
Client-facing controls include cloud rendering/quality, precipitation, fog, particles, visual lightning and weather sounds. Availability/polish of individual effects depends on the beta status.

On **Fabric**, optional Cloth Config and Mod Menu expose an in-game settings UI. Without these optional mods, edit the client file directly.

## Server controls
The **server is authoritative**. Changing a local client file cannot override server gameplay rules. Edit the server configuration on the server and restart if necessary. **Hot reload is not yet claimed complete or validated** in this prerelease.

Do not publish real production configuration files or private endpoint details when reporting issues.
