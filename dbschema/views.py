from django.shortcuts import render, get_object_or_404
from .models import (
    Project,
    Dataset,
    DatasetFile
)
import os
from django.conf import settings
from django.http import HttpResponse, Http404

# Create your views here.
def project_list(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'dbschema/project-list.html', context)

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)

    context = {
        'project':project,
    }

    return render(request, 'dbschema/project-detail.html', context)

def show_file(request, id):
    file = get_object_or_404(DatasetFile, id=id)

    context = {
        'file': file,
    }

    return render(request, 'dbschema/')
