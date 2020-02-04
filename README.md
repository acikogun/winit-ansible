[![Build Status](https://travis-ci.com/acikogun/winit-ansible-role.svg?branch=master)](https://travis-ci.com/acikogun/winit-ansible-role)

winit-ansible-role
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
go, docker, ansible, cloudsdk, awscli, IPython, git

Notes:
- Python3 and pip installed automatically.
- kubectl installed as a dependency to cloudsdk.


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
    - stretch
    - buster
Ubuntu:
  versions:
    - xenial
    - bionic
```

Install
--------------
```
ansible-galaxy install acikogun.winit_ansible_role
```

Example Playbook
--------------
```
---
- hosts: local
  roles:
    - acikogun.winit_ansible_role

```

Role Variables
--------------

```
# Install cloudsdk
# [true | false]
cloudsdk_enabled: true

# Install docker-ce
# [true | false]
docker_enabled: true

# Install python3 suite (python3, pip)
# [true | false]
python3_enabled: true

# Install Go
# [true | false]
go_enabled: true

# Install git
# [true | false]
git_enabled: true

# Install awscli
# [true | false]
awscli_enabled: true

# Install IPython
# [true | false]
ipython_enabled: true

# Install ansible
# [true | false]
ansible_enabled: true
```

