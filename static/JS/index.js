async function fetchFlavors() {
  try {
    const response = await fetch("http://localhost:8002/flavors/"); 
    const flavors = await response.json();

    const flavorsContainer = document.getElementById("flavors-container");
    const seasonalFlavorsContainer = document.getElementById("seasonal-flavors-container");

    flavorsContainer.innerHTML = ""; 
    seasonalFlavorsContainer.innerHTML = "";

    flavors.forEach(flavor => {
      const flavorCard = document.createElement("div");
      flavorCard.className = "flavor-card";
      flavorCard.innerHTML = `
      <img src="${flavor.image}" alt="${flavor.flavor}">
        <h3>${flavor.flavor}</h3>
        <p>${flavor.description}</p>
        <p><strong>Available:</strong> ${flavor.available ? "Yes" : "No"}</p>
        
      `;
      flavorsContainer.appendChild(flavorCard);

      if (flavor.seasonal){
        const seasonalFlavor = document.createElement("div");
        seasonalFlavor.className = "seasonal-flavor-card";
        seasonalFlavor.innerHTML = `
        <img src="${flavor.image}" alt="${flavor.flavor}">
        <h3>${flavor.flavor}</h3>
        <p>${flavor.description}</p>
        <p><strong>Available:</strong> ${flavor.available ? "Yes" : "No"}</p>
        
      `;
        seasonalFlavorsContainer.appendChild(seasonalFlavor);
      }
    });
  } catch (error) {
    console.error("Error fetching flavors:", error);
  }
}
window.onload = fetchFlavors;



document.getElementById("suggestions-form").addEventListener("submit", async function(event){
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const customer_name = formData.get("customer_name");
    const customer_email = formData.get("customer_email");
    const flavor_suggestion = formData.get("flavor_suggestion");
    const allergy_concern = formData.get("allergy_concern");
    console.log({ ingredient_name, quantity, unit });

    try{
        response = await fetch("http://localhost:8002/suggestions/", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken' : formData.get('csrfmiddlewaretoken')
            },
            body: JSON.stringify({
                customer_name,
                customer_email,
                flavor_suggestion,
                allergy_concern
            })
        });

        if (response.ok){
            alert("Suggestion Successfully Submitted!");
            form.reset();
        }
        else{
            alert("Error submitting suggestion");
        }
    } catch (error) {
        console.error("Error submitting suggestion:", error);
    }
});



