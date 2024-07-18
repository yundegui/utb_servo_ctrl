from cx_Freeze import setup, Executable

icon = "favicon.ico"  # 假设图标文件名为icon.ico，位于当前目录下
executables=[Executable("main.py", icon=icon)]

setup(
    name="多舵机控制",
    version="V1.0.0",
    description="舵机调试工具",
    executables=[Executable("main.py")],
)
