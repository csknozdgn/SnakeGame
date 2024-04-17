import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()
        self.snake = [(200, 200)]
        self.food = self.spawn_food()
        self.direction = (0, -1)
        self.root.bind("<KeyPress>", self.change_direction)
        self.update()

    def spawn_food(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        return x, y

    def change_direction(self, event):
        key = event.keysym
        if key == "Up":
            self.direction = (0, -1)
        elif key == "Down":
            self.direction = (0, 1)
        elif key == "Left":
            self.direction = (-1, 0)
        elif key == "Right":
            self.direction = (1, 0)

    def update(self):
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0] * 10, head_y + self.direction[1] * 10)
        # Duvarlardan geçiş kontrolü
        if 0 <= new_head[0] < 400 and 0 <= new_head[1] < 400:
            self.snake.insert(0, new_head)
            if new_head == self.food:
                self.food = self.spawn_food()
            else:
                self.snake.pop()

            self.canvas.delete("all")
            for segment in self.snake:
                x, y = segment
                self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green")

            fx, fy = self.food
            self.canvas.create_oval(fx, fy, fx + 10, fy + 10, fill="red")
        else:
            self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("Helvetica", 24), anchor="center")
            self.root.after(2000, self.root.destroy)  # Oyunu kapat

        self.root.after(100, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
