import sys

def find_pairs(numbers):
    pairs = []
    seen = set()

    for num in numbers:
        target = 10 - num
        if target in seen:
            pairs.append((target, num))
        seen.add(num)

    return pairs

if __name__ == '__main__':
    numbers = [int(num) for num in sys.argv[1:]]
    
    pairs = find_pairs(numbers)
    for pair in pairs:
        print(f"{pair[0]} + {pair[1]}")
