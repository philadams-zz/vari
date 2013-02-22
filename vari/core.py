#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Phil Adams http://philadams.net

Color representation conversions in Python.
"""


class Vari(object):
    """Color representation and representation conversion.
    In Finnish, väri means color."""

    def __init__(self, **kwargs):

        self._rgb = None  # internal repr
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    def __getattr__(self, label):
        if ('get_' + label) in self.__class__.__dict__:
            return getattr(self, 'get_' + label)()
        else:
            raise AttributeError("'%s' not an attribute" % label)

    def __setattr__(self, label, value):
        if label == '_rgb':
            self.__dict__[label] = value
        else:
            fnc = getattr(self, 'set_' + label)
            fnc(value)

    def __eq__(self, other):
        return self._rgb == other._rgb

    def get_rgb(self):
        return self._rgb

    def set_rgb(self, rgb):
        self._rgb = rgb


def main(args):
    pass


def cli():
    import argparse

    # populate and parse command line options
    desc = 'Color representation conversions in Python.'
    desc += '\nhttp://github.com/philadams/vari'
    parser = argparse.ArgumentParser(description=desc)
    args = parser.parse_args()

    print('commandline tool coming soon...')
