"""src/datafun/newapp.py - Project script.

Author: Julie Tietz
Date: 2026-08-26

HOW TO RUN THIS FILE:

From the VS Code menu (with only this project open in VS Code),
click "Terminal" / New Terminal to
open an integrated Terminal in the root project folder.
Paste the following command and press ENTER or RETURN
to run this file as a script:

uv run python -m datafun.newapp

DOMAIN:

A dataset of penguins.
See docs/data-card.md for more information about the dataset.

EXPLORE:

The data is loaded from a CSV file in the data/ folder.
Open that CSV in Excel and look at it.
One row of data represents one penguin.
We can
- open Excel and explore data OR
- open an editor and write Python

With Python, the instructions are write once / use as many times
as we like, and we can copy the instructions to other projects.
Work can be stored in GitHub and shared with others.

ORGANIZATION:

This file is the main script for the project.
Execution begins at the start of the main() function.
We organize the instructions into different files
(a Python file is called a module).
"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path
import pandas as pd

# Load the penguins dataset from the CSV file into a pandas DataFrame.
penguins = pd.read_csv("data/newpenguins.csv")

from datafun.utils_data import inspect

# === CONFIGURE LOGGER ONCE FOR THE APPLICATION ===

LOG: logging.Logger = get_logger("P01", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS ===

# Some global variables are CONSTANT, # they do NOT change when the program runs.
# By convention, constants are named in # UPPERCASE_WITH_UNDERSCORES.
# `Final` is added to indicate these variables # should not be reassigned.

# === PATHS ARE IMPORTANT ===

# Clearly define relative paths to important items (like data files).
# The `Python Standard Library` is available in every Python project.

# One of the modules in the Python Standard Library is `pathlib`,
# which provides classes for handling filesystem paths.

# === LOCATE THE DATA FILE ===

# Use the Path() constructor to create a Path object representing the "data" folder.
# Combine with the CSV file name
# to get the full path to the data file.
DATA_FILE_PATH: Final[Path] = Path("data") / "newpenguins.csv"

# === OPEN THE DATA FILE IN EXCEL ===

# Look in the data/ folder. Open the file in Excel.
# Understand what is there and record your observations.

# === DETERMINE WHAT A ROW REPRESENTS ===

# CUSTOM: This is the GRAIN of the dataset - the single most
# important thing to know about any dataset.
# Come up with a short phrase that describes it.
# Fill this string value AFTER exploring the data.
GRAIN: Final[str] = "one penguin"  # CUSTOM


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Entry point when running this file as a Python script.

    This is where the instructions begin.

    Arguments: None.
    Returns: None.
    """
    log_header(LOG, "P01")

    LOG.info("===================================")
    LOG.info("START main()")
    LOG.info("===================================")

    LOG.info("-------------------------------")
    LOG.info("01. LOAD the data.")
    LOG.info("-------------------------------")

    # Use the imported privacy-preserving log_path() function
    # To indicate where we will look for the data file.
    log_path(LOG, "data file", path=DATA_FILE_PATH)

    # Call the built-in pandas `read_csv` function.
    # Store the tabular pandas DataFrame returned
    # in a local variable named `df`.

    df: pd.DataFrame = pd.read_csv(DATA_FILE_PATH)

    LOG.info("Data loaded successfully.")

    LOG.info("-------------------------------")
    LOG.info("02. INSPECT the data.")
    LOG.info("-------------------------------")

    # Call the inspect() function to get a string
    # with basic information about the DataFrame.
    # Pass in the pandas DataFrame (df)
    # The grain (what one row represents)
    # And the log so it knows where to send messages.

    inspection_string: str = inspect(df=df, grain=GRAIN, log=LOG)

    LOG.info(inspection_string)

    LOG.info("-------------------------------")
    LOG.info("03. DESCRIBE the data.")
    LOG.info("-------------------------------")

    # Calculate the average mass of each species of penguin using the pandas `groupby` method.
    # Display the result in a table format using the `print` function.
    average_mass = penguins.groupby("species", as_index=False)["body_mass_g"].mean()

    print(average_mass)

    LOG.info("===================================")
    LOG.info("END main() - Executed successfully!")
    LOG.info("===================================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: This is standard Python "boilerplate" - we copy and paste it
# into every Python script. It is a "conditional execution" guard,
# meaning: if this file is being run as a script, then execute the code
# in the main() function.

if __name__ == "__main__":
    main()
