from .models import Course
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin , PermissionRequiredMixin


class 	OwnerMixin(object):
		def get_queryset(self):
			qs = super(OwnerMixin , self).get_queryset()
			return qs.filter(owner=self.request.user)


class 	OwnerEditMixin(object):
		def form_valid(self , form):
			form.instance.owner = self.request.user
			return super(OwnerEditMixin , self).form_valid(form)


class 	OwnerCourseView(OwnerMixin):
		model = Course


class 	OwnerCourseEditMixin(OwnerCourseMixin , OwnerEditMixin):
		fields = ['subject','title','slug','overview']
		success_url = reverse_lazy('manage_course_list')
		template_name = 'courses/manage/course/form.html'


class 	OwnerCourseMixin(OwnerMixin , LoginRequiredMixin):
		model = Course
		fields = ['subject','title','slug','overview']
		success_url = reverse_lazy('manage_course_list')		

