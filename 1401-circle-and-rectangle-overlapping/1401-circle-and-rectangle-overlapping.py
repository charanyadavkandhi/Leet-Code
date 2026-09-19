class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:

        # Closest x-coordinate in rectangle
        closest_x = max(x1, min(xCenter, x2))

        # Closest y-coordinate in rectangle
        closest_y = max(y1, min(yCenter, y2))

        # Squared distance from circle center to closest point
        dx = xCenter - closest_x
        dy = yCenter - closest_y

        return dx * dx + dy * dy <= radius * radius