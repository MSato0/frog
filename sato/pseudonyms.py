"""project 1 : Funny Name Generator"""
import sys
import random

def main():
    """２つのタプルからランダムに名前を選んで画面に表示する"""
    print("welcome Name Picker \n")
    print("A name just like sean world pick for Gus\n")

    first = ('sato', 'kato', 'ito', 'kudo')
    last = ('hanako', 'taro', 'ichiro', 'sestuko')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        print("\n\n")
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit")

if __name__ == "__main__":
    main()
