from django.forms import ModelForm
from alunos.models import Aluno
from alunos.models import Turma


class AlunoForm(ModelForm):
    class Meta:
    	model = Aluno
    	fields = ['turma','nomeAluno', 'cpf','telefone', 'dataNasc']

class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = ['codigoTurma', 'nomeTurma', 'descricaoTurma']