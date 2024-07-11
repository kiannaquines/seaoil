from xhtml2pdf import pisa
from datetime import datetime
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from django.views.decorators.http import require_GET
from app.models import WarehouseProductModel,SaleModel
import os
from django.utils import timezone
from django.db.models import F,Sum
from app.models import CustomUser
import random

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

@require_GET
def generate_sales_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="seaoil-sales-report-{datetime.now()}.pdf"'
    context = {}
    context['date_generated'] = datetime.now()
    context['logo_path'] = os.path.join(settings.MEDIA_ROOT,'logo','seaoil-logo.svg')
    context['sales'] = SaleModel.objects.all().order_by('sale_date_added')

    template = get_template('sale_template.html')

    rendered_html = template.render(context)
    createPDF = pisa.CreatePDF(rendered_html, dest=response)

    if createPDF.err:
        return HttpResponse('Error generating PDF: %s' % createPDF.err)
    
    return response

def generate_sales_invoice(request,name,encoder):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=sale-invoice-{name}.pdf'
    today = timezone.now().date()

    query_invoice = SaleModel.objects.filter(
        sale_date_added__date=today,
        sale_customername=name,
        encoded_by=request.user
    ).annotate(
        per_order_total_price=F('sale_quantity') * F('sale_amount')
    ).all()

    sum_total_amounts = query_invoice.aggregate(
        sum_total_amount=Sum('per_order_total_price')
    )
    encoder_queryset = CustomUser.objects.get(username=encoder)
    tax_calculated = f'{(sum_total_amounts['sum_total_amount'] / 1.12) * 0.12:.2f}'

    context = {
        'invoice': query_invoice,
        'customer_name': name,
        'date_generated': today,
        'tax_calculated': tax_calculated,
        'receipt_number': f'#{random.randint(100, 200)}{timezone.now().strftime("%Y%m%d")}',
        'encoder': f'{encoder_queryset.username.capitalize()}' if encoder_queryset else 'N/A',
        'total_sum':sum_total_amounts['sum_total_amount'],
        'logo_path': os.path.join(settings.MEDIA_ROOT,'logo','seaoil-logo.svg'),
        'peso_path': os.path.join(settings.MEDIA_ROOT,'logo','peso.svg')
    }

    template = get_template('sale_invoice_template.html')
    template_rendered = template.render(context)
    createPDF = pisa.CreatePDF(template_rendered, dest=response)

    if createPDF.err:
        return HttpResponse('Error generating PDF: %s' % createPDF.err)

    return response

