# Network Security and Firewall Assignment Report

## 1. Introduction
- This report documents the process and results of implementing a simple firewall using OpenFlow-enabled switches in Mininet.
- The primary goal was to allow ICMP and ARP traffic while blocking all other traffic types, minimizing the network exposure and improving security.

---

## 2. Environment Setup
- **Setup Tools**: The environment was configured using Vagrant to create a virtualized Mininet instance and POX as the OpenFlow controller.
- **Network Topology**: The topology used included several hosts connected through OpenFlow-enabled switches, as described in `topo2.py`.
- **POX Controller**: The POX controller was set up to manage the network flow and enforce firewall rules.

### Screenshots
- **Environment Setup Confirmation**
  - This screenshot shows the terminal output after setting up the environment in Vagrant and starting Mininet to verify connectivity.
  - ![Environment Setup Confirmation](path/to/setup_confirmation_screenshot.png)

---

## 3. Firewall Rules Implementation
- **Firewall Rules**: The firewall rules were implemented to meet the following conditions:
  - **Allow**: All ICMP (ping) traffic.
  - **Allow**: All ARP traffic.
  - **Drop**: All other types of traffic by default.
- These rules were coded in the `exe1-controller.py` file using the POX framework to create specific flow entries in the switch's flow table.

### Screenshots
- **Firewall Rules Configuration**
  - This screenshot shows the firewall rules set up in the `exe1-controller.py` file, configured to allow only ARP and ICMP traffic.
  - ![Firewall Rules Configuration](path/to/firewall_rules_screenshot.png)

---

## 4. Testing the Topology and Firewall

### 4.1 Ping Test (pingall)
- **Test Objective**: To verify if the firewall correctly handles ICMP and ARP traffic, while dropping all other traffic types.
- **Test Execution**: The `pingall` command was run within Mininet to test connectivity among all hosts.
- **Expected Outcome**:
  - Hosts should be able to ping each other only when ICMP packets are allowed by the firewall.
  - ARP packets should be exchanged between all hosts, enabling address resolution.
  - Other types of packets should be dropped, with limited communication among hosts.
- **Results**: The expected behavior was observed, with ICMP and ARP packets allowed and all other traffic blocked.

### Screenshots
- **Pingall Test Results**
  - This screenshot shows the output of the `pingall` command, indicating successful ICMP packet transmission between allowed hosts and dropped packets where the firewall blocked them.
  - ![Pingall Test Results](path/to/pingall_test_results_screenshot.png)

---

### 4.2 Flow Table Inspection
- **Objective**: To verify that the firewall rules were correctly installed in the switch's flow table.
- **Execution**: The `dpctl dump-flows` command was used to inspect the flow entries in the switch.
- **Expected Outcome**: The flow table should show entries that accept ARP and ICMP traffic while dropping all other traffic by default.

### Screenshots
- **Flow Table Verification**
  - This screenshot displays the flow table entries confirming that only ARP and ICMP traffic is allowed, while other traffic is blocked.
  - ![Flow Table Verification](path/to/flow_table_screenshot.png)

---

## 5. Analysis of `l2_learning.py`
- **Overview**: The `l2_learning.py` script functions as a learning switch, dynamically learning MAC addresses of connected hosts and forwarding packets to the correct destination based on this knowledge.
- **ICMP Packet Transmission**: When `h1` pings `h4`, `l2_learning.py` should learn each host’s location on the network and direct the ICMP packet only to `h4`. There is minimal chance of receiving this packet at `h2` since the learning switch builds a forwarding table to avoid unnecessary flooding of known destinations.
- **Conclusion**: This setup ensures efficient packet delivery, reducing network traffic and preventing unintended hosts from receiving packets not meant for them.

### Screenshots
- **Learning Switch Results**
  - This screenshot shows the output from running the `l2_learning.py` controller and verifying that ICMP packets are forwarded only to the intended destination.
  - ![Learning Switch Results](path/to/learning_switch_results_screenshot.png)

---

## 6. Conclusion
- **Summary**: The firewall was successfully implemented, allowing ICMP and ARP traffic while blocking other traffic types. The Mininet environment effectively demonstrated the functionality of the OpenFlow-enabled firewall rules.
- **Challenges and Learnings**: Key challenges included configuring the environment and troubleshooting rule applications. The assignment reinforced understanding of network security, OpenFlow controller operations, and flow table management.
- **Future Considerations**: Enhancing the firewall to support more granular control over traffic types and handling dynamic network environments could improve its functionality.

---


