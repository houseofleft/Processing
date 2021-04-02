import shades
from random import randint

canvas = shades.Canvas(1000, 1000)
shade = shades.BlockColor(
    warp_size=140,
    warp_noise=[shades.NoiseField(scale=0.003) for i in range(2)]
)
gradient = shades.NoiseGradient(
    color=(100,200,200),
    noise_fields=[shades.NoiseField(scale=0.002) for i in range(3)]
)

def random_point():
    x = randint(-100, canvas.width+100)
    y = randint(-100, canvas.height+300)
    return (x, y)

def nearby_point(point):
    x = point[0] + randint(-50, 50)
    y = point[1] + randint(-50, 50)
    return (x, y)

points = [random_point() for i in range(5000)]

for point in points:
    color = gradient.determine_shade(nearby_point(point))
    shade.color = color
    shade.line(canvas, point, (point[0], point[1] + 200), 2)

canvas.show()
