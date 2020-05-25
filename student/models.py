from django.db import models


# Create your models here.

class Student(models.Model):
    SEX_ITEMS = [
        (1, 'male'),
        (2, 'female'),
        (0, 'unknown'),
    ]
    STATUS_ITEMS = [
        (0, 'apply'),
        (1, 'pass'),
        (2, 'reject'),
    ]
    id = models.CharField(max_length=128, verbose_name="ID", auto_created=True, primary_key=True)
    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="性別")
    profession = models.CharField(max_length=128, verbose_name="職業")
    email = models.EmailField(verbose_name="Email")
    qq = models.CharField(max_length=128, verbose_name="QQ")
    phone = models.CharField(max_length=128, verbose_name="電話")
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="審核狀態")
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="創建時間")

    def __str__(self):
        return '<Student: {}>'.format(self.name)

    class Meta:
        db_table = 'Students'
        verbose_name = "學員信息"
        verbose_name_plural = verbose_name

    @property
    def sex_show(self):
        return dict(self.SEX_ITEMS)[self.sex]

    @classmethod
    def get_all(cls):
        return cls.objects.all()
