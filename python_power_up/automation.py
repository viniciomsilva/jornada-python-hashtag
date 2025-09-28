import pandas as pd
import pyautogui as pg


class Automation:

    def __init__(self, db_filepath: str, pause: float = 0.5):
        pg.PAUSE = pause
        self.df = pd.read_csv(db_filepath)

    @staticmethod
    def view_mouse_pointer_position() -> None:
        print(pg.position())

    def open_system(self, system_url: str, navigator: str = "chrome") -> None:
        pg.hotkey("win", "q")
        pg.typewrite(navigator)
        pg.press("enter")
        pg.hotkey("ctrl", "t")
        pg.typewrite(system_url)
        pg.press("enter")

    def login(self, email: str, password: str, coord: dict[str, int]) -> None:
        pg.click(x=coord["x"], y=coord["y"])
        pg.typewrite(email)
        pg.press("tab")
        pg.typewrite(password)
        pg.press("tab")
        pg.press("enter")

    def register(self, coord: dict[str, int]) -> None:
        for index in self.df.index:
            pg.click(x=coord["x"], y=coord["y"])

            for column in self.df.columns:
                if not pd.isna(self.df.loc[index, column]):
                    pg.typewrite(str(self.df.loc[index, column]))
                pg.press("tab")

            pg.press("enter")
            pg.hotkey("ctrl", "home")
