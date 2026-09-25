class IncidentTicket:
    def __init__(self, incident_id, bot, description):
        self.__incident_id = incident_id
        self.__bot = bot
        self.__description = description

    def get_incident_id(self):
        return self.__incident_id

    def get_bot(self):
        return self.__bot

    def get_description(self):
        return self.__description

    def display_ticket(self):
        print("Incident ID:", self.__incident_id)
        print("Bot:", self.__bot)
        print("Description:", self.__description)
        print("------------------------------")


class IncidentTicketManager:
    def __init__(self):
        self.tickets = []

    def add_ticket(self):
        print()
        print("===== ADD INCIDENT TICKET =====")

        incident_id = input("Enter Incident ID: ")
        bot = input("Enter Bot: ")
        description = input("Enter Short Description: ")

        ticket = IncidentTicket(incident_id, bot, description)
        self.tickets.append(ticket)

        print()
        print("Ticket added successfully!")

    def display_tickets(self):
        print()
        print("===== ACTIVE INCIDENT TICKETS =====")

        if len(self.tickets) == 0:
            print("No active incident tickets.")
        else:
            for ticket in self.tickets:
                ticket.display_ticket()

    def search_ticket(self):
        print()
        print("===== SEARCH INCIDENT TICKET =====")

        incident_id = input("Enter Incident ID to search: ")

        for ticket in self.tickets:
            if ticket.get_incident_id() == incident_id:
                print()
                print("Ticket Found!")
                ticket.display_ticket()
                return

        print()
        print("Ticket not found.")

    def remove_ticket(self):
        print()
        print("===== REMOVE RESOLVED TICKET =====")

        incident_id = input("Enter Incident ID to remove: ")

        for ticket in self.tickets:
            if ticket.get_incident_id() == incident_id:
                self.tickets.remove(ticket)

                print()
                print("Ticket removed successfully!")
                return

        print()
        print("Ticket not found.")

    def count_tickets(self):
        print()
        print("===== ACTIVE TICKET COUNT =====")
        print("Total Active Incident Tickets:", len(self.tickets))


manager = IncidentTicketManager()


# Sample Data

manager.tickets.append(IncidentTicket("INC1392939", "BOT-Inventory", "Failed to generate the daily report"))
manager.tickets.append(IncidentTicket("INC1392940", "BOT-Email", "Failed to send the scheduled notification"))
manager.tickets.append(IncidentTicket("INC1392941", "BOT-DataSync", "Encountered an error during data transfer"))
manager.tickets.append(IncidentTicket("INC1392942", "BOT-Invoice", "Failed to process an invoice"))
manager.tickets.append(IncidentTicket("INC1392943", "BOT-Report", "Failed to generate the weekly report"))
manager.tickets.append(IncidentTicket("INC1392944", "BOT-FileTransfer", "Failed to upload the required file"))
manager.tickets.append(IncidentTicket("INC1392945", "BOT-DataEntry", "Encountered an error while entering records"))
manager.tickets.append(IncidentTicket("INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"))
manager.tickets.append(IncidentTicket("INC1392947", "BOT-Validation", "Failed to validate the submitted records"))
manager.tickets.append(IncidentTicket("INC1392948", "BOT-Notification", "Failed to send the system alert"))


# Menu

while True:
    print()
    print("==============================================")
    print("    IT AUTOMATION INCIDENT TICKET MANAGER")
    print("==============================================")
    print("1. Add Incident Ticket")
    print("2. Display All Active Tickets")
    print("3. Search for a Ticket")
    print("4. Remove Resolved Ticket")
    print("5. Count Active Tickets")
    print("6. Exit")
    print("==============================================")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        manager.add_ticket()

    elif choice == "2":
        manager.display_tickets()

    elif choice == "3":
        manager.search_ticket()

    elif choice == "4":
        manager.remove_ticket()

    elif choice == "5":
        manager.count_tickets()

    elif choice == "6":
        print()
        print("Program ended.")
        break

    else:
        print()
        print("Invalid choice. Please try again.")