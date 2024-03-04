import random
import time
from priority_linked_list import PriorityQueue

# Generate a random sleep time between 0.5 and 2.0 seconds
sleep_time = random.uniform(0.5, 2.0)
# Fixed sleep time of 0.5 seconds
sleep_time2 = 0.5

def simulate_airport():
    # Create a priority queue for landing requests
    landing_queue = PriorityQueue()
    # Create a priority queue for takeoff requests
    takeoff_queue = PriorityQueue()

    def add_request(flight_number, request_type):
        if request_type == "landing":
            # Add landing request to the landing queue with priority 0
            landing_queue.insert(flight_number, 0)
        elif request_type == "emergency":
            # Add emergency landing request to the landing queue with priority 1
            landing_queue.insert(flight_number, 1)
        elif request_type == "takeoff":
            # Add takeoff request to the takeoff queue with priority 0
            takeoff_queue.insert(flight_number, 0)

        # Print the flight number and request type
        print(f"Flight {flight_number} requests {request_type}")

    def control_airport():
        # Process landing requests until the landing queue is empty
        while not landing_queue.empty():
            # Get the highest priority landing request and remove it from the list
            flight_number = landing_queue.remove()
            # Print the landing message
            print(f"Flight {flight_number} is landing...")
            # Sleep for the random sleep time
            time.sleep(sleep_time)
            # Print the landed message
            print(f"Flight {flight_number} has landed.")

        # Process takeoff requests until the takeoff queue is empty
        while not takeoff_queue.empty():
            # Get the highest priority takeoff request and remove it from the list
            flight_number = takeoff_queue.remove()
            # Print the takeoff message
            print(f"Flight {flight_number} is taking off...")
            # Sleep for the random sleep time
            time.sleep(sleep_time)
            # Print the taken off message
            print(f"Flight {flight_number} has taken off.")

    # Simulate 2 requests
    for n in range(2):
        print(f"----Request No: {n + 1} started----")
        # Add 3 random requests to the airport
        for i in range(3):
            # Generate a random flight number between 100 and 999
            flight_number = random.randint(100, 999)
            # Choose a random request type
            request_type = random.choice(["landing", "takeoff", "emergency"])
            # Add the request to the appropriate queue
            add_request(flight_number, request_type)
            # Sleep for the fixed sleep time
            time.sleep(sleep_time2)

        # Call the control_airport function to control the airport operations
        control_airport()
        print(f"----Request No: {n + 1} completed----\n")
        time.sleep(1)

# Call the simulate_airport function to start the simulation
simulate_airport()
