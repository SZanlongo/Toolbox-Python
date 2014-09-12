# Check if two circles overlap
def is_overlap(circle1, circle2):
    distance = ((circle1.x - circle2.x) ** 2 + (circle1.y - circle2.y) ** 2) ** 0.5
    return distance < circle1.r + circle2.r

# Distance from point to line segment
# (x0, y0) is the point
# x (x1, y1), (x2, y2) are the endpoints of the line segment
def distancePointLine (x0, y0, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    dist = abs(dx * x0 - dx * y0 - x1 * y2 + x2 * y1) / math.sqrt(dx ** 2 + dy ** 2)

    return dist
