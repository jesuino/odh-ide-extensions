"""Server side test configuration."""

import pytest

pytest_plugins = "pytest_jupyter.jupyter_server"


@pytest.fixture
def jp_server_config():
    """Return the default server config for testing."""
    return {"ServerApp": {"jpserver_extensions": {"odh_jupyter_trash_cleanup": True}}}
