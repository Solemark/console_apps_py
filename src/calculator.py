class Calculator:
    def __init__(self, a: int | float, b: int | float) -> None:
        self.a: int | float = a
        self.b: int | float = b

    def add(self) -> int | float:
        return self.a + self.b

    def sub(self) -> int | float:
        return self.a - self.b

    def mul(self) -> int | float:
        return self.a * self.b

    def div(self) -> int | float:
        return self.a / self.b
