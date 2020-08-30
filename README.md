[![Build Status](https://travis-ci.com/acikogun/winit-ansible.svg?branch=master)](https://travis-ci.com/acikogun/winit-ansible)

winit-ansible
=========
Ansible role for [winit](https://github.com/acikogun/winit) that is a collection of installer bash scripts for tools I use on my development workstation.


  - [Available tools](#available-tools)
  - [Requirements](#requirements)
  - [Supported platforms](#supported-platforms)
  - [Install](#install)
  - [Example Playbook](#example-playbook)
  - [Role Variables](#role-variables)

Available tools
------------

- ansible
- awscli
- azurecli
- cloudsdk
- docker
- docker-compose
- eksctl
- go
- helm
- ipython
- java8
- java11
- node
- packer
- shellcheck
- terraform
- vagrant


Notes:
-  **git**, **python3**, **pip**, **virtualenv** and **ipython** are installed as
requirements before any tool.
-  **node** version is LTS(Erbium). **npm** and **yarn** are installed as dependencies.
-  **cloudsdk** installs **kubectl** as dependency.
-  **docker** installs **docker-compose** as dependency.
-  bash completion is enabled for **aws**, **kubectl**, **helm**, **eksctl** and **npm**.


Requirements
------------

This role was developed using Ansible 2.8.4. Backwards compatibility is not guaranteed.


Supported platforms
------------

Note: Only linux/amd64 is supported.

```yaml
CentOS:
  versions:
    - 7
    - 8
Debian:
  versions:
    - 9 (stretch)
    - 10 (buster)
Ubuntu:
  versions:
    - 16 (xenial
    - 18 (bionic)
```

Install
--------------

```bash
ansible-galaxy install acikogun.winit
```

Example Playbook
--------------

```yaml
---
- hosts: local
  roles:
    - acikogun.winit

```

Role Variables
--------------

```yaml
# Install cloudsdk
# [true | false]
cloudsdk_enabled: true

# Install azurecli
# [true | false]
azurecli_enabled: true

# Install docker-ce
# [true | false]
docker_enabled: true

# Install Go
# [true | false]
go_enabled: true

# Install awscli
# [true | false]
awscli_enabled: true

# Install ansible
# [true | false]
ansible_enabled: true

# Install nodejs
# [true | false]
nodejs_enabled: true

# Install java
# [true | false]
java_enabled: true

# Install terraform
# [true | false]
terraform_enabled: true

# Install packer
# [true | false]
packer_enabled: true

# Install vagrant
# [true | false]
vagrant_enabled: true

# Install docker-compose
# [true | false]
docker_compose_enabled: true

# Install eksctl
# [true | false]
eksctl_enabled: true

# Install helm
# [true | false]
helm_enabled: true

# Install helm
# [true | false]
shellcheck_enabled: true


```
