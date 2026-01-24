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

4. Creating a Bullet Class
    - Bullets are a Rect that are triggered by the player during an event and travel straight up the scrteen until they disappear off the top of the screen.
        * To create a Bullet.py file, first we need to add some settings for our bullet in our Settings.py:
            - Dimensions of Rect (Width and Height)
            - Bullet Speed
            - Bullet Color
    - Create a Bullet class in 'Bullet.py'
        * Our Bullet class will inherit from Sprite, which we import from 'pygame.sprite' module.
        * To create a bullet instance, '__init__()' needs the current instance of AlienInvasion, and we call 'super()' to inherit properly from Sprite. 
        * We also reference Settings to get the proper attributes of our bullets from the settings objects. 
        
### Pygame Objects

1. Rect - contains helpful methods that represent a rectangle area. Rectangles are created from the 'pygame.Rect()' function. For more useful information, follow this link: https://www.pygame.org/ftp/contrib/pygame_docs.pdf on page 67/88 to read more about Rect's.

    * Rect -> Integers only
    * Store positions as a float so we can move objects accurately, then copy that value into the Rect because pygame requires integers.