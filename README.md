# Requirements

Python 3.9+.

# Package Management

This package uses [Poetry](https://python-poetry.org/) to manage dependencies and
isolated [Python virtual environments](https://docs.python.org/3/library/venv.html).

To proceed, 
[install Poetry globally](https://python-poetry.org/docs/#installing-with-the-official-installer)
onto your system.

## Dependencies

Dependencies are defined in [`pyproject.toml`](./pyproject.toml) and specific versions are locked
into [`poetry.lock`](./poetry.lock).

To install all dependencies into an isolated virtual environment:

```bash
$ poetry install
```

To [activate](https://python-poetry.org/docs/basic-usage#activating-the-virtual-environment) the
virtual environment that is automatically created by Poetry:

```bash
$ poetry shell
```

To deactivate the environment:

```bash
(bookstore) $ exit
```

To upgrade all dependencies to their latest versions:

```bash
$ poetry update
```