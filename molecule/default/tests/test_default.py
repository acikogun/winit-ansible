import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_python3_is_installed(host):
    py3 = """python3 -V"""
    cmd = host.run(py3)
    assert 'Python' in cmd.stdout


def test_docker_is_installed(host):
    docker = host.package("docker-ce")
    assert docker.is_installed


def test_docker_running_and_enabled(host):
    docker_service = host.service("docker")
    assert docker_service.is_running
    assert docker_service.is_enabled


def test_git_is_installed(host):
    git = host.package("git")
    assert git.is_installed


def test_go_is_installed(host):
    go = """go version"""
    cmd = host.run(go)
    assert 'linux/amd64' in cmd.stdout


def test_gcloud_is_installed(host):
    gcloud = """gcloud --version"""
    cmd = host.run(gcloud)
    assert 'Google Cloud SDK' in cmd.stdout


def test_awscli_is_installed(host):
    aws = """aws --version"""
    cmd = host.run(aws)
    assert 'aws-cli' in cmd.stdout


def test_ansible_is_installed(host):
    ansible = """ansible --version"""
    cmd = host.run(ansible)
    assert 'python version' in cmd.stdout


def test_ipython_is_installed(host):
    ipython = """ipython --help"""
    cmd = host.run(ipython)
    assert 'IPython' in cmd.stdout


def test_bash_completion_files(host):
    assert host.file('/etc/profile.d/kubectl_bash_completion.sh').exists
    assert host.file('/etc/profile.d/pip_bash_completion.sh').exists
    assert host.file('/etc/profile.d/awscli_bash_completion.sh').exists
