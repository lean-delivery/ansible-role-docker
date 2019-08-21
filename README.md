docker role
=========

[![License](https://img.shields.io/badge/license-Apache-green.svg?style=flat)](https://raw.githubusercontent.com/lean-delivery/ansible-role-docker/master/LICENSE)
[![build status](https://travis-ci.org/lean-delivery/ansible-role-docker.svg?branch=master)](https://travis-ci.org/lean-delivery/ansible-role-docker)
[![Build Status](https://gitlab.com/lean-delivery/ansible-role-docker/badges/master/pipeline.svg)](https://gitlab.com/lean-delivery/ansible-role-docker/pipelines)
[![Galaxy](https://img.shields.io/badge/galaxy-lean__delivery.docker-blue.svg)](https://galaxy.ansible.com/lean_delivery/docker)
![Ansible](https://img.shields.io/ansible/role/d/28987.svg)
![Ansible](https://img.shields.io/badge/dynamic/json.svg?label=min_ansible_version&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F28987%2F&query=$.min_ansible_version)

## Summary

This Ansible role has the following features:

 - Install docker-ce

Requirements
------------

 - Version of the ansible for installation: >=2.7
 - **Supported OS**:  
   - EL
     - 7
   - Ubuntu
     - 18.04
   - Debian
     - stretch
   - Amazon Linux 2

## Role Variables

- required
  - `docker_version`  
  Specific version of Docker CE. Default value is `18.06`.

- defaults
  - `docker_storage_driver`  
  Docker storage driver. Default value is `overlay2`
  - `docker_users`  
  Adding a users to the "docker" group. Default value is `ansible_user_id`
  - `docker_packages_additional`   
    Install additional packages for all installs. Default value is `[]`
  - `docker_repo`   
    Repository for docker packages. Default value depends on OS family:   
      * Debian: `deb [arch=amd64] https://download.docker.com/linux/{{ ansible_distribution | lower }} {{ ansible_distribution_release }} stable`   
      * RedHat: `https://download.docker.com/linux/centos/7/$basearch/stable`
  - `docker_gpg`  
    GPG key for Debian/RedHat repos. Default value is:
      * Debian: `https://download.docker.com/linux/{{ ansible_distribution | lower }}/gpg`
      * RedHat: `https://download.docker.com/linux/centos/gpg`

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
    docker_version: 19.03
```

### Installing docker-ce to centos 7 with overlay2 driver and custom data root:
```yaml
- name: Converge
  hosts: all
  roles:
    - role: lean_delivery.docker
  vars:
    daemon_conf:
      storage-driver: overlay2
      data-root: /mnt/volume/docker
```

License
-------

Apache

Author Information
------------------

authors:
  - Lean Delivery <team@lean-delivery.com>
