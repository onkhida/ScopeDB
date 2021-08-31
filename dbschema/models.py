from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse

# The Whole Structure
# Basically, each project has datasets concerning whatever.
# In those datasets, one may include multiple files

# For Example,
# If I have a project called plants
# There may be a dataset on like hibiscus flowers
# Then the user may upload files concerning hibiscus flowers
# Maybe: hibiscus_length.csv, hibiscus_weight.csv
# That was my thought process for this thing
# Project > Datasets > Files


class Project(models.Model):
    curator = models.ForeignKey(User,
                                related_name='projects',
                                on_delete=models.CASCADE)
    published = models.DateField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    description = models.TextField()
    institute = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    dburl = models.URLField()
    samples = models.PositiveIntegerField()

    # i will add tags for the future
    # tags help in things like powerful search ranking etc

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project', args=[self.id])
    tags = TaggableManager()


class Dataset(models.Model):
    name = models.CharField(max_length=255)
    free = models.BooleanField(default=True) # the dataset is free by default

    # the specific user who made the dataset
    curator = models.ForeignKey(User,
                                related_name='curator',
                                on_delete=models.CASCADE)
    # the specific database that the dataset is tied to
    database = models.ForeignKey(Project,
                                 related_name='datasets',
                                 on_delete=models.CASCADE)
    samples = models.PositiveIntegerField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{} dataset on {} project'.format(self.name, self.database.name)

    # from what i hear, the user may upload multiple csv files to be part of that dataset

class DatasetFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    dataset = models.ForeignKey(Dataset,
                                on_delete=models.CASCADE,
                                related_name='files')

    def __str__(self):
        return 'File in {}'.format(self.dataset.name)

    def get_absolute_url(self):
        return reverse('show-file', args=[self.id])

    # basically this dataset file is tied to a specific dataset





