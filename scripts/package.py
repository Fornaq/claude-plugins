"""Build a reproducible plugin ZIP containing only the reviewed allowlist."""
import hashlib
import json
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from check import FILES, PLUGIN, ROOT, validate

validate()
version = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())["version"]
output = ROOT / "dist"
output.mkdir(exist_ok=True)
archive = output / f"lazy-schedule-{version}.zip"
with ZipFile(archive, "w") as bundle:
    for relative in sorted(FILES):
        info = ZipInfo(relative, (2026, 1, 1, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.create_system = 3
        info.external_attr = 0o100644 << 16
        bundle.writestr(info, (PLUGIN / relative).read_bytes())
digest = hashlib.sha256(archive.read_bytes()).hexdigest()
(output / "SHA256SUMS").write_text(f"{digest}  {archive.name}\n")
print(archive)
print(digest)
