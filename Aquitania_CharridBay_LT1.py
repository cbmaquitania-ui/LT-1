total_notebooks = float(input("What is the total number of notebooks? "))
fit_in_box = float(input("How many notebooks fit in one box? "))

print("The total number of notebooks is", round(total_notebooks), ", and you can fit", round(fit_in_box), "in one box.")

full_boxes = print("The number of full boxes is", round(total_notebooks) // round(fit_in_box))
loose_notebooks = print("The number of loose notebooks is", round(total_notebooks) % round(fit_in_box))

#This kind of case needs its own code so that the order is clear.
if total_notebooks < fit_in_box:
    print("No box was filled.")