#Ex4
filename = input("Enter file name: ")
try:
    with open(filename, 'r') as file:
        words = []
        for line in file:
            for word in line.split():
                if word not in words:
                    words.append(word)

        words.sort()
        print(words)

except FileNotFoundError:
    print("File not found:", filename)