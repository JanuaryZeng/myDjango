from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from myDjan.models import moneychangetable,lovertable,moneytypetable,notetable,usertable,friendtable
from . import models

@admin.register(moneychangetable)
class moneychangetableAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('moneychangeid', 'moneydate','moneynumber','loverid','moneytypeid')

    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    #ordering设置默认排序字段，负号表示降序排序
    # ordering = ('-publish_time',)

    #list_editable 设置默认可编辑字段
    list_editable = ['moneydate','moneynumber','loverid','moneytypeid']

    #fk_fields 设置显示外键字段
    fk_fields = ('loverid')
    search_fields = ('moneydate','moneynumber','loverid','moneytypeid')  # 搜索字段

@admin.register(lovertable)
class lovertableAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('loverid','loverpassword','loverdate','moneyout','moneyin')

    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    #ordering设置默认排序字段，负号表示降序排序
    # ordering = ('-publish_time',)

    #list_editable 设置默认可编辑字段
    list_editable = ['loverpassword','loverdate','moneyout','moneyin']

    #fk_fields 设置显示外键字段
    # fk_fields = ('loverid')
    search_fields = ('loverid','loverpassword','loverdate','moneyout','moneyin')  # 搜索字段



@admin.register(moneytypetable)
class moneytypetableAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('moneytypeid', 'moneytypeicon','moneydirction')

    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    #ordering设置默认排序字段，负号表示降序排序
    # ordering = ('-publish_time',)

    #list_editable 设置默认可编辑字段
    list_editable = ['moneytypeicon','moneydirction']

    #fk_fields 设置显示外键字段
    # fk_fields = ('loverid')
    search_fields = ('moneytypeid', 'moneytypeicon','moneydirction')  # 搜索字段

@admin.register(notetable)
class notetableAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('noteid', 'loverid','moneytypeid','notedate','notetext','notestatus')

    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('noteid',)

    #list_editable 设置默认可编辑字段
    list_editable = [ 'loverid','moneytypeid','notedate','notetext','notestatus']

    #fk_fields 设置显示外键字段
    fk_fields = ('loverid','moneytypeid')
    search_fields = ('noteid', 'loverid','moneytypeid','notedate','notetext','notestatus')  # 搜索字段

@admin.register(usertable)
class usertableAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('userid', 'loverid', 'usergender', 'username', 'usericon', 'userborn')

    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('userid',)

    #list_editable 设置默认可编辑字段
    list_editable = [ 'loverid', 'usergender', 'username', 'usericon', 'userborn']

    #fk_fields 设置显示外键字段
    fk_fields = ('loverid')
    search_fields = ('userid', 'loverid', 'usergender', 'username', 'usericon', 'userborn')  # 搜索字段

@admin.register(friendtable)
class friendtableAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('friendid', 'loverid', 'usergender', 'frienddate', 'friendphotos1','friendphotos2','friendphotos3','friendphotos4', 'friendtext')

    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('friendid',)

    #list_editable 设置默认可编辑字段
    list_editable = [ 'loverid', 'usergender', 'frienddate', 'friendphotos1','friendphotos2','friendphotos3','friendphotos4', 'friendtext']

    #fk_fields 设置显示外键字段
    fk_fields = ('loverid')
    search_fields = ('friendid', 'loverid', 'usergender', 'frienddate', 'friendphotos1','friendphotos2','friendphotos3','friendphotos4', 'friendtext')  # 搜索字段



admin.site.site_title="恋爱记管理"
admin.site.site_header="恋爱记管理"
admin.site.index_title="恋爱记管理"


admin.site.unregister(lovertable)
admin.site.unregister(moneychangetable)
admin.site.unregister(moneytypetable)
admin.site.unregister(notetable)
admin.site.unregister(usertable)
admin.site.unregister(friendtable)


admin.site.register(lovertable,lovertableAdmin)
admin.site.register(moneychangetable,moneychangetableAdmin)
admin.site.register(moneytypetable,moneytypetableAdmin)
admin.site.register(notetable,notetableAdmin)
admin.site.register(usertable,usertableAdmin)
admin.site.register(friendtable,friendtableAdmin)