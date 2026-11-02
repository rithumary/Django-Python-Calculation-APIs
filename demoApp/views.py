from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class FactorialView(View):
    def post(self,request):
        request_body=request.body
        form_body=loads(request_body)
        num=form_body.get('num')
        fact=1
        for i in range(1,num+1):
            fact*=i
        fact={
            "Factorial":fact
        }
        return JsonResponse(fact)

@method_decorator(csrf_exempt,name='dispatch')
class ArmstrongView(View):
    def post(self,request):
        request_body=request.body
        form_body=loads(request_body)
        num=form_body.get('num')
        temp=num
        sum=0
        length=len(str(num))
        while num>0:
            digits=num%10
            sum+=digits**length
            num=num//10
        if temp==sum:
            result={
                "Armstrong":True
            }
        else:
            result={
                "Armstrong":False
            }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class ProfitView(View):
    def post(self,request):
        request_body=request.body
        form_body=loads(request_body)
        cost_price=form_body.get('cost_price')
        selling_price=form_body.get('selling_price')
        quantity=form_body.get('quantity')
        total_cost=cost_price*quantity
        total_sales=selling_price*quantity
        profit=total_cost-total_sales
        result={
            "cost_price"   : cost_price,
            "selling_price": selling_price,
            "quantity"    :  quantity,
            "total_cost"   : total_cost,
            "total_sales"  : total_sales,
            "profit"       : profit
        }
        return JsonResponse(result) 
@method_decorator(csrf_exempt,name='dispatch')
class SalaryView(View):
    def post(self,request):
        request_body=request.body
        form_body=loads(request_body)
        hours_worked=form_body.get('hours_worked')
        regular_hours=form_body.get('regular_hours')
        hourly_rate=form_body.get('hourly_rate')
        overtime_rate=form_body.get('overtime_rate')
        regular_pay=regular_hours*hourly_rate
        overtime_hours=hours_worked-regular_hours
        overtime_pay=overtime_hours*overtime_rate
        total_salary=regular_pay+overtime_pay
        result={
            "hours_worked": hours_worked,
            "regular_hours": regular_hours,
            "hourly_rate": hourly_rate,
            "overtime_rate": overtime_rate,
            "regular_pay": regular_pay,
            "overtime_hours": overtime_hours,
            "overtime_pay": overtime_pay,
            "total_salary": total_salary
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class AgeView(View):
    def post(self,request):
        request_body=request.body
        form_body=loads(request_body)
        age=form_body.get('Age')
        months=age*12
        weeks=age*52
        days=age*365
        result={
            "Age":age,
            "Months":months,
            "Weeks":weeks,
            "Days":days
        }
        return JsonResponse(result)


