class ThreatDetector:
    def __init__(self, device_name, ip_address,threat_level):
        self.device_name=device_name
        self.ip_address=ip_address
        self.threat_level=threat_level

    def scan(self):
        threat_level=self.threat_level

        if threat_level=="Low":
            status="System is safe"
        elif threat_level=="Medium":
            status="Suspicious Activity"
        elif threat_level=="High":
            status="Critical threat Detected"
        else:
            status="Unknown threat level"

        print(f"Device Name : {self.device_name}")
        print(f"IP Address    : {self.ip_address}")
        print(f"Threat Level  : {threat_level}")
        print(f"System Status : {status}")
        print("-" * 40)


device1 = ThreatDetector("Laptop-01", "192.168.1.10", "Low")
device2 = ThreatDetector("Main server", "192.168.1.20", "Medium")
device3 = ThreatDetector("Router Core", "192.168.1.1", "High")

device1.scan()
device2.scan()
device3.scan()