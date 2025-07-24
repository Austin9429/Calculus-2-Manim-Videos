from manim import *
import numpy as np

class Testing(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, PI, 1],
            y_range=[0, 4, 1],
            x_length=7,
            y_length=4,
            axis_config={"include_ticks": False, "include_numbers": False},
        ).shift(LEFT*2)
        labels = axes.get_axis_labels(x_label="", y_label="")

        f = lambda x: np.sin(x) + 2
        g = lambda x: np.cos(x) + 1

        f_graph = axes.plot(f, color=BLUE)
        g_graph = axes.plot(g, color=GREEN)

        f_label = MathTex("f(x)", color=BLUE).next_to(axes.c2p(PI * 0.75, f(PI * 0.75)), UP + RIGHT, buff=0.4)
        g_label = MathTex("g(x)", color=GREEN).next_to(axes.c2p(PI * 0.25, g(PI * 0.25)), DOWN + LEFT, buff=0.4)

        self.play(Create(axes), Write(labels))
        self.play(Create(f_graph), Write(f_label))
        self.play(Create(g_graph), Write(g_label))
        self.wait(1)

        a = 0.75
        b = 2.25

        a_line = DashedLine(
            start=axes.c2p(a, 0),
            end=axes.c2p(a, 4),
            color=WHITE,
            stroke_width=3
        )
        b_line = DashedLine(
            start=axes.c2p(b, 0),
            end=axes.c2p(b, 4),
            color=WHITE,
            stroke_width=3
        )

        a_label = MathTex("a").next_to(a_line, DOWN, buff=0.2)
        b_label = MathTex("b").next_to(b_line, DOWN, buff=0.2)

        self.play(Create(a_line), Write(a_label))
        self.play(Create(b_line), Write(b_label))
        self.wait(1)

        dx = 0.15
        x_vals = np.arange(a, b, dx)
        rectangles = VGroup()

        for x in x_vals:
            top = f(x)
            bottom = g(x)
            height = top - bottom

            rect_width = axes.c2p(dx, 0)[0] - axes.c2p(0, 0)[0]
            rect_height = axes.c2p(0, height)[1] - axes.c2p(0, 0)[1]

            rect = Rectangle(
                width=rect_width,
                height=rect_height,
                fill_opacity=0.75,
                fill_color=YELLOW,
                stroke_color=BLACK,
                stroke_width=1,
            )

            rect.move_to(axes.c2p(x + dx / 2, g(x) + height / 2))
            rectangles.add(rect)

        for rect in rectangles:
            self.play(GrowFromEdge(rect, edge=LEFT), run_time=0.05)

        self.wait(2)
        self.wait(1)

        center_index = len(rectangles) // 2
        center_rect = rectangles[center_index]
        rect_copy = center_rect.copy()

        target_pos = RIGHT * 3 + UP * 0.5
        self.play(rect_copy.animate.move_to(target_pos), run_time=1)
        self.wait(0.5)

        height_brace = Brace(
            rect_copy, direction=RIGHT, buff=0.1
        )
        h_label = height_brace.get_tex(r"f(x) - g(x)", buff=0.15).set_color(WHITE)

        dx_brace = Brace(
            rect_copy, direction=DOWN, buff=0.1
        )
        dx_label = dx_brace.get_tex(r"dx", buff=0.15).set_color(WHITE)

        self.play(Create(height_brace), Write(h_label))
        self.play(Create(dx_brace), Write(dx_label))
        self.wait(2)