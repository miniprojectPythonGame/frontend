import pygame

from .ItemBox import ItemBox


class ItemGrid:
    def __init__(self, x, y, item_size, item_padding, cols, amount, screen, backpack_ref):
        self.x = x
        self.y = y
        self.item_size = item_size
        self.item_padding = item_padding
        self.cols = cols
        self.amount = amount
        self.screen = screen
        self.backpack_ref = backpack_ref
        self.backpack = self.initateBackpack()

    def draw(self):
        for item in self.backpack:
            item.draw()

    def initateBackpack(self):
        backpack = []
        x = self.x
        y = self.y
        ib_offset = 20

        for i in range(len(self.backpack_ref)):
            backpack.append(
                ItemBox(x, y, self.item_size, self.item_size, self.screen,
                        path=self.backpack_ref[i]['img_path'], offset=ib_offset)
            )

            if i % self.cols == self.cols - 1:
                y += self.item_size + self.item_padding
                x = self.x
            else:
                x += self.item_size + self.item_padding

        for i in range(len(self.backpack_ref), self.amount):
            backpack.append(
                ItemBox(x, y, self.item_size, self.item_size, self.screen, offset=ib_offset)
            )

            if i % self.cols == self.cols - 1:
                y += self.item_size + self.item_padding
                x = self.x
            else:
                x += self.item_size + self.item_padding

        return backpack
