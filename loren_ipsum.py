#!/usr/bin/env python

import argparse
import logging
import random
import re
import sys

logger = logging.getLogger('loren-ipsum')

words = [
        'ad',
        'adipisicing',
        'aliqua',
        'aliquip',
        'anim',
        'aute',
        'cillum',
        'commodo',
        'consectetur',
        'consequat',
        'culpa',
        'cupidatat',
        'deserunt',
        'do',
        'dolor',
        'dolore',
        'duis',
        'ea',
        'eiusmod',
        'elit',
        'enim',
        'esse',
        'est',
        'et',
        'eu',
        'ex',
        'excepteur',
        'exercitation',
        'fugiat',
        'id',
        'in',
        'incididunt',
        'ipsum',
        'irure',
        'labore',
        'laboris',
        'laborum'
        'lorem',
        'magna',
        'minim',
        'mollit',
        'nisi',
        'non',
        'nostrud',
        'nulla',
        'occaecat',
        'officia',
        'pariatur',
        'proident',
        'qui',
        'quis',
        'reprehenderit',
        'sed',
        'sint',
        'sunt',
        'tempor',
        'ullamco',
        'ut',
        'velit',
        'veniam',
        'voluptate',
        ]


class Transform(object):
    def __init__(self):
        self.rules = {}
        self.rules['F'] = ['A', 'B', 'FB', 'FA', 'FGF']
        self.rules['S'] = ['FT']
        self.rules['A'] = ['WW']
        self.rules['B'] = ['WWW']
        self.rules['G'] = [',']
        self.rules['T'] = ['.']
        self.rules['P'] = ['S', 'PS']

    def transform(self, s):
        """Transform a string according to the rules"""

        previous = str(s)
        while True:
            logger.debug(previous)

            # Iterate through each character in the string and transform it if there is
            # a rule associated with it. Otherwise, just copy the character.
            current = []
            for c in previous:
                if c in self.rules:
                    current.append(random.choice(self.rules[c]))
                else:
                    current.append(c)

            current = ''.join(current)

            # If the transformed string is identical to the original string, the
            # transformation is at a fixed point and successive transformations will
            # have no effect.
            if previous == current:
                return current

            previous = current


def format_sentence(tokens):
    w = []
    for c in tokens:
        if c == 'W':
            w.append(random.choice(words))
        else:
            w.append(c)

    w[0] = w[0].title()

    return re.sub(r' ,', r',', '{}.'.format(' '.join(w)))

def format_paragraph(paragraph):
    sentences = [s for s in paragraph.split('.') if s]
    return ' '.join(format_sentence(s) for s in sentences)


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('action',
            choices=('word', 'sentence', 'paragraph'),
            default='sentence')

    args = parser.parse_args(argv)

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    if args.action == 'word':
        print(random.choice(words))
        return

    if args.action == 'sentence':
        t = Transform()
        print(format_sentence(t.transform('F')))
        return

    if args.action == 'paragraph':
        t = Transform()
        print(format_paragraph(t.transform('P')))


if __name__ == "__main__":
    logging.basicConfig()
    main()
