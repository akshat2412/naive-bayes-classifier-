from django import forms
from classifier.models import Files

class FileForm(forms.ModelForm):
	class Meta:
		model=Files
		fields = {
			"file_info",
		}