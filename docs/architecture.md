# Architecture Notes

AWX is the orchestration boundary. It launches Ansible playbooks, manages credentials, stores job history, and exposes an API for scheduling and audit.

Discovery plugins are isolated Python collectors. They should return normalized `DiscoveredAsset` models so correlation and persistence can evolve without rewriting collectors.

The platform should tolerate partial discovery failures. For example, an SNMP timeout should be logged and attached to job results without blocking DNS, SSL, SMB, or reporting stages.

## Initial AWX Job Templates

- Discover Network
- DNS Enrichment
- SNMP Collection
- SSL Collection
- SMB Collection
- Asset Correlation
- Inventory Update
- Generate Reports
