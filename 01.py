"""
Question 1
Create a base class with:

• Three properties initialized at construction
• One empty classmethod
• One empty instance method
"""


class Base:
    def __init__(self, prop1, prop2, prop3):
        self.prop1 = prop1
        self.prop2 = prop2
        self.prop3 = prop3

    @classmethod
    def class_method(cls) -> None:
        pass

    def instance_method(self) -> None:
        pass


if __name__ == '__main__':
    instance = Base(1, 2, 3)
    instance.class_method()
    instance.instance_method()
