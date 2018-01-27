from django.shortcuts import render
from django.views.generics.list import ListView
from .models import Course
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from braces.views import LoginRequiredMixin , PermissionRequiredMixin
from .mixins import *


class 	ManageCourseListView(OwnerCourseMixin , ListView):
		template_name = 'courses/manage/course/list.html'


class 	CourseCreateView(PermissionRequiredMixin , OwnerCourseEditMixin , CreateView):
		permission_required = 'courses.add_course'


class 	CourseUpdateView(PermissionRequiredMixin , OwnerCourseEditMixin , UpdateView)
		permission_required = 'courses.change_course'


class 	CourseDeleteView(PermissionRequiredMixin , OwnerCourseMixin , DeleteView):
		template_name = 'courses/manage/course/delete.html'
		success_url = reverse_lazy('manage_course_list')
		permission_required = 'courses.delete_course'



# class 	ManageCourseListView(ListView):
# 		model = Course
# 		template_name = 'courses/manage/course/list.html'


# 		def get_queryset(self):
# 			qs = super(ManageCourseListView , self).get_queryset()
# 			return qs.filter(owner = self.request.user)
