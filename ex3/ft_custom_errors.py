class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        Exception.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        Exception.__init__(self, message)


def raise_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("\nTesting PlantError...")
    try:
        raise_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        raise_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise_plant_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        raise_water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
