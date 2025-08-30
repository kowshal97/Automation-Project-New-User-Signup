import pytest

@pytest.mark.regression
def test_regression():
    print("Testing regression")

@pytest.mark.xfail
def test_regression2():
    print("Testing regression2")
    assert 5 == 6


@pytest.mark.sanity
def test_regression2():
    print("Testing regression")