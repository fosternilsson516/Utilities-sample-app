document.addEventListener("DOMContentLoaded", function () {
    // Fetch the CSRF token from the hidden input field
    const form = document.getElementById("myForm");
    //const zipCodeDiv = document.getElementById("zipCode");
    //const selectedAppliancesDiv = document.getElementById("selectedAppliances");
    

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission behavior

        const zipCodeInput = document.getElementById("zipCodeInput");
        const zipCode = zipCodeInput.value;

        console.log(zipCodeInput);
        console.log(zipCode);

        const appliances = [];
        const applianceCheckboxes = document.querySelectorAll('input[name="appliances[]"]:checked');
        applianceCheckboxes.forEach(function (checkbox) {
            appliances.push(checkbox.value);
        });
        console.log("Selected Appliances:", appliances);
        const csrfTokenInput = document.querySelector('input[name="csrf_token"]').value;

        const formData = new FormData();
        console.log(formData)
        formData.append("csrf_token", csrfTokenInput);
        formData.append("zipCode", zipCode);
        appliances.forEach((appliance) => {
            formData.append("appliances[]", appliance);
        });
        console.log("Selected Appliances:", appliances);
        // Send the data to the server using an HTTP POST request (e.g., with Axios)
        sendZipCode(formData);
    });

    function sendZipCode(formData) {
        axios.post("/submit", formData)
        .then(function (response) {
            const data = response.data;

            if (data.redirect) {
                // Redirect to the /result route
                window.location.href = data.redirect;
            } else {
                // Handle other data or errors
                console.error("Unexpected response:", data);
            }
        })
        .catch(function (error) {
            // Handle errors
            console.error("An error occurred:", error);
        });
    
            
            // Handle the response data
           // if (data.zipCode) {
           //     zipCodeDiv.innerHTML = "zip code: " + data.zipCode;
           // } else {
            //    zipCodeDiv.innerHTML = "No result available.";
          //  }

            // Check if selected appliances data is available
           // if (data.appliances && data.appliances.length > 0) {
           //     selectedAppliancesDiv.innerHTML = "Selected Appliances: " + data.appliances.join(", ");
           // } else {
          //      selectedAppliancesDiv.innerHTML = "No appliances selected.";
          //  }

       // })
         //   .catch(function (error) {
                // Handle errors
          //      zipCodeDiv.innerHTML = "An error occurred while processing the request.";
         //       selectedAppliancesDiv.innerHTML = "No appliances selected.";
         //   });
    }
});