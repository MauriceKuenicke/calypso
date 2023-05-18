# Pre-Commit Hooks

## **Introduction**
-------------------------------

Pre-commit hooks are scripts that are run before a commit is made in a version control system. These hooks can be used to perform a variety of tasks, such as linting code, formatting code, and running tests, among others. The purpose of this page is to guide you through the process of setting up pre-commit hooks for this project.

## **Installing Pre-Commit**
-------------------------------

The first step is to install pre-commit. You can install pre-commit using pip. To install pre-commit, run the following command:

```sh
pip install pre-commit
```

## **Pre-commit Configuration File**
-------------------------------

The project contains a configuration file named `.pre-commit-config.yaml` in the root directory. This file contains the tools and basic configurations for them that will be used
when running the hooks. Following hooks are currently being used:

- [x] **black**
- [x] **flake8**
- [x] **isort**
- [x] **mypy**
- [x] **pydocstyle**
- [x] **check-yaml**

## **Installing Pre-commit Hooks**
-------------------------------

```sh
pre-commit install
```

This command will install the hooks specified in the pre-commit configuration file. Whenever you make a commit, pre-commit will run the specified hooks before allowing the commit to proceed.