from django.contrib import admin
from food.models import Food

class FoodAdmin(admin.ModelAdmin):
	# 관리자 페이지에 표시할 필드 목록을 튜플 형식으로 선언
	list_display = ["shop_no","shop_nm","reg_id","reg_dt"]
	
# 관리자 사이트에 테이블 등록
admin.site.register(Food, FoodAdmin)
