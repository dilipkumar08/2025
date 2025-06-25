class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_distance=0
        y_distance=0
        if x<z:
            x_distance=z-x
        else:
            x_distance=x-z

        if y<z:
            y_distance=z-y
        else:
            y_distance=y-z

        if x_distance==y_distance:
            return 0
        elif x_distance>y_distance:
            return 2
        else:
            return 1
        ©leetcode
