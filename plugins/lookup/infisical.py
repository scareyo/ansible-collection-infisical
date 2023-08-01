# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r"""
  name: infisical
  author: Sam Carey <sam@scarey.me>
  version_added: "0.1.0"
  short_description: Lookup secrets from Infisical
  description:
      - This lookup returns a value from an Infisical key
  options:
    _terms:
      description: key(s) to retreive value from
      required: True
"""

import os

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

from infisical import InfisicalClient

display = Display()
client = InfisicalClient(token=os.environ['INFISICAL_SERVICE_TOKEN'])

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        if not terms:
            raise AnsibleError("No keys specified")

        ret = []

        infisical_env = os.environ['INFISICAL_ENVIRONMENT']

        for term in terms:
            secret = client.get_secret(term, environment=infisical_env)
            ret.append(secret.secret_value)

        return ret
