from app.models import CustomUser, SaleModel, WarehouseProductModel, InvoiceRequestModel
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Sum, Count, F
from django.db.models.functions import TruncMonth, ExtractYear, ExtractMonth, Round
from django.utils import timezone
from datetime import datetime
from core.settings import MINIMUM
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from app.decorators import (
    check_already_loggedin,
    check_user_permission_based_on_user_type,
)

from app.forms import RequestInvoiceForm


@login_required(login_url="/auth/login/")
def get_monthly_product_in(request):
    monthly_totals = (
        WarehouseProductModel.objects.annotate(
            month=TruncMonth("warehouse_product_date_added")
        )
        .values("month")
        .annotate(total=Count("warehouse_product_id"))
        .order_by("month")
    )
    totals_list = [
        {"month": datetime.strftime(total["month"], "%b"), "total": total["total"]}
        for total in monthly_totals
    ]
    return JsonResponse(totals_list, safe=False)


@login_required(login_url="/auth/login/")
def get_monthly_yearly_sales(request):
    data = (
        SaleModel.objects.annotate(
            year=ExtractYear("sale_date"), 
            month=ExtractMonth("sale_date")
        )
        .values("year", "month")
        .annotate(
            total_paid=Sum(F("sale_product__product_price") * F('sale_quantity')),
            total=Round(F('total_paid') + (F('total_paid') / 1.12) * 0.12, 2)
        )
        .order_by("year", "month")
    )

    result = {}
    for entry in data:
        year = str(entry["year"])
        month = entry["month"]
        month_name = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ][month - 1]

        if year not in result:
            result[year] = []

        result[year].append({"month": month_name, "total": round(entry["total"], 2)})

    return JsonResponse(result)


@login_required(login_url="/auth/login/")
@check_user_permission_based_on_user_type
def index(request):
    today_date = timezone.now().date()
    last_week = today_date - timezone.timedelta(days=7)
    warehouse_product_count = WarehouseProductModel.objects.all().count()
    product_count_today = (
        WarehouseProductModel.objects.filter(
            warehouse_product_date_added__date=today_date
        )
        .all()
        .count()
    )
  
    latest_transactions = InvoiceRequestModel.objects.values('customer_name').annotate(
        total_paid=Sum(F('request_order__sale_quantity') * F('request_order__sale_product__product_price')),
        new_amount_with_tax=Round(F('total_paid') + (F('total_paid') / 1.12) * 0.12, 2),
    ).prefetch_related('request_order__sale_product__product_warehouse_product')[:7]
    
    last_weeks_data = WarehouseProductModel.objects.filter(
        warehouse_product_date_added__range=[last_week, today_date]
    ).count()

    warehouse_product_stock_check = WarehouseProductModel.objects.filter(
        warehouse_product_stock__lt=MINIMUM
    ).all()

    context = {
        "total_products_count": warehouse_product_count,
        "todays_product_count": product_count_today,
        "warehouseproduct_count": warehouse_product_count,
        "latest_transactions": latest_transactions,
        "last_weeks_data_count": last_weeks_data,
        "warehouse_product_stock_check": warehouse_product_stock_check,
    }

    return render(request, "index.html", context)


@check_already_loggedin
def auth_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        login_action = CustomUser.objects.filter(username=username)

        if login_action.exists():

            if login_action[0].is_active is not True:
                messages.error(
                    request,
                    "Your account is not activated yet, wait while we process your account activation.",
                    extra_tags="login_inactive",
                )
                return HttpResponseRedirect("/auth/login/")
            else:
                auth = authenticate(request, username=username, password=password)

            if auth is not None:
                login(request, auth)
                messages.success(
                    request,
                    "You have successfully logged in.",
                    extra_tags="login_success",
                )

                if login_action[0].user_type == CustomUser.USER_TYPE[0][0]:
                    return HttpResponseRedirect(reverse_lazy("main_page"))
                elif login_action[0].user_type == CustomUser.USER_TYPE[1][0]:
                    return HttpResponseRedirect(reverse_lazy("attendant_page"))
                elif login_action[0].user_type == CustomUser.USER_TYPE[2][0]:
                    return HttpResponseRedirect(reverse_lazy("manager_page"))
            else:
                messages.error(
                    request,
                    "Incorrect username/password, please try again.",
                    extra_tags="login_invalid",
                )
                return render(request, "auth/login.html")
        else:
            messages.error(
                request,
                "We cannot find your account, please try again.",
                extra_tags="login_error",
            )
            return render(request, "auth/login.html")

    return render(request, "auth/login.html")


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect("/auth/login")


@check_already_loggedin
def auth_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        password = make_password(request.POST.get("password"))

        if CustomUser.objects.filter(username=username).exists():
            messages.error(
                request,
                "Sorry, username already exist, please try again.",
                extra_tags="auth_invalid",
            )
            return render(request, "auth/register.html")

        CustomUser.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_active=False,
        )
        messages.success(
            request,
            "You have successfully registered, please wait to activate your account.",
            extra_tags="auth_success",
        )
        return HttpResponseRedirect("/auth/login")

    return render(request, "auth/register.html")


@login_required(login_url="/auth/login/")
def user_profile(request, pk):
    context = {}
    if request.method == "GET":
        user = CustomUser.objects.get(pk=pk)
        context["user"] = user
        return render(request, "auth/profile.html", context)


@login_required(login_url="/auth/login/")
def user_update(request, pk):
    pass


# DONE
@login_required(login_url="/auth/login/")
def request_list(request):
	context = {}
	context["request_list"] = InvoiceRequestModel.objects.all()
	context["warehouse_product_stock_check"] = WarehouseProductModel.objects.filter(warehouse_product_stock__lt=MINIMUM).all()
	return render(request, "request.html", context)

# DONE
@login_required(login_url="/auth/login/")
def approve_request(request):
    if request.method == "POST":
        request_id = request.POST.get("request_id")

        request_approve = InvoiceRequestModel.objects.filter(request_id=request_id)
        request_approve.update(request_status=True)
        messages.success(request, "Yahooo, you approved the invoice download request successfully.")
        return HttpResponseRedirect(reverse_lazy("request_list"))
    else:
        return HttpResponseRedirect(reverse_lazy("request_list"))

# DONE    
@login_required(login_url="/auth/login/")
def attendant_request_list(request):
    context = {
        'form': RequestInvoiceForm(),
        'request_list' : InvoiceRequestModel.objects.filter(request_by=request.user).all(),
        'type': 'all'
    }

    if request.method == "POST":
        form = RequestInvoiceForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            request_obj = InvoiceRequestModel(
                customer_name = data['customer_name'],
                request_by=request.user,
            )
            request_obj.save()
            request_obj.request_order.set(data['request_order'])

            for sale in data['request_order']:
                sale.status = True
                sale.save()

                print(sale)
            
            messages.success(request, "Yahooo, you requested for an invoice download successfully.",extra_tags="add_success")
        else:
            messages.error(request, "Oops, something went wrong. Please try again.",extra_tags="some_error")

        return HttpResponseRedirect(reverse_lazy('attendant_request_list'))

    return render(request, "attendant/request_list.html", context)