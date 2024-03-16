# Import the main function from the output module.
from output import main

# This conditional statement checks if the script is being run directly by the Python interpreter
# and not being imported as a module in another script.
if __name__ == "__main__":
    # If the script is run directly, call the main function imported from the output module.
    # This is the entry point of the program.
    main()