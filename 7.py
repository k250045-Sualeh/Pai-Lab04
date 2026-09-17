class CyberAgent:
    def __init__(self, agent_name, status="Idle"):
        self.agent_name = agent_name
        self.status = status
        self.__threat_score = 0   

    def update_threat_score(self, score):
        if 0 <= score <= 100:
            self.__threat_score = score
        else:
            print(f"Can't set threat score to {score} — it has to be between 0 and 100.")

    def get_threat_score(self):
        return self.__threat_score

    def analyze(self):
        print(f"{self.agent_name} is checking things out, nothing specific configured yet.")

    def respond(self):
        print(f"{self.agent_name} doesn't have a specific response set up.")


class NetworkAgent(CyberAgent):
    def analyze(self):
        self.status = "Analyzing"
        self.update_threat_score(65)
        print(f"{self.agent_name} [{self.status}] is going through the network traffic logs. "
              f"Current threat score: {self.get_threat_score()}")

    def respond(self):
        if self.get_threat_score() >= 50:
            self.status = "Responding"
            print(f"{self.agent_name} [{self.status}]: found something suspicious, blocking the IPs involved.")
        else:
            print(f"{self.agent_name}: traffic looks fine for now, no action needed.")


class MalwareAgent(CyberAgent):
    def analyze(self):
        self.status = "Analyzing"
        self.update_threat_score(85)
        print(f"{self.agent_name} [{self.status}] is scanning files for known malware signatures. "
              f"Current threat score: {self.get_threat_score()}")

    def respond(self):
        if self.get_threat_score() >= 50:
            self.status = "Responding"
            print(f"{self.agent_name} [{self.status}]: infected files found, moving them to quarantine.")
        else:
            print(f"{self.agent_name}: scan came back clean.")


class IncidentResponseAgent(CyberAgent):
    def analyze(self):
        self.status = "Analyzing"
        self.update_threat_score(90)
        print(f"{self.agent_name} [{self.status}] is reviewing how serious this incident actually is. "
              f"Current threat score: {self.get_threat_score()}")

    def respond(self):
        if self.get_threat_score() >= 50:
            self.status = "Responding"
            print(f"{self.agent_name} [{self.status}]: this looks serious — isolating the affected systems and alerting the admin.")
        else:
            print(f"{self.agent_name}: not urgent, just keeping an eye on it for now.")


agents = [
    NetworkAgent("Network-Agent-01"),
    MalwareAgent("Malware-Agent-01"),
    IncidentResponseAgent("IR-Agent-01")
]

print("Kicking off a scan across all agents...\n")

for agent in agents:
    agent.analyze()
    agent.respond()
    print("-" * 50)