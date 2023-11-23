I have developed a small tool that can be used to gather or scrape links from the web. Though basic, it proves to be quite useful in finding hidden links within complex webs. It can be particularly helpful in the initial phases of the pentest, allowing the user to analyze all the links present on a website and understand their functions. Additionally, the tool can save the links in a TXT file, which is especially useful for bug hunters who can scrape all URLs  and extract all the different JS files of each hyperlink. The extracted JS files can then be searched for juice words or endpoints like API, keys, usernames, etc. I have created another tool specifically for this purpose.

The use is simple. Write **python3 Linktracker.py** and then put the URL of the website from which you want to extract the hyperlinks and file name that you want save the results.

<img width="991" alt="image" src="https://github.com/svaltheim/crwl/assets/30341113/a320543c-27d4-4787-a4fd-b00b0cf36efb">



