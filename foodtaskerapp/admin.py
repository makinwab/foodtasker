# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from foodtaskerapp.models import Restaurant, Customer, Driver

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)
