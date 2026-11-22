from django.shortcuts import render
from .forms import ProgramaForm

def crear_programa(request):
    mensaje = ""
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProgramaForm()
            mensaje = "Programa guardado correctamente"
    else:
        form = ProgramaForm()

    return render(request, 'crear_programa.html', {'form': form, 'mensaje': mensaje})