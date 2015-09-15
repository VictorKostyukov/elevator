#!/usr/bin/env python3

from src.elevator import Elevator


# Tests the elevator by running it and outputting statistics
# This function assumes that floors have already been requested
def test(elevator):

    # Output initial parameters and state of elevator
    print('Number of floors: {}'.format(elevator.num_floors))
    print('Starting at floor {}'.format(elevator.current_floor))
    print('Requested floors: {}'.format(
        ', '.join(map(str, elevator.requested_floors))))
    elevator.travel()
    # Output statistics pertaining to elevator's completed journey
    print('Visited floors: {}'.format(
        ', '.join(map(str, elevator.visited_floors))))
    print('Number of floors traveled: {}'.format(elevator.num_floors_traveled))
    # Output blank line to improve readability
    print()


# Runs elevator against various cases to determine overall efficiency
def main():

    elevator = Elevator(num_floors=5, starting_floor=1)
    elevator.request_floor(5)
    test(elevator)

    elevator = Elevator(num_floors=5, starting_floor=1)
    elevator.request_floor(5)
    elevator.request_floor(3)
    elevator.request_floor(4)
    test(elevator)

    elevator = Elevator(num_floors=5, starting_floor=2)
    elevator.request_floor(5)
    elevator.request_floor(4)
    elevator.request_floor(1)
    test(elevator)

    elevator = Elevator(num_floors=6, starting_floor=1)
    elevator.request_floor(6)
    elevator.request_floor(5)
    elevator.request_floor(1)
    test(elevator)

    elevator = Elevator(num_floors=5, starting_floor=3)
    elevator.request_floor(1)
    elevator.request_floor(2)
    elevator.request_floor(4)
    elevator.request_floor(5)
    test(elevator)

    elevator = Elevator(num_floors=5, starting_floor=1)
    elevator.request_floor(2)
    elevator.request_floor(3)
    elevator.request_floor(4)
    elevator.request_floor(5)
    test(elevator)

if __name__ == '__main__':
    main()
