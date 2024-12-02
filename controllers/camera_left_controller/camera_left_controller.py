from controller import Robot, Camera

# 初始化机器人
robot = Robot()

# 获取时间步长
timestep = int(robot.getBasicTimeStep())

# 获取摄像头设备
camera = robot.getDevice('cameraleft')

# 启用摄像头
camera.enable(timestep)

# 主循环
while robot.step(timestep) != -1:
    # 获取摄像头图像
    image = camera.getImage()

    # 检查图像是否为空
    pass
