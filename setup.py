from cx_Freeze import setup, Executable

# 假设图标文件名为favicon.ico，位于当前目录下
icon = "icon.ico"

# 正确配置executables，包含图标路径
executables = [Executable("main.py", icon=icon)]

setup(
    name="多舵机控制",
    version="V1.0.0",
    description="舵机调试工具",
    executables=executables,  # 使用包含图标的executables定义
)
