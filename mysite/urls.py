from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('doctor/', include('doctor.urls')),
                  path('location/', include('location.urls')),
                  path('patient/', include('patient.urls')),
                  path('transaction/', include('transaction.urls')),
                  path('support/', include('support.urls')),
                  path('account/', include('account.urls')),
                  path('refund/', include('refund.urls')),
                  path('visit/', include('visit.urls')),
                  path('', TemplateView.as_view(template_name='index.html'), name='home'),
                  path('about/', TemplateView.as_view(template_name='static_templates/about.html'), name='about'),
                  path('contact/', TemplateView.as_view(template_name='static_templates/contact.html'), name='contact')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
