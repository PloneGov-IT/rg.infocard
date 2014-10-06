# -*- coding: utf-8 -*-
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from rg.infocard import rg_infocard_msgfactory as _
from z3c.form.object import registerFactoryAdapter
from zope.interface import Interface, implementer
from zope import schema


class IInfocardComplexField(Interface):
    arg_title = schema.TextLine(
        title=_(u"title"),
        default=u"",
        required=True,
    )
    arg_value = schema.Text(
        title=_(u"value"),
        default=u"",
        required=True,
    )
    arg_public = schema.Bool(
        title=_(u"value"),
        default=False,
        required=True,
    )


@implementer(IInfocardComplexField)
class InfocardComplexField(object):

    def __str__(self):
        ''' Return the representation of thi object
        '''
        return repr(self.arg_title, self.arg_value, self.arg_public)




registerFactoryAdapter(IInfocardComplexField, InfocardComplexField)
