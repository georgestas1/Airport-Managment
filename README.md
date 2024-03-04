Airport Simulation
This script simulates an airport with landing and takeoff requests. It uses two priority queues to manage these requests: one for landing and one for takeoff.

Table of Contents
Installation
Usage
Functions
simulate_airport
add_request
control_airport
Notes
Installation
To run the script, you need to have Python 3.x and the priority_linked_list module installed.

Install Python 3.x from the official website.
Install the priority_linked_list module using pip:
Copy code
pip install priorityqueue
Usage
After installing the required dependencies, simply run the script using Python:

Copy code
python airport_simulation.py
Functions
simulate_airport
This function simulates airport operations with landing and takeoff requests.

Parameters

None

Returns

None

add_request
This function adds a landing, takeoff, or emergency request to the appropriate queue.

Parameters

flight_number: int, the flight number to add to the queue
request_type: str, the type of request ("landing", "takeoff", or "emergency")
Returns

None

control_airport
This function controls airport operations, processing landing and takeoff requests.

Parameters

None

Returns

None

Notes
The simulate_airport function generates 2 sets of 3 random requests, simulating 2 requests overall.
Each request is added to the appropriate queue with a random priority between 0 and 1.
The control_airport function processes landing requests first, followed by takeoff requests.
For each request, the script prints a message indicating the request type and flight number, as well as a message when the flight has landed or taken off.
Between requests, the script waits for a random sleep time between 0.5 and 2.0 seconds.
After each request set, the script waits for 1 second before starting the next request set.
