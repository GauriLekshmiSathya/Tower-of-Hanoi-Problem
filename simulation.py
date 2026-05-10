import tkinter as tk
import time

NUM_DISKS = 5
WIDTH = 800
HEIGHT = 400

root = tk.Tk()
root.title("Tower of Hanoi")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

tx = [200, 400, 600]
ty = 300

for x in tx:
    canvas.create_rectangle(x - 5, 100, x + 5, ty, fill="black")

canvas.create_rectangle(100, ty, 700, ty + 10, fill="black")

towers = {
    'A': list(range(NUM_DISKS, 0, -1)),
    'B': [],
    'C': []
}

obj = {}

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def draw():
    canvas.delete("disk")

    for tower_name, disks in towers.items():
        x = tx[ord(tower_name) - ord('A')]

        for i, disk in enumerate(disks):
            y = ty - (i + 1) * 20

            width = disk * 25
            rect = canvas.create_rectangle(
                x - width,
                y,
                x + width,
                y + 20,
                fill=colors[disk % len(colors)],
                tags="disk"
            )

            obj[disk] = rect

    root.update()

draw()

def move(s, d):
    disk = towers[s].pop()
    towers[d].append(disk)

    draw()
    time.sleep(0.5)

def toh(n, s, a, d):
    if n == 1:
        move(s, d)
        return

    toh(n - 1, s, d, a)

    move(s, d)

    toh(n - 1, a, s, d)

root.update()
time.sleep(1)

toh(NUM_DISKS, 'A', 'B', 'C')

root.mainloop()