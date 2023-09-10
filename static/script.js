document.addEventListener("DOMContentLoaded", function () {
    // Fetch the CSRF token from the hidden input field
    const zipCodeInput = document.getElementById("zipCodeInput");
    const submitButton = document.getElementById("submitButton");
    const resultDiv = document.getElementById("result");

    submitButton.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent the default form submission behavior

        var zipCode = zipCodeInput.value;
        var csrfTokenInput = document.querySelector('input[name="csrf_token"]').value;
        if (zipCode.length === 5 && /^\d+$/.test(zipCode)) {
            // Valid zip code format

            
            const formData = new FormData();
            formData.append("csrf_token", csrfTokenInput); // Include the CSRF token
            formData.append("zipCode", zipCode);

            sendZipCode(formData);
        } else {
            resultDiv.innerHTML = "Please enter a valid 5-digit zip code.";
        }
    });

    function sendZipCode(formData) {
        axios.post("/", formData)
            .then(function (response) {
                resultDiv.innerHTML = "Result: " + response.data.result;
            })
            .catch(function (error) {
                resultDiv.innerHTML = "Error processing the zip code.";
            });
    }
});
