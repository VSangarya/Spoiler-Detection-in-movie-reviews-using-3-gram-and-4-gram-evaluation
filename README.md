# Spoiler-Detection-in-movie-reviews-using-3-gram-and-4-gram-evaluation
This is a simple movie spoiler detection in reviews. It uses the main synposis/plot from wikipedia of each movie and compares it with the review we give as input.
It processes botht the documents and checks the 3gram and 4gram similarity. Based on the calculated output, the movie review is classified as having spoilers or not.

template:
-templates
---new2.html   (templates/new2.html)
-a4
---a1.txt(Processed wiki plot of the selected movie)
---a2.txt(Out input movie review processed into a bag of words)
---a3.txt(Wiki summary of movie 1)
---a4.txt(Wiki summary of movie 2)
---a5.txt(Wiki summary of movie 3)

Note : It's primarily designed for large movie reviews with multiple spoilers.
I've added some sample reviews of Avengers:Endgame (some of which contain spoilers and some don't) for testing purposes

P.S : I'm still a novice in terms of how to handle text data and processing. Hence, for the text cleaning and using IF-TDF I've used an open sourced code.(The processing of both the text files in the code)
