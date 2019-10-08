# Feedback

## Question 1
I like that you've made a generic solution that would work for any input and that you're also taking the input from the user rather than hard coding it.
In terms of parsing the response from the github api, it returns the data as json so you could just use the return value from the requests.get() call.
By doing json.loads(result.text) you are getting the text value out of a json response and converting that text back to json essentially doing two operations that cancel each other out.

I think your idea of splitting it into two functions is so that you have one function that gets all the user information and then another that will pull out the bio.
That way if you want to re-use the user info to get other bits of information you can re-use the user information from the first function call.
If that was indeed your idea thats not bad, but I would not pass that burden to consumers of this class, where anyone using this class needs to make two separate calls, passing the output
of the first as the input to the next. Instead, I would make the one call of get_user_bio() which internally makes the call to github to get the user info.

Either ways, your solution works, but I would address the stylistic points I've brought up above.

## Question 2
What you've done works, but here's how I would have approached it

* I would've used flask's ability to parse out the parameter values from the url and place them as arguemnts to my function for me rather than explicitly going via requests
* In forming the response I would've created a response object with one field of sum or probably a dictionary with one key of sum and the value of the sum and sent it back via json rather than manually constructing the json string

## Question 3
### Update statement
I would run the update statement by searching for the user by firstname and last name rather than by the id.

### Select
The select criteria is incomplete.

* The task was to select employees in new york that made > 70000. You've selected the NY employees but you're missing the > 70000 in the where clause
* I would select the branch by joining to the branch table and setting the state = "NY" in the where clause. That way you know your sql will be generic enough to run regardless of the auto-generated id of the branch.

## Question 4
I would get the length of the list within the function (since if the function takes in the list, it should know how to get its length rather than having the caller pass it from the outside)
Works otherwise.

## Score
90%. I will take of 10% for the missed select criteria and for not doing a join to get the branch.

## Overall
I think your solutions work. I think your code overall can be improved by making it more self-contained, rather than relying on stuff to be passed in from the outside -- as I've pointed out in the way you've implemented some of the functions. That would make you're code look a little more cleaner and callers of your functions would have to do less `work`.
