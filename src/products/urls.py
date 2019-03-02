
from django.conf.urls import url

from products.views import (
    ProductListView,
    # product_list_view,
    # ProductDetailView,
    # product_detail_view,
    # ProductFeaturedListView,
    # ProductFeaturedDetailView,
    ProductDetailSlugView,
    )

urlpatterns = [

    url(r'^', ProductListView.as_view()),

    url(r'^(?P<slug>[\w-])/$', ProductDetailSlugView.as_view()),



]
    # url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    # url(r'^products-fbv/', product_list_view),
    # url(r'^featured/', ProductFeaturedListView.as_view()),
    # url(r'^featured-fbv/(?P<pk>\d+)', ProductFeaturedDetailView),
    # url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),

