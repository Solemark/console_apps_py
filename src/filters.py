type Arr = list[int | float]


class Filters:
    def __init__(self, a: Arr) -> None:
        self.a: Arr = a

    def negative(self) -> Arr:
        return [i for i in self.a if i >= 0]

    def positive(self) -> Arr:
        return [i for i in self.a if i <= 0]

    def odds(self) -> Arr:
        return [i for i in self.a if i % 2 != 0]

    def evens(self) -> Arr:
        return [i for i in self.a if i % 2 == 0]
