def read_input(file_path):
    file = open(file_path, 'r')
    return file.read()


input_lines = read_input("day_10.txt")
print(input_lines)