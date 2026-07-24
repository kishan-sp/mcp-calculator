import os
import uvicorn
from mcp.server.fastmcp import FastMCP

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


# Option A: If using mcp.run() directly
def main():
    port = int(os.environ.get("PORT", 8000))
    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=port,
        host_origin_protection=False,  # Disables strict Host header filtering for remote hosting
    )


if __name__ == "__main__":
    main()
