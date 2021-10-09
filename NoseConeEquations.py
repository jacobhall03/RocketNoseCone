'''Nose Cone Equations'''

import math


def conical_shape(x: float, radius: float, length: float) -> float:
    '''Takes x position, radius, and length. Returns conical y value.'''

    return (x * radius) / length


def biconic_shape(x: float, top_radius: float, top_length: float, base_radius: float, full_length: float) -> float:
    '''Takes x position, top cone radius, top cone length, base radius, and length. Returns biconic y value.'''

    if x <= top_length:
        return (x * top_radius) / top_length
    else:
        tan_the = (base_radius - top_radius) / full_length
        return top_radius + (x - top_length) * tan_the
    

def tangent_ogive_shape(x: float, radius: float, length: float) -> float:
    '''Takes x position, radius, and length. Returns ogive y value.'''

    rho = (radius**2 + length**2) / (2 * radius)
    return math.sqrt(rho**2 - (x - length)**2) + (radius - rho)


def elliptical_shape(x: float, radius: float, length: float) -> float:
    '''Takes x position, radius, and length. Returns elliptical y value.'''

    return radius * math.sqrt(1 - ((length - x)**2 / length**2))

