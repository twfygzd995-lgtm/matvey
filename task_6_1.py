# ============ установка uv ============
# Linux / macOS
$ curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows (PowerShell)
> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# Универсально (если уже есть Python)
$ pip install uv

# ============ базовые команды ============
$ uv --version
$ uv venv .venv
$ uv venv --python 3.12 .venv312
$ uv pip install requests --python .venv
$ uv pip list --python .venv
$ uv pip freeze --python .venv
$ uv python list
$ uv python install 3.13
