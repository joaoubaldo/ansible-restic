import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

version = '0.8.0'
def test_restic(host):
    f = host.file('/usr/local/bin/restic')

    assert f.exists
    assert f.is_symlink
    assert f.user == 'root'
    assert f.group == 'root'

    linked = f.linked_to
    fl = host.file(f.linked_to)
    assert linked == '/opt/restic/bin/restic-'+version
    assert fl.user == 'root'
    assert fl.group == 'root'
    assert fl.mode == 0o755
