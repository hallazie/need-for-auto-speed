import math
from PIL import Image

print(math.log(10+1))
print(math.e**(math.log(11))-1)
box = [
    [
        655.8260869565217,
        599.0
    ],
    [
        789.3664596273292,
        502.1055900621118
    ]
]


def _norm_box(box):
    x0, x1 = min(box[0][0], box[1][0]), max(box[0][0], box[1][0])
    y0, y1 = min(box[0][1], box[1][1]), max(box[0][1], box[1][1])
    return [[x0, y0], [x1, y1]]

box = _norm_box(box)

img = Image.open('data/click-frame-speedmeter/frame-2660.jpg')
print(img.size)
img = img.crop((int(box[0][0])-1, int(box[0][1])-1, int(box[1][0])-1, int(box[1][1])-1))
img.show()