# Ansible Collection - scareyo.infisical

An Ansible collection for Infisical lookups

## Installation

```
pip install infisical --user
```

```
ansible-galaxy collection install scareyo.infisical
```

## Environment variables

```INFISICAL_SERVICE_TOKEN```: Infisical service token for your project

## Usage

```
- name: Print secret
  debug: msg="{{ lookup('scareyo.infisical.infisical', 'TEST_VALUE_1', 'TEST_VALUE_2') }}"
```
