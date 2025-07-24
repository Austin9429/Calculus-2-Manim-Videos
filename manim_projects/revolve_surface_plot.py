from manim import *
import numpy as np

class RevolveSurface(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[0, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=5,
            y_length=5,
            z_length=5,
            axis_config={
                "color": GREY,
                "include_tip": True,
                "tip_shape": ArrowTriangleFilledTip,
                "tip_width": 0.15,
                "tip_height": 0.15,
            }
        )
        
        axes.z_axis.set_opacity(0)

        labels = axes.get_axis_labels(x_label="x", y_label="f(x)", z_label="")
        labels[1].rotate(-PI / 2)

        self.play(Create(axes), Write(labels))

        def func(x):
            return 0.25 * (x - 1) * (x - 3) * (x - 4) + 3
        
        curve_3d = ParametricFunction(
            lambda t: axes.c2p(t, func(t), 0),
            t_range=[0, 4],
            color=YELLOW,
            use_smoothing=True,
        )

        self.play(Create(curve_3d))
        self.play(Indicate(axes.x_axis, color=YELLOW))
        self.move_camera(phi=45 * DEGREES, theta=-45 * DEGREES, run_time=2)

        angle_tracker = ValueTracker(0)
        surface = always_redraw(lambda: Surface(
            lambda u, v: axes.c2p(
                u,
                func(u) * np.cos(v),
                func(u) * np.sin(v)
            ),
            u_range=[0, 4],
            v_range=[0, angle_tracker.get_value()],
            resolution=(30, 30),
            fill_opacity=0.4,
            checkerboard_colors=[BLUE_D, BLUE_E]
        ))

        self.add(surface)

        self.play(
            FadeOut(curve_3d),
            angle_tracker.animate.set_value(TAU),
            run_time=5,
            rate_func=linear,
        )

        self.wait()
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=2)

        x_val = 2
        radius = func(x_val)
        thickness = 0.10

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

        target_x = 7.5
        original_center = axes.c2p(x_val, 0, 0)
        target_center = axes.c2p(target_x, 0, 0)
        shift_vector = target_center - original_center

        self.play(disc.animate.shift(shift_vector), run_time=2)
        self.play(disc.animate.rotate(-PI / 2, axis=UP), run_time=2)
        self.wait()

        center = target_center
        edge = axes.c2p(target_x, radius, 0)
        radius_line = Line(start=center, end=edge, color=WHITE)
        center_dot = Dot(center, color=WHITE)

        formula = MathTex("A = \\pi r^2")
        formula.next_to(center, UP, buff=3)

        self.play(Write(formula))
        self.play(Create(radius_line), FadeIn(center_dot))
        self.wait()

        radius_label = MathTex("f(x)").next_to(radius_line, RIGHT, buff=0.2)
        
        self.play(Write(radius_label))
        self.wait()

        formula = MathTex("A = \\pi", "r", "^2")
        formula.next_to(center, UP, buff=3)

        fx_formula = MathTex("A = \\pi", "f(x)", "^2")
        fx_formula.move_to(formula)

        self.play(Write(formula))
        self.wait()
        self.play(TransformMatchingTex(formula, fx_formula))
        self.wait()
