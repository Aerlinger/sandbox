#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Can't import from non-package folder
try:
    import a_normal_folder
except ImportError as ex:
    print ex


from package_folder.a_module import NormalFolder1

nf = NormalFolder1("something")

nf.getMyName()