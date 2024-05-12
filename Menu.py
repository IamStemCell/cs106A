#MainMenuInteractive

from turtle import *
import turtle
import math
import colorsys

from Mod1 import *
from Mod2 import *
from Mod3 import *
from Mod4 import *
from Mod5 import *
from Mod6 import *


def main():
    welcome_message()
    
    while True:
        
        display_menu()
        choice = input("Enter the number of the concept you want to run (1-6), or type '7' to exit: ")
        if choice == '1':
            print("You have chosen Square The Circle.")
            run_module1()
        elif choice == '2':
            print("You have chosen Pentagonal Nautilus.")
            run_module2()
        elif choice == '3':
            print("You have chosen De Nive Sexangulae.")
            run_module3()     
        elif choice == '4':
            print("You have chosen Heptagonal Rainbow.")
            run_module4()
        elif choice == '5':
            print("You have chosen Cyber Flower.")
            run_module5()
        elif choice == '6':
            print("You have chosen Phyllotaxis Girasole")
            run_module6()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def welcome_message():
    print("Welcome to the Abstract Art Exhibit!")
    print("Let's take you on a journey of exploration how truly beautiful math can be, with little help of Python graphic module.")

def run_module1():
          exec(open("Mod1.py").read())

def run_module2():
          exec(open("Mod2.py").read())
          
def run_module3():
          exec(open("Mod3.py").read())

def run_module4():
          exec(open("Mod4.py").read())

def run_module5():
          exec(open("Mod5.py").read())

def run_module6():
          exec(open("Mod6.py").read())


def display_menu():
     
    print("Please choose from the following abstract art concepts:")
    print("1. Square The Circle")
    print("2. Pentagonal Nautilus")
    print("3. De Nive Sexangulae")
    print("4. Heptagonal Rainbow")
    print("5. Cyber Flower")
    print("6. Phyllotaxis Girasole")
    print("7. Exit")


if __name__ == "__main__":
    main()

