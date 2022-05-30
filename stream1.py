#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import os
import glob
from pdf2image import convert_from_path
import re
import cv2
import numpy as np
from PIL import Image
st.header('FILE AMPLIFIER')
st.write('1. Pdf to img ->Enter the full path of the folder of which you want to convert pdfs into image(all pdfs in folder will be converted) ') 
st.write('2. Img to pdf ->put the images that you want to merge to a pdf into a folder and put the path in the entry')
st.write('3. Deblur ->Enter the full path of the file which you want to deblur')
gh=st.text_input("Enter File path")
st.write(gh)
#uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
     
#      # To read file as bytes:
#      bytes_data = uploaded_file.getvalue()
#      #st.write(bytes_data)

#      # To convert to a string based IO:
#      #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#      #st.write(stringio)

#      # To read file as string:
#      #string_data = stringio.read()
#      #st.write(string_data)

#      # Can be used wherever a "file-like" object is accepted:
#      dataframe = pd.read_csv(uploaded_file)
#      #st.write(dataframe)
def itp(gh):
    from PIL import Image
    cw=os.getcwd()
    os.chdir(gh)
    i=0
    imagelist=[]
    for file in glob.glob("*.jpg"):
        if i==0:
            rt = file[:-4]
            image1 = Image.open(file)
            im1 = image1.convert('RGB')
            i=i+1
            continue
        image2 = Image.open(file)
        #image3 = Image.open('/Users/shreyashmarwade/Documents/wce_pro2/rel-2.jpg')
        
        
        im2 = image2.convert('RGB')
        #im3 = image3.convert('RGB')
        imagelist.append(im2)
        i=i+1
    #imagelist = []#[im2,im3]
    im1.save(rt+'.pdf',save_all=True, append_images=imagelist)
    cw=os.getcwd()
def pdi(gh):
    cw=os.getcwd()
    os.chdir(gh)
    i=0
    for file in glob.glob("*.pdf"):
        images = convert_from_path(file)
        rt = file[:-4]
        for b in range(len(images)):
   
          #Save pages as images in the pdf
            try :
                   images[b].save(rt+ str(b) +'.jpg', 'JPEG')
            except:
                   print("only 2")
            i=i+1
    os.chdir(cw)
def dblr(gh):
    image = cv2.imread(gh)
    rt=re.findall('/[^/]*jpg',gh)
    rt=rt[-1][1:-4]
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(image, -1, sharpen_kernel)
    cv2.imwrite(rt+'_dblur.jpg', sharpen)

def load_image(image_file):
    img = Image.open(image_file)
    return img

if st.button('pdf to image'):
    pdi(gh)
if st.button('image to pdf'):
    itp(gh)
if st.button('deblur'):
    dblr(gh)
    if gh is not None:

      # To See details
#         file_details = {"filename":uploaded_file.name, "filetype":uploaded_file.type,
#                            "filesize":uploaded_file.size}
        st.write(gh)

          # To View Uploaded Image
        st.image(load_image(gh),width=400)
