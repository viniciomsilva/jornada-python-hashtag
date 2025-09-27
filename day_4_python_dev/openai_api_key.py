from pathlib import Path


def get() -> str:
    with open(
        file=Path(__file__).parent.joinpath("api_key.txt").resolve()
    ) as file:
        return file.read().strip()


if __name__ == "__main__":
    print(get())
