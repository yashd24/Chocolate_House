# Chocolate House

A web-based **Inventory Management System** for Chocolate House built using **Django**. This system allows users to manage inventory items, including adding, deleting, and updating product details like ingredient name, quantity, and unit. It also includes a **Customer Suggestions** feature, where customers can submit their flavor suggestions and allergy concerns.

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
- The application will be accessible at http://<your_server_ip>:8002 or (http://localhost:8002).

## Documentation

## [Postman Link](https://orange-comet-842903.postman.co/workspace/SocialApp~4793c6e6-ca9d-4829-b619-c437488e9a69/collection/27788962-deaba1ef-61c1-48dc-9fb6-9c1eeb2ba585?action=share&creator=27788962)
