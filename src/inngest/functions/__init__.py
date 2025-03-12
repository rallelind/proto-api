"""
This file makes the functions directory a proper Python package and
exports all functions for easy importing elsewhere.
"""

from src.inngest.functions.my_function import my_function
from src.inngest.functions.example_function import example_function

__all__ = [
    "my_function",
    "example_function",
    # Add more functions here as they are created
]

# List of all functions to be registered with Inngest
