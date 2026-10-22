class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.small = small
        self.medium = medium

        self.parking_lot = {1:self.big,2:self.medium,3:self.small}


        
    def addCar(self, carType: int) -> bool:
        if carType not in self.parking_lot:
            raise ValueError("car type not supported")

        if self.parking_lot[carType]!=0:
            self.parking_lot[carType] = self.parking_lot.get(carType)-1
            return True

        return False 