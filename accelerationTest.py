from manim import *

class ProjectileMotion(Scene):
    def construct(self):
        # Constants for the motion
        initial_velocity_x = 4   # Initial horizontal velocity
        initial_velocity_y = 5   # Initial vertical velocity
        g = 9.8  # Gravitational acceleration

        # Create the ball as a dot or small circle
        ball = Dot(radius=0.2, color=BLUE)
        ball.move_to(ORIGIN)  # Start at the origin

        # Create a ValueTracker to track time
        time_tracker = ValueTracker(0)

        # Define a function to update the ball's position
        def update_ball(ball):
            t = time_tracker.get_value()
            new_x = initial_velocity_x * t  # Horizontal displacement
            new_y = initial_velocity_y * t - 0.5 * g * t**2  # Vertical displacement
            ball.move_to(np.array([new_x, new_y, 0]))  # Update ball's position

        # Attach the updater to the ball
        ball.add_updater(update_ball)

        # Add the ball to the scene
        self.add(ball)

        # Animate the ValueTracker to simulate time passing (projectile motion)
        self.play(time_tracker.animate.set_value(2), run_time=2, rate_func=linear)

        # Stop the updater once the animation is done
        ball.clear_updaters()
