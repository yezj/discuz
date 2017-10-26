from django.contrib import admin
import simplejson as json
from django.utils.translation import ugettext_lazy as _
from models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


class AdvertShipInline(admin.TabularInline):
    classes = ('grp-collapse grp-open',)
    model = AdvertShip
    fields = ('advert', 'section', 'position')
    raw_id_fields = ('advert', 'section')
    related_lookup_fields = {
        'fk': ('advert',)
    }
    extra = 0


class AdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url', 'created_at', 'edit_at')


class SectionAdmin(admin.ModelAdmin):
    inlines = (AdvertShipInline,)
    list_display = ('name',)


class AdvertShipAdmin(admin.ModelAdmin):
    list_display = ('advert', 'section', 'created_at', 'position')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Advert, AdvertAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(AdvertShip, AdvertShipAdmin)
