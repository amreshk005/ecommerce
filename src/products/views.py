from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    # def get_context_data(self,*args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args,**kwargs)
    #     return context

    def get_queryset(self, ):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()

    context = {
        'object_list':queryset
    }
    return render(request, "product/product_list_view.html",context)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/Detail.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active = True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except ProductDoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            queryset = Product.objects.filter(slug=slug, active=True)
        except:
            raise Http404("huhh!")
        raise instance


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/Detail.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        return context

    
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("product doesn't exist")
        raise instance


        def get_queryset(self, ):
            request = self.request
            return Product.objects.all()


def product_detail_view(request,pk=None,*args,**kwargs):
    queryset = Product.objects.all()
    isinstance =get_object_or_404(Product, pk=pk)
    context = {
        'object_detail':queryset
    }
    return render(request, "product/product_detail_view.html",context)



class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, ):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = 'products/Detail.html'
    

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()



     


