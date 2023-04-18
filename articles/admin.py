from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_filter = ['date']


admin.site.register(HomeCaruselModel)
admin.site.register(FutureModels)
admin.site.register(SubMenuModels)
admin.site.register(MainSiteModels)
# admin.site.register(About)
admin.site.register(AboutMaydon)
admin.site.register(Newsmodel, NewsAdmin)
admin.site.register(NewsPrise)
admin.site.register(XodimModel)
