from django.shortcuts import render

# Create your views here.
def home(request):
    context={'file':FileAdmin.objects.all()}
    return render(request,'upload/home.html',context)



def download(request,path):
    file_path=os.path(' mypath/', csrf_exempt(GraphQLView.as_view(graphiql=True)))
