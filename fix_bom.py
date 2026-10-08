# 去掉 BOM
with open('action_rec/main_gui.py', 'rb') as f:
    content = f.read()

# 去掉开头的 BOM
if content.startswith(b'\xef\xbb\xbf'):
    content = content[3:]
    print('已去掉 BOM')

with open('action_rec/main_gui.py', 'wb') as f:
    f.write(content)

# 继续检查语法
try:
    compile(content.decode('utf-8'), 'main_gui.py', 'exec')
    print('语法正确')
except SyntaxError as e:
    print(f'语法错误: 第{e.lineno}行 - {e.msg}')
    if e.text:
        print(f'  内容: {e.text.strip()[:100]}')
