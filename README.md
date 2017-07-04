Introduction
------------
Unearths one or more artifacts about a Mac. Run it standalone to output to `stdout`; import it into your own scripts; use it with the `--jss` argument to work it into a Jamf Extension Attribute.

Usage
-----

    usage: unearth [-h] [--list] [--version] [--jss [[...]]] [--quiet [[...]]] ...

    Returns one or more facts about a Mac

    positional arguments:
    remnants

    optional arguments:
    -h, --help         show this help message and exit
    --list             list categories
    --version          show the version number
    --jss [ [ ...]]    return in jss format
    --quiet [ [ ...]]  return only the values

Examples
--------

    $ ./unearth primary_interface console_user battery_percentage
    battery_percentage => 65
    console_user => chilcote
    primary_interface => en0

    $ ./unearth --quiet primary_interface console_user battery_percentage
    65
    chilcote
    en0

    $ ./unearth --jss primary_interface console_user battery_percentage
    <result>65
    chilcote
    en0</result>

Excavate Module
----------------
If you wish, you may import the `Excavate()` module into your very own python scripts:

    >>> from excavate import Excavate
    >>> artifacts = Excavate()
    >>> gimme_artifacts = artifacts.get(['primary_interface', 'console_user', 'battery_percentage'])
    >>> print gimme_artifacts
    {'battery_percentage': '70', 'console_user': u'chilcote', 'primary_interface': u'en0'}

Adding Artifacts
------------

Add your own modules that `artifacts` subdirectory. They must have a `fact()` function that returns a dictionary of keys and values.

    factoid = 'favorite_book'

    def fact():
        '''Returns my favorite book'''
        return {factoid: ['John Kennedy Toole', 'A Confederacy of Dunces']}

About
-----
Some of these facts are taken from the [godawful pyfacts script](https://github.com/chilcote/pylab/blob/master/pyfacts) I've failed to maintain for the past few years.

I've wanted to break these up into modules for a long time. Inspiration came via the inimitable Greg Neagle's vastly more hip [munki-facts](https://github.com/munki/munki-facts) scripts. My apologies to Greg for once again bastardizing his code, and again I thank him for resisting the urge to put out a restraining order on me. As an offering of good faith, all of the facts herein are of a standard format and should work within `munki-facts`.

License
-------

	Copyright 2017-Present Joseph Chilcote

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

		http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.

Code shamelessly ripped off from [munki-facts](https://github.com/munki/munki-facts) is licensed [here](https://github.com/munki/munki/blob/master/LICENSE.md).
