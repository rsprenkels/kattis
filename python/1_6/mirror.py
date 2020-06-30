def mirror(image):
    return [line[::-1] for line in image][::-1]

for test_case in range(int(input())):
    print(f"Test {test_case + 1}")
    image = []
    rows, cols = list(map(int, input().split()))
    for _ in range(rows):
        image.append(input())
    for line in mirror(image):
        print(line)
        
# from 359.5 1072 to 361.1 1060       