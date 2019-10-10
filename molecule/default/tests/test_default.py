import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_python3_installed(host):
    py3 = """python3 -V"""
    cmd = host.run(py3)
    assert 'Python 3' in cmd.stdout


def test_pip3_installed(host):
    pip3 = """pip3 -V"""
    cmd = host.run(pip3)
    assert 'python 3' in cmd.stdout


def test_git_installed(host):
    git = host.package("git")
    assert git.is_installed


def test_docker_installed(host):
    docker = host.package("docker-ce")
    assert docker.is_installed


def test_go_installed(host):
    go = """go version"""
    cmd = host.run(go)
    assert 'go version' in cmd.stdout
    assert 'linux/amd64' in cmd.stdout


def test_gcloud_installed(host):
    gcloud = """gcloud -v"""
    cmd = host.run(gcloud)
    assert 'Google Cloud SDK' in cmd.stdout
    assert 'kubectl' in cmd.stdout


def test_awscli_installed(host):
    aws = """aws --version"""
    cmd = host.run(aws)
    assert 'aws-cli' in cmd.stdout
    assert 'Python/3' in cmd.stdout


def test_ansible_installed(host):
    ansible = """ansible --version"""
    cmd = host.run(ansible)
    assert 'ansible' in cmd.stdout
    assert 'python version = 3' in cmd.stdout


def test_ipython_installed(host):
    ipython = """ipython --help"""
    cmd = host.run(ipython)
    assert 'IPython' in cmd.stdout


def test_bash_completion_files(host):
    assert host.file('/etc/profile.d/kubectl_bash_completion.sh').exists
    assert host.file('/etc/profile.d/pip_bash_completion.sh').exists
    assert host.file('/etc/profile.d/awscli_bash_completion.sh').exists
