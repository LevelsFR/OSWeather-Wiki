# Commands

All listed commands are registered under `/osweather`. Permission level **2** is required for `debug`, `reload`, `set` and `clear`.

| Command | Actual behavior |
|---|---|
| `/osweather status` | Shows the caller's current Overworld weather summary. Requires a player context. |
| `/osweather info` | Alias for `status`; it prints the same summary. |
| `/osweather debug` | Same summary as `status`, gated at permission level 2; it is not a separate diagnostics dump. |
| `/osweather set <weather> [player [seconds]]` | Applies a visual and gameplay command override. Defaults to the caller and 600 seconds. Duration is 1–86,400 seconds. |
| `/osweather clear [player]` | Releases only the active `/osweather set` command override for the caller or named player. |
| `/osweather reload` | Reloads `osweather-server.toml` and applies its settings immediately without restarting the server. Requires permission level 2. |

Examples: `/osweather set rain`, `/osweather set osweather:heavy_snow Alex 300`, `/osweather clear Alex`.

A weather id without a namespace is lowercased and prefixed with `osweather:`. The optional seconds argument can only follow a player argument. The commands that operate on a player need a player context unless an explicit player is supplied.

Vanilla `/weather clear`, `rain` and `thunder` requests are bridged into OS Weather. This does not establish compatibility with every third-party weather mod. See [support](support.md) for bug-report details.