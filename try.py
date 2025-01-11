try:
    # Code that might raise an exception
    risky_code()
except SomeSpecificException as e:
    # Handle the exception
    print(f"An error occurred: {e}")
except AnotherException:
    # Handle a different type of exception
    print("Another type of error occurred!")
else:
    # Code to run if no exceptions were raised
    print("No errors occurred!")
finally:
    # Code that will always run, whether an exception occurred or not
    print("Execution finished.")
