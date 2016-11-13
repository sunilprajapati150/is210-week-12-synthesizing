#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Custom excepting in debugging error"""

class CustomError(Exception):
    def __init__(self, message, cause):
       
        Exception.__init__(self, message, cause)
        self.cause = cause
""" custom class for error debugging """
