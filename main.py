from employee import Employee
from car import *
from other.boat import BoatObj


def main():
    employee = Employee('Adam', 'Smith', 50000)
    employee.displayFullName()
    car1 = CarObj()
    boat1 = BoatObj()


if __name__ == '__main__':
    main()