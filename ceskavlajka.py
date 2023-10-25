width = 30
height = 10
colors = {
    "red": "\033[91m\u2588\033[0m",
    "white": "\u2588",
    "blue": "\033[94m\u2588\033[0m",
}

for j in range(1, height//2 + 1):
    print(3*j * colors['blue'] + (width-j*2) * colors['white'])

for i in range(height//2 + 1, 0, -1):
    print(3*i * colors['blue'] + (width-i*2) * colors['red'])