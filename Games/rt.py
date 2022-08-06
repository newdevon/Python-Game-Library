"""Reaction Time

Hit Enter when Go is shown, using time and random module
"""
import time, random

def reaction_time():
    while True:
        print("\nWelcome to Reaction Time")
        time.sleep(0.5)
        print("\nLet's see how fast your reflexes are")
        time.sleep(0.75)
        print("\nLet's get started")
        time.sleep(1)
        print("On you marks")
        time.sleep(0.5)
        print("Get set")
        time.sleep(random.uniform(1,5))
        print("\nGO!!! PRESS NOW!!!")
        now = time.time()
        input()
        later = time.time()
        print(f"\nYou reacted in {later - now} seconds")
        time.sleep(1)
        
        play_again = input("Try again (yes/no)? ")
        if play_again != "yes":
            break     