import sys, random

print("welcome Name Picker \n")
print("A name just like sean world pick for Gus\n")

first = ('sato', 'kato', 'ito', 'kudo')
last = ('hanako', 'taro', 'ichiro', 'sestuko')

while True:
    firstName = random.choice(first)
    lastName  = random.choice(last)

    print("\n\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
    if try_again.lower() == "n" :
        break

input("\nPress Enter to exit")