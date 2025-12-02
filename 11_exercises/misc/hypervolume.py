#!/usr/bin/env python3
# A simple function that calculates the area / volume of triangles, cuboids, hypercuboids


def hypervolume(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v


# calculate the area of a rectangle
hypervolume(2, 4)

# calculate the volume of a cuboid
hypervolume(2, 4, 6)

# calculate the volume of a hypercuboid
hypervolume(2, 4, 6, 8)
