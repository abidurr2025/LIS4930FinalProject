import random
import csv
import os


class DiceSimulator:
    def __init__(self, sides, rolls):
        self.sides = sides
        self.rolls = rolls
        self.frequencies = [0] * sides  # Initialize frequency tracker for each face

    def roll_die(self):
        return random.randint(1, self.sides)  # Simulate a single die roll

    def run_experiment(self):
        for _ in range(self.rolls):
            face = self.roll_die()
            self.frequencies[face - 1] += 1  # Increment frequency of the rolled face

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Face', 'Frequency'])  # CSV header
            for face, freq in enumerate(self.frequencies, start=1):
                writer.writerow([face, freq])  # Write face-frequency pairs

    def load_from_csv(self, filename):
        if not os.path.exists(filename):
            return False
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            self.frequencies = []
            for row in reader:
                self.frequencies.append(int(row[1]))  # Load frequencies from CSV
        return True

    def analyze_distribution(self):
        max_freq = max(self.frequencies)
        print("\nDistribution Analysis (ASCII Histogram):")
        for face, freq in enumerate(self.frequencies, start=1):
            bar = '█' * int((freq / max_freq) * 50)  # Scale bar to 50 characters max
            print(f"Face {face}: {bar} {freq} rolls")

    def chi_squared_test(self, alpha=0.05):
        expected = self.rolls / self.sides  # Expected frequency per face
        chi_sq = sum((freq - expected) ** 2 / expected for freq in self.frequencies)  # χ² = Σ[(O-E)²/E]
        critical_value = 12.592  # Pre-calculated for α=0.05 and 6 degrees of freedom (adjust if sides≠6)
        print(f"\nChi-Squared Test (α=0.05):")
        print(f"χ² = {chi_sq:.2f}, Critical Value = {critical_value}")
        return chi_sq > critical_value  # True if die is biased

    def deviation_analysis(self):
        expected = self.rolls / self.sides
        print("\nDeviation Analysis:")
        for face, freq in enumerate(self.frequencies, start=1):
            dev_abs = freq - expected
            dev_pct = (dev_abs / expected) * 100
            print(f"Face {face}: {dev_abs:+.2f} ({dev_pct:+.2f}%) deviation")


def main():
    # User inputs
    sides = int(input("Enter number of die sides: "))
    rolls = int(input("Enter number of rolls: "))
    filename = "dice_data.csv"

    # Run experiment and save data
    simulator = DiceSimulator(sides, rolls)
    simulator.run_experiment()
    simulator.save_to_csv(filename)
    print(f"\nSaved data to {filename}.")

    # Reload data and analyze
    if simulator.load_from_csv(filename):
        simulator.analyze_distribution()
        if simulator.chi_squared_test():
            print("Result: Die is biased (reject H₀).")
        else:
            print("Result: Die is fair (fail to reject H₀).")
        simulator.deviation_analysis()
    else:
        print("Error loading data.")


main()
