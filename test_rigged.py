from .rigged import Rigged_RNG


def test_less_than(monkeypatch):
    monkeypatch.setattr("numpy.random.rand", lambda: 0.3)
    monkeypatch.setattr("numpy.random.rand", lambda: 0.7)

    result = Rigged_RNG(5, 0.75, 10)
    assert result == 5

def test_more_than(monkeypatch):
    monkeypatch.setattr("numpy.random.rand", lambda: 0.7)
    monkeypatch.setattr("numpy.random.rand", lambda: 0.3)

    result = Rigged_RNG(5, 0.75, 10)
    assert result == 5