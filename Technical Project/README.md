**PRODUCTION NETWORK -**
**Integrate Palo Alto Firewall into Kali Purple SIEM:**

**Network Configuration:**
**Note: **KaliPurple VM networking is set to bridged mode for communication with the Palo Alto firewall on the production network.

**Syslog Configuration:**
**Note: **Palo Alto Firewall will send syslog logs to port 9001.

If PFsense integration is installed, ensure PFsense integration is switched off as it uses the same port 9001.

**Timezone Setting:**

Set the timezone to Australia/Melbourne.

Path: Device > Setup > Management - General Settings

Timezone: Australia/Melbourne

**Update Databases:**

To ensure the latest AV, applications, and threats databases are installed.

Path: Device > Dynamic Updates

Check Now

AntiVirus: Download and install

Applications and threats: Download and install

**Create a Security Policy:**

Path: Policies > Security - Add

**General:**

Name: Inside-to-Outside

Source:

Source Zone: Inside
Destination:

Destination Zone: Outside
Application:

Applications: Any
Service/URL Category:

Service: application-default
URL Category: Any
Actions:

Action setting: Allow

Log Setting: Log at session end

Click **OK**

**Create a Source NAT Policy:**

Path: Policies > NAT - Add

General:

Name: NatInsideToOutside

NAT Type: IPv4

Original Packet:

Source Zone: Inside

Destination Zone: Outside

Destination Interface: ethernet1/1

Service: any

Source Address: any

Destination Address: any

Translated Packet:

Source Address Translation:

Translation Type: Dynamic IP and Port

Address Type: Interface Address

Interface: ethernet1/1

IP Address: 192.168.108.2XX 

Destination Address Translation:

Translation Type: None

Click OK

Commit Changes:

Click COMMIT

**Testing**:
Test conducted by pinging or browsing from the Inside Zone, and check traffic logs.
Path: Monitor > Logs > Traffic
**Note**: Wait for session end to see the logs.
