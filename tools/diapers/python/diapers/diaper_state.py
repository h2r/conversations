from g3.state import State, Action

class DiaperState(State):
    """
    """
    def __init__(self, objects, robot, caregiver, child):
        self.objects = objects
        self.robot = robot
        self.caregiver = caregiver
        self.child = child
        

class Pickup(Action):
    def __init__(self, obj):
        self.obj = obj
        self.name = "pickup"
        

class Handoff(Action):
    def __init__(self):
        self.name = "handoff"


         
