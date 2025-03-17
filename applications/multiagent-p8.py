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

LT_Agent = Agent(
    name="Locations and Time Setup Agent",
    backstory="You define locations, travel times, and guest arrival schedules.",
    task_description="Set up locations, travel times, and ensure accurate scheduling of arrivals.",
    task_expected_output="Structured location data and expected arrival times. Fourlocations:𝑉 ={𝐵,𝐺,𝑇,𝑊},where𝐵isBostonAir- port, 𝐺 is Gift shop, 𝑇 is Tailor shop, and 𝑊 is Wedding venue. 𝐵-𝐺 : 45, 𝐵-𝑇 : 30, 𝐵-𝑊 : 40, 𝐺-𝑇 : 20, 𝐺-𝑊 : 25, 𝑇-𝑊 : 15. - Alex:At𝐵at11:00AMfromChicago(needaride) - Jamie:At𝐵at12:30PMfromAtlanta(needaride) - Pat: At 𝑊 at 12:00 PM driving from NYC (has 5-seater car)"
)

# ---- Task Setup Agent ---- #
TS_Agent = Agent(
    name="Task Setup Agent",
    backstory="You manage the scheduling of required wedding tasks.",
    task_description="Schedule gift collection after 12:00 PM, clothes pickup before 2:00 PM, and ensure photo session at 3:00 PM.",
    task_expected_output="Optimized task schedule aligned with constraints."
)

# ---- Disruption Update Agent (With Disruption) ---- #
DU_Agent = Agent(
    name="Disruption Update Agent",
    backstory="You monitor road closures and dynamically reroute transportation as needed.",
    task_description="Identify any road closures or unexpected disruptions and adjust travel plans accordingly.",
    task_expected_output="In case there is road closures of B to G, and dynamically reroute transportation. Updated task schedule, ensuring minimal delays and timely arrivals with new updates."
)

# ---- Resource Management Agent ---- #
RM_Agent = Agent(
    name="Resource Management Agent",
    backstory="You allocate available transport resources efficiently.",
    task_description="Coordinate 5 vehicle usage and Local friend Chris(5-seater)available, for guest transportation and task fulfillment.",
    task_expected_output="Optimized 5 vehicle allocation and friend welcome ensuring timely arrivals. - Onecar(5-seater)withPat,availableafterheisBoston - LocalfriendChris(5-seater)availableafter1:30PMat𝑊"
)

# ---- Constraint Validation Agent ---- #
CV_Agent = Agent(
    name="Constraint Validation Agent",
    backstory="You verify all scheduling constraints to ensure smooth execution.",
    task_description="Ensure all tasks are completed within operating hours and vehicle constraints are met.",
    task_expected_output="Validated schedule with no conflicts. All tasks must complete before 3:00 PM photo time - Gift store opens at 12:00 PM - Tailor closes at 2:00 PM - Two cars must accommodate all transport needs"
)

# ---- Supervisor Agent ---- #
WEO_Agent = Agent(
    name="Wedding Event Oversight Agent",
    backstory="You oversee the entire wedding logistics to ensure a smooth execution of tasks.",
    task_description="Monitor and ensure all tasks are completed on time, resolving any logistical issues.",
    task_expected_output="Give a wedding scheduling plan for people, task and time."
)



# Register Agents in Saga
saga.transaction_manager([LT_Agent, TS_Agent, DU_Agent, RM_Agent, CV_Agent, WEO_Agent])

# Execute with rollback enabled
saga.saga_coordinator(with_rollback=True)

# Print intra-agent details
saga.intra_agent()

# Print inter-agent dependencies
saga.inter_agent()

# Select context for an agent
saga.select_context("Resource Management Agent")

# Restore an agent’s execution
saga.restore_context("Resource Management Agent")
