from manim import *


class AE(VMobject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.lines = []

        self.lines.append(Line([3,-1,0],[-3,-1,0])) # Ground
        self.draw_tower()
        self.draw_terminal()

        for line in self.lines:
            self.add(line)

    def draw_tower(self):

        self.lines.append(Line([2.6, -1, 0],[2.6, 1.5, 0])) # Righ wall
        self.lines.append(Line([2, -1, 0],[2, 1.5, 0])) # Left wall
        self.lines.append(Line([2.6, 1.5, 0],[2, 1.5, 0])) # Upper base support
        self.lines.append(Line([2, -0.5, 0],[2.6, -0.5, 0])) # Lower base support
        self.lines.append(Line([2, 1.5, 0],[1.9, 2, 0])) #Left platform support
        self.lines.append(Line([2.6, 1.5, 0],[2.7, 2, 0])) #Right platform support
        self.lines.append(Line([1.9, 2, 0],[2.7, 2, 0])) #Top platform support
        self.lines.append(Line([1.7, 2, 0],[2.9, 2, 0])) # Room floor
        self.lines.append(Line([1.7, 2, 0], [1.7, 2.6, 0])) # Left room wall
        self.lines.append(Line([2.9, 2, 0], [2.9, 2.6, 0])) # Right room wall
        self.lines.append(Line([1.7, 2.6, 0], [2.9, 2.6, 0])) # Room roof
        self.lines.append(Line([1.7, 2.4, 0], [2.9, 2.4, 0])) # Room Panel
        self.lines.append(Line([2.05, 2, 0], [2.05, 2.4, 0])) # Left Room Window
        self.lines.append(Line([2.55, 2, 0], [2.55, 2.4, 0])) # Right Room Window
        self.lines.append(Line([1.9, 2.6, 0],[1.7, 2.8, 0])) # Lower Left Radar support
        self.lines.append(Line([2.7, 2.6, 0],[2.9, 2.8, 0])) # Lower Right Radar support
        self.lines.append(Line([2.9, 2.8, 0],[1.7, 2.8, 0])) # Radar support floor
        self.lines.append(Line([1.7, 3.1, 0],[1.7, 2.8, 0])) # Left Radar support wall
        self.lines.append(Line([2.9, 3.1, 0],[2.9, 2.8, 0])) # Right Radar support wall
        self.lines.append(Line([1.7, 3.1, 0], [2.9, 3.1, 0])) # Radar support roof
        self.lines.append(Line([2.3, 3.1, 0], [2.3, 3.6, 0])) # Radar

    def draw_terminal(self):
        self.lines.append(Line([1.6, -1, 0], [1.6, 0.1, 0])) # Right Terminal wall
        self.lines.append(Line([-2.4, -1, 0], [-2.4, 0.1, 0])) # Left Terminal wall
        self.lines.append(Line([-2.4, 0.1, 0], [1.6, 0.1, 0])) # Terminal Roof
        self.lines.append(Line([-2.4, -0.2, 0], [1.3, -0.2, 0])) # Terminal Panel
        self.lines.append(Line([1.3, -0.2, 0], [1.3, -1, 0])) # Terminal Side Panel
        self.lines.append(Line([-2.1, -0.2, 0], [-2.1, -1, 0])) # Terminal window 1
        self.lines.append(Line([-1.6, -0.2, 0], [-1.6, -1, 0])) # Terminal window 2
        self.lines.append(Line([-1.1, -0.2, 0], [-1.1, -1, 0])) # Terminal window 3
        self.lines.append(Line([-0.5, -0.2, 0], [-0.5, -1, 0])) # Terminal window 4
        self.lines.append(Line([0.1, -0.2, 0], [0.1, -1, 0])) # Terminal window 5
        self.lines.append(Line([0.7, -0.2, 0], [0.7, -1, 0])) # Terminal window 6
        
        self.lines.append(Line([1.5, 0.1, 0], [1.5, 0.8, 0])) # Loft Right wall
        