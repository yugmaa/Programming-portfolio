def main():
    log = []
    os.system('cls') # clears the screen
    user_name = input("\t\t\t\t\t\t\tEnter your name: ") # prompts user name
    os.system('cls')

    # displaying the greeting message
    print(f"\t\t\t\t\t\t\t UNIVERSITY OF POPPLETON")
    print(f"\t\t\t\t\t\t\tVIRTUAL ASSISTANT SERVICE\n")
    print(f"\n\t\t\t\tHello, {user_name}! Welcome to University of Poppleton's virtual assistant service. ")
    print(f"\t\t\t\tI'm {agent_name}. I will be your assistant for this virtual session. Nice to meet you!")
    print(f"\t\t\t\t\t\t\tFeel free to ask me anything!")

    # adding information to chat log list to store in file later
    log.append(f"\n--------------------------")
    log.append(f"User name: {user_name}\nAgent name: {agent_name}")
    log.append(f"--------------------------")

    while True:
        query = input(f"\t{user_name}: ").strip()
        log.append(f"{user_name}: {query}") # adds user query in the log list
        query = query.lower()

        # detects if the user wants to quit. 
        if query in ["bye", "quit", "exit", "goodbye"]:
            print(f"\t{agent_name}: Goodbye, {user_name}! Have a nice day!")
            log.append("Chat ended by user.")
            break
