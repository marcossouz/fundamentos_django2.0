from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

from .models import Transacao
from .forms import TransacaoForm

def home(request):
    data = {}
    data['now'] = datetime.datetime.now()
    data['transacoes'] = ['t1','t2','t3']
    # html = "<html><body>It's is now %s. </body></html>" % now
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def novaTransacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render(request, 'contas/form.html', {'form': form})

def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render(request, 'contas/form.html', {'form': form, 'transacao': transacao})

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')
