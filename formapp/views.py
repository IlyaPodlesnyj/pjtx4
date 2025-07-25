from django.shortcuts import render, redirect
from .models import DynamicFormData

def form_view(request):
    if request.method == 'POST':
        names = request.POST.getlist('field[]')
        print("Полученные данные:", names)  # Для отладки, посмотреть в консоли
        # Удаляем пустые значения, если есть
        names = [name for name in names if name.strip()]
        if names:
            DynamicFormData.objects.create(data=names)
        return redirect('show_data')

    return render(request, 'formapp/form.html')


def show_data(request):
    # Если у модели нет created_at — убрать order_by
    all_data = DynamicFormData.objects.all().order_by('-id')
    return render(request, 'formapp/show.html', {'all_data': all_data})

# Create your views here.
