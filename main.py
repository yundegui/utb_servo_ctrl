import tkinter as tk
from tkinter import ttk
import serial
import serial.tools.list_ports
import UTB


class ServoControllerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("舵机控制界面(uf4)")
        self.geometry("1200x700")

        # 串口和波特率选择
        self.available_ports = [port.device for port in serial.tools.list_ports.comports()]
        self.selected_port = tk.StringVar(value=self.available_ports[0] if self.available_ports else "")
        self.baud_rate = tk.IntVar(value=115200)

        # 串口选择下拉菜单
        port_label = ttk.Label(self, text="选择串口:")
        port_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        port_menu = ttk.Combobox(self, textvariable=self.selected_port, values=self.available_ports)
        port_menu.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # 波特率选择下拉菜单
        baud_rate_label = ttk.Label(self, text="波特率:")
        baud_rate_label.grid(row=0, column=2, sticky="w", padx=5, pady=5)
        baud_rates = [114, 19200, 114514, "还想要其他的？？？", 115200]
        baud_rate_menu = ttk.Combobox(self, textvariable=self.baud_rate, values=baud_rates)
        baud_rate_menu.grid(row=0, column=3, sticky="ew", padx=5, pady=5)


        # 创建多个舵机控制区域
        for i in range(12):  # 控制12个舵机
            self.create_servo_control_area(i)

    def create_servo_control_area(self, index):
        # 舵机名称
        servo_name = tk.StringVar(value=f"我是大煞笔")
        servo_name_label = ttk.Label(self, text=f"舵机名称:")
        servo_name_label.grid(row=index + 1, column=0, sticky="w", padx=5, pady=5)
        servo_name_entry = ttk.Entry(self, textvariable=servo_name)
        servo_name_entry.grid(row=index + 1, column=1, sticky="ew", padx=5, pady=5)

        # 输入舵机ID
        servo_id = tk.IntVar(value=index)
        servo_id_label = ttk.Label(self, text=f"舵机ID:")
        servo_id_label.grid(row=index + 1, column=2, sticky="w", padx=5, pady=5)
        servo_id_entry = ttk.Entry(self, textvariable=servo_id)
        servo_id_entry.grid(row=index + 1, column=3, sticky="ew", padx=5, pady=5)

        # 输入角度
        angle = tk.IntVar(value=120)
        angle_label = ttk.Label(self, text="角度:")
        angle_label.grid(row=index + 1, column=4, sticky="w", padx=5, pady=5)
        angle_entry = ttk.Entry(self, textvariable=angle)
        angle_entry.grid(row=index + 1, column=5, sticky="ew", padx=5, pady=5)

        # 输入时间
        time = tk.IntVar(value=20)
        time_label = ttk.Label(self, text="时间(单位20ms):")
        time_label.grid(row=index + 1, column=6, sticky="w", padx=5, pady=5)
        time_entry = ttk.Entry(self, textvariable=time)
        time_entry.grid(row=index + 1, column=7, sticky="ew", padx=5, pady=5)

        # 控制按钮
        control_button = ttk.Button(
            self, text=f"控制舵机 {index + 1}", command=lambda idx=index: self.control_servo(idx)
        )
        control_button.grid(row=index + 1, column=8, sticky="ew", padx=5, pady=5)

        # 保存变量引用
        setattr(self, f'servo_name_{index}', servo_name)
        setattr(self, f'servo_id_{index}', servo_id)
        setattr(self, f'angle_{index}', angle)
        setattr(self, f'time_{index}', time)
    def control_servo(self, index):
        port = self.selected_port.get()
        baud_rate = self.baud_rate.get()
        servo_id = getattr(self, f'servo_id_{index}').get()
        angle = getattr(self, f'angle_{index}').get()
        time = getattr(self, f'time_{index}').get()
        servo_name = getattr(self, f'servo_name_{index}').get()



        try:
            with serial.Serial(port, baud_rate) as ser:
                servo = UTB.UBT_SERVO(ser, servo_id)
                servo.servo_do(angle, time, 0, 0)
                # print(f"舵机ID {servo_id} 设置为角度 {angle}，持续时间 {time}")
                print(f"{servo_name} ({angle}，{time},0,0)")

        except Exception as e:
            print(f"控制舵机时发生错误: {e}")


if __name__ == "__main__":
    app = ServoControllerApp()
    app.mainloop()
