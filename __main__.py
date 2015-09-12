#!/usr/bin/env python3

from elevator import Elevator


# Runs elevator against various cases to determine overall efficiency
def main():

    elevator = Elevator(num_floors=5, starting_floor=1)
    elevator.request_floor(5)
    elevator.travel()

    elevator = Elevator(num_floors=5, starting_floor=1)
    elevator.request_floor(5)
    elevator.request_floor(3)
    elevator.request_floor(4)
    elevator.travel()

    elevator = Elevator(num_floors=5, starting_floor=2)
    elevator.request_floor(5)
    elevator.request_floor(4)
    elevator.request_floor(1)
    elevator.travel()

    elevator = Elevator(num_floors=6, starting_floor=1)
    elevator.request_floor(6)
    elevator.request_floor(5)
    elevator.request_floor(1)
    elevator.travel()

    elevator = Elevator(num_floors=6, starting_floor=3)
    elevator.request_floor(1)
    elevator.request_floor(2)
    elevator.request_floor(4)
    elevator.request_floor(5)
    elevator.travel()

    elevator = Elevator(num_floors=6, starting_floor=1)
    elevator.request_floor(2)
    elevator.request_floor(1)
    elevator.request_floor(4)
    elevator.request_floor(5)
    elevator.travel()

if __name__ == '__main__':
    main()
