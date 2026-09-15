---
name: setup
description: Connect the Lazy Schedule plugin, explain its account permissions, or troubleshoot missing Lazy Schedule tools or authorization errors.
disable-model-invocation: true
---

# Connect Lazy Schedule

This plugin connects to `https://lazyschedule.com/mcp` using the host's OAuth flow. It does not need an API key, a local server, or a password in the conversation.

1. In Claude Code, ask the user to open `/mcp`, select this plugin's Lazy Schedule connection, and authenticate. In Claude's plugin/connector interface, use the connection's sign-in control. If the plugin was just installed in Claude Code, run `/reload-plugins` or restart the session when the host requests it.
2. Let the user sign in directly to Lazy Schedule and choose the permission categories on its consent page. Never request passwords, verification codes, session cookies, or bearer tokens in chat. Do not handle browser consent on the user's behalf.
3. Explain only the permissions relevant to the requested workflow. Reading plans needs task/goal read access. Creating or updating them also needs the corresponding write access. Community posting needs social write access. Delete permissions are separate and are not needed for ordinary planning.
4. After connection, verify using one relevant read, such as `goals_list` with a small limit. An empty successful list is a valid result. Do not create a test record or post just to prove connectivity.
5. Report whether the connection worked. If it did not, distinguish authentication, missing permission, and server errors. A permission error is not an empty account. Do not invent data or retry a write after an uncertain result.

Permissions are category-based, not grants for individual goals. Available tools and data depend on the granted permissions and the server's access checks. The connection can be revoked at [Settings → Connected apps](https://www.lazyschedule.com/settings/connected-apps).

If the tools remain unavailable, ask the user to refresh the connection in their host. Avoid adding a second manually configured MCP server on top of the plugin. The fallback manual connection URL is the same URL above.
