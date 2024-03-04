# Airport Traffic Control Simulation

This Python program simulates an airport's traffic control system using priority queues. It generates random landing, takeoff, and emergency landing requests for flights, prioritizing emergency landings over regular ones.

## Requirements

- Python 3.x
- priority_linked_list.py

## Installation

1. Clone the repository:

    git clone https://github.com/yourusername/airport-traffic-control.git

2. Navigate to the directory:

    cd airport-traffic-control

3. Run the program:

    python airport_traffic_control.py

## Description

The program simulates airport operations by processing landing and takeoff requests. It generates random flight numbers and request types, including regular landing, takeoff, and emergency landing requests. Requests are added to priority queues based on their priority level. Emergency landing requests have the highest priority, followed by regular landing and takeoff requests. The program then processes these requests accordingly, simulating the landing and takeoff procedures with random sleep times.

## Usage

To run the simulation, execute the `airport_traffic_control.py` file. The program will simulate airport operations for a predefined number of requests. Each request cycle includes adding random flight requests, processing them through the control_airport function, and completing the cycle.

## Example

