import urllib
import urllib2
import urlparse
import logging
import paymill

from lxml import etree
from zExceptions import Redirect
from zope.i18nmessageid import MessageFactory
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from zope.interface import alsoProvides
from zope import schema
from plone.supermodel import model

from zope.interface import Interface
from zope.interface import provider

from bda.plone.payment.interfaces import IPaymentData
from bda.plone.payment import Payment
from bda.plone.payment import Payments

from bda.plone.shop import message_factory as _

from bda.plone.shop.interfaces import IShopSettings
from bda.plone.shop.interfaces import IShopSettingsProvider

logger = logging.getLogger('bda.plone.payment')
_ = MessageFactory('bda.plone.payment')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""


    
#from zope.interface import Attribute


#testkey
paymill_context = paymill.PaymillContext('06fc8133e9a5fe5e7fac12847270541d')    


@provider(IShopSettingsProvider)
class IPaymillPaymentSettings(model.Schema):
    
    model.fieldset('paymill',label=_(u'Paymill', default=u'Paymill'),
        fields=[
        'paymill_server_url',
        'paymill_private_key',
        'paymill_public_key',
        ],
    )
                   
    paymill_server_url = schema.ASCIILine(title=_(u'paymill_server_url', default=u'Server URL'),
                 required=True
    )

    paymill_public_key = schema.ASCIILine(title=_(u'paymill_private_key', default=u'Paymill public key'),
               required=True
    )
    
    paymill_private_key = schema.ASCIILine(title=_(u'paymill_public_key', default=u'Paymill private key'),
               required=True
    )

alsoProvides(IPaymillPaymentSettings, IShopSettingsProvider)
