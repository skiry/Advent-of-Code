HEIGHT = 6
WIDTH = 25

def main():
    best = float("inf")
    result = 0

    image = input()
    for index in range(0, len(image), HEIGHT * WIDTH):
        layer = image[index:HEIGHT * WIDTH + index]
        print(layer)
        zeros = layer.count("0")
        if zeros < best:
            print(zeros)
            best = zeros
            result = layer.count("1") * layer.count("2")
    return result

print(main())