#!/usr/bin/python3

from jinja2 import Environment, select_autoescape, FileSystemLoader
import glob
import os


if __name__ == "__main__":
    env = Environment(
        loader=FileSystemLoader(searchpath='templates'),
        autoescape=select_autoescape(['html'])
    )

    os.chdir('templates')
    templates = glob.glob('*.html')
    os.chdir('..')

    for t in templates:
        template = env.get_template(t)
        with open(t, 'w') as f:
            f.write(template.render())
        # print(t)
