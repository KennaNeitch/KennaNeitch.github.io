# make a dictionary linking each text with its year
# assign names for each half of the key:value pair in the loop
# set the loop function
publication_info = {"Jane Eyre": "1847", "Cane": "1923", "Wide Sargasso Sea": "1966", "Citizen: An American Lyric": "2014"}
for title, date in publication_info.items():
    print(title + " was published in " + date + ".")
