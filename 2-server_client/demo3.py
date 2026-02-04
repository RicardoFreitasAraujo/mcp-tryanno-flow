# FastMCP HTTP Server and Client Example - Part 3/4

'''
A working AO tool server in just 6 liens of code-no complex routing or protocol handling required.
'''

# This imports "FASTMCP", the core for craeting AI-callable tools with default STDIO transport. It
# bridges Python funcions to AI models through decorators, handling serialization, validation, and execution
# while supporting HTTP and SSE trnasports for web service. The server can also be managed via CLI or
# composed with FASTAPI/Starlette apps dor comples deployments.
from fastmcp import FastMCP

# Initializes the FastMCP server instance with STDIO as the default trnasport. The server name paramater is 
# optional and primarily used for debuggind contest, while HTTP transport is recommended for web services.
# This instance becomes the central registry for all API-callable tools and resources, with support for
# composition with ohter servrs via the "mount()" method.
mcp = FastMCP("My MCP Server")

# The "@mcp.tool" decorator this Python function as an AI-callable endpoint isn FAstMCP. it generates
# an OpenAPI schema from type hints ans docstrings, handles serailziation/deserialziation, and routes calls
# over the default STDIO trnasport or optional HTTP/Server-Sent Events transports.
# 
# This is the primary pattern for creating tools that AI models can discover an invoke, with built-in
# valdiation and automatic registration in the FastMCP server. 
@mcp.tool
def greet(name:str) -> str:
  return f"Hello, {name}"

if (__name__ == "__main__"):
  mcp.run()

