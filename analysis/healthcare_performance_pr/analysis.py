import pandas as pd
import matplotlib.pyplot as plt

TARGET = 4.5

def main():
    df = pd.read_csv("data/patient_satisfaction_2024.csv")
    df["DeltaToTarget"] = df["PatientSatisfaction"] - TARGET
    df["QoQChange"] = df["PatientSatisfaction"].diff()
    avg = round(df["PatientSatisfaction"].mean(), 1)
    print("Average:", avg)  # should be 2.1
    print("QoQ changes:", df["QoQChange"].fillna(0).round(2).tolist())
    print("Quarters below target:", int((df["PatientSatisfaction"] < TARGET).sum()))
    # Trend line
    plt.figure()
    plt.plot(df["Quarter"], df["PatientSatisfaction"], marker="o")
    plt.axhline(y=TARGET, linestyle="--")
    plt.title("Patient Satisfaction Score – 2024 Trend vs Target")
    plt.xlabel("Quarter")
    plt.ylabel("Score")
    for i, v in enumerate(df["PatientSatisfaction"]):
        plt.annotate(f"{v}", (df["Quarter"][i], v), textcoords="offset points", xytext=(0,8), ha='center')
    plt.savefig("figures/trend_vs_target.png", bbox_inches="tight")
    plt.close()
    # Bars
    plt.figure()
    plt.bar(df["Quarter"], df["PatientSatisfaction"])
    plt.axhline(y=TARGET, linestyle="--")
    plt.title("Quarterly Patient Satisfaction – Benchmark Comparison")
    plt.xlabel("Quarter")
    plt.ylabel("Score")
    plt.savefig("figures/quarterly_bars.png", bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    main()
