from django.db import models
from authenticate.models import User
from usgsfeatures.models import SSGI

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(SSGI, on_delete=models.CASCADE)  # Changed `ssgi` to `SSGI`
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='No description provided')

    def __str__(self):
        return f"Bookmark {self.id} by {self.user.username}"
