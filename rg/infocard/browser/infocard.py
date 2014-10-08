# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.dexterity.browser.add import DefaultAddView
from plone.dexterity.browser.edit import DefaultEditView


class AddView(DefaultAddView):
    ''' Custom form for infocardcontainer add form
    '''
    index = ViewPageTemplateFile('templates/rg.infocard.layout.pt')


class EditView(DefaultEditView):
    ''' Custom form for infocardcontainer edit form
    '''
    index = ViewPageTemplateFile('templates/rg.infocard.layout.pt')
