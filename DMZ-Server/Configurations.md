## 1. Ubuntu server install - Prototype:

Oracle virtual box  
Ubuntu22.04.4 Desktop – 80Gig dynamic disk , 8Gig RAM  
Note: use NAT networking to start with

Oracle Virtual Box Storage > controller > Optical drive image - C:\Users\sgale\Downloads\ubuntu-22.04.4-desktop-amd64.iso


Install The OS, login and run terminal,

VirtualBox Tools > Network Manager - Nat Networks

Create NatNetwork1 - Right click - Properties

General Options

Name: DMZ Network

IPv4Prefix: 192.168.50.0/24

APPLY
## 2.Update Ubuntu DMZ WEB Server
```
sudo apt update
sudo apt upgrade
```
## 3. Configure Host only network to connect DMZ WEB Server to OPNsense firewall
PROTOTYPE NETWORK:

VirtalBox > Network

- Adapter 1
  - Attached to: Internal Network
  - Name: intnet
- Adapter 2
  - Attached to: Bridged Adapter
  - Name: Ethernet OR Wifi
- Adapter 3
  - Attached to: Host Only Adapter
  - Name: VirtualBox Host-Only Ethernet Adapter #2

VirtualBox  
File > Tools > network manager

- Host-only Networks
  
  - Create - VirtualBox Host-Only Ethernet Adapter #2
    
    - Adapter
      
      - Configure adapter Manually
        
      - IPv4 Address: 192.168.50.254
        
      - Subnet mask: 255.255.255.0
        
    - DHCP server (disable - dont enable)
      

Apply

VirtualBox - OPNsense VM Machine > settings > Network

- Adapter 3
  
  - Enable network Adapter
    
  - Attached to: Host Only Adapter
    
  - Name: VirtualBox Host-Only Ethernet Adapter #2

OK

Virtual Box DMZ server VM - Settings

Network - Adapter 1 Enable

Attached to: Host-only Adapter Name: VirtualBox Host-Only Ethernet Adapter #2

VirtualBox  
OPNsense VM - Start

VirtualBox  
kaliPurple VM - Start

Firefox - [http://192.168.100.1](http://192.168.100.1/)  
root  
opnsense  
Interfaces > Assignments

New interface: em2  
Description: DMZ  
[+] Add  
OPT1 - select link  
Enable: Tick Enable interface  
Description: DMZ  
IPv4 configuration type: Static IPv4  
Static IPv4 configuration  
IPv4 Address: 192.168.50.1 /24

Save  
Apply Changes

## 3. Install Elastic Defend agent in DMZ WEB Server
Virtual Box kaliPurple VM - kibana

#### Fleet Agent Policy - Linux server policy

Fleet > Agent Policies - Create Agent policy - Linux Server policy

- Create Agent Policy

Linux server policy - Add Agent  
Enroll in Fleet  
Copy linux Tar code to clipboard

#### Install the agent in the linux server via Linux Tar script

Virtual Box DMZ server VM - terminal:

```
$sudo apt install curl  
$nano elasticAgentScript.sh
```

add --insecure to the last line of the file  
Paste Linux Tar contents into this file and save the file  
Paste the code into a terminal prompt to execute the script with --insecure

eg. (with your enrolment token)

```
$curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-8.8.2-linux-x86_64.tar.gz
tar xzvf elastic-agent-8.8.2-linux-x86_64.tar.gz
cd elastic-agent-8.8.2-linux-x86_64
sudo ./elastic-agent install --url=https://192.168.100.200:8220 --enrollment-token=XXXXXXXXXXXXXXX --insecure  
```

Execute the script ./elasticAgentScript.sh

```
chmod +x elasticAgentScript.sh
./elasticAgentScript.sh
```

the last line will prompt you want to continue: y (yes) , When the agent is sucessfully installed go back to the kaliPurple VM

#### confirm Linux DMZ server logs are sucessfully sent to kibana

Kibana - Discover  
filter = agent.name : "Your server name here"

eg. filter = agent.name : "I40-DMZ"

Confirm that logs are coming in from the DMZ server

####
