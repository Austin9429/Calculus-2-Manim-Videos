from manim import *

class VolumeTheoremStatement(Scene):
    def construct(self):
        # Title (blue and large)
        title = Text("Volume Problem", font_size=36, color=BLUE).to_edge(UP)

        # Smaller font size for the body text
        font_scale = 0.65  # You can tweak this slightly if needed

        # Explanatory text (each line is scaled down)
        line1 = Tex(r"Let $S$ be a solid that extends along the $x$-axis,").scale(font_scale).next_to(title, DOWN, buff=0.5)
        line2 = Tex(r"bounded on the left and right by planes perpendicular").scale(font_scale).next_to(line1, DOWN, aligned_edge=LEFT)
        line3 = Tex(r"to the $x$-axis at $x = a$ and $x = b$, respectively.").scale(font_scale).next_to(line2, DOWN, aligned_edge=LEFT)
        line4 = Tex(r"If, for each $x \in [a, b]$, the cross-sectional area").scale(font_scale).next_to(line3, DOWN, aligned_edge=LEFT)
        line5 = Tex(r"of $S$ perpendicular to the $x$-axis is $A(x)$,").scale(font_scale).next_to(line4, DOWN, aligned_edge=LEFT)
        line6 = Tex(r"then the volume of the solid is").scale(font_scale).next_to(line5, DOWN, aligned_edge=LEFT)

        # Integral formula
        volume_formula = MathTex(r"V = \int_a^b A(x)\, dx").scale(0.9).set_color(YELLOW).next_to(line6, DOWN, buff=0.5)

        # Integrability condition
        condition = Tex(r"provided $A$ is integrable.").scale(font_scale).next_to(volume_formula, DOWN, buff=0.5)

        # Animate
        self.play(Write(title))
        self.wait(0.3)

        for line in [line1, line2, line3, line4, line5, line6]:
            self.play(Write(line), run_time=0.6)

        self.play(Write(volume_formula))
        self.wait(0.5)
        self.play(Write(condition))
        self.wait(2)
