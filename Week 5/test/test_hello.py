from hello import hello


def test_default():
    assert hello() == "Hello, world"


def test_argument():
    assert hello("David") == "Hello, David"


