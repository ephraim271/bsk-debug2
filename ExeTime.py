
import numpy as np
from Basilisk.architecture import messaging
from Basilisk.utilities import macros as mc, simulationArchTypes
import time


class ExeTime(simulationArchTypes.PythonModelClass):
    """
    This class inherits from the `PythonModelClass` available in the ``simulationArchTypes`` module.
    The `PythonModelClass` is the parent class which your Python BSK modules must inherit.
    The class uses the following
    virtual functions:

    #. ``reset``: The method that will initialize any persistent data in your model to a common
       "ready to run" state (e.g. filter states, integral control sums, etc).
    #. ``updateState``: The method that will be called at the rate specified
       in the PythonTask that was created in the input file.

    Additionally, your class should ensure that in the ``__init__`` method, your call the super
    ``__init__`` method for the class so that the base class' constructor also gets called to
    initialize the model-name, activity, moduleID, and other important class members:

    .. code-block:: python

        super(ExeTime, self).__init__(modelName, modelActive, modelPriority)

    You class must implement the above four functions. Beyond these four functions you class
    can complete any other computations you need (``Numpy``, ``matplotlib``, vision processing
    AI, whatever).
    """

    def __init__(self, modelName, modelActive=True, modelPriority=-1):
        super(ExeTime, self).__init__(modelName, modelActive, modelPriority)

        # Output message name
        self.count = 0
        self.prev_exec = time.time()
        self.name = modelName


    def reset(self, currentTime):
        """
        The reset method is used to clear out any persistent variables that need to get changed
        when a task is restarted.  This method is typically only called once after selfInit/crossInit,
        but it should be written to allow the user to call it multiple times if necessary.
        :param currentTime: current simulation time in nano-seconds
        :return: none
        """
        return

    def updateState(self, currentTime):
        """
        The updateState method is the cyclical worker method for a given Basilisk class.  It
        will get called periodically at the rate specified in the Python task that the model is
        attached to.  It persists and anything can be done inside of it.  If you have realtime
        requirements though, be careful about how much processing you put into a Python updateState
        method.  You could easily detonate your sim's ability to run in realtime.

        :param currentTime: current simulation time in nano-seconds
        :return: none
        """
        execution_time = time.time()
        print(f"{self.name} in ms {1000*(execution_time-self.prev_exec)}")
        self.prev_exec = execution_time
        print(f"{self.count=}")
        self.count+=1
        
        return
       
