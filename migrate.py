#!/usr/bin/python

import glob
import os
import shutil
import string
import re

IMAGE_PATTERN = re.compile("")

BASE='../blog.old/content/'
TARGET='content'


def list_items(kind):
    for root, dirs, files in os.walk(os.path.join(BASE, kind)):
        for f in files:
            if f.endswith('.md'):
                yield f


def nameof(filename):
    return os.path.splitext(filename)[0]


def extensionof(filename):
    return os.path.splitext(filename)[1]


def new_article_name(name):
    return name.replace('.', '_')


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


def copy_illustration(article_name, target):
    base = os.path.join(BASE, 'images', article_name)
    def is_illustration(image):
        return len(image)-len(base) == 4

    for image in glob.glob(os.path.join(BASE, 'images', article_name+'*')):
        if is_illustration(image):
            shutil.copyfile(image, os.path.join(target, 'illustration' + extensionof(image)))
        else:
            shutil.copyfile(image, os.path.join(target, image[len(base)+1:]))


def translate_front_matter(line):
    if line.startswith('Title:'):
        return ['title: ' + line[7:]]
    elif line.startswith('Summary:'):
        return ['description: ' + line[9:]]
    elif line.startswith('Authors:'):
        return ['authors:'] + ["  - " + author.strip() for author in line[9:].split(',')]
    elif line.startswith('Tags:'):
        return ['tags:'] + ["  - " + tag.strip() for tag in line[6:].split(',')]
    elif line.startswith('Status:'):
        if 'draft' in line:
            return ['draft: true']
        return []
    elif line.startswith('Modified:'):
        return ['lastmod: ' + line[10:]]
    return [line]


def render_kwargs_as_front_matter(kwargs):
    lines = []
    for key, value in kwargs.iteritems():
        if value is list:
            lines.append(key+':')
            lines.extends(["  - " + v for v in value])
        else:
            lines.append(key + ': ' + value)
    return lines


def translate_image_link(kind, article_name, line):
    if '({filename}' in line:
        start = line.index('(')+1
        stop = line.index(')')
        image = line[start:stop][len('{filename}/images/'):]
        if image.startswith(article_name):
            image = image[len(article_name)+1:]
        new_image = os.path.join('/', kind, new_article_name(article_name), image)
        return line[:start] + new_image + line[stop:]
    return line


def translate_article(kind, article_name, content, **kwargs):
    lines = ['---']
    in_header = True
    for line in content.split('\n'):
        if in_header:
            if ':' in line:
                lines.extend(translate_front_matter(line))
            else:
                lines.extend(render_kwargs_as_front_matter(kwargs))
                lines.append('---')
                lines.append('')
                in_header = False
        else:
            lines.append(translate_image_link(kind, article_name, line))
    return string.join(lines, '\n')


def translate_category(kind):
    for article in list_items(kind):
        name = nameof(article)
        date = name[0:10]
        target = os.path.join(TARGET, kind, new_article_name(name))
        ensure_directory(target)
        write_article(
            os.path.join(target, 'index.md'),
            translate_article(
                kind,
                name,
                read_article(os.path.join(BASE, kind, article)),
                date=date,
                publishdate=date,
                aliases='/'+name+'.html')
        )
        copy_illustration(name, target)


translate_category('articles')
translate_category('news')
