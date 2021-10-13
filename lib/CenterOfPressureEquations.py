'''Library of Nose Cone Center of Pressure Functions

'cp' is short for center of pressure'''

import math
import NoseConeShapeEquations as shape
import numpy as np  # remove
import matplotlib.pyplot as plt  # remove


def base_area(base_radius: float) -> float:
    '''Takes base radius. Returns base area.'''
    return math.pi * base_radius**2


def solid_volume(length: float, y_position: list) -> float:
    '''Takes nosecone length, y-position values.
    Returns solid volume revolved about x-axis.

    300 data points were found to have an error-margin of 0.01%
    1000 data points were found to have an error-margin of 0.001%
    for a cone with equal length and radius.'''

    dx = length / (len(y_position) - 1)
    volume = 0.0
    for i in range(0, len(y_position) - 2):
        volume += math.pi * ((y_position[i] + y_position[i + 1]) / 2)**2 * dx
    return volume


# CP Equations
def conical_cp(length: float) -> float:
    '''Takes nosecone length. Returns ~x-position.

    Reference point from forward end of nose cone.'''
    return length - (length / 3)


def ogive_cp(length: float) -> float:
    '''Takes nosecone length. Returns ~x-position.

    Reference point from forward end of nose cone.

    Estimate for lengths greater than six times the radius
    ( L > 6R )'''
    return length - (0.534 * length)


def parabolic_cp(length: float) -> float:
    '''Takes parabolic nosecone length. Returns ~x-position.

    Reference point from forward end of nose cone.'''
    return length - (length / 2)


def general_cp(length: float, volume: float, base_area: float) -> float:
    '''Takes nosecone volume and base area.
    Returns ~x-position of the center of pressure.

    Reference point from forward end of nose cone.

    All of the rules of thumb CP calculations (conical, ogive, parabolic,
    elliptical. etc.) are derived from this equation:

    x = volume / area. (reference point at aft end)
    '''
    return length - (volume / base_area)


# delete this code block
if __name__ == '__main__':
    fig, ax = plt.subplots()
    ax.set_title("CP using general_cp() vs. ogive_cp() approx\n\
    for 10cm R x 40cm L Tangent Ogive\n(R is NOT greater than 6 * L)")
    ax.set_xlabel("# of Data Points")
    ax.set_ylabel("CP (cm from tip)")
    ax.grid()

    radius = 10
    length = 40
    BaseArea = base_area(radius)
    x_pos = np.linspace(0, length, num=1000+1)
    i = 10
    x = []
    generalcp = []
    for f in range(1, 101):
        dp = i*f
        x_pos = np.linspace(0, length, num=dp+1)
        y_pos = [shape.tangent_ogive_shape(x, radius, length) for x in x_pos]
        volume = solid_volume(length, y_pos)
        x.append(dp)
        generalcp.append(general_cp(length, volume, BaseArea))
    ogivecp = [ogive_cp(length) for x in x]
    ax.plot(x, generalcp, 'r--')
    ax.plot(x, ogivecp, 'k-.')
    ax.legend(("general_cp()", "ogive_cp()"))
    plt.show()
