# D3HotKeySimulation

方便自己在mac上玩暗黑3，使用pyautogui实现一个基本的鼠标宏。

# Todo

* [ ] 自动拾取
* [ ] 自动分解
* [ ] 图形界面

# 使用方法

运行程序后，F2开始，F4暂停，F8停止。

## 配置

目前共设计了7个按键

| 按键     | 默认按键 |
| -------- | -------- |
| 强制移动 | E        |
| 技能1    | 1        |
| 技能2    | 2        |
| 技能3    | 3        |
| 技能4    | 4        |
| 左键技能 | 鼠标左键 |
| 右键技能 | 鼠标右键 |

四种模式

| 模式 | tag |
| ---- | --- |
| 按住 | 1   |
| 间隔 | 2   |
| 站立 | 3   |
| 停止 | 4   |

以 `config/monk_config.py`为例：

`args_mouse_right= ('mouse', 'right', 2, 3.0)`

该命令的意义是，设置鼠标右键为间隔释放，间隔时间3秒。
