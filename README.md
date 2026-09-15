# Fornaq Claude plugins

Claude plugins from Fornaq, the makers of [Lazy Schedule](https://www.lazyschedule.com).

## Install Lazy Schedule

In Claude Code:

```text
/plugin marketplace add Fornaq/claude-plugins
/plugin install lazy-schedule@fornaq
/reload-plugins
```

Then open `/mcp` and authenticate the Lazy Schedule connection in your browser. Or run `/lazy-schedule:setup` for guidance.

The plugin connects your account to Claude for task planning, goal tracking, and sharing progress. [Plugin documentation](plugins/lazy-schedule/README.md) explains workflows, permissions, supported hosts, and limitations.

## Develop and validate

```sh
claude plugin validate . --strict
claude plugin validate ./plugins/lazy-schedule --strict
python3 scripts/check.py
python3 scripts/package.py
```

Test locally with `claude --plugin-dir ./plugins/lazy-schedule`. Perform the [account acceptance checks](docs/acceptance.md) with a disposable test account before claiming end-to-end validation. Package checks do not prove account-level OAuth or write operations.

The generated ZIP contains only the plugin files. It can be downloaded from [Releases](https://github.com/Fornaq/claude-plugins/releases). This repository contains the distributable plugin, not the Lazy Schedule application or server implementation.

## Releases

Update the version in `plugins/lazy-schedule/.claude-plugin/plugin.json`, add a changelog entry, validate, and package. Publish the corresponding `vX.Y.Z` GitHub release with the ZIP and SHA-256 checksum. Marketplace users can update with `claude plugin update lazy-schedule@fornaq`.

## Directory submission

See [submission information](docs/submission.md). Fornaq's marketplace is independently installable. Directory review and approval are controlled by Anthropic.

The plugin package is MIT licensed. Lazy Schedule's hosted service has its own terms and privacy policy. Support: [support@fornaq.com](mailto:support@fornaq.com).
