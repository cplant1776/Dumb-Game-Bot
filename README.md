## A Time-Saving, Dumb Game Bot

A simple Python program that I wrote to automate grindy aspects of a game that I otherwise enjoy. I do not wish to say the name of the game, and have omitted the images used for image recognition, but if you are familiar with it you can probably figure it out from function/variable names. At this point it is not robust in the slightest and I expect to squash many bugs, but it gets the job done.

## Motivation

I created this project with three objectives:

1. Automate grindy aspects of the game so that I can enjoy the other parts of it in my spare time
2. Gain more practice structuring non-trivial projects in Python
3. Dip my toes into machine learning in order to make the bot more robust

As much as I love playing the game, there are certain parts of it that are just a time waste at this point. As there is no bot/cheat protection of any sort, I figured it would be a good opportunity to sharpen my skills while saving myself time in the future. I am still getting used to logically structuring Python programs, so I welcome more practice. 

Additionally, I see a great opportunity to get started with some basic machine learning in this project. The game is 3D, so the objects I need to interact with can be viewed from many many angles and distances. This makes generic image recognition unviable for some functions, as far as I can tell. The current solution is to move the character generally where the objects should be and then click about like a madman till the desired menu pops up. My rudimentary understanding of machine learning suggests that I can instead train it to (attempt to)  recognize the object and move directly to it most of the time, and fall back to the old method if that fails.

## Usage

#### Clone the Repo:
```shell
git clone https://github.com/cplant1776/Dumb-Game-Bot.git
```
#### Running

1. Set the appropriate initial conditions in-game (intentionally left out)
2. Run `python3 main.py`
* Note that You may need to substitute "python3" above for the appropriate command on your system.
3. Set Leveler's window as active window and then set Farmer's window as active window within 10 seconds of running the program
4. Go do something else

#### Requirements

##### Python
```
version 3.X
```
##### Packages

```
See requirements.txt
```



## Upcoming Changes (by Priority)

1. Add recovery for if the Farmer is defeated
2. Add timeout management for every action
3. Attempt to teach it to recognize my target objects
4. Text/email an alert to me if the bot encounters a problem
5. Generalize the bot to adapt to other missions dynamically
