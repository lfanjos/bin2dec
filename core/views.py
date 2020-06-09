from django.shortcuts import render
from .forms import NumeroForm
from django.contrib import messages


def index(request):
    output = 0
    form = NumeroForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            numero = str(form.cleaned_data['numero'])
            tipo = form.cleaned_data['tipo']
            if tipo == 'BINARIO':
                if len(numero) > 32:
                    output = 'Insira um número binário com até 8 dígitos binário!'
                else:
                    bina = [1]
                    ind = -1
                    if numero.count('1') + numero.count('0') != len(numero):
                        messages.error(request, 'Por favor, insira apenas 0 e 1.')
                        output = ''
                    else:
                        messages.success(request, 'Número convertido sem falhas!')
                        for i in range(0, len(numero) - 1):
                            bina.append(2 ** (i + 1))
                        for digit in numero:
                            if digit == '1':
                                output += bina[ind]
                            ind -= 1
                        output = f'Binário: {numero} \t\t Decimal: {output}'
            elif tipo == 'DECIMAL':
                numero = int(numero)
                origin = numero
                bina = [1]
                dec = 1
                string = ''
                while 2 ** dec <= int(numero):
                    bina.append(2 ** dec)
                    dec += 1
                bina.reverse()
                for num in bina:
                    if num <= numero:
                        numero -= num
                        string += '1'
                    else:
                        string += '0'
                if len(string) < 4:
                    string = str('0' * (4 - len(string))) + string
                output = f'Binário: {string} \t\t Decimal: {origin}'
                messages.success(request, 'Número convertido sem falhas!')
            form = NumeroForm()
        else:
            messages.error(request, 'Erro ao converter número!')
    elif str(request.method) == 'GET':
        output = ''
    context = {
        'form': form,
        'output': output,
    }
    return render(request, 'index.html', context)
