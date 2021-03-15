from django.shortcuts import render

# Create your views here.
# No. 2 eu am creat funtia home, this function return the template 
# render = a face , a reda, reda pagina home.html din app-ul base 
def home(request):
	return render(request, 'base/home.html')
