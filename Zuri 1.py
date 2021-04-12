class Car:
    """
    This is a car class
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color
        """
        This a method for a car class
        """
    def accel(self):
        print('%s accelerates at 100mph' % self.name)
        print(f'{self.name} accelerates at 100mph')
        print(self.name, 'accelerates at 100mph')


car_1 = Car('Toyota', 'Off-white')

car_1.accel()
print(help(Car))
