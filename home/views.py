import json
from unicodedata import category

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Product, Productimage, Category, Categorysub, Change, TBanner


def index(request):
    return render(request, 'index.html')


def menu_page(request):
    result = {}
    li = []
    lis = []
    # try:
    cates = Category.objects.all()
    banners = TBanner.objects.all()
    if cates:
        for cate in cates:
            # s = cate.id
            cate.page = cate.qs_to_dict(Categorysub.objects.filter(cid=cate.id))
            li.append(cate.to_dict())
            result.update(static=200, msg='success', data=li)
        for banner in banners:
            lis.append(banner.path)
            result.update(img=lis)
        return HttpResponse(json.dumps(result), content_type='Application/json')


def shop_infor(request):
    result = {}
    li = []
    products = Category.objects.all()
    # pro_imgs = Productimage.objects.first(type='type_detail')
    if products:
        for product in products:
            subs = product.product_set.all()  # 相当于 subs = product.product_set.all() 和 Product.objects.all() Product.objects.filter()表示查询每个分类商品的信息
            for cate in subs:
                cate.img = Change.qs_to_dict(cate.product_image.all())
            product.subs = Change.qs_to_dict(subs)
            li.append(product.to_dict())
            result.update(static=200, msg='success', data=li)
        return HttpResponse(json.dumps(result), content_type='Application/json')


def add_shop(request):
    result = {}
    li = []
    lis = []
    pid = request.GET.get('pid')
    products = Product.objects.filter(id=pid)
    for product in products:
        product.img = Change.qs_to_dict(Productimage.objects.filter(pid=pid,type='type_single'))
        a = product.cid.id #特例:product.cid 取出一个product对象,无法与id相等,需要进一步取出里面的id才能与Category的id比较.
        product.topimg = Change.qs_to_dict(Category.objects.filter(id=product.cid.id))
        li.append(product.to_dict())
    result.update(static=200, msg='success', data=li)
    return HttpResponse(json.dumps(result), content_type='Application/json')
