class Computer:
    def __init__(self, cpu_usage, ram_usage, battery_level):
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
        self.battery_level = battery_level

    def system_status(self):
        warnings = []

        if self.cpu_usage > 80:
            warnings.append("Heavy CPU Load")

        if self.ram_usage > 85:
            warnings.append("High Memory Usage")

        if self.battery_level < 20:
            warnings.append("Low Battery")

        if warnings:
            print("System requires attention:")
            for warning in warnings:
                print("-", warning)
        else:
            print("System is operating normally.")

computer1 = Computer(90, 70, 15)
computer2 = Computer(50, 60, 80)

print("Computer 1:")
computer1.system_status()

print("\nComputer 2:")
computer2.system_status()