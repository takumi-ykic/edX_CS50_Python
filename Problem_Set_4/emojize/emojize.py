import emoji

# userin = input("Input: ")

if "_" in userin:
    print(emoji.emojize(userin))
else:
    print(emoji.emojize(userin, language="alias"))

# ":earth_asia:" is no longer existed in this library
# Now :globe_showing_Asia-Australia: is used for that emoji



