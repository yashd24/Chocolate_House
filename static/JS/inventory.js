document.querySelectorAll(".delete-button").forEach(button => {
    button.addEventListener("click", async function(event) {
        event.preventDefault();
        
        if (confirm("Are you sure you want to delete this item?")) {
            const id = this.getAttribute("data-id");
            try {
                const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                const response = await fetch(`http://localhost:8002/inventory/${id}/`, {
                    method: "DELETE",
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    }
                });
                if (response.ok) {
                    alert("Item Successfully Deleted!");
                    // Remove the row from the table
                    this.closest('tr').remove();
                } 
                else {
                    
                    alert("Error Deleting Item");
                }
            } 
            
            catch (error) {
                console.error("Error Deleting Item:", error);
                alert(`Error: ${error.message}`);
            }
        }
    });
});




document.getElementById("inventory-form").addEventListener("submit", async function(event){
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const ingredient_name = formData.get("ingredient_name");
    const quantity = formData.get("quantity");
    const unit = formData.get("unit");

    try{
        response = await fetch("http://localhost:8002/inventory/", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken' : formData.get('csrfmiddlewaretoken')
            },
            body: JSON.stringify({
                ingredient_name,
                quantity,
                unit
            })
        });

        if (response.ok){
            alert("Item Successfully Added!");
            form.reset();
            window.location.reload();
        }
        else{
            alert("Error Adding Item");
        }
    } catch (error) {
        console.error("Error Adding Item:", error);
    }
});