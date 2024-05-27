# human project (might be impossible)

def __sleep_mode__():
    # turns off most sensory and functional features
    pass

def __awaken__():
    # shuts down sleep mode and reverts its changes
    pass

class system_motor:
    def __init__(self):
        pass

class Muscles:
    def __init__(self, name, area, size):
        self.name = name
        self.area = area
        self.size = size

    def contract(area):
        if Muscles.area == area:
            size /= 0.8
    
    def extend(area):
        if Muscles.area == area:
            size *= 1.2

    def release(area):
        if Muscles.area == area:
            size *= 1.2

head_muscle_1 = Muscles("Occipitofrontalis", "face")
head_muscle_2 = Muscles("Orbicularis oculi", "face")
head_muscle_3 = Muscles("Orbicularis oris", "face")
head_muscle_4 = Muscles("Zygomaticus major", "face")
neck_muscle_1 = Muscles("Sternocleidomastoid", "neck")
shoulder_muscle_1 = Muscles("Trapezius", "shoulder")
breast_muscle_1 = Muscles("Pectoralis major", "breast")
breast_muscle_2 = Muscles("Latissimus dorsi", "breast")
breast_muscle_3 = Muscles("Serratus anterior", "breast")
arms_muscle_1 = Muscles("Deltoid", "arms")
arms_muscle_2 = Muscles("Biceps brachii", "arms")

Muscles.contract