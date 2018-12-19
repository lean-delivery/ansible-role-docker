docker role
=========

[![License](https://img.shields.io/badge/license-Apache-green.svg?style=flat)](https://raw.githubusercontent.com/lean-delivery/ansible-role-docker/master/LICENSE)
[![build status](https://travis-ci.org/lean-delivery/ansible-role-gitlab.svg?branch=master)](https://travis-ci.org/lean-delivery/ansible-role-docker)
[![Galaxy](https://img.shields.io/badge/galaxy-lean__delivery.docker-blue.svg)](https://galaxy.ansible.com/lean_delivery/docker)
![Ansible](https://img.shields.io/ansible/role/d/28987.svg)
![Ansible](https://img.shields.io/badge/dynamic/json.svg?label=min_ansible_version&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F28987%2F&query=$.min_ansible_version)

## Summary

This Ansible role has the following features:

 - Install docker-ce

Requirements
------------

 - Version of the ansible for installation: 2.5
 - **Supported OS**:  
   - EL
     - 7
   - Ubuntu
     - 18.04

## Role Variables

- required
  - `docker_version`  
  Specific version of Docker CE. Default value is `18.06`.

- defaults
  - `docker_storage_driver`  
  Docker storage driver. Default value is `overlay2`
  - `docker_users`  
  Adding a users to the "docker" group. Default value is `ansible_user_id`
  - `packages_base_yum`  
  Install required packages for RedHat. Default value is `yum-utils, device-mapper-persistent-data, lvm2`
  - `packages_base_apt`  
  Install required packages for Debian. Default value is `apt-transport-https, ca-certificates, curl, software-properties-common`
  - `packages_additional`  
  Install additional packages for all installs. Default value is `[]`
  - `docker_apt_repo`  
  Stable repository for Debian. Default value is `deb [arch=amd64] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} stable`
  - `docker_apt_pgp`  
  GPG key for Debian. Default value is `https://download.docker.com/linux/ubuntu/gpg`
  - `docker_yum_repo`  
  Stable repository for Redhat. Default value is `https://download.docker.com/linux/centos/7/$basearch/stable`
  - `docker_yum_gpg`  
  GPG key for Redhat. Default value is `https://download.docker.com/linux/centos/gpg`

## Some examples of the installing current role

ansible-galaxy install lean_delivery.docker

Example Playbook
----------------

### Installing docker-ce to centos 7:
```yaml
- name: Converge
  hosts: all
  roles:
    - role: lean_delivery.docker
```

### Installing docker-ce to ubuntu 18.04:
```yaml
- name: Converge
  hosts: all
  roles:
    - role: lean_delivery.docker
      vars:
        docker_version: "18.03.1"
```

### Installing docker-ce to centos 7 with vfs driver:
```yaml
- name: Converge
  hosts: all
  roles:
    - role: lean_delivery.docker
      vars:
        docker_storage_driver: vfs
```

License
-------

Apache

Author Information
------------------

authors:
  - Lean Delivery <team@lean-delivery.com>
