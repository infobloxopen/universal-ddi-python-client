# Changelog

All notable changes to the Universal DDI Python Client will be documented in this file.

## [v0.2.0](https://github.com/infobloxopen/universal-ddi-python-client/releases/tag/v0.2.0) (2026-07-16)

### New Features

- **[DNS Traffic Control]** Added full support for the DTC (DNS Traffic Control) API ([#30](https://github.com/infobloxopen/universal-ddi-python-client/pull/30), [#38](https://github.com/infobloxopen/universal-ddi-python-client/pull/38)):
   - CRUD operations for Pools
   - CRUD operations for Servers
   - HTTP, ICMP, TCP, PDP, and SIP Health Checks
   - Topology
- **[DNS Configuration]** Added support for LBDN object ([#35](https://github.com/infobloxopen/universal-ddi-python-client/pull/35))
- **[DNS Data]** Added record protection support for DNS records ([#36](https://github.com/infobloxopen/universal-ddi-python-client/pull/36))

### Improvements

- **[DNS Configuration]** Added `compartment_id` field to `ACL`, `AuthZone`, `ForwardZone`, `View`, and `AuthNsg` models ([#35](https://github.com/infobloxopen/universal-ddi-python-client/pull/35))
- **[IPAM]** Updated `DHCPConfig` and `InheritedDHCPConfig` models with new fields (`hold_reclaimed_time`, `authoritative_dhcp`, and others) to align with the latest IPAM API schema ([#44](https://github.com/infobloxopen/universal-ddi-python-client/pull/44))

### Fixes

- **[DNS Data]** Set `name_in_zone` to default `None` on the `Record` model and added `compartment_id` field to DNS record types ([#37](https://github.com/infobloxopen/universal-ddi-python-client/pull/37))
   - Fixes [#28](https://github.com/infobloxopen/universal-ddi-python-client/issues/28): Unable to create DNS records: required record name fields are absent despite providing required fields.
   - Fixes [#29](https://github.com/infobloxopen/universal-ddi-python-client/issues/29): Record.to_dict() includes name_in_zone: "" default which conflicts with absolute_name_spec.
- **[Cloud Discovery]** Updated Cloud Discovery schemas to include zone filters and related fields ([#51](https://github.com/infobloxopen/universal-ddi-python-client/pull/51))

### Maintenance

- Updated minimum supported Python version from 3.8 to 3.10 ([#45](https://github.com/infobloxopen/universal-ddi-python-client/pull/45))

## [v0.1.1](https://github.com/infobloxopen/universal-ddi-python-client/releases/tag/v0.1.1) (2025-04-28)

### Fixes

- **[IPAM]** Updated Fixed Address to set `Address` as an optional field ([#23](https://github.com/infobloxopen/universal-ddi-python-client/pull/23))
- **[Cloud Discovery]** Updated Providers to set `Source Config ID` as an optional field ([#24](https://github.com/infobloxopen/universal-ddi-python-client/pull/24))

### Improvements

- Added environment variable support for Debug operations ([#25](https://github.com/infobloxopen/universal-ddi-python-client/pull/25))

### Maintenance

- Updated Package Requirements for `urllib3` and `setuptools` ([#27](https://github.com/infobloxopen/universal-ddi-python-client/pull/27))

## [v0.1.0](https://github.com/infobloxopen/universal-ddi-python-client/releases/tag/v0.1.0) (2025-01-31)

### Initial Release for Universal DDI Python Client

The initial release of the **Universal DDI Python Client** supports the following Universal DDI APIs:

#### Infoblox Cloud

- **Infrastructure Management**
- **Infrastructure Provision** (HostActivation API)
- **Anycast Configuration Manager**
- **Upgrade Policy**

#### Infoblox Threat Defense

- **Threat Defense Cloud** (FW API)
- **DNS Forwarding Proxy** (DFP API)
- **Redirect**

#### Universal DDI

- **IP Address Management**
- **DNS Configuration**
- **DNS Data**
- **Keys**
- **Cloud Discovery Providers**
- **IPAM Federation**