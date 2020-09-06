# To Do App

## A simple to do app with multiple to do lists, each of which has multiple to do items
The original version of the app is part of Udacity's Full Stack nanodegree.

### Functionality Added Independent of Udacity Tutorials
- Feature 1 [x]: add a feature that allows the user to create a new to do list
- Feature 2 [x]: add a checkbox to each to do list that marks all of that lists' to do items as completed
- Feature 3 [x]: add a delete button (x) to each list; deleting a list should delete all associated to do items
- Udacity Bugs
  - Bug 1 [x]: to do item creation was broken after adding the list association
  - Bug 2 [ ]: creating an item or a list results in the element showing up but its checkbox and delete buttons not being active; we might solve this by refreshing the app when adding a list or item
  - Bug 3 [ ]: the app shouldn't allow blank items or lists
  - Bug 4 [x]: checkboxes don't show up until after refresh when creating a new list
  - Bug 5 [ ]: the behavior of complete all items in a list needs further testing (i.e. what happens when we uncheck the list? Should all items become unchecked or should it revert to some previous state?)
  - Bug 6 [x]: when you add a list, it doesn't add it as a link
- Update 1 [ ]: style the page (positioning, background and borders, width)
- Update 2 [x]: add a readme file that tracks the difference between the Udacity basic app and this version along with any bugs

### Functionality from Udacity
- Basic ability to CRUD to do items
- Database relationship between a to do item and a to do list
- Simple index view with embedded styles and scripts
- Simple controller with ability to add, delete and complete to do items
