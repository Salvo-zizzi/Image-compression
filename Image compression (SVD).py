import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import svd

# Load an image (grayscale)
image_path = input("Please enter the path to the image: ")
image = plt.imread(image_path)  # Replace with your image path
image = image[:, :, 0]  # Convert to grayscale if it's RGB

# Perform SVD
U, S, Vt = svd(image, full_matrices=False)

# Choose the number of singular values to keep
k = 50  # You can adjust this value
U_k = U[:, :k]
S_k = np.diag(S[:k])
Vt_k = Vt[:k, :]

# Reconstruct the image
compressed_image = np.dot(U_k, np.dot(S_k, Vt_k))

# Display original and compressed images
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Compressed Image (k={})'.format(k))
plt.imshow(compressed_image, cmap='gray')
plt.axis('off')

plt.show()