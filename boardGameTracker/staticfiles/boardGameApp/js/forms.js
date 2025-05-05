document.addEventListener('DOMContentLoaded', function() {
    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        // Add validation classes on input
        const inputs = form.querySelectorAll('input[required]');
        inputs.forEach(input => {
            input.addEventListener('input', function() {
                const formGroup = this.closest('.form-group');
                if (formGroup) {
                    if (this.validity.valid) {
                        formGroup.classList.remove('error');
                        const errorElement = formGroup.querySelector('.form-error');
                        if (errorElement) {
                            errorElement.remove();
                        }
                    } else {
                        showError(this);
                    }
                }
            });
        });

        // Handle form submission
        form.addEventListener('submit', function(event) {
            let hasErrors = false;
            
            // Clear previous errors
            form.querySelectorAll('.form-error').forEach(error => error.remove());
            form.querySelectorAll('.form-group').forEach(group => group.classList.remove('error'));
            
            // Validate required fields
            inputs.forEach(input => {
                if (!input.validity.valid) {
                    event.preventDefault();
                    hasErrors = true;
                    showError(input);
                }
            });

            // Password matching validation for registration form
            if (form.id === 'register-form') {
                const password1 = form.querySelector('#password1');
                const password2 = form.querySelector('#password2');
                if (password1.value !== password2.value) {
                    event.preventDefault();
                    hasErrors = true;
                    showError(password2, 'Hasła nie są identyczne.');
                }
            }

            // Add loading state if no errors
            if (!hasErrors) {
                form.classList.add('loading');
                const submitButton = form.querySelector('button[type="submit"]');
                if (submitButton) {
                    submitButton.classList.add('loading');
                    submitButton.disabled = true;
                }
            }
        });
    });

    // Error display helper function
    function showError(input, customMessage) {
        const formGroup = input.closest('.form-group');
        if (!formGroup) return;

        formGroup.classList.add('error');
        
        // Remove existing error message if any
        const existingError = formGroup.querySelector('.form-error');
        if (existingError) {
            existingError.remove();
        }

        // Create and add new error message
        const errorElement = document.createElement('div');
        errorElement.className = 'form-error';
        
        if (customMessage) {
            errorElement.textContent = customMessage;
        } else if (input.validity.valueMissing) {
            errorElement.textContent = 'To pole jest wymagane.';
        } else if (input.validity.patternMismatch) {
            errorElement.textContent = input.title || 'Nieprawidłowy format.';
        } else if (input.validity.tooShort) {
            errorElement.textContent = `Minimalna długość to ${input.minLength} znaków.`;
        } else {
            errorElement.textContent = input.validationMessage;
        }

        formGroup.appendChild(errorElement);
    }

    // Auto-hide messages after 5 seconds
    const messages = document.querySelectorAll('.message');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 300);
        }, 5000);
    });
}); 