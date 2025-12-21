# Changelog

## 2.1.0 (21 Dec 2025)

- Use the factored out `run-test` and `check-typing` actions.

## 2.0.1 (10 Apr 2025)

- Check the package on all the specified Python versions

## 2.0.0 (10 Apr 2025)

- Switch to `ruff` for formatting, using `cjw296/python-action/check-formatting`.

Make sure any `black` config in `pyproject.toml` is updated to `ruff` config.

## 1.1.0 (2 Apr 2025)

- Use `cjw296/python-action/check-coverage`.

## 1.0.1 (27 Mar 2025)

- Use `--resolution lowest-direct` instead of  `--resolution lowest`.
  See [this discussion](https://github.com/pypa/pip/issues/8085#issuecomment-2757196495).

## 1.0.0 (5 Mar 2025)

- Initial implementation of the `uv-ci` workflow.
