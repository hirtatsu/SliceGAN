from tifffile import TiffFile
import numpy as np
import matplotlib.pyplot as plt

path = "/home/tatsumi/SliceGAN/Trained_Generators/SUS/64model/64model.tif" # パスを格納

with TiffFile(path) as tif:
    img = tif.asarray()
plt.imshow(img)