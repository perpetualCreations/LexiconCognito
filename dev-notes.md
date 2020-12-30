## Development Notes
This Markdown document include various notes made during development. Users need not pay attention to this, feel free to read it regardless.

#### Search
One of the rules of engineering is that the first solution created for a problem is likely the worst or with severe caveats.   
I'm disregarding that rule, it's now a mere suggestion.

We have two inputs, search-by-kind, and search-term.  
Search-by-kind is a dropdown that selects the type of search-term, determining weather to search by title, author, publisher, source/distributor, date published, date added, and by tags.  
Search-term is a text entry box, being the actual term searched.  
Search-by-kind is auto-filled with by title, text entry however is empty. Both fields need to be filled for the search to work.

The Flask server will listen for client POST, that provides both of these fields.  
Obviously, we then have the server fetch a SQLite query for the search term, with the given type, and compile them into a list. Here comes the hard part.  

We need to format the list which will, in likely circumstances, probably exceed a page. One solution would be infinite scrolling, however I follow the path of the least resistance.  
No we have standards, we divide the list into groups of 10s, so we'll have pages with 10 documents each.  

With our processed query neatly divided into 10s, we render searchresults.html as a template.
Flask has dynamic URLs. We'll apply this feature to searchresults.html, as /search/< type here >/< term here >/< page number here >.  

When filling in the pre-drawn 1x10 grid of document slots, we use the given dynamic URL and use it as an index to retrieve the contents from the previously generated list.  

Voilà, the result of an engineer's depressing afterthought.

#### Content
Remember dynamic URLs? We're using them again, but now as /content/< numeric id>.  

That's literally it. I'm going to bed.

#### Security
The Flask application has no security features. 

It lacks:
 - User accounts for authentication and permissions management.
 - User input sanitation for SQLite interactions.
 - Access logging.

These should be fixed immediately after release.
