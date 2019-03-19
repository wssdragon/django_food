from django.db import models
from datetime import datetime

class Food(models.Model):
	shop_no = models.AutoField(primary_key=True) # 상점번호
	shop_nm = models.CharField(null=False,max_length=50) # 상점명
	place_id = models.IntegerField(null=True) # 네이버지도테이블 PK
	restaurant_type = models.CharField(null=True,max_length=3) # 상점타입
	group_seat_yn = models.CharField(null=True,max_length=1,default="N") # 단체석상태
	type = models.CharField(null=True,max_length=1) # 성격F=격식,C=캐주얼)
	hash_tag = models.CharField(null=True,max_length=200) # 해시태그
	shop_img = models.CharField(null=True,max_length=500) # 상점이미지
	reg_id = models.CharField(null=False,max_length=25) # 등록ID
	reg_dt = models.DateField(default=datetime.now,blank=True) # 등록일
	chg_id = models.CharField(null=True,max_length=25) # 수정ID
	chg_dt = models.DateField(null=True,blank=True) # 수정일
