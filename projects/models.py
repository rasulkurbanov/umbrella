from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=1023, null=True, blank=True)
    source_link = models.CharField(max_length=1023, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Upgrade vote'),
        ('down', 'Downgrade vote')
    )
    project = models.ForeignKey(Project, on_delete=CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
