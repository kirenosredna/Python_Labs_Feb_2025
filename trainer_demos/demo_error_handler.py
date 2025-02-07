#! /usr/bin/env python3
# Author: DCameron
# Description: This script will generate 6 RANDOM lottery numbers.
"""
    Docstring:
"""
import re
import sys

class BillandTed(BaseException):
    pass

# Example of a user function with parameter passing
# and default values
def search_pattern(pattern=r"^.{19}$", file=r"c:\labs\words"):
    # assert file != None, "No filename given for search_pattern"
    if not file:
        raise BillandTed('Excellent')

    lines = 0
    try:
        fh_in = open(file, mode="rt")
    except PermissionError as err:
        print(f"Error code={err.args[0]}, {err.args[1]}, {err.filename}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as err:
        print(f"Error code={err.args[0]}, {err.args[1]}, {err.filename}", file=sys.stderr)
        sys.exit(2)
    except BaseException as err:
        print("Error occurred, investigate", file=sys.stderr)
        sys.exit(3)
    else:
        # Executes if try block succeeds
        reobj = re.compile(pattern) # Compile pattern ONCE
        for line in fh_in:
            m = reobj.search(line)
            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")
    finally:
        print("And now for something completely different..")
        fh_in.close()
    return lines

def main():
    search_pattern(file=None)
    return None

if __name__ == "__main__":
    main()

