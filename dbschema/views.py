from django.shortcuts import render, get_object_or_404
from .models import (
    Project,
    Dataset,
    DatasetFile
)
import csv
from django.http import HttpResponse
from django.template import loader

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

# still working on how to display csv files
# def show_file(request, id):
#     response = HttpResponse(
#         content_type='text/csv',
#         headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
#     )
#
#     file = get_object_or_404(DatasetFile, id=id)
#     file_path = file.file.path
#
#     csv_data = csv.reader(file_path, delimiter=',')
#     t = loader.get_template('dbschema/showfile.txt')
#     c = {'data': csv_data}
#
#     response.write(t.render(c))
#
#     return c



