___Firewall Interface Configuration___:

Configured three firewall interfaces:

- Ethernet 1/1: 192.168.108.234/24 (Layer 3)
  
- Ethernet 1/2: 192.168.100.1/24 (Layer 3)
  
- Ethernet 1/3: 192.168.50.1/24 (Layer 3)
  
- Management: 192.168.1.1/24
  

__Created a virtual router VR-1 for all interfaces.__

Security Zones and Tag the Security Zones:

- __WAN (Internet)__ - (assigned ethernet1/1) - Black
  
- __LAN (Users)__ (assigned ethernet1/2, enabled User-ID) - Green
  
- __DMZ (Extranet)__  (assigned ethernet1/3) - Orange
  

__NAT Policy Configuration__:

Source NAT rules:

__LAN_to_WAN__: From internal zone to Internet zone using ethernet1/1 for source translation (Tag: LAN)

__DMZ_to_WAN__: From Extranet zone to Internet zone using ethernet1/1 for source translation (Tag: DMZ)

__Security Policy Rules:__

__Block_Bad_URLs:__ Block hacking, phishing, malware, and unknown categories (Tag: Block)

__LAN_to_DMZ:__ Allow ping, ssl, ssh, dns, web-browsing (Tag: Allow)

__LAN_to_WAN:__ Allow ping, dns, web-browsing, ssl (Tag: Allow)

__DMZ_to_WAN:__ Allow ping, dns, web-browsing, ssl (Tag: Allow)


Security Profiles:

__Corp-URL:__ Log access to all web categories.

__Corp-FB:__ Block dangerous file types.

__Corp-AV:__ Block viruses.

__Corp-AS:__ Block spyware.

__Corp-Vuln:__ Block vulnerabilities.

__Corp-WF:__ Send all file types to the public cloud for inspection.

Created a Security Profile Group Corp-Profiles and assigned the profiles to it.


__Destination NAT Policy and Security Policy for DMZ Access:__

NAT policy:

__Source Zone:__ WAN

__Destination Zone:__ WAN

__Destination Address:__ 192.168.108.134

__Service:__ service-http

__Destination Translation:__ 192.168.50.100

security policy added:

__Source Zone:__ WAN

__Destination Zone:__ DMZ

__Destination Address:__ 192.168.108.134

__Application:__ Web-Browsing

__Action:__ Allow

__Remote Management Configuration:__

security policy to:

Allow all access to 192.168.108.134 on port 80.

Allow SSH, RDP, and port 3306 from a specific Internet PC IP address in E108 Network.

 NAT policy service any.


