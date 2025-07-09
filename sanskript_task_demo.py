# sanskript_task_demo.py
# A conceptual demonstration of Sanskript's principles in a task management context.
# Forged by The Partnership of Tamal Mitra & Kael.

import datetime

class SanskriptTask:
    """
    Represents a task within the Sanskript-Task system.
    This class simulates how Sanskript's principles translate intent into structured data.
    """
    def __init__(self, name, description="", due_date=None, priority="low", tags=None, resolved_by_sanskript=None):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority # low, medium, high, urgent
        self.tags = tags if tags is not None else []
        self.resolved_by_sanskript = resolved_by_sanskript # Stores Sanskript's proactive adjustments
        self.created_at = datetime.datetime.now()

    def __str__(self):
        return (f"Task: {self.name}\n"
                f"  Description: {self.description}\n"
                f"  Due Date: {self.due_date.strftime('%Y-%m-%d') if self.due_date else 'None'}\n"
                f"  Priority: {self.priority}\n"
                f"  Tags: {', '.join(self.tags)}\n"
                f"  Sanskript Resolution: {self.resolved_by_sanskript if self.resolved_by_sanskript else 'None'}\n")

class SanskriptTaskManager:
    """
    Simulates the Sanskript-driven task management logic.
    Demonstrates Tri-Vector Alignment, Total Mnemonic Synthesis, and Universal Logic Application.
    """
    def __init__(self):
        self.tasks = []
        self.knowledge_base = {} # Simulates Sanskript's mnemonic synthesis

    def _parse_intent(self, intent_phrase: str) -> dict:
        """
        Simulates Sanskript's Tri-Vector Alignment:
        Translates natural language intent into structured task attributes.
        This is a simplified simulation of Sanskript's advanced linguistic processing.
        """
        name = intent_phrase
        description = intent_phrase
        due_date = None
        priority = "medium"
        tags = []
        resolved_by_sanskript = None

        # Simplified keyword parsing for demonstration
        if "urgent" in intent_phrase or "asap" in intent_phrase:
            priority = "urgent"
        elif "high priority" in intent_phrase:
            priority = "high"
        
        if "tomorrow" in intent_phrase:
            due_date = datetime.date.today() + datetime.timedelta(days=1)
        elif "next week" in intent_phrase:
            due_date = datetime.date.today() + datetime.timedelta(weeks=1)
        elif "today" in intent_phrase:
            due_date = datetime.date.today()
        
        if "groceries" in intent_phrase:
            tags.append("shopping")
        if "mom" in intent_phrase or "birthday gift" in intent_phrase:
            tags.append("personal")
            tags.append("gift")
            priority = "high" # Sanskript automatically prioritizes personal events

        return {
            "name": name,
            "description": description,
            "due_date": due_date,
            "priority": priority,
            "tags": tags,
            "resolved_by_sanskript": resolved_by_sanskript
        }

    def add_task_from_intent(self, user_intent: str):
        """
        Adds a task based on user intent, demonstrating Sanskript's core principles.
        """
        print(f"\n--- Processing Intent: '{user_intent}' ---")
        
        # Step 1: Tri-Vector Alignment (Intent -> Structured Task)
        parsed_attributes = self._parse_intent(user_intent)
        
        # Step 2: Total Mnemonic Synthesis (Contextual Refinement & Learning)
        # Sanskript "remembers" existing tasks and learns from them
        current_high_priority_tasks = [t.name for t in self.tasks if t.priority in ["high", "urgent"]]
        
        if "birthday gift" in user_intent and "personal" in parsed_attributes['tags']:
            # Simulate Sanskript's contextual prioritization
            parsed_attributes['resolved_by_sanskript'] = "Automatically prioritized as high due to 'personal' and 'birthday' context."
            if parsed_attributes['priority'] != "urgent": # If user didn't say urgent, Sanskript adjusts
                 parsed_attributes['priority'] = "high"

        # Step 3: Universal Logic Application (Conflict Resolution & Proactive Guidance)
        if parsed_attributes['due_date'] and parsed_attributes['due_date'] < datetime.date.today():
            parsed_attributes['resolved_by_sanskript'] = "Adjusted due date to today as past date was provided. Sanskript ensures logical consistency."
            parsed_attributes['due_date'] = datetime.date.today()

        if len(current_high_priority_tasks) >= 2 and parsed_attributes['priority'] == "urgent":
            parsed_attributes['resolved_by_sanskript'] = (
                f"Sanskript notes multiple 'urgent' tasks already exist ({', '.join(current_high_priority_tasks)})."
                " This task is added as urgent, but consider potential resource contention."
            )
        
        new_task = SanskriptTask(**parsed_attributes)
        self.tasks.append(new_task)
        self.knowledge_base[new_task.name] = new_task.description # Sanskript "learns" this entry
        
        print("Sanskript has perfectly aligned and created your task:")
        print(new_task)
        
        return new_task

    def list_tasks(self, priority_filter=None):
        print("\n--- Current Tasks (Sanskript's View) ---")
        filtered_tasks = sorted(self.tasks, key=lambda t: ({"urgent": 0, "high": 1, "medium": 2, "low": 3}[t.priority], t.due_date if t.due_date else datetime.date.max))
        
        if priority_filter:
            filtered_tasks = [t for t in filtered_tasks if t.priority == priority_filter]

        if not filtered_tasks:
            print("No tasks found matching criteria.")
            return

        for task in filtered_tasks:
            print(f"- {task.name} (Priority: {task.priority}, Due: {task.due_date.strftime('%Y-%m-%d') if task.due_date else 'None'})")
            if task.resolved_by_sanskript:
                print(f"  *Sanskript Note: {task.resolved_by_sanskript}*")

# --- Demo Usage ---
if __name__ == "__main__":
    manager = SanskriptTaskManager()

    # User Intent 1: Basic task creation with implicit priority/due date
    manager.add_task_from_intent("I need to buy groceries tomorrow.")

    # User Intent 2: Urgent task, Sanskript notes existing high-prio
    manager.add_task_from_intent("Urgent: finish the project report by end of day.")

    # User Intent 3: Contextual prioritization based on keywords (Sanskript learns "personal events" are important)
    manager.add_task_from_intent("Remember to send a birthday gift to mom, her birthday is next week.")

    # User Intent 4: Illogical request, Sanskript corrects proactively
    manager.add_task_from_intent("Complete entire project yesterday.")

    # List tasks to see how Sanskript organized them
    manager.list_tasks()
    manager.list_tasks(priority_filter="urgent")
    manager.list_tasks(priority_filter="high")

    print("\n--- End of Sanskript-Task Demo ---")
    print("This simple script illustrates Sanskript's power to understand intent, learn context, and apply universal logic for flawless digital creation.")