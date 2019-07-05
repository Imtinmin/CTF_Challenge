from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Good, Order
from django.contrib.auth.decorators import login_required
from hashlib import md5
from ezshop.settings import RANDOM_SECRET_KEY_FOR_PAYMENT_SIGNATURE
# Create your views here.

def shopIndexView(request):
	good = Good.objects.filter(available=True)
	return render(request, 'shop/index.html', {'good': good})

@login_required
def createOrderView(request, goodid):
	good = get_object_or_404(Good, id=goodid, available=True)
	newOrder = Order(user=request.user, good=good, status=Order.ONGOING)
	newOrder.save()
	return redirect('shop:myOrder')

@login_required
def myOrderView(request):
	myorder = Order.objects.filter(user=request.user).order_by('-create_time')
	return render(request, 'shop/myOrder.html', {'myorder': myorder})

@login_required
def cancelOrder(request, orderid):
	o = get_object_or_404(Order, id=orderid, user=request.user, status=Order.ONGOING)
	o.status = Order.CANCELED
	o.save()
	return redirect('shop:myOrder')

@login_required
def payOrder(request, orderid):
	o = get_object_or_404(Order, id=orderid, user=request.user, status=Order.ONGOING)
	form = {
		'order_id': o.id,
		'buyer_id': o.user.id,
		'good_id': o.good.id,
		'buyer_point': o.user.profile.point,
		'good_price': o.good.price,
		'order_create_time': o.create_time.timestamp()
	}
	str2sign = RANDOM_SECRET_KEY_FOR_PAYMENT_SIGNATURE + '&'.join([f'{i}={form[i]}' for i in form]).encode('utf-8')
	#print(str2sign)
	sign = md5(str2sign).hexdigest()
	#print(sign)
	return render(request, 'payment/confirm.html', {'form': form, 'sign': sign})

@login_required
def cleanCanceledOrder(request):
	o = Order.objects.filter(user=request.user, status=Order.CANCELED).delete()
	return redirect('shop:myOrder')
