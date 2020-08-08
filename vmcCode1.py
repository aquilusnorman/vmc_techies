####################
## Aquilus Norman ##
####################
import mariadb
import sys
import RPi.GPIO as GPIO
from time import sleep

# ITEMS AND PRICES
#items = []
prices = []

# DATABASE CONNECTION
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="vmcdb"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()
cur.execute("SELECT item_price FROM item_stock")

for i in cur:
    prices.append(i)

# PINS
leds = [4, 23, 12, 20] # LEDS
btns = [17, 25, 13, 21] # BUTTONS
mtrs = [6, 19, 26, 16] # MOTORS

# PREPARE RPI PINS
def prepareGPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    #SETUP
    GPIO.setup(leds, GPIO.OUT) # LED SETUP
    GPIO.setup(btns, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # BUTTONS SETUP
    GPIO.setup(mtrs, GPIO.OUT) # MOTORS SETUP

# ACCEPT CASH
def acceptCash():
    cash = int(input("Insert Cash : "))
    return cash

# MAIN FUNCTION
if  __name__ == "__main__":

    available_items = []

    try:
        while True:
            cash = acceptCash()

            for i in prices:
                if cash > i:
                    available_items.append(prices.index(i))
                    GPIO.output(leds[prices.index(i)], GPIO.HIGH)
