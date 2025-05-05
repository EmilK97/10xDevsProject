// Main JavaScript file for BoardGameTracker
document.addEventListener('DOMContentLoaded', function() {
    console.log('BoardGameTracker application loaded');
    
    // Handle message fade-out
    const messages = document.querySelectorAll('.message');
    if (messages.length > 0) {
        setTimeout(() => {
            messages.forEach(msg => {
                msg.style.opacity = '0';
                setTimeout(() => {
                    msg.style.display = 'none';
                }, 500);
            });
        }, 3000);
    }
}); 