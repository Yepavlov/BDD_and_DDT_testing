import pytest

from rest.lambdatest import LambdaTestService


@pytest.fixture
def context():
    return dict()


@pytest.fixture(scope="session")
def lambda_test_service():
    return LambdaTestService()
