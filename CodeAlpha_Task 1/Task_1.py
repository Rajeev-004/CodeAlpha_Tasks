from scapy.all import sniff, Ether, IP, TCP, UDP, ICMP

def packet_callback(packet):
    """Processes and prints details of each captured packet."""    
    # Check if the packet has an Ethernet layer
    if packet.haslayer(Ether):
        eth = packet[Ether]
        print(f"🔹 Ethernet Frame: {eth.src} ➝ {eth.dst} | Type: {hex(eth.type)}")
    
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        ip = packet[IP]
        print(f"🌍 IP Packet: {ip.src} ➝ {ip.dst} | Protocol: {ip.proto}")
    
        # Identify the transport layer protocol
        if packet.haslayer(TCP):
            tcp = packet[TCP]
            print(f"🔵 TCP Packet: {ip.src}:{tcp.sport} ➝ {ip.dst}:{tcp.dport} | Flags: {tcp.flags}")
        elif packet.haslayer(UDP):
            udp = packet[UDP]
            print(f"🟢 UDP Packet: {ip.src}:{udp.sport} ➝ {ip.dst}:{udp.dport}")
        elif packet.haslayer(ICMP):
            print(f"⚡ ICMP Packet: {ip.src} ➝ {ip.dst}")
    
print("📡 Sniffing network traffic... (Capturing 20 packets)\n")

# Start sniffing 20 packets
sniff(prn=packet_callback, store=0, count=20)

print("\n✅ Packet capture complete!")
