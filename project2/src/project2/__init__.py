"""Project 2 - A sample project that depends on project1."""

from project1 import greet

__version__ = "0.1.0"

def welcome(name: str) -> str:
    """Welcome message using project1."""
    greeting = greet(name)
    return f"Welcome! {greeting}"
