import pytest
from db_management import check_login_parameters


def test_login():
    assert check_login_parameters("s", "s")
