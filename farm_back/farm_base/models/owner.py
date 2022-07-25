from django.contrib.gis.db import models
from django.utils.translation import gettext as _
from farm_base.models.utils import choices

class Owner(models.Model):
    name = models.CharField(verbose_name=_("Name"),
                            max_length=255)

    document = models.CharField(verbose_name=_("Document"),
                                max_length=255)

    document_type = models.CharField(verbose_name=_("Document type"),
                                     max_length=10,
                                     choices=choices.DOCUMENT_TYPE_CHOICES)

    creation_date = models.DateTimeField(verbose_name=_("Creation date"),
                                         auto_now_add=True, editable=False)

    last_modification_date = models.DateTimeField(
        verbose_name=_("Last modification date"), auto_now=True)

    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)

    def __str__(self):
        return str(self.name)

    def get_class_name(self):
        return "owner"

    class Meta:
        unique_together = ['document', 'document_type']
        ordering = ['id']
        verbose_name = _('Owner')
        verbose_name_plural = _('Owners')


def get_sentinel_owner():
    return Owner.objects.get_or_create(name="Sentinel Owner", document="N/A", document_type="CPF")[0]

def get_sentinel_owner_id():
    return get_sentinel_owner().id
    