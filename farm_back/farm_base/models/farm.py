from django.contrib.gis.db import models
from django.utils.translation import gettext as _
from farm_base.models.utils import choices
from farm_base.models.owner import Owner, get_sentinel_owner, get_sentinel_owner_id

class Farm(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255,
                            null=False, blank=False, default="N/A")

    municipality = models.CharField(verbose_name=_("Municipality"), max_length=255, 
                                    null=False, blank=False, default="N/A")
    
    state = models.CharField(verbose_name=_("State"), max_length=2,
                            choices=choices.STATE_CHOICES, null=False, blank=False, default="SP")

    owner = models.ForeignKey(Owner, verbose_name=_("Owner"), on_delete=models.SET(get_sentinel_owner), 
                                null=False, blank=False, default=get_sentinel_owner_id)

    geometry = models.GeometryField(verbose_name=_("Geometry"),
                                    null=True, blank=True)

    area = models.FloatField(verbose_name=_("Area"),
                             blank=True, null=True)

    centroid = models.PointField(verbose_name=_("Centroid"),
                                 blank=True, null=True)

    creation_date = models.DateTimeField(verbose_name=_("Creation date"),
                                         auto_now_add=True, editable=False)

    last_modification_date = models.DateTimeField(
        verbose_name=_("Last modification date"), auto_now=True)

    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['id']
        verbose_name = _('Farm')
        verbose_name_plural = _('Farms')