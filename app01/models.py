from django.db import models
class Book(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    title = models.CharField(max_length=32) # 书籍名称
    price = models.DecimalField(max_digits=5, decimal_places=2) # 书籍价格
    publish = models.CharField(max_length=32) # 出版社名称
    objects = models.Manager()
    def myadd(id,title,price,publish):
        insert = Book(id=id,title=title, price=price, publish=publish)
        insert.save()
    def mydelete(id):
        Book.objects.filter(id=id).delete()
    def AddorUpdate(id,title,price,publish):
        alllist = Book.objects.all()
        old_id = []#记录出现过的主码id
        mylist = []
        for v in alllist:
            if(v.id in id):
                old_id.append(v.id)
        for i in range(len(id)):
            if(id[i] not in old_id):
                obj = Book(id=id[i], title=title[i], price=price[i], publish=publish[i])
                mylist.append(obj)
            else:
                Book.objects.filter(id=id[i]).update(title=title[i], price=price[i], publish=publish[i])
        Book.objects.bulk_create(mylist)




    
