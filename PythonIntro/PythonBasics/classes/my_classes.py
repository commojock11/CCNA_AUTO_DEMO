class Car:
    def __init__(self, make: str, model: str, year: int, mileage: int, condition: str, color: str) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.condition = condition
        self.color = color
        self.is_running = False
        self.speed = 0

    def start(self) -> None:
        if self.is_running:
            print(f"The {self.year} {self.make} {self.model} is already running.")
            return
        else:
            self.is_running = True
        print(f"The {self.year} {self.make} {self.model} is starting.")

    def stop(self) -> None:
        if not self.is_running:
            print(f"The {self.year} {self.make} {self.model} is already stopped.")
            return
        else:
            self.is_running = False
        print(f"The {self.year} {self.make} {self.model} is stopping.")
    def accelerate(self, speed: int) -> None:
        if not self.is_running:
            print(f"The {self.year} {self.make} {self.model} is not running.")
            return
        else:
            self.speed += speed
            print(f"The {self.year} {self.make} {self.model} is accelerating to {self.speed} mph.")
