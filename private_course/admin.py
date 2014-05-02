from .models import *
from django.contrib import admin

class MembershipInline(admin.TabularInline):
    model = Membership

class PrivateCourseAdmin(admin.ModelAdmin):
  list_display = ('title', 'description', 'position', 'active', 'capacity', 'hours')
  list_editable = ('position', 'active', 'capacity', 'hours')
  list_filter = ('active',)
  ordering = ('position', 'capacity')
  search_fields = ('title',)

  inlines = (MembershipInline,)

class MemberAdmin(admin.ModelAdmin):
    pass

class MembershipAdmin(admin.ModelAdmin):
    pass

admin.site.register(PrivateCourse, PrivateCourseAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Membership, MembershipAdmin)
