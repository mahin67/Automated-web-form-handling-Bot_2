from django.shortcuts import render, HttpResponse
from .models import FIleUpload,Information

def home(request):
        if request.method == "POST" :

                print('Page reloaded')
                name1=request.POST['Name']
                dob1 = request.POST['DOB']
                fname1 = request.POST['Fname']
                mname1 = request.POST['Mname']
                gen1 = request.POST['Gender']
                addr1 = request.POST['Address']
                cty1 = request.POST['City']
                pin1 = request.POST['Pin_Code']
                cntry1 = request.POST['Country']
                ins = Information(name=name1,dob=dob1,fname=fname1,mname=mname1,gen=gen1,addr=addr1,cty=cty1,pin=pin1,cnty=cntry1)
                print(name1,dob1,fname1,mname1,gen1,addr1,cty1,pin1,cntry1)
                ins.save()
                print('Saved in database')
        return render(request, 'Loading_page.html')





'''
file2 = request.FILES['file']
                document = FIleUpload.objects.create(file = file2)
                document.save()
'''