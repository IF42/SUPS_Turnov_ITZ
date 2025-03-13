import json
import sys
import random
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


if __name__ == "__main__":
    assert len(sys.argv) > 1
 
    with open(sys.argv[-1], 'r') as file:
        data = json.load(file)

    while True:
        cls()
        print("Press Enter key")
        input()

        cls()
        num = random.randint(0, len(data) - 1)
        print(data[num])

        if input() == "q":
            break

    cls()
    print("Program exit")   

