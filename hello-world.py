#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""    
just test
"""

import argparse

__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)

def setparser():
    """parser funtion.

    Args:
    Returns:
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-V', '--version', action='version', version='%(prog)s ('+__version__+')')
    args = parser.parse_args()
    args = args
if __name__ == "__main__":
    setparser()
    print 'hello-world'
