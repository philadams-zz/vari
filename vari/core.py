#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Phil Adams http://philadams.net

Color representation conversions in Python.
"""

import re

from helpers import COLORS_NAMES

COLORS_RGB = dict((v, k) for k, v in COLORS_NAMES.iteritems())
HEX_COLOR = re.compile(r'^#[0-9a-fA-F]{6}')
HEX_COLOR_SHORT = re.compile(r'^#[0-9a-fA-F]{3}')


def rgb2hex(clr):
    """Convert rgb to hex values.
    - (r,g,b) where each value is 0..255
    - RRGGBB where each value is 00..FF"""
    return '#' + ''.join(map(chr, clr)).encode('hex')


def hex2rgb(clr):
    """Convert hex to rgb values.
    - (r,g,b) where each value is 0..255
    - RRGGBB where each value is 00..FF"""
    return tuple(map(ord, clr[1:].decode('hex')))


def rgb2x256(clr):
    """convert rgb to x256 8-bit color
    - (r,g,b) where each value is 0..255
    - 256 colors in 8 bits RRRGGGBB, returned as single int 0..255"""
    r, g, b = clr
    grey = False
    maybe_gray = True
    for i in range(3, 256, 42):
        if r <= i or g <= i or b <= i:
            grey = r <= i and g <= i and b <= i
            break
    if grey:
        color = 232 + int(sum(clr) / 33.0)
    else:
        components = ((r, 36), (g, 6), (b, 1))
        color = sum([16] + [int(6*val/256.0)*bmp for val, bmp in components])
    return color


class Vari(object):
    """Color representation and representation conversion.
    In Finnish, väri means color."""

    def __init__(self, color=None, **kwargs):

        self._rgb = None  # internal repr
        self.update(color, **kwargs)

        # if we've not set self._rgb, we couldn't init the color
        if not self._rgb:
            raise ValueError('cannot initialize Vari instance')

    def update(self, color, **kwargs):

        # handle kwargs[rgb]
        if 'rgb' in kwargs:
            self._rgb = tuple(map(int, kwargs['rgb']))

        elif color:

            # handle hex
            if color.startswith('#'):
                if HEX_COLOR.match(color):
                    self._rgb = hex2rgb(color)
                elif HEX_COLOR_SHORT.match(color):
                    clr = '#' + ''.join(['%s%s' % (e,e) for e in color[1:]])
                    self._rgb = hex2rgb(clr)

            # handle web
            elif color in COLORS_NAMES:
                self._rgb = COLORS_NAMES[color]


    def __eq__(self, other):
        return self._rgb == other._rgb

    def __repr__(self):
        return '<Vari %s>' % self.hex

    @property
    def rgb(self):
        return self._rgb

    @rgb.setter
    def rgb(self, rgb):
        self._rgb = rgb

    @property
    def hex(self):
        return rgb2hex(self._rgb)

    @property
    def web(self):
        return COLORS_RGB.get(self._rgb, self.hex)

    @property
    def x256(self):
        return rgb2x256(self._rgb)

def cli():
    import argparse

    # populate and parse command line options
    desc = 'Color representation conversions in Python.'
    desc += '\nhttp://github.com/philadams/vari'
    parser = argparse.ArgumentParser(description=desc)
    args = parser.parse_args()

    print('commandline tool coming soon...')
