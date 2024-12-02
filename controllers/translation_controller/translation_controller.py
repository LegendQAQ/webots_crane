from controller import Robot, Keyboard

# 创建一个Robot实例
robot = Robot()

# 设置时间步长
timestep = int(robot.getBasicTimeStep())

# 初始化键盘
keyboard = Keyboard()
keyboard.enable(timestep)

# 获取Robot的translation字段
translation_field = robot.getField("translation")

# 定义平移速度
speed = 0.1

# 主循环
while robot.step(timestep) != -1:
    key = keyboard.getKey()

    # 获取当前位置信息
    current_position = translation_field.getSFVec3f()

    # 键盘控制
    if key == Keyboard.UP:  # 向上移动
        new_position = (current_position[0], current_position[1] + speed, current_position[2])
        translation_field.setSFVec3f(new_position)
    elif key == Keyboard.DOWN:  # 向下移动
        new_position = (current_position[0], current_position[1] - speed, current_position[2])
        translation_field.setSFVec3f(new_position)
    elif key == Keyboard.LEFT:  # 向左移动
        new_position = (current_position[0] - speed, current_position[1], current_position[2])
        translation_field.setSFVec3f(new_position)
    elif key == Keyboard.RIGHT:  # 向右移动
        new_position = (current_position[0] + speed, current_position[1], current_position[2])
        translation_field.setSFVec3f(new_position)


