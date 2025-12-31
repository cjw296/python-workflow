import sys


def greet(name: str) -> str:
    return f"Hello, {name}!"


def version_specific() -> str:
    """Return different values based on Python version."""
    if sys.version_info < (3, 10):
        return "python39"
    else:
        return "python310plus"


def optional_feature() -> str:
    """Return different values based on whether requests is available."""
    try:
        import requests  # noqa: F401

        return "with_requests"
    except ImportError:
        return "without_requests"
