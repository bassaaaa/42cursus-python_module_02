def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    input1 = "25"
    input2 = "abc"
    try:
        print(f"Input data is '{input1}'")
        temp = input_temperature(input1)
        print(f"Temperature is now {temp}°C\n")
    except ValueError:
        print(
            f"Caught input_temperature error: "
            f"invalid literal for int() with base 10: '{input1}'\n"
        )

    try:
        print(f"Input data is '{input2}'")
        temp = input_temperature(input2)
        print(f"Temperature is now {temp}°C\n")
    except ValueError:
        print(
            f"Caught input_temperature error: "
            f"invalid literal for int() with base 10: '{input2}'\n"
        )

    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()


if __name__ == "__main__":
    main()
