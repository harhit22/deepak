import numpy as np

# Load the .npz file
data = np.load('calibration_data.npz')

# List all files contained in the archive
print("Keys in the .npz file:", data.files)

# Access individual arrays
mtx = data['mtx']
dist = data['dist']
rvecs = data['rvecs']
tvecs = data['tvecs']

# Print the contents
print("Camera matrix (mtx):")
print(mtx)
print("Distortion coefficients (dist):")
print(dist)
print("Rotation vectors (rvecs):")
print(rvecs)
print("Translation vectors (tvecs):")
print(tvecs)

# Close the file after loading
data.close()
