## Setup and Installation

Clone the repository:
- git clone https://github.com/yourusername/fastapi-item-manager.git
- cd fastapi-item-manager

Create a virtual environment and activate it:
- python -m venv venv
- source venv/bin/activate  # On Windows, use venv\Scripts\activate

Install the required packages:
- pip install -r requirements.txt

Run the application:
- uvicorn app.main:app --reload


Open your browser and navigate to `http://localhost:8000`

## API Endpoints

- GET `/items/`: List all items
- POST `/items/`: Create a new item
- GET `/items/{item_id}`: Get details of a specific item

## Frontend Pages

- `/`: Home page with a list of all items
- `/item/{item_id}`: Detail page for a specific item

## Custom ast-grep Rules

Custom ast-grep rules are located in the `rules/` directory. These rules help maintain code quality and consistency.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.




