import pytest


@pytest.fixture
def fixture1():
    return 'fixture1'


@pytest.fixture
def fixture2(fixture1):
    return [fixture1, 'fixture2']


def test_chained_fixtures(fixture2):
    assert fixture2 == ['fixture1', 'fixture2']


def test_config(config):
    assert config is not None
