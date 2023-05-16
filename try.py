from turtle import forward
from typing_extensions import Self


class hxb():
    a = True
    def __init__(self) -> None:
        pass
    def f(self):
        return self.a


if __name__ == "__main__":
   c = hxb()
   print('=',c.a)
   c.f()