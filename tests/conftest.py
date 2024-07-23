# pytest_plugins = ["pytest_auto_fixture"]

# for local development, manually register plugin
def pytest_configure(config):
    if not config.pluginmanager.hasplugin("auto_fixture"):
        import pytest_auto_fixture
        config.pluginmanager.register(pytest_auto_fixture)
