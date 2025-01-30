def recursive_sum(a: list[int], i: int = 0) -> int:
    return a[i] if i >= len(a) - 1 else a[i] + recursive_sum(a, i + 1)


def recursive_sum_tail(a: list[int], i: int = 0, total: int = 0) -> int:
    return total if i > a.__len__() - 1 else recursive_sum_tail(a, i + 1, total + a[i])
