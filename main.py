#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Standard libraries.
import sys  # For program termination.
import matplotlib.pyplot as plt  # For data visualization.

import pandas as pd  # For data manipulation.


class SGR:
    """Container class for Select Graphic Rendition style codes."""
    BOLD = "1"
    ITALIC = "3"
    UNDERLINE = "4"
    BLINK = "5"
    INVERT = "7"
    STRIKE = "9"
    NOT_BOLD = "22"
    NOT_ITALIC = "23"
    NOT_UNDERLINE = "24"
    NOT_BLINK = "25"
    NOT_INVERT = "27"
    NOT_STRIKE = "29"
    RESET_ALL = "0"

    BLACK_F = "30"
    RED_F = "31"
    GREEN_F = "32"
    YELLOW_F = "33"
    BLUE_F = "34"
    MAGENTA_F = "35"
    CYAN_F = "36"
    WHITE_F = "37"
    B_BLACK_F = "90"
    B_RED_F = "91"
    B_GREEN_F = "92"
    B_YELLOW_F = "93"
    B_BLUE_F = "94"
    B_MAGENTA_F = "95"
    B_CYAN_F = "96"
    B_WHITE_F = "97"
    RESET_F = "39"

    BLACK_B = "40"
    RED_B = "41"
    GREEN_B = "42"
    YELLOW_B = "43"
    BLUE_B = "44"
    MAGENTA_B = "45"
    CYAN_B = "46"
    WHITE_B = "47"
    B_BLACK_B = "100"
    B_RED_B = "101"
    B_GREEN_B = "102"
    B_YELLOW_B = "103"
    B_BLUE_B = "104"
    B_MAGENTA_B = "105"
    B_CYAN_B = "106"
    B_WHITE_B = "107"
    RESET_B = "49"


# Create useful constants for pretty terminal text.
CSI = "\x1b["
RESET_ALL = CSI + SGR.RESET_ALL + "m"
ENTER = CSI + SGR.B_GREEN_F + "mENTER" + RESET_ALL
X_BUTTON = CSI + SGR.B_RED_B + "m" + CSI + SGR.B_WHITE_F + "m[X]" + RESET_ALL
LEGO = CSI + SGR.B_RED_F + "mL" + CSI + SGR.B_YELLOW_F + "mE" + \
       CSI + SGR.B_GREEN_F + "mG" + CSI + SGR.B_BLUE_F + "mO" + RESET_ALL


def main() -> None:
    """Run the main program."""
    # Load in the data set from the file.
    print(f"Reading {LEGO} set data from file...", end="")
    try:
        # Have pandas load in the data.
        lego_sets = pd.read_csv("sets.csv")
        # Show the user it was a success.
        print("complete!")
    except OSError as ex:
        # Show the user that the data loading failed and why.
        print(f"failed!\n{CSI + SGR.RED_F}mError reading file: {ex.__class__.__name__} {ex}{CSI + SGR.RESET_ALL}m")
        # Exit with an error code to show something went wrong.
        sys.exit(1)
    # Explain the program to the user.
    print(f"This is an interactive data viewing program for {LEGO} sets.")
    print(f"Follow along and you might learn something about {LEGO}s!")
    input(f"Press {ENTER} to view the data overview:")
    # Print a data overview which includes the data structure.
    print("Data information:")
    lego_sets.info(memory_usage="deep")
    print("Total bytes in use:", lego_sets.memory_usage(deep=True).sum(), "B")
    input(f"Press {ENTER} when ready to view the data:")
    # Obtain just the year and num_parts columns together.
    parts_by_year = lego_sets[["year", "num_parts"]]
    # Create useful data sets.
    year_parts_dict: dict[int, int] = {}
    year_parts_list: list[tuple[int, int]] = []
    # Aggregate the piece count by year.
    for i, row in parts_by_year.iterrows():
        if row["year"] in year_parts_dict:
            year_parts_dict[row["year"]] += row["num_parts"]
        else:
            year_parts_dict[row["year"]] = row["num_parts"]
    # Add them as tuples into a list for sorting.
    for year, parts in year_parts_dict.items():
        year_parts_list.append((parts, year))
    # Sort the list in place in descending order so item zero is the largest year for piece count.
    year_parts_list.sort(reverse=True)
    # Explain the data to the user.
    print("How has piece count changed over time?")
    print("What are the biggest years for piece count?")
    input(f"Press {ENTER} to see the top ten years for piece count:")
    # Display the top ten years.
    # This is the first ten items in the sorted list.
    print("Year: # of pieces")
    i = 0
    for parts, year in year_parts_list:
        i += 1
        if i > 10:
            break
        print(f"{year}: {parts}")
    # Create a plot of piece count by year using matplotlib.
    parts_by_year.plot(kind="scatter", x="year", y="num_parts")
    # Explain the chart to the user.
    print("Wow! That is a lot of pieces!")
    print(f"It sure looks like {LEGO} sets get more complex every year, but let's see if that is true...")
    print("Here is a scatterplot showing piece count for each set according to year.")
    # Explain how to exit the plot.
    print(f"Press {X_BUTTON} on the window when done viewing.")
    input(f"Press {ENTER} to see the plot:")
    # Set up the plot title and display it.
    plt.title("Piece Count Per Set By Year")
    plt.show()
    # Time for the next data question.
    years = lego_sets["year"]
    # Count how many times year appears, which tells us how many sets were released in that year.
    sets_per_year = years.value_counts(sort=False)
    # Sort the years by time in place.
    sets_per_year.sort_index(inplace=True)
    # Create a plot of the sets per year using matplotlib.
    sets_per_year.plot(kind="bar", x="year")
    # Explain the previous chart to the user.
    print(f"It looks like the average piece count for {LEGO} sets has been trending upwards as time goes on!")
    input(f"Press {ENTER} to continue to the next visualization:")
    # Introduce the next chart to the user.
    print(f"How many {LEGO} sets release by year?")
    print("Does it trend downwards, upwards, or stay constant?")
    print("Here is a bar chart showing the number of sets released per year.")
    # Explain how to exit the plot.
    print(f"Press {X_BUTTON} on the window when done viewing.")
    input(f"Press {ENTER} to see the chart:")
    # Set up the plot title and display it.
    plt.title("LEGO Sets Released Per Year")
    plt.show()
    # Explain the previous plot to the user.
    print(f"It looks like {LEGO} has been releasing more sets per year as well!")
    print(f"This means that {LEGO} sets have been getting more complex as their numbers increase!")
    # Thank the user for interacting with the program.
    print("Thank you for interacting with this program!")
    print(f"I hope you learned something about {LEGO}s!")


# If this script is being run directly.
if __name__ == '__main__':
    # Run the main program.
    main()
