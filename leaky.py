import random
import time

# Constants
NOF_PACKETS = 5

def send_packet(packet_size, output_rate):
    """Simulate sending packets."""
    while packet_size > 0:
        sent = min(packet_size, output_rate)
        print(f"Packet of size {sent} Transmitted---", end="")
        packet_size -= sent
        print(f"Bytes Remaining to Transmit: {packet_size}")
        time.sleep(1)  # Simulate time delay between packets

def main():
    # Generate random packet sizes
    packet_size = [random.randint(0, 99) for _ in range(NOF_PACKETS)]

    for i in range(NOF_PACKETS):
        print(f"packet[{i}]: {packet_size[i]} bytes")

    # Input output rate and bucket size
    output_rate = int(input("Enter the Output rate: "))
    bucket_size = int(input("Enter the Bucket Size: "))

    # Process each packet
    for i in range(NOF_PACKETS):
        print(f"\nIncoming Packet size: {packet_size[i]}")
        if packet_size[i] > bucket_size:
            print(f"Incoming packet size ({packet_size[i]} bytes) is Greater than bucket capacity ({bucket_size} bytes) - PACKET REJECTED")
            continue

        print(f"Bytes remaining to Transmit: {packet_size[i]}")
        send_packet(packet_size[i], output_rate)

if __name__ == "__main__":
    main()
