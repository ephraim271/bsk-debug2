from Basilisk.moduleTemplates import cModuleTemplate
from Basilisk.utilities import SimulationBaseClass
from Basilisk.utilities import macros
from Basilisk.utilities import unitTestSupport
import ExeTime
from Basilisk.simulation.simSynch import ClockSynch


def run():
    """
    Illustration of recording messages
    """

    #  Create a sim module as an empty container
    scSim = SimulationBaseClass.SimBaseClass()

    #  create the simulation process
    dynProcess = scSim.CreateNewProcess("dynamicsProcess", 100)

    # create the dynamics task and specify the integration update time
    dynProcess.addTask(scSim.CreateNewTask("dynamicsTask", macros.sec2nano(0.005)))

    # create modules
    nmodules = 75
    for i in range(nmodules):
        exec(f'mod{i} = cModuleTemplate.cModuleTemplateConfig()')
        exec(f'mod{i}Wrap = scSim.setModelDataWrap(mod{i})')
        exec(f'mod{i}Wrap.ModelTag = "cModule{i}"')
        exec(f'scSim.AddModelToTask("dynamicsTask", mod{i}Wrap, mod{i})')
        exec(f'mod{i}.dataInMsg.subscribeTo(mod{i}.dataOutMsg)')
        

    x = []
    for i in range(nmodules):
        # setup message recording
        exec(f'msgRec{i} = mod{i}.dataOutMsg.recorder()')
        exec(f'scSim.AddModelToTask("dynamicsTask", msgRec{i})')
        #x.append(eval(f"msgRec{i}"))
        print(i)
        
    clockSync = ClockSynch()
    clockSync.accelFactor = 1
    clockSync.displayTime = True
    clockSync.accuracyNanos = 0
    

    
    scSim.AddModelToTask("dynamicsTask", clockSync)

        
    TimeProcess = scSim.CreateNewPythonProcess("TimeProc", 99)
    TimeProcess.createPythonTask("TimeTask", macros.sec2nano(0.01), True)
    
    TimeModule = ExeTime.ExeTime("TimeModule")

    TimeProcess.addModelToTask("TimeTask", TimeModule)




    #  initialize Simulation:
    scSim.InitializeSimulation()

    #   configure a simulation stop time and execute the simulation run
    scSim.ConfigureStopTime(macros.sec2nano(180))
    scSim.ShowExecutionFigure(True)
    scSim.ExecuteSimulation()
if __name__ == "__main__":
    run()



