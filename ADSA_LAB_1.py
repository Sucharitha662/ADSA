#Implement a Singly linked List to Manage Patient Details(Name, Age ,ID). Perform Insertion and Deletion

class PatientNode:
    def __init__(self, name, age, patient_id):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.next = None

class PatientLinkedList:
    def __init__(self):
        self.head = None

    def insert_patient(self, name, age, patient_id):
        new_node = PatientNode(name, age, patient_id)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f" Inserted: {name}, Age: {age}, ID: {patient_id}")

    def delete_patient(self, patient_id):
        current = self.head
        previous = None
        while current:
            if current.patient_id == patient_id:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print(f" Deleted patient with ID: {patient_id}")
                return
            previous = current
            current = current.next
        print(f" Patient with ID {patient_id} not found.")

    def display_patients(self):
        if self.head is None:
            print(" No patients in the list.")
            return
        print(" Patient List:")
        current = self.head
        while current:
            print(f" Name: {current.name}, Age: {current.age}, ID: {current.patient_id}")
            current = current.next

# Example usage
if __name__ == "__main__":
    plist = PatientLinkedList()
    plist.insert_patient("Alice", 30, 101)
    plist.insert_patient("Bob", 45, 102)
    plist.insert_patient("Charlie", 25, 103)

    plist.display_patients()

    plist.delete_patient(102)
    plist.display_patients()
    plist.delete_patient(84)
    plist.display_patients()