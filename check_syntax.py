import sys
try:
    with open('action_rec/main_gui.py', 'r', encoding='utf-8') as f:
        compile(f.read(), 'main_gui.py', 'exec')
    print('语法正确')
except SyntaxError as e:
    print(f'语法错误: 第{e.lineno}行 - {e.msg}')
    if e.text:
        print(f'  内容: {e.text.strip()[:80]}')
