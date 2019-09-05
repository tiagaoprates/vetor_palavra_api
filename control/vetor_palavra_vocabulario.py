# -*- coding: utf-8 -*-

from odoo import models, api
from collections import OrderedDict
ACENTUACAO_LISTA = [',', '.', ':', ';', '?', '!', '-']


class VetorPalavraVocabulario(models.Model):
    _description = 'Classe de manipulacao do vocabulario.'
    _inherit = 'vetor.palavra.vocabulario'

    @api.model
    def create(self, vals):
        vals = self.gerar_vocabulario(vals)
        return super(VetorPalavraVocabulario, self).create(vals)

    @api.model
    def write(self, vals):
        vals.update({'name': self.read(['name'])[0].get('name') + ' ' + vals.get('name')})
        vals = self.gerar_vocabulario(vals)
        return super(VetorPalavraVocabulario, self).writecreate(vals)

    @api.multi
    def gerar_vocabulario(self, vals):
        vals.update({'vocabulario_isolado': self.gerar_vocabulario_isolado(vals.get('name')),
                     'vocabulario_2_palavra': self.gerar_vocabulario_2_palavra(vals.get('name'))})
        return vals

    @api.multi
    def gerar_vocabulario_isolado(self, texto):
        lista_palavra = ''.join(filter(lambda i: i not in ACENTUACAO_LISTA,
                                       texto.lower())).split(' ')
        lista_palavra = list(OrderedDict.fromkeys(lista_palavra))
        vocabulario = ' '.join(lista_palavra)
        return vocabulario

    @api.multi
    def gerar_vocabulario_2_palavra(self, texto):
        lista_palavra = ''.join(filter(lambda i: i not in ACENTUACAO_LISTA,
                                       texto.lower())).split(' ')
        vocabulario_lista = []
        aux = 0
        for palavra in lista_palavra:
            if not aux:
                aux += 1
                vocabulario_lista.append(palavra + ' ' + lista_palavra[aux])
            elif lista_palavra.index(palavra) == 1:
                continue
            else:
                vocabulario_lista.append(lista_palavra[aux - 1] + ' ' + palavra)
                aux += 1
            if aux == 1:
                aux += 1
        vocabulario = ' '.join(vocabulario_lista)
        return vocabulario
