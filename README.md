# Chocolate House

A brief description of what this project does and who it's for

## Features

- **Add New Inventory Items**: Users can add new items to the inventory by providing ingredient name, quantity, and unit.
- **Delete Inventory Items**: Users can delete items from the inventory.
- **Update Inventory**: Allows updating item details such as quantity and unit.
- **Customer Suggestions**: Customers can submit their flavor suggestions along with allergy concerns. This helps gather valuable feedback and improve the product offerings.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **API**: Django Rest Framework
- **Docker**: For containerization of the application.

## Setup

### Prerequisites

Before running the project, ensure you have the following installed:

- Docker and Docker Compose

### Installation

#### Step 1. Clone the repository:

```bash
git clone https://github.com/yashd24/Chocolate_House.git
cd Chocolate_House
```

#### Step 2. Build & Run Docker Containers

```bash
docker-compose up --build
```

This will:

- Build the Docker images.
- Start services for the web app.
- The application will be accessible at http://<your_server_ip>:8002.
