"""sync.py - Copy the latest frontend + JSON stores from the repo into vercel/.

Run from the project root before `vercel --prod`:
    python AI_Automation/vercel/sync.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
WEB = ROOT / "AI_Automation" / "web"
DB = ROOT / "AI_Automation" / "database"
V = Path(__file__).resolve().parent

for name in ("index.html", "style.css", "app.js"):
    (V / "public" / name).write_bytes((WEB / name).read_bytes())

for name in ("campaigns", "competitors", "visibility", "visits", "kpis", "market_share"):
    src = DB / f"{name}.json"
    if src.exists():
        (V / "database" / f"{name}.json").write_bytes(src.read_bytes())

(V / "api" / "market_fetch.py").write_bytes((WEB / "market_fetch.py").read_bytes())

print("synced frontend, stores and market_fetch.py into vercel/")
