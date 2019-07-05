from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from hashlib import md5
from shop.models import Good, Order
from django.contrib.auth.models import User
from os import urandom
from ezshop.settings import RANDOM_SECRET_KEY_FOR_PAYMENT_SIGNATURE, REAL_FLAG
from random import randint


# Create your views here.

@csrf_exempt
def checkPayment(request):
	# print(request.body)
	ret = {'result': '未知错误', 'status': 'danger'}
	sign = request.GET.get('signature', '')
	if md5(RANDOM_SECRET_KEY_FOR_PAYMENT_SIGNATURE + request.body).hexdigest() == sign:
		o = get_object_or_404(Order, id=request.POST.get('order_id'))
		g = get_object_or_404(Good, id=request.POST.get('good_id'))
		u = get_object_or_404(User, id=request.POST.get('buyer_id'))
		# 检查订单是否为待支付状态
		if o.status != Order.ONGOING:
			ret['result'] = f'订单 {o.id} 状态异常，可能已完成或已取消'
		# 检查商品是否可购买
		elif g.available != True or g.amount <= 0:
			ret['result'] = f'商品 {g.id} 暂时不可购买，可能库存不足'
		# 检查用户可用积分是否足够
		elif u.profile.point < g.price:
			ret['result'] = f'用户 {u.username} 可用积分不足，无法完成支付'
		else:
			if u.is_staff != True:
				u.profile.point -= g.price
				u.save()
			g.amount -= 1
			if g.name == 'FLAG':
				o.message = REAL_FLAG
			else:
				o.message = f'fake_flag{{{md5(urandom(32)).hexdigest()}}}<br>(购买“FLAG”才能获得真正的 flag)'
			if g.amount <= randint(0, 100):
				g.amount += randint(100, 200)
			g.save()
			o.status = Order.FINISHED
			o.save()
			ret['result'] = f'订单 {o.id} 支付成功！'
			ret['status'] = 'success'
	else:
		ret['result'] = '签名不正确，数据可能被篡改！'
	return render(request, 'payment/result.html', ret)
