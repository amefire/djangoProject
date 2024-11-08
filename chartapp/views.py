from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from nvd3 import pieChart

from rest_framework.decorators import api_view
from rest_framework.response import Response
#from typing import Optional

def login_view(request):
    # Your custom login implementation here
    pass

@login_required
def chart_view(request):
    chart = pieChart(name='pieChart', color_category='category20c')
    data = [{'label': "Category A", 'value': 20}, {'label': "Category B", 'value': 30}]
    chart.add_serie(y=[d['value'] for d in data], x=[d['label'] for d in data])
    chart.buildhtml()
    return render(request, 'chart.html', {'chart': chart})



@api_view(['GET'])
def chart_data_api(request):
    data = [
        {"label": "Category A", "value": 20},
        {"label": "Category B", "value": 30}
    ]
    return Response(data)