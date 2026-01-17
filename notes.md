### Game Window

<details>
    <summary> At runtime, the very first thing the game does at initialization is create the game window for the player to see. That is why when we run the command 'pygame.init()' function,it initializes the background settings that Pygame needs to work properly. The 'pygame.display.set_mode((x,y))' creates the dimensions for the display window of the game. Inside that window we will have the game graphical elements. 
    </summary>
</details>


[![Display Window](assets/display_window.png)](https://github.com/bluemau-dev)

|Function                         |Description                                                |
|---------------------------------|-----------------------------------------------------------|
|pygame.init()                    |Initializes background setting                             |
|pygame.display.set_caption("")   |Title/Caption of the Window Screen                         |
|pygame.display.set_mode((x,y))   |Create Display Window with screen dimensions               |
|.fill(colorValue)                |Fills screen with certain RGB color value                  |

### Game Initiliazation

<details>
    <summary>
        Create a settings.py file. This file is for any future changes we have on the projects settings like the background, window size, and etc.
    </summary>
</details>