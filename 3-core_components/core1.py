# FastMCP Server Core Components Guide - Part 1/16

"""
Need to create an AI assistant server that actually tells users how to interact with it?

You'll see how to set up a "FastMCP" server with clear instructions, so clients know exactly what tools 
are available and how to call them. We'll start with a basic server, then add guidance that appears 
right in the client interface.
"""

from fastmcp import FastMCP

# Create a baic server instance
mcp = FastMCP(name="MyAssistanceServer")

# You can also add instructions for how to interecatr with server

# This demosntrates FastMCS's configurable server initialization. The instructions parameter defines how
# AI models should interact with your tools, creating self-documenting endpoints. This pattern replaces
# separate APo documentation by embedding usage guidance directly in the server setup.
mcp_with_instructions = FastMCP(
  name="HelpfullAssistant",
  # This defines as multi-line string for server isntructions. FastMCP uses to document available tools
  # and guide AI interactions, functioning as both APO documentation ans usage hints.
  instructions="""
    This server provides data analysis tools.
    Call get_avergare() to analyse numerical data.
  """
)

"""
This demonstrates the server-as-container pattern for building modular AI-integrated services.
The `FastMCP` class acts as a central registry that transforms ordinary Python functions into 
discoverable, callable components through declarative decorators. What makes this distinctive 
is its dual role as both a runtime server and a development-time organizer, bridging the gap 
between local Python logic and remote client access.

The pattern works by treating the server instance as a composition root where you register 
capabilities (tools, resources, prompts) rather than writing transport-specific code. 
Components remain pure Python functions while the framework handles serialization, validation, 
and protocol translation automatically. This separation of concerns lets you focus 
on business logic while the server manages all cross-cutting concerns like type coercion, 
error handling, and transport negotiation.

This approach matters because it eliminates the traditional RPC boilerplate without sacrificing 
type safety or discoverability. You get OpenAPI-like documentation and client SDKs automatically 
generated from your Python code, making it ideal for AI tooling, microservices, or any scenario 
where you need to expose backend logic to heterogeneous clients. The tradeoff ios framwork coupling, 
but the productivity gains in reduced glue code typically outwirgh this for most applciaitons 
use cases.
"""