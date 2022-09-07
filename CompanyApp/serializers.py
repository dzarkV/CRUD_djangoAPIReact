from rest_framework import serializers
from CompanyApp.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('CompanyId',
                  'CompanyName',
                  'Address',
                  'NIT',
                  'PhoneNumber')