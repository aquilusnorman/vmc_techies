import RPi.GPIO as GPIO
from time import sleep

def acceptCash():
    cash = int(input("Insert Cash : "))
    return cash

if  __name__ == "__main__":
    acceptCash()
