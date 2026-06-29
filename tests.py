from main import Calculator

# El test intentara sumar 2 + 2
def test_sums_2_numbers():
    assert Calculator().sum(2,2) == 4