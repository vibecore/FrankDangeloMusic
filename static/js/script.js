

function searchDirections(location) {
    // Construct the Google search URL
    var searchUrl = 'https://www.google.com/search?q=' + encodeURIComponent('Directions to ' + location);

    // Open a new window or tab with the Google search
    window.open(searchUrl, '_blank');
}