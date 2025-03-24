from scapy.all import sniff, IP, TCP, UDP, Ether, Raw

def packet_callback(packet):
    """
    Callback function to process each captured packet.
    """
    try:
    # Extract Ethernet layer information.
        if Ether in packet:
           print(f"[Ethernet] Source MAC: {packet[Ether].src}, Destination MAC: {packet[Ether].dst}")

    # Extract IP layer information.
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            print(f"[IP] Source IP: {src_ip}, Destination IP: {dst_ip}")
        
        # Extract protocol information
            if TCP in packet:
                print(f"[TCP] Source Port: {packet[TCP].sport}, Destination Port: {packet[TCP].dport}")
            elif UDP in packet:
                print(f"[UDP] Source Port: {packet[UDP].sport},  Destination Port: {packet[UDP].dport}")

        # Extract payload data (first 64 bytes)
            if packet.haslayer(Raw):
                payload = packet[Raw].load[:64] # Limit payload to display 64 bytes.
                try:
                    payload_text = payload.decode('utf-8', errors="replace")
                    print(f"[Payload] {payload_text}")
                except UnicodeDecodeError:
                    print(f"[Payload] (Raw Bytes) {payload}")

        print("-" * 50)
    except Exception as e:
        print(f"Error processing packet: {e}")

def main():
    print("Starting packet sniffer... Press CTRL+C to stop.")
    try:
        sniff(prn=packet_callback, store=False)
    except KeyboardInterrupt:
        print("\nPacket sniffer stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()