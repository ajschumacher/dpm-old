'''datapkg is a tool for distributing, discovering and installing knowledge and
data 'packages'.

datapkg has two main distinct uses:

    1. Find, obtaining and accessing material made available *by* others.
    2. Assisting you to make material available *to* others.

NB: in what follows items prefixed with $ should be run on the command line.

1. Obtaining Material
=====================

1.1 Set Up Your Local Repository
--------------------------------

First set up your local repository::

    $ datapkg init

This will create a .datapkg directory in your home directory along with various
files including a main configuration file (config.ini).

[Optional] Edit your configuration file::

    $ vi .datapkg/config.ini

1.2 Obtain and Install Material
-------------------------------

Install a package directly from a url::

    $ datapkg install ${url}

[NOT YET OPERATIONAL]

Update the index::

    $ datapkg update

[NOT YET OPERATIONAL]

Search for a package::

    $ datapkg search *

1.3 Access This Material
------------------------

[NOT YET OPERATIONAL]


2. Making Your Material Available to Others
===========================================

1. Create a skeletal package::

       $ datapkg create {my-new-package}

   See the help for the create command for more details.

2. Add material to this package::

       $ cd {my-new-package}
       $ cp {lots-of-my-data-files} .

[NOT YET OPERATIONAL]

3. Register your package with registry (such as CKAN)::

       $ datapkg register




3. For Developers
=================

The easiest thing (which also guarantees up-to-date-ness) is to look through
the unit tests in ./tests/
'''
__version__ = '0.1dev'
__description__ = 'Data packaging system and utilities.'
__description_long__ = __doc__
__license__ = 'MIT'
__license_full__ = \
'''All material is licensed under the MIT License:

Copyright (c) 2005-2008, Open Knowledge Foundation

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os

def create(name, base_path=''):
    '''Create a skeleton data package

    >>> import datapkg
    >>> os.chdir('/tmp')
    >>> pkg_name = 'my-random-name'
    >>> datapkg.create(pkg_name)
        ...
    '''
    import package
    pkg = package.Package(name)
    pkg.create_file_structure(base_path)

from paste.script.templates import Template
class DataPkgTemplate(Template):
    _template_dir = 'templates/default_distribution'
    summary = 'DataPkg default distribution template'

def install(name):
    from manager import PackageManager
    mgr = PackageManager()
    mgr.install(name)

def upload(path='.'):
    fns = os.listdir('.')
    if 'setup.py' not in fns:
        msg = '%s does not look like a data package (no setup.py ...)' % path
        raise Exception(msg)
    # TODO: implement the rest of this
    
