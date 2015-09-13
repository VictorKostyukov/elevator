#!/usr/bin/env python3

import nose.tools as nose
from elevator import Elevator


def test_init_params():
    """should store correct initial parameters when elevator is initalized"""
    elevator = Elevator(num_floors=5, starting_floor=2)
    nose.assert_equal(elevator.num_floors, 5)
    nose.assert_equal(elevator.current_floor, 2)
    nose.assert_set_equal(elevator.requested_floors, set())
    nose.assert_list_equal(elevator.visited_floors, [])
    nose.assert_equal(elevator.num_floors_traveled, 0)


def test_request_floor():
    """should register requested floors"""
    elevator = Elevator(num_floors=5, starting_floor=1)
    elevator.request_floor(3)
    elevator.request_floor(5)
    nose.assert_set_equal(elevator.requested_floors, {3, 5})


def test_visited_floors():
    """should register visited floors in order"""
    elevator = Elevator(num_floors=5, starting_floor=5)
    elevator.request_floor(4)
    elevator.request_floor(2)
    elevator.travel()
    nose.assert_list_equal(elevator.visited_floors, [4, 2])


def test_current_floor_after_travel():
    """should set current floor to last visited floor"""
    elevator = Elevator(num_floors=6, starting_floor=4)
    elevator.request_floor(5)
    elevator.request_floor(2)
    elevator.travel()
    nose.assert_equal(elevator.current_floor, 2)


def test_num_floors_traveled_up():
    """should keep track of the number of floors traveled going up"""
    elevator = Elevator(num_floors=5, starting_floor=1)
    elevator.request_floor(5)
    elevator.travel()
    nose.assert_equal(elevator.num_floors_traveled, 4)


def test_num_floors_traveled_down():
    """should keep track of the number of floors traveled going down"""
    elevator = Elevator(num_floors=5, starting_floor=5)
    elevator.request_floor(1)
    elevator.travel()
    nose.assert_equal(elevator.num_floors_traveled, 4)


def test_num_floors_traveled_up_down():
    """should keep track of the number of floors traveled going up then down"""
    elevator = Elevator(num_floors=5, starting_floor=3)
    elevator.request_floor(5)
    elevator.request_floor(1)
    elevator.travel()
    nose.assert_equal(elevator.num_floors_traveled, 6)


def test_minimize_retrace():
    """should minimize the retracing of the elevator's path"""
    elevator = Elevator(num_floors=5, starting_floor=1)
    elevator.request_floor(4)
    elevator.request_floor(5)
    elevator.request_floor(3)
    elevator.request_floor(2)
    elevator.travel()
    nose.assert_equal(elevator.visited_floors, [2, 3, 4, 5])
