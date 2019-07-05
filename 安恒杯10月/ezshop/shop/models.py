from django.db import models
from django.contrib.auth.models import User

class Good(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=2000)
	price = models.IntegerField(default=0)
	amount = models.IntegerField(default=0)
	available = models.BooleanField(default=True)

class Order(models.Model):
	user = models.ForeignKey(to=User, on_delete=models.CASCADE)
	good = models.ForeignKey(to=Good, on_delete=models.CASCADE)
	create_time = models.DateTimeField(auto_now_add=True)
	CANCELED = 0
	ONGOING = 1
	FINISHED = 2
	ORDER_STATUS_CHOICES = (
		(CANCELED, '已取消'),
		(ONGOING, '待支付'),
		(FINISHED, '已完成')
	)
	status = models.IntegerField(choices=ORDER_STATUS_CHOICES)
	message = models.CharField(max_length=400, default='')
