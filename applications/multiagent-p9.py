import sys
import os


# Get the project root by going up one level from 'applications'
project_root = os.path.abspath(os.path.join(os.getcwd(), '..'))
print(f"📂 Project Root: {project_root}")

# Append 'src' directory to sys.path
src_path = os.path.join(project_root, 'src')
sys.path.append(src_path)

# Print sys.path to verify
print("🔍 Updated sys.path:")
for path in sys.path:
    print(path)

# Try importing Saga again
try:
    from multi_agent.saga import Saga
    from multi_agent.agent import Agent
    print("✅ Saga imported successfully!")
    print("✅ Agent imported successfully!")
except ModuleNotFoundError as e:
    print("❌ Import failed:", e)



# Initialize Saga
saga = Saga()

# ---- Member & Time Setup Agent ---- #
MT_Agent = Agent(
    name="Member & Time Setup Agent",
    backstory="You track family members' arrivals and ensure accurate scheduling.",
    task_description="Set up arrival times, locations, and travel durations for all family members.",
    task_expected_output="Structured schedule ensuring all members arrive on time for dinner. - Sarah(Mom):Host,athome, - James(Dad):LandsatBOS1:00PMfromSF, - Emily(Sister):LandsatBOS2:30PMfromChicago - Michael(Brother):Driving,arrives3:00PMfromNY - Grandma:NeedspickupfromsuburbanBoston"
)

# ---- Requirement Setup Agent ---- #
RS_Agent = Agent(
    name="Requirement Setup Agent",
    backstory="You manage cooking schedules and key logistical needs.",
    task_description="Schedule turkey and side dish preparation while ensuring someone stays home for supervision.",
    task_expected_output="Optimized cooking schedule aligning with dinner timing. cooking requirements:  -Turkey:4hourscookingtime, - Sidedishes:2hourspreparation, - Someonemuststayhomeduringcooking, "
)

# ---- Disruption Update Agent ---- #
DU_Agent = Agent(
    name="Disruption Update Agent",
    backstory="You manage unexpected disruptions such as flight delays.",
    task_description="Adjust schedule due to James's flight delay by 1 hour.",
    task_expected_output="Updated schedule reflecting James's new arrival time at 2:00 PM."
)

# ---- Constraint Validation Agent ---- #
CV_Agent = Agent(
    name="Constraint Validation Agent",
    backstory="You verify all scheduling constraints and ensure compliance.",
    task_description="Validate that all pickups, cooking timelines, and supervision requirements are met.",
    task_expected_output="A conflict-free schedule ensuring all tasks are completed efficiently. - Jamesmustrentcarafterlanding, - Emilyrequiresairportpickup ,- Traveltimes: – HometoBOSAirport:60min – BOSAirporttoGrandma’s:60min – HometoGrandma’s:30min"
)

# ---- Supervisor Agent ---- #
SA_Agent = Agent(
    name="Supervisor Agent",
    backstory="You oversee all logistical elements and generate the final dinner preparation report.",
    task_description="Monitor and report on key tasks, including cooking start time, Emily's pickup, and Grandma's pickup.",
    task_expected_output="Comprehensive report detailing dinner preparation logistics and arrivals. key requirement: - Allfamilymembersathomefor6:00PMdinner - Turkeyandsidesreadybydinnertime - Allpickupscompletedwithavailabledrivers - Cookingsupervisionmaintained"
)

# Register Agents in Saga
saga.transaction_manager([MT_Agent, RS_Agent, DU_Agent, CV_Agent, SA_Agent])

# Execute with rollback enabled
saga.saga_coordinator(with_rollback=True)

# Print intra-agent details
saga.intra_agent()

# Print inter-agent dependencies
saga.inter_agent()

# Select context for an agent
saga.select_context("Member & Time Setup Agent")

# Restore an agent’s execution
saga.restore_context("Member & Time Setup Agent")
