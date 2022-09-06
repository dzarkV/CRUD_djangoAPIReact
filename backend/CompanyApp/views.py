from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CompanyApp.models import Company
from CompanyApp.serializers import CompanySerializer

# Create your views here.

@csrf_exempt
def companyApi(request,id=0):
    if request.method=='GET':
        companies = Company.objects.all()
        company_serializer = CompanySerializer(companies, many=True)
        return JsonResponse(company_serializer.data, safe=False)

    elif request.method=='POST':
        company_data = JSONParser().parse(request)
        company_serializer = CompanySerializer(data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        company_data = JSONParser().parse(request)
        company = Company.objects.get(CompanyId = company_data['CompanyId'])
        company_serializer = CompanySerializer(company,data = company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        company = Company.objects.get(CompanyId=id)
        employee.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
