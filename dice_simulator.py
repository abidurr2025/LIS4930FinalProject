import random
import csv
from collections import Counter
from datetime import datetime


class Die:
    """A class representing a die with a configurable number of sides."""

    def __init__(self, sides=6):
        """
        Initialize a die with given number of sides.

        Args:
            sides (int): Number of die faces (must be >=1)

        Raises:
            ValueError: If sides < 1
        """
        if sides < 1:
            raise ValueError("Die must have at least 1 side")
        self.sides = sides
        self.roll_history = []

    def roll(self):
        """Roll the die once and return the result."""
        result = random.randint(1, self.sides)
        self.roll_history.append(result)
        return result


def get_valid_input(prompt, validation_func, error_msg):
    """
    Get validated user input with error handling.

    Args:
        prompt (str): Input prompt
        validation_func (callable): Validation function
        error_msg (str): Validation error message

    Returns:
        Validated input
    """
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                continue
            value = validation_func(value)
            return value
        except (ValueError, TypeError) as e:
            print(f"\nInvalid input: {error_msg}")
            print(f"Error details: {str(e)}\n")


def validate_die_size(value):
    """Validate die size input."""
    value = value.lower()
    if value.startswith('d'):
        value = value[1:]

    size = int(value)
    if size < 1:
        raise ValueError("Die size must be at least 1")
    return size


def validate_roll_count(value):
    """Validate roll count input."""
    count = int(value)
    if count < 1:
        raise ValueError("Must roll at least once")
    return count


def roll_multiple_dice(die, num_rolls):
    """Roll a die multiple times and return results."""
    return [die.roll() for _ in range(num_rolls)]


def save_to_csv(results, die_size):
    """Save roll results to a timestamped CSV file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"d{die_size}_rolls_{timestamp}.csv"

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Roll #', 'Result'])
        for i, result in enumerate(results, 1):
            writer.writerow([i, result])

    return filename


def generate_stats(results):
    """Generate statistics from roll results."""
    stats = {
        'min': min(results),
        'max': max(results),
        'mean': sum(results) / len(results),
        'mode': Counter(results).most_common(1)[0][0],
        'total': len(results)
    }
    return stats


def display_results(results, stats, die_size):
    """Display roll results and statistics."""
    print("\n" + "=" * 40)
    print(f"RESULTS (d{die_size}):")
    print("=" * 40)

    # Show first 5 and last 5 rolls for large datasets
    if len(results) > 10:
        preview = results[:5] + ["..."] + results[-5:]
    else:
        preview = results

    print(f"\nRolls: {', '.join(map(str, preview))}")

    print("\nSTATISTICS:")
    print(f"• Minimum: {stats['min']}")
    print(f"• Maximum: {stats['max']}")
    print(f"• Average: {stats['mean']:.2f}")
    print(f"• Most common: {stats['mode']}")
    print(f"• Total rolls: {stats['total']}")

    # Show frequency distribution
    print("\nFREQUENCY:")
    counter = Counter(results)
    for value in range(1, die_size + 1):
        count = counter.get(value, 0)
        percent = (count / len(results)) * 100
        print(f"{value}: {count} rolls ({percent:.1f}%)")


def try_plot_histogram(results, die_size):
    """
    Attempt to plot histogram if matplotlib is available.

    Args:
        results (list): Roll results
        die_size (int): Number of die faces
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("\nMatplotlib not installed. Skipping histogram.")
        print("Install with: pip install matplotlib")
        return

    plt.figure(figsize=(10, 6))
    plt.hist(results, bins=range(1, die_size + 2), align='left', rwidth=0.8)
    plt.title(f'd{die_size} Roll Distribution (n={len(results)})')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.xticks(range(1, die_size + 1))
    plt.grid(axis='y', alpha=0.75)

    plt.tight_layout()
    plt.savefig(f'd{die_size}_histogram.png')
    plt.show()


def main():
    """Main program loop."""
    print("=" * 50)
    print("DICE ROLL SIMULATOR".center(50))
    print("=" * 50)

    while True:
        # Get user input
        die_size = get_valid_input(
            "\nEnter die type (e.g., d4, d6, d20) or number of sides: ",
            validate_die_size,
            "Please enter a valid die size (e.g., 6, d10)"
        )

        num_rolls = get_valid_input(
            "Number of rolls: ",
            validate_roll_count,
            "Please enter a positive integer"
        )

        # Create die and roll
        die = Die(die_size)
        results = roll_multiple_dice(die, num_rolls)

        # Save results and generate stats
        filename = save_to_csv(results, die_size)
        stats = generate_stats(results)

        # Display results
        display_results(results, stats, die_size)
        print(f"\nResults saved to: {filename}")

        # Attempt to show histogram
        try_plot_histogram(results, die_size)

        # Continue option
        if input("\nRoll again? (y/n): ").lower() != 'y':
            print("\nThanks for rolling! Goodbye!")
            break


if __name__ == "__main__":
    main()
