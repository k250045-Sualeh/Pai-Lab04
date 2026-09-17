class Robot:
    LOW_BATTERY_THRESHOLD = 20

    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery

    def can_move(self):
        if self.battery < self.LOW_BATTERY_THRESHOLD:
            print(f"{self.name}: Battery too low ({self.battery}%). Cannot move. Please charge.")
            return False
        return True

    def move(self):
        if self.can_move():
            print(f"{self.name} is moving.")

    def charge(self, amount=100):
        self.battery = min(100, self.battery + amount)
        print(f"{self.name} is charging... Battery level: {self.battery}%")


class DeliveryRobot(Robot):
    def move(self):
        if self.can_move():
            print(f"{self.name} is moving to the delivery location. Battery: {self.battery}%")
            self.battery -= 10  


class SecurityRobot(Robot):
    def move(self):
        if self.can_move():
            print(f"{self.name} is patrolling the designated area. Battery: {self.battery}%")
            self.battery -= 10


class RescueRobot(Robot):
    def move(self):
        if self.can_move():
            print(f"{self.name} is heading toward the disaster location. Battery: {self.battery}%")
            self.battery -= 10


robots = [
    DeliveryRobot("Delivery-Bot-1", battery=50),
    SecurityRobot("Security-Bot-1", battery=15), 
    RescueRobot("Rescue-Bot-1", battery=30)
]

print("---- Initial Movement Attempts ----")
for robot in robots:
    robot.move()

print("\n---- Charging the Low-Battery Robot ----")
robots[1].charge()

print("\n---- Retrying Movement ----")
for robot in robots:
    robot.move()