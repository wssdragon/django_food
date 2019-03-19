from django.shortcuts import render, render_to_response
from food.models import Food
from django.template.defaulttags import register

# Create your views here.


def boardList(request):
	
	food_list = Food.objects.all().order_by('-shop_no')
	restrn_type = {'FU':'퓨전'
		,'KR':'한식'
		,'IT':'이태리'
		,'JP':'일식'
		,'CN':'중식'
		,'VT':'베트남'
		,'TH':'태국'
		,'US':'아메리칸'
		,'MX':'멕시코'
		,'AA':'술집'
	}
	test_list = ["1","2","3"]
	return render_to_response("boardList.html", {"food_list":food_list, "restrn_type":restrn_type, "test_list":test_list})


# 딕셔너리 get 필터
@register.filter
def get_item(dictionary, key):
	return dictionary.get(key)

# String Split 필터
@register.filter(name='split')
def split(value, arg):
	return value.split(arg)
