# Ex5
filename = input("Enter name file: ")
try:
    with open(filename, 'r') as file:
        count = 0
        for line in file:
            line = line.strip()
            if line.startswith("From "):
                words = line.split()
                if len(words) >= 2:
                    print(words[1])
                    count += 1
        print("There were", count, "lines in the file with From as the first word")
except FileNotFoundError:
    print("File not found:", filename)
