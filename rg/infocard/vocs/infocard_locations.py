# -*- coding: utf-8 -*-
from .base import SimpleSafeVocabulary
from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm


@grok.provider(IContextSourceBinder)
def InfocardLocations(context):
    '''
    Get the locations from the parent infocardcontainer

    :param context: a Plone object
    '''
    terms = []
    from rg.infocard.models.infocardcontainer import Infocardcontainer
    for obj in context.aq_chain:
        if isinstance(obj, Infocardcontainer):
            values = set([x.strip() for x in obj.locations if x.strip()])
            values = sorted(values)
            [terms.append(SimpleTerm(value)) for value in values]
    terms.sort(key=lambda x: x.title)
    return SimpleSafeVocabulary(terms)
