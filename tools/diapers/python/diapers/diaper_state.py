from g3.state import State, Action
from spatial_features.groundings import PhysicalObject, Prism
from numpy import transpose as tp
from esdcs.context import Context

class DiaperState(State):
    @staticmethod
    def example_state():
        robot = PhysicalObject(Prism.from_points_xy(tp([(0, 0), (1, 0), (1, 1), (0, 1)]),
                                                    0, 2),
                               tags=("robot",), 
                               lcmId=DiaperState.AGENT_ID + 2)
        caregiver = PhysicalObject(Prism.from_points_xy(tp([(3, 2), (4, 2), (4, 3), (3, 3)]),
                                                    0, 2),
                               tags=("caregiver",), 
                               lcmId=DiaperState.AGENT_ID + 3)
        child = PhysicalObject(Prism.from_points_xy(tp([(4, 4), (5, 4), (5, 5), (4, 5)]),
                                                    0, 0.5),
                               tags=("child",), 
                               lcmId=DiaperState.AGENT_ID + 3)


        objects = [
            PhysicalObject(Prism.from_points_xy(tp([(-1, 1.1), (2, 1.1), (2, 3),
                                                        (-1, 3)]),
                                                    1, 1.25), tags=("table",), lcmId=3),
            PhysicalObject(Prism.from_points_xy(tp([(0.5, 1.5), (0.75, 1.5), 
                                                    (0.75, 1.75), (0.5, 1.75)]),
                                                1.25, 1.3), tags=("wipes",), 
                           lcmId=4), 
            PhysicalObject(Prism.from_points_xy(tp([(1, 2), (1.25, 2), 
                                                    (1.25, 2.25), (1, 2.25)]),
                                                1.25, 1.3), tags=("diaper",), 
                           lcmId=5)]
        return DiaperState(robot, caregiver, child, objects)
    
    """
    """
    def __init__(self, robot, caregiver, child, objects):
        self.objects = objects
        self.robot = robot
        self.caregiver = caregiver
        self.child = child

        self.groundings = objects + [self.robot, self.caregiver, self.child]

    def to_context(self):
        return Context.from_groundings(self.groundings)
        

class Pickup(Action):
    def __init__(self, obj):
        self.obj = obj
        self.name = "pickup"
        

class Handoff(Action):
    def __init__(self):
        self.name = "handoff"


         
