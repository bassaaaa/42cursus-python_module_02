class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def raise_error(error: GardenError) -> None:
    raise error


def test_plant_error(error: PlantError) -> None:
    print("\nTesting PlantError...")
    try:
        raise_error(error)
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error(error: WaterError) -> None:
    print("\nTesting WaterError...")
    try:
        raise_error(error)
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_all_garden_errors(errors: list[GardenError]) -> None:
    print("\nTesting catching all garden errors...")
    for error in errors:
        try:
            raise_error(error)
        except GardenError as e:
            print(f"Caught GardenError: {e}")


def test_unknown_errors(errors: list[GardenError]) -> None:
    print("\nTesting unknown errors...")
    for error in errors:
        try:
            raise_error(error)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
        except WaterError as e:
            print(f"Caught WaterError: {e}")
        except GardenError as e:
            print(f"Caught GardenError: {e}")


def test_custom_errors() -> None:
    plant_error = PlantError("The tomato plant is wilting!")
    water_error = WaterError("Not enough water in the tank!")

    test_plant_error(plant_error)
    test_water_error(water_error)
    test_all_garden_errors([plant_error, water_error])
    test_unknown_errors([PlantError(), WaterError(), GardenError()])


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
