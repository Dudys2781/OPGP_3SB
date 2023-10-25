width = 30
height = 10
colors = {
    "red": "\033[91m\u2588\033[0m",
    "white": "\u2588",
    "blue": "\033[94m\u2588\033[0m",
}

for j in range(2):
    print(width * colors['white'])
for i in range(2):
    print(width * colors['blue'])
for x in range(2):
    print(width * colors['red'])

