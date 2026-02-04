# FastMCP HTTP Server and Client Example - Part 1/4

'''
Want to spin up a production-ready MCP server in under 10 seconds?

We'll create the core FASTMCP container tha handles all protocol details, tool registration, and
serialization-with optional parameters for versioning, client instructions, and even visual branding.
You'll see how this two-line setup becomes the launchpad for everything from local testing to cloud
deployment, thought we'll still neet to explicitly start it before use.
'''
# This imports "FastMCP", the core class for creating AI-callable tools bridges Python functions to AI
# models. The cosntructor accpets optionl parameter like "name" (default to "FastMCP"), "instructions" for
# client guidance, "version" for API versioning, an UI metadata like "website_url" and "icons" (v2.14.0+),
# though the server still requires explicit startup via "mcp.run()" or CLI.
from fastmcp import FastMCP

# Intializes the FastMCP server instance with optional configuration, where "My MCP Server" sets a
# human-readble indentifier thas defaults to "FASTMCP" is omitted. This isntance server as your container for
# registering AI-callable tools via decorators like "@mcp.tool", but requires startup via
# "mcp.run()" or CLI commands like "fastmcp run"
mcp = FastMCP("My MCP Server")

'''
This demonstrates the container RPC pattern, where a "FastMCP" instance server as both a tool registry
and deployment unit. The two-loines inicialization creates a foundation for AI-callable services, with the
optional name paramter (defaulting to "FastMCP") identifying the server in logs and client interfaces. The
pattern's key advantage os its dual role as a development container and prodution-ready server, supporting
progressive configuration from simple protoypes to full deplyments.

The approach combines declarative tool registration woth explicit runtime control. Decoratos like
"@mcp.too" define callable endpoints while keepgin business logic framework-agnostic, and the container
manages protocol handling, serialziation, ans transport selection. However, unlike automatic web
frameworks, FastMCP requires explicit startup via "mcp.run()" or CLI commands, givind developers 
precise control over execution context and transport layer configuration.

This pattern solves the tension between rapid iteration and production requirements. The container model
enables adding metadata like isntructions, versioning, an UI elements (website_url, icons) without 
modifying tool implementations. While the basic setup is mnimal, the framework suports gradula complexity
through additional parameters and configuration-making it equally suitable for local testing via STDIO or
clouddeployment with HTTP trnasport. The tradeoff is explicit starup management, but this ensures
prediactalbe behavior across environemnts.
'''
