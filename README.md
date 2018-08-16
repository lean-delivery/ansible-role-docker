docker role
=========

[![License](https://img.shields.io/badge/license-Apache-green.svg?style=flat)](https://raw.githubusercontent.com/lean-delivery/ansible-role-docker  /master/LICENSE)
[![build status](https://git.epam.com/dip-roles/ansible-role-docker/badges/master/build.svg)](https://git.epam.com/dip-roles/ansible-role-docker/pipelines)

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
    - role: ansible-role-docker
```

### Installing docker-ce to ubuntu 18.04:
```yaml
- name: Converge
  hosts: all
  roles:
    - role: ansible-role-docker
      vars:
        docker_version: "18.03.1"
```

### Installing docker-ce to centos 7 with vfs driver:
```yaml
- name: Converge
  hosts: all
  roles:
    - role: ansible-role-docker
      vars:
        docker_storage_driver: vfs
```

License
-------

Apache2

Author Information
------------------

authors:
  - Lean Delivery <team@lean-delivery.com>
