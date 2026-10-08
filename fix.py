# -*- coding: utf-8 -*-
import os

with open('action_rec/main_gui.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复路径行
old_path = "sys.path.insert(0, _BASE_DIR)`nsys.path.insert(0, os.path.dirname(_BASE_DIR))  # 项目根目录"
new_path = "sys.path.insert(0, _BASE_DIR)\n" + "sys.path.insert(0, os.path.dirname(_BASE_DIR))  # 项目根目录"
content = content.replace(old_path, new_path)

# 修复 POSE_HINTS
old_hints = "ShakeHeadStatus.LEFT_SHAKE_HEAD: '"
import re
# 直接修复未闭合的字符串
content = re.sub(
    r"ShakeHeadStatus\.LEFT_SHAKE_HEAD: '[^']*,",
    "ShakeHeadStatus.LEFT_SHAKE_HEAD: '请向左转头',",
    content
)
content = re.sub(
    r"ShakeHeadStatus\.RIGHT_SHAKE_HEAD: '[^']*,",
    "ShakeHeadStatus.RIGHT_SHAKE_HEAD: '请向右转头',",
    content
)
content = re.sub(
    r"ShakeHeadStatus\.FRONT_SHAKE_HEAD: '[^']*',",
    "ShakeHeadStatus.FRONT_SHAKE_HEAD: '面对摄像头',",
    content
)

with open('action_rec/main_gui.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('修复完成')
