from pyscript import document, display, HTML

# Non-metals dictionary storing required attributes
nonmetals = {
    "H": {"name": "Hydrogen", "number": 1, "mass": 1.008},
    "He": {"name": "Helium", "number": 2, "mass": 4.0026},
    "C": {"name": "Carbon", "number": 6, "mass": 12.011},
    "N": {"name": "Nitrogen", "number": 7, "mass": 14.007},
    "O": {"name": "Oxygen", "number": 8, "mass": 15.999},
    "F": {"name": "Fluorine", "number": 9, "mass": 18.998},
    "Ne": {"name": "Neon", "number": 10, "mass": 20.180},
    "P": {"name": "Phosphorus", "number": 15, "mass": 30.974},
    "S": {"name": "Sulfur", "number": 16, "mass": 32.06},
    "Cl": {"name": "Chlorine", "number": 17, "mass": 35.45},
    "Ar": {"name": "Argon", "number": 18, "mass": 39.948},
    "Se": {"name": "Selenium", "number": 34, "mass": 78.971},
    "Br": {"name": "Bromine", "number": 35, "mass": 79.904},
    "Kr": {"name": "Krypton", "number": 36, "mass": 83.798},
    "I": {"name": "Iodine", "number": 53, "mass": 126.90},
    "Xe": {"name": "Xenon", "number": 54, "mass": 131.29},
    "At": {"name": "Astatine", "number": 85, "mass": 210},
    "Rn": {"name": "Radon", "number": 86, "mass": 222},
    "Ts": {"name": "Tennessine", "number": 117, "mass": 294},
    "Og": {"name": "Oganesson", "number": 118, "mass": 294},
    "Fe": {"name": "Iron", "number": 26, "mass": 55.845},
    "B": {"name": "Boron", "number": 5, "mass": 10.81}
}

def check_element(event):
    # Retrieve user input and normalize casing
    user_input = document.querySelector("#symbol_input").value.strip().capitalize()
    
    # Nested .get() retrieval without if statements
    info = nonmetals.get(user_input, {})
    elem_name = info.get("name")
    elem_number = info.get("number")
    elem_mass = info.get("mass")
    
    # Join detailed output using HTML line breaks (<br>)
    found_output = "<br>".join([
        f"Symbol: {user_input}",
        f"Element: <i>{elem_name}</i>",
        f"Atomic Number: {elem_number}",
        f"Atomic Mass: {elem_mass}"
    ])
    
    # Format fallback error message
    not_found_output = f"The element '{user_input}' doesn't exist in the list."

# unexplained code    
    # Boolean indexing trick to avoid if/else statements
    has_key = int(user_input in nonmetals)
    final_output = [not_found_output, found_output][has_key]
    
    # Wrap string in HTML() so PyScript renders <br> properly without errors
    display(HTML(final_output), target="output1", append=False)