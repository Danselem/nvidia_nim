install-python:
	uv python install


init:
	uv init
	uv tool install black

install:
	uv venv
	. .venv/bin/activate
	# uv pip install --all-extras --requirement pyproject.toml
	# uv pip sync requirements.txt
	uv add -r requirements.txt

env:
	cp example.env .env

llama31:
	uv run src/reasoning/llama31.py

llama32:
	uv run src/reasoning/llama32.py

mistral:
	uv run src/reasoning/mistral.py

nemo:
	uv run src/reasoning/nemotron.py

phi:
	uv run src/reasoning/phimoe.py

palm:
	uv run src/reasoning/palmyra.py

llamvis:
	uv run src/vision/llama32.py

kosmos:
	uv run src/vision/kosmos.py

lint:
	ruff check

format:
	ruff format
	
ruff: lint format