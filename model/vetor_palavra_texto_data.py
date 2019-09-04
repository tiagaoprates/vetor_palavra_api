# -*- coding: utf-8 -*-

from odoo import models, fields


class VetorPalavraTexto(models.Model):
    _description = 'Classe de manipulacao dos textos.'
    _name = 'vetor.palavra.texto'

    name = fields.Text(string='Texto', required=True)
