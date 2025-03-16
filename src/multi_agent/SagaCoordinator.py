from collections import deque

class SagaCoordinator:
    def __init__(self):
        self.transactions = deque()  # Stores executed transactions
        self.rollback_stack = deque()  # Stack for rollback actions

    def execute(self, agent):
        """Executes an agent and stores its rollback step."""
        try:
            print(f"✅ Running {agent.name}...")
            agent.run()
            self.transactions.append(agent)
            self.rollback_stack.append(agent.rollback)  # Store rollback function
        except Exception as e:
            print(f"❌ Error in {agent.name}: {e}")
            self.rollback()
            raise  # Stop execution

    def rollback(self):
        """Undo executed steps in reverse order."""
        print("🔄 Rolling back transactions...")
        while self.rollback_stack:
            rollback_step = self.rollback_stack.pop()
            rollback_step()
        print("✅ Rollback complete.")
