import stairway_adder
import stairway_reader
import stairway_writer
import stairway_list_reader

from word_counter import word_count

def main():
    try:
        while True:
            menu = ["Skrifa fyrsta erindi í \"stairway.txt\"",
                    "Prenta \"stairway.txt\"",
                    "Bæta öðru erindi í \"stairway.txt\"",
                    "Prenta \"stairway.txt\" með readlines() aðferðinni",
                    "Telja orð í \"stairway.txt\"",
                    "Hætta"]

            for number, item in enumerate(menu):
                print(f"{number + 1}. {item}")

            choice = int(input("Veldu aðgerð úr listanum ~ "))

            if choice == 1:
                stairway_writer.main()
                print("Skrifaði fyrsta erindi í \"stairway.txt\"\n")
            elif choice == 2:
                try:
                    stairway_reader.main()
                except FileNotFoundError:
                    print("Skráin finnst ekki.\n")

            elif choice == 3:
                stairway_adder.main()
                print("Bætti öðru erindi við í \"stairway.txt\"\n")

            elif choice == 4:
                try:
                    stairway_list_reader.main()
                except FileNotFoundError:
                    print("Skráin finnst ekki.\n")

            elif choice == 5:
                word = input("Hvaða orð viltu finna? ~ ")
                try:
                    print(f"Orðið \"{word}\" kemur fyrir {word_count('out/stairway.txt', word)} sinnum.\n")
                except FileNotFoundError:
                    print("Skráin finnst ekki.\n")

            elif choice == 6:
                break

            else:
                print("Ógild aðgerð.\n")
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()