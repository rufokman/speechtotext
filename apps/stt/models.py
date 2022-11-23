from django.db import models
from django.urls.base import reverse


class Record(models.Model):
    id = models.IntegerField(db_column='id', blank=False, null=False, primary_key=True, editable=False)
    audio_name = models.TextField()
    voice_record = models.FileField(upload_to="records")
    language = models.CharField(max_length=50, null=True, blank=True)
    dtcreate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("record_detail", kwargs={"id": str(self.id)})

