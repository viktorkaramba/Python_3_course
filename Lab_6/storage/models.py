from django.db import models


class Goods(models.Model):
    id_go = models.IntegerField(db_column='ID_GO', primary_key=True)  # Field name made lowercase.
    id_se = models.ForeignKey('Sections', models.DO_NOTHING, db_column='ID_SE')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    goodstype = models.CharField(db_column='GOODSTYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goods'


class Sections(models.Model):
    id_se = models.IntegerField(db_column='ID_SE', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sections'


class Number(models.Model):
    id_se = models.IntegerField()

    class Meta:
        managed = False
