#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 09:27:53 2022

@author: svenmaurice
"""


def kaya_equation(pop, gdp, enInt, carbInt):
    """
    Calculate yearly CO2 emission via Kaya Equation.

    Parameters
    ----------
    pop
        Population in mio.
    gdp
        Gross Domestic Product in $1000/person.
    enInt
        Energy Intensity in Gigajoule/$1000GDP.
    carbInt
        Carbon Intensity in tonnes CO2/Gigajoule.

    Returns
    -------
    numeric
        Yearly CO2 emission according to Kaya Equation
    """
    assert isinstance(pop, (int, float))
    assert isinstance(gdp, (int, float))
    assert isinstance(enInt, (int, float))
    assert isinstance(carbInt, (int, float))
    assert pop >= 0, "Population must be a non-negative number!"
    assert gdp >= 0, "GDP must be a non-nengative number!"
    assert enInt >= 0, "Energ Intensity must be a non-negative number!"
    assert carbInt >= 0, "Carbon Intensity must be a non-negative number!"

    return(pop * gdp * enInt * carbInt)
