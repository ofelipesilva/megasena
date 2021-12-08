from django.shortcuts import render

from .gerador import GeradorMega

ultimo_resultado = GeradorMega().ultimo_resultado()
# Create your views here.
def home(request):
    jogo = GeradorMega()
    
    html = None
    if request.method == 'POST' and 'run_script' in request.POST:
        html = jogo.gerar_html(jogo.gerar_numeros())

    context = {
        'jogo': html,
        'ultimo_resultado': ultimo_resultado
    }

    return render(request, 'home.html', context)
