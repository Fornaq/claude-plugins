# Lazy Schedule for Claude

Work with tasks, goals, and progress updates in your Lazy Schedule account through its hosted MCP connection.

## Install in Claude Code

```text
/plugin marketplace add Fornaq/claude-plugins
/plugin install lazy-schedule@fornaq
/reload-plugins
```

Open `/mcp` and authenticate the Lazy Schedule connection. Sign in in your browser and choose the permission categories you want to grant. No API key or local server is required.

## Workflows

| Command | Purpose |
| --- | --- |
| `/lazy-schedule:setup` | Connect your account or troubleshoot permissions. |
| `/lazy-schedule:manage-plans` | Read and update tasks, dates, next steps, and goals. |
| `/lazy-schedule:share-progress` | Read goal updates, draft a post, or publish to your chosen audience. |

Example requests:

- “Show my active goals and their next steps in Lazy Schedule.”
- “Move my morning run to Friday at 7 a.m. Eastern.”
- “Update my first 5K goal to 50%.”
- “Draft a followers-only progress update for my bookshelf goal.”

The last example creates a draft, not a published post. Ask to publish when you are ready.

## Connection and permissions

The plugin declares one remote Streamable HTTP MCP server at `https://lazyschedule.com/mcp`. OAuth is handled by your Claude host and Lazy Schedule. Read, write, and delete permissions are selected by category (tasks, goals, community); they are not individual-goal grants. Some workflows require multiple categories. Server access rules still apply.

The MCP service can expose more tools than the three guided workflows, depending on your permissions. Authorized tools can read account data or change tasks, goals, shared content, and membership. Grant only the categories you need. Revoke access in [Settings → Connected apps](https://www.lazyschedule.com/settings/connected-apps). Removing the plugin from Claude does not by itself revoke the server-side connection.

This package contains configuration and Markdown skills. It has no local executable, hooks, background jobs, bundled credentials, or analytics code. Tool requests go to Lazy Schedule; tool results become available in your Claude conversation. Hosting and account data are governed by [Lazy Schedule's privacy policy](https://www.lazyschedule.com/privacy-policy) and [terms](https://www.lazyschedule.com/terms-and-conditions), together with the policies of your Claude host.

## Claude plugins and Cowork

The same plugin folder is packaged as a ZIP in GitHub Releases for hosts that support plugin upload. Available installation options depend on your Claude plan and organization settings. After installing, use the host's connection controls to sign in. The ZIP is a Claude plugin, not a desktop `.mcpb` extension.

Public directory review is separate from installation through Fornaq's marketplace. Distribution here does not imply Anthropic approval or inclusion in its directory.

## Limits and troubleshooting

- A Lazy Schedule account and the relevant consent permissions are required.
- A 401 response means authentication is required; a missing-scope error requires reviewing the connection's permissions. Neither means your account is empty.
- New goals default to private. Publishing and changing visibility are separate actions.
- Goal progress is your estimate. It is not automatically derived from task completion.
- The current goal-update tool does not clear fields through null values.
- This integration does not provide external-calendar sync, email sending, payments, or appointment booking.

Support: [support@fornaq.com](mailto:support@fornaq.com).
