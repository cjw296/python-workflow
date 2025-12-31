from test_package import greet, optional_feature, version_specific


def test_greet() -> None:
    assert greet("World") == "Hello, World!"


def test_version_specific() -> None:
    result = version_specific()
    assert result in ("python39", "python310plus")


def test_optional_feature() -> None:
    result = optional_feature()
    assert result in ("with_requests", "without_requests")
