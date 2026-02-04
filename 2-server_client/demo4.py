# FastMCP HTTP Server and Client Example - Part 4/4

"""
Your FastMCP server is ready-now let's actually use it. This example cuts through the noise to show the 
minimal code needed for a Python client to call remote tools.

We'll connect to a running MCP server, execute a tool with a single argument, and handle the response-all 
while letting FastMCP manage the transport layer automatically. The async pattern ensures non-blocking execution, 
and the context manager guarantees clean connection handling, even with HTTP's connection pooling.
"""

# Imports asyncio`, Python's standard library for asynchronous programming. This enables the async/await '
# pattern required for FastMCP's non-blocking client operations, particularly over HTTP transport which is 
# automatically inferred from the URL parameter.
import asyncio

# This imports the `Client` class, FastMCP's high-level interface for remote tool invocation. The Client 
# handles protocol operations while delegating actual connection management to the Transport layer, 
# with automatic transport inference from the URL parameter-HTTP in this case.
from fastmcp import Client


# Creates a FastMCP client instance configured for HTTP transport, automatically inferred from the localhost URL. 
# This client manages all protocol operations while delegating connection handling to the separate
# Transport layer, enabling clean separation of concerns. The base URL assumes the MCP server runs locally 
# on port 8000 with the `/mcp` route prefix.
client = Client("http://localhost:8000/mcp")

# Defines an async function `call_tool` that takes a string parameter for tool invocation. The Client 
# automatically infers HTTP transport from the URL parameter, handling protocol operations while the 
# underlying Transport layer manages the actual connection. This pattern enables non-blocking RPC calls to 
# existing FastMCP tools with automatic connection cleanup via the context manager.
async def call_tool(name: str):
  # Async context manager for FastMCP client lifecycle. Automatically infers HTTP transport from the URL 
  # parameter while ensuring proper connection cleanup, preventing resource leaks. The Client class handles 
  # protocol operations while delegating low-level connection management to the separate Transport layer.
  async with client:
    # This executes a remote tool call to the MCP server's "greet" endpoint, passing the name parameter as a 
    # dictionary payload. The Client automatically infers HTTP transport from the URL and handles all protocol 
    # operations, while the underlying Transport layer manages the actual connection lifecycle. The async with 
    # pattern ensures proper connection cleanup, which is critical for HTTP transports that may use connection 
    # pooling.
    result = await client.call_tool("greet", {"name": name}) 
    print(result)

asyncio.run(call_tool("Ford"))

"""
This demonstrates the asynchronous client pattern for remote tool invocation in FastMCP. The code shows how 
to establish a connection to an MCP server, call a registered tool by name, and handle the response 
asynchronously, with the `Client` class serving as the primary interface for all server interactions. The
distinctive aspect here is the complete abstraction of transport details, allowing the same client code 
to work across different connection types.

The pattern works through a clean separation between protocol operations and transport management. 
The `Client class handles MCP protocol specifics like tool discovery and argument serialization, while the 
transport layer (automatically inferred as HTTP from the URL parameter) manages the actual connection 
lifecycle. The `async with` context ensures proper resource cleanup, and the `call_tool` method provides a 
uniform interface regardless of whether you're using HTTP, STDIO, or in-memory transports for testing. 

This approach matters because it eliminates transport-specific boilerplate while maintaining flexibility. 
You can switch between local testing (using a FastMCP instance directly) and production HTTP connections 
just by changing the client initialization, without modifying your tool invocation logic. The async design 
prevents blocking during network operations, and the context manager pattern ensures connections are 
properly managed, making it ideal for both simple scripts and complex applications that need to reuse client 
instances across multiple tool calls.
"""