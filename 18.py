# Program to demonstrate variable scope

global_var = "Global Variable"

def outer():
    outer_var = "Outer Variable"

    def inner():
        nonlocal outer_var
        local_var = "Local Variable"

        print("Local:", local_var)
        print("Nonlocal:", outer_var)
        print("Global:", global_var)

        outer_var = "Modified Outer Variable"

    inner()
    print("After modification:", outer_var)

outer()
