// Modal control functions
function showAddGameModal() {
    const modal = document.getElementById('add-game-modal');
    if (modal) {
        modal.style.display = 'flex';
        // Add a small delay before adding the show class to trigger the animation
        requestAnimationFrame(() => {
            modal.classList.add('show');
        });
        
        // Reset form and feedback when showing modal
        const form = modal.querySelector('form');
        const feedback = modal.querySelector('.feedback-message');
        if (form) {
            form.reset();
            const submitButton = form.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.disabled = false;
                submitButton.textContent = 'Dodaj';
            }
        }
        if (feedback) feedback.remove();
    }
}

function hideAddGameModal() {
    const modal = document.getElementById('add-game-modal');
    if (modal) {
        modal.classList.remove('show');
        // Wait for the animation to complete before hiding the modal
        setTimeout(() => {
            modal.style.display = 'none';
            // Reset form state when hiding modal
            const form = modal.querySelector('form');
            if (form) {
                form.reset();
                const submitButton = form.querySelector('button[type="submit"]');
                if (submitButton) {
                    submitButton.disabled = false;
                    submitButton.textContent = 'Dodaj';
                }
            }
        }, 300); // Match the transition duration from CSS
    }
}

// Form validation and submission
function validateGameForm(form) {
    const gameName = form.querySelector('#game-name').value.trim();
    const lastPlayed = form.querySelector('#last-played').value;
    const gameType = form.querySelector('input[name="game_type"]:checked');
    
    if (gameName.length < 2) {
        return { valid: false, message: 'Nazwa gry musi mieć co najmniej 2 znaki.' };
    }
    
    if (!lastPlayed) {
        return { valid: false, message: 'Data ostatniej rozgrywki jest wymagana.' };
    }
    
    if (!gameType) {
        return { valid: false, message: 'Wybierz typ gry.' };
    }
    
    return { valid: true };
}

function showFeedback(form, message, isError = false) {
    // Remove any existing feedback
    const existingFeedback = form.querySelector('.feedback-message');
    if (existingFeedback) {
        existingFeedback.remove();
    }
    
    // Create new feedback element
    const feedback = document.createElement('div');
    feedback.className = `feedback-message ${isError ? 'error' : 'success'}`;
    feedback.textContent = message;
    
    // Insert before the buttons
    const buttons = form.querySelector('.modal-buttons');
    form.insertBefore(feedback, buttons);
}

function handleFormSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const submitButton = form.querySelector('button[type="submit"]');
    
    // Validate form
    const validation = validateGameForm(form);
    if (!validation.valid) {
        showFeedback(form, validation.message, true);
        submitButton.disabled = false;
        submitButton.textContent = 'Dodaj';
        return;
    }
    
    // Show loading state and disable button
    submitButton.disabled = true;
    submitButton.textContent = 'Dodawanie...';
    
    // Get the CSRF token
    const csrfToken = form.querySelector('[name="csrfmiddlewaretoken"]').value;
    
    // Submit form
    fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: {
            'X-CSRFToken': csrfToken,
            'Accept': 'application/json'
        },
        credentials: 'same-origin'
    })
    .then(response => {
        if (!response.ok) {
            if (response.headers.get('content-type')?.includes('application/json')) {
                return response.json().then(data => {
                    throw new Error(data.message || 'Wystąpił błąd podczas dodawania gry.');
                });
            } else {
                throw new Error('Wystąpił błąd podczas dodawania gry.');
            }
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            showFeedback(form, data.message);
            // Keep button disabled and wait for modal to close
            setTimeout(() => {
                hideAddGameModal();
                window.location.reload();
            }, 1500);
        } else {
            throw new Error(data.message || 'Wystąpił błąd podczas dodawania gry.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showFeedback(form, error.message, true);
        // Re-enable button on error
        submitButton.disabled = false;
        submitButton.textContent = 'Dodaj';
    });
}

// Close modal when clicking outside of it
window.onclick = function(event) {
    const modal = document.getElementById('add-game-modal');
    if (event.target === modal) {
        hideAddGameModal();
    }
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('Library script loaded');

    // Get filter checkboxes
    const showNormalCheckbox = document.getElementById('show-normal');
    const showWarningCheckbox = document.getElementById('show-warning');
    const showAlarmCheckbox = document.getElementById('show-alarm');

    // Log if checkboxes were found
    console.log('Checkboxes found:', {
        normal: showNormalCheckbox !== null,
        warning: showWarningCheckbox !== null,
        alarm: showAlarmCheckbox !== null
    });

    // Function to update game visibility based on filters
    function updateGameVisibility() {
        console.log('Updating visibility');
        const gameTiles = document.querySelectorAll('.game-tile');
        console.log('Found game tiles:', gameTiles.length);
        
        gameTiles.forEach(tile => {
            const hasWarning = tile.classList.contains('warning');
            const hasAlarm = tile.classList.contains('alarm');
            const isNormal = !hasWarning && !hasAlarm;

            let shouldShow = false;

            if (isNormal && showNormalCheckbox.checked) {
                shouldShow = true;
            } else if (hasWarning && showWarningCheckbox.checked) {
                shouldShow = true;
            } else if (hasAlarm && showAlarmCheckbox.checked) {
                shouldShow = true;
            }

            console.log('Tile state:', {
                hasWarning,
                hasAlarm,
                isNormal,
                shouldShow,
                normalChecked: showNormalCheckbox.checked,
                warningChecked: showWarningCheckbox.checked,
                alarmChecked: showAlarmCheckbox.checked
            });

            tile.style.display = shouldShow ? 'flex' : 'none';
        });
    }

    // Add event listeners to checkboxes
    if (showNormalCheckbox) {
        showNormalCheckbox.addEventListener('change', () => {
            console.log('Normal checkbox changed:', showNormalCheckbox.checked);
            updateGameVisibility();
        });
    }

    if (showWarningCheckbox) {
        showWarningCheckbox.addEventListener('change', () => {
            console.log('Warning checkbox changed:', showWarningCheckbox.checked);
            updateGameVisibility();
        });
    }

    if (showAlarmCheckbox) {
        showAlarmCheckbox.addEventListener('change', () => {
            console.log('Alarm checkbox changed:', showAlarmCheckbox.checked);
            updateGameVisibility();
        });
    }

    // Initial visibility update
    console.log('Running initial visibility update');
    updateGameVisibility();

    // Add form submit handler
    const addGameForm = document.querySelector('#add-game-modal form');
    if (addGameForm) {
        addGameForm.addEventListener('submit', handleFormSubmit);
    }

    // Add escape key handler for modal
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            hideAddGameModal();
        }
    });
}); 