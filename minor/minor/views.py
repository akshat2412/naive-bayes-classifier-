from django.http import HttpResponse, JsonResponse
from django.template import Template, Context
from django.views.generic.base import TemplateView
from classifier.models import *
from django.shortcuts import render
from Thumbnail import createAndStoreThumbnail
from .forms import FileForm
from django.core import serializers as Orig_S
from rest_framework import serializers
import json
from minor.serializers import FileSerializer
import PyPDF2
import sys
from django.core.cache import cache
import subprocess
sys.path.insert(0, '/home/akshat/Downloads')

import input_document

# from google.cloud import language
# from google.cloud.language import enums
# from google.cloud.language import types

# The main lesson here is this: a view is just a Python function that takes an 
# HttpRequest as its first parameter and returns an instance of HttpResponse.


# Each view function takes at least one parameter, called request by convention. 
# This is an object that contains information about the current web request that 
# has triggered this view, and is an instance of the class django.http.HttpRequest.

# second parameter onwards should be the argument of the view function.





imageLocation="/home/akshat/Classifier/minor/static/thumbnails/"
fileLocation="/home/akshat/Classifier/minor/uploads/"
class HomeView(TemplateView):

    template_name = 'Documents.html'
    def get(self, request):
    	test_list=Categories.objects.all()
    	# print test_list
    	files=Files.objects.all()
    	serializer=FileSerializer(files, many=True)
    	dict_1={"files_and_images":serializer.data}
    	# files=json.dumps(files)
    	# files=json.loads(files)
    	# data = Orig_S.serialize("json", files)
    	# # print(type(data))
    	# data = data.encode('ascii')
    	# data = list(data)
    	# # print(type(data))
    	# # data=json.dumps(data)
    	# # data=json.loads(data)
    	# dict_1["context_data"]=data
    	# for item in dict_1["context_data"][0]:
    	# 	print(item)
    	# print("**************")
    	# print(type(dict_1["context_data"][0]))
    	# data=Context({"context_data":data})
    	# print(data["context_data"])
    	# createAndStoreThumbnail(fileLocation=fileLocation, fileName=fileName, imageName=imageName, imageLocation=imageLocation)
    	# test_google_api()
    	# render function is the shortcut function that returns HttpResponse.
    	# its arguments are request, template name and the dictionary.
    	return render(request, self.template_name, dict_1)
    	# return JsonResponse(serializer.data, safe=False)

    def post(self, request):
    	fileForm=FileForm(request.POST, request.FILES)
    	cache.clear()
    	if fileForm.is_valid():
    		# print("Working")
    		fileForm.save()
    		name=str(fileForm.cleaned_data['file_info'])
    		# print(name)
    		image_name=createAndStoreThumbnail(fileName=name, fileLocation=fileLocation, imageName=name[:-4], imageLocation=imageLocation)
    		# # fileForm.save(image_name=image_name)
    		obj=Files.objects.get(name=name)
    		# print(obj)
    		obj.image_name=image_name

    		# pdfFileObj = open("./uploads/"+name, 'rb')
    		# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    		target_file = open("input.txt","w")
    		# pdf_file = open(", "rb")
    		subprocess.call(['pdftotext', "./uploads/"+name, 'input.txt'])
    		# read_pdf = PyPDF2.PdfFileReader(pdf_file)
    		# num_of_pages = read_pdf.getNumPages()
    		# print(num_of_pages)
    		# for page in range(0, num_of_pages):
    		# 	page = read_pdf.getPage(page)
    		# 	page_content = page.extractText()
    		# 	page_content = page_content.encode('utf-8')
    		# 	print("********************************************")
    		# 	print(page_content)
    		# 	target_file.write(page_content)
    		# print page_content
    		# target_file.close()
    		# pdf_file.close()
    		max_class=input_document.prelim("/home/akshat/Classifier/minor/input.txt")
    		obj.categories.add(str(max_class))
    		obj.save()
    		files=Files.objects.all()
    		serializer=FileSerializer(files, many=True)
    		dict_1={"files_and_images":serializer.data}
    		return render(request, self.template_name, dict_1)
    		# return HttpResponse(str(max_class))
    	print("form is not valid")
    	return HttpResponse("Not Working")