from math import pi
from manim import *
import numpy as np

''' PATH: "OneDrive\Desktop\School\2021-2022\Math\Math Lesson" '''

class Transformation(Scene):
    def construct(self) -> None:

        scale = 1 # x > 1 shrinks, 0 < x < 1 grows
        stretch = 1 # x > 1 compresses, 0 < x < 1 stretches
        degree = 2 # Degree of which to exponentiate by
        def function(x) -> float:
            ''' Function to Graph and Transform'''
            x *= stretch
            y = x
            return y/scale

        # Generate axis at correct scale
        axes = Axes(x_range=[-6*scale, 6*scale], y_range=[-3*scale, 3*scale])

        # Initial Function
        function_one = FunctionGraph(
            lambda x : function(x),
            color=YELLOW,
            x_range=(-6, 6)
        )

        # Transformed Function
        function_two = FunctionGraph(
            lambda x : function(x)**degree,
            color=RED,
            x_range=(-6, 6)
        )

        # Graph Equations
        label_one = MathTex("x", font_size=48).move_to(UR * 3)
        label_two = MathTex("x^2", font_size=48).move_to(UR * 3)

        # Draw first, animate transformation, hold
        self.play(DrawBorderThenFill(axes))
        self.play(DrawBorderThenFill(function_one), FadeIn(label_one))
        self.play(Transform(function_one, function_two), Transform(label_one, label_two))
        self.wait()
