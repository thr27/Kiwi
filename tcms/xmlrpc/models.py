from django.db import models
from django.conf import settings


class XmlRpcRecord(models.Model):
    dt_inserted = models.DateTimeField(auto_now_add=True)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    method      = models.CharField(max_length=255)
    args        = models.TextField(blank=True)

    def __unicode__(self):
        return u"%s: %s" % (self.user, self.method)
