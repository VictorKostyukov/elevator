# Elevator
*Copyright 2015, Caleb Evans*  
*Released under the MIT license*

[![Build Status](https://travis-ci.org/caleb531/elevator.svg?branch=master)](https://travis-ci.org/caleb531/elevator)
[![Coverage Status](https://coveralls.io/repos/caleb531/elevator/badge.svg?branch=master)](https://coveralls.io/r/caleb531/elevator?branch=master)

This small project consists of my algorithm for controlling the path of an elevator according to supplied parameters and initial state. The algorithm is implemented in Python 3 and consists of a class (`elevator/elevator.py`) and a driver (`elevator/__main__.py`).

## Goals

This algorithm and its implementation here were designed with simplicity and efficiency in mind. The primary goal is to maximize elevator efficiency, which is virtually achieved by minimizing the number of floors traveled during the lifetime of the elevator's journey.

## Usage

The flow for testing the implementation of this algorithm is as follows. See `elevator/__main__.py` for complete code examples.

1. Instantiate a new elevator object with the required parameters (total number of floors, starting floor)
2. Request any number of floors
3. Start the elevator's journey to each of those requested floors; the algorithm determines the order in which these floors are visited

```python
elevator = Elevator(num_floors=5, starting_floor=1)
elevator.request_floor(3)
elevator.request_floor(5)
elevator.travel()
```

## Algorithm

Once floors have been requested and the elevator is started, the elevator visits the closest requested floor, and continues visiting the next closest requested floor until all requested floors have been visited.

The algorithm makes no distinction between someone requesting a floor and someone requesting the elevator from any floor. Thus, the algorithm is never concerned with the direction of the elevator: not any requested direction nor the current direction.

For maximal efficiency, every elevator should start at either the lowest or highest floor because the elevator would never need to change direction at any point.

### A note about timing

For the sake of simplicity, the implementation of the algorithm is synchronous. However, real-world elevators must be able to handle intermittent requests. Fortunately, the implementation can still simulate the requesting of floors while the elevator is traveling. To do so, simply call `request_floor()` after calling `travel()`, as this will have the same effect.

```python
elevator = Elevator(num_floors=5, starting_floor=1)
elevator.request_floor(3)
elevator.request_floor(5)
elevator.travel()
elevator.request_floor(3)
elevator.request_floor(1)
elevator.travel()
```

In terms of the algorithm, this implies that the elevator must finish visiting the current set of requests before visiting the next set (*i.e.* the set of those floors requested while the elevator was currently visiting floors).

However, if floors are requested intermittently for real-world elevators, the algorithm must somehow determine how requests are grouped together. Otherwise, requested floors would always be queued up, and the elevator may not be able to achieve maximum efficiency. An ideal solution to this problem would to group together requests that fall within a certain time interval. For example, requests made within the same 30 seconds are grouped together.

## Running tests

To run the included unit tests, first install the required Python packages via `pip` (note that you may wish to create a virtualenv first):

```bash
pip install -r requirements.txt
```

Then, use the `coverage` package to run unit tests and generate coverage data:

```bash
coverage run -m nose
```

Finally, to view the coverage report, run `coverage report`.
