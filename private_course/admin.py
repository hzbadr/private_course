from .models import *
from django.contrib import admin


class PrivateCourseAdmin(admin.ModelAdmin):
  list_display = ('title', 'description', 'position', 'active', 'capacity', 'hours')
  list_editable = ('position', 'active', 'capacity', 'hours')
  list_filter = ('active',)
  # list_select_related = ('members',)
  ordering = ('position', 'capacity')
  search_fields = ('title',)

class MemberAdmin(admin.ModelAdmin):
    pass

class MembershipAdmin(admin.ModelAdmin):
    pass

admin.site.register(PrivateCourse, PrivateCourseAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Membership, MembershipAdmin)
