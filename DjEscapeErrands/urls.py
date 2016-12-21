from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # host/admin/
    url(r'^admin/', admin.site.urls),
    # host/time_table/
    url(r'^time_table/', include("time_table.urls")),
]
