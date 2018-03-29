from django.shortcuts import render
from django.http import HttpResponse
from django.core.files import File
from .models import data1,data2,undata2,Patient,Myuser
from .forms import uform
from django.contrib.auth import authenticate, login, logout

import csv
import knn1,knn2,bayes
# Create your views here.


def Index(request):
    return render(request, 'analyze/index.html')


def EegSignal(request):
    alpha=request.POST.get('alpha')
    beta=request.POST.get('beta')
    theta=request.POST.get('theta')
    delta=request.POST.get('delta')
    print alpha

    tuple=str(alpha)+","+str(beta)+","+str(theta)+","+str(delta)+","+"Null"
    tuple1=str(alpha)+","+str(beta)+","+str(theta)+","+str(delta)

    with open('/Users/smrutimukundvarvadekar/Downloads/eeg.data', 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        print "lllllll"


    f = open('/Users/smrutimukundvarvadekar/Downloads/eeg.data', 'r')
    myfile = File(f)
    bayes.execbayes(tuple1)
    knn1.exect(tuple)
    #knn1.main()
    if f.mode=="r":
        contents=f.read()
        print "ppqpqppqpqppqq"
        print contents[0][0]

    f.close()
    print "fffffffff"
    print knn1.send
    print bayes.decision

    print myfile
    context={'send':knn1.send}
    return render(request, 'analyze/symptomsInfo.html',context)

def EegSignalForm(request):
    return render(request, 'analyze/eegSignalInfo.html')

def SymptomsForm(request):
    return render(request,'analyze/symptomsInfo.html')

def Symptoms(request,send):
    age = request.POST.get('age')
    memory = request.POST.get('memory')
    interpretation = request.POST.get('interpretation')
    muffled = request.POST.get('muffled')

    behaviour = request.POST.get('behaviour')
    hallucination = request.POST.get('visual')

    print 'values'
    print age
    print memory
    print interpretation
    print muffled
    print behaviour
    print hallucination

    s=undata2()
    s.age=age
    print 'divita'
    print s.age
    s.memory=memory
    s.interpretation=interpretation
    s.muffled=muffled
    s.behaviour=behaviour
    s.visual=hallucination
    s.slowing=send
    s.chances=0
    s.flag=1
    s.save()

    symptoms=undata2.objects.all()
    print "helllllo"
    list_age=[]
    for t in symptoms:
        list_age.append(t.age)
    min_age=float(min(list_age))
    max_age=float(max(list_age))
    print  min_age

    list_memory = []
    for t in symptoms:
        list_memory.append(t.memory)
    min_memory = min(list_memory)
    max_memory = max(list_memory)
    print list_memory
    print   max_memory

    list_interpretation = []
    for t in symptoms:
        list_interpretation.append(t.interpretation)
    min_interpretation = min(list_interpretation)
    max_interpretation = max(list_interpretation)
    print list_interpretation
    print  max_interpretation

    list_behaviour = []
    for t in symptoms:
        list_behaviour.append(t.behaviour)
    min_behaviour = min(list_behaviour)
    max_behaviour = max(list_behaviour)
    print list_behaviour
    print max_behaviour

    list_muffled = []
    for t in symptoms:
        list_muffled.append(t.muffled)
    min_muffled = min(list_muffled)
    max_muffled = max(list_muffled)
    print list_muffled
    print max_muffled

    list_visual = []
    for t in symptoms:
        list_visual.append(t.visual)
    min_visual = min(list_visual)
    max_visual = max(list_visual)
    print list_visual
    print max_visual

    n_age=(float(age)-min_age)/(max_age-min_age)
    n_memory=(float(memory)-min_memory)/(max_memory-min_memory)
    n_interpretation=(float(interpretation)-min_interpretation)/(max_interpretation-min_interpretation)
    n_muffled=(float(muffled)-min_muffled)/(max_muffled-min_muffled)
    n_behaviour=(float(behaviour)-min_behaviour)/(max_behaviour-min_behaviour)
    n_hallucination=(float(hallucination)-min_visual)/(max_visual-min_visual)





    tuple2=str(send)+","+str(n_age)+","+str(n_memory)+","+str(n_interpretation)+","+str(n_muffled)+","+str(n_behaviour)+","+str(n_hallucination)+","+"0"

    print tuple2
    final_tuple=str(tuple2)
    knn2.exec2(tuple2)
    accuracy=knn2.accuracy
    result=knn2.result
    slow = 'NO'
    if send == '1':
        slow = "YES"



    context={'slow':slow,'accuracy':accuracy,'result':result,'n_age':n_age,'n_memory':n_memory,'n_interpretation':n_interpretation,'n_muffled':n_muffled,'n_behaviour':n_behaviour,'n_hallucination':n_hallucination,'send':send}
    return  render(request, 'analyze/result.html',context)

def results(request,slowing,age,ml,difii,mspeech,b,vh,result):
    print "ffddddd"
    print result
    print slowing
    slow='NO'
    if slowing==1:
        slow="YES"

    tuple2="\n"+str(slowing)+","+str(age)+","+str(ml)+","+str(difii)+","+str(mspeech)+","+str(b)+","+str(vh)+","+str(result)
    print 'tuplee2222'
    print tuple2
    print 'hahaha'
    f = open('/Users/smrutimukundvarvadekar/Downloads/eegfinal.data', 'a+')

    if f.mode == "a+":
        f.write(tuple2)
    f.close()

    f = open('/Users/smrutimukundvarvadekar/Downloads/eegfinal.data', 'r')


    if f.mode == "r":
        contents = f.read()
        print contents

    s=undata2.objects.get(flag=1)
    s.flag=0
    s.chances=result
    s.save()
    print ' checkkkkkkkkkkk'
    print slow
    print result


    return render(request,'analyze/index.html')


def deleteObject(request):
    s=undata2.objects.get(flag=1)
    s.delete()
    return render(request, 'analyze/index.html')

def Login(request):
    return render(request, 'analyze/login.html')


def getreg(request):
    form = uform()
    return render(request, 'analyze/login.html', {'form': form})


def Signup_user(request):
    if request.method == 'POST':
        form = uform(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            print("hii")
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            return render(request, 'analyze/dashboard.html', {'form':form})
    return HttpResponse("outerrr loop")


def Login_user(request):
    print("in loginuser view")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(username,password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'analyze/index.html')
            else:
                return render(request, 'analyze/login.html')
        else:
            return render(request, 'analyze/login.html')

    else:
        return render_to_response('analyze/login.html', {}, context)

def display(request):
    obj = Patient.objects.all()
    obj1=data1.objects.all()
    final=[]
    ti=[]
    for t in obj:
        c=data1.objects.get(pid=t.patient_id)
        final.append(c)
        ti.append(t)
        print final
        lis=zip(ti,final)
        print lis
    return render(request,'analyze/analyze.html',{'obj':obj,'final':final,'lis':lis})

def display1(request):
    obj=undata2.objects.all()
    for t in obj:
        if t.memory==1:
            t.memory="Low"
        elif t.memory==2:
            t.memory="Medium"
        else:
            t.memory="High"
        if t.muffled == 1:
            t.muffled = "Low"
        elif t.muffled == 2:
            t.muffled = "Medium"
        else:
            t.muffled = "High"
        if t.interpretation == 1:
            t.interpretation = "Low"
        elif t.interpretation == 2:
            t.interpretation = "Medium"
        else:
            t.interpretation = "High"
        if t.behaviour == 1:
            t.behaviour = "Abnormal"
        else:
            t.behaviour = "Normal"
        if t.visual == 1:
            t.visual = "Low"
        elif t.visual == 2:
            t.visual = "Medium"
        else:
            t.visual = "High"

    return render(request,'analyze/analyze1.html',{'obj':obj})