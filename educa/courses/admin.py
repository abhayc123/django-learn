from django.contrib import admin
from .models import Subject , Course , module


@admin.register(Subject)
class 	SubjectAdmin(admin.ModelAdmin):
		list_display = ('title','slug',)
		prepopulated_fields = {'slug':('title',)}


class 	ModuleInline(admin.StackedInline):
		model = module


@admin.register(Course)
class 	CourseAdmin(admin.ModelAdmin):
		list_display = ('title','subject','created')	
		list_filter = ('created','subject')
		search_field = ('title','overview')
		prepopulated_fields = {'slug' : ('title',)}
		inlines = [ModuleInline]

		pass