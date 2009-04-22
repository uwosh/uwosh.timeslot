from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from uwosh.timeslot import timeslotMessageFactory as _


class ISignupResults(Interface):
    """
    ChooseTimeSlot view interface
    """
    

class SignupResults(BrowserView):
    """
    ChooseTimeSlot browser view
    """
    implements(ISignupResults)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def wasSignupSuccessful(self):
        success = self.request.get('success')
        return bool(int(success))
    
    def wasAddedToWaitingList(self):
        waiting = self.request.get('waiting')
        return bool(int(waiting))
        