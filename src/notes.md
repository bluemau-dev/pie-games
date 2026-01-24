### Starting a Project
1. Install pygame
2. Creating a Pygame Window and Responding to User Input
    - def __init__():
        * Import 'sys' and 'pygame' modules. This is for our game to function.
        * Create a class related to your Python file, and define an initialization method that will have 'pygame.init()' function that will create the backgrounds settings that Pygame needs
        * Call this function: 'pygame.display.set_mode((WIDTH, HEIGHT))'. This will graphically draw the window elements. In the following argument that we labeled "WIDTH, HEIGHT", is a tuple that defines the dimensions of the game window. For default, try 1200 pixels by 800 pixels. Assign 'self.screen' to this function.
        * Call a function to create a window caption: 'pygame.display.set_caption("MY CAPTION")
    - def run_game():
        * In this function inside the same class, we call a while loop that contains an event loop and code that manages screen updates. An event is an action that the user performs while playing the game.
        * To access the events that Pygame detects we will use the 'pygame.event.get()' function that returns a list of event that have taken place since the last time this function was called. Inside that loop we will pass an if statement to deetect and respond to specific events. Like for example the 'sys.exit()' to exit the game if the player proceeds to try and exit the game. 

3. Creating a Settings Class
    - Create a Settings file to store all values in one place.
        * Screen Dimensions
        * Player Velocity
        * Background Color
        * Any interchangeable values