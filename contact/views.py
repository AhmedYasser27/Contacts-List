from django.shortcuts import render,redirect
from contact.models import Contact

# Create your views here.


def index(request):
    contacts=Contact.objects.all()
    search_input=request.GET.get('search-area')
    if search_input:
        contacts=Contact.objects.filter(Full_Name__icontains=search_input)
    else:
        contacts4=Contact.objects.all()
        search_input=''
    return render (request,'index.html',{'contacts':contacts , 'search_input':search_input})


def addcontact(request):
    if request.method=='POST':
        new_contact=Contact(
            Full_Name=request.POST['fullname'],
            Job_Title=request.POST['job title'],
            Email=request.POST['email'],
            EXT=request.POST['ext'],
            Dir_Phone=request.POST['direct phone'],
            Mobile=request.POST['mobile'],
            Branch=request.POST['branch'],
        )
        new_contact.save()
        return redirect('/')
    return render(request,'new.html')


def contactprofile(request,pk):
    contact=Contact.objects.get(id=pk)
    return render(request,'contact-profile.html',{'contact':contact})

def editcontact(request,pk):
    contact=Contact.objects.get(id=pk)
    if request.method=='POST':
        contact.Full_Name=request.POST['fullname']
        contact.Job_Title=request.POST['job title']
        contact.Branch=request.POST['branch']
        contact.Email=request.POST['email']
        contact.EXT=request.POST['ext']
        contact.Dir_Phone=request.POST['dir_phone']
        contact.Mobile=request.POST['mobile']

        contact.save()
        return redirect('/profile/'+str(contact.id))
    return render(request,'edit.html', {'contact':contact})


def deletecontact(request,pk):
    contact=Contact.objects.get(id=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('/')
    return render(request,'delete.html',{'contact':contact})