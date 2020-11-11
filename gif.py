# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:47:36 2020

@author: GRUPO 3 - MCOC2020

Felipe Bravo
Jose Tomás Martinez
Eduardo Torres
"""
import glob
from PIL import Image
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

#caso_yz

#FRAME
fp_in = "fig/caso_yz_*.png"
fp_out = "ev_caso_yz.gif"

listaImagenes = sorted(glob.glob(fp_in))

print("sorted(glob.glob(fp_in)): ", listaImagenes)
listaImagenes.sort(key=natural_keys)
print("listaImagenes: ", listaImagenes)
img, *imgs = [Image.open(f) for f in listaImagenes]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=150, loop=0)

#caso_xy

#FRAME
fp_in = "fig/caso_xy_*.png"
fp_out = "ev_caso_xy.gif"

listaImagenes = sorted(glob.glob(fp_in))

print("sorted(glob.glob(fp_in)): ", listaImagenes)
listaImagenes.sort(key=natural_keys)
print("listaImagenes: ", listaImagenes)
img, *imgs = [Image.open(f) for f in listaImagenes]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=150, loop=0)

#caso_xz

#FRAME
fp_in = "fig/caso_xz_*.png"
fp_out = "ev_caso_xz.gif"

listaImagenes = sorted(glob.glob(fp_in))

print("sorted(glob.glob(fp_in)): ", listaImagenes)
listaImagenes.sort(key=natural_keys)
print("listaImagenes: ", listaImagenes)
img, *imgs = [Image.open(f) for f in listaImagenes]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=150, loop=0)
