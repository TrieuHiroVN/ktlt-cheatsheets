def bai_tap_2():
    # Tính giá trị trung bình của 'X-DSPAM-Confidence:' trong tập tin.
    filename = input("Enter the file name: ")
    confidence_values = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith("X-DSPAM-Confidence:"):
                    try:
                        confidence = float(line.split(':')[1].strip())
                        confidence_values.append(confidence)
                    except (ValueError, IndexError):
                        continue

        count = len(confidence_values)
        if count == 0:
            print(f"No 'X-DSPAM-Confidence:' lines found in {filename}.")
        else:
            average_confidence = sum(confidence_values) / count
            print(f"Average spam confidence: {average_confidence}")

    except FileNotFoundError:
        print(f"File cannot be opened: {filename}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

bai_tap_2()