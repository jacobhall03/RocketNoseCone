'''Library of Nose Cone Equations'''

import math


def conical_shape(x: float, radius: float, length: float) -> float:
    '''Takes x position, radius, and length. Returns conical y value.'''

    return (x * radius) / length


def biconic_shape(x: float,
                  top_radius: float, top_length: float,
                  base_radius: float, full_length: float) -> float:
    '''Takes x position, top cone radius, top cone length, base radius, and length.
    Returns biconic y value.'''

    if x <= top_length:
        return (x * top_radius) / top_length
    else:
        tan_the = (base_radius - top_radius) / full_length
        return top_radius + (x - top_length) * tan_the


def powerseries_shape(x: float, radius: float,
                      length: float, power: float) -> float:
    '''Takes x position, radius, length, and power.
    Returns power series y-value.'''
    return radius * ((x / length)**power)


def ogive_radius(radius: float, length: float) -> float:
    '''Takes nosecone radius and length. Returns ogive radius.'''
    return (radius**2 + length**2) / (2 * radius)


def tangent_ogive_shape(x: float, radius: float, length: float) -> float:
    '''Takes x position, radius, and length. Returns ogive y value.'''

    rho = ogive_radius(radius, length)
    return math.sqrt(rho**2 - (x - length)**2) + (radius - rho)


def secant_ogive_shape(x: float, radius: float,
                       length: float, rho: float) -> float:
    '''Takes x position, radius, length, and rho value. Returns ogive y value.

    rho value must be greater than twice the radius (rho > (2 * length))
    or calculation defaults to that of a tangent ogive shape.'''

    if (rho > (2 * length)):
        alpha = math.atan(radius / length) \
            - math.acos(math.sqrt(length**2 + radius**2) / (2 * rho))

        return math.sqrt(rho**2 - (x - rho * math.cos(alpha))**2) \
            + rho * math.sin(alpha)
    else:
        return tangent_ogive_shape(x, radius, length)


def elliptical_shape(x: float, radius: float, length: float) -> float:
    '''Takes x position, radius, and length. Returns elliptical y value.'''

    return radius * math.sqrt(1 - ((length - x)**2 / length**2))
