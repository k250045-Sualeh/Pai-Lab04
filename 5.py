class Agent:
    def __init__(self, name, status="Idle"):
        self.name = name
        self.status = status

    def perform_task(self):
        print(f"{self.name} is performing a generic task.")


class SecurityAgent(Agent):
    def perform_task(self):
        self.status = "Active"
        print(f"{self.name} [{self.status}]: Detecting cyber threats...")


class MonitoringAgent(Agent):
    def perform_task(self):
        self.status = "Active"
        print(f"{self.name} [{self.status}]: Monitoring system activity...")


class RecoveryAgent(Agent):
    def perform_task(self):
        self.status = "Active"
        print(f"{self.name} [{self.status}]: Recovering system services...")

agents = [
    SecurityAgent("Agent Nova 1"),
    MonitoringAgent("Agent Sage 1"),
    RecoveryAgent("Agent Bravo 1")
]

print("System Startup: Dispatching all agents...\n")

for agent in agents:
    agent.perform_task()