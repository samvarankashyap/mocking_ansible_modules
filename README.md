# Example implementation of ansible mocking using 
# action plugins

## Usage

When you run ansible-playbook with extra-vars linchpin-mock=true
it returns mocked value of example else it would return actual value of module

example run without linchpin_mock
```
ansible-playbook -vvvv test_example.yaml
```
output:
```
[@localhost test_action_plugins]$ ansible-playbook -vv test_example.yml 
No config file found; using defaults
[WARNING]: No inventory was parsed, only implicit localhost is available

[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'


PLAYBOOK: test_example.yml ***************************************************************************************************************************************
1 plays in test_example.yml

PLAY [localhost] *************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************
task path: /home/srallaba/workspace/lp_ws_backup/lp_ws/test_action_plugins/test_example.yml:1
ok: [localhost]
META: ran handlers

TASK [Run example module with path var] **************************************************************************************************************************
task path: /home/srallaba/workspace/lp_ws_backup/lp_ws/test_action_plugins/test_example.yml:3
ok: [localhost] => {"Results": "This is the result", "changed": false, "gid": 0, "group": "root", "mode": "0755", "owner": "root", "path": "/etc/default", "size": 4096, "state": "directory", "uid": 0}
META: ran handlers
META: ran handlers

PLAY RECAP *******************************************************************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Action plugin ran with mocked output

ansible-playbook -vvvv test_example.yaml -e"linchpin_mock=true"

output:
```
[@localhost test_action_plugins]$ ansible-playbook -vv test_example.yml -e"linchpin_mock=true"
No config file found; using defaults
[WARNING]: No inventory was parsed, only implicit localhost is available

[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'


PLAYBOOK: test_example.yml ***************************************************************************************************************************************
1 plays in test_example.yml

PLAY [localhost] *************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************
task path: /home/srallaba/workspace/lp_ws_backup/lp_ws/test_action_plugins/test_example.yml:1
ok: [localhost]
META: ran handlers

TASK [Run example module with path var] **************************************************************************************************************************
task path: /home/srallaba/workspace/lp_ws_backup/lp_ws/test_action_plugins/test_example.yml:3
ok: [localhost] => {"changed": false, "result": "This is a mocked result that can be used for testing"}
META: ran handlers
META: ran handlers

PLAY RECAP *******************************************************************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
This action plugin can be implemented to any ansible module by just 
renaming it to the appropriate module name.

