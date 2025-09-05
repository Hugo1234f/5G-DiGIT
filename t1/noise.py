from manim import *
from VMObjects import *




class draw_AE(Scene):
    def construct(self):
        ae = AE()
        
        self.play(Create(ae), run_time=2)
        self.wait()

        