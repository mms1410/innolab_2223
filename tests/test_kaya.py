#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 09:54:29 2022

@author: svenmaurice
"""

import pytest
from src.kaya import kaya_equation


class TestKayaEquation(object):
    """
    Unit Tests for kaya_equation
    """

    def test_kaya_equation(self):
        assert isinstance(kaya_equation(2, 3, 4, 5), int)
        assert kaya_equation(2, 3, 4, 5) == pytest.approx(120)
        assert isinstance(kaya_equation(2.2, 3.3, 4.4, 5.5), float)
        assert kaya_equation(2.2, 3.3, 4.4, 5.5) == pytest.approx(175.692)
