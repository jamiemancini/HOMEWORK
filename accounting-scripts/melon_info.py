"""Print out all the melons in our inventory."""


from melons import all_melons


def print_melon(all_melons):
    """Print each melon with corresponding attribute information."""

    for melon, information in all_melons.items():
        print(melon)
    
        for description, values in information.items():
            print(f"       {description:<10}: {values}")
        print()
    

print_melon(all_melons)