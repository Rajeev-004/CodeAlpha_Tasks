from scapy.all import sniff

def packet_call(packet):

    print(packet.summary())

print("Sniffing network traffic...\n")
sniff(prn=packet_call, store=0, count=20)

print("\nPacket capture complete.")