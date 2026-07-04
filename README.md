# Cyber Asset Discovery and Inventory Platform

Production-inspired asset discovery platform that uses AWX as the orchestration layer, Ansible for automation, Python discovery plugins for data collection, PostgreSQL for persistence, and FastAPI for the service API.

## Architecture

```text
GitHub -> CI/CD -> Docker Build -> AWX Project Sync
                                      |
                                      v
                             AWX Job Templates
                                      |
                                      v
                              Ansible Playbooks
                                      |
                                      v
                         Python Discovery Plugins
                                      |
                                      v
                          Normalize and Correlate
                                      |
                                      v
                         PostgreSQL -> FastAPI -> Dashboard
```

## Why AWX

AWX owns scheduling, credentials, RBAC, audit history, notifications, workflow templates, and the execution trail. Python modules collect and normalize data, but AWX launches and records the automation.

## Repository Layout

```text
awx/                AWX inventory, project, credential, and template definitions
ansible/            Playbooks, inventories, roles, and automation entry points
discovery/          Python discovery plugin framework and collectors
api/                FastAPI service for assets and health checks
dashboard/          Dashboard placeholder
docker/             Container build files
database/           PostgreSQL schema and seed data
tests/              Unit tests
.github/workflows/  CI pipeline
docs/               Architecture and operating notes
```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
uvicorn api.app.main:app --reload
```

Or run the starter stack:

```bash
docker compose up --build
```

## Initial Workflow

1. AWX syncs this Git repository as a project.
2. AWX launches job templates for discovery, enrichment, correlation, and reporting.
3. Ansible playbooks call Python discovery modules.
4. Results are normalized and stored in PostgreSQL.
5. FastAPI exposes inventory data to the dashboard and integrations.

## Roadmap

- Add real Nmap, DNS, SNMP, SMB, and SSL collectors.
- Add AWX workflow template export/import automation.
- Add asset change tracking and deduplication rules.
- Add dashboard views for assets, services, certificates, and risk signals.
- Add cloud and virtualization discovery plugins.
