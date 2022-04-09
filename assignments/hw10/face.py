from graphics import Circle, Line


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.size = size
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        face = self.head
        left_eye = self.left_eye
        right_eye = self.right_eye
        top_mouth = self.mouth
        sides = top_mouth.clone()
        side_1 = Line(sides/2, sides/2)
        side_2 = Line(sides/2 + 100, sides/2 + 100)
        side_1.draw(self.window)
        side_2.draw(self.window)
        face.draw(self.window)
        left_eye.draw(self.window)
        right_eye.draw(self.window)
        top_mouth.draw(self.window)

    def shock(self):
        face = self.head
        left_eye = self.left_eye
        right_eye = self.right_eye
        top_mouth = self.mouth
        top_mouth.undraw()
        shock_center = self.mouth.getCenter()
        shock_mouth = Circle(shock_center, self.size/4)

        face.draw(self.window)
        left_eye.draw(self.window)
        right_eye.draw(self.window)
        shock_mouth.draw(self.window)




    def wink(self):
        face = self.head
        left_eye_open = self.left_eye
        right_eye = self.right_eye
        top_mouth = self.mouth
        left_eye_open.undraw()

        left_eye_wink = Line(self.size/2, self.size/2)
        sides = top_mouth.clone()
        side_1 = Line(sides / 2,sides / 2)
        side_2 = Line(sides / 2 + 100,sides / 2 + 100)
        side_1.draw(self.window)
        side_2.draw(self.window)
        face.draw(self.window)
        left_eye_wink.draw(self.window)
        right_eye.draw(self.window)
        top_mouth.draw(self.window)

