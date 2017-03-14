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


def copy_illustration(article_name, destination):
    for ext in ['.jpg', '.png']:
        illustration = os.path.join(BASE, 'images', article_name+ext)
        if os.path.exists(illustration):
            shutil.copyfile(illustration, destination+ext)


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


def translate_article(content, **kwargs):
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
            lines.append(line)
    return string.join(lines, '\n')


def translate_category(kind):
    for article in list_items(kind):
        name = nameof(article)
        date = name[0:10]
        target = os.path.join(TARGET, kind, name.replace('.', '_'))
        ensure_directory(target)
        write_article(
            os.path.join(target, 'index.md'),
            translate_article(
                read_article(os.path.join(BASE, kind, article)),
                date=date,
                publishdate=date,
                aliases='/'+name+'.html')
        )
        copy_illustration(name, os.path.join(target, 'illustration'))


translate_category('articles')
translate_category('news')
