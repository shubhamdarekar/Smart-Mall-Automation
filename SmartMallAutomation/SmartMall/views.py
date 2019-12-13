from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

#from django.db import connection
#from .models import EvaluationApp
from django.template import loader
#from django.template import context
#import mysql.connector
from SmartMall.forms import LoginForm
from .models import Product,Fridge,Buyer,Seller,SellerStock,Order,Fridgetemp,Fridgehumidity,User1
# from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.db import connection
import numpy as np
import mysql.connector
from django.contrib.staticfiles.templatetags.staticfiles import static
import urllib.request
import matplotlib.pyplot as plt

def index(request):

		return render(request,"SmartMall/Lap.html")
# Create your views here.

def Login(request):
	return render(request,"SmartMall/Login.html")

def openadmin(request):
	return render(request,"SmartMall/Admin.html")

def openFridge(request):
	return render(request,"SmartMall/Fridge.html")

def openbuyer(request):
	return render(request,"SmartMall/Buyer.html")

def openOrder(request):
	return render(request,"SmartMall/Order.html")

def openseller(request):
	return render(request,"SmartMall/Seller.html")

def openStock(request):
	return render(request,"SmartMall/Stock.html")


def verifyLogin(request):
	try:
		if request.method == 'POST':
			email = request.POST['email']
			pwd = request.POST['password']
			
			user = User1.objects.get(email = email)
			
			if pwd == user.password :
				request.session['logged_in'] = user.id
				if user.role == 'ADM':
					return redirect('/adminDashboard/')
				elif user.role == 'BUY':
					return redirect('/buyerDashboard/')
				elif user.role == 'SEL':
					return redirect('/sellerDashboard/')
				else:
				    return HttpResponse("Error!!")

			# user = authenticate(username=email, password=pwd)
			# if user is not None:
			# 	if user.is_superuser == 2:
			# 		return redirect('/adminDashboard/')
			# 	elif user.is_superuser == 3:
			# 		return redirect('/buyerDashboard/')
			# 	elif user.is_superuser == 4:
			# 		return redirect('/sellerDashboard/')	

			else:
				return HttpResponse("error")
				
	except:
		return HttpResponse("Error!! Invalid Details")

def Signup(request):

	return render(request,"SmartMall/Signup.html")


def signup(request):
	if request.method == 'POST':
		name = request.POST['name']
		phone = request.POST['phone']
		email = request.POST['email']
		flat = request.POST['flat']
		city = request.POST['city']
		pincode = request.POST['pincode']
		# role = request.POST['role']
		pwd = request.POST['password']
		

		newuser = User1()
		newuser.Name = name
		newuser.Phone = phone
		newuser.email = email
		newuser.Flat = flat
		newuser.City = city
		newuser.Pincode = pincode
		newuser.role = 'BUY'
		newuser.password = pwd
		newuser.save()
		return render(request,'SmartMall/Login.html')

def addsel(request):
	if request.method == 'POST':
		name = request.POST['name']
		phone = request.POST['phone']
		email = request.POST['email']
		flat = request.POST['flat']
		city = request.POST['city']
		pincode = request.POST['pincode']
		# role = request.POST['role']
		pwd = request.POST['password']
		

		newuser = User1()
		newuser.Name = name
		newuser.Phone = phone
		newuser.email = email
		newuser.Flat = flat
		newuser.City = city
		newuser.Pincode = pincode
		newuser.role = 'SEL'
		newuser.password = pwd
		newuser.save()
		return render(request,'SmartMall/Admin.html')

def ordAPP(request):
	if request.method == 'POST':
		qunt = request.POST['quantity']
		User_id = request.session['logged_in']
		

		neworder = Order()
		neworder.OrderQuantity = qunt
		neworder.BuyerID_id = User_id
		neworder.ProductID_id = 1
		neworder.OrderPrice = int(qunt)*60
		neworder.save()
		return render(request,'SmartMall/Buyer.html')

def ordORG(request):
	if request.method == 'POST':
		qunt = request.POST['quantity']
		User_id = request.session['logged_in']
		

		neworder = Order()
		neworder.OrderQuantity = qunt
		neworder.BuyerID_id = User_id
		neworder.ProductID_id = 2
		neworder.OrderPrice = int(qunt)*40
		
		neworder.save()
		return render(request,'SmartMall/Buyer.html')

def ordBAN(request):
	if request.method == 'POST':
		qunt = request.POST['quantity']
		User_id = request.session['logged_in']
		

		neworder = Order()
		neworder.OrderQuantity = qunt
		neworder.BuyerID_id = User_id
		neworder.ProductID_id = 3
		neworder.OrderPrice = int(qunt)*30
		
		neworder.save()
		return render(request,'SmartMall/Buyer.html')

def ordPEA(request):
	if request.method == 'POST':
		qunt = request.POST['quantity']
		User_id = request.session['logged_in']
		

		neworder = Order()
		neworder.OrderQuantity = qunt
		neworder.BuyerID_id = User_id
		neworder.ProductID_id = 4
		neworder.OrderPrice = int(qunt)*400*0.7
		
		neworder.save()
		return render(request,'SmartMall/Buyer.html')

def ordPIN(request):
	if request.method == 'POST':
		qunt = request.POST['quantity']
		User_id = request.session['logged_in']
		

		neworder = Order()
		neworder.OrderQuantity = qunt
		neworder.BuyerID_id = User_id
		neworder.ProductID_id = 5
		neworder.OrderPrice = int(qunt)*50
		
		neworder.save()
		return render(request,'SmartMall/Buyer.html')

def ordCHE(request):
	if request.method == 'POST':
		qunt = request.POST['quantity']
		User_id = request.session['logged_in']
		

		neworder = Order()
		neworder.OrderQuantity = qunt
		neworder.BuyerID_id = User_id
		neworder.ProductID_id = 6
		neworder.OrderPrice = int(qunt)*90
		
		neworder.save()
		return redirect('/buyerDashboard/')	

def logout(request):
	try:
		del request.session['logged_in']
	except KeyError:
		pass
	return render(request,"SmartMall/Lap.html")			

def adminDash(request):
	

	with connection.cursor() as cursor:
		cursor.execute("SELECT id,OrderQuantity,OrderPrice,BuyerID_id,ProductID_id,SellerID_id,SellerStockID_id from SmartMall_order")
		res=cursor.fetchall()
		# return HttpResponse(res)
		a=0
		data=dict()
		for r in res:
			data[a]={
			"id": r[0],
			"OrderQuantity": r[1],
			"OrderPrice": r[2],
			"BuyerID_id": r[3],
			"ProductID_id": r[4],
			"SellerID_id": r[5],
			"SellerStockID_id":r[6]
			}
			a+=1

	
	
				
			
	# if(request.user.is_authenticated):
		return render(request,"SmartMall/Admin.html",{"data":data})
	# else:
	# 	return HttpResponse("Error")

def buyerDash(request):

	User_id = request.session['logged_in']
	with connection.cursor() as cursor:
		cursor.execute("SELECT FridgeHumidity, FridgeTemperature from SmartMall_fridgehumidity, SmartMall_fridgetemp")
		res=cursor.fetchall()
		# return HttpResponse(res)
		x=0
		data=dict()
		for r in res:
			data[x]={
			# "id": r[0],
			# "Fridge Number": r[1],
			"Fridge Humidity": r[0],
			"Fridge Temperature": r[1],
			
			}
			x+=1

	with connection.cursor() as cursor6:
		cursor6.execute("SELECT id, ProductPrice, ProductName  from SmartMall_product")
		res6=cursor6.fetchall()
		# return HttpResponse(res)
		m=0
		data6=dict()
		for r in res6:
			data6[m]={
			"id": r[0],
			
			"ProductPrice": r[2],
			"ProductName": r[1],
			
			}
			m+=1
	with connection.cursor() as cursor4:
		cursor4.execute("SELECT  A.id,A.ProductPrice, A.ProductName  from SmartMall_product as A inner join (Select min(ProductPrice) as min from SmartMall_product) as B on A.ProductPrice=B.min")
		res4=cursor4.fetchall()
		# return HttpResponse(res)
		p=0
		data4=dict()
		for r in res4:
			data4[p]={
			"id": r[0],
			
			"Price": r[2],
			"Name": r[1],
			
			}
			p+=1
	with connection.cursor() as cursor7:
		cursor7.execute("SELECT  A.id,A.ProductPrice, A.ProductName  from SmartMall_product as A inner join (Select max(ProductPrice) as max from SmartMall_product) as B on A.ProductPrice=B.max")
		res7=cursor7.fetchall()
		# return HttpResponse(res)
		p=0
		data7=dict()
		for r in res7:
			data7[p]={
			"id": r[0],
			
			"Price": r[2],
			"Name": r[1],
			
			}
			p+=1		

	with connection.cursor() as cursor2:
		cursor2.execute("SELECT id,Name,Phone,email,Flat,City,Pincode from SmartMall_user1 Where id=%s"%(User_id))
		res2=cursor2.fetchall()
		# return HttpResponse(res)
		z=0
		data2=dict()
		for r in res2:
			data2[z]={
			"id": r[0],
			"Name": r[1],
			"Phone": r[2],
			"email": r[3],
			"Flat": r[4],
			"City": r[5],
			"Pincode":r[6]
			}
			z+=1

	with connection.cursor() as cursor3:
		cursor3.execute("SELECT SmartMall_fridge.id,SmartMall_fridge.FridgeQuantity,SmartMall_fridge.RequiredLimit,SmartMall_product.ProductName from SmartMall_fridge inner join SmartMall_product on SmartMall_fridge.ProductID_id=SmartMall_product.id Where BuyerID_id=(Select id from SmartMall_buyer where UserID_id=%s)"%(User_id))
		res3=cursor3.fetchall()
		# return HttpResponse(res)
		w=0
		data3=dict()
		for r in res3:
			data3[w]={
			"id": r[0],
			"Fridge Quantity": r[1],
			"Required Limit": r[2],
			"Product Id": r[3],
			# "Buyer Id": r[4],
			}
			w+=1	

	with connection.cursor() as cursor1:
		cursor1.execute("SELECT id,BuyerCash from SmartMall_buyer Where UserID_id=%s"%(User_id))
		res1=cursor1.fetchall()
		# return HttpResponse(res)
		y=0
		data1=dict()
		for r in res1:
			data1[y]={
			"Buyer id": r[0],
			"Buyer Cash": r[1],
			
			}
			y+=1

	with connection.cursor() as cursor5:
		cursor5.execute("SELECT SmartMall_order.id,SmartMall_order.OrderQuantity,SmartMall_order.OrderPrice,SmartMall_order.BuyerID_id,SmartMall_product.ProductName,SmartMall_order.SellerID_id,SmartMall_order.SellerStockID_id from SmartMall_order inner join SmartMall_product on SmartMall_order.ProductID_id=SmartMall_product.id Where SmartMall_order.BuyerID_id=(SELECT id from SmartMall_buyer Where UserID_id=%s)"%(User_id))
		res5=cursor5.fetchall()
		# return HttpResponse(res)
		a=0
		data5=dict()
		for r in res5:
			data5[a]={
			"id": r[0],
			"OrderQuantity": r[1],
			"OrderPrice": r[2],
			"BuyerID_id": r[3],
			"ProductID_id": r[4],
			"SellerID_id": r[5],
			"SellerStockID_id":r[6]

			# "SmartMall_product.ProductName":r[7]
			}
			a+=1
	


			
	User_id = request.session['logged_in']		
	with connection.cursor() as cursor8:
		cursor8.execute("SELECT SmartMall_order.OrderQuantity,SmartMall_order.OrderPrice,SmartMall_product.ProductName from SmartMall_order inner join SmartMall_product on SmartMall_order.ProductID_id=SmartMall_product.id  inner join (Select min(OrderPrice) as minimum from SmartMall_order) as B on SmartMall_order.OrderPrice=B.minimum Where SmartMall_order.BuyerID_id=(SELECT id from SmartMall_buyer Where UserID_id=%s)"%(User_id))
		res8=cursor8.fetchall()
		# return HttpResponse(res)
		q=0
		data8=dict()
		for r in res8:
			data8[q]={
			
			"OrderQuantity": r[0],
			"OrderPrice": r[1],
			
			"ProductID_id": r[2],
			

			
			}
			q+=1
	with connection.cursor() as cursor9:
		cursor9.execute("SELECT SmartMall_order.OrderQuantity,SmartMall_order.OrderPrice,SmartMall_product.ProductName from SmartMall_order inner join SmartMall_product on SmartMall_order.ProductID_id=SmartMall_product.id  inner join (Select max(OrderPrice) as maximum from SmartMall_order) as B on SmartMall_order.OrderPrice=B.maximum Where SmartMall_order.BuyerID_id=(SELECT id from SmartMall_buyer Where UserID_id=%s)"%(User_id))
		res9=cursor9.fetchall()
		# return HttpResponse(res)
		l=0
		data9=dict()
		for r in res9:
			data9[l]={
			
			"OrderQuantity": r[0],
			"OrderPrice": r[1],
			
			"ProductID_id": r[2],
			

			
			}
			l+=1		
	
	with connection.cursor() as cursor10:
		cursor10.execute("SELECT SmartMall_order.OrderQuantity,SmartMall_order.OrderPrice,SmartMall_product.ProductName from SmartMall_order inner join SmartMall_product on SmartMall_order.ProductID_id=SmartMall_product.id  inner join (Select min(OrderPrice) as min from SmartMall_order) as B on SmartMall_order.OrderPrice=B.min ")
		res10=cursor10.fetchall()
		# return HttpResponse(res)
		a=0
		data10=dict()
		for r in res10:
			data10[a]={
			
			"OrderQuantity": r[0],
			"OrderPrice": r[1],
			
			"ProductID_id": r[2],
			

			# "SmartMall_product.ProductName":r[7]
			}
			a+=1

	with connection.cursor() as cursor11:
		cursor11.execute("SELECT SmartMall_order.OrderQuantity,SmartMall_order.OrderPrice,SmartMall_product.ProductName from SmartMall_order inner join SmartMall_product on SmartMall_order.ProductID_id=SmartMall_product.id  inner join (Select max(OrderPrice) as min from SmartMall_order) as B on SmartMall_order.OrderPrice=B.min ")
		res11=cursor11.fetchall()
		# return HttpResponse(res)
		a=0
		data11=dict()
		for r in res11:
			data11[a]={
			
			"OrderQuantity": r[0],
			"OrderPrice": r[1],
			
			"ProductID_id": r[2],
			

			# "SmartMall_product.ProductName":r[7]
			}
			a+=1

	with connection.cursor() as cursor12:
		cursor12.execute("SELECT MAX(pp),ww FROM (SELECT sum(SmartMall_order.OrderQuantity) as pp, SmartMall_product.ProductName as ww FROM SmartMall_order inner join SmartMall_product on SmartMall_order.ProductID_id=SmartMall_product.id GROUP BY SmartMall_product.ProductName) AS A ")
		res12=cursor12.fetchall()
		# return HttpResponse(res)
		a=0
		data12=dict()
		for r in res12:
			data12[a]={
			
			"OrderQuantity": r[0],
			
			
			"ProductID_id": r[1],
			

			# "SmartMall_product.ProductName":r[7]
			}
			a+=1

	with connection.cursor() as cursor13:
		cursor13.execute("SELECT pp,ww FROM (SELECT sum(SmartMall_order.OrderQuantity) as pp, SmartMall_product.ProductName as ww FROM SmartMall_order inner join SmartMall_product on SmartMall_order.ProductID_id=SmartMall_product.id GROUP BY SmartMall_product.ProductName) AS A ")
		res13=cursor13.fetchall()
		# return HttpResponse(res)
		a=0
		data13=dict()
		for r in res13:
			data13[a]={
			
			"OrderQuantity": r[0],
			
			
			"ProductID_id": r[1],
			

			# "SmartMall_product.ProductName":r[7]
			}
			a+=1								
	return render(request,"SmartMall/Buyer.html",{"data":data,"data1":data1,"data2":data2,"data3":data3,"data4":data4,"data5":data5,"data6":data6,"data7":data7,"data8":data8,"data9":data9,"data10":data10,"data11":data11,"data12":data12,"data13":data13})
	

	# else:
	# 	return HttpResponse("Error")
	

def sellerDash(request):
	# if(request.user.is_authenticated):

	User_id = request.session['logged_in']
	print(User_id)
	with connection.cursor() as cursor:
		cursor.execute("SELECT SmartMall_order.id,SmartMall_order.OrderQuantity,SmartMall_order.OrderPrice,SmartMall_order.BuyerID_id,SmartMall_product.ProductName,SmartMall_order.SellerID_id,SmartMall_order.SellerStockID_id from SmartMall_order inner join SmartMall_product on SmartMall_order.ProductID_id=SmartMall_product.id Where SellerID_id=(SELECT id from SmartMall_seller Where UserID_id=%s)"%(User_id))
		res=cursor.fetchall()
		# return HttpResponse(res)
		x=0
		data=dict()
		for r in res:
			data[x]={
			"id": r[0],
			"OrderQuantity": r[1],
			"OrderPrice": r[2],
			"BuyerID_id": r[3],
			"Product Name": r[4],
			"SellerID_id": r[5],
			"SellerStockID_id":r[6]
			}
			x+=1

		# return HttpResponse(data.items())
	#return HttpResponse(model_to_dict(data))
	with connection.cursor() as cursor2:
		cursor2.execute("SELECT id,Name,Phone,email,Flat,City,Pincode from SmartMall_user1 Where id=%s"%(User_id))
		res2=cursor2.fetchall()
		# return HttpResponse(res)
		z=0
		data2=dict()
		for r in res2:
			data2[z]={
			"id": r[0],
			"Name": r[1],
			"Phone": r[2],
			"email": r[3],
			"Flat": r[4],
			"City": r[5],
			"Pincode":r[6]
			}
			z+=1


	with connection.cursor() as cursor6:
		cursor6.execute("SELECT id, ProductPrice, ProductName  from SmartMall_product")
		res6=cursor6.fetchall()
		# return HttpResponse(res)
		m=0
		data6=dict()
		for r in res6:
			data6[m]={
			"id": r[0],
			
			"ProductPrice": r[2],
			"ProductName": r[1],
			
			}
			m+=1		
	
	with connection.cursor() as cursor1:
		cursor1.execute("SELECT id,SellerCash from SmartMall_seller Where UserID_id=%s"%(User_id))
		res1=cursor1.fetchall()
		# return HttpResponse(res)
		y=0
		data1=dict()
		for r in res1:
			data1[y]={
			"Seller id": r[0],
			"Seller Cash": r[1],
			
			}
			y+=1

	with connection.cursor() as cursor3:
		cursor3.execute("SELECT SmartMall_sellerstock.id,SmartMall_sellerstock.StockQuantity,SmartMall_product.ProductName,SmartMall_sellerstock.SellerID_id from  SmartMall_sellerstock inner join SmartMall_product on SmartMall_sellerstock.ProductID_id=SmartMall_product.id Where SellerID_id=(SELECT id from SmartMall_seller Where UserID_id=%s)"%(User_id))
		res3=cursor3.fetchall()
		# return HttpResponse(res)
		w=0
		data3=dict()
		for r in res3:
			data3[w]={
			"Seller id": r[0],
			"Seller Cash": r[1],
			"Phone": r[2],
			"email": r[3],
			
			}
			w+=1

	with connection.cursor() as cursor10:
		cursor10.execute("SELECT SmartMall_order.OrderQuantity,SmartMall_order.OrderPrice,SmartMall_product.ProductName from SmartMall_order inner join SmartMall_product on SmartMall_order.ProductID_id=SmartMall_product.id  inner join (Select min(OrderPrice) as min from SmartMall_order) as B on SmartMall_order.OrderPrice=B.min ")
		res10=cursor10.fetchall()
		# return HttpResponse(res)
		a=0
		data10=dict()
		for r in res10:
			data10[a]={
			
			"OrderQuantity": r[0],
			"OrderPrice": r[1],
			
			"ProductID_id": r[2],
			

			# "SmartMall_product.ProductName":r[7]
			}
			a+=1

	with connection.cursor() as cursor11:
		cursor11.execute("SELECT SmartMall_order.OrderQuantity,SmartMall_order.OrderPrice,SmartMall_product.ProductName from SmartMall_order inner join SmartMall_product on SmartMall_order.ProductID_id=SmartMall_product.id  inner join (Select max(OrderPrice) as min from SmartMall_order) as B on SmartMall_order.OrderPrice=B.min ")
		res11=cursor11.fetchall()
		# return HttpResponse(res)
		a=0
		data11=dict()
		for r in res11:
			data11[a]={
			
			"OrderQuantity": r[0],
			"OrderPrice": r[1],
			
			"ProductID_id": r[2],
			

			# "SmartMall_product.ProductName":r[7]
			}
			a+=1

	with connection.cursor() as cursor7:
		cursor7.execute("SELECT SmartMall_order.OrderQuantity,SmartMall_order.OrderPrice,SmartMall_product.ProductName from SmartMall_order inner join SmartMall_product on SmartMall_order.ProductID_id=SmartMall_product.id  inner join (Select max(OrderPrice) as min from SmartMall_order) as B on SmartMall_order.OrderPrice=B.min Where SmartMall_order.SellerID_id=(SELECT id from SmartMall_seller Where UserID_id=%s)"%(User_id))
		res7=cursor7.fetchall()
		# return HttpResponse(res)
		a=0
		data7=dict()
		for r in res7:
			data7[a]={
			
			"OrderQuantity": r[0],
			"OrderPrice": r[1],
			
			"ProductID_id": r[2],
			

			# "SmartMall_product.ProductName":r[7]
			}
			a+=1				
	return render(request,"SmartMall/seller.html",{"data":data,"data1":data1,"data2":data2,"data3":data3,"data6":data6,"data10":data10,"data11":data11,"data7":data7})
	# else:
	# 	return HttpResponse("Error")







def addbuyer(request):

	return render(request,"SmartMall/AdminAddBuyer.html")

def addseller(request):
	return render(request,"SmartMall/AdminAddSeller.html")

def addproduct(request):
	return render(request,"SmartMall/AdminAddProduct.html")

def weeklyreport(request):
	return render(request,"SmartMall/AdminWeeklyReport.html")

def buyerwisereport(request):
	return render(request,"SmartMall/AdminBuyerwiseReport.html")

def sellerwisereport(request):
	return render(request,"SmartMall/AdminSellerwiseReport.html")	






def buyerprofile(request):
	return render(request,"SmartMall/BuyerProfile.html")

def buyercashdetails(request):
	return render(request,"SmartMall/BuyerCashDetails.html")

def buyerfridgestatus(request):
	return render(request,"SmartMall/BuyerFridgeStatus.html")

def buyerreport(request):
	return render(request,"SmartMall/BuyerReport.html")





def sellerprofile(request):
	return render(request,"SmartMall/SellerProfile.html")

def sellercashdetails(request):
	return render(request,"SmartMall/SellerCashDetails.html")	

def sellerreport(request):
	return render(request,"SmartMall/SellerReport.html")	







def fridgestocks(request):
	return render(request,"SmartMall/FridgeStocks.html")

def fridgeaddproducts(request):
	return render(request,"SmartMall/FridgeAddProducts.html")	

def fridgeeditproducts(request):
	return render(request,"SmartMall/FridgeEditProducts.html")	







def placeorder(request):
	return render(request,"SmartMall/OrderPlaceOrder.html")

def ordercashdetails(request):
	return render(request,"SmartMall/OrderCashDetails.html")

def buyerorderhistory(request):
	return render(request,"SmartMall/OrderHistory.html")

def suggestions(request):
	return render(request,"SmartMall/OrderSuggestions.html")	






def sellerstock(request):
	return render(request,"SmartMall/StockSellerStock.html")

def sellerorderhistory(request):
	return render(request,"SmartMall/StockSellerOrderHistory.html")	

def sellercashdetail(request):
	return render(request,"SmartMall/StockSellerCashDetails.html")	


def addP(request):
	if request.method == 'POST':
		
		ProductPrice = request.POST['ProductPrice']
		ProductName = request.POST['ProductName']
		table = Product()
		table.ProductPrice = ProductPrice
		table.ProductName = ProductName
		table.save()
	return redirect('/adminDashboard/')

def selectsel(request):
	if request.method == 'POST':
		SelID = request.POST['selid']
		
		
	with connection.cursor() as cursor1:
		cursor1.execute("SELECT SmartMall_order.id,SmartMall_order.OrderQuantity,SmartMall_order.OrderPrice,SmartMall_order.BuyerID_id,SmartMall_product.ProductName,SmartMall_order.SellerID_id,SmartMall_order.SellerStockID_id from SmartMall_order inner join SmartMall_product on SmartMall_order.ProductID_id=SmartMall_product.id Where SellerID_id=%s"%(SelID))
		res1=cursor1.fetchall()
		
		# return HttpResponse(res)
		x=0
		data1=dict()
		for r in res1:
			data1[x]={
			"id": r[0],
			"OrderQuantity": r[1],
			"OrderPrice": r[2],
			"BuyerID_id": r[3],
			"Product Name": r[4],
			"SellerID_id": r[5],
			"SellerStockID_id":r[6]
			}
			x+=1

	
		

	with connection.cursor() as cursor:
		cursor.execute("SELECT id,OrderQuantity,OrderPrice,BuyerID_id,ProductID_id,SellerID_id,SellerStockID_id from SmartMall_order")
		res=cursor.fetchall()
		# return HttpResponse(res)
		a=0
		data=dict()
		for r in res:
			data[a]={
			"id": r[0],
			"OrderQuantity": r[1],
			"OrderPrice": r[2],
			"BuyerID_id": r[3],
			"ProductID_id": r[4],
			"SellerID_id": r[5],
			"SellerStockID_id":r[6]
			}
			a+=1
			
	return render(request,"SmartMall/Admin.html",{"data":data,"data1":data1})

def selectbuy(request):
	if request.method == 'POST':
		
		BuyID = request.POST['buyid']
		
	

	with connection.cursor() as cursor2:
		cursor2.execute("SELECT SmartMall_order.id,SmartMall_order.OrderQuantity,SmartMall_order.OrderPrice,SmartMall_order.BuyerID_id,SmartMall_product.ProductName,SmartMall_order.SellerID_id,SmartMall_order.SellerStockID_id from SmartMall_order inner join SmartMall_product on SmartMall_order.ProductID_id=SmartMall_product.id Where BuyerID_id=%s"%(BuyID))
		res2=cursor2.fetchall()
		
		# return HttpResponse(res)
		x=0
		data2=dict()
		for r in res2:
			data2[x]={
			"id": r[0],
			"OrderQuantity": r[1],
			"OrderPrice": r[2],
			"BuyerID_id": r[3],
			"Product Name": r[4],
			"SellerID_id": r[5],
			"SellerStockID_id":r[6]
			}
			x+=1
		

	with connection.cursor() as cursor:
		cursor.execute("SELECT id,OrderQuantity,OrderPrice,BuyerID_id,ProductID_id,SellerID_id,SellerStockID_id from SmartMall_order")
		res=cursor.fetchall()
		# return HttpResponse(res)
		a=0
		data=dict()
		for r in res:
			data[a]={
			"id": r[0],
			"OrderQuantity": r[1],
			"OrderPrice": r[2],
			"BuyerID_id": r[3],
			"ProductID_id": r[4],
			"SellerID_id": r[5],
			"SellerStockID_id":r[6]
			}
			a+=1
			
	return render(request,"SmartMall/Admin.html",{"data":data,"data2":data2})

def addSTO(request):
	if request.method == 'POST':
		
		pid = request.POST['id']
		quant = request.POST['Quantity']
		User_id = request.session['logged_in']
		sid="SELECT id from SmartMall_seller Where UserID_id=%s)"%(User_id)
		with connection.cursor() as cursor1:
			cursor1.execute("SELECT id from SmartMall_seller Where UserID_id=%s"%(User_id))
			res1=cursor1.fetchone()
		
		


		table = SellerStock()
		table.ProductID_id = pid
		table.StockQuantity = quant
		table.SellerID_id = res1[0] 


		table.save()
	return redirect('/sellerDashboard/')	

def addB(request):
	if request.method == 'POST':
		
		Username= request.POST['Username']
		FirstName = request.POST['FirstName']
		LastName = request.POST['LastName']
		Flat = request.POST['Flat']
		City = request.POST['City']
		Pin = request.POST['Pin']
		
		table = User2()
		table.Username=Username
		table.FirstName = FirstName
		table.LastName = LastName
		table.Flat = Flat
		table.City = City
		table.Pincode = Pin
		table.Role='BUY'
	
		table.save()
	return redirect('/adminDashboard/')	

def addcashS(request):
	if request.method == 'POST':
		
		cash= request.POST['cash']
		User_id = request.session['logged_in']
		
		latitude= request.POST['latitude']
		longitude= request.POST['longitude']
		table = Seller()
		table.SellerCash=cash
		table.UserID_id = User_id 
		table.Slatitude=latitude
		table.Slongitude=longitude

		
		table.save()
	return redirect('/sellerDashboard/')		

def addcashB(request):
	if request.method == 'POST':
		
		cash= request.POST['cash']
		User_id = request.session['logged_in']
		
		latitude= request.POST['latitude']
		longitude= request.POST['longitude']
		table = Buyer()
		table.BuyerCash=cash
		table.UserID_id = User_id 
		table.Blatitude=latitude
		table.Blongitude=longitude

		
		table.save()
	return redirect('/buyerDashboard/')

def addfpro(request):
	if request.method == 'POST':
		
		# fno= request.POST['fno']
		User_id = request.session['logged_in']
		with connection.cursor() as cursor1:
			cursor1.execute("SELECT id from SmartMall_buyer Where UserID_id=%s"%(User_id))
			res1=cursor1.fetchone()
		
		limit= request.POST['limit']
		productid= request.POST['productid']
		table = Fridge()
		# table.FridgeNumber=fno
		table.BuyerID_id = res1[0] 
		table.RequiredLimit=limit
		table.ProductID_id=productid

		
		table.save()
	return redirect('/buyerDashboard/')	

def fridgeProducts(request):
	if request.method == 'POST':
		
		FridgeNumber = request.POST['FridgeNumber']
		ProductId = request.POST.get('ProductId')
		RequiredLimit = request.POST['RequiredLimit']
		table = Fridge()
		table.FridgeNumber = FridgeNumber
		table.ProductId = ProductId
		table.RequiredLimit = RequiredLimit
		table.save()
	return redirect('/openfridge/')	


# def sendmail(request):
# 	import smtplib
# 	import mysql.connector

# 	connection = mysql.connector.connect(host='localhost',
#                                      database='library',
#                                      user='root',
#                                      password='')

# 	while(True):


#     try:

#         cursor = connection.cursor()
#         # sql = "select s.email from student as s, violations as v where s.s_id = v.s_id group by v.s_id having count(v.s_id)>10"
#         # sql = "select s_id from student"
#         # result = cursor.execute(sql)
#         cursor.execute("select s.email from student as s, violations as v where s.s_id = v.s_id group by v.s_id having count(v.s_id)>10")

#         result = cursor.fetchall()
#         #print(1)
#         #print(result)
#         # connection.commit()
#         #print("Record inserted successfully into violations table")
#         cursor.close()


#     except mysql.connector.Error as error:
#         print("Failed to insert record into Laptop table {}".format(error))

#     for i in result:
#         print(i[0])
#         s = smtplib.SMTP('smtp.gmail.com', 587)
#         s.starttls()
#         s.login("shubhamkelkar2302@gmail.com","targetIFS")
#         message = "Hello "+",\nYou've received 15 warnings.\nPlease pay the penalty of Rs50 while entering the library next time.\nThank You."
#         s.sendmail("shubhamkelkar2302@gmail.com",i[0], message)
#         s.quit()
#         cursor = connection.cursor()
#         #print(1)
#         sql2="delete from violations where s_id=any(select s_id from student where email='%s')"
#         # sql2 ="truncate violations"
#         #print(2)
#         result = cursor.execute(sql2 %i[0])
#         #print(3)
#         connection.commit()
#         cursor.close()

#     return redirect('/adminDashboard/')   


def email(request):
   
    subject = 'SmartMall Order Details'
    message = ' \nWelcome to a new week of hassle free ordering. \nAfter reviewing you fridge stocks a new order for weekly stocks has been placed. \nThank You '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['2017.mitali.ranawat@ves.ac.in',]
    send_mail( subject, message, email_from, recipient_list )


    return redirect('/adminDashboard/') 


# def people(request):
#     istekler = Order.objects.all()
#     return render(request, 'list.html', locals())    												




