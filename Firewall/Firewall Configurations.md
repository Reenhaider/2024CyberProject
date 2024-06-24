**

____Firewall Interface Configuration___:

Configured three firewall interfaces:

- Ethernet 1/1: 192.168.108.234/24 (Layer 3)
  
- Ethernet 1/2: 192.168.100.1/24 (Layer 3)
  
- Ethernet 1/3: 192.168.50.1/24 (Layer 3)
  
- Management: 192.168.1.1/24
  

Created a virtual router VR-1 for all interfaces.

Security Zones and Tag the Security Zones:

- WAN (Internet) - (assigned ethernet1/1) - Black
  
- LAN (Users) (assigned ethernet1/2, enabled User-ID) - Green
  
- DMZ (Extranet)  (assigned ethernet1/3) - Orange
  

NAT Policy Configuration:

Source NAT rules:

LAN_to_WAN: From internal zone to Internet zone using ethernet1/1 for source translation (Tag: LAN)

DMZ_to_WAN: From Extranet zone to Internet zone using ethernet1/1 for source translation (Tag: DMZ)

Security Policy Rules:

Block_Bad_URLs: Block hacking, phishing, malware, and unknown categories (Tag: Block)

LAN_to_DMZ: Allow ping, ssl, ssh, dns, web-browsing (Tag: Allow)

LAN_to_WAN: Allow ping, dns, web-browsing, ssl (Tag: Allow)

DMZ_to_WAN: Allow ping, dns, web-browsing, ssl (Tag: Allow)

**

**

Security Profiles:

Corp-URL: Log access to all web categories.

Corp-FB: Block dangerous file types.

Corp-AV: Block viruses.

Corp-AS: Block spyware.

Corp-Vuln: Block vulnerabilities.

Corp-WF: Send all file types to the public cloud for inspection.

Created a Security Profile Group Corp-Profiles and assigned the profiles to it.

**

**

Destination NAT Policy and Security Policy for DMZ Access:

NAT policy:

Source Zone: WAN

Destination Zone: WAN

Destination Address: 192.168.108.134

Service: service-http

Destination Translation: 192.168.50.100

security policy added:

Source Zone: WAN

Destination Zone: DMZ

Destination Address: 192.168.108.134

Application: Web-Browsing

Action: Allow

Remote Management Configuration:

Modified  security policy to:

Allow all access to 192.168.108.134 on port 80.

Allow SSH, RDP, and port 3306 from a specific Internet PC IP address in E108 Network.

Modified NAT policy for service any.

**
