import os
import uvicorn
from mcp.server.fastmcp import FastMCP

# 1. Initialize FastMCP server
mcp = FastMCP("Calculator Tool")


# 2. Add Calculator Tools
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
    """Divides a by b. Raises error on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# 3. Entrypoint configured for Render deployment
def main():
    # Render automatically sets the PORT environment variable (defaults to 8000 locally)
    port = int(os.environ.get("PORT", 8000))

    # Run the server with SSE transport over HTTP
    mcp.run(
        transport="sse",
        host="0.0.0.0",  # Required for Render to route external traffic
        port=port,
    )


if __name__ == "__main__":
    main()
