# Image-compression
Image compression with dimensionality reduction tecnics
Above there are two files, a .ipynb and a .py, the notebook version is a image compression using SVD (Singular Values Decomposition) with k=40, the .py file is a python program that take in input a filepath and return the plot like the .ipynb file, but with k=50.

### Singular Value Decomposition (SVD) in Image Compression

Singular Value Decomposition (SVD) is a powerful mathematical tool used in various fields, including image processing and compression. In the context of image compression, SVD helps reduce the storage requirements of an image by approximating it with a smaller set of data while retaining the most important features.

#### How it Works:
1. **Decomposition**: An image is represented as a matrix of pixel values, typically with dimensions \( m \times n \). SVD decomposes this matrix \( A \) into three smaller matrices:

   $$A = U \Sigma V^T$$

   where:
   - \( U \) is an $\( m \times m \$) orthogonal matrix (containing the left singular vectors),
   - \($\Sigma \$) is an $\( m \times n \$) diagonal matrix (containing singular values),
   - $\( V^T \$) is an $\( n \times n \$) orthogonal matrix (containing the right singular vectors).

2. **Compression**: In the context of compression, the idea is to keep only the largest singular values in $\( \Sigma \$) and corresponding columns in \( U \) and \( V \), as these capture the most significant features of the image. By truncating small singular values, the image can be represented with far fewer components, achieving compression.

3. **Reconstruction**: The compressed image is obtained by multiplying the truncated matrices:

   $$A' = U_k \Sigma_k V_k^T$$

   where \( k \) is the number of singular values kept. This results in a lower-rank approximation of the original matrix, which is an approximation of the original image.

#### Advantages:
- **Efficient Storage**: By reducing the number of singular values, the image can be stored in much less space.
- **Minimal Loss of Quality**: By retaining the most significant singular values, the reconstructed image is visually very similar to the original one, often with only a small loss in quality.
- **Noise Reduction**: SVD also helps reduce noise and artifacts by eliminating smaller singular values that may correspond to less important image features.

In summary, SVD is a powerful technique for image compression that reduces the dimensionality of an image while preserving its essential features, making it ideal for storage and transmission of large image datasets.


![Example Image](Figure_1.png)
