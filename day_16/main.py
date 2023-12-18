from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type",["Electric", "Water", "Fire"])


#
table = PrettyTable(["Pokemon Name","Type"])
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

print(table)

