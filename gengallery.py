#!/usr/bin/python2.7
from glob import glob
from jinja2 import Environment, FileSystemLoader
from os import path

import Image
import sys

class img(object) :
    full = ''
    thumb = ''

    def __init__(self, full, thumb) :
        self.full = full
        self.thumb = thumb

    def __repr__(self) :
        return self.full+' '+self.thumb

files = glob('*.jpg')
images = []
for f in files :
    if not f.endswith('_thumb.jpg') :
        outfile = path.splitext(f)[0] + '_thumb.jpg'
        images.append(img(f, outfile))

        if path.isfile(outfile) :
            continue

        try :
            print "thumb for "+f
            im = Image.open(f)
            im.thumbnail((512,512))
            im.save(outfile, "JPEG")
        except IOError :
            print "error", f

print images
env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('template.html')


out = open('index.html', 'w')
out.write(template.render(images=images))
out.close()
