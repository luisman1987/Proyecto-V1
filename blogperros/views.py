from django.shortcuts import render
from blogperros.models import Perro,Persona
from django.shortcuts import render, render_to_response ,get_object_or_404
from blogperros.forms import PerroForm
from django.shortcuts import redirect
from blogperros.models import Persona, Asignacion
from blogperros.forms import PersonaForm

#Autenticacion
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from blogperros.forms import SignUpForm
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required()
def home(request):
    return render_to_response('blogperros/listado_perros.html', {'user': request.user}, context_instance=RequestContext(request))


def main(request):
    return render_to_response('blogperros/main.html', {}, context_instance=RequestContext(request))


@login_required()
def listado_perros(request):
    posts = Perro.objects.all()
    return render(request, 'blogperros/listado_perros.html', {'posts': posts})

@login_required()
def detalle_perro(request, pk):
    post = get_object_or_404(Perro, pk=pk)
    return render(request, 'blogperros/detalle_perro.html', {'post': post})

@login_required()
def perro_nuevo(request):
        if request.method == "POST":
            form = PerroForm(request.POST, request.FILES or None)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('blogperros.views.perro_editar', pk=post.pk)
        else:
            form = PerroForm()
        return render(request, 'blogperros/editar_perro.html', {'form': form})

def perro_eliminar(request, pk=None):
    instance = get_object_or_404(Perro, pk=pk)
    instance.delete()
    redirect('blogperros.views.listado_perros')
    return HttpResponseRedirect('/home')

@login_required()
def perro_editar(request, pk):
    post = get_object_or_404(Perro, pk=pk)
    if request.method == "POST":
        form = PerroForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blogperros.views.detalle_perro', pk=post.pk)
    else:
        form = PerroForm(instance=post)
    return render(request, 'blogperros/editar_perro.html', {'form': form})

@login_required()
def listado_personas(request):
    posts = Persona.objects.all()
    return render(request, 'blogperros/listado_persona.html', {'posts': posts})

@login_required()
def detalle_persona(request, pk):
    post = get_object_or_404(Persona, pk=pk)
    perros = Asignacion.objects.filter(persona=post)
    return render(request, 'blogperros/detalle_persona.html', {'post': post, 'perros':perros})


@login_required()
def persona_nueva(request):
    if request.method == "POST":
        formulario = PersonaForm(request.POST,request.FILES or None)
        if formulario.is_valid():
            persona = Persona.objects.create(dpi=formulario.cleaned_data['dpi'],nombre=formulario.cleaned_data['nombre'],apellido=formulario.cleaned_data['apellido'],foto=formulario.cleaned_data['foto'])
            for perro_id in request.POST.getlist('perros'):
               asignacion = Asignacion(persona_id = persona.id, perro_id=perro_id)
               asignacion.save()

            messages.add_message(request, messages.SUCCESS, 'Asgnacion exitosa')
    else:
        formulario = PersonaForm()
    return render(request, 'blogperros/editar_persona.html', {'formulario': formulario})

@login_required()
def editar_persona(request, pk):
    post = get_object_or_404(Persona, pk=pk)
    if request.method == "POST":
        form = PersonaForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blogperros.views.detalle_persona', pk=post.pk)
    else:
        form = PersonaForm(instance=post)
    return render(request, 'blogperros/editar_persona.html', {'form': form})



def asignacion_nueva(request):
    if request.method == "POST":
        formulario = AsignacionForm(request.POST)
        if formulario.is_valid():

            asignacion = Asignacion.objects.create(persona=formulario.cleaned_data['persona'])
            for perro_id in request.POST.getlist('perro'):

               asig = Asignacion(perro_id=perro_id, persona_id = asignacion.id)
               asig.save()

            messages.add_message(request, messages.SUCCESS, 'Asgnacion exitosa')
    else:
        formulario = AsignacionForm()
    return render(request, 'blogperros/asignacion_editar.html', {'formulario': formulario})




def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name

            # Save new user attributes
            user.save()

            return HttpResponseRedirect(reverse('main'))  # Redirect after POST
    else:
        form = SignUpForm()

    data = {
        'form': form,
    }
    return render_to_response('blogperros/signup.html', data, context_instance=RequestContext(request))
