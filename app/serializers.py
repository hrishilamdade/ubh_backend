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
    education = serializers.JSONField()
    experience = serializers.JSONField()

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
            "education",
            "experience",
            "price",
            "geography",
            "skills"
        ]

    
    def get_education(self,obj):
        education = obj.education
        if education:
            return json.loads(education)
        return []
    
    def get_experience(self,obj):
        experience = obj.experience
        if experience:
            return json.loads(experience)
        return []
    
    def get_skills(self,obj):
        skills = obj.skills
        if skills:
            return json.loads(skills)
        return []