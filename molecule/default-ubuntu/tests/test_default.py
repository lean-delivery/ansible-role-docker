import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_package_is_installed(host):
    docker_pkg = host.package("docker-ce")
    assert docker_pkg.is_installed
    assert docker_pkg.version.startswith("18.03.1")


def test_docker_service_running_and_enabled(host):
    docker_svc = host.service("docker")
    assert docker_svc.is_running
    assert docker_svc.is_enabled
