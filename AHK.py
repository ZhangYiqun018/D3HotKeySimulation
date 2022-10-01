import pyautogui as pag
import time

class AHK():
    def __init__(self, 
        type: str, 
        button: str,
        model: str,
        intelval: int
        ):
        if type == '键盘' or type == 'keyboard':
            self.keyboard(button, model, intelval)
        elif type == '鼠标' or type == 'mouse':
            self.mouse(button, model, intelval)
        else:
            print('type设置错误！')
    def keyboard(self, button, model, interval):
        # 四种模式
        # 1 按住不动
        # 2 间隔按
        # 3 站立按
        # 4 禁止
        if model == 1:
            pag.keyDown(button)
        elif model == 2:
            while True:
                pag.press(button)
                time.sleep(interval)
        elif model == 3:
            while True:
                pag.keyDown('shift')
                pag.press(button)
                pag.keyUp('shift')
                time.sleep(interval)
        elif model == 4:
            pass

    def mouse(self, button, model, interval):
        if button != 'left' and button != 'right':
            print('button设置错误！')
        if model == 1:
            pag.mouseDown(
                button=button
            )
        elif model == 2:
            while True:
                pag.click(
                    clicks=1,
                    button=button,
                )
                time.sleep(interval)
        elif model == 3:
            while True:
                pag.keyDown('shift')
                pag.click(
                    clicks=1,
                    button=button
                )
                pag.keyUp('shift')
                time.sleep(interval)
        elif model == 4:
            pass
        elif model == 5:
            # 鼠标特殊事件，连点模式
            print("连点20下")
            for _ in range(20):
                pos = pag.position()
                pag.click(
                    x = pos[0],
                    y = pos[1],
                    clicks=1,
                    button='left',
                )
                time.sleep(interval)