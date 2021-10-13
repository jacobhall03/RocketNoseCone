'''Library of Nose Cone Center of Pressure Functions

'cp' is short for center of pressure'''

import math


def base_area(base_radius: float) -> float:
    '''Takes base radius. Returns base area.'''
    return math.pi * base_radius**2


def solid_volume(length: float, y_position: list) -> float:
    '''Takes nosecone length, y-position values.
    Returns solid volume revolved about x-axis.

    Uses equation revolved about the x-axis volume aprox.
    Similar to the 'disk method', although we are actually calculating
    the sum of the volumes of cylinders.

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


def elliptical_cp(length: float) -> float:
    '''Takes elliptical nosecone length. Returns ~x-position.

    Reference point from forward end of nose cone.'''
    return length - (3 * length / 2)


def lvhaack_cp(length: float) -> float:
    '''Takes LV-Haack Series nosecone length. Returns ~x-position.

    Reference point from forward end of nose cone.'''
    return length - (0.437 * length)


def ldhaack_cp(length: float) -> float:
    '''Takes LD-Haack Series (Von Karmon) nosecone length. Returns ~x-position.

    Reference point from forward end of nose cone.'''
    return length - (0.500 * length)


def general_cp(length: float, volume: float, base_area: float) -> float:
    '''Takes nosecone volume and base area.
    Returns ~x-position of the center of pressure.

    Reference point from forward end of nose cone.

    All of the rules of thumb CP calculations (conical, ogive, parabolic,
    elliptical. etc.) are derived from this equation:

    x = volume / area. (reference point at aft end)
    '''
    return length - (volume / base_area)
