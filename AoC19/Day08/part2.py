from collections import defaultdict
HEIGHT = 6
WIDTH = 25

def main():
    image = input()
    final_image = defaultdict(lambda:2)

    for index in range(0, len(image), HEIGHT * WIDTH):
        layer = image[index:HEIGHT * WIDTH + index]
        for idx, pixel in enumerate(layer):
            if final_image[idx] in [0, 1]:
                continue
            final_image[idx] = int(pixel)

    return "".join(str(x[1]) for x in sorted(final_image.items(), key=lambda x: x[0]))

print(main())
#8345d3bc-d654-46e3-b310-006c863ca954