import os

# for local development, manually register plugin
if not os.environ.get("CI"):
    pytest_plugins = ["pytest_autofixture"]

# def pytest_configure(config):
#     if not config.pluginmanager.hasplugin("autofixture"):
#         import pytest_autofixture
#         config.pluginmanager.register(pytest_autofixture)
