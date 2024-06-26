# 2024CyberProject -CSOC Cybersecurity Operations Centre for SME's

### Project overview
The cybersecuirty project implements the development execution, evaluation and documentation of a prototype cybersecurity model (CSOC) infrastructure for a small to medium size organisation. It includes both physical and virtualised firewalls, servers, clients and SIEM. Project systems testing, Red and Blue (Purple) teaming activities are undertaken and documented.

### Project Requirements


The project incorportes the development, execution, evaluation and documentation of kaliPurple SIEM in a simulated virtual environment. It includes creating, configuring and interconnecting the following physical and virtualised systems:

- PaloAlto firewall,
- Cisco Switch,
- KaliPurple SIEM,
- Windows server 22 Domain Controller
- endpoint protected windows 10/11 clients using Elastc defend,
- Ubuntu LAMP DMZ WEB server,
- suricata IDS/IPS in OPNsense firewall.

The Project also includes red and blue (purple) teaming exercises :

- Red team testing and evaluation using Kali, for testing and evaluating the firewall rules, windows clients and DMZ Web Server
- Blue team responding using Kali Purple SIEM for alert detection and response.

### Prototype VS Production system configuration

The prototype lab environment uses virtualised systems and a Virtual OPNsense firewall with VMs connected using VirtualBox internal networking.

The production lab environment uses virtualised systems that use bridged networking to connect via a physical Cisco Switch to a physical Palo Alto Firewall.  
