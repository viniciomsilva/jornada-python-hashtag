from pathlib import Path


def get() -> str:
    with open(
        file=Path(__file__).parent.parent.joinpath(
            "data", "api_key.txt"
        ).resolve()
    ) as file:
        return file.read().strip()
