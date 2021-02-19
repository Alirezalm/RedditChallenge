# Restful API project by using Django Rest Framework (DRF)

## This backend project is designed dnd distributed by [JungleDevs](https://www.jungledevs.com).

## Description
**Project goal**: The idea of the project is to implement a very simplified version of [Reddit](https://www.reddit.com) REST API. 
Meaning there will have *Users*, *Topics*, *Posts* and *Comments*. 

## Acceptance criteria
- Separate your project into 4 Django apps, one for each entity:
  - User
  - Topic
  - Post
  - Comment
- Have all the required fields for each entity as described on this README
- Use the URL structure described on this README with Nested URL Routers

## Prerequisites

- [Python 3.7](https://www.python.org)
- [Docker](https://www.docker.com)
- [Docker Compose](https://docs.docker.com/compose/)
- [Virtualenv](https://github.com/pypa/virtualenv/)
- [Git](https://git-scm.com/)


### Entities

As mentioned in the description, this challenge will have four entities (each one should be a separate app). 
Here are brief descriptions of what they are and what are the expected properties of each (keep in mind that you can 
improve them as you wish!):

* *User*: can be used plain from what is offered by Django;
* *Topic*: the equivalent of a sub-reddit. The suggest fields are:
    * Name
    * Title
    * Author
    * Description
    * URLName - the name we want to use to reach it through the browser (check [SlugField](https://docs.djangoproject.com/en/2.1/ref/models/fields/#slugfield))
    * Created_at
    * Updated_at
* *Post*: the equivalent of a *Reddit thread*, a *post* belongs to a *specific topic* and is *created by an user*. The 
suggested fields are:
    * Title
    * Content
    * Created_at
    * Updated_at
    * Topic
* *Comment*: the equivalent of a comment, a comment belongs to a *specific post* (which belongs to a *specific topic*) 
and is *created by an user*. The suggested fields are:
    * Title
    * Content
    * Created_at
    * Updated_at
    * Post
    
### URLs    

We want to have a behavior similar to *Reddit (not necessarily equal)*, so ideally we'd like a structure like this:

* */topics/* - lists all available topics
* */topics/{urlname}/* - details (as well as some posts) from a specific topic (identified by *urlname*)
* */topics/{urlname}/posts/* - lists all posts from a specific topic
* */topics/{urlname}/posts/{post_id}/* - lists details and some comments from a post
* */topics/{urlname}/posts/{post_id}/comments/* - lists all comments from a post
* */topics/{urlname}/posts/{post_id}/comments/{comment_id}/* - lists details from a comment

