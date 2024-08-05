import cv2
import numpy as np
import glob

# Define the chessboard dimensions (inner corners)
chessboard_size = (7, 7)

# Prepare object points, like (0,0,0), (1,0,0), ..., (6,6,0)
objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane

# Load images
images = glob.glob('calibration_images/*.jpg')
print(f"Images found: {images}")

# Termination criteria for corner sub-pixel accuracy
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)
    print(f"Chessboard found in {fname}: {ret}")
    print(corners)

    # If found, add object points, image points (after refining them)
    if ret:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, chessboard_size, corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(500)
    else:
        print(f"Chessboard corners not found in image: {fname}")
        cv2.imshow('img', img)
        cv2.waitKey(500)

cv2.destroyAllWindows()

# Check if there are valid points before calibration
if len(objpoints) > 0 and len(imgpoints) > 0:
    # Calibration
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    # Save the calibration results
    np.savez('calibration_data.npz', mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)
    print("Calibration successful. Results saved to 'calibration_data.npz'.")
else:
    print("Not enough valid calibration images to perform calibration.")
