# Network-Automation-Demo
:floppy_disk:
This is my first attempt at creating a network automation demo for submission to Cisco DevNet's Automation Exchange - https://developer.cisco.com/network-automation/

### **About the LAB to run the demo:**
We will be interacting with an Always-On Sandbox instance of a Cisco Cloud Services Router - CSR1000v

Sandbox URL: https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology

**CSR1000V Host:** ios-xe-mgmt.cisco.com

**SSH Port:** 8181

**NETCONF Port:** 10000

**RESTCONF Ports:** 9443 (HTTPS)

**Credentials of this public available Sandbox to specify when prompted for it:**

**Username:** developer

**Password:** C1sco12345

**Dependencies:** See requirements.txt 
------------------------------------------

***Walk***

1. Create and activate a virtual environment to conduct this lab in
2. Fork and clone the GitHub repository: 
git clone https://github.com/xanderstevenson/network-automation-demo.git
3. Install required dependencies:
pip install -r requirements.txt
4. Run the script
python main.py
5. You will be prompted to enter the credentials (username & password listed above)
6. Make a choice from the options in this menu:
+--------+-------------------------------------+<br>
| OPTION |                CONFIG               |<br>
+--------+-------------------------------------+<br>
|   1    | Running Config - View and Print Log |
|   2    |  Interfaces - View and Print Log(s) |
|   3    | Startup Config - View and Print Log |
|   4    |                 Exit                |
+--------+-------------------------------------+

For the main 3 choices, a copy of the relevant log will be automatically copied as backup to a text file in your local repo.

If you read this entire README.md, then congratulations! Have a cookie: :cookie:
