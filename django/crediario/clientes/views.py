from django.shortcuts import render
from crediario.clientes.models import Cliente, Configloja
from crediario.clientes.forms import ClienteBuscaForm
from django.contrib import messages


def vw_clientes(request):
    data = {}
    context = {}
    conf = Configloja.objects.get(cd_chave='ZIM   1')
    data['cd_regiao'], data['sg_loja'] = conf.no_conf.split(':')[:2]
    data['cd_regiao'] = int(data['cd_regiao'])
    form = ClienteBuscaForm(initial=data)

    if request.method == 'POST':
        form = ClienteBuscaForm(initial=data, data=request.POST)

        if form.is_valid():
            
            clientes = Cliente.objects.none()

            if form.cleaned_data['cd_cliente'] is not None:
                cd_chave = '{0}{1}'.format(
                    str(form.cleaned_data['cd_regiao']).rjust(2),
                    str(form.cleaned_data['cd_cliente']).rjust(8))
                clientes = Cliente.objects.filter(cd_chave = cd_chave)
            else:
                clientes = Cliente.objects.filter(cd_nomcod__istartswith=form.cleaned_data['no_cliente'])

            context['clientes'] = clientes

            if clientes.count() == 0:
                messages.add_message(request, messages.INFO, 'Cliente inexistente')


    context['form'] = form

    return render(request, 
        'clientes/change_list.html',
        context
    )