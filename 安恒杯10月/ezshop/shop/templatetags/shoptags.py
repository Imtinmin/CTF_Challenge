from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def form_readable(s):
	form = {
		'order_id': '订单号',
		'buyer_id': '用户 ID',
		'good_id': '商品 ID',
		'buyer_point': '可用积分',
		'good_price': '商品价格',
		'order_create_time': '订单创建时间'
	}
	return form[s] if s in form else s