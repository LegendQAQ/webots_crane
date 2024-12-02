from controller import Supervisor, Display,Keyboard

# 初始化 Supervisor
supervisor = Supervisor()
crane = supervisor.getFromDef("display")

# 获取时间步长
timestep = int(robot.getBasicTimeStep())

# 初始化键盘输入
keyboard = Keyboard()
keyboard.enable(timestep)

# 获取 Display 设备
display = supervisor.getDevice('display')

# 设置背景颜色
display.setColor(0xFFFFFF)  # 白色背景
display.fillRectangle(0, 0, display.getWidth(), display.getHeight())

# 清空 Display
display.setColor(0xFFFFFF)  # 白色背景
display.fillRectangle(0, 0, display.getWidth(), display.getHeight())

# 绘制固定矩形
display.setColor(0xFF0000)  # 红色
display.drawRectangle(100, 100, 300, 300)  # 绘制矩形

# 主循环
while supervisor.step(timestep) != -1:
    key = keyboard.getKey()
    
    trans = crane.getField("translation")
     # 获取当前位置信息
    current_position = trans.getSFVec3f()
    
    # 根据键盘输入进行平移
    if key == Keyboard.UP:  # 向上移动
        new_position = [current_position[0], current_position[1] + speed, current_position[2]]
        trans.setSFVec3f(new_position)
        
         # 清空 Display
        display.setColor(0xFFFFFF)  # 白色背景
        display.fillRectangle(0, 0, display.getWidth(), display.getHeight())

        # 绘制固定矩形
        display.setColor(0xFF0000)  # 红色
        display.drawRectangle(100, 100, 300, 300)  # 绘制矩形

        # 绘制移动矩形
        display.setColor(0x00FF00)  # 绿色
        display.drawRectangle(int(current_translation[0] * 100), int(current_translation[2] * 100), 50, 50)  # 绘制矩形
    elif key == Keyboard.DOWN:  # 向下移动
        new_position = [current_position[0], current_position[1] - speed, current_position[2]]
        trans.setSFVec3f(new_position)
         # 清空 Display
        display.setColor(0xFFFFFF)  # 白色背景
        display.fillRectangle(0, 0, display.getWidth(), display.getHeight())

        # 绘制固定矩形
        display.setColor(0xFF0000)  # 红色
        display.drawRectangle(100, 100, 300, 300)  # 绘制矩形

        # 绘制移动矩形
        display.setColor(0x00FF00)  # 绿色
        display.drawRectangle(int(current_translation[0] * 100), int(current_translation[2] * 100), 50, 50)  # 绘制矩形
    elif key == Keyboard.LEFT:  # 向左移动
        new_position = [current_position[0] - speed, current_position[1], current_position[2]]
        trans.setSFVec3f(new_position)
         # 清空 Display
        display.setColor(0xFFFFFF)  # 白色背景
        display.fillRectangle(0, 0, display.getWidth(), display.getHeight())

        # 绘制固定矩形
        display.setColor(0xFF0000)  # 红色
        display.drawRectangle(100, 100, 300, 300)  # 绘制矩形

        # 绘制移动矩形
        display.setColor(0x00FF00)  # 绿色
        display.drawRectangle(int(current_translation[0] * 100), int(current_translation[2] * 100), 50, 50)  # 绘制矩形
    elif key == Keyboard.RIGHT:  # 向右移动
        new_position = [current_position[0] + speed, current_position[1], current_position[2]]
        trans.setSFVec3f(new_position)
         # 清空 Display
        display.setColor(0xFFFFFF)  # 白色背景
        display.fillRectangle(0, 0, display.getWidth(), display.getHeight())

        # 绘制固定矩形
        display.setColor(0xFF0000)  # 红色
        display.drawRectangle(100, 100, 300, 300)  # 绘制矩形

        # 绘制移动矩形
        display.setColor(0x00FF00)  # 绿色
        display.drawRectangle(int(current_translation[0] * 100), int(current_translation[2] * 100), 50, 50)  # 绘制矩形

    


