### S1#show run
Building configuration...

Current configuration : 2645 bytes
!

version 12.2

no service pad

service timestamps debug datetime msec

service timestamps log datetime msec

service password-encryption

!

hostname S1

!

boot-start-marker

boot-end-marker


!

username admin secret 5 $1$5voL$U7Hv3v2.uV32THbjh72lz/

!


no aaa new-model

switch 1 provision ws-c3750e-48pd

system mtu routing 1500

!


no ip domain-lookup

ip domain-name sg.local

!

spanning-tree mode pvst

spanning-tree extend system-id

!


vlan internal allocation policy ascending

!

interface FastEthernet0

 no ip address
 
 shutdown
 
!

interface GigabitEthernet1/0/1

!

interface GigabitEthernet1/0/2

!

interface GigabitEthernet1/0/3

!

interface GigabitEthernet1/0/4

!

interface GigabitEthernet1/0/5

!

interface GigabitEthernet1/0/6

!

interface GigabitEthernet1/0/7

!

interface GigabitEthernet1/0/8

!

interface GigabitEthernet1/0/9

!

interface GigabitEthernet1/0/10

!

interface GigabitEthernet1/0/11

!

interface GigabitEthernet1/0/12

!

interface GigabitEthernet1/0/13

!

interface GigabitEthernet1/0/14

!

interface GigabitEthernet1/0/15

!

interface GigabitEthernet1/0/16

!

interface GigabitEthernet1/0/17

!

interface GigabitEthernet1/0/18

!

interface GigabitEthernet1/0/19

!

interface GigabitEthernet1/0/20

!

interface GigabitEthernet1/0/21

!

interface GigabitEthernet1/0/22

!

interface GigabitEthernet1/0/23

!

interface GigabitEthernet1/0/24

!

interface GigabitEthernet1/0/25

!

interface GigabitEthernet1/0/26

!

interface GigabitEthernet1/0/27

!

interface GigabitEthernet1/0/28

!

interface GigabitEthernet1/0/29

!

interface GigabitEthernet1/0/30

!

interface GigabitEthernet1/0/31

!

interface GigabitEthernet1/0/32

!

interface GigabitEthernet1/0/33

!

interface GigabitEthernet1/0/34

!

interface GigabitEthernet1/0/35

!

interface GigabitEthernet1/0/36

!

interface GigabitEthernet1/0/37

!

interface GigabitEthernet1/0/38

!

interface GigabitEthernet1/0/39

!

interface GigabitEthernet1/0/40

!

interface GigabitEthernet1/0/41

!

interface GigabitEthernet1/0/42

!

interface GigabitEthernet1/0/43

!

interface GigabitEthernet1/0/44

!

interface GigabitEthernet1/0/45

!

interface GigabitEthernet1/0/46

!

interface GigabitEthernet1/0/47

!

interface GigabitEthernet1/0/48

!

interface GigabitEthernet1/0/49

!

interface GigabitEthernet1/0/50

!

interface GigabitEthernet1/0/51

!

interface GigabitEthernet1/0/52

!

interface TenGigabitEthernet1/0/1

!

interface TenGigabitEthernet1/0/2

!

interface Vlan1

 ip address 192.168.100.254 255.255.255.0
!

ip classless

ip http server

ip http secure-server

!

logging trap debugging

logging 192.168.100.200

!

line con 0

line vty 0 4

 login local
 
 transport input ssh
 
line vty 5 15

 login
 
!

ntp server 192.168.100.100

end


S1#

