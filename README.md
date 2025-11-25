The config below defines the servers used and basic instructions to start them.

The repository uses a JSON structure like this:
``` json
{
    "mcpServers": {
        "mcpserverexample": {
            "command": "uvx",
            "args": [
                "--from",
                "git+https://github.com/asingh388/mcpserverexample.git",
                "mcp-server"
            ]
        }
    }
}
```