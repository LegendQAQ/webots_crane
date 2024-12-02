from controller import Supervisor, Keyboard

robot = Supervisor()

# 获取名为"crane"的节点
crane = robot.getFromDef("crane")

# 获取translation和rotation字段
trans = crane.getField("translation")

# 获取当前位置信息
current_translation = trans.getSFVec3f()

# 获取 crane 节点的子节点
children_field = crane.getField('children')

# 获取 Display 设备
display = robot.getDevice('display')

# 设置背景颜色
display.setColor(0xFFFFFF)  # 白色背景
display.fillRectangle(0, 0, display.getWidth(), display.getHeight())

# 清空 Display
display.setColor(0xFFFFFF)  # 白色背景
display.fillRectangle(0, 0, display.getWidth(), display.getHeight())

# 绘制固定矩形
display.setColor(0xFF0000)  # 红色
display.drawRectangle(100, 100, 300, 300)  # 绘制矩形

# 绘制移动矩形
display.setColor(0x00FF00)  # 绿色1
x = int(current_translation[0] + 116)
y = int(current_translation[1] + 244)
display.drawRectangle(y, x, 40, 300)  # 绘制矩形


# 获取时间步长
timestep = int(robot.getBasicTimeStep())

# 初始化键盘输入
keyboard = Keyboard()
keyboard.enable(timestep)

# 设置平移速度
speed = 0.2

# 主循环
while robot.step(timestep) != -1:
    key = keyboard.getKey()
    
    trans = crane.getField("translation")
    rotation = crane.getField("rotation")
    
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
        display.drawRectangle(current_position[1]-speed+ 244, current_position[0]+116, 40, 300)  # 绘制矩形
        print(trans.getSFVec3f())
        
        
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
        display.drawRectangle(current_position[1]+speed+ 244, current_position[0]+ 116, 40, 300)   # 绘制矩形
        print(trans.getSFVec3f())
        
        
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
        display.drawRectangle(current_position[1]+ 244, current_position[0]+speed+ 116, 40, 300)   # 绘制矩形
        print(trans.getSFVec3f())
        
        
    elif key == Keyboard.RIGHT:  # 向右移动
        x = int(current_translation[0] + 30)
        y = int(current_translation[1] + 100)
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
        display.drawRectangle(current_position[1]+ 244, current_position[0]-speed+ 116, 40, 300)  # 绘制矩形
        print(trans.getSFVec3f())
        
        
    elif key == 87:  # 向前移动
        new_position = [current_position[0], current_position[1], current_position[2] + speed]
        trans.setSFVec3f(new_position)
        print(trans.getSFVec3f())
    elif key == 83:  # 向后移动
        new_position = [current_position[0], current_position[1], current_position[2] - speed]  
        trans.setSFVec3f(new_position)
        print(trans.getSFVec3f())

     



