# Virtual-assistant

It is a menu driven program using python code which will execute the required user query when user gives the input as a text.
It can open notepad,windows media player,vlc,chrome,youtube,facebook,calculator,spotify,gmail .

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip install selenium
```

## Usage

```python
import os
from selenium import webdriver

```
Use the [link](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver) to install webdriver.

## Bugs faced

I encountered some error , when i type 'Dont open notepad' ,it opened the notepad,so i fixed it by adding a boolean operator to check the word and don't run if it detects the word.

## Future improvements

This project will be further converted to a voice based virtual assistant than typing it by incorporating some libraries.
