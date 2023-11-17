import re
from unidecode import unidecode


intencao = [['Atualizar-Pagamento', r'([Aa]tualiz[ao](r)?|[Mm]uda(r)?)', r'([Pp]agamento|[Cc]artao de credito)', r'([Cc]omo|[Pp]reciso|[Qq]uero|\?)'],
            ['Status-Pedido', r'([Ss]tatus|[Oo]nde|[Rr]astrear)',r'([Pp]edido|[Ee]ntrega)'],
            ['Ola', r'([Oo](i|l[áa]))']
            ]

resposta = {'Atualizar-Pagamento': 'Para atualizar o seu matodo de pagamento, abra o menu e selecione atualizar metodo de pagamento',
            'Status-Pedido': "Para acampanhar o status do seu pedido aperte o botão status do pedido no menu",
             "N":"Não entendi, tente perguntar de outra forma",
             'Ola': "Oi, tudo bem? Como posso te ajudar?"
             }

def defInt(acao):
    for i in intencao:
        mVal = 0
        for n in i:
            teste = re.search(n, acao)
            if re.search(n, acao):
                mVal += 1
            if mVal == (len(i)-1):
                return(i[0])
    return('N')            

while True:
    acao = input()
    if re.fullmatch('[Ss]air', acao):
        break
    print(resposta[defInt(unidecode(acao))])
