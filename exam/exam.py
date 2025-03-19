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

    prev = []
    while True:
        cls()
        print("Press Enter key")
        if input() == "q":
            break;

        cls()
        while True:
            num = random.randint(0, len(data) - 1)
            if num not in prev:
                break
        
        if len(prev) >= len(data) - 2:     
            prev = prev[1:]

        prev.append(num)

        print(data[num])

        if input() == "q":
            break

    cls()
    print("Program exit")   

