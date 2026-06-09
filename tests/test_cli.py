"""Tests for the hello CLI command."""

from click.testing import CliRunner

from src.cli import hello


def test_hello_default() -> None:
    runner = CliRunner()
    result = runner.invoke(hello, [])
    assert result.exit_code == 0
    assert "Hello, World!" in result.output


def test_hello_with_name() -> None:
    runner = CliRunner()
    result = runner.invoke(hello, ["--name", "Desenrolai"])
    assert result.exit_code == 0
    assert "Hello, Desenrolai!" in result.output
