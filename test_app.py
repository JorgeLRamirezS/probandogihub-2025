"""
Tests para la aplicacion Hello World
"""

import pytest
from app import hello_world, main
from io import StringIO
import sys


def test_hello_world():
    """Test that hello_world returns the correct message"""
    result = hello_world()
    assert result == "Hello World"
    assert isinstance(result, str)
    assert len(result) > 0


def test_hello_world_content():
    """Test specific content of the hello world message"""
    result = hello_world()
    assert "Hello" in result
    assert "World" in result
    assert result.startswith("Hello")
    assert result.endswith("World")


def test_main_function():
    """Test the main function"""
    result = main()
    assert result == "Hello World"


def test_main_prints_output(capsys):
    """Test that main function prints to stdout"""
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World"


def test_hello_world_not_empty():
    """Test that hello_world doesn't return empty string"""
    result = hello_world()
    assert result != ""
    assert result is not None


@pytest.mark.parametrize("expected", ["Hello World"])
def test_hello_world_parametrized(expected):
    """Parametrized test for hello_world function"""
    result = hello_world()
    assert result == expected
