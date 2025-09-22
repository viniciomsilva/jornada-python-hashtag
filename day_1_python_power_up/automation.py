import pandas as pd
import pyautogui as pa


class Automation:

    def __init__(
        self,
        db_filepath: str,
        system_url: str,
        pause: float = 0.5,
        login_screen: dict = {"x": 0, "y": 0},
        registration_screen: dict = {"x": 0, "y": 0}
    ):
        pa.PAUSE = pause

        self.system_url = system_url
        self.df = pd.read_csv(db_filepath)
        self.mouse_pointer_positions: dict = {
            "login_screen": login_screen,
            "registration_screen": registration_screen
        }

        print(self.df.info())

    @staticmethod
    def view_mouse_pointer_position() -> None:
        print(pa.position())

    def open_system(self, navigate_name: str = "chrome") -> None:
        pa.hotkey("win", "q")
        pa.write(navigate_name)
        pa.press("enter")
        pa.write(self.system_url)
        pa.press("enter")

    def login(self, email: str, password: str) -> None:
        pa.click(
            x=self.mouse_pointer_positions["login_screen"]["x"],
            y=self.mouse_pointer_positions["login_screen"]["y"]
        )
        pa.write(email)
        pa.press("tab")
        pa.write(password)
        pa.press("tab")
        pa.press("enter")

    def register(self) -> None:
        for row in self.df.index:
            pa.click(
                x=self.mouse_pointer_positions["registration_screen"]["x"],
                y=self.mouse_pointer_positions["registration_screen"]["y"]
            )
            pa.write(self.df.loc[row, "codigo"])
            pa.press("tab")
            pa.write(self.df.loc[row, "marca"])
            pa.press("tab")
            pa.write(self.df.loc[row, "tipo"])
            pa.press("tab")
            pa.write(str(self.df.loc[row, "categoria"]))
            pa.press("tab")
            pa.write(str(self.df.loc[row, "preco_unitario"]))
            pa.press("tab")
            pa.write(str(self.df.loc[row, "custo"]))
            pa.press("tab")

            if not pd.isna(self.df.loc[row, "obs"]):
                pa.write(self.df.loc[row, "obs"])

            pa.press("tab")
            pa.press("enter")
            pa.hotkey("ctrl", "home")
