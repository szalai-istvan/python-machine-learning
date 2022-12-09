class Header:
    def __init__(self):
        self.left = 0
        self.right = 0

    def score(self, direction: str):
        if direction == 'left':
            self.left += 1
        elif direction == 'right':
            self.right += 1

    def getHeader(self):
        return f'Pong - ({self.left} - {self.right})'