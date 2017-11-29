from rest_framework import serializers
from classifier.models import Files

class FileSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    name = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    image_name= serializers.CharField(max_length=100)

    class Meta:
        model = Files
        fields = ('name', 'image_name', 'category')
    
    def get_name(self, obj):
    	file=Files.objects.get(name=obj.name)
    	return file.filename()
    def get_category(self, obj):
    	file=Files.objects.get(name=obj.name)
    	category=file.categories.names()
    	if len(category) <= 0:
    		return str(category)
    	category=category[0]
    	category=category.encode('utf-8')
    	return category