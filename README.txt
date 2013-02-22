väri
====

Color representations and representation conversions in Python. _Väri_ means
'color' in Finnish.

install
-------

`pip install vari`. Done.

use
---

Create a `Vari` object with one of many color representations:

    color = Vari(rgb=(255, 0, 0))

Ask the object for other representations:

    color.rgb  # (255, 0, 0)

acknowledgements
----------------

The search from rgb to x256 is a python port of [node-x256][node-x256] (MIT license, James Halliday).

future
------

- hex repr
- python port of substack/node-x256 for terminal colors
- human readable CSS web color list
- hsl repr

[node-x256]: https://github.com/substack/node-x256
