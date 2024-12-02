import cv2

# Read the image in BGR format
image_bgr = cv2.imread(r"D:\Projects\webots2\webots\sam2\data\frame_0612.jpg")

# No need to convert colors if the image is already in BGR format
# If the image is in RGB, use cv2.COLOR_RGB2BGR
# image_bgr = cv2.cvtColor(image_bgr, cv2.COLOR_RGB2BGR)

# Define the line parameters
start_point = (1,1616)
end_point = (3830,1531)
color = (0, 0, 255)  # Red color in BGR
thickness = 2

# Draw the line on the image
cv2.line(image_bgr, start_point, end_point, color, thickness)

# Save the image with the drawn line
cv2.imwrite(r"D:\Projects\webots2\webots\sam2\data\frame_0612_with_line.jpg", image_bgr)

# Display the image (optional)
cv2.imshow('Camera Image', image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()