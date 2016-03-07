# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:02:34 2016

@author: hazem.soliman
"""

class wireless_area(object):
    """
    the class for the area
    """
    def __init__(self,x_min,x_max,y_min,y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.traffic = []
        self.service = []
        
class Access_point(object):
    """
    the class for the access point
    """
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.active = []
        
        
