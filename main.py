from pyscript import display, document

NMElements = { # dicionary that stores all the elements and tuple for the values stored
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.065), 
    "Cl": ("Chlorine", 17, 35.453),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.960),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90),
    "Xe": ("Xenon", 54, 131.29),
    "At": ("Astatine", 85, 210),
    "Rn": ("Radon", 86, 222),
    "Ts": ("Tennessine", 117, 294),
    "Og": ("Oganesson", 118, 294),
}


def element_checker(e): # runs when user clicks a button

    document.getElementById("result").innerHTML = "" # clears the results

    element1 = document.getElementById("element_name").value.strip().capitalize() # ensures that whatever the user typed is in correct format

    result = NMElements.get( # gets the element from the dictionary and if its not there it shows element not found
        element1, ("Element not found", "-", "-")
    )

    if result[0] == "Element not found": # js shows that the element isnt from the dictionary same for line 39 to 42

        document.getElementById("result").innerHTML = """   
        <b>Result:</b> Element not found.<br>
        Please enter a valid non-metal symbol.
        """

    else: # if the element the user input is there it will show the stuff below from 46 to 51

        document.getElementById("result").innerHTML = f""" 
        <b>Symbol:</b> {element1}<br>
        <b>Element Name:</b> {result[0]}<br>
        <b>Atomic Number:</b> {result[1]}<br>
        <b>Atomic Mass:</b> {result[2]}
        """