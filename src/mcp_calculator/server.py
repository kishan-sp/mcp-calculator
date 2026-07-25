import os

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

# Single FastMCP instance. DNS rebinding protection stays ON; we explicitly
# allowlist the real deployed hostname (plus localhost, for local testing)
# instead of disabling the protection outright.
mcp = FastMCP(
    "mcp-calculator",
    transport_security=TransportSecuritySettings(
        allowed_hosts=[
            "mcp-calculator-fbsb.onrender.com",
            "localhost:*",
            "127.0.0.1:*",
        ]
    ),
)


@mcp.tool()
def add(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divides a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main() -> None:
    """Entry point used by the `start-calculator` script (see pyproject.toml).

    Runs over streamable HTTP so it can be deployed on Render. Render sets
    the PORT env var; we bind to 0.0.0.0 so the platform can route to it.
    """
    port = int(os.environ.get("PORT", 8000))
    mcp.settings.host = "0.0.0.0"
    mcp.settings.port = port
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()