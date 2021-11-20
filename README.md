# MTGA Card Detector

Python utility to find the location of playable cards in MTGA. Provides a script with the function `mtga_get_card_positions` which returns a list of screen-relative `(x, y)` tuples that are a clickable region of a playable card.

Currently about 80% of the way there, still struggles on some corner cases like yellow/white highlights of the leftmost card in a full hand.

## Usage
- Install `OpenCV` and `pyautogui` into your environment
    - e.g. `pip install opencv-python pyautogui`
- Run `python test_script.py`
- Copy/import `mtga_get_card_positions` into whatever you want to use it with

## Assumptions
- Tested @ 1440p
    - Likely needs minor tweaks to `border_` and `card_region` variables to work at 1080p
- MTGA in full-screen open on your main screen with no visibility blocking overlays
- No alt-style cards (need to have a black border)
- Cards in default state:
    - Playable cards highlighted in blue
    - Not hovering over any cards
    - No animations etc over the cards
    
## Process
- Aim to run fast (currently <0.1s locally) therefore vectorised as much as possible 
    - Lets `numpy`/`OpenCV` do the majority of the heavy lifting
- Use MTGA's blue/yellow "playable" border to find the rough region
    - Left-most card has a darkened effect
    - Use region to strip out everything else
- Use black border to find individual cards
    - Will always be delineated by blue borders
    - Parameterise black border to catch most cases
    - Pull border coordinates to get a clickable position

## Talon Use-Case
This was specifically designed to pipe coordinates to the excellent [Talon](https://talonvoice.com/) in order to facilitate voice-control of the game.

Original region, roughly clipped by screen percent:
![screenshot](img/mtga_screenshot.png)

Processed region with border highlighted:
![screenshot](img/mtga_screenshot_processed.png)

Talon overlay:
![screenshot](img/mtga_screenshot_talon.png)
