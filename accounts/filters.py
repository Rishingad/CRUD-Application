import django_filters
from django_filters import DateFilter, CharFilter

from .models import *
# We have a number of fields and we want to let our users filter based on the name, the price or the release_date. We create a FilterSet for this:
class OrderFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	note = CharFilter(field_name='note', lookup_expr='icontains')
    
	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer','date_created']