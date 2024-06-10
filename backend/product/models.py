from django.db import models

from backend.core.models import TimeStampedModel, CreatedBy


class Product(TimeStampedModel, CreatedBy):
    title = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='products',
        db_column='nc_t_52___Category_id',
        null=True,
        blank=True
    )

    class Meta:
        managed = False
        db_table = 'nc_t_52__Product'

    def __str__(self):
        return f'{self.title}'


class Category(TimeStampedModel, CreatedBy):
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nc_t_52___Category'

    def __str__(self):
        return f'{self.title}'
