import numpy as np
import xml.etree.ElementTree as ET

# Your camera parameters
mtx = np.array([[655.87277362, 0., 361.16236141],
                [0., 643.3209444, 441.26729131],
                [0., 0., 1.]])
dist = np.array([[0.68173456, -3.6808909, -0.0235271, 0.09214856, 8.35183307]])
rvecs = np.array([[[0.04086178], [-0.51183392], [0.05862361]],
                  [[0.03963176], [-0.59140787], [0.06499816]],
                  [[0.06280132], [-0.30863994], [0.06659396]],
                  [[0.05946815], [-0.43015637], [0.04105233]]])
tvecs = np.array([[[-4.8042016], [-0.80767501], [19.77456459]],
                  [[-4.74739818], [-0.81187482], [19.82797931]],
                  [[-4.12571899], [-0.17679696], [20.73448666]],
                  [[-4.67048173], [-1.04304834], [19.66372027]]])

# Create the root element
root = ET.Element("opencv_storage")

# Add CameraMatrix element
camera_matrix = ET.SubElement(root, "CameraMatrix", type_id="opencv-matrix")
ET.SubElement(camera_matrix, "rows").text = "3"
ET.SubElement(camera_matrix, "cols").text = "3"
ET.SubElement(camera_matrix, "dt").text = "d"
ET.SubElement(camera_matrix, "data").text = ' '.join(map(str, mtx.flatten()))

# Add Intrinsics element (assuming this is the same as the camera matrix for this example)
intrinsics = ET.SubElement(root, "Intrinsics", type_id="opencv-matrix")
ET.SubElement(intrinsics, "rows").text = "3"
ET.SubElement(intrinsics, "cols").text = "3"
ET.SubElement(intrinsics, "dt").text = "d"
ET.SubElement(intrinsics, "data").text = ' '.join(map(str, mtx.flatten()))

# Add Distortion element
distortion = ET.SubElement(root, "Distortion", type_id="opencv-matrix")
ET.SubElement(distortion, "rows").text = "1"
ET.SubElement(distortion, "cols").text = str(dist.shape[1])
ET.SubElement(distortion, "dt").text = "d"
ET.SubElement(distortion, "data").text = ' '.join(map(str, dist.flatten()))

# Convert to a string and write to a file
tree = ET.ElementTree(root)
with open("camera_parameters.xml", "wb") as fh:
    tree.write(fh)
