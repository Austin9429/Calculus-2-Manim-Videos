from manim import *

# words * 3/5 = wpm

class FunctionTendsToInfinity(Scene):
    def construct(self):
        ####################################################################################################
        # Title
        title = Tex(r"Definition of Function Tending to Infinity").scale(1.5)
        title.set_color(BLUE)
        title.to_edge(UP)

        # Definition lines
        definition_1 = MathTex(
            r"\text{Let } D \subseteq \mathbb{R} \text{ be unbounded above and } f:D\to\mathbb{R}."
        )
        definition_2 = MathTex(
            r"f \text{ tends to } \infty \iff"
        )
        definition_3 = MathTex(
            r"\forall k > 0, \text{ } \exists M \in \mathbb{R}^+ \text{ such that } f(x) > k,"
        )
        definition_4 = MathTex(
            r"\forall x \in D \text{ such that } x \geq M."
        )

        # Grouping definitions
        definition_group = VGroup(definition_1, definition_2, definition_3, definition_4)
        definition_group.arrange(DOWN, center=True)
        definition_group.next_to(title, DOWN)
        
        # Show the definition
        self.play(FadeIn(title))
        self.wait(2.6)
        self.play(Write(definition_1, run_time=7.8))
        self.wait(1)
        self.play(Write(definition_2, run_time=3))
        self.wait(1)
        self.play(Write(definition_3, run_time=9))
        self.wait(1)
        self.play(Write(definition_4, run_time=5.4))
        self.wait(5)
        ####################################################################################################

        ####################################################################################################
        # Extract Key Parts for Highlighting
        k_part = definition_3[0][0:4].copy()  # \forall k > 0
        M_part = definition_3[0][5:10].copy()  # \exists M \in \mathbb{R}^+
        inequality_part = definition_3[0][18:24].copy()  # f(x) > k
        x_in_D_part = definition_4[0][0:4].copy()  # \forall x \in D
        x_greater_M_part = definition_4[0][12:15].copy()  # x \geq M

        # Create Bounding Boxes
        box_k = SurroundingRectangle(k_part, color=WHITE)
        box_M = SurroundingRectangle(M_part, color=WHITE)
        box_inequality = SurroundingRectangle(inequality_part, color=WHITE)
        box_x_in_D = SurroundingRectangle(x_in_D_part, color=WHITE)
        box_x_greater_M = SurroundingRectangle(x_greater_M_part, color=WHITE)

        # Highlight key parts
        self.play(
            Create(box_k), 
            Create(box_M), 
            Create(box_inequality), 
            Create(box_x_in_D), 
            Create(box_x_greater_M)
        )

        self.wait(1)
        ####################################################################################################

        ####################################################################################################
        # Duplicate and keep extracted text in place before moving
        k_part_moved = k_part.copy().move_to(k_part.get_center())
        M_part_moved = M_part.copy().move_to(M_part.get_center())
        inequality_part_moved = inequality_part.copy().move_to(inequality_part.get_center())
        x_in_D_part_moved = x_in_D_part.copy().move_to(x_in_D_part.get_center())
        x_greater_M_part_moved = x_greater_M_part.copy().move_to(x_greater_M_part.get_center())

        # Group copied elements
        boxed_moved_group = VGroup(
            k_part_moved, 
            M_part_moved, 
            inequality_part_moved, 
            x_in_D_part_moved, 
            x_greater_M_part_moved
        )

        self.add(boxed_moved_group)

        # Group title and definition together
        title_definition_group = VGroup(title, definition_group)

        self.wait(1)

        self.play(
            FadeOut(
                title_definition_group, 
                box_k, 
                box_M, 
                box_M, 
                box_inequality, 
                box_x_in_D, 
                box_x_greater_M
            )
        )

        self.wait(1)

        # Move extracted text into a single column
        extracted_parts = VGroup(
            k_part, 
            M_part, 
            inequality_part, 
            x_in_D_part, 
            x_greater_M_part
        )
        extracted_parts.arrange(DOWN, center=True, buff=0.5)
        extracted_parts.to_corner(RIGHT)

        box_to_do_list = SurroundingRectangle(extracted_parts, color = WHITE, buff=0.25)

        self.play(
            k_part_moved.animate.move_to(extracted_parts[0]),
            M_part_moved.animate.move_to(extracted_parts[1]),
            inequality_part_moved.animate.move_to(extracted_parts[2]),
            x_in_D_part_moved.animate.move_to(extracted_parts[3]),
            x_greater_M_part_moved.animate.move_to(extracted_parts[4]),
        )

        self.play(Create(box_to_do_list))

        self.wait(2)

        # Group the extracted text and the box together
        extracted_parts_with_box = VGroup(boxed_moved_group, box_to_do_list)

        # Shrink both the text and the box together
        self.play(extracted_parts_with_box.animate.scale(0.7), run_time=1)

        self.wait(2)
        ####################################################################################################

        ####################################################################################################
        # Axes
        axes = Axes(
            x_range=[0, 10, 1], y_range=[0, 10, 1],
            axis_config={"color": BLUE},
            x_length=5, y_length=5,
        )
        
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        self.play(FadeIn(axes), Write(labels))
        ####################################################################################################

        ####################################################################################################
        # Function definition
        func = axes.plot(lambda x: x, color=YELLOW)
        self.play(Create(func, run_time=5))
        ####################################################################################################

        ####################################################################################################
        # k and M illustration
        k_val = 5  # Selected k value
        M_val = 5  # Selected M value
        
        # k Line and Label (initially at 0)
        k_line = Line(axes.c2p(0, 0), axes.c2p(10, 0), color=PURPLE)
        k_label = MathTex("k", color=PURPLE).next_to(k_line, LEFT)
        
        # Animations
        k_smooth_move = k_line.animate.put_start_and_end_on(axes.c2p(0, k_val), axes.c2p(10, k_val)).set_rate_func(rate_functions.ease_out_sine)
        k_label_smooth_move = k_label.animate.move_to(axes.c2p(-0.5, k_val)).set_rate_func(rate_functions.ease_out_sine)

        # M Line and Label
        M_line = Line(axes.c2p(M_val, 0), axes.c2p(M_val, k_val), color=GREEN)
        M_label = MathTex("M", color=GREEN).next_to(M_line, DOWN)

        # Highlight function above M
        highlight_region = axes.plot(lambda x: x, x_range=[M_val, 10], color=RED, stroke_width=6)
        
        # Animation sequence
        self.wait(1)
        self.play(Indicate(k_part_moved))
        self.wait(0.5)
        self.play(Create(k_line), Create(k_label))
        self.wait(0.5)
        self.play(k_smooth_move, k_label_smooth_move)
        self.wait(1)
        
        self.play(Indicate(M_part_moved))
        self.wait(0.5)
        self.play(Create(M_line), Write(M_label))
        self.wait(1)

        self.play(Indicate(inequality_part_moved))
        self.wait(0.5)
        self.play(Create(highlight_region, run_time=5))
        self.wait(1)
