def bai_tap_1():
    # Đọc tập tin và in ra nội dung từng dòng dưới dạng chữ hoa.
    filename = input("Enter a file name: ")
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.upper(), end='')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

bai_tap_1()