# Check if two circles overlap
def is_overlap(circle1, circle2):
    distance = ((circle1.x - circle2.x) ** 2 + (circle1.y - circle2.y) ** 2) ** 0.5
    return distance < circle1.r + circle2.r