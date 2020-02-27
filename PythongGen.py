site_name = input( " Type the name of the site: ")
site_1abr = input( " Type a abbreviation of the site: ")
site_2abr = input( " Change the capitalization: ")


verb = input(f" How do you use {site_name}? ")
toot_verb = input(verb+", shorten your response to a word: ")
ab_verb = input(toot_verb+", abbreviate the word: ")
fnl_verb = input(ab_verb+", Change the capitalization: ")


content = input(" One word to describe this site: ")
ab_content = input( " Change the capitalization and abbreviate the word: ")


print(f" You have finished!, here is  the finished password!! ")
print(f" {site_2abr}{ab_content}{fnl_verb} ")                                