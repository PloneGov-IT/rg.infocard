# -*- coding: utf-8 -*-
from collective.z3cform.datagridfield.blockdatagridfield import BlockDataGridField  # noqa
from plone.app.textfield import RichText
from rg.infocard import rg_infocard_msgfactory as _
from z3c.form.interfaces import IFieldWidget, IFormLayer
from z3c.form.widget import FieldWidget
from zope.interface import Interface
from zope import schema
from zope.component import adapter
from zope.interface import implementer


class InfocardDataGridField(BlockDataGridField):
    ''' Like its parent but with allow_reorder
    '''
    allow_reorder = True


@adapter(schema.interfaces.IField, IFormLayer)
@implementer(IFieldWidget)
def InfocardDataGridFieldFactory(field, request):
    """IFieldWidget factory for DataGridField."""
    return FieldWidget(field, InfocardDataGridField(request))


class IInfocardComplexField(Interface):
    arg_title = schema.TextLine(
        title=_("infocard_complex_field_title", "Label"),
        default=u"",
        required=True,
    )
    arg_public = schema.Bool(
        title=_("infocard_complex_field_public", "Public?"),
        default=False,
        required=True,
    )
    arg_value = RichText(
        title=_("infocard_complex_field_value", "Value"),
        default=u"",
        required=False,
    )
