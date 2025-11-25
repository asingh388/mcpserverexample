# Server
from mcp.server.fastmcp import FastMCP

# Create server instance
mcp = FastMCP("Demo")

# Tool to add two numbers
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

# Tool to subtract two numbers
@mcp.tool()
def subtract_numbers(a: int, b: int) -> int:
    """Subtract second number from first number."""
    return a - b

# Tool to multiply two numbers
@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b

# Tool to divide two numbers
@mcp.tool()
def divide_numbers(a: int, b: int) -> float:
    """Divide first number by second number."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b