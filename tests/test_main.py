import pytest

from ..main import run, InvalidArgument


@pytest.fixture()
def sentence_one():
    return "moi toi lui moi lui elle"

@pytest.fixture()
def sentence_two():
    return "bar baz foo foo zblah zblah zblah baz toto bar"


def test_run_one(sentence_one):
    res = run(sentence_one, 2)
    assert len(res) == 2
    assert res[0] == ("lui", 2)
    assert res[1] == ("moi", 2)


def test_run_two(sentence_two):
    res = run(sentence_two, 3)
    assert len(res) == 3
    assert res[0] == ("zblah", 3)
    assert res[1] == ("bar", 2)
    assert res[2] == ("baz", 2)


def test_run_three(sentence_two):
    with pytest.raises(InvalidArgument):
        run(sentence_two, "Not An Integer")

