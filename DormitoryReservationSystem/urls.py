import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('dorm/', include("dorm.urls")),
	path('', include("main.urls")),
	path('account/', include("account.urls")),
	path('booking/', include("booking.urls")),
	path('manage/', include("administer.urls")),
	path("pr/", include("blog.urls"))
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
						  document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,
						  document_root=settings.MEDIA_ROOT)
	urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
