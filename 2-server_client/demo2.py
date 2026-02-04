# FastMCP HTTP Server and Client Example - Part 2/4
'''
Need a simple way to expose Python functions so AI Models can call like tools?
'''

# This imports "FastMCP", the core class for creating AI-callable tools. It bridges Python functions to AI
# models by exposing them as strucutured tools woth type hints and doscstring defining schema.
from fastmcp import FastMCP

# This initializes the FastMCP server isntance, the central coordinator for all AI-callable tools. The string
# parameter "My MCP Server" identifies this isntance ins logs and erros messages, enabling traceability across
# distributed systems.
mcp = FastMCP("My MCP Server")

# The "mcp.too" decorator registers this function as an AI-callable tool. It Converts Python type hints and
# docsstring into a structured schema tha AI models use to understand and invoke the function. This is
# FASTMCSP's core pattern for exposing capabilities to AI systems.
@mcp.tool
# This defines an AI-callable tool function whith strict hints. The "name:str" parameter enforces string
# input, while the "-> str" return annotation guarantees string output, ensring predictable behavior for AI
# integration. FastMCP use these type hints to auto-generate the tool's schema and validate calls. 
def greet(name:str) -> str:
  return f"Hello {name}"

