def main():
    with open('out/stairway.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.endswith('\n') or line.endswith('\r\n'):
                print(line, end='')
            else:
                print(line)

if __name__ == '__main__':
    main()