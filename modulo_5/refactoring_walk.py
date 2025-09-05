class RandomWalk:
    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)
