from import_export import resources
from .models import *

class HospitalResource(resources.ModelResource):
    class meta:
        model = hospital