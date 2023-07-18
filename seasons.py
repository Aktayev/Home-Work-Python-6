from datetime import date
import inflect
import sys
import re

def main():

    bd = (input("Birth date is: "))
    minuts = min_at_bd(bd)
    words = number_to_words(minuts)
    print(f"{words} minuts")

def min_at_bd(data):
    if date_1 := re.search(r"^([0-9]{4})-([0-9]{2})\-([0-9]{2})$", data):
        date_1 = date.fromisoformat(data)
        today = date.today()
        date_dif = today - date_1
        date_str = str(date_dif)
        day, string, time = date_str.split(' ')
        minuts = int(day) * 24 * 60
        print(minuts)
    else:
        sys.exit("Please enter correct date type YYYY-MM-DD")
    return minuts

def number_to_words(min):
    p = inflect.engine()
    words = p.number_to_words(min, andword="")
    return words

if __name__ =="__main__":
    main()


