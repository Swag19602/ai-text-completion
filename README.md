## Running the Flask Application
- Clone the Repository:
    git clone repository-url

- Install Dependencies:
    cd repository-directory
    pip install -r requirements.txt

- Set Environment Variables:
    Create a .env file in the root directory.
    Add the following environment variables:
    makefile
    Copy code
    DB_URI=sqlite:///openai_logs.db
    OPENAI_API_KEY=your-openai-api-key

- Run the Application:
    python app.py

## Access the API:
    The Flask application will run on http://127.0.0.1:5000/ by default.
       - Interacting with the Endpoint
            1. POST Endpoint: /openai-completion
                - Description:
                    This endpoint generates a completion using the OpenAI API based on the provided prompt.
                - Request Format:
                    - Method: POST
                        URL: http://127.0.0.1:5000/openai-completion

                    - Headers:
                        Content-Type: application/json

                    - Body:
                        {
                            "prompt": "Your prompt text here",
                            "user_id": "swag1"
                        }
                - Response Format:
                    - Status Code: 200 OK

                    - Body:
                        {
                            "completion": "Generated completion text here"
                        }
## Postman API documentation link
- https://documenter.postman.com/preview/20527777-ad646c69-d99f-4476-aee5-be3e86fdf455?environment=&versionTag=latest&apiName=CURRENT&version=latest&documentationLayout=classic-double-column&documentationTheme=light&logo=https%3A%2F%2Fres.cloudinary.com%2Fpostman%2Fimage%2Fupload%2Ft_team_logo%2Fv1%2Fteam%2Fanonymous_team&logoDark=https%3A%2F%2Fres.cloudinary.com%2Fpostman%2Fimage%2Fupload%2Ft_team_logo%2Fv1%2Fteam%2Fanonymous_team&right-sidebar=303030&top-bar=FFFFFF&highlight=FF6C37&right-sidebar-dark=303030&top-bar-dark=212121&highlight-dark=FF6C37