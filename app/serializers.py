import json
from this import d
from rest_framework import serializers
from .models import *

class EmpanelmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empanelment
        fields = '__all__'

    def validate(self,data):
        for key in data:
            try:
                data[key] = data[key].lower()
            except:
                print("Cannot convert to string")
        return data

    
class MetaExpertSerializer(serializers.ModelSerializer):

    skills = serializers.JSONField()
    
    class Meta:
        model = MetaExpert
        fields = [
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "phone",
            "company",
            "designation",
            "reference_id",
            "biography",
            "price",
            "geography",
            "skills"
        ]

        
    def get_skills(self,obj):
        skills = obj.skills
        if skills:
            return json.loads(skills)
        return []