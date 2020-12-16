class Pixel:
    def __init__(self, color: str):
        if color in ['B', 'W', 'R', 'G']:
            self.color = color
        else:
            raise ValueError('Введён неправильный цвет')


class Image:
    def __init__(self, width: int, height: int):
        self.image = []
        for self.y in range(height):
            self.image.append([])
            for _ in range(width):
                self.image[self.y].append(Pixel('G'))

    def set_color(self, color: str, x: int, y: int):
        if color in ['B', 'W', 'R', 'G']:
            self.image[y][x] = Pixel(color)
        else:
            raise ValueError('Введён неправильный цвет')

    def fill_rectangle(self, color: str, x1: int, y1: int, x2: int, y2: int):
        for self.x in range(x1 - 1, x2):
            for self.y in range(y1 - 1, y2):
                self.set_color(color, self.x, self.y)

    def __str__(self):
        img = ''
        for y in range(len(self.image)):
            for x in range(len(self.image[y])):
                img += self.image[y][x].color
            img += '\n'
        return img


img = Image(5, 7)
print(img)
img.fill_rectangle(color="B", x1=3, y1=3, x2=5, y2=7)
print(img)
img.fill_rectangle(color="R", x1=4, y1=5, x2=5, y2=7)
print(img)




