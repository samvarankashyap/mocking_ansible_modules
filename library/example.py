#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *

# This is a simplified module which takes path as ansible variable 
# and returns it back to with Results
if __name__ == '__main__':
    global module
    module = AnsibleModule(
        argument_spec={
            'path': { 'required': True, 'type': 'str' }
        },
        supports_check_mode=False
    )

    args = module.params
    orig_file = args['path']       
    result = {"Results": "This is the result", "path": orig_file}
    module.exit_json(**result)
