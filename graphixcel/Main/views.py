from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import graphGen

def Main(request):
    requestDict=dict(request.POST.items())
    if request.method=='POST' and ('xaxis' in requestDict or 'yaxis' in requestDict or 'column' in requestDict):
        print(requestDict['graph'])
        if requestDict['graph']=="bar":
            graphGen.generate_bar_chart(requestDict['xaxis'],requestDict['yaxis'])
        elif requestDict['graph']=="line":
            graphGen.plot_with_matplotlib(requestDict['xaxis'],requestDict['yaxis'])
        elif requestDict['graph']=="pie":
            graphGen.generate_pie_chart(requestDict['column'])
        list=graphGen.getDataList()
        return render(request,'index.html',{'output':'true','file':'true','columns':list})
    elif request.method=='POST':
        print(dict(request.POST.items()))
        file=request.FILES['file']
        fileStorageSystem=FileSystemStorage()
        file.name="file."+file.name.split('.')[1]
        fileStorageSystem.save(file.name,file)
        list=graphGen.getDataList()
        return render(request,'index.html',{'columns':list,'file':'true'})
    return render(request,'index.html')