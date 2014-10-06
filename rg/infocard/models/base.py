# -*- coding: utf-8 -*-
from rg.infocard import rg_infocard_msgfactory as _
from zope.interface import Interface
from zope import schema
from plone.app.textfield import RichText


class IInfocardComplexField(Interface):
    arg_title = schema.TextLine(
        title=_("infocard_complex_field_title", "Label"),
        default=u"",
        required=True,
    )
    arg_value = schema.Text(
        title=_("infocard_complex_field_value", "Value"),
        default=u"",
#        default_mime_type='text/structured',
#        output_mime_type='text/html',
#        allowed_mime_types=('text/structured', 'text/plain',),
        required=False,
    )
    arg_public = schema.Bool(
        title=_("infocard_complex_field_public", "Public?"),
        default=False,
        required=True,
    )
