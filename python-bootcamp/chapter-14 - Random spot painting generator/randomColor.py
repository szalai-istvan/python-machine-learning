import random
def randomColor() -> tuple[int, int, int]:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b
