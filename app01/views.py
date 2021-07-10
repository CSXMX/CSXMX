from django.shortcuts import render,redirect
from app01.models import Book
def add_publisher(request):
    request.encoding = 'utf-8'
    if request.method == 'POST' and request.POST:
        id = request.POST.get("id")
        title = request.POST.get("title")
        price = request.POST.get("price")
        publish = request.POST.get("publish")
        if 'add' in request.POST:
            Book.myadd(id,title,price,publish)
        if 'delete' in request.POST:
            Book.mydelete(id)
        if 'AddorUpdate' in request.POST:
            id = [1,2,3]
            title = ['编译原理','操作系统', '数字媒体']
            price = [10,20, 30]
            publish = ['120','200', '355']
            Book.AddorUpdate(id, title, price, publish)
        print(id,title,price,publish)
        #print(Book.objects.all())
        return redirect("/app01/publisher_list/")
    return render(request,"add_publisher.html")

def publisher_list(request):
    list = Book.objects.all()
    return render(request, "publisher_list.html",{"list":list})

