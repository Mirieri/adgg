import json

from django.db import models
from django.utils.functional import cached_property

from . import constants


class Reg02Maininfo(models.Model):
    surveyid = models.CharField(max_length=80, blank=True, null=True)
    originid = models.CharField(max_length=15, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    deviceid = models.CharField(max_length=60, blank=True, null=True)
    regdate = models.DateTimeField(verbose_name='Registration Date', blank=True, null=True)
    enumtype = models.CharField(max_length=1, db_column='enumtype', blank=True, null=True, choices=constants.ENUMTYPE)
    #aitechid = models.ForeignKey('Reg01Maininfo', models.DO_NOTHING, db_column='aitechid', blank=True, null=True)
    #datacollid = models.ForeignKey('Reg01BMaininfo', models.DO_NOTHING, db_column='datacollid', blank=True, null=True)
    #hh_country = models.ForeignKey('Reg01LkphhCountry', models.DO_NOTHING, db_column='hh_country', blank=True, null=True)
    #hh_region = models.ForeignKey('Reg01LkphhRegion', models.DO_NOTHING, db_column='hh_region', blank=True, null=True)
    hh_district = models.ForeignKey('Reg01Lkpmaindistrict', models.DO_NOTHING, db_column='hh_district', blank=True, null=True, verbose_name='District')
    #hh_kebele = models.ForeignKey('Reg01Lkpmainwards', models.DO_NOTHING, db_column='hh_kebele', blank=True, null=True)
    #hh_village = models.ForeignKey('Reg02LkphhVillage', models.DO_NOTHING, db_column='hh_village', blank=True, null=True)
    farmername = models.TextField(verbose_name='Farmer Full Name', blank=True, null=True)
    farmermobile = models.CharField(primary_key=True, max_length=60, verbose_name='Farmer Mobile Number')
    #farmergender = models.ForeignKey('Reg01Lkptechgender', models.DO_NOTHING, db_column='farmergender', blank=True, null=True)
    #farmerage = models.ForeignKey('Reg02Lkpfarmerage', models.DO_NOTHING, db_column='farmerage', blank=True, null=True)
    farmerhhhead = models.IntegerField(verbose_name='Farmer household head', blank=True, null=True)
    #farmerrltshiphhoth = models.ForeignKey('Reg02Lkpfarmerrltshiphhoth', models.DO_NOTHING, db_column='farmerrltshiphhoth', blank=True, null=True)
    hhhname = models.TextField(verbose_name='House Hold Name',blank=True, null=True)
    hhhmobile = models.CharField(verbose_name='House Hold Mobile',max_length=60, blank=True, null=True)
    hhhgender = models.CharField(verbose_name='House Hold Gender',max_length=1, db_column='hhhgender', blank=True, null=True, choices=constants.ENUMTYPE_GENDER)
    #hhhage = models.ForeignKey('Reg02Lkpfarmerage', models.DO_NOTHING, db_column='hhhage', blank=True, null=True)
    nmale0to5 = models.IntegerField(verbose_name='Number of males 0 to 5', blank=True, null=True)
    nfem0to5 = models.IntegerField(verbose_name='Number of females 0 to 5', blank=True, null=True)
    nmale6to14 = models.IntegerField(verbose_name='Number of males 6 to 14', blank=True, null=True)
    nfem6to14 = models.IntegerField(verbose_name='Number of females 6 to 14', blank=True, null=True)
    nmale15to64 = models.IntegerField(verbose_name='Number of males 15 to 64', blank=True, null=True)
    nfem15to64 = models.IntegerField(verbose_name='Number of females 15 to 64', blank=True, null=True)
    nmaleo65 = models.IntegerField(verbose_name='Number of males above 65', blank=True, null=True)
    nfemo65 = models.IntegerField(verbose_name='Number of males above 65', blank=True, null=True)
    members_no = models.IntegerField(blank=True, null=True)
    c_percelno = models.IntegerField(blank=True, null=True)
    lvstckinhh = models.CharField(verbose_name='Livestock in household',max_length=15, blank=True, null=True)
    cattletotalowned = models.IntegerField(verbose_name='Total cattle owned', blank=True, null=True)
    cattleownmle = models.IntegerField(verbose_name='Cattle owned by males', blank=True, null=True)
    cattleownfmle = models.IntegerField(verbose_name='Cattle owned by females', blank=True, null=True)
    cattleownjntly = models.IntegerField(verbose_name='Cattle owned Jointly', blank=True, null=True)
    totanim = models.CharField(verbose_name='Total animals', max_length=255, blank=True, null=True)
    animcatowned = models.CharField(max_length=13, blank=True, null=True)
    hhproblems = models.CharField(verbose_name='House hold problems', max_length=22, blank=True, null=True)
    hhproblemsoth = models.TextField(verbose_name='Other House Hold Problems',blank=True, null=True)
    gpsloc = models.CharField(verbose_name='GPS location',max_length=60, blank=True, null=True)
    rowuuid = models.CharField(max_length=80, blank=True, null=True)
    welcomesent = models.IntegerField(blank=True, null=True)
    apologysent = models.IntegerField(blank=True, null=True)
    inadggbundle = models.IntegerField(blank=True, null=True)
    inpaidbundle = models.IntegerField(blank=True, null=True)
    icow = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'reg02_maininfo'
        
    @cached_property
    def animals_categories_numbers(self):
        if self.animcatowned is not None:
            return self.animcatowned.split(' ')
        return None
    
    @cached_property
    def animals_categories_owned(self):
        d = dict(constants.ANIMAL_CATEGORIES)
        category_numbers = self.animals_categories_numbers
        if category_numbers is not None:
            return [d[number] for number in category_numbers]
        return None
   
    @cached_property
    def house_hold_problem_numbers(self):
        if self.hhproblems is not None:
            return self.hhproblems.split(' ')
        return None
    
    @cached_property
    def house_hold_problems(self):
        d = dict(constants.HOUSE_HOLD_PROBLEMS)
        problem_number = self.house_hold_problem_numbers
        if problem_number is not None:
            return [d[number] for number in problem_number]
        return None

    @cached_property
    def gps_location(self):
        result = {}
        if self.gpsloc:
            values = self.gpsloc.split(' ')
            if len(values) == 4:
                result['longitude'] = float(values[0])
                result['latitude'] = float(values[1])
                result['altitude'] = float(values[2])
                result['accuracy'] = float(values[3])
            else:
                raise ValueError(
                    'The record {} has less than 4 values.'.format(self.gpsloc)
                )
        return result

    @cached_property
    def geojson(self):
        if self.gps_location:
            result = {
                'type': 'Point',
                'coordinates': [
                    self.gps_location['latitude'],
                    self.gps_location['longitude']
                ]
            }
            return json.dumps(result)
        return None

class Reg01Lkpmaindistrict(models.Model):
    maindistrict_cod = models.IntegerField(primary_key=True)
    maindistrict_des = models.CharField(max_length=120, blank=True, null=True)
   # hh_region_cod = models.ForeignKey('Reg01LkphhRegion', models.DO_NOTHING, db_column='hh_region_cod', blank=True, null=True)
    rowuuid = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reg01_lkpmaindistrict'

    def __str__(self):
        return self.maindistrict_des


class Reg04Maininfo(models.Model):
    surveyid = models.CharField(max_length=80, blank=True, null=True)
    originid = models.CharField(max_length=15, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    deviceid = models.CharField(max_length=60, blank=True, null=True)
   # enumtype = models.ForeignKey('Reg02Lkpenumtype', models.DO_NOTHING, db_column='enumtype', blank=True, null=True)
   # aitechid = models.ForeignKey('Reg01Maininfo', models.DO_NOTHING, db_column='aitechid', blank=True, null=True)
   # datacollid = models.ForeignKey('Reg01BMaininfo', models.DO_NOTHING, db_column='datacollid', blank=True, null=True)
    hh = models.ForeignKey('Reg02Maininfo', models.DO_NOTHING, primary_key=True, related_name='reg04maininfo')
    regdate = models.DateField()
    animregis = models.IntegerField(blank=True, null=True)
    gpsloc = models.CharField(max_length=60, blank=True, null=True)
    rowuuid = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reg04_maininfo'
        unique_together = (('hh', 'regdate'),)
