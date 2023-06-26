from manimlib import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_stroke(BLUE_E, width=4)

        self.play(ShowCreation(circle))
        self.wait()

        text = Text(text="""My name is Rahul""", t2c={"Rahul": RED})
        story = Text(text="""And this is my story""", t2c={"Story": ORANGE})

        VGroup(text, story).arrange(DOWN, buff=1)

        self.play(Write(text))
        self.wait()
        self.play(FadeIn(story, UP))
