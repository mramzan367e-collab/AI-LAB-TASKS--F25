
class Controller:
    def __init__(self):
        self.previous = None

    def control(self, temp, occupied):
        if not occupied:
            mode = "OFF"
        elif temp <= 18:
            mode = "HEAT"
        elif temp >= 30:
            mode = "COOL"
        else:
            mode = "OFF"

        old = self.previous

        if mode == old:
            command = "No command"
        else:
            command = "Send command"
            self.previous = mode

        print("Previous Mode:", old)
        print("Target Mode:", mode)
        print("Command:", command)


c = Controller()

while True:
    temp = float(input("Enter temperature: "))
    occupied = input("Is room occupied? (yes/no): ").lower()

    c.control(temp, occupied == "yes")

    again = input("Enter more inputs? (yes/no): ").lower()
    if again != "yes":
        break
