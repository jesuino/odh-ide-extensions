"""Init the extension backend."""

try:
    from ._version import __version__
except ImportError:
    # Fallback when using the package in dev mode without installing
    # in editable mode with pip. It is highly recommended to install
    # the package from a stable release or in editable mode:
    # https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs
    import warnings

    warnings.warn(
        """
        Importing 'odh_jupyter_trash_cleanup outside a proper installation.
        """
    )
    __version__ = "dev"
from .handlers import setup_handlers


def _jupyter_labextension_paths():
    return [{"src": "labextension", "dest": "odh-jupyter-trash-cleanup"}]


def _jupyter_server_extension_points():
    return [{"module": "odh_jupyter_trash_cleanup"}]


def _load_jupyter_server_extension(server_app):
    """Register the API handlers.

    The handlers receive and handle requests from the frontend.

    Parameters
    ----------
    server_app: jupyterlab.labapp.LabApp
        JupyterLab application instance
    """
    setup_handlers(server_app.web_app)
    name = "odh_jupyter_trash_cleanup"
    server_app.log.info("Registered %s server extension", name)
