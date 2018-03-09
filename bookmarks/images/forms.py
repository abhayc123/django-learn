from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
	class Meta:
		model = Image 
		fields = ('title','url','description')
		widget = {
			'url' : forms.HiddenInput
		}		


	def clean(self):
		url = self.cleaned_data['url']
		valid_extensions = ['jpg','jpeg']
		extension = url.rplit('.',1)[1].lower()
		if 	extension not in valid_extensions:
			raise forms.ValidationError('The given URL does not match valid image exxtensions.')

		return url
		