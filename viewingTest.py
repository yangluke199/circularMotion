from manim import *

class RotatingArrowWithVGroup(Scene):
    def construct(self):
        # Create an arrow that will move and rotate
        arrow = Arrow(start=ORIGIN, end=[2, 2, 0], color=YELLOW, buff=0)

        # Create a label for the arrow
        label = Text("v", font_size=24)

        # Position the label at the tip of the arrow
        label.next_to(arrow.get_end(), UP)

        # Create a VGroup that contains both the arrow and the label
        arrow_group = VGroup(arrow, label)

        # Add the VGroup to the scene
        self.add(arrow_group)

        # Animate the entire group rotating in a circle
        self.play(Rotating(arrow_group, radians=PI, about_point=ORIGIN, run_time=2))
        self.wait()
