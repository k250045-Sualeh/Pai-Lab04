class SecuritySystem:
    def __init__(self, tool_name):
        self.tool_name = tool_name

    def respond(self):
        print(f"{self.tool_name} is responding to the threat in a generic way.")


class Firewall(SecuritySystem):
    def respond(self):
        print(f"{self.tool_name} Response: Blocking suspicious network traffic.")


class Antivirus(SecuritySystem):
    def respond(self):
        print(f"{self.tool_name} Response: Isolating malicious files.")


class IntrusionDetectionSystem(SecuritySystem):
    def respond(self):
        print(f"{self.tool_name} Response: Generating security alert.")


security_tools = [
    Firewall("Firewall-01"),
    Antivirus("Antivirus-Pro"),
    IntrusionDetectionSystem("IDS-Sensor")
]

print("Cyber Attack Detected! Activating all security tools...\n")

for tool in security_tools:
    tool.respond()