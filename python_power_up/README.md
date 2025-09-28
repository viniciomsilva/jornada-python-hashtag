# 💪 Python Power Up

The project automates the task of registering the products of the ` ../data/products.csv ` in the Python Journey system.

## #1. Technologies Used

* Pandas: Python library for data processing
* Pyautogui: automation library

```bash
pip install pandas pyautogui
```

> NOTE: If the installation of all requirements by the ` requirements.txt ` has already been done file, no longer need
> to install.

## #2. Project Flow

1. Import the data
2. Open the browser preferably
3. Login
   1. Access the system
   2. Login
4. Start product registration until the end of the database

## #3. About Scripts

```python
# script automation.py

import pandas as pd
import pyautogui as pg

class Automation:

    def __init__(self, db_filepath: str):
        self.df = pd.read_csv(db_filepath)  # read the CSV file and save it to a DataFrame structure

    # imitate the human step-by-step process of opening the system in the browser
    def open_system(self, system_url: str, navigator: str = "chrome") -> None:
        pg.hotkey("win", "q")
        pg.typewrite(navigator)
        pg.press("enter")
        pg.hotkey("ctrl", "t")
        pg.typewrite(system_url)
        pg.press("enter")

    def login(self, email: str, password: str,
        # coord is a Python dictionary with the Cartesian coordinates that map the click position to pyautogui
        coord: dict[str, int]
    ) -> None:
        pg.click(x=coord["x"], y=coord["y"])
        pg.typewrite(email)
        pg.press("tab")
        pg.typewrite(password)
        pg.press("tab")
        pg.press("enter")

    def register(self, coord: dict[str, int]) -> None:
        # for each index (row)
        for index in self.df.index:
            pg.click(x=coord["x"], y=coord["y"])  # click on the first field of the form

            # for each column
            for column in self.df.columns:
                if not pd.isna(self.df.loc[index, column]):  # verify if the value is NaN
                    pg.typewrite(str(self.df.loc[index, column]))  # fill the field with the column value
                pg.press("tab")  # go to next field

            pg.press("enter")  # submit the forma
            pg.hotkey("ctrl", "home")  # return to top

```
