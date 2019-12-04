from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse
from typing import Optional
from typing import Sequence


def main(argv=None):  # type: (Optional[Sequence[str]]) -> int
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        with open(filename, 'rb') as f:
            if f.read(3) == b'\xef\xbb\xbf':
                retv = 1
                print('{}: Has a byte-order marker'.format(filename))

    return retv


if __name__ == '__main__':
    exit(main())
