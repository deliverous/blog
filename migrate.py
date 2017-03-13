#!/usr/bin/python

import os
import shutil
import string

BASE='../blog.old/content/'
TARGET='content'


def list_items(kind):
    for root, dirs, files in os.walk(os.path.join(BASE, kind)):
        for f in files:
            if f.endswith('.md'):
                yield f


def list_articles():
    return list_items('articles')


def nameof(filename):
    return os.path.splitext(filename)[0]


def ensure_directory(path):
    try:
        os.makedirs(path)
    except OSError:
        pass


def read_article(path):
    with open(path, 'r') as f:
        return f.read()


def write_article(path, content):
    with open(path, 'w') as f:
        f.write(str(content))


def translate_article(content):
    lines = ['---']
    in_header = True
    for line in content.split('\n'):
        if in_header:
            if ':' in line:
                lines.append(line)
            else:
                lines.append('---')
                lines.append('')
                in_header = False
        else:
            lines.append(line)
    return string.join(lines, '\n')

for article in list_articles():
    name = nameof(article)
    target = os.path.join(TARGET, 'articles', name)
    ensure_directory(target)
    write_article(
        os.path.join(target, 'index.md'),
        translate_article(read_article(os.path.join(BASE, 'articles', article)))
    )
