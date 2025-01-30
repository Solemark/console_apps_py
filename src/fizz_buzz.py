class FizzBuzz:
    def __init__(self, fizz: int, buzz: int, last: int) -> None:
        self.fizz = fizz
        self.buzz = buzz
        self.last = last

    def play(self) -> str:
        """play a game of Fizz Buzz"""
        output: str = ""
        for i in range(1, self.last + 1):
            if i % 3 == 0:
                output += "fizz"
            if i % 5 == 0:
                output += "buzz"
            if output.__len__() == 0 or output[-1] != "z":
                output += f"{i}"
            output += ", "
        return output[0:-2]
