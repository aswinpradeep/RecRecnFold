#!/usr/bin/env python

from __future__ import print_function

import sys
import os
import argparse
from os import listdir
from os.path import isfile, join

ALLOWED_IMAGE_EXTENSIONS = ['.jpeg', '.jpg', '.png']

def is_exists(path):
    if os.path.exists(path):
        return True
    else:
        print("Could not find the given file - ", path)
        return False


def get_all_images(dir):
    if is_exists(dir):
        files = [f for f in listdir(dir) if isfile(join(dir, f))]
        images = [f for f in files for ext in ALLOWED_IMAGE_EXTENSIONS if f.lower().endswith(ext.lower())]
        return images


def get_extension(file):
    file, ext = os.path.splitext(file)
    return ext


def rename_img(old, new, base_dir, i):
    if is_exists(old):
        new=new+str(i)
        ext = get_extension(old).lower()
        os.rename(old, join(base_dir,new + ext))
        print("Renaming ", old, "to ",  new + ext)
	print("***************************************************")




def get_caption(image_file):
    imfl=image_file
    os.system('rm -r xyz.txt')
    os.system('python ./label_image.py  --graph=./retrained_graph.pb --image=./'+imfl+' >>xyz.txt')
    caption_text = open('xyz.txt', 'r').read().strip()
    return caption_text


def full_path(base, file):
    return base + "/" + file


def init(dir):
    images = get_all_images(dir)
    i=0
    for image in images:
        file = full_path(dir, image)
        print("Processing image - ", image)
        new_name = get_caption(image)
        rename_img(image, new_name, dir, i)
	i=i+1


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help="Absolute path of image directory", type=str)
    args = parser.parse_args()

    try:
        init(args.dir)
    except ValueError:
        print("Try again")


if __name__ == '__main__':
    arg_parser()

