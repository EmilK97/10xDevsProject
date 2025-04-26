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
}); 