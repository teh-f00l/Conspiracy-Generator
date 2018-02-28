import wikipedia

#scraping function
def web_scraper(page):
	##create string to store conspiracies
	theory_list=''

	#extract text from tags
	page=page.content

	##break up the text by section
	theories=page.split('===')

	#loop through theories, storing titles and paragraphs in tuples
	# I used a counter rather than enumerate since working with odds and evens
	#this allows me to avoid the headings for each section and just get the page content
	j=1
	for i in theories:
        #add the evenly indexed elements, as they are the content of the page(odd elements are titles)
		if j % 2 ==0:
			theory_list=theory_list+str(theories[j])
		j+=1
		if j > len(theories)/2:

			break

	return theory_list


#write over the blank conspiracy text file
conspiracy_file = open('conspiracies.txt','w')
book_text=(web_scraper(wikipedia.page('List_of_conspiracy_theories')))

link=wikipedia.page('List_of_conspiracy_theories').links
#use store each link in a variables, extract its text, and add it to the corpus, this will take some time
for i in link:
    #pass over links identifying multiple pages, or without the proper id
    # use exceptions to ignore links without content or identification
    try:
        conspiracy=web_scraper(wikipedia.page(i))
    except wikipedia.exceptions.PageError as e:
	    pass
    except wikipedia.exceptions.DisambiguationError as e:
        pass


    book_text=book_text+conspiracy

#convert the list of content to a string and save it
conspiracy_file.write(book_text)
conspiracy_file.close()
