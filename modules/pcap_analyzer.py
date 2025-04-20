import pyshark
import os

def analyze_pcap(file_path):
    if not os.path.exists(file_path):
        return ["Error: File does not exist."]

    output = []
    count = 0

    try:
        # Load the capture with fast JSON parsing
        cap = pyshark.FileCapture(file_path, use_json=True)

        for packet in cap:
            try:
                if 'IP' in packet:
                    src = packet.ip.src
                    dst = packet.ip.dst
                    proto = packet.highest_layer
                    output.append(f"{src} → {dst} | Protocol: {proto}")
                elif 'WLAN' in packet:
                    src = getattr(packet.wlan, 'sa', 'Unknown')
                    dst = getattr(packet.wlan, 'da', 'Unknown')
                    output.append(f"Wi-Fi Frame | {src} → {dst} | 802.11")
                else:
                    output.append(f"Other Packet | {packet.highest_layer}")
            except Exception as e:
                output.append(f"Error parsing packet: {e}")

            count += 1
            if count >= 50:
                break

        cap.close()
        return output if output else ["No usable packets found."]
    
    except Exception as e:
        return [f"Error loading PCAP: {e}"]
