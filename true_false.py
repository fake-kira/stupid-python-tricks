#!/usr/bin/env python3

""" A python port of the old #define TRUE FALSE trick. """

import __builtin__

__builtin__.True = False
