### Game Window

<details>
<summary> At runtime, the very first thing the game does at initialization is create the game window for the player to see. That is why when we run the command 'pygame.init()' function,it initializes the background settings that Pygame needs to work properly. The 'pygame.display.set_mode((x,y))' creates the dimensions for the display window of the game. Inside that window we will have the game graphical elements. 
</summary>



[![Display Window](assets/display_window.png)](https://github.com/bluemau-dev)

|Function                         |Description                                                |
|---------------------------------|-----------------------------------------------------------|
|pygame.init()                    |Initializes background setting                             |
|pygame.display.set_caption("")   |Title/Caption of the Window Screen                         |
|pygame.display.set_mode((x,y))   |Create Display Window with screen dimensions               |
|.fill(colorValue)                |Fills screen with certain RGB color value                  |



### Game Initiliazation

<summary>
    Create a settings.py file. This file is for any future changes we have on the projects settings like the background, window size, and etc.
</summary>
</details>

### Creating a Object Class
An object class can refer to a game object such as a player, enemy, or a literal object. To visualize our in game object we use (.bmp) files instead of (.jpg) or (.png) formats.

|Function                         |Description                                                |
|---------------------------------|-----------------------------------------------------------|
|pygame.blit()                    |Method to draw the image to screen                         |
|pygame.transform.scale(surface())|Transform the scale of the object in (x,y) amount of pixels|

### Responding to a Keypress
Keypress is registered in Pygame as an event. If we want our game object to do something in particular during a keypress then we must let that event happen in our event method. Specifying which key is pressed down will return true depending on if it was pressed or not. In addition, there are commands to check if a key is no longer being pressed down.

In our game object, we added an update method and boolean value to determine if the game object is being moved when a key input is triggered.