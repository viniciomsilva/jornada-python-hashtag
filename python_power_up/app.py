from os import getcwd, path
from time import sleep

from automation import Automation


if __name__ == "__main__":
    auto = Automation(
        db_filepath=path.join(getcwd(), "data", "products.csv")
    )

    auto.open_system(
        navigator="edge",
        system_url="https://dlp.hashtagtreinamentos.com/python/intensivao/login"
    )
    sleep(3)

    auto.login(
        email="my@mail.com",
        password="qwe123@",
        coord={"x": 795, "y": 380}
    )
    sleep(3)

    auto.register(coord={"x": 725, "y": 250})
