from eval_pol import eval_pol
import pytest

@pytest.mark.benchmark
def test_python_float_one_hundred(benchmark):
    result = benchmark(eval_pol, 100, 0.5)

    assert result == 400

@pytest.mark.benchmark
def test_python_float_one_thousand(benchmark):
    result = benchmark(eval_pol, 1000, 0.05)

    assert result == 2105.263157894749

@pytest.mark.benchmark
def test_python_float_ten_thousand(benchmark):
    result = benchmark(eval_pol, 10000, 0.2)

    assert result == 25000
