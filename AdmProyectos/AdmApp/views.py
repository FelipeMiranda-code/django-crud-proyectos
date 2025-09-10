from django.shortcuts import render, redirect

# Create your views here.

proyectos = []

def mostrarPaginaInicio (request):
    return render(request, 'index.html')

def listarProyectos (request):
    return render(request, 'proyectos.html', {'proyectos': proyectos} )

def agregarProyecto(request):
    if request.method == 'POST':
        proyecto = {
            'id': len(proyectos) + 1,
            'nombre': request.POST['nombre'],
            'fecha_inicio': request.POST['fecha_inicio'],
            'fecha_termino': request.POST['fecha_termino'],
            'responsable': request.POST['responsable'],
            'prioridad': request.POST['prioridad'],
        }
        proyectos.append(proyecto)
        return redirect('listarproyectos')
    return render(request, 'agregar.html')

def actualizarProyecto(request, id):
    proyecto = next((p for p in proyectos if p['id'] == id), None)
    if request.method == 'POST' and proyecto:
        proyecto['nombre'] = request.POST['nombre']
        proyecto['fecha_inicio'] = request.POST['fecha_inicio']
        proyecto['fecha_termino'] = request.POST['fecha_termino']
        proyecto['responsable'] = request.POST['responsable']
        proyecto['prioridad'] = request.POST['prioridad']
        return redirect('listarproyectos')
    return render(request, 'actualizar.html', {'proyecto': proyecto})

def eliminarProyecto(request, id):
    global proyectos
    proyectos = [p for p in proyectos if p['id'] != id]
    return redirect('listarproyectos')