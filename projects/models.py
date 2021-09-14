from django.db import models
from django.conf import settings
from django.dispatch import receiver

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    # instance is the self Release model, I can access the Release model by it!
    return 'packages/user_{0}/{1}/release_{2}/{3}'.format(instance.author.id, instance.project.id, instance.name, filename)

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    url = models.URLField()
    requirements = models.TextField()
    released_on = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Release(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="releases")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to=user_directory_path)
    released_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project', 'name'], name='project_release_name_unique')
        ]
    def __str__(self):
        return f"release {self.name} in project {self.project} id={self.id}"