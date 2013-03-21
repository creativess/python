#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Image, ImageDraw, ImageFont
text = "Написал генератор эдвайсов"
text_ = "На python"
color = (0, 0, 120)
img = Image.open('tp.png')
imgDrawer = ImageDraw.Draw(img)
font=ImageFont.truetype('impact.ttf', 34)
W, H = (img.size[0], img.size[1])
w, h = imgDrawer.textsize(text)
imgDrawer.text(((W-w)/2 - 75,20), unicode(text, 'utf-8'), font=font)
imgDrawer.text(((W-w)/2 + 45, img.size[1]-70), unicode(text_, 'utf-8'), font=font)
img.save("ed", 'PNG')
