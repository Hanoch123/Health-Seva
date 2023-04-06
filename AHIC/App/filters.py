import django_filters
from django_filters import *

from App.models import *
from Insurance.models import *
from hospital.models import *

class BankFilter(django_filters.FilterSet):
    no_plans = CharFilter(field_name ='no_plans', lookup_expr = 'icontains')
    class Meta:
        model = BankInsurance
        fields = ['no_plans','coverage','plan_type','insurance_for','tenure']

class StatusFilter(django_filters.FilterSet):
    class Meta:
        model = UserDetails
        fields = ['status','policy_no']

class ClaStatusFilter(django_filters.FilterSet):
    class Meta:
        model = Billing
        fields = ['status']

class HospStatusFilter(django_filters.FilterSet):
    class Meta:
        model = Billing
        fields = ['hosp_status']