from django.shortcuts import render, redirect 
from django.http import HttpResponse,HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
from .models import *
from .forms import CreateUserForm 
# Create your views here.
from .forms import OrderForm, CreateUserForm, Customer1Form ,CustomerForm,CustomerUserForm
from .forms import QuestionForm,QuestionForm1
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			#group=Group.objects.get(name="customer")
			#user.groups.add(group)
			#Customer.objects.create(
				#user=user,
				#name=user.username,
				#)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
	context = {'form':form}
	return render(request, 'app/register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'app/login.html', context)

def logoutPage(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer','admin'])
def home(request):
	return render(request, 'app/main.html')

 
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer','admin'])
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Contact" 
			body = {
			'full_name': form.cleaned_data['full_name'], 
			'phone': form.cleaned_data['phone'], 
			'email': form.cleaned_data['email_address'], 
			'subject':form.cleaned_data['subject'],
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'email_address', ['sunkavamshinath@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("/")
      
	form = ContactForm()
	return render(request, "app/contact.html", {'form':form})
	 
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer','admin'])
def about(request):
	return render(request, 'app/about.html')
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer','admin'])
def services(request):
	return render(request, 'app/services1.html')
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer','admin'])
def status(request):
	return render(request, 'app/status.html')
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer','admin'])
def apply(request):
	return render(request, 'app/apply.html')
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer','admin'])
def portfolio(request):
	return render(request, 'app/portfolio.html')
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer','admin'])
def faqs(request):
	return render(request, 'app/faqs.html')
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer','admin'])
def news(request):
	return render(request, 'app/news.html')
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs 

	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
	'myFilter':myFilter}
	return render(request, 'app/customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def application(request):
	application=Applications.objects.all()
	return render(request, 'app/application.html',{'application':application})

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
	orders =  request.user.customer.order_set.all()

	total_orders=orders.count()
	p=orders.filter(status='Published').count()
	np=orders.filter(status='Not Published').count()
	w=orders.filter(status='Working on It').count()

	print('ORDERS:', orders)

	context = {'orders':orders, 'total_orders':total_orders,
	'p':p,'np':np,'w':w}
	return render(request, 'app/user.html', context)

@login_required(login_url='login')
@admin_only
def main(request):
	orders=order.objects.all()
	customers=Customer.objects.all()
	total_customers=customers.count()
	total_orders=orders.count()
	membership_count=customers.filter(membership="5 years").count()
	membership_count1=customers.filter(membership="1 years").count()
	membership_count2=customers.filter(membership="No Membership").count()
	malecount=customers.filter(gender="M").count()
	femalecount=customers.filter(gender="F").count()
	none=customers.filter(gender="none").count()
	p=orders.filter(status='Published').count()
	np=orders.filter(status='Not Published').count()
	w=orders.filter(status='Working on It').count()
	context={'none':none,'malecount':malecount,'femalecount':femalecount,'orders':orders, 'customers':customers,'p':p,'np':np,'w':w,'total_orders':total_orders,'total_customers':total_customers,'membership_count':membership_count,'membership_count1':membership_count1,'membership_count2':membership_count2}

	return render(request,'app/dashboard.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, order, fields=('Applications', 'status'), extra=1 )
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=order.objects.none(),instance=customer)
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'app/order_form.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
	orders = order.objects.get(id=pk)
	form = OrderForm(instance=order)
	if request.method == 'POST':

		form = OrderForm(request.POST, instance=orders)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'app/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
	orders = order.objects.get(id=pk)
	if request.method == "POST":
		orders.delete()
		return redirect('/')

	context = {'item':orders}
	return render(request, 'app/delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)
	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()
	 

	context = {'form':form}
	return render(request, 'app/settings.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def membership(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'app/membership.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def applymembership(request):
	customer = request.user.customer
	form = Customer1Form(instance=customer)

	if request.method == 'POST':
		form = Customer1Form(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'app/applymembership.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def payment(request):
	return render(request, 'app/payment.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def ask_question_view(request):
    customer = Customer.objects.get(user_id=request.user.id)
    questionForm=QuestionForm() 
    
    if request.method=='POST':
        questionForm=QuestionForm(request.POST)
        if questionForm.is_valid():
            
            question = questionForm.save(commit=False)
            question.customer=customer
            question.save()
            return redirect('question-history')
    return render(request,'app/ask_question.html',{'questionForm':questionForm,'customer':customer})
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def question_history_view(request):
    customer = Customer.objects.get(user_id=request.user.id)
    questions = Question.objects.all().filter(customer=customer)
    return render(request,'app/question_history.html',{'questions':questions,'customer':customer})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_question_view(request):
    questions = Question.objects.all()
    return render(request,'app/admin_question.html',{'questions':questions})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_question_view(request,pk):
    question = Question.objects.get(id=pk)
    questionForm=QuestionForm(instance=question)
    
    if request.method=='POST':
        questionForm=QuestionForm(request.POST,instance=question)
        
        if questionForm.is_valid():

            admin_comment = request.POST.get('admin_comment')
            
            
            question = questionForm.save(commit=False)
            question.admin_comment=admin_comment
            question.save()
           
            return redirect('admin-question')
    return render(request,'app/update_question.html',{'questionForm':questionForm})



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_view_customer_view(request):
    customers= Customer.objects.all()
    return render(request,'app/admin_view_customer.html',{'customers':customers})



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_customer_view(request,pk):
    customer=Customer.objects.get(id=pk)
    user=User.objects.get(id=customer.user_id)
    userForm=CustomerUserForm(instance=user)
    customerForm=CustomerForm(request.FILES,instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=CustomerUserForm(request.POST,instance=user)
        customerForm=CustomerForm(request.POST,request.FILES,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return redirect('admin-view-customer')
    return render(request,'app/update_customer.html',context=mydict)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_customer_view(request,pk):
    customer=Customer.objects.get(id=pk)
    user=User.objects.get(id=customer.user_id)
    user.delete()
    customer.delete()
    return HttpResponseRedirect('/admin-view-customer')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def invest(request,pk):
	customer=Customer.objects.get(id=pk)
	user=User.objects.get(id=customer.user_id)
	customers=Idea.objects.all().order_by('asked_date')
	context={'customer':customer,'user':user,'customers':customers}
	return render(request,'app/investmentgraph.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def feed(request):
    customer = Customer.objects.get(user_id=request.user.id)
    questionForm=QuestionForm1() 
    
    if request.method=='POST':
        questionForm=QuestionForm1(request.POST)
        if questionForm.is_valid():
            
            question = questionForm.save(commit=False)
            question.customer=customer
            question.save()
            return redirect('question-history')
    return render(request,'app/feed.html',{'questionForm':questionForm,'customer':customer})

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def feedhistory(request):
    customer = Customer.objects.get(user_id=request.user.id)
    questions = Idea.objects.all().filter(customer=customer)
    return render(request,'app/feedhistory.html',{'questions':questions,'customer':customer})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def investoridea(request):
    questions = Idea.objects.all()
    return render(request,'app/investoridea.html',{'questions':questions})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def feedupdate(request,pk):
    question = Idea.objects.get(id=pk)
    questionForm1=QuestionForm1(instance=question)
    if request.method=='POST':
        questionForm1=QuestionForm1(request.POST,instance=question)
        
        if questionForm1.is_valid():

            investor_comment = request.POST.get('investor_comment')
            price=request.POST.get('price')
            question = questionForm1.save(commit=False)
            question.investor_comment=investor_comment
            question.price=price
            question.save()
           
            return redirect('investoridea')
    return render(request,'app/feedupdate.html',{'questionForm1':questionForm1})