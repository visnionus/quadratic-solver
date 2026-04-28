from quadratic import solve


def test_dva_norm_kornya():
    x1, x2 = solve(1, -3, 2)  # x^2 - 3x + 2 = 0
    assert x1 == 2
    assert x2 == 1


def test_odin_koren():
    x1, x2 = solve(1, -2, 1)  # (x-1)^2
    assert x1 == 1
    assert x2 == 1


def test_kompleksniy_koren():
    x1, x2 = solve(1, 0, 1)  # x^2 + 1 = 0
    assert x1 == 1j or x1 == -1j
    assert x2 == 1j or x2 == -1j


def test_esli_a_eto_nol_to_gg():
    try:
        solve(0, 2, 1)
        assert False
    except ValueError:
        assert True