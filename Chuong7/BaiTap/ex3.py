def bai_tap_3():
    # Kiểm tra tên tập tin 'na na boo boo' và xử lý lỗi File Not Found.

    filename = input("Enter the file name: ")

    if filename.strip().lower() == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        return

    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"There were {line_count} subject lines in {filename}.")

    except FileNotFoundError:
        print("File cannot be opened: " + filename)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

bai_tap_3()