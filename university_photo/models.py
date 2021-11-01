from django.db import models
from django.contrib.auth.models import User

class MenuMaster(models.Model): #授業マスター
    CHOICES = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fry', 'Fryday'),
        ('Sat','Saturday'),
        ('Sun','Sunday')
    )
    menu_name = models.CharField(max_length=50)
    created_at = models.DateTimeField("登録日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)
    student = models.ManyToManyField(User,through='RegisterMenu')
    start_time = models.CharField(max_length=20)
    finish_time = models.CharField(max_length=20)
    day = models.CharField(max_length=10,choices = CHOICES)

    def __str__(self):
        return self.menu_name

    
class RegisterMenu(models.Model): #履修
    menu = models.ForeignKey("MenuMaster",on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.menu)
    

class Picture(models.Model): #写真
    register_menu = models.ForeignKey("RegisterMenu",on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField("登録日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True, 
        blank=True
    )
    picture = models.FileField(upload_to='http://university-picture.s3.amazonaws.com/')
    description = models.CharField(max_length=50,blank=True,null=True)
    

class Talk(models.Model): #トーク
    register_menu = models.ForeignKey('RegisterMenu',on_delete=models.CASCADE)
    created_at = models.DateTimeField("登録日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    message = models.TextField()
    image = models.ImageField(upload_to='')



