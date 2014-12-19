from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo_project.views.home', name='home'),
    # url(r'^demo_project/', include('demo_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^index2$', TemplateView.as_view(template_name='index2.html'), name="index2"),
    url(r'^index3$', TemplateView.as_view(template_name='index3.html'), name="index3"),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name="contact"),
    url(r'^form$', 'bootstrap_demo.views.demo_form'),
    url(r'^form_template$', 'bootstrap_demo.views.demo_form_with_template'),
    url(r'^form_inline$', 'bootstrap_demo.views.demo_form_inline'),
    url(r'^formset$', 'bootstrap_demo.views.demo_formset', {}, "formset"),
    url(r'^tabs$', 'bootstrap_demo.views.demo_tabs', {}, "tabs"),
    url(r'^pagination$', 'bootstrap_demo.views.demo_pagination', {}, "pagination"),
    url(r'^widgets$', 'bootstrap_demo.views.demo_widgets', {}, "widgets"),
    url(r'^buttons$', TemplateView.as_view(template_name='buttons.html'), name="buttons"),
)
