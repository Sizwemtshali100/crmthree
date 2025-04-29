from django.shortcuts import render, redirect
from . models import CustomerModel
from . forms import CustomerForm, CustomerRegistration
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import csv
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.

def MyProfile(request):
    return render(request, 'MyProfile.html')

def TheLogOut(request):
    logout(request)
    return redirect('TheLogin')

def TheDownload(request):
    myResponse = HttpResponse(content_type='text/csv')
    myResponse['Content-Disposition'] = 'attachment; filename="TheData.csv"'
    write = csv.writer(myResponse)
    downloadingData = CustomerModel.objects.all()
    write.writerow(['TheDate',
                    'Created_by',
                    'Region',
                    'Rep',
                    'Items',
                    'Units',
                    'Cost'])
    for download in downloadingData:
        write.writerow([    
            download.TheDate,
            download.Created_by,
            download.Region,
            download.Rep,
            download.Items,
            download.Units,
            download.Cost
            ])
    return myResponse 
    
@login_required(login_url='TheLogin')
def home(request):
    theData = CustomerModel.objects.all().order_by('id')
    theDataPencil = CustomerModel.objects.filter(Items='Pencil').count()
    theDataBender = CustomerModel.objects.filter(Items='Binder').count()
    theDataPen = CustomerModel.objects.filter(Items='Pen').count()
    theDataDesk = CustomerModel.objects.filter(Items='Desk').count()
    theDataPenSet = CustomerModel.objects.filter(Items='Pen Set').count()
    myPagnitor = Paginator(theData, 5)
    pageNumber = request.GET.get('page')
    pageObject = myPagnitor.get_page(pageNumber)
    return render(request, 'home.html',{#'theData':theData,
                                        'pageObject':pageObject,
                                        'theDataPencil':theDataPencil,
                                        'theDataBender':theDataBender,
                                        'theDataPen':theDataPen,
                                        'theDataDesk':theDataDesk,
                                        'theDataPenSet':theDataPenSet,
                                        })

@login_required(login_url='TheLogin')
def Theform(request):
    if request.method == 'POST':
        TheCustomerForm = CustomerForm(request.POST)
        if TheCustomerForm.is_valid():
            myUser = TheCustomerForm.save(commit=False)
            myUser.Created_by = request.user
            TheCustomerForm.save()
            return redirect('home')
    else:
        TheCustomerForm = CustomerForm(request.POST)
    return render(request, 'Theform.html',
                  {'TheCustomerForm':TheCustomerForm})

@login_required(login_url='TheLogin')
def TheDetails(request, details_id):
    theDataDetails = CustomerModel.objects.get(pk=details_id)
    return render(request, 'TheDetails.html',
                  {'theDataDetails':theDataDetails})

@login_required(login_url='TheLogin')
def TheEdit(request, edit_id):
    EditData = CustomerModel.objects.get(pk=edit_id)
    Editform = CustomerForm(request.POST or None, instance=EditData)
    if request.method == 'POST':
        if Editform.is_valid():
            Editform.save()
            return redirect('home')
    return render(request, 'TheEdit.html',{'Editform':Editform,
                                           'EditData':EditData})                  

def TheLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        TheUser = authenticate(request, username=username, password=password)
        if TheUser is not None:
            login(request, TheUser)
            return redirect('home')
    else:
            messages.error(request, "Something aren't right") 
       
    return render(request, 'TheLogin.html')

def TheRegister(request):
    if request.method == 'POST':
        TheRegistration = CustomerRegistration(request.POST)
        if TheRegistration.is_valid():
            user = TheRegistration.save(commit=False)  # Save without committing
            user.save()  # Save the user
            return redirect('TheLogin')  # Redirect to home page
    else:
        TheRegistration = CustomerRegistration()  # Empty form on GET request

    return render(request, 'TheRegister.html', {'TheRegistration': TheRegistration})