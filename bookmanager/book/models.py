from django.db import models

# Create your models here.
"""
1.我们的模型类 需要继承自model.Model
2.系统会自动为我们添加一个主键--id
3.字段
    
    字段=model.类型(选项)
    字段名其实就是数据表的字段名
    字段名不要使用python,mysql等关键字
    
    char(m)
    varchar(m)
    m 就是选项
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    # 重写 str方法以让admin来显示书籍名字
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
