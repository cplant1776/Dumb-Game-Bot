## A Time-Saving, Dumb Game Bot

A simple Python program that I wrote to automate grindy aspects of a game that I otherwise enjoy. I do not wish to say the name of the game, and have omitted the images used for image recognition, but if you are familiar with it you can probably figure it out from function/variable names. At this point it is not robust in the slightest and I expect to squash many bugs, but it gets the job done.

## Motivation

I created this project with three objectives:

1. Automate grindy aspects of the game so that I can enjoy the other parts of it in my spare time
2. Gain more practice structuring non-trivial projects in Python

As much as I love playing the game, there are certain parts of it that are just a time waste at this point. As there is no bot/cheat protection of any sort, I figured it would be a good opportunity to apply my skills while saving myself time in the future.

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

## To-Do(?)

1. Recover if the Farmer is defeated
1. Timeout management for every action
1. Text/email an alert if it encounters a problem
