import plotly.express as px

# Do not modify the line below.
countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", 
             "Falkland Islands", "Guyana", "Paraguay", "Peru", "Suriname",
               "Uruguay", "Venezuela"]

# Do not modify the line below.
colors = ["blue", "green", "red", "yellow"]


graphOfCountries = {"Argentina": ["Bolivia", "Brazil", "Chile", "Paraguay", "Uruguay"],
                    "Bolivia": ["Argentina", "Brazil", "Chile", "Paraguay", "Peru"],
                    "Brazil": ["Argentina", "Bolivia", "Colombia", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay",
                               "Venezuela"],
                    "Chile": ["Argentina", "Bolivia", "Peru"],
                    "Colombia": ["Brazil", "Ecuador", "Peru", "Venezuela"],
                    "Ecuador": ["Colombia", "Bolivia", "Peru"],
                    "Falkland Islands": [],
                    "Guyana": ["Brazil", "Suriname", "Venezuela"],
                    "Paraguay": ["Argentina", "Bolivia", "Brazil"],
                    "Peru": ["Bolivia", "Brazil", "Chile", "Colombia", "Ecuador"],
                    "Suriname": ["Brazil", "Guyana"],
                    "Uruguay": ["Argentina", "Brazil"],
                    "Venezuela": ["Brazil", "Colombia", "Guyana"]
                    }


def sortCountries(graph, unSortedCountries):
    newCountry = {}
    retCountries = []
    for country in unSortedCountries:
        newCountry.update({country: len(graph[country])})

    newCountry = list(sorted(newCountry.items(), key=lambda kv: kv[1]))

    i = len(newCountry) - 1
    while i > -1:
        retCountries.append(newCountry[i][0])
        i -= 1

    return retCountries



def trueColoring(graph, testMap):
    for node in graph:
        edges = (graph[node])
        if node in testMap:
            colorOfNode = testMap[node]
            for edge in edges:
                if edge in testMap:
                    colorOfEdge = testMap[edge]
                    if colorOfNode == colorOfEdge:
                        return False
    return True


def colorTheCountry(graph, colorMap, unSortedCountries):
    sortedCountries = sortCountries(graph, unSortedCountries)
    color_index = 0
    country_index = 0
    solverCounter = 0
    isSolved = True

    while country_index < len(sortedCountries):
        if solverCounter == len(colors):
            print("Problem not solved.")
            isSolved = False
            break
        temp = country_index
        colorMap[sortedCountries[country_index]] = colors[color_index]
        if not trueColoring(graph, colorMap):
            country_index -= 1
        color_index = (color_index + 1) % len(colors)
        country_index += 1
        if temp == country_index:
            solverCounter += 1
        else:
            solverCounter = 0
    return colorMap, isSolved


# Do not modify this method, only call it with an appropriate argument.
# colormap should be a dictionary having countries as keys and colors as values.
def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


# Implement main to call necessary functions
if __name__ == "__main__":


    # coloring test
    colormap_test = {"Argentina": "blue", "Bolivia": "red", "Brazil": "yellow", "Chile": "yellow", "Colombia": "red",
                     "Ecuador": "yellow", "Falkland Islands": "yellow", "Guyana": "red", "Paraguay": "green",
                     "Peru": "green", "Suriname": "green", "Uruguay": "red", "Venezuela": "green"}

    print(f"colormap_test {trueColoring(graphOfCountries, colormap_test)} colored.")
    coloringMap = {}
    coloringMap, isTrue = colorTheCountry(graphOfCountries, coloringMap, countries)
    print(f"coloringMap {trueColoring(graphOfCountries, coloringMap)} colored.")

    if isTrue:
        plot_choropleth(colormap=colormap_test)

