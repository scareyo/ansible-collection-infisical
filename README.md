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

`INFISICAL_SERVICE_TOKEN`: Infisical service token for your project

## Parameters

`env (default='dev')`: The slug name of the environment from where secrets should be fetched from.

`path (default='/')`: The path from where secrets should be fetched from.

## Usage

```
- name: Print secret
  debug: msg="{{ lookup('scareyo.infisical.infisical', 'TEST_VALUE_1', 'TEST_VALUE_2') }}"

- name: Print secret specifying an environment and path
  debug: msg="{{ lookup('scareyo.infisical.infisical', 'TEST_FOLDER_VALUE', env='staging', path='/folder') }}"
```
