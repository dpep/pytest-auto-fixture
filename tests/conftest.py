import os

# for local development, manually register plugin
if not os.environ.get("CI"):
    pytest_plugins = ["pytest_auto_fixture"]

# def pytest_configure(config):
#     if not config.pluginmanager.hasplugin("auto_fixture"):
#         import pytest_auto_fixture
#         config.pluginmanager.register(pytest_auto_fixture)
