# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from forms import AlunoForm
from alunos.models import Aluno
from django.shortcuts import render, redirect
from alunos.models import Aluno
from alunos.forms import AlunoForm


def lista(request):
	alunos = Aluno.objects.all()
	context = RequestContext(request, {'alunos': alunos})
	return render_to_response('aluno/list.html', context)


def create(request):
	form = AlunoForm(request.POST or None)
	
	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect('/alunos/')

	context = RequestContext(request, {'form': form})
	return render_to_response('aluno/create.html', context)


def delete(request, codigoAluno):
    aluno = Aluno.objects.get(pk=codigoAluno)

    if request.method == "POST":
        aluno.delete()
        return HttpResponseRedirect('/alunos/')

    context = RequestContext(request, {'aluno': aluno})
    return render_to_response('aluno/delete.html', context)


def update(request, codigoAluno):
	alunos = Aluno.objects.get(pk=codigoAluno)
	
	if request.method == 'POST':
		form = AlunoForm(request.POST, instance=alunos)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/alunos/')

	else:
		form = AlunoForm(instance=alunos)
		
	context = RequestContext(request, {'form': form, 'codigoAluno': codigoAluno})
	return render_to_response('aluno/update.html', context)	
