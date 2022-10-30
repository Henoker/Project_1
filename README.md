# Projct Title: Design a Wikipedia-like online encyclopedia.


## About the assignment

This assignment requires writing a Wiki type Encyclopedia web app using Markdow File as page entries. 
I have learned and implemented the following by developing the app.

* How to Crate Entry Page in django using Markdown file by Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, to render a page that displays the contents of that encyclopedia entry.
- How to make the view get the content of the encyclopedia entry by calling the appropriate util function.
- If an entry is requested that does not exist, the user is presented with an error page indicating that their requested page was not found.
- If the entry does exist, the user is presented with a page that displays the content of the entry. The title of the page includes the name of the entry.
* How to create Index Page: I Updated index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.
* How to implement Search: Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
- If the query matches the name of an encyclopedia entry, the user is redirected to that entry’s page.
- If the query does not match the name of an encyclopedia entry, the user is instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python would appear in the search results.
- Clicking on any of the entry names on the search results page would take the user to that entry’s page.
* New Page: Clicking “Create New Page” in the sidebar would take the user to a page where they can create a new encyclopedia entry.
- Users would be able to enter a title for the page and, in a textarea, should be able to enter the Markdown content for the page.
-When the page is saved, if an encyclopedia entry already exists with the provided title, the user would be presented with an error message.
* Edit Page: On each entry page, the user would be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
- The textarea is pre-populated with the existing Markdown content of the page. (i.e., the existing content from the django backend database is the initial value of the textarea).
* As per the specification of th project, on each entry’s page, any Markdown content in the entry file is converted to HTML before being displayed to the user. I have used python-markdown2 package to perform this conversion.
* Random Page: Clicking “Random Page” in the sidebar will take a user to a random encyclopedia entry.

## Built using:
- HTML
- CSS
- Markdown
- Bootstrap 4.4.1

## Getting started:
- Clone this repository or fork it
    - To clone this repository type git clone `https://github.com/Henoker/Project_1.git` on your command line
    - To fork this repository, click fork button of this repository then type git clone `https://github.com/<your username>/Project_1.git`
- open it with your favorite editor
- RUN pip install -r requirements.txt
- CD to wiki folder and run python manage.py makemigrations
- You project will be accessible in your web browse.


## License
Distributed under the [MIT](https://github.com/Henoker/bookstore/blob/master/LICENSE) License. See [`LICENSE`](https://github.com/Henoker/Project-0/blob/master/LICENSE) for more information.

## Contact
- Henock Beyene Testfatsion - [hennybany@gmail.com](mailto:hennybany@gmail.com)
- Project link: https://github.com/Henoker/Project_1

## Love my effort?

<a href='https://www.linkedin.com/in/henock-beyene-tesfatsion-921ba54b/' target='_blank'><img height='35' style='border:0px;height:34px;' src='wiki/images/download.jpg' border='0' alt='Hire me at LinkediN' />