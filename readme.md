#Collection of Machine Learning related functions which will later be integrated with the main application

* grade.py -> auto grading using gpt4-turbo
* text_extr.py -> text extraction
* plag.py -> sends request to copyleaks api
* plagiarism/ -> gets response from copyleaks api (this is a django app because an endpoint is required for copyleaks api)

You will need to change ngrok URL at plag.py and plagiarism/plagiarism/settings.py

run `pip install -r requirements.txt` to install all packages