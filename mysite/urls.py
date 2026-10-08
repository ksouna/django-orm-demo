from django.urls import path

from app01 import views

urlpatterns = [
    path('index/', views.index),

    path('user/list/',views.user_list),

    path('user/add/',views.user_add),

    path('tpl/',views.tpl),

    path('weather/',views.weather),

    path('something/',views.something),

    path('login/',views.login),

    path('orm',views.orm),

    path('info/list/',views.info_list),

    path('info/add/',views.info_add),

    path('info/delete/',views.info_delete)
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gx_day15',  # 数据库名字
        'USER': 'root',
        'PASSWORD': 'root123',
        'HOST': '127.0.0.1',  # 那台机器安装了MySQL
        'PORT': 3306,
    }
}


