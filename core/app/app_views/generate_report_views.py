import os
from xhtml2pdf import pisa
from datetime import datetime
from django.http import HttpResponse
from django.conf import settings
from app.models import WarehouseProductModel,SaleModel,InvoiceRequestModel
from django.utils import timezone
from django.db.models import F,Sum
from app.models import CustomUser
from django.views.decorators.http import require_GET
from django.template.loader import get_template
from app.utils import receipt_number_generator
from django.contrib.auth.decorators import login_required

@require_GET
@login_required(login_url="/auth/login/")
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
@login_required(login_url="/auth/login/")
def generate_sales_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="seaoil-sales-report-{datetime.now()}.pdf"'
    
    request_invoice = InvoiceRequestModel.objects.values(
        'customer_name',
        'request_order__sale_date',
        'request_order__sale_product__product_warehouse_product__warehouse_product_name',
        'request_order__sale_product__product_price',
        'request_order__sale_quantity',
        'request_order__encoded_by__username',
    ).annotate(
        customer=F('customer_name'),
        sale_date=F('request_order__sale_date'),
        product=F('request_order__sale_product__product_warehouse_product__warehouse_product_name'),
        price=F('request_order__sale_product__product_price'),
        sale_quantity=F('request_order__sale_quantity'),
        encoder=F('request_order__encoded_by__username'),
    ).values(
        'customer', 
        'sale_date', 
        'product', 
        'price', 
        'sale_quantity', 
        'encoder'
    )

    context = {}
    context['date_generated'] = datetime.now()
    context['logo_path'] = os.path.join(settings.MEDIA_ROOT,'logo','seaoil-logo.svg')
    context['sales'] = request_invoice
    
    template = get_template('sale_template.html')

    rendered_html = template.render(context)
    createPDF = pisa.CreatePDF(rendered_html, dest=response)

    if createPDF.err:
        return HttpResponse('Error generating PDF: %s' % createPDF.err)
    
    return response

@require_GET
@login_required(login_url="/auth/login/")
def generate_sales_invoice(request,customer,encoder,request_id):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=sale-invoice-{customer}.pdf'
    today = timezone.now().date()

    request_invoice = InvoiceRequestModel.objects.filter(
        request_id=request_id,
        request_by=request.user,
    ).prefetch_related('request_order__sale_product__product_warehouse_product')

    sum_total_amount = 0
    total_prices_per_order = []
    for sale in request_invoice:
        for order in sale.request_order.all():
            order_total_price = order.sale_quantity * order.sale_product.product_price
            sum_total_amount += order_total_price
            total_prices_per_order.append({
                'order': order,
                'total_price': order_total_price,
            })

    encoder_queryset = CustomUser.objects.get(username=encoder)
    tax_calculated = f'{(sum_total_amount / 1.12) * 0.12:.2f}'
    context = {
        'invoice': request_invoice,
        'total_prices_per_order': total_prices_per_order,
        'customer_name': customer,
        'date_generated': today,
        'tax_calculated': tax_calculated,
        'receipt_number': f'#{receipt_number_generator()}',
        'encoder': f'{encoder_queryset.username.capitalize()}' if encoder_queryset else 'N/A',
        'subtotal': sum_total_amount,
        'total_sum': f'{sum_total_amount + float(tax_calculated):.2f}',
        'logo_path': os.path.join(settings.MEDIA_ROOT, 'logo', 'seaoil-logo.svg'),
        'peso_path': os.path.join(settings.MEDIA_ROOT, 'logo', 'peso.svg'),
    }

    template = get_template('sale_invoice_template.html')
    template_rendered = template.render(context)
    createPDF = pisa.CreatePDF(template_rendered, dest=response)

    if createPDF.err:
        return HttpResponse('Error generating PDF: %s' % createPDF.err)

    return response

@require_GET
@login_required(login_url="/auth/login/")
def generate_sales_invoice_admin(request,customer,encoder,request_id):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=sale-invoice-{customer}.pdf'
    today = timezone.now().date()
    
    user_obj = CustomUser.objects.get(username=encoder)

    request_invoice = InvoiceRequestModel.objects.filter(
        request_id=request_id,
        request_by=user_obj,
    ).prefetch_related('request_order__sale_product__product_warehouse_product')
    
    sum_total_amount = 0
    total_prices_per_order = []
    for sale in request_invoice:
        for order in sale.request_order.all():
            order_total_price = order.sale_quantity * order.sale_product.product_price
            sum_total_amount += order_total_price
            total_prices_per_order.append({
                'order': order,
                'total_price': order_total_price,
            })

    encoder_queryset = CustomUser.objects.get(username=encoder)
    tax_calculated = f'{(sum_total_amount / 1.12) * 0.12:.2f}'
    context = {
        'invoice': request_invoice,
        'total_prices_per_order': total_prices_per_order,
        'customer_name': customer,
        'date_generated': today,
        'tax_calculated': tax_calculated,
        'receipt_number': f'#{receipt_number_generator()}',
        'encoder': f'{encoder_queryset.username.capitalize()}' if encoder_queryset else 'N/A',
        'subtotal': sum_total_amount,
        'total_sum': f'{sum_total_amount + float(tax_calculated):.2f}',
        'logo_path': os.path.join(settings.MEDIA_ROOT, 'logo', 'seaoil-logo.svg'),
        'peso_path': os.path.join(settings.MEDIA_ROOT, 'logo', 'peso.svg'),
    }

    template = get_template('sale_invoice_template.html')
    template_rendered = template.render(context)
    createPDF = pisa.CreatePDF(template_rendered, dest=response)

    if createPDF.err:
        return HttpResponse('Error generating PDF: %s' % createPDF.err)

    return response

