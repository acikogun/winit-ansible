[![Build Status](https://travis-ci.com/acikogun/wsprov-ansible-role.svg?branch=master)](https://travis-ci.com/acikogun/wsprov-ansible-role)

wsprov-ansible-role
=========
Ansible role for [wsprov](https://github.com/acikogun/wsprov) that is a collection of installer bash scripts for tools I use on my development workstation.

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
Debian:
  versions:
    - stretch
    - buster
Ubuntu:
  versions:
    - xenial
    - bionic
Fedora:
  versions:
    - 30
```

Role Variables
--------------

A description of the settable variables for this role should go here, including
any variables that are in defaults/main.yml, vars/main.yml, and any variables
that can/should be set via parameters to the role. Any variables that are read
from other roles and/or the global scope (ie. hostvars, group vars, etc.) should
be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables that
are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: workspace-installer-ansible-role, x: 42 }


Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
