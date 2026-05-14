import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
            risks.append("High BP")

        if self.sugar > 140:
            risks.append("Diabetes")

        if len(risks) == 0:
            risks.append("Normal")

        return ", ".join(risks)

patients = []

n = int(input("Enter number of patients: "))

for i in range(n):

    print("\nPatient", i+1)
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    bp = int(input("Enter Blood Pressure: "))
    sugar = int(input("Enter Sugar Level: "))

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


# Create DataFrame
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
print("BP Standard Deviation:", np.std(bp_values))

print()

print("Average Sugar:", np.mean(sugar_values))
print("Maximum Sugar:", np.max(sugar_values))
print("Minimum Sugar:", np.min(sugar_values))
print("Sugar Standard Deviation:", np.std(sugar_values))

# Save report
df.to_csv("health_report.csv", index=False)

print("\nCSV Report Saved")

# ------------------------
# MATPLOTLIB
# ------------------------

plt.figure(figsize=(8,5))

plt.bar(df["Name"], df["BP"])

plt.title("Patient Blood Pressure")

plt.xlabel("Patient Name")

plt.ylabel("BP")

plt.savefig("bp_chart.png")

plt.close()


plt.figure(figsize=(8,5))

plt.plot(df["Name"],df["Sugar"])

plt.title("Sugar Levels")

plt.xlabel("Patient Name")

plt.ylabel("Sugar")

plt.grid()

plt.savefig("sugar_chart.png")

plt.close()

# ------------------------
# SEABORN
# ------------------------

sns.scatterplot(
    x=df["BP"],
    y=df["Sugar"]
)

plt.title("BP vs Sugar")

plt.show()

sns.boxplot(
    x=df["BP"]
)

plt.title("BP Distribution")

plt.savefig("heatmap_chart.png")

plt.close()

sns.countplot(
    x=df["Risk"]
)

plt.title("Risk Category Count")

plt.show()

correlation = df[["Age","BP","Sugar"]].corr()
sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()
