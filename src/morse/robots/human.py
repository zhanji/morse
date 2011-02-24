import GameLogic
import morse.helpers.robot
from morse.core.services import service

class HumanClass(morse.helpers.robot.MorseRobotClass):
    """ Class definition for the human as a robot entity
        Sub class of Morse_Object. """

    def __init__(self, obj, parent=None):
        """ Constructor method.
            Receives the reference to the Blender object.
            Optionally it gets the name of the object's parent,
            but that information is not currently used for a robot. """
        # Call the constructor of the parent class
        print ("######## ROBOT '%s' INITIALIZING ########" % obj.name)
        super(self.__class__,self).__init__(obj, parent)

        print ('######## ROBOT INITIALIZED ########')

    @service
    def move(self, speed, rotation):
        """ move the human. a request to use by a socket.
        Done for wiimote remote control.
        """
        
        human = self.blender_obj
        
        #TODO : speed and rotation limit.
        human.applyMovement( [speed,0,0], True )
        human.applyRotation( [0,0,rotation], True )
        
        
    def default_action(self):
        """ Main function of this component. """
        pass
