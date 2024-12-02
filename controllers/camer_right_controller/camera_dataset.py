from controller import Robot, Camera
import cv2
import os
import numpy as np
# 初始化机器人
robot = Robot()

# 获取时间步长
timestep = int(robot.getBasicTimeStep())

# 获取摄像头设备
camera = robot.getDevice('cameraright')

# 启用摄像头
camera.enable(timestep)

# 设置视频编码器
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 获取图像的宽度和高度
width = camera.getWidth()
height = camera.getHeight()

# 创建 VideoWriter 对象
out = cv2.VideoWriter(r'D:\Projects\webots2\webots\sam2\data\output.avi', fourcc, 20.0, (width, height))
print(f"Width: {width}, Height: {height}")

save_path = r'D:\Projects\webots2\webots\sam2\data'

# 主循环
frame_count = 0
while robot.step(timestep) != -1 and frame_count<20:
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

        # 保存为 JPG 文件
        cv2.imwrite(os.path.join(save_path, f'frame_{frame_count:04d}.jpg'), image_bgr)

        # 写入视频文件
        out.write(image_bgr)


        frame_count += 1



# 释放 VideoWriter 资源
#out.release()
