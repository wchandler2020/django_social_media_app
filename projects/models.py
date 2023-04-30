from django.db import models
import uuid

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    demo_link = models.TextField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updatd = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "tb_projects"


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    #owner=
    project= models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updatd = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.project} got a {self.value} from user'

    class Meta:
        db_table = "tb_reviews"

class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updatd = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        db_table = "tb_tags"
