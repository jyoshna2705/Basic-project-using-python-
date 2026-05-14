import numpy as np
import pandas as pd

# Patient Class
class Patient:

    def __init__(self, name, age, bp, sugar):
        self.name = name
        self.age = age
        self.bp = bp
        self.sugar = sugar

    def check_risk(self):

        risks = []

        if self.bp > 140:
            risks.append("High BP Risk")

        if self.sugar > 140:
            risks.append("Diabetes Risk")

        if len(risks) == 0:
            risks.append("Normal")

        return ", ".join(risks)


patients = []

n = int(input("Enter number of patients: "))

for i in range(n):

    print("\nPatient", i+1)

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    bp = int(input("Enter BP: "))
    sugar = int(input("Enter sugar level: "))

    p = Patient(name, age, bp, sugar)

    patients.append(p)


# Store data for Pandas
data = {
    "Name": [],
    "Age": [],
    "BP": [],
    "Sugar": [],
    "Risk": []
}

for p in patients:

    data["Name"].append(p.name)
    data["Age"].append(p.age)
    data["BP"].append(p.bp)
    data["Sugar"].append(p.sugar)
    data["Risk"].append(p.check_risk())


df = pd.DataFrame(data)

print("\n------ Patient Report ------")
print(df)


# NumPy Statistics
bp_values = np.array(data["BP"])
sugar_values = np.array(data["Sugar"])

print("\n------ Health Statistics ------")

print("Average BP:", np.mean(bp_values))
print("Maximum BP:", np.max(bp_values))
print("Minimum BP:", np.min(bp_values))

print("Average Sugar:", np.mean(sugar_values))
print("Maximum Sugar:", np.max(sugar_values))
print("Standard Deviation Sugar:", np.std(sugar_values))


