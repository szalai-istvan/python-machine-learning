import time
class Header:
    def __init__(self):
        self.score = 0
        self.startTime = time.time_ns()

        file = open('highscore.txt')
        self.highScore = int(file.read())
        file.close()

    def getTime(self):
        now = time.time_ns()
        start = self.startTime
        seconds = (now - start) // 1_000_000_000
        minutes = seconds // 60
        seconds = seconds % 60
        additionalZeroMinutes = '0' if minutes < 10 else ''
        additionalZeroSeconds = '0' if seconds < 10 else ''
        return f'{additionalZeroMinutes}{minutes}:{additionalZeroSeconds}{seconds}'

    def getHeader(self, increment: bool = False):
        if increment:
            self.score += 1
        return f'Snake game - Time: {self.getTime()} - Score: {self.score} - High score: {self.highScore}'

    def gameOver(self):
        if self.score > self.highScore:
            open('highscore.txt', 'w').close()
            file = open('highscore.txt', 'w')
            file.write(str(self.score))
            file.close()
            return f'Game over! {self.score} is a new high score! Nice job!'
        return 'Game over!'