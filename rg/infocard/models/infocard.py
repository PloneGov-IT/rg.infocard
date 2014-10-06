# -*- coding: utf-8 -*-
from .base import IInfocardComplexField
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from plone.supermodel.model import Schema
from plone.dexterity.content import Container
from plone.directives import form
from rg.infocard import rg_infocard_msgfactory as _
from rg.infocard.vocs.infocard_locations import InfocardLocations
from rg.infocard.vocs.infocard_recipients import InfocardRecipients
from zope.interface import implementer
from zope import schema


class IInfocard(Schema):
    form.model('infocard.xml')
    locations = schema.Tuple(
        title=_(
            'label_locations',
            u"Locations"
        ),
        value_type=schema.Choice(
            source=InfocardLocations
        ),
        default=(),
        required=True,
    )
    recipients = schema.Tuple(
        title=_(
            'label_recipients',
            u"Recipients"
        ),
        value_type=schema.Choice(
            source=InfocardRecipients,
        ),
        default=(),
        required=True,
    )
    default_args = schema.List(
        title=_(
            'label_default_infos',
            u"List of default informations"
        ),
        value_type=DictRow(
            title=_(u"infocard_info", "Info"),
            schema=IInfocardComplexField,
        ),
        required=False,
        default=[],
        missing_value=[]
    )
    form.widget(default_args=DataGridFieldFactory)


@form.default_value(field=IInfocard['default_args'])
def default_default_args(data):
    ''' Use the parent default_args
    '''
    from rg.infocard.models.infocardcontainer import Infocardcontainer
    for obj in data.context.aq_chain:
        if isinstance(obj, Infocardcontainer):
            return obj.default_args
    return []


@implementer(IInfocard)
class Infocard(Container):
    '''
    Infocard class
    '''
