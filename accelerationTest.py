from manim import *

class AcceleratingBall(MovingCameraScene):
    def construct(self):
        # Create the ball
        ball = Dot(color=BLUE).move_to(LEFT * 5 + UP * 10)  # Start the ball on the top left
        self.play(self.camera.frame.animate.scale(5))
        # Initial velocities for both axes
        ball.velocity_x = 0.5  # Horizontal velocity (in units per second)
        ball.velocity_y = 0  # Vertical velocity (in units per second)

        # Accelerations for both axes
        acceleration_x = 0  # Horizontal acceleration (in units per second^2)
        acceleration_y = -6  # Vertical acceleration (gravity in units per second^2)

        # Define the updater function for horizontal and vertical movement
        def update_ball(ball):
            # Update the horizontal velocity and position
            ball.velocity_x += acceleration_x  # Increase horizontal velocity
            ball.shift(RIGHT * ball.velocity_x )  # Move based on horizontal velocity

            # Update the vertical velocity and position
            ball.velocity_y += acceleration_y   # Increase vertical velocity (gravity)
            ball.shift(UP * ball.velocity_y )  # Move based on vertical velocity

        # Attach the updater to the ball
        ball.add_updater(update_ball)

        # Add the ball to the scene
        self.add(ball)

        # Wait to observe the animation for 5 seconds
        self.wait(5)

        # Remove the updater after the animation
        ball.clear_updaters()