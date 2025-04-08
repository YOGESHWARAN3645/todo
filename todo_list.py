tasks = []

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("5. Exit the application")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("✅ Task added!")

    elif choice == "2":
        if tasks:
            print("\n📝 Your Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("📭 No tasks found.")

    elif choice == "3":
        if tasks:
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"❌ Removed: {removed}")
            else:
                print("⚠️ Invalid task number.")
        else:
            print("📭 No tasks to remove.")

    elif choice == "4":
        confirm = input("⚠️ Are you sure you want to clear all tasks? (yes/no): ").lower()
        if confirm == "yes":
            tasks.clear()
            print("🧹 All tasks cleared!")
        else:
            print("❎ Clear all canceled.")

    elif choice == "5":
        print("👋 Exiting...")
        break

    else:
        print("❌ Invalid choice.")
