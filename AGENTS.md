# Repository Guidelines

## Project Structure & Module Organization
- Backend entry points live at `sau_backend.py` (Flask API) and `cli_main.py` (CLI). Platform upload logic is organized under `uploader/` (for example `douyin_uploader/`, `tencent_uploader/`).
- Shared Python helpers are in `utils/` and `myUtils/`. SQLite storage lives in `db/database.db` with schema init in `db/createTable.py`.
- Frontend code lives in `sau_frontend/`. Key areas are `sau_frontend/src/views/` (pages), `sau_frontend/src/components/` (shared components), `sau_frontend/src/api/` (API clients), `sau_frontend/src/stores/` (Pinia), and `sau_frontend/src/styles/` (SCSS).
- Operational assets include `cookies/` and `cookiesFile/` for session data, `videos/` for upload inputs, `media/` for docs assets, and `examples/` for runnable scripts.

## Build, Test, and Development Commands
- `pip install -r requirements.txt` installs backend dependencies (use a virtualenv).
- `playwright install chromium` installs browser drivers required by the uploaders.
- `python db/createTable.py` initializes the local SQLite database.
- `python sau_backend.py` starts the backend at `http://localhost:5409`.
- `python cli_main.py <platform> <account> login` and `python cli_main.py <platform> <account> upload <video> -pt 0|1 -t "YYYY-MM-DD HH:MM"` run the CLI.
- `cd sau_frontend && npm install` installs frontend dependencies.
- `npm run dev` starts the Vite dev server at `http://localhost:5173`; `npm run build` and `npm run preview` are for production builds.
- `start-win.bat` launches backend and frontend in separate Windows terminals.

## Coding Style & Naming Conventions
- Python uses 4-space indentation, `snake_case` for functions and files, and `UPPER_SNAKE` for constants. Keep changes consistent with existing modules.
- Vue SFCs follow the `src/views` and `src/components` split. SCSS uses BEM-style class naming as documented in the frontend README.
- No repo-wide formatter or linter is configured, so avoid large reformatting and keep diffs minimal.

## Testing Guidelines
- There is no automated test suite in this repository. Validate changes by running the backend and frontend, and use `examples/` or the CLI to exercise uploader flows.

## Commit & Pull Request Guidelines
- Recent commits use Conventional Commit prefixes such as `feat`, `fix`, `docs`, or `style` with optional scopes like `feat(frontend): ...`. Short Chinese summaries also appear; match the existing style in the area you touch.
- PRs should include a clear description, linked issue (if any), test notes (platforms and commands), and screenshots for UI changes.

## Configuration & Security Notes
- Copy `conf.example.py` to `conf.py` and set values like `LOCAL_CHROME_PATH` before running.
- Do not commit cookies or account data. Keep session files inside `cookies/` or `cookiesFile/`.
