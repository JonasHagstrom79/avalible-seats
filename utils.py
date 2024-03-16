# Import the random module for generating random numbers and the TOTAL_SEATS constant from the constants module.
import random
from constants import TOTAL_SEATS

def initialize_seating():
    """
    Initializes the seating arrangement for the theater.
    Returns a list representing the seats, all initially unoccupied (set to None).
    """
    # Create and return a list with a length equal to TOTAL_SEATS, with each element set to None, representing an unoccupied seat.
    return [None] * TOTAL_SEATS

def choose_random_seat(occupied_seats):
    """
    Chooses a random seat from the available seats.
    Args:
        occupied_seats: A list indicating the occupancy status of each seat (None for unoccupied).
    Returns:
        The index of a randomly chosen available seat, or None if no available seat is found.
    """
    # Create a list of indices for seats that are unoccupied (None).
    available_seats = [index for index, seat in enumerate(occupied_seats) if seat is None]
    # If there are no available seats, return None.
    if not available_seats:
        return None
    # Otherwise, return the index of a randomly chosen available seat.
    return random.choice(available_seats)

def simulate_seating():
    """
    Simulates the seating process as described in the project.
    Kenneth (the first visitor) chooses a random seat, and subsequent visitors
    either sit in their assigned seat or choose a random available seat if theirs is taken.
    Returns:
        A boolean indicating whether the last person to enter sits in their assigned seat.
    """
    # Initialize the seating arrangement.
    seats = initialize_seating()
    # Kenneth chooses a random seat.
    kenneths_seat = random.randint(0, TOTAL_SEATS - 1)
    seats[kenneths_seat] = 'Kenneth'

    # Iterate over the rest of the seats.
    for seat_number in range(1, TOTAL_SEATS):
        # If the current seat is unoccupied, the visitor takes their assigned seat.
        if seats[seat_number] is None:
            seats[seat_number] = seat_number
        else:
            # If the seat is taken, find a random available seat.
            random_seat = choose_random_seat(seats)
            # If a random seat is found, assign it to the current visitor.
            if random_seat is not None:
                seats[random_seat] = seat_number
          

    # Check if the last person sits in their assigned seat and return the result.
    return seats[-1] == TOTAL_SEATS - 1
