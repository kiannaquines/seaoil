from xhtml2pdf import pisa
from datetime import datetime
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from django.views.decorators.http import require_GET
from app.models import WarehouseProductModel
import os

@require_GET
def generate_inventory_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="seaoil-warehouse-inventory-report-{datetime.now()}.pdf"'
    context = {}
    context['date_generated'] = datetime.now()
    context['logo_path'] = os.path.join(settings.MEDIA_ROOT,'logo','seaoil-logo.svg')
    context['warehouse_product'] = WarehouseProductModel.objects.all().order_by('warehouse_product_date_added')

    template = get_template('inventory_template.html')

    rendered_html = template.render(context)
    createPDF = pisa.CreatePDF(rendered_html, dest=response)

    if createPDF.err:
        return HttpResponse('Error generating PDF: %s' % createPDF.err)
    
    return response
