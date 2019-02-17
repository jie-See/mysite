from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


# Create your views here.


def hello(request):
    '''
    request.path                完整的路径，不含域名，但是包含前导斜线 ,如“/hello/”
    request.get_host()          主机名（即通常所说的“域名”）,如“127.0.0.1:8000”或“www.example.com”
    request.get_full_paht()     包含查询字符串（如果有的话）的路径，如“/hello/?print=true”
    request.is_secure()         通过 HTTPS 访问时为 True，否则为 False，如True 或 False
    request.META的值是一个字典：
        HTTP_REFERER：入站前的 URL（可能没有）。（注意，要使用错误的拼写，即 REFERER。）
        HTTP_USER_AGENT：浏览器的用户代理（可能没有）。例如："Mozilla/5.0 (X11; U; Linux i686; frFR;rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17"。
        REMOTE_ADDR：客户端的 IP 地址，例如 "12.345.67.89"。（如果请求经由代理，这个首部的值可能是一组 IP 地址，以逗号分隔，例如 "12.345.67.89,23.456.78.90"。）
    '''
    return HttpResponse('hello world')


def current_url_view_bad(request):
    return HttpResponse('Welcome to the page at /current/')


def current_url_view_good(request):
    return HttpResponse('Welcome to the page at %s' % request.get_host())


def ua_display_bad(request):
    ua = request.META['HTTP_USER_AGENT']
    return HttpResponse("Your browser is %s" % ua)


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    if 'q' in request.GET:
        message = 'You searched for:%r'%request.GET['q']
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request,'search_results.html', {'books': books, 'query': q})
    else:
        # message = 'You submitted an empty form.'
        # return HttpResponse(message)
        return render(request, 'search_form.html', {'error': True})
