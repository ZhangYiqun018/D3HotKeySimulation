from multiprocessing import Process
import pynput.keyboard as pk
import pynput
import argparse
from AHK import *
# keyboard 操作
# keyDown 按住不动
# press 按下
# keyUp 松开
# 监听键盘事件

def on_press(key):
    if key == pynput.keyboard.Key.f2:
        print(f"开启鼠标宏...")
        global process
        process = create_process()
        start_process(process)
    if key == pynput.keyboard.Key.space:
        AHK('mouse', 'left', 5, 0.1)

def hotkey_release():
    pag.keyUp('1')
    time.sleep(0.1)
    pag.keyUp('2')
    time.sleep(0.1)
    pag.keyUp('3')
    time.sleep(0.1)
    pag.keyUp('4')
    time.sleep(0.1)
    pag.keyUp('e')
    time.sleep(0.1)
    pag.mouseUp(button='left')
    time.sleep(0.1)
    pag.mouseUp(button='right')

def on_release(key):
    if key == pynput.keyboard.Key.f4:
        print('暂停...')
        hotkey_release()
        end_process(process)
    elif key == pynput.keyboard.Key.f8:
        print('结束...')
        hotkey_release()
        end_process(process)
        return False

def create_process():
    key_e_process       = Process(target=AHK, args=args_key_e)
    key_1_process       = Process(target=AHK, args=args_key_1)
    key_2_process       = Process(target=AHK, args=args_key_2)
    key_3_process       = Process(target=AHK, args=args_key_3)
    key_4_process       = Process(target=AHK, args=args_key_4)
    mouse_left_process  = Process(target=AHK, args=args_mouse_left)
    mouse_right_process = Process(target=AHK, args=args_mouse_right)
    return key_e_process, key_1_process, key_2_process, key_3_process, key_4_process, mouse_left_process, mouse_right_process

def start_process(process):
    for p in process:
        p.start()

def end_process(process):
    for p in process:
        p.terminate()

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--play_role', default='dh', type=str, help='choice your role config')

    args = parser.parse_args()
    return args
if __name__ == '__main__':
    # model 
    ## 1 按住不动
    ## 2 间隔按键
    ## 3 按住shift
    config = get_args()
    if config.play_role == 'dh':
        from config.dh_config import *
    elif config.play_role == 'monk':
        from config.monk_config import *
    else:
        print('error loading config file ...')
    with pk.Listener(on_press=on_press, on_release=on_release) as pklistener:
        pklistener.join()
