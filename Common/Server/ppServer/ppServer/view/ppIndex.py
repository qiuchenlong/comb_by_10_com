# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

from ppServer.view.ppAnalyze import read_file

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def dir_list(path, allfile, result_object):
    filelist = os.listdir(path)


    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dir_list(filepath, allfile, result_object)
        else:
            allfile.append(filepath)
            if '.py' in filepath and '.pyc' not in filepath:

                result_object.append(read_file(filepath))



    return result_object


def get_inspector(request):
    context = {}

    result_object = []
    dir_list(BASE_DIR.replace('/Common/Server/ppServer/ppServer', ''), [], result_object)
    context['inspectorObject'] = result_object

    # context['inspectorObject'] = read_file()

    return render(request, 'inspector.html', context)