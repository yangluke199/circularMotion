from manim import *

class viewingTest(Scene):
    def construct(self):

        dot1 = Dot().move_to(ORIGIN)
        dot2 = Dot().move_to([-7, 0, 0])
        dot3 = Dot().move_to([7, 0, 0])
        dot4 = Dot().move_to([0, 4, 0])
        dot5 = Dot().move_to([0, -4, 0])

        self.play(Create(dot1), Create(dot2), Create(dot3), Create(dot4), Create(dot5) )
