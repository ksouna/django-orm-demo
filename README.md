Django 初学项目
 
这是一份 Django 入门练习项目，覆盖路由配置、视图函数、模板渲染（DTL模板语法）、ORM操作MySQL、静态文件、请求与响应、重定向、调用外部天气API等Django核心知识点。本项目在 Django 5.2.17 + Python 3.10 环境下编写并测试通过。
 
一、项目结构总览
 
plaintext
  
mysite/
├── manage.py
├── mysite/                 # 项目核心配置目录
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # 项目全局配置
│   ├── urls.py              # 主路由配置
│   └── wsgi.py
├── app/                     # 业务应用
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py            # 数据模型（ORM）
│   ├── tests.py
│   ├── urls.py              # 应用子路由
│   ├── views.py             # 视图函数
│   └── templates/           # 模板文件
│       └── app/
│           └── *.html
└── static/                  # 静态资源：css、js、图片
 
 
二、环境要求
 
- Python： 3.10 
- Django： 5.2.17 
- 数据库：MySQL 8.0+
- 系统：Windows / macOS / Linux
 
三、从零搭建
 
第1步：安装 Python
 
1. 下载 Python3.10，安装时勾选  Add Python to PATH 
2. 验证安装
 
bash
  
python --version
 
 
第2步：创建虚拟环境
 
bash
  
# 创建虚拟环境
python -m venv venv
# 激活虚拟环境
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
 
 
第3步：安装依赖
 
bash
  
pip install django==5.2.17 pymysql requests
# 导出依赖清单
pip freeze > requirements.txt
 
 
第4步：安装并配置 MySQL
 
1. 安装 MySQL8.0，启动服务
2. 创建项目专用数据库
 
sql
  
CREATE DATABASE django_demo DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
 
 
第5步：准备数据库
 
新建数据库用户，分配  django_demo  库权限。
 
第6步：修改数据库连接配置
 
修改  settings.py  中 DATABASES 配置：
 
python
  
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_demo',
        'USER': '你的用户名',
        'PASSWORD': '你的密码',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
 
 
第7步：执行数据迁移
 
bash
  
python manage.py makemigrations
python manage.py migrate
 
 
第8步：启动开发服务器
 
bash
  
python manage.py runserver
 
 
访问： http://127.0.0.1:8000/ 
 
四、功能与页面速览
 
- 首页展示：基础信息展示
- 天气查询页面：调用第三方天气API，输入城市获取实时天气
- 数据列表页：ORM读取MySQL数据展示
- 新增/编辑页面：表单提交，数据库写入
- 404页面：自定义错误页面
 
五、所有URL路由对照表
 
路由地址 对应视图 说明 
 /  index 首页 
 /weather/  weather_view 天气查询 
 /list/  data_list 数据列表 
 /add/  data_add 新增数据 
 
六、核心代码逐模块讲解
 
1. 配置文件 settings.py
 
重点配置项：
 
-  INSTALLED_APPS ：注册app应用
-  STATIC_URL  /  STATICFILES_DIRS ：静态文件路径
-  DATABASES ：数据库连接
-  TEMPLATES ：模板目录配置
 
2. 路由文件 urls.py
 
主路由分发，包含项目根urls与app子路由include引入。
 
3. 视图文件 views.py
 
包含请求接收、参数处理、ORM增删改查、API请求、模板渲染、HttpResponse、redirect重定向。
 
4. 数据模型 models.py
 
Django ORM模型定义，自动映射数据库表结构。
 
5. 模板文件 templates
 
DTL模板语法使用：变量渲染、for循环、if判断、模板继承。
 
6. 静态文件 static
 
css、js、图片资源加载，静态资源引用写法。
 
七、ORM操作速查
 
python
  
# 查询
models.xxx.objects.all()
models.xxx.objects.filter()
# 新增
models.xxx.objects.create()
# 修改
obj = models.xxx.objects.get()
obj.xxx = "xxx"
obj.save()
# 删除
obj.delete()
 
 
八、常见报错与排查
 
1. 数据库连接失败：检查IP、端口、账号密码、数据库是否存在
2. 迁移报错：检查models语法，字段冲突
3. 静态文件404：确认settings静态路径配置正确
4. 模板渲染报错：检查DTL语法、变量是否传递
 
九、项目拓展方向
 
- 用户登录注册（Auth模块）
- 分页功能
- 表单校验
- 部署上线（Gunicorn + Nginx）
 

