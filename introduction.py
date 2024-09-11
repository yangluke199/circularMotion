from manim import *

template = TexTemplate(preamble=r'\usepackage{ulem}')

class UniformCircularMotionExplained(MovingCameraScene):
    def construct(self):
        
        
        
        intro_text = Text("What is Uniform Circular Motion?", font_size=48)
        intro_box = SurroundingRectangle(intro_text, color=BLUE, buff=0.2)
        underline = Line(start=LEFT, end=RIGHT).set_width(intro_text.width).next_to(intro_text, DOWN, buff=0.1)
        
        # Group the text, box, and underline
        intro_group = VGroup(intro_text, intro_box, underline).move_to(ORIGIN)
        
        # Play the animation of the text appearing
        self.play(Write(intro_text), Create(intro_box), Create(underline))
        self.wait(1)

        # Move the group to the top of the screen
        self.play(
            intro_group.animate.scale(0.6).shift(UP * 3),  # Scale down and move to the top
            run_time=2
        )
        self.wait(2)

        ball = Dot(color=WHITE).move_to(ORIGIN)
        ball2 = ball.copy().shift(LEFT * 2)
        circle = Circle(radius=2, color=BLUE).reverse_direction().move_to(ORIGIN)
        self.play(GrowFromCenter(circle), Create(ball))
        self.play(Rotate(circle, angle=-PI))
        self.play(Transform(ball, ball2))
        
        self.play(MoveAlongPath(ball, circle), run_time=4, rate_func=linear)
        self.play(
        AnimationGroup(
        MoveAlongPath(ball, circle, run_time=4, rate_func=linear),  # Ball keeps moving
        FadeOut(intro_group, run_time=1),
        self.camera.frame.animate.scale(0.8),
        lag_ratio=0  # Ensure animations run simultaneously
    )
)
        
        centripetal_arrow = always_redraw(
            lambda: Arrow(
                start=ball.get_center(),  # Start at the ball
                end=ball.get_center() + 1 * (ORIGIN - ball.get_center()),  # End at the center of the circle
                buff=0.15,  # Small buffer space from the ball
                color=RED
            )
        )
        
            
        self.add(centripetal_arrow)
        
        # Move the ball along the circle path while the arrow continuously points to the center
        self.play(MoveAlongPath(ball, circle, run_time=4, rate_func=linear))
        
        
        
        self.play(MoveAlongPath(ball, circle), run_time=4, rate_func=linear)
        
        
        
        
        
        self.play(FadeOut(ball), FadeOut(circle), FadeOut(centripetal_arrow))
        
        ball = Dot(color=YELLOW).move_to(LEFT * 4)
        self.play(FadeIn(ball))


        
        velocity_arrow = Arrow(ball.get_center() + RIGHT * 0.2, ball.get_center() + RIGHT * 1.2, buff=0, color=GREEN)
        self.play(Create(velocity_arrow))
        
        
        
        self.wait(1.5)
        
        self.play(FadeOut(velocity_arrow))
        
        velocity_text = always_redraw(lambda: 
                                      Text("Constant Speed", font_size=28, color=GREEN).next_to(ball.get_center(), UP)
                                     )
        
        # ball is travelling rightwards at 0.5 units per second.
        
        self.play(ball.animate.shift(RIGHT * 0.5), run_time=1, rate_func=rate_functions.linear)
        self.add(velocity_text)
        self.play(ball.animate.move_to(ORIGIN + LEFT * 0.5), run_time=6, rate_func=rate_functions.linear)
        
        
        circle = Circle(radius=1, color=BLUE).reverse_direction().move_to(DOWN * 1).rotate(PI/2)
        self.play(
        ball.animate.move_to(ORIGIN), 
        Create(circle), 
        run_time=1, 
        rate_func=rate_functions.linear
)
        self.play(MoveAlongPath(ball, circle), run_time=4 * PI, rate_func=linear)
        
        yellowball = Dot(color=YELLOW).move_to( LEFT * 5 + UP * 2)
        
        self.play(FadeOut(ball), FadeOut(circle), FadeOut(velocity_text), FadeIn(yellowball))
        
        self.wait(3)
        
        
        