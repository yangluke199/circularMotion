from manim import *

template = TexTemplate(preamble=r'\usepackage{ulem}')

class UniformCircularMotionExplained(MovingCameraScene):
    def construct(self):



        intro_text = Tex("What is Uniform Circular Motion?", font_size=48)
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
        self.camera.frame.animate.scale(0.65),
        lag_ratio=0  # Ensure animations run simultaneously
    )
)

        centripetal_arrow = always_redraw(
            lambda: Arrow(
                start=ball.get_center(),  # Start at the ball
                end=ball.get_center() + 0.8 * (ORIGIN - ball.get_center()),  # Small buffer space from the ball
                buff=-1,
                color=RED,
            )
        )


        self.add(centripetal_arrow)


        # Move the ball along the circle path while the arrow continuously points to the center
        self.play(MoveAlongPath(ball, circle, run_time=4, rate_func=linear))

        eq0 = MathTex(r"\text{where } v = |\vec{v}|,")
        eq1 = MathTex(r"a_c = \frac{v^2}{r} = r\omega^2 = v\omega")  # Centripetal acceleration
        eq2 = MathTex(r"v = r \omega") # Linear velocity
        eq3 = MathTex(r"T = \frac{2\pi}{r} = 2\pi f")  # Period of rotation

                # Arrange the equations vertically
        equations = VGroup(eq0, eq1, eq2, eq3)

        equations.arrange(DOWN, buff=1).scale(0.5).shift(RIGHT * 4)

        box = SurroundingRectangle(equations, color=WHITE, buff=0.2)

        self.play(
        AnimationGroup(
        MoveAlongPath(ball, circle, run_time=4, rate_func=linear),
        self.camera.frame.animate.shift(RIGHT * 1.5),
        Write(equations),
        Create(box, reverse=False),
        lag_ratio=0.1  # Ensure animations run simultaneously
    ))

        self.play(MoveAlongPath(ball, circle), run_time=4, rate_func=linear)

        self.play(FadeOut(ball), FadeOut(box), FadeOut(circle), FadeOut(centripetal_arrow), FadeOut(equations), self.camera.frame.animate.scale(1/0.65).shift(LEFT * 1.5))

        ball = Dot(color=WHITE).move_to([-4, 2, 0])
        self.play(Create(ball))

        velocity_arrow = Arrow(ball.get_center() + RIGHT * 0.2, ball.get_center() + RIGHT * 1.2, buff=0, color=GREEN)

        self.play(GrowArrow(velocity_arrow), run_time=0.5)

        self.wait(0.5)

        self.play(FadeOut(velocity_arrow), run_time=0.1)

        velocity_text = always_redraw(lambda:
                                      Tex("Constant Speed", font_size=28, color=GREEN).next_to(ball.get_center(), UP)
                                     )

        # ball is travelling rightwards at 0.5 units per second.

        self.play(ball.animate.shift(RIGHT * 0.5), run_time=1, rate_func=rate_functions.linear)
        self.add(velocity_text)
        self.play(ball.animate.move_to([-0.5, 2, 0]), run_time=6, rate_func=rate_functions.linear)



        circle = Circle(radius=2, color=BLUE).reverse_direction().move_to(ORIGIN).rotate(PI/2)
        self.play(
        ball.animate.move_to([0, 2, 0]),
        Create(circle),
        run_time=1,
        rate_func=rate_functions.linear
)
        self.play(MoveAlongPath(ball, circle), run_time=8 * PI, rate_func=linear)

        self.play(FadeOut(ball), FadeOut(circle), FadeOut(velocity_text))

        ball = Dot(color=WHITE).move_to([-4, 2, 0])
        self.play(Create(ball))

        velocity_arrow = Arrow(ball.get_center() + RIGHT * 0.2, ball.get_center() + RIGHT * 1.2, buff=0, color=GREEN)

        self.play(GrowArrow(velocity_arrow), run_time=0.5)

        self.wait(0.5)

        self.play(FadeOut(velocity_arrow), run_time=0.1)

        velocity_text = always_redraw(lambda:
                                      Text("Constant Speed", font_size=28, color=GREEN).next_to(ball.get_center(), UP)
                                     )

        # ball is travelling rightwards at 0.5 units per second.

        self.play(ball.animate.shift(RIGHT * 0.5), run_time=1, rate_func=rate_functions.linear)
        self.add(velocity_text)
        self.play(ball.animate.move_to([-0.5, 2, 0]), run_time=6, rate_func=rate_functions.linear)



        circle = Circle(radius=2, color=BLUE).reverse_direction().move_to(ORIGIN).rotate(PI/2)
        self.play(
        ball.animate.move_to([0, 2, 0]),
        Create(circle),
        run_time=1,
        rate_func=rate_functions.linear
)

        centripetal_arrow2 = always_redraw(
            lambda: Arrow(
                start=ball.get_center(),  # Start at the ball
                end=ball.get_center() + 0.8 * (ORIGIN - ball.get_center()),  # Small buffer space from the ball
                color=RED,
                buff=-1
            )
        )

        centripetal_force_label = Tex("Centripetal Force", color=RED, font_size=17)

        centripetal_force_label.move_to(centripetal_arrow2.get_left() + LEFT * 0.61)



        self.camera.frame.save_state()

        self.play(
            GrowArrow(centripetal_arrow2),
            self.camera.frame.animate.scale(0.5).move_to(ball)
        )

        self.camera.frame.add_updater(lambda m: m.move_to(ball.get_center()))

        self.wait(1)



        velocity_text2 = always_redraw(lambda:
            Tex("Constant Speed", font_size=28, color=GREEN)
            .next_to(ball.get_center(), UP)
            .set_opacity(0.4)  # Keep the desired opacity
            .scale(0.6)  # Keep the desired scale
        )

        self.play(Write(centripetal_force_label), FadeOut(velocity_text, run_time=0.5), FadeIn(velocity_text2))

        centripetal_force_label_tracking = always_redraw(
            lambda: Tex(r"\textbf{Centripetal Force}", font_size=17, color=RED)
            .move_to(centripetal_arrow2.get_left() + LEFT * 0.61).move_to(centripetal_arrow2.get_left()  + UP * 0.15 + RIGHT * 0.05).rotate( 90 * DEGREES).scale(0.65)
        )

        self.play(Transform(centripetal_force_label, centripetal_force_label_tracking)
        )

        self.wait(2)

        linear_velocity_arrow = always_redraw(
            lambda: Arrow(
                start=ball.get_center(),  # Start at the ball
                # Perpendicular velocity vector: normalize the tangent direction
                end=ball.get_center() + 0.85 * normalize(rotate_vector(ORIGIN - ball.get_center(), angle=PI / 2)),  # Small buffer space from the ball
                color=PURPLE,
                buff=-1
            )
        )

        self.play(GrowArrow(linear_velocity_arrow))

        linear_velocity_text = Tex("Velocity", font_size=12).next_to(linear_velocity_arrow, UP, buff=-0.05).set_color(PURPLE).shift( LEFT * 0.1)

        self.play(Write(linear_velocity_text))

        self.wait(2)

        linear_velocity_text2 = Tex(r"\textbf{Linear Velocity{", font_size=7.6).next_to(linear_velocity_arrow, UP, buff=-0.05).set_color(PURPLE).shift( LEFT * 0.095)

        linear_velocity_text_2 = always_redraw(
            lambda: Tex(r"\textbf{Linear Velocity}", font_size=7.6)
            .next_to(linear_velocity_arrow, UP, buff=-0.05).set_color(PURPLE).shift( LEFT * 0.095)
        )

        self.play(Transform(linear_velocity_text, linear_velocity_text2))

        self.play(
        MoveAlongPath(ball, circle),
        Rotate(velocity_text2, angle=-2 * PI, about_point=circle.get_center()),
        Rotate(centripetal_force_label, angle=-2 * PI, about_point=circle.get_center()),
        Rotate(linear_velocity_text, angle=-2 * PI, about_point=circle.get_center()),
        run_time=8, rate_func=linear)

        self.wait(3)

        self.play(
            AnimationGroup(
                FadeOut(velocity_text2, centripetal_force_label, linear_velocity_text, circle, ball, centripetal_arrow2, linear_velocity_arrow, run_time=0.5),
                self.camera.frame.animate.move_to(ORIGIN).set_width(config["frame_width"]).set_rotation(0),
                lag_ratio=0  # This ensures both animations start at the same time
            )
        )

        self.wait(3)
