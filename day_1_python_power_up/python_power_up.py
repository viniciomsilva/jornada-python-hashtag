from os import getcwd, path
from time import sleep

import pandas as pd
import pyautogui as auto

# definir valores constantes
DB_FILEPATH: str = path.join(getcwd(), "day_1_python_power_up", "products.csv")
SYSTEMA_URL: str = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
POSITIONS: list = [
    [795, 380],  # posição do clique na tela de login
    [725, 250],  # posição do clique na tela de cadastro
]
TIME_SLEEP: int = 2

auto.PAUSE = 0.4  # valor de delay entre os comandos o pyautogui


def get_position():
    sleep(5)
    print(auto.position())


def power_up() -> None:
    # carrega a base de dados
    dataframe = pd.read_csv(DB_FILEPATH)
    print(dataframe.info())

    auto.hotkey("win", "q")
    auto.write("edge")
    auto.press("enter")
    auto.hotkey("win", "up")
    auto.press("f4")
    auto.write(SYSTEMA_URL)
    auto.press("enter")

    sleep(TIME_SLEEP)

    auto.click(x=POSITIONS[0][0], y=POSITIONS[0][1])
    auto.write("test@test.com")
    auto.press("tab")
    auto.write("qwe123@")
    auto.press("tab")
    auto.press("enter")

    sleep(TIME_SLEEP)

    for row in dataframe.index:
        auto.click(x=POSITIONS[1][0], y=POSITIONS[1][1])

        auto.write(dataframe.loc[row, "codigo"])
        auto.press("tab")

        auto.write(dataframe.loc[row, "marca"])
        auto.press("tab")

        auto.write(dataframe.loc[row, "tipo"])
        auto.press("tab")

        auto.write(str(dataframe.loc[row, "categoria"]))
        auto.press("tab")

        auto.write(str(dataframe.loc[row, "preco_unitario"]))
        auto.press("tab")

        auto.write(str(dataframe.loc[row, "custo"]))
        auto.press("tab")

        obs = dataframe.loc[row, "obs"]
        if not pd.isna(obs):
            auto.write(obs)
        auto.press("tab")

        auto.press("enter")
        auto.hotkey("ctrl", "home")


power_up()
