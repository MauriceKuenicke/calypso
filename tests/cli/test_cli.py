from typing import Any

from calypso.cli.cli import start_development_server
from click.testing import CliRunner


def test_run_dev_server(monkeypatch: Any) -> None:
    """Test the run dev server command of the CLI tool."""
    mock_popen = lambda: None  # noqa: E731
    mock_uvicorn = lambda: None  # noqa: E731
    mock_register = lambda: None  # noqa: E731

    monkeypatch.setattr("calypso.cli.cli.Popen", mock_popen)
    monkeypatch.setattr("calypso.cli.cli.uvicorn.run", mock_uvicorn)
    monkeypatch.setattr("calypso.cli.cli.atexit.register", mock_register)

    runner = CliRunner()
    _ = runner.invoke(start_development_server)
