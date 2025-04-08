Building a Basic Network Sniffer Steps:-

Step 1:-
        Install Dependecies Before running the Script, ensure you have Scapy installed.

        Installd Scapy Run the following command in the Command Prompt(CMD) or the Terminal:-
            >> pip install scapy

        For Windows users, you also need Npcap
        Install Npcap Downoad and Install it from:-
            https://nmap.org/npcap/

            During Installation, select
                Install Npcap in WinPcap API - compatible mode

Step 2:-
        Import Required Libraries we will use Scapy to capture Network packets.

Step 3:-
        Setting Up Packet Capture

            To capture packets, a sniffer listens on a network interface and processes incomeing data.

            You can define rules for filtering and analyzing the packets to focus on specific type of traffic.

Step 4:-
        Running the Sniffer

            After setting up the environment and configuring the sniffer, execute it in Command Prompt (Windows) or Terminal (Linux/macOS) to begin capturing packets.

Step 5:-
        Expected Output

            Once the sniffer captures packets, it display relevent information such as Ethernet, IP, and transport layer details. The output includes:

                Source and Destination MAC Addresses
                IP Addresses and Protocol Type 
                Transport Layer Details (TCP, UDP, ICMP) 