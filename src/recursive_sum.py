type Number = int | float


def number(m: Number, i: Number = 0, t: Number = 0) -> Number:
    return t if i > m else number(m, i + 1, t + i)


def array(a: list[Number], i: int = 0, t: Number = 0) -> Number:
    return t if i > a.__len__() - 1 else array(a, i + 1, t + a[i])
