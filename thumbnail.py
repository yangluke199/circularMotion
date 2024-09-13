from manim import *

class UniformCircularMotionThumbnail(Scene):
    def construct(self):
        # Create a circle path
        circle = Circle(radius=2, color=WHITE)

        # Create a ball at the edge of the circle
        ball = Dot(radius=0.2, color=BLUE).move_to(circle.point_from_proportion(0))

        # Create the velocity and centripetal force vectors
        velocity_vector = Arrow(start=ball.get_center(), end=[3, 0, 0], color=YELLOW, buff=0)
        centripetal_vector = Arrow(start=ball.get_center(), end=[0, 0, 0], color=RED, buff=0)

        # Animate the ball in a circular motion
        self.play(Create(circle))
        self.play(FadeIn(ball))
        self.play(Create(velocity_vector), Create(centripetal_vector))

        # Add text
        text = Text("Uniform Circular Motion", font_size=48, color=WHITE).to_edge(UP)

        # Show text on screen
        self.play(Write(text))

        # Keep the final frame
        self.wait(2)
