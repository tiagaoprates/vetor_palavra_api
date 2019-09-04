# -*- coding: utf-8 -*-

from odoo import models, api


class VetorPalavraVocabulario(models.Model):
    _description = 'Classe de manipulacao do vocabulario.'
    _inherit = 'vetor.palavra.vocabulario'

    @api.model
    def create(self, vals):
        vals = self.generate_vocabulary(vals)
        return super(VetorPalavraVocabulario, self).create(vals)

    @api.model
    def write(self, vals):
        vals.update({'name': self.read(['name'])[0].get('name') + ' ' + vals.get('name')})
        vals = self.generate_vocabulary(vals)
        return super(VetorPalavraVocabulario, self).writecreate(vals)

    @api.multi
    def generate_vocabulary(self, vals):
        vals.update({'vocabulario_isolado': '',
                     'vocabulario_2_palavra': ''})
        return vals
