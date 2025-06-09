from manim import *
import numpy as np

class RevolveSurface(ThreeDScene):
    def construct(self):
        # Set up 3D Axes
        axes = ThreeDAxes(
            x_range=[0, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=5,
            y_length=5,
            z_length=5,
            axis_config={"color": GREY}
        )

        # Remove the z axis
        axes.z_axis.set_opacity(0)

        # Set the axis labels
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)", z_label="")
        
        # Rotate the f(x) axis label
        labels[1].rotate(-PI / 2)

        # Create axes and labels
        self.play(Create(axes), Write(labels))

        # Define the function
        def func(x):
            return 0.25 * (x - 1) * (x - 3) * (x - 4) + 3
        
        # Show the original curve (not rotating)
        curve_3d = ParametricFunction(
            lambda t: axes.c2p(t, func(t), 0),
            t_range=[0, 4],
            color=YELLOW,
            use_smoothing=True,
        )
        self.play(Create(curve_3d))

        self.play(Indicate(axes.x_axis, color=YELLOW))

        # Switch to 3D camera view
        self.move_camera(phi=45 * DEGREES, theta=-45 * DEGREES, run_time=2)

        # Define a ValueTracker to control the sweep angle
        angle_tracker = ValueTracker(0)

        # Define the surface to be updated
        surface = always_redraw(lambda: Surface(
            lambda u, v: axes.c2p(
                u,
                func(u) * np.cos(v),
                func(u) * np.sin(v)
            ),
            u_range=[0, 4],
            v_range=[0, angle_tracker.get_value()],
            resolution=(30, 30),
            fill_opacity=0.6,
            checkerboard_colors=[BLUE_D, BLUE_E]
        ))

        self.add(surface)

        # Animate the surface sweeping around the x-axis
        self.play(
            angle_tracker.animate.set_value(TAU),
            run_time=5,
            rate_func=linear
        )

        self.wait()

        # Define the disc (ring shape) at x = 2
        x_val = 2
        radius = func(x_val)
        thickness = 0.10

        # Parametrize a thick ring-like disc using Surface
        disc = Surface(
            lambda u, v: axes.c2p(
                x_val,
                (radius - thickness) * np.cos(u) + v * np.cos(u),
                (radius - thickness) * np.sin(u) + v * np.sin(u)
            ),
            u_range=[0, TAU],
            v_range=[0, thickness],
            resolution=(50, 4),
            fill_opacity=0.85,
            checkerboard_colors=[RED_D, RED_E]
        )

        self.play(FadeIn(disc), run_time=1)
        self.wait(1)

        # Animate: Move disc to the side
        self.play(disc.animate.shift(axes.c2p(8, 0, 0)), run_time=2)

        # Animate camera back to original view
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=2)

        # Rotate disc to face camera (xy-plane facing forward)
        self.play(disc.animate.rotate(-PI / 2, axis=UP), run_time=2)

        self.wait()


