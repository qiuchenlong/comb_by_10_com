# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

from ppServer.view.ppAnalyze import read_file

def get_inspector(request):
    # return HttpResponse('hello world!')
    context = {}
    context['inspectorObject'] = read_file()

    return render(request, 'inspector.html', context)