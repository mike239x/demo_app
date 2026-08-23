FROM ubuntu

COPY --from=ghcr.io/astral-sh/uv:0.12.5 /uv /uvx /bin/
EXPOSE 8000
WORKDIR /root
COPY main.py .
COPY uv.lock .
COPY pyproject.toml .
RUN uv sync --locked
ENTRYPOINT ["uv", "run", "fastapi", "run"]