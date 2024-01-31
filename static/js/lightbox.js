// static/js/lightbox.js
document.addEventListener('DOMContentLoaded', function () {
    const thumbnailLinks = document.querySelectorAll('.thumbnail-link');
    
    thumbnailLinks.forEach(function (link) {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const photoFilename = this.href.split('/').pop(); // Extract the filename from the URL
            const photoUrl = largeImagePath + photoFilename; // Combine with the new path
            
            const overlay = document.createElement('div');
            overlay.className = 'lightbox-overlay';
            overlay.innerHTML = `<div class="lightbox-content"><img src="${photoUrl}" class="img-fluid"><span class="lightbox-close-btn" onclick="closeLightbox()">X</span></div>`;
            
            document.body.appendChild(overlay);
        });
    });
});

function closeLightbox() {
    const overlay = document.querySelector('.lightbox-overlay');
    if (overlay) {
        overlay.remove();
    }
}
