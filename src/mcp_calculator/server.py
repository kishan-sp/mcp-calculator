import os
import uvicorn
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

# Initialize FastMCP
mcp = FastMCP("Calculator Tool")


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


# Option A: Disable DNS rebinding protection (Recommended for public cloud hosting)
mcp = FastMCP(
    "mcp-calculator",
    transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
)

# --- OR ---

# Option B: Explicitly allow your Render hostname
# mcp = FastMCP(
#     "mcp-calculator",
#     transport_security=TransportSecuritySettings(
#         allowed_hosts=["mcp-calculator-fbsb.onrender.com", "localhost:*", "127.0.0.1:*"]
#     )
# )


if __name__ == "__main__":
    main()
