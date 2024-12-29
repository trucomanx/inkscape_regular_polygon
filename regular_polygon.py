#!/usr/bin/env python
# coding=utf-8
import inkex
import math
from lxml import etree

class RegularPolygonGenerator(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--tab")
        pars.add_argument("--num_sides", type=int, default=5, help="Number of sides of the polygon")
        pars.add_argument("--side_length", type=float, default=100.0, help="Length of each side of the polygon")

    def effect(self):
        num_sides = self.options.num_sides
        side_length = self.options.side_length

        if num_sides < 3:
            inkex.errormsg("The number of sides must be at least 3.")
            return

        # Calculate the angle between the vertices
        angle = 2 * math.pi / num_sides

        # Calculate the coordinates of the vertices
        points = []
        for i in range(num_sides):
            x = side_length+side_length * math.cos(i * angle)
            y = side_length+side_length * math.sin(i * angle)
            points.append(f"{x},{y}")

        # Create the polygon element
        polygon = etree.Element(
            inkex.addNS("polygon", "svg"),
            {
                "points": " ".join(points),
                "style": "fill:none;stroke:black;stroke-width:1",
            },
        )
        self.svg.get_current_layer().append(polygon)

if __name__ == "__main__":
    RegularPolygonGenerator().run()

