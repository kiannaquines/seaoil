from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.models import CustomUser,SaleModel,WarehouseProductModel
from django.contrib import messages
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth.hashers import make_password
from app.decorators import check_already_loggedin
from django.db.models import Sum,Count
from django.db.models.functions import TruncMonth,ExtractYear, ExtractMonth
from django.utils import timezone
from datetime import datetime

@login_required(login_url="auth/login/")
def get_monthly_product_in(request):
    monthly_totals = WarehouseProductModel.objects.annotate(month=TruncMonth('warehouse_product_date_added')).values('month').annotate(total=Count('warehouse_product_id')).order_by('month')
    totals_list = [
        {'month': datetime.strftime(total['month'], '%b'), 'total': total['total']}
        for total in monthly_totals
    ]
    return JsonResponse(totals_list, safe=False)

@login_required(login_url="auth/login/")
def get_monthly_yearly_sales(request):
	data = SaleModel.objects.annotate(
        year=ExtractYear('sale_date'),
        month=ExtractMonth('sale_date')
    ).values('year', 'month').annotate(
        total=Sum('sale_amount')
    ).order_by('year', 'month')

	result = {}
	for entry in data:
		year = str(entry['year'])
		month = entry['month']
		month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][month - 1]

		if year not in result:
			result[year] = []

		result[year].append({
			"month": month_name,
			"total": round(entry['total'], 2)
		})

	return JsonResponse(result)

@login_required(login_url="auth/login/")
def index(request):
	today_date = timezone.now().date()
	last_week = today_date - timezone.timedelta(days=7)
	total_sale = SaleModel.objects.aggregate(sale=Sum('sale_amount'))
	warehouse_product_count = WarehouseProductModel.objects.all().count()
	product_count_today = WarehouseProductModel.objects.filter(warehouse_product_date_added__date=today_date).all().count()
	latest_transactions = SaleModel.objects.all().order_by('-sale_date_added')[:7]
	last_weeks_data = WarehouseProductModel.objects.filter(warehouse_product_date_added__range=[last_week, today_date]).count()

	context = {
		'total_sale':total_sale,
		'total_products_count':warehouse_product_count,
		'todays_product_count':product_count_today,
		'warehouseproduct_count':warehouse_product_count,
		'latest_transactions':latest_transactions,
		'last_weeks_data_count':last_weeks_data,
	}

	return render(request,"index.html",context)

@check_already_loggedin
def auth_login(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		login_action = CustomUser.objects.filter(username=username)

		if login_action.exists():

			if login_action[0].is_active is not True:
				messages.error(request,"Your account is not activated yet, wait while we process your account activation.")
				return HttpResponseRedirect('/auth/login/')
			else:
				auth = authenticate(request,username=username,password=password)
			
			if auth is not None:
				login(request,auth)
				messages.success(request,"You have successfully logged in.")
				return HttpResponseRedirect('/')
			else:
				messages.error(request,"Incorrect username/password, please try again.")
				return render(request,"auth/login.html")
		else:
			messages.error(request,"We cannot find your account, please try again.")
			return render(request,"auth/login.html")
		
	return render(request,"auth/login.html")


def auth_logout(request):
	logout(request)
	return HttpResponseRedirect('/auth/login')

@check_already_loggedin
def auth_register(request):
	if request.method == "POST":
		username = request.POST.get("username")
		first_name = request.POST.get("firstname")
		last_name = request.POST.get("lastname")
		password = make_password(request.POST.get("password"))


		if CustomUser.objects.filter(username=username).exists():
			messages.error(request,"Sorry, username already exist, please try again.")
			return render(request,"auth/register.html")
		
		CustomUser.objects.create(username=username,first_name=first_name,last_name=last_name,password=password,is_active=False)
		messages.success(request,"You have successfully registered, please wait to activate your account.")
		return HttpResponseRedirect("/auth/login")

	return render(request,"auth/register.html")

@login_required(login_url="auth/login/")
def user_profile(request,pk):
	context = {}
	if request.method == "GET":
		user = CustomUser.objects.get(pk=pk)
		context["user"] = user
		return render(request,"auth/profile.html",context)
	
@login_required(login_url="auth/login/")
def user_update(request,pk):
	pass

