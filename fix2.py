# -*- coding: utf-8 -*-
with open('action_rec/main_gui.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找到第 49 行（索引 48），它被合并了
# 原始应该是:
#   ShakeHeadStatus.RIGHT_SHAKE_HEAD: '请向右转头',
# }
# 空行
# class CameraWorker(QThread):
#     def __init__(self, parent=None):
#         super().__init__(parent)

old_line = lines[48]
print('修复前:', repr(old_line))

# 拆分这一行
new_lines = [
    "    ShakeHeadStatus.RIGHT_SHAKE_HEAD: '请向右转头',\n",
    "}\n",
    "\n",
    "class CameraWorker(QThread):\n",
    "    def __init__(self, parent=None):\n",
    "        super().__init__(parent)\n",
]

# 替换第 49 行，然后删除原来的 50-53 行（因为已经合并进来了）
lines = lines[:48] + new_lines + lines[54:]

with open('action_rec/main_gui.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('修复完成')
print('第49-55行:')
for i in range(48, 55):
    print(f'  {i+1}: {repr(lines[i])}')
