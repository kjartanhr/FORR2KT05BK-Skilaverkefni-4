def word_count(filename, word):
    counter = 0
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if word in line.split():
                counter += 1
    return counter

def main():
    print(word_count('out/stairway.txt', 'a'))

if __name__ == '__main__':
    main()