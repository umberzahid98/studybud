from django.shortcuts import render


rooms = [
  { 'id': 1, 'name': 'lets learn python!'},
  { 'id': 2, 'name':  'design with me!'},
  { 'id': 3, 'name': 'FE developer!'}

]

# Create your views here.
def home(request):
    context = { 'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')
