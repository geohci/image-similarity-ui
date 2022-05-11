# Image Similarity UI
Toolforge interface to allow users to explore reverse image search for Wikimedia Commons 

UI based on the following template: https://github.com/wikimedia/research-api-interface-template

## Test it out
<https://imagesimilarity.toolforge.org/>

## Development

### Relevant Files
The important files are as follows:
* `app.py`: basic code for serving the UI and taking pre-formed URL parameters
* `templates/index.html`: this is where the UI HTML lives and Javascript code for taking input image names, hitting the API, and formatting the results
* `static/style.css`: you likely will not need to edit this file but can find details about relevant classes [here](https://github.com/wikimedia/research-api-interface-template).

### Deploying
I find it easiest to test the interface locally (you may need to update the path to the CSS files but otherwise everything should work)
The steps for updating the interface then:
* Push your local changes to Github
* ssh in to the tool -- e.g., `ssh isaacj@login.toolforge.org` and then `become imagesimilarity`
* Navigate to the UI code: `cd www/python/src/`
* Pull the changes locally: `git pull`
* Restart the webservice: `webservice restart`
* Test to make sure it's working (navigate to <https://imagesimilarity.toolforge.org/> and interact accordingly)

## License
The source code for this interface is released under the [MIT license](https://github.com/geohci/wikidata-topic-model-api/blob/master/LICENSE).

Screenshots of the results in the API may be used without attribution, but a link back to the application would be appreciated.
Note that the images displayed by the tool likely have their own attribution requirements that you should seek to follow.