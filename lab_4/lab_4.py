def analyze_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        total_lines = len(lines)
        empty_lines = lines.count('\n')
        lines_with_z = sum('z' in line for line in lines)
        z_count = sum(line.count('z') for line in lines)
        lines_with_and = sum('and' in line for line in lines)

        print(f"File: {file_path}")
        print(f"total lines: {total_lines}")
        print(f"empty lines: {empty_lines}")
        print(f"lines with 'z': {lines_with_z}")
        print(f"'z' count: {z_count}")
        print(f"lines with 'and': {lines_with_and}")


if __name__ == '__main__':
    while True:
        file_path = input("Enter the file path (or 'q' to quit): ")
        if file_path == 'q':
            break

        analyze_file(file_path)
        