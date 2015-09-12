# Elevator
*Copyright 2015, Caleb Evans*  
*Released under the MIT license*

This small project consists of my algorithm for controlling the path of an elevator according to supplied parameters and initial state. The algorithm is implemented in Python 3 and consists of a class (`elevator.py`) and a driver (`__main__.py`).

## Goals

This algorithm was designed with simplicity and efficiency in mind. The primary goal is to maximize elevator efficiency, which is virtually achieved by minimizing the number of floors traveled during the lifetime of the elevator's journey.

## Usage

To keep this implementation simple, the algorithm is only concerned with the state of parameters at the moment the elevator is started. In other words, the class must be used as follows:

1. Instantiate a new Elevator object with the required parameters (total number of floors, starting floor)
2. Request any number of floors
3. Start the elevator's journey to each of those request floors in the order determined by the algorithm

See `__main__.py` for complete code examples.

## Algorithm

Once floors have been requested and the elevator is started, the elevator visits the closest requested floor, and continues visiting the next closest floor until all requested floors have been visited.

In order to maintain simplicity, the algorithm makes no distinction between someone requesting a floor and someone requesting the elevator from any floor. Thus, the algorithm is not at all concerned with the direction of the elevator, either the requested direction or the current direction at any instant.

For maximal efficiency, every elevator should start at either the lowest or highest floor, and the driver program demonstrates the inefficiency of starting at any other floor.
