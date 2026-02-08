from build123d import *
from ocp_vscode import show
from pprint import pprint
def project_vertex(vertex, sketch):
    vertex = Vector(vertex)
    origin = sketch.workplanes[0].origin
    x_dir = sketch.workplanes[0].x_dir
    y_dir = sketch.workplanes[0].y_dir
    x_val = (vertex - origin).dot(x_dir)
    y_val = (vertex - origin).dot(y_dir)
    print(x_val, y_val)
    return (x_val, y_val)
Origin = Vector(0,0,0)
Corner_1 = Vector(1,0,0)
Corner_2 = Vector(0,1,0)
def makething3():
    with BuildPart() as part:
        with BuildSketch(Plane.XY) as sketch:
            a = project_vertex(Origin, sketch)
            b = project_vertex(Corner_1, sketch)
            c = project_vertex(Corner_2, sketch)
            with BuildLine() as line:
                Polyline(a, b, c, close=True)
            make_face()
        my_extrude = extrude(amount=0.05)
        for i in range(1,10):
            next_face = my_extrude.faces().sort_by(Axis.Z)[-1]
            with BuildSketch(next_face) as sketch:
                a = project_vertex(Origin, sketch)
                b = project_vertex(Origin + (Corner_1 - Origin) * (1 - i * 0.1), sketch)
                c = project_vertex(Corner_2, sketch)
                with BuildLine() as line:
                    Polyline(a, b, c, close=True)
                make_face()
            my_extrude = extrude(amount=0.05)
    show(part)
makething3()
