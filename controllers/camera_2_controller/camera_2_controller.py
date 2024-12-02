from controller import Robot, Camera
import cv2
import numpy as np
import os
import torch
import matplotlib.pyplot as plt
from PIL import Image
import sys
from Python.sam2.sam2.sam2_image_predictor import SAM2ImagePredictor
from Python.sam2.sam2.build_sam import build_sam2
import time

if torch.cuda.is_available():
    device = torch.device("cuda")

sys.path.append(r'D:\Projects\webots2\webots\sam2/')

sam2_path = 'D:\Projects\webots2\webots\sam2'

sam2_checkpoint = sam2_path+"/checkpoints/sam2.1_hiera_large.pt"
model_cfg = sam2_path+"/sam2/configs/sam2.1/sam2.1_hiera_l.yaml"

sam2_model = build_sam2(model_cfg, sam2_checkpoint, device=device)

predictor = SAM2ImagePredictor(sam2_model)

np.random.seed(3)

box1 = np.array([1635, 951, 1800, 1300], dtype=np.float32)
box2 = np.array([1847, 1347, 2055, 1467], dtype=np.float32)
box3 = np.array([1489, 1487, 1931, 1646], dtype=np.float32)
box4 = np.array([1492, 1448, 1591, 1516], dtype=np.float32)
box5 = np.array([1654, 1432, 1695, 1461], dtype=np.float32)

# 设定从每个框中生成的点的数量
num_points_box1 = 5
num_points_box2 = 5
num_points_box3 = 5
num_points_box4 = 5
num_points_box5 = 5

# 生成第一个框内的随机点
points_box1 = np.random.uniform(low=[box1[0], box1[1]], high=[box1[2], box1[3]], size=(num_points_box1, 2)).astype(np.float32)

# 生成第二个框内的随机点
points_box2 = np.random.uniform(low=[box2[0], box2[1]], high=[box2[2], box2[3]], size=(num_points_box2, 2)).astype(np.float32)

# 生成第三个框内的随机点
points_box3 = np.random.uniform(low=[box3[0], box3[1]], high=[box3[2], box3[3]], size=(num_points_box3, 2)).astype(np.float32)

# 生成第四个框内的随机点
points_box4 = np.random.uniform(low=[box4[0], box4[1]], high=[box4[2], box4[3]], size=(num_points_box4, 2)).astype(np.float32)

# 生成第四个框内的随机点
points_box5 = np.random.uniform(low=[box5[0], box5[1]], high=[box5[2], box5[3]], size=(num_points_box5, 2)).astype(np.float32)

# 合并所有框生成的点
points = np.concatenate((points_box1, points_box2, points_box3, points_box4,points_box5), axis=0)

# 创建标签数组，前100个点label为1，后30个点label为0
labels = np.ones(num_points_box1 + num_points_box2 + num_points_box3 + num_points_box4+num_points_box5, dtype=np.int32)
labels[num_points_box1 + num_points_box2 + num_points_box3+num_points_box4:] = 0

def show_mask(mask, ax, random_color=False, borders = True):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([30/255, 144/255, 255/255, 0.6])
    h, w = mask.shape[-2:]
    mask = mask.astype(np.uint8)
    mask_image =  mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    if borders:
        import cv2
        contours, _ = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # Try to smooth contours
        contours = [cv2.approxPolyDP(contour, epsilon=0.01, closed=True) for contour in contours]
        mask_image = cv2.drawContours(mask_image, contours, -1, (1, 1, 1, 0.5), thickness=2)
    ax.imshow(mask_image)

def show_points(coords, labels, ax, marker_size=375):
    pos_points = coords[labels==1]
    neg_points = coords[labels==0]
    ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)
    ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)

def show_box(box, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0, 0, 0, 0), lw=2))

def show_masks(image, masks, scores,name, point_coords=None, box_coords=None, input_labels=None, borders=True):
    for i, (mask, score) in enumerate(zip(masks, scores)):
        plt.figure(figsize=(10, 10))
        plt.imshow(image)
        show_mask(mask, plt.gca(), borders=borders)
        if point_coords is not None:
            assert input_labels is not None
            show_points(point_coords, input_labels, plt.gca())
        if box_coords is not None:
            # boxes
            show_box(box_coords, plt.gca())
        if len(scores) > 1:
            plt.title(f"Mask {i+1}, Score: {score:.3f}", fontsize=18)
        plt.axis('off')
        plt.savefig(f'mask_frame_test_{name:04d}.jpg')
        plt.show()



# 初始化机器人
robot = Robot()

# 获取时间步长
timestep = int(robot.getBasicTimeStep())

# 获取摄像头设备
camera = robot.getDevice('cameraright')

# 启用摄像头
camera.enable(timestep)

# 设置视频编码器
#fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 获取图像的宽度和高度
width = camera.getWidth()
height = camera.getHeight()

# 创建 VideoWriter 对象
#out = cv2.VideoWriter(r'D:\Projects\webots2\webots\sam2\data\output.avi', fourcc, 20.0, (width, height))
print(f"Width: {width}, Height: {height}")

save_path = r'D:\Projects\webots2\webots\sam2\data'

# 主循环
frame_count = 0
while robot.step(timestep) != -1 :
    # 获取摄像头图像
    image = camera.getImage()

    if image:
        # 将图像数据转换为 numpy 数组
        image_array = np.frombuffer(image, np.uint8).reshape(height, width, 4)

        # 提取 BGRA 数据
        image_rgba = image_array[:, :width * 4].reshape(height, width, 4)

        # 取 BGR 通道
        image_bgr = image_rgba[:, :, :3]

        image_cv = cv2.cvtColor(image_bgr, cv2.COLOR_RGB2BGR)

        start_time = time.time()

        predictor.set_image(image_cv)

        masks, scores, _ = predictor.predict(
            point_coords=points,
            point_labels=labels,
            multimask_output=False,
        )

        # 记录预测结束时间
        end_time = time.time()

        # 计算预测所花费的时间
        prediction_time = end_time - start_time

        print("prediction done!")
        print(f"Prediction done! Time taken: {prediction_time:.4f} seconds")

        # show_masks(image_cv, masks, scores,name=frame_count)

        frame_count += 1


# 释放 VideoWriter 资源
#out.release()