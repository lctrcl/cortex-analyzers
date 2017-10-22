# cortex-analyzers
Custom analyzers for the Cortex (https://thehive-project.org/, https://github.com/CERT-BDF/Cortex) 

## Manalyze

Manalyze analyzer for Cortex is based on [Manalyze](https://github.com/JusticeRage/Manalyze), static analyzer for PE files, and it's useful to quickly triage malicious executables.

### Requirements

Install docker on the cortex instance. `docker pull evanowe/manalyze`  or build your own docker image ([https://github.com/lctrcl/docker-manalyze](https://github.com/lctrcl/docker-manalyze), don't forget to adjust docker image name in the code).

Copy Manalyze folder to folder, where cortex-analyzers are located and imported included template.

Supported types: **file**