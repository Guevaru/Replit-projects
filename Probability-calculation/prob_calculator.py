import random
import copy

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
        else:
            for _ in range(num_balls):
                ball = random.choice(self.contents)
                self.contents.remove(ball)
                drawn_balls.append(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_count = {color: drawn_balls.count(color) for color in set(drawn_balls)}

        success = True
        for color, count in expected_balls.items():
            if drawn_balls_count.get(color, 0) < count:
                success = False
                break

        if success:
            successful_experiments += 1

    return successful_experiments / num_experiments
