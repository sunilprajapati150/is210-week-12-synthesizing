#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Creating custom class """

class BaseError(Exception):
    """base class extending exception"""
    pass

class StringError(BaseError, TypeError):
    """subclass class of baseerror and typeerror"""
    pass

class NumberError(BaseError, TypeError):
    """subclass error for number of baseerror typeerror"""
    pass

class NonZeroError(NumberError):
    """subclass class of numbererror"""
    pass
