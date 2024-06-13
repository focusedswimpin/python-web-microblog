
# Microblog Application with Flask and MongoDB

This is a simple microblogging web application built using Flask and MongoDB. Users can submit entries with content, and each entry is stored in MongoDB with a timestamp. Entries are displayed with their content and formatted date.

## Setup

### Prerequisites

- Python 3.8 or higher installed on your system.
- MongoDB Atlas account or a local MongoDB server running.

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Microblog
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   MONGODB_URI=<your-mongodb-uri>
   ```

   Replace `<your-mongodb-uri>` with your MongoDB connection URI. If you're using MongoDB Atlas, this URI can be found in your Atlas dashboard.

### Running the Application

1. Make sure your MongoDB server is running or your MongoDB Atlas cluster is accessible.

2. Start the Flask application:
   ```bash
   python app.py
   ```

3. Open your web browser and go to `http://localhost:5000` to view the application.

## Usage

- **Homepage:** The homepage displays all entries submitted by users. Each entry shows its content and the formatted date of submission.
- **Submitting Entries:** Use the form on the homepage to submit new entries. Once submitted, the page will refresh, showing all entries including the new one.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### Notes:

- Update `<repository-url>` with the actual URL of your repository.
- Customize the instructions based on your specific application setup.
- Provide more details about deployment if needed, such as deploying to a cloud platform or containerizing the application.
