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

# A set of rules for transforming symbols to create sentences
rules = {}
rules['F'] = ['A', 'B', 'FB', 'FA', 'FGF']
rules['S'] = ['FT']
rules['A'] = ['WW']
rules['B'] = ['WWW']
rules['G'] = [',']
rules['T'] = ['.']
rules['P'] = ['S', 'PS']

def transform(s):
    """Transform a string according to the rules"""
    logger.debug(s)

    # Iterate through each character in the string and transform it if there is
    # a rule associated with it. Otherwise, just copy the character.
    t = []
    for c in s:
        if c in rules:
            t.append(random.choice(rules[c]))
        else:
            t.append(c)

    t = ''.join(t)

    # If the transformed string is identical to the original string, the
    # transformation is at a fixed point and successive transformations will
    # have no effect.
    if s == t:
        return t

    # Transform again
    return transform(t)


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
        print(format_sentence(transform('F')))
        return

    if args.action == 'paragraph':
        print(format_paragraph(transform('P')))


if __name__ == "__main__":
    logging.basicConfig()
    main()
