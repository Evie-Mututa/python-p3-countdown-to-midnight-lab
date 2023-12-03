#function without the pause between each count:
def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print("HAPPY NEW YEAR!")

#function with a one second pause between each count
import time

def countdown_with_sleep(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        time.sleep(1)  # Pauses for 1 second
        number -= 1
    print("HAPPY NEW YEAR!")


