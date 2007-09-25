#!/usr/bin/env python
#
# Copyright 2007 Doug Hellmann.
#
#
#                         All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of Doug
# Hellmann not be used in advertising or publicity pertaining to
# distribution of the software without specific, written prior
# permission.
#
# DOUG HELLMANN DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN
# NO EVENT SHALL DOUG HELLMANN BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

"""

"""

__module_id__ = "$Id$"

#
# Import system modules
#
from distutils.core import setup
import glob
import os

#
# Import local modules
#


#
# Module
#

PROJECT = 'PyMOTW'

# Find the list of sub-packages
packages = [ PROJECT ]
for candidate in glob.glob('%s/*/__init__.py' % PROJECT):
    parts = os.path.split(candidate)
    packages.append(parts[0].replace('/', '.'))

# Where is the project hosted?
project_url = 'http://www.doughellmann.com/projects/PyMOTW/'
feed_url = 'http://feeds.feedburner.com/PyMOTW'

# Use a variable for the long description
readme = '''This package includes example code from my Python Module of the Week
blog series (%(project_url)s or
%(feed_url)s)

The plan is for me to work my way through all of the Python standard
library modules, writing a short post with example code for each one.
I am releasing all of the example code in this easy to download
collection.
''' % { 'project_url':project_url, 'feed_url':feed_url }

setup (
    name = PROJECT,
    version = 'trunk',

    description = 'Python Module of the Week Examples',
    long_description = readme,

    author = 'Doug Hellmann',
    author_email = 'doug.hellmann@gmail.com',

    url = project_url,
    download_url = 'http://www.doughellmann.com/downloads/%s-%s.tar.gz' % (PROJECT, 'trunk'),

    classifiers = [ 'Development Status :: 5 - Production/Stable',
                    'Environment :: Console',
                    'Intended Audience :: Developers',
                    'Intended Audience :: Education',
                    'License :: OSI Approved :: BSD License',
                    'Operating System :: POSIX',
                    'Programming Language :: Python',
                    'Topic :: Software Development',
                    ],

    platforms = ('Any',),
    keywords = ('python', 'PyMOTW'),

    packages = packages,

    package_dir = { 'PyMOTW':'PyMOTW' },
    )
