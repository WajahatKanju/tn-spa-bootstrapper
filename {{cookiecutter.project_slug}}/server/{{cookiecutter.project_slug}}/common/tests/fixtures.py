import pytest


@pytest.fixture
def JSON_RQST_HEADERS():
    return dict(
        content_type="application/json",
        HTTP_ACCEPT="application/json",
    )
