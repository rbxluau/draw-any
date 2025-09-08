import turtle
import svgpathtools
from sys import argv
from tqdm import tqdm

config = {
    "t": 10,
    "size": 0.04,
    "x": -250,
    "y": -250
}

for segments in tqdm([path for paths in svgpathtools.svg2paths(argv[1])[0] for path in paths.continuous_subpaths()]):
    turtle.penup()
    for segment in tqdm(segments, leave=False):
        for i in range(1, config["t"]+1):
            point = segment.point(i/config["t"])
            turtle.goto(point.real*config["size"]+config["x"], point.imag*config["size"]+config["y"])
            turtle.pendown()

turtle.done()
