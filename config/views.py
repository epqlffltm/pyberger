from django.shortcuts import render
from burgers.models import Burger

def main(request):
  return render(request,"main.html")

def burger_list(request):
  burgers = Burger.objects.all()
  print("전체 햄버거 목록: ",burgers)
  content = {"burgers":burgers}
  return render(request,"burger_list.html",content)

def burger_search(request):
  print(request.GET)
  keyword = request.GET.get("keyword")
  burgers = Burger.objects.filter(name__icontains=keyword) if keyword else Burger.objects.none()
  print(keyword)
  print("검색된 햄버거 목록:", burgers)
  context = {"burgers":burgers}
  return render(request,"burger_search.html",context)