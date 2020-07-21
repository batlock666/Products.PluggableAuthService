import unittest

from Products.PluggableAuthService.tests.conformance import IAuthenticationPlugin_conformance  # NOQA
from Products.PluggableAuthService.tests.conformance import ICredentialsResetPlugin_conformance  # NOQA
from Products.PluggableAuthService.tests.conformance import ICredentialsUpdatePlugin_conformance  # NOQA
from Products.PluggableAuthService.tests.conformance import IRolesPlugin_conformance  # NOQA


class DelegatingMultiPluginTests(
        unittest.TestCase,
        IAuthenticationPlugin_conformance,
        IRolesPlugin_conformance,
        ICredentialsResetPlugin_conformance,
        ICredentialsUpdatePlugin_conformance):

    def _getTargetClass(self):
        from Products.PluggableAuthService.plugins.DelegatingMultiPlugin import DelegatingMultiPlugin  # NOQA

        return DelegatingMultiPlugin

    def _makeOne(self, id='test', *args, **kw):
        return self._getTargetClass()(id=id, *args, **kw)
