from manim import *

class LimitAtInfinity(Scene):
    def construct(self):
        ####################################################################################################
        # Title
        title = Tex(r"Definition of Limit at Infinity").scale(1.5)
        title.set_color(BLUE)
        title.to_edge(UP)

        # Definition lines
        definition_1 = MathTex(
            r"\text{Let } D \subseteq \mathbb{R} \text{ be unbounded above and } f:D\to\mathbb{R}."
        )
        definition_2 = MathTex(
            r"f \text{ has a limit at } \infty \iff"
        )
        definition_3 = MathTex(
            r"\exists L \in \mathbb{R} \text{ such that } \forall \epsilon > 0,"
        )
        definition_4 = MathTex(
            r"\exists M > 0 \text{ such that } |f(x) - L| < \epsilon,"
        )
        definition_5 = MathTex(
            r"\forall x \in D \text{ such that } x \geq M."
        )

        # Grouping definitions
        definition_group = VGroup(definition_1, definition_2, definition_3, definition_4, definition_5)
        definition_group.arrange(DOWN, center=True)
        definition_group.next_to(title, DOWN)

        # Show the definition
        self.play(FadeIn(title))
        self.wait(2)
        self.play(Write(definition_1, run_time=7.8))
        self.wait(1)
        self.play(Write(definition_2, run_time=4.2))
        self.wait(1)
        self.play(Write(definition_3, run_time=6))
        self.wait(1)
        self.play(Write(definition_4, run_time=7.2))
        self.wait(1)
        self.play(Write(definition_5, run_time=5.4))
        self.wait(5)
        ####################################################################################################

        ####################################################################################################
        # Extract Key Parts for Highlighting
        L_part = definition_3[0][0:4].copy()  # \exists L \in \mathbb{R}
        epsilon_part = definition_3[0][12:16].copy()  # \forall \epsilon > 0
        M_part = definition_4[0][0:4].copy()  # \exists M > 0
        inequality_part = definition_4[0][12:22].copy()  # |f(x) - L| < \epsilon
        x_in_D_part = definition_5[0][0:4].copy()  # \forall x \in D
        x_greater_M_part = definition_5[0][12:15].copy()  # x \geq M

        # Create Bounding Boxes
        box_L = SurroundingRectangle(L_part, color=WHITE)
        box_epsilon = SurroundingRectangle(epsilon_part, color=WHITE)
        box_M = SurroundingRectangle(M_part, color=WHITE)
        box_inequality = SurroundingRectangle(inequality_part, color=WHITE)
        box_x_in_D = SurroundingRectangle(x_in_D_part, color=WHITE)
        box_x_greater_M = SurroundingRectangle(x_greater_M_part, color=WHITE)

        # Highlight key parts
        self.play(
            Create(box_L), 
            Create(box_epsilon), 
            Create(box_M),
            Create(box_inequality), 
            Create(box_x_in_D), 
            Create(box_x_greater_M)
        )

        self.wait(1)
        ####################################################################################################

        ####################################################################################################
        # Duplicate and keep extracted text in place before moving
        L_part_moved = L_part.copy().move_to(L_part.get_center())
        epsilon_part_moved = epsilon_part.copy().move_to(epsilon_part.get_center())
        M_part_moved = M_part.copy().move_to(M_part.get_center())
        inequality_part_moved = inequality_part.copy().move_to(inequality_part.get_center())
        x_in_D_part_moved = x_in_D_part.copy().move_to(x_in_D_part.get_center())
        x_greater_M_part_moved = x_greater_M_part.copy().move_to(x_greater_M_part.get_center())

        # Group copied elements
        boxed_moved_group = VGroup(
            L_part_moved, 
            epsilon_part_moved, 
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
                box_L,
                box_epsilon,
                box_M,
                box_inequality,
                box_x_in_D,
                box_x_greater_M
            )
        )

        self.wait(1)

        # Move extracted text into a single column
        extracted_parts = VGroup(
            L_part, 
            epsilon_part, 
            M_part, 
            inequality_part, 
            x_in_D_part, 
            x_greater_M_part
        )
        extracted_parts.arrange(DOWN, center=True, buff=0.5)
        extracted_parts.to_corner(RIGHT)

        box_to_do_list = SurroundingRectangle(extracted_parts, color = WHITE, buff=0.25)  

        self.play(
            L_part_moved.animate.move_to(extracted_parts[0]),
            epsilon_part_moved.animate.move_to(extracted_parts[1]),
            M_part_moved.animate.move_to(extracted_parts[2]),
            inequality_part_moved.animate.move_to(extracted_parts[3]),
            x_in_D_part_moved.animate.move_to(extracted_parts[4]),
            x_greater_M_part_moved.animate.move_to(extracted_parts[5]),
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
        # Graphical representation
        axes = Axes(
            x_range=[0, 10, 1], y_range=[0, 5, 1],
            x_length=7, y_length=4,
            axis_config={"color": WHITE}
        ).shift(LEFT)
        
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        self.play(FadeIn(axes), Write(labels))
        ####################################################################################################

        ####################################################################################################
        graph = axes.plot(lambda x: 3 + 1/x, x_range=[1, 10], color=BLUE)
        L_line = DashedLine(start=axes.c2p(0, 3), end=axes.c2p(10, 3), color=YELLOW)
        L_label = MathTex("L").next_to(axes.c2p(0, 3), LEFT, buff=0.2)
        
        self.play(Create(graph))
        self.play(Create(L_line), Write(L_label))
        ####################################################################################################

        ####################################################################################################
        # Epsilon band
        epsilon = 0.5
        upper_band = DashedLine(start=axes.c2p(0, 3 + epsilon), end=axes.c2p(10, 3 + epsilon), color=RED)
        upper_label = MathTex("L + \epsilon").next_to(axes.c2p(0, 3 + epsilon), LEFT, buff=0.2)
        
        lower_band = DashedLine(start=axes.c2p(0, 3 - epsilon), end=axes.c2p(10, 3 - epsilon), color=RED)
        lower_label = MathTex("L - \epsilon").next_to(axes.c2p(0, 3 - epsilon), LEFT, buff=0.2)
        
        self.play(Create(upper_band), Create(lower_band), Write(upper_label), Write(lower_label))
        
        # Showing M condition
        M_value = 4
        M_line = DashedLine(start=axes.c2p(M_value, 0), end=axes.c2p(M_value, 5), color=GREEN)
        M_label = MathTex("M").next_to(axes.c2p(M_value, 0), DOWN, buff=0.2)
        
        self.play(Create(M_line), Write(M_label))
        self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        ####################################################################################################








        ####################################################################################################
        '''
        # Example 1
        example_1_a = MathTex(r"\text{Let } f:\mathbb{Q}\setminus\{2\} \to \mathbb{R} \text{ by } f(x) = \frac{4x}{x-2}.")

        example_1_b = MathTex(r"\text{Prove } f \text{ has a limit at } \infty.")

        example_1 = VGroup(example_1_a, example_1_b)

        example_1.arrange(DOWN, center=True, buff=0.3)

        example_1.to_corner(UL)

        box_question = SurroundingRectangle(example_1, color = WHITE, buff=0.25)

        self.play(Write(example_1, run_time=3), Create(box_question))

        # Add "Proof." in italics below the question
        proof_text = Tex(r"\textit{Proof.}").next_to(example_1, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(proof_text))
        self.wait(1)

        # Create a copy and place it in the intended position
        example_1_a_copy = example_1_a.copy()
        example_1_a_copy.next_to(proof_text, DOWN, aligned_edge=LEFT)

        # Display where the copy would be (for debugging)
        self.add(example_1_a_copy)  # Check if this appears in the right place
        self.wait(1)

        # Now attempt the transformation
        self.play(Transform(example_1_a, example_1_a_copy))
        self.wait(1)

        self.play(Indicate(L_part_moved), run_time=1)

        # Create a VGroup of everything currently on screen at the end
        final_scene_group = VGroup(
            extracted_parts_with_box,  # The key extracted parts and their box
            example_1,  # The example problem
            box_question,  # The surrounding box for the example
            proof_text,  # The proof text
            example_1_a_copy
        )

        # Save the state of the entire scene
        final_scene_group.save_state()

        # Fade everything out
        self.play(FadeOut(final_scene_group))
        self.wait(2)

        limit_1 = MathTex(r"\lim\limits_{x \to \infty} f(x)")
        limit_2 = MathTex(r"=\lim\limits_{x \to \infty} \frac{4x}{x-2}")
        limit_3 = MathTex(r"=\lim\limits_{x \to \infty} \frac{4x}{x}")
        limit_4 = MathTex(r"=\lim\limits_{x \to \infty} 4")
        limit_5 = MathTex(r"=4.")
        limit_6 = MathTex(r"\therefore L = 4 \in \mathbb{R}.")

        limit_group = VGroup(limit_1, limit_2, limit_3, limit_4, limit_5, limit_6)
        limit_group.arrange(DOWN, center=True, buff=0.3)

        self.play(Write(limit_1, run_time=3))
        self.wait(1)
        self.play(Write(limit_2, run_time=3))
        self.wait(1)
        self.play(Write(limit_3, run_time=3))
        self.wait(1)
        self.play(Write(limit_4, run_time=3))
        self.wait(1)
        self.play(Write(limit_5, run_time=3))
        self.wait(1)

        # Bring everything back with FadeIn instead of Restore
        final_scene_group.restore()  # Ensure the position is reset
        self.play(FadeIn(final_scene_group))
        self.wait(2)
        '''