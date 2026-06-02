"""
Intern Task 1: String utilities
"""


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def count_vowels(s: str) -> int:
    """Count vowels in a string."""
    return sum(1 for char in s.lower() if char in "aeiou")


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
