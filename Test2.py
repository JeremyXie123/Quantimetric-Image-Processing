import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import convolve2d as conv2

from skimage import color, data, restoration

from skimage import io
from skimage import color, data, restoration
camera = color.rgb2gray(data.camera())
from scipy.signal import convolve2d
psf = np.ones((5, 5)) / 25
noisy_camera = convolve2d(camera, psf, 'same')
noisy_camera += 0.1 * camera.std() * np.random.standard_normal(camera.shape)
deconvolved = restoration.richardson_lucy(camera, psf, 5)


fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 5))
plt.gray()

for a in (ax[0], ax[1], ax[2]):
       a.axis('off')

ax[0].imshow(camera)
ax[0].set_title('Original Data')

ax[1].imshow(noisy_camera)
ax[1].set_title('Noisy data')

ax[2].imshow(deconvolved, vmin=noisy_camera.min(), vmax=noisy_camera.max())
ax[2].set_title('Restoration using\nRichardson-Lucy')


fig.subplots_adjust(wspace=0.02, hspace=0.2,
                    top=0.9, bottom=0.05, left=0, right=1)
plt.show()