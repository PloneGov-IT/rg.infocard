# -*- coding: utf-8 -*-
from .base import IInfocardComplexField
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from plone.dexterity.content import Container
from plone.directives import form
from plone.supermodel.model import Schema
from rg.infocard import rg_infocard_msgfactory as _
from zope.interface import implementer
from zope import schema


class IInfocardcontainer(Schema):
    form.model('infocardcontainer.xml')

    locations = schema.List(
        title=_(
            'label_locations',
            u"Locations"
        ),
        value_type=schema.TextLine(
            title=_(u"location", "Location")
        ),
        default=[],
        required=True,
    )
    recipients = schema.Tuple(
        title=_(
            'label_recipients',
            u"Recipients"
        ),
        value_type=schema.TextLine(
            title=_(u"recipient", "Recipient")
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


@implementer(IInfocardcontainer)
class Infocardcontainer(Container):
    '''
    Infocardcontainer class
    '''
