# -*- coding: utf-8 -*-

from odoo import models, api


class VetorPalavraTexto(models.Model):
    _description = 'Classe de manipulacao dos textos.'
    _inherit = 'vetor.palavra.texto'

    @api.model
    def create(self, vals):
        res = super(VetorPalavraTexto, self).create(vals)
        obj_vocabulario = self.env['vetor.palavra.vocabulario']
        vocabulario_id = obj_vocabulario.search([])
        vocabulario_id and vocabulario_id.write({'name': vals.get('name')}) or \
            obj_vocabulario.create({'name': vals.get('name')})
        return res
