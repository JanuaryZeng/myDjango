import os
from django.conf.urls import url
from django.conf.urls.static import static

from myDjango.settings import BASE_DIR
from . import views

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/') # media即为图片上传的根路径
MEDIA_URL = '/media/'

urlpatterns = [
    # 定义url，移动端通过这个url访问服务端
    url(r'^users/$', views.user_api),
    # username就是之前views中another_user_api方法中的参数
    url(r'^users/(?P<userid>[A-Za-z0-9]+)/$', views.another_user_api),
    url(r'^android_user/$', views.android_user_api),
    url(r'^uploading/$', views.uploadImages),
    url(r'^uploadicon/$', views.upLoadIcon)

]+ static(MEDIA_URL, document_root=MEDIA_ROOT)
