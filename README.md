# Deploy the Brand Custodian Dashboard to Vercel

Serverless version: static dashboard + JSON stores + live Google-Sheet
market-trend. MSSQL endpoints (`/api/overview`, `/sales-by-*`, `/budget`)
return graceful "not available" messages because `pymssql` cannot build on
Vercel's Python runtime.

## First deploy

1. Install the Vercel CLI:

   ```bash
   npm i -g vercel
   ```

2. From this folder (`AI_Automation/vercel`):

   ```bash
   vercel login
   python sync.py            # copy latest frontend + stores into this folder
   vercel                    # preview deploy (logs in with your account)
   vercel --prod             # production deploy
   ```

   Keep `sync.py` before every deploy to push latest UI/data changes.

3. Set the Google token as an environment variable (the dashboard reads it
   instead of `database/token.json` in serverless):

   ```bash
   vercel env add GOOGLE_TOKEN_JSON production
   ```
   Paste the full JSON contents of `AI_Automation/database/token.json`.

4. Optional env vars (defaults are fine):
   - `MARKET_SHEET_FILE` = `1NDWiW6q1PuykQ2uuNLcMuyU_90tVSBqLARlQxiaPgss`
   - `MARKET_SHEET_GID` = `1519626691`

## Local test (Windows)

```powershell
$env:PORT = "8050"
python api\index.py
# then open http://localhost:8050
```

## What is in this folder

- `api/index.py` — Flask app: static dashboard + JSON API (Vercel serverless)
- `api/market_fetch.py` — live market-trend puller from Google Sheets
- `public/` — dashboard UI (synced from `web/` by `sync.py`)
- `database/` — editable JSON stores (campaigns, competitors, market share, ...)
- `vercel.json` — function limits + static rewrites
- `.gitignore` — keeps `token.json` / `credentials.json` out of Git/Vercel