# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:10:19 2022

@author: utilisateur
"""

import os
from os import listdir
import cv2
from skimage.io import imread, imsave, imshow
import numpy as np
from numpy import load
import tensorflow
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from numpy import save, asarray

#%%
# Préparer data 
size = 150
# repertoir d'images avec deux sous dossiers "Cat" et "Dog"
image_directory = r"C:/Users/utilisateur/PetImages"
images = []  # liste pour images  
label = []  # liste pour Label (0 ou 1) pour deux classes.

# utiliser "os" pour avoir les noms des images dans chaque sous dossier
cat_images = os.listdir("PetImages/Cat")
dog_images = os.listdir("PetImages/Dog")
#%%
# utiliser une boucle pour lire chaque image, redimensionner en (150,150,3),
# et la mettre dans images, et mettre le label(0 ou 1) selon le type dans "label"

for file in listdir("PetImages/Dog/"):
   
    #load image
    
    try:
        image=np.float32(load_img("PetImages/Dog/"+file))
        resized=cv2.resize(image,(size,size), interpolation=cv2.INTER_AREA)
        
        #convert to numpy array
        image=img_to_array(image)
        images.append(image)
        label.append(0)
        
    except:
        print(f"erreur sur l'image {file}")
        
    #else:
        #images.append(image)
        #label.append(0)


for file in listdir("PetImages/Cat/"):
    
   
    #load image
    
    try:
        image=np.float32(load_img("PetImages/Cat/"+file))
        resized=cv2.resize(image,(size,size), interpolation=cv2.INTER_AREA)
        #convert to numpy array
        image=img_to_array(image)
        images.append(image)
        label.append(1)
    except:
        print(f"erreur sur l'image {file}")
        
    #else:
        #images.append(image)
        #label.append(1)


    
    #convert to a numpy array
images=asarray(images)
label=asarray(label)
            
# il y a des images corrumpues, utiliser try ... catch except pour les ignorer

#%%
# show shape
print(images.shape)
print(label.shape)
print(images)
#%%
# np;save data as ".npy" file
np.save("dog_cat_images",images)
#%%
np.save("dog_cat_label",label)
#%%
X=images
y=label
#%% 
print(y)






