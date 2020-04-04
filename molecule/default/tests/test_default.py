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


def test_azurecli_installed(host):
    az = """az version"""
    cmd = host.run(az)
    assert 'azure-cli' in cmd.stdout


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


def test_java_installed(host):
    java = """java -version 2>&1"""
    cmd = host.run(java)
    assert 'openjdk' in cmd.stdout
    assert 'AdoptOpenJDK' in cmd.stdout


def test_nodejs_installed(host):
    nodejs = """node -v"""
    cmd = host.run(nodejs)
    assert 'v12' in cmd.stdout


def test_npm_installed(host):
    npm = """npm help"""
    cmd = host.run(npm)
    assert 'Usage: npm ' in cmd.stdout


def test_yarn_installed(host):
    yarn = """yarn versions"""
    cmd = host.run(yarn)
    assert 'yarn' in cmd.stdout
    assert 'node' in cmd.stdout
    assert 'v8' in cmd.stdout


def test_terraform_installed(host):
    terraform = """/usr/bin/terraform -v"""
    cmd = host.run(terraform)
    assert 'Terraform' in cmd.stdout


def test_packer_installed(host):
    packer = """/usr/bin/packer -h"""
    cmd = host.run(packer)
    assert 'Usage: packer' in cmd.stdout


def test_vagrant_installed(host):
    """
    I don't test by executing vagrant like terraform and packer
    because it doesn't work properly in containers.
    """
    assert host.file('/usr/bin/vagrant').exists


def test_docker_compose_installed(host):
    compose = """/usr/bin/docker-compose -v"""
    cmd = host.run(compose)
    assert 'docker-compose version' in cmd.stdout


def test_eksctl_installed(host):
    eksctl = """/usr/bin/eksctl help version"""
    cmd = host.run(eksctl)
    assert 'Usage: eksctl version' in cmd.stdout


def test_helm_installed(host):
    helm = """/usr/bin/helm version"""
    cmd = host.run(helm)
    assert 'Version' in cmd.stdout
    assert 'GoVersion' in cmd.stdout


def test_shellcheck_installed(host):
    shellcheck = """/usr/bin/shellcheck -V"""
    cmd = host.run(shellcheck)
    assert 'ShellCheck - shell script analysis tool' in cmd.stdout


def test_bash_completion_files(host):
    assert host.file('/etc/profile.d/kubectl_bash.sh').exists
    assert host.file('/etc/profile.d/pip_bash.sh').exists
    assert host.file('/etc/profile.d/awscli_bash.sh').exists
    assert host.file('/etc/profile.d/eksctl_bash.sh').exists
    assert host.file('/etc/profile.d/helm_bash.sh').exists
    assert host.file('/etc/profile.d/npm_bash.sh').exists
