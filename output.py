# Import the random module for generating random numbers and the simulate_seating function from the utils module.
import random
from utils import simulate_seating

# Define the main function that will run the simulation.
def main():
    # Set the number of simulations to run.
    simulations = 10000
    # Initialize a counter for the number of times the last person sits in their correct seat.
    correct_seat_count = 0

    # Run the simulation for the specified number of times.
    for _ in range(simulations):
        # Call the simulate_seating function. If it returns True (last person sits in their correct seat), increment the counter.
        if simulate_seating():
            correct_seat_count += 1

    # Calculate the probability by dividing the number of successful outcomes by the total number of simulations.
    probability = correct_seat_count / simulations
    # Print the calculated probability, formatted to four decimal places.
    print(f"Probability that the last person sits in their assigned seat: {probability:.4f}")

# Check if this script is being run directly (as opposed to being imported as a module), and if so, call the main function to start the simulation.
if __name__ == "__main__":
    main()
