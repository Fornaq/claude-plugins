"""Validate the distribution boundary; optionally check public OAuth discovery."""
import argparse
import json
import re
from pathlib import Path
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/lazy-schedule"
FILES = (
    ".claude-plugin/plugin.json", ".mcp.json", "README.md", "LICENSE",
    "skills/setup/SKILL.md", "skills/manage-plans/SKILL.md",
    "skills/share-progress/SKILL.md",
)
ENDPOINT = "https://lazyschedule.com/mcp"


def validate():
    marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    manifest = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
    config = json.loads((PLUGIN / ".mcp.json").read_text())
    assert marketplace["name"] == "fornaq"
    assert len(marketplace["plugins"]) == 1
    entry = marketplace["plugins"][0]
    assert entry["name"] == manifest["name"] == "lazy-schedule"
    assert (ROOT / entry["source"]).resolve() == PLUGIN
    assert re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", manifest["version"])
    assert config == {"mcpServers": {"lazy-schedule": {"type": "http", "url": ENDPOINT}}}
    actual = {str(path.relative_to(PLUGIN)) for path in PLUGIN.rglob("*") if path.is_file()}
    assert actual == set(FILES), f"Unexpected or missing plugin files: {actual ^ set(FILES)}"
    for relative in FILES:
        path = PLUGIN / relative
        assert not path.is_symlink(), f"Symlink in distribution: {relative}"
        assert path.stat().st_size > 0
        if relative.endswith("SKILL.md"):
            text = path.read_text()
            assert text.startswith("---\n") and "\ndescription: " in text
            assert "\nname: " in text
    assert (PLUGIN / "LICENSE").read_bytes() == (ROOT / "LICENSE").read_bytes()
    print("Package boundary, marketplace source, remote MCP config, and skill files: passed")


def public_checks():
    def get(url):
        with urllib.request.urlopen(url, timeout=30) as response:
            assert response.status == 200
            return json.load(response)

    assert get(ENDPOINT + "/health")["status"] == "ok"
    resource = get("https://lazyschedule.com/.well-known/oauth-protected-resource/mcp")
    assert resource["resource"] == ENDPOINT
    assert resource["authorization_servers"] == [ENDPOINT + "/oauth"]
    auth = get("https://lazyschedule.com/.well-known/oauth-authorization-server/mcp/oauth")
    assert auth["issuer"] == ENDPOINT + "/oauth"
    assert auth["registration_endpoint"] == ENDPOINT + "/oauth/register"
    assert "S256" in auth["code_challenge_methods_supported"]
    request = urllib.request.Request(ENDPOINT, data=json.dumps({
        "jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
            "protocolVersion": "2025-03-26", "capabilities": {},
            "clientInfo": {"name": "lazy-schedule-plugin-check", "version": "1.0.0"},
        },
    }).encode(), headers={"Content-Type": "application/json", "Accept": "application/json, text/event-stream"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raise AssertionError(f"Unauthenticated MCP access unexpectedly returned {response.status}")
    except urllib.error.HTTPError as error:
        assert error.code == 401
        assert 'resource_metadata="https://lazyschedule.com/.well-known/oauth-protected-resource/mcp"' in error.headers.get("WWW-Authenticate", "")
    print("Public health, OAuth discovery, PKCE, and unauthenticated access rejection: passed")
    print("Authenticated account operations were not exercised.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true", help="Check public endpoints without credentials")
    args = parser.parse_args()
    validate()
    if args.live:
        public_checks()
