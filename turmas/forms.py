from django.forms import ModelForm
from alunos.models import Aluno
from alunos.models import Turma



class AlunoForm(ModelForm):
    class Meta:
    	model = Aluno
    	fields = ['nomeAluno', 'cpf','telefone', 'dataNasc', 'turma']

class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = ['nomeTurma', 'descricaoTurma']