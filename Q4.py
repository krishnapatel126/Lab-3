main_string = input("Enter a String: ")
to_remove = input("Enter String to be removed: ")
if to_remove in main_string:
    main_string = main_string.replace(to_remove, "")
print(main_string)
