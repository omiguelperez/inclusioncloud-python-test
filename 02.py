"""
Question 2
Create a derived class from the base class

• Inherits all properties and methods from the base class
• Initialize the properties differently from the base class
• Add code to the empty methods
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


class Derived(Base):
    def __init__(self, prop1, prop2, prop3, prop4, prop5, prop6):
        super().__init__(prop1, prop2, prop3)
        self.prop4 = prop4
        self.prop5 = prop5
        self.prop6 = prop6

    @classmethod
    def class_method(cls) -> None:
        print("Derived class method")

    def instance_method(self) -> None:
        print("Derived instance method")


if __name__ == '__main__':
    instance = Derived(1, 2, 3, 4, 5, 6)
    instance.class_method()
    instance.instance_method()
