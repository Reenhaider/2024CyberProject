
__PROJECT PLAN SCOPE – CSOC Cybersecurity Operations Centre for SME's:__

|     |     |
| --- | --- |
| __PROJECT NO.__ | DATE SUBMITTED |
| VU2230 | 21/04/2023 |
| __PROJECT OBJECTIVES__ |     |
| Develop a prototype cybersecurity model (CSOC) infrastructure tailored for a small to medium-sized organization.<br><br>1. Implement both physical and virtualized firewalls to secure the network perimeter.<br>2. Configure PaloAlto firewall to enforce network security policies and monitor traffic.<br>3. Integrate Cisco Switch for network management and control.<br>4. Design, deploy, and configure KaliPurple SIEM for comprehensive security event monitoring and analysis.<br>5. Set up Windows Server 22 Domain Controller for centralized authentication and access control.<br>6. Secure endpoint devices by deploying Elastic defend on Windows 10/11 clients.<br>7. Establish Ubuntu LAMP DMZ WEB server with appropriate security measures.<br>8. Deploy Suricata IDS/IPS on OPNsense firewall to detect and prevent intrusions.<br>9. Conduct red team testing exercises using Kali to assess the effectiveness of firewall rules, Windows clients, and DMZ Web Server security.<br>10. Perform blue team activities leveraging Kali Purple SIEM for timely alert detection and response.<br>11. Execute systematic project testing to ensure the functionality and security of the implemented systems.<br>12. Document all development, execution, evaluation, and testing processes for future reference and knowledge transfer. |     |

## Step 1. Project Deliverables:  
|     |
| --- |
| List all project deliverables and briefly describe each. Do not list dates. |
| Deliverables should include outputs and ancillary results: PM reports, documentation, etc. |
| The level of detail will be dependent upon the project objectives. |

|     |     |
| --- | --- |
| __DELIVERABLE NO__ | __DESCRIPTION__ |
| 1   | Cybersecurity Model (CSOC) Infrastructure Documentation: Comprehensive documentation outlining the design, architecture, and implementation details of the cybersecurity model tailored for a small to medium-sized organization. |
| 2   | Physical and Virtualized Firewall Configuration Documentation: Detailed documentation on the configuration of PaloAlto firewall and OPNsense firewall, including network security policies, rule sets, and monitoring configurations. |
| 3   | Cisco Switch Configuration Documentation: Documentation covering the configuration of Cisco Switch for network management and control, including VLAN setup, port configurations, and security features. |
| 4   | KaliPurple SIEM Implementation Documentation: Detailed documentation on the deployment and configuration of KaliPurple SIEM, including data sources integration, correlation rules, and incident response procedures. |
| 5   | Windows Server 22 Domain Controller Setup Documentation: Documentation outlining the setup and configuration of Windows Server 22 Domain Controller for centralized authentication and access control. |
| 6   | Endpoint Security Documentation: Documentation covering the deployment and configuration of Elastic defend on Windows 10/11 clients for endpoint protection. |
| 7   | Ubuntu LAMP DMZ WEB Server Configuration Documentation: Documentation detailing the setup and security configuration of Ubuntu LAMP DMZ WEB server, including web server software, database, and security measures. |
| 8   | Suricata IDS/IPS Configuration Documentation: Documentation covering the deployment and configuration of Suricata IDS/IPS on OPNsense firewall for intrusion detection and prevention. |
| 9   | Red Team Testing Report: Report documenting the findings and results of red team testing exercises conducted using Kali, including vulnerabilities identified and recommendations for improvement. |
| 10  | Blue Team Response Report: Report documenting the blue team response activities using KaliPurple SIEM, including alerts detected, incidents investigated, and response actions taken. |
| 11  | Project Testing Results: Documentation containing the results of systematic project testing, including functional testing, security testing, and performance testing. |
| 12  | Project Documentation: Overall documentation summarizing the project scope, objectives, methodologies, outcomes, and lessons learned. |
| 13  | Training Materials: Training materials and guides for future maintenance and operation of the implemented cybersecurity infrastructure. |
| 14  | Presentation: Presentation slides summarizing the project overview, objectives, key findings, and recommendations for stakeholders. |

## Step 2. List of Project Tasks:
  
List all project tasks to be completed, based on the deliverables listed in the previous section. Do not list dates. Add more rows as necessary. 

Alternatively, you can attach your work breakdown structure (WBS) to the scope statement. 

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Work breakdown structure (WBS) attached | NO  | X   | YES |     |
| Provide link, if applicable. | N/A |     |     |     |

|     |     |     |
| --- | --- | --- |
| TASK NO. | DESCRIPTION | FOR DELIVERABLE NO. …ENTER TASK # |
| 1   | Initiation | <br> |
| 1.1 | Define Project scope | 12  |
| 1.2 | Define project tasks and work breakdown structure (WBS) | 12  |
| 1.3 | Identify and secure project resources (hardware, software, personnel) | <br> |
| 2   | Project management | <br> |
| 2.1 | Conduct weekly standups | <br> |
| 2.2 | Conduct monthly project meetings | <br> |
| 2.3 | Develop and maintain project risk register | <br> |
| 3   | Prototype Development | <br> |
| 3.1 | Set up and interconnect Networking infrastructure | 2,3 |
| 3.2 | Set up configure and interconnect Virtual environment, firewall , servers and client | 2,4,5,6,7 |
| 3.2.1 | Set up and configure virtual firewall | 2   |
| 3.2.2 | Set up and configure virtual servers | 4,5,7 |
| 3.2.3 | Set up and configure virtual clients | 6   |
| 3.3 | Configure kali Purple - for remote management - ssh, rdp, console | 7   |
| 3.4 | Implement kali Purple SIEM - install elastic stack - elastic , kibana | 4   |
| 3.5 | Implement Fleet Server and end point protection agent - overview / installation | 6   |
| 3.6 | Integrate OPNsense firewall logs with KaliPurple SIEM | 4,8 |
| 3.7 | Integrate Palo Alto Firewall into Kali Purple SIEM | 8   |
| 3.8 | DMZ Web server | 7   |
| 3.9 | Test and validate functionality of implemented systems | 11  |
| 4   | Production Deployment | <br> |
| 4.1 | Set up and interconnect Networking infrastructure | 2,3 |
| 4.2 | Set up configure and interconnect Virtual environment, firewall , servers and client | 2,4,5,6,7 |
| 4.2.1 | Set up and configure virtual firewall | 2   |
| 4.2.2 | Set up and configure virtual servers | 4,5,7 |
| 4.2.3 | Set up and configure virtual clients | 6   |
| 3.3 | Configure kali Purple - for remote management - ssh, rdp, console | 7   |
| 3.4 | Implement kali Purple SIEM - install elastic stack - elastic , kibana | 4   |
| 3.5 | Implement Fleet Server and end point protection agent - overview / installation | 6   |
| 3.6 | Integrate OPNsense firewall logs with KaliPurple SIEM | 4,8 |
| 3.7 | Integrate Palo Alto Firewall into Kali Purple SIEM | 8   |
| 3.8 | DMZ Web server | 7   |
| 3.9 | Test and validate functionality of implemented systems | 11  |
| 5   | Evaluation | <br> |
| 5.1 | Conduct functional testing | 11  |
| 5.2 | Plan and execute red team testing exercises | <br> |
| 5.3 | Conduct blue team response activities using KaliPurple SIEM | 10  |
| 5.4 | Develop red team testing report | 9   |
| 5.5 | Develop blue team response report | 10  |
| 5.6 | Conduct performance testing and optimisation | <br> |
| 6   | Documentation | <br> |
| 6.1 | Document project management processes | 12  |
| 6.2 | Document technical implementation details | 1-11 |
| 6.3 | Develop training materials for future maintenance and operation | 13  |
| 7   | Handover | <br> |
| 7.1 | Prepare final presentation | 14  |
| 7.2 | Submit project documentation | 12  |
| 7.3 | Conduct knowledge transfer session | <br> |

## Step 3. Out of Scope:
  

|     |     |
| --- | --- |
| This project will NOT accomplish or include the following: | - The project will not ensure any physical security measures like access control systems, CCTV surveillance, etc. <br>- It will not Integrate with any additional systems or services that are not explicitly mentioned in the project requirements.<br>- It will not provide any comprehensive cybersecurity training for employees.<br>- Disaster recovery and business continuity planning will not be included in this project.<br>- It will not ensure compliance with specific regulations or standards beyond what is explicitly mentioned in the project requirements. |

## Step 4. Project Assumptions:
  

|     |     |
| --- | --- |
| NO. | ASSUMPTION |
| 1   | It is assumed that all the necessary hardware and software resources (like PaloAlto firewall, Cisco Switch, KaliPurple SIEM, Windows server 22, Elastic Defend, etc.) are available and functional. If this assumption proves false, it could lead to delays in project execution and increased costs. |
| 2   | The project assumes that there will be effective communication among all project team members and stakeholders. Poor communication could lead to misunderstandings, conflicts, and delays in project execution. |
| 3   | All team members will turn up regularly. Failure to do so will impact the project schedule and cohesion. |

## Step 5. Project Constraints:
  

|     |     |
| --- | --- |
| PROJECT START DATE | 04/16/2024 |
| LAUNCH / GO-LIVE DATE | 06/18/2024 |
| PROJECT END DATE | 06/30/2024 |
| LIST ANY HARD DEADLINE(S) | <br> |
| LIST OTHER DATES / DESCRIPTIONS OF KEY MILESTONES | Identify project milestonesInitial, prototype, production, test, RBT threat hunting, documentation, presentation / handover |
| BUDGET CONSTRAINTS | Total Project Budget:The total project budget for the development of the CSOC infrastructure is set at  $13000.00 (Team of 3 working 9 hours a week, each getting paid $45).The project must adhere to a predefined budget for procurement and implementation. |
| QUALITY OR PERFORMANCE CONSTRAINTS | Thorough system testing must be conducted to ensure the functionality and security of the implemented systems.Red Team (RBT) Threat Hunting exercises must be conducted to assess the effectiveness of the infrastructure.The implemented CSOC infrastructure must comply with the Australian Signals Directorate (ASD) Essential 8 Strategies to mitigate cybersecurity incidents. |
| EQUIPMENT / PERSONNEL CONSTRAINTS | VMs -stored VDI files : The number of virtual machines (VMs) must be limited due to storage capacity constraints, especially considering the size of the stored VDI files.Skills and team members availability : The availability of team members with specific skills may be limited. |
| REGULATORY CONSTRAINTS | The project must comply with legal and regulatory requirements, including data protection laws and industry standards, ASD essential 8, PII legislations - privacy act.Additionally, the project must adhere to industry standards such as ISO 27001 for information security management and NIST guidelines for cybersecurity. |

## Step 6. Updated Estimates:
  

|     |     |
| --- | --- |
| Estimate the hours required to complete the project. | 90 hrs |

## Step 7. Approvals:
  

|     |     |     |     |
| --- | --- | --- | --- |
| STAKEHOLDER NAME & TITLE | ROLE OF STAKEHOLDER / APPROVER | DATE SUBMITTED FOR APPROVAL | DATE APPROVAL RECEIVED |
| Steve Gale | approver | <br> | <br> |
| Nicholas Woolcock | contributor | <br> | <br> |
| Jarna Salonen | contributor | <br> | <br> |
| Shehreen Haider | contributor | <br> | <br> |
| <br> | <br> | <br> | <br> |

**
