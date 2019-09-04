# -*- coding: utf-8 -*-

from odoo import models, fields


class VetorPalavraVocabulario(models.Model):
    _description = 'Classe de manipulacao do vacublario.'
    _name = 'vetor.palavra.vocabulario'

    name = fields.Text(string='Texto completo')
    vocabulario_isolado = fields.Text(string='Vocabulario Isolado')
    vocabulario_2_palavra = fields.Text(string='Vocabulario 2 palavras')
