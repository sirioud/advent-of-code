import os 

START_POSITION: int = 50
DIAL_SIZE: int = 100
FILE_PATH: str = "input.txt"

def read_txt(file_path: str) -> list[str]:
    """
    Reads a text file and returns its content as a string.

    Args:
        file_path (str): The path to the text file.

    Returns:
        list[str]: The content of the text file.
    """
    input: list[str] = []

    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")

    with open(file_path, 'r') as input_file:
        for line in input_file:
            input.append(line.strip())
    return input

  
def rotate(current_position: int, instruction: str) -> int:
    direction: str = instruction[0]
    distance: int = int(instruction[1:])
    
    if direction == 'L':
            rotated_number = (current_position - distance) % 100
    elif direction == 'R':
            rotated_number = (current_position + distance) % 100
    else:
        raise ValueError("Invalid direction. Use 'L' for left or 'R' for right.")
    return rotated_number

def solve(file_path: str) -> int:
    """
    Reads a text file containing rotation instructions and calculates the final position
    on a dial based on those instructions.

    Args:
        file_path (str): The path to the text file containing rotation instructions.
    """
    COUNTER: int = 0
    CURRENT_POSITION: int = START_POSITION

    try:
        instructions: list[str] = read_txt(file_path)
        for instruction in instructions:
            CURRENT_POSITION = rotate(CURRENT_POSITION, instruction)

            if CURRENT_POSITION == 0:   
                COUNTER += 1

        print(f"Final Position: {CURRENT_POSITION}, Total times zero was reached: {COUNTER}")

    except FileNotFoundError as e:
        print(e)
    
    return COUNTER

if __name__ == "__main__":
    
    Result:int=solve(FILE_PATH)

    print(f"The dial went through zero a total of {Result} times.")
    