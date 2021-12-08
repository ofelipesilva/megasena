from random import sample
import requests


class GeradorMega:
    def __init__(self):
        self.loteria = 'mega-sena'
        self.api_2 = f'https://loteriascaixa-api.herokuapp.com/api/{self.loteria}/latest'

    def gerar_numeros(self):
        return sample(range(1, 61), k=6)

    def gerar_html(self, dezenas):
        generated_html = '<div class="row">'
        for number in dezenas:
            generated_html += f'''
                <div class="col-sm-2">
                    <div class="card">
                        <div class="card-body mega_numbers" align="center">
                            <p class="card-text">{int(number):02d}</p>
                        </div>
                    </div>
                </div>
            '''
        generated_html += '</div>'
        return generated_html

    def ultimo_resultado(self):
        r = requests.get(self.api_2).json()
        data = {
            'concurso': r['concurso'],
            'data': r['data'],
            'dezenas': self.gerar_html(r['dezenas']),
            'acumulou': 'Sim' if r['acumulou'] else 'Não',
            'prox_premio': r['acumuladaProxConcurso'],
            'prox_concurso': r['dataProxConcurso']
        }

        return data
