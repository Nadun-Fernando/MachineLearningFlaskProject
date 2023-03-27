document.addEventListener('DOMContentLoaded', function() {
    // Find the form element
    const form = document.querySelector('form');

    // Find the loader element
    const loader = document.getElementById('loader');

    // Find the content element
    const content = document.getElementById('content');

    // Add a submit event listener to the form
    form.addEventListener('submit', function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Show the loading animation and blur the content
        loader.style.display = 'block';
        content.classList.add('blur');


        // Create a new FormData object with the form values
        const formData = new FormData(form);

        // Send the form data to the server using the Fetch API
        fetch("{{ url_for('predict') }}", {
            method: 'POST',
            body: formData
        })
            .then(response => response.text())
            .then(data => {
                // Replace the current page with the results page
                document.open();
                document.write(data);
                document.close();
            })
            .catch(error => {
                // Hide the loading animation, remove the blur effect, and show an error message
                loader.style.display = 'none';
                content.classList.remove('blur');
                alert('Error: ' + error);
            });
    });
});