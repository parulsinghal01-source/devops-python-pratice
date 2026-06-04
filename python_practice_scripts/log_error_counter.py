#! /usr/bin/python3

def count_errors(filename, error_message):
    count = 0

    with open(filename, "r") as file:
        for line in file:
            if error_message in line:
                count += 1

    return count


if __name__ == "__main__":
    filename = "app.log"
    error_message = "ERROR"

    result = count_errors(filename, error_message)
    print(f"Found {result} lines containing {error_message}")
