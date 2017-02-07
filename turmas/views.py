# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from forms import TurmaForm
from turmas.models import Turma
from django.shortcuts import render, redirect
from turmas.models import Turma
from turmas.forms import TurmaForm


def lista(request):
	turmas = Turma.objects.all()
	context = RequestContext(request, {'turmas': turmas})
	return render_to_response('turma/list.html', context)


def create(request):
	form = TurmaForm(request.POST or None)
	
	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect('/turmas/lista')

	context = RequestContext(request, {'form': form})
	return render_to_response('turma/create.html', context)


def delete(request, codigoTurma):
    turma = Turma.objects.get(pk=codigoTurma)

    if request.method == "POST":
        turma.delete()
        return HttpResponseRedirect('/turmas/')

    context = RequestContext(request, {'turma': turma})
    return render_to_response('turma/delete.html', context)


def update(request, codigoTurma):
	turmas = Turma.objects.get(pk=codigoTurma)
	
	if request.method == 'POST':
		form = TurmaForm(request.POST, instance=turmas)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/turmas/')

	else:
		form = TurmaForm(instance=turmas)
		
	context = RequestContext(request, {'form': form, 'codigoTurma': codigoTurma})
	return render_to_response('turma/update.html', context)	
