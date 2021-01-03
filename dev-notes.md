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

#### File Support
This project was originally intended as an e-library application, however the scope exponentially began increasing. 
Technical debt however becomes less daunting as it is broken down.

There are multiple standards for video, audio, PDFs and other document formats, code, and webpages.

For video, the supported files are MP4 and MPEG-X. 
There are many Javascript-based video players available, integrating a player will be trivial.
The auxiliary metadata for the AUX field under the items table will contain length of video and resolution.

For audio, the supported files are MP3, FLAC, and WAV. There is an exhaustive list of additional formats that will find implementation later.
Alike to video, there are plenty of open media players that can be integrated and customized.
The auxiliary metadata for the AUX field under the items table will contain length of audio. 

For documents, the supported files are PDF, .DOCX, Markdown, LaTEX, rich-text and plain-text. 
None of these are fun to implement! They all have their own gimmicks, and I'll need find or write viewers for all of them.

For code, script files will be treated as regular plain-text files, with their own monospaced, dedicated font.
Executables, installers, and software packages will not have viewers. Maybe add a hex viewer.
The auxiliary metadata for the AUX field under the items table will contain language of the file.

For webpages, well. They can be written as stand-alone HTML files, or be packaged as a directory with stylesheets and resources.
The content can be viewed through an iframe.

Hopefully after integrating these content types, support will be added for Git repositories and ZIP files.

