from os import getcwd, path
from time import sleep

from automation import Automation


if __name__ == "__main__":
    auto = Automation(
        db_filepath=path.join(getcwd(), "databases", "products.csv"),
        system_url="https://dlp.hashtagtreinamentos.com/python/intensivao/login",
        login_screen={"x": 795, "y": 380},
        registration_screen={"x": 725, "y": 250}
    )

    auto.open_system(navigate_name="edge")
    sleep(3)
    auto.login(email="my@mail.com", password="qwe123@")
    sleep(3)
    auto.register()
