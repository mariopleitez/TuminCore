from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def HowItWorks(request):
    api_urls = {
        'Sample Output'
    }
    return Response(sorted(api_urls), 200)


@api_view(['GET'])
def GenerateLoanPaymentPlan(request, Amount, Term, InterestRate):
   


    response = {
        'message': 'Loan has been calculated'
    }
    return Response(response, 200)