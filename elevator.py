#!/usr/bin/env python3


# Elevator class which implements my algorithm for controlling the
# decision-making logic of an elevator (i.e. deciding which floor to go next)
class Elevator(object):

    # Initializes a new Elevator object
    def __init__(self, num_floors, starting_floor):
        # Total number of floors accessible by the elevator
        self.num_floors = num_floors
        # An unordered set of floor numbers that have been requested
        self.requested_floors = set()
        # Current floor number
        self.current_floor = starting_floor
        # Number of floors traveled since the elevator was started
        self.floors_traveled = 0

    # Registers a request to visit a specific floor
    def request_floor(self, floor):
        self.requested_floors.add(floor)

    # Computes the number of floors passed when traveling from the current
    # floor to the given floor (including the given floor itself)
    def get_floor_difference(self, floor):
        return abs(self.current_floor - floor)

    # Travels to at the given floor to pick up or drop off passengers
    def visit_floor(self, floor):
        self.floors_traveled += self.get_floor_difference(floor)
        self.current_floor = floor
        # discard() will not raise an exception if floor does not exist
        self.requested_floors.discard(self.current_floor)

    # Starts elevator and travels computed route according to current requests
    def travel(self):
        # Output initial parameters and state of elevator
        print('Number of floors: {}'.format(self.num_floors))
        print('Starting at floor {}'.format(self.current_floor))
        print('Requested floors: {}'.format(
            ', '.join(map(str, self.requested_floors))))
        # Visit next closest requested floor until there are
        # no more requested floors to visit
        while len(self.requested_floors) != 0:
            closest_floor = min(
                self.requested_floors, key=self.get_floor_difference)
            print('Visiting floor {}'.format(closest_floor))
            self.visit_floor(closest_floor)
        # Output statistics at end of elevator's journey
        print('Floors traveled: {}'.format(self.floors_traveled))
        # Output blank line to improve readability
        print()
