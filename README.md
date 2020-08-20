# Virtual-asst

It is a menu driven program using python code which will execute the required user query when user will give the input as a text.

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

I encountered some error , when i type 'Dont open notepad' ,it opened the notepad,so i fixed it by adding a boolean operator to check the word and don't run if it detects the word .
