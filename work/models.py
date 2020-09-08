from django.db import models

# Create your models here.

"""快捷清单"""
class QuickList(models.Model):
  id = models.BigAutoField(primary_key=True, db_column='id', verbose_name='主键')
  itemName = models.CharField(max_length=50, db_column='item_name', verbose_name='待办事项')
  dealTime = models.DateTimeField(db_column='deal_time', verbose_name='处理时间')
  userNo = models.CharField(max_length=10, db_column='user_no', verbose_name='用户账户')
  userName = models.CharField(max_length=10, db_column='user_name', verbose_name='用户姓名', null=True)
  orderNo = models.PositiveSmallIntegerField(db_column='order_no', verbose_name='顺序号')
  complateFlag = models.BooleanField(db_column='complete_flag', verbose_name='完成情况：0：未完成；1：已完成')
  complateRemark = models.CharField(max_length=500, db_column='complete_remark', verbose_name='完成备注', null=True)
  createTime = models.DateTimeField(db_column='create_time', verbose_name='创建时间')
  updateTime = models.DateTimeField(db_column='update_time', verbose_name='更新时间')

  class Meta:
    db_table = 'biz_quick_list'
