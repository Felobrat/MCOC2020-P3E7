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

#caso_1

#FRAME
fp_in = "fig/caso_1_*.png"
fp_out = "ev_caso_1.gif"

listaImagenes = sorted(glob.glob(fp_in))

print("sorted(glob.glob(fp_in)): ", listaImagenes)
listaImagenes.sort(key=natural_keys)
print("listaImagenes: ", listaImagenes)
img, *imgs = [Image.open(f) for f in listaImagenes]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=150, loop=0)

#caso_2

#FRAME
fp_in = "fig/caso_2_*.png"
fp_out = "ev_caso_2.gif"

listaImagenes = sorted(glob.glob(fp_in))

print("sorted(glob.glob(fp_in)): ", listaImagenes)
listaImagenes.sort(key=natural_keys)
print("listaImagenes: ", listaImagenes)
img, *imgs = [Image.open(f) for f in listaImagenes]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=150, loop=0)

#caso_3

#FRAME
fp_in = "fig/caso_3_*.png"
fp_out = "ev_caso_3.gif"

listaImagenes = sorted(glob.glob(fp_in))

print("sorted(glob.glob(fp_in)): ", listaImagenes)
listaImagenes.sort(key=natural_keys)
print("listaImagenes: ", listaImagenes)
img, *imgs = [Image.open(f) for f in listaImagenes]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=150, loop=0)

#caso 4

#FRAME
fp_in = "fig/caso_4_*.png"
fp_out = "ev_caso_4.gif"

listaImagenes = sorted(glob.glob(fp_in))

print("sorted(glob.glob(fp_in)): ", listaImagenes)
listaImagenes.sort(key=natural_keys)
print("listaImagenes: ", listaImagenes)
img, *imgs = [Image.open(f) for f in listaImagenes]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=150, loop=0)

#caso_5

#FRAME
fp_in = "fig/caso_5_*.png"
fp_out = "ev_caso_5.gif"

listaImagenes = sorted(glob.glob(fp_in))

print("sorted(glob.glob(fp_in)): ", listaImagenes)
listaImagenes.sort(key=natural_keys)
print("listaImagenes: ", listaImagenes)
img, *imgs = [Image.open(f) for f in listaImagenes]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=150, loop=0)

#caso_6

#FRAME
fp_in = "fig/caso_6_*.png"
fp_out = "ev_caso_6.gif"

listaImagenes = sorted(glob.glob(fp_in))

print("sorted(glob.glob(fp_in)): ", listaImagenes)
listaImagenes.sort(key=natural_keys)
print("listaImagenes: ", listaImagenes)
img, *imgs = [Image.open(f) for f in listaImagenes]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=150, loop=0)

#caso_7_enunciado

#FRAME
fp_in = "fig/caso_7p_*.png"
fp_out = "ev_caso_7_enunciado.gif"

listaImagenes = sorted(glob.glob(fp_in))

print("sorted(glob.glob(fp_in)): ", listaImagenes)
listaImagenes.sort(key=natural_keys)
print("listaImagenes: ", listaImagenes)
img, *imgs = [Image.open(f) for f in listaImagenes]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=150, loop=0)


#caso_7

#FRAME
fp_in = "fig/caso_7_*.png"
fp_out = "ev_caso_7.gif"

listaImagenes = sorted(glob.glob(fp_in))

print("sorted(glob.glob(fp_in)): ", listaImagenes)
listaImagenes.sort(key=natural_keys)
print("listaImagenes: ", listaImagenes)
img, *imgs = [Image.open(f) for f in listaImagenes]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=150, loop=0)



