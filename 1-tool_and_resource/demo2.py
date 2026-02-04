#FastMCP Tools and Resources Example - Part 2/2

'''
Need to search documentation form directyl inside your Python code?

You'll see how FastMCP's client lets you query its own documentation server with a single async call. We'll
connect to the live FaSTMcp docs, execute a search tool, and print results-all in under 10 lines of
code.
'''

# Import Pythons builtin "asyncio" library, enabling asynchronous I/O operations. This is required for the
# "async/await" syntax used throughout the script and for running the async "main()" function. Without it,
# the FastMCP client's non-blocking network calls would't work. 
import asyncio
# This improts the "Client" class form fastmacp, the primary interface for conencting to MCP servers. It
# handles authentication, connection pooling, and request serialization under the hood.
from fastmcp import Client

# Defines na async entry point. This is the standard pattern for async scripts, allowing "await" usage
# inside. The function name "main" is conventional for the primary execution coroutine.
async def main():
  
  # This uses an async context manager to handle FastMCP client connection. The pattern guarantess proper
  # resource cleanup when the block exits, preveting connection leaks. All MCP client interactions should use
  # this pattern for reliable connection lifecycle managment.
  async with Client("https://gofastmcp.com/mcp") as client:

    # This invoke the "SearchFastMcp" tools asynchronously, passing the query aurgments. The "await" ensures the
    # class complete before proceeding, handling the async operation property whithin the context manager's scope.
    result = await client.call_tool(
      # This specifies wich FastMCP tools to execute. The name must exactly match a registered tool on the server,
      # ensuting the correct function gets called with provided arguments.
      name="SearchFastMcp",
      # This passes the query string as tools argument in dictionary format. FastMCP tools expect structured input
      # this way, with the dictionary keys the tool's parameter nbames. The patten ensures type safety and
      # explicit parameter passing between client and server.
      arguments={"query":"deploy a FastMCP server"}
    )
  # Output te tool's response
  print(result)  

# Thos boots the async event loop and executes "main()", the entry point for our async operations. Without
# "asyncio.run()", the coroutine would never execute, as Python doesn't autmatically start async contexts.
# It's the standard pattern for running top-level async code in scripts.
asyncio.run(main())

'''
This demonstrate the client-server pattern for AI tool integration using tho Model Contecxt Protocol. The
code shows how a Python client can remotely invoke tools exposed by an MCS server, abstracting the network
communication behind a simple async interface. Whats makes this distinctive is the seamless  bridge between
local python code and distributed AI capabilities, eith the protocol handling serialization, transport ans 
discovery automatically

The pattern works by establishing a clean separation between tool consumers and providers. Clients interact
with tools through a standardized interface tha hides implementation details, while server expose 
functionality through declarative tool definitions. This design enalbes loose coupling, where clientes only
nedd to know the tool name and input schema, not the server's location, technology stack, or iternal
workflow.

This approach solves the integration complexity of conencting AI moels to backend systems. It eliminates
the need for custom Api clientes, manual request handling, or protocol-specific code, while maintaining type
safety through Python's native type hints. The pattern is partcullary valuable when building LLM
applications that need to interact with multiple tools across different services, or when you wany to
expose existing Python functions to AI system without rewriting them as HTTP APIs.
'''

