document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('nyaya-form');
    const queryInput = document.getElementById('user-query');
    const contentContainer = document.getElementById('doj-content');

    // Function to fetch general DOJ data
    function fetchDOJData() {
        fetch('/aboutDOJ')  // Fetch data about DOJ from your Flask endpoint
            .then(response => response.json())
            .then(data => {
                if (data.content && data.content.length > 0) {
                    displayDOJContent(data.content);
                } else {
                    displayError('No content available from the Department of Justice.');
                }
            })
            .catch(error => {
                console.error('Error fetching DOJ data:', error);
                displayError('Failed to load Department of Justice content.');
            });
    }

    // Function to fetch functions of DOJ data
    function fetchFunctionsDOJData() {
        fetch('/functions-of-doj')  // Fetch data about DOJ functions from your Flask endpoint
            .then(response => response.json())
            .then(data => {
                if (data.content && data.content.length > 0) {
                    displayDOJContent(data.content);
                } else {
                    displayError('No functions data available from the Department of Justice.');
                }
            })
            .catch(error => {
                console.error('Error fetching functions of DOJ data:', error);
                displayError('Failed to load functions data from the Department of Justice.');
            });
    }

    // Function to fetch about DOJ data
    function fetchAboutData() {
        fetch('/about')  // Fetch data about DOJ from the new endpoint
            .then(response => response.json())
            .then(data => {
                if (data.content && data.content.length > 0) {
                    displayDOJContent(data.content);
                } else {
                    displayError('No content available from the new DOJ about page.');
                }
            })
            .catch(error => {
                console.error('Error fetching about data:', error);
                displayError('Failed to load about content from the Department of Justice.');
            });
    }

    // Function to fetch NJDG data
    function fetchNJDGData() {
        fetch('/njdg')  // Fetch data about NJDG from the new endpoint
            .then(response => response.json())
            .then(data => {
                if (data.content && data.content.length > 0) {
                    displayDOJContent(data.content);
                } else {
                    displayError('No content available from the National Judicial Data Grid.');
                }
            })
            .catch(error => {
                console.error('Error fetching NJDG data:', error);
                displayError('Failed to load National Judicial Data Grid content.');
            });
    }

    // Function to fetch Tele-Law data
    function fetchTeleLawData() {
        fetch('/tele-law')  // Fetch data about Tele-Law from the new endpoint
            .then(response => response.json())
            .then(data => {
                if (data.content && data.content.length > 0) {
                    displayDOJContent(data.content);
                } else {
                    displayError('No content available about Tele-Law.');
                }
            })
            .catch(error => {
                console.error('Error fetching Tele-Law data:', error);
                displayError('Failed to load Tele-Law content.');
            });
    }

    // Function to display DOJ content on the page
    function displayDOJContent(content) {
        contentContainer.innerHTML = ''; // Clear any previous content
        content.forEach(paragraph => {
            const p = document.createElement('p');
            p.textContent = paragraph;
            contentContainer.appendChild(p);
        });
    }

    // Function to display an error message
    function displayError(message) {
        contentContainer.innerHTML = `<p class="error">${message}</p>`;
    }

    // Listen for form submission
    form.addEventListener('submit', function (event) {
        event.preventDefault();  // Prevent the form from submitting the traditional way
        const userQuery = queryInput.value.trim().toLowerCase();

        console.log('User Query:', userQuery);  // Debug output

        if (userQuery.includes('department of justice') && userQuery.includes('functions')) {
            fetchFunctionsDOJData();  // Fetch DOJ functions if the query asks about functions
        } else if (userQuery.includes('department of justice')) {
            fetchDOJData();  // Fetch general DOJ data
        } else if (userQuery.includes('tele-law') || userQuery.includes('about tele-law')) {
            fetchTeleLawData();  // Fetch about Tele-Law data
        } else if (userQuery.includes('national judicial data grid') || userQuery.includes('njdg')) {
            fetchNJDGData();  // Fetch NJDG data
        } else {
            displayError('Please ask about the Department of Justice or related services.');
        }
    });
});
