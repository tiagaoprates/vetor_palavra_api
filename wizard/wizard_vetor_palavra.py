# -*- coding: utf-8 -*-

from odoo import models, fields, api
ACENTUACAO_LISTA = [',', '.', ':', ';', '?', '!', '-']


class WizardVetorPalavra(models.TransientModel):
    _description = 'Classe temporaria para exibicao dos vetores e vocabularios.'
    _name = 'wizard.vetor.palavra'

    name = fields.Text(string='Resultados')

    @api.multi
    def exibe_vocabulario_isolado(self):
        obj_vocabulario = self.env['vetor.palavra.vocabulario']
        vocabulario_id = obj_vocabulario.search([])
        return self.write({'name': vocabulario_id and vocabulario_id.vocabulario_isolado or ''})

    @api.multi
    def exibe_vocabulario_2_palavra(self):
        obj_vocabulario = self.env['vetor.palavra.vocabulario']
        vocabulario_id = obj_vocabulario.search([])
        return self.write({'name': vocabulario_id and vocabulario_id.vocabulario_2_palavra or ''})

    @api.multi
    def exibe_vetor_vocabulario_isolado(self):
        vocabulario_id = self.env['vetor.palavra.vocabulario'].search([])
        vocabulario_lista = vocabulario_id and vocabulario_id.vocabulario_isolado.split(' ') or []
        if not vocabulario_lista:
            return False
        vetor_lista = []
        for texto in self.env['vetor.palavra.texto'].search([]):
            texto = ''.join(filter(lambda i: i not in ACENTUACAO_LISTA,
                                   texto.name.lower())).split(' ')
            vetor = []
            for palavra in vocabulario_lista:
                vetor.append(texto.count(palavra))
            vetor_lista.append(vetor)
        dados = ', '.join(vetor_lista)
        self.write({'name': dados})

    @api.multi
    def exibe_vetor_vocabulario_2_palavra(self):
        vocabulario_id = self.env['vetor.palavra.vocabulario'].search([])
        vocabulario_lista = vocabulario_id and vocabulario_id.vocabulario_2_palavra.split(' ') or []
        if not vocabulario_lista:
            return False
        vetor_lista = []
        for texto in self.env['vetor.palavra.texto'].search([]):
            texto = ''.join(filter(lambda i: i not in ACENTUACAO_LISTA,
                                   texto.name.lower())).split(' ')

            texto_lista = []
            aux = 0
            for palavra in texto:
                if not aux:
                    aux += 1
                    texto_lista.append(palavra + ' ' + texto[aux])
                elif texto.index(palavra) == 1:
                    continue
                else:
                    texto_lista.append(texto[aux - 1] + ' ' + palavra)
                    aux += 1
                if aux == 1:
                    aux += 1

            vetor = []
            for palavra in vocabulario_lista:
                vetor.append(texto_lista.count(palavra))
            vetor_lista.append(vetor)
        dados = ', '.join(vetor_lista)
        self.write({'name': dados})

