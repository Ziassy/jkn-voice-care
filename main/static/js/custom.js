const playButtons = document.querySelectorAll('.play');
const translationContent = document.getElementById('translationContent');
const menuDetailLink = document.getElementById('menuDetailLink');
const toggleSwitch = document.getElementById('toggleSwitch');
const select = document.getElementById('languageSelect');
const translationForm = document.querySelector('form[method="get"]');
let isToggleOn = toggleSwitch.checked;

toggleSwitch.addEventListener('change', function () {
  isToggleOn = toggleSwitch.checked;
  localStorage.setItem('isToggleOn', isToggleOn ? 'true' : 'false'); // Store toggle status in local storage as a string

  select.disabled = !isToggleOn;

  // Display the "Play" button when the toggle switch is true
  if (isToggleOn) {
    playButtons.forEach(button => {
      button.style.display = 'block';
    });
  } else {
    playButtons.forEach(button => {
      button.style.display = 'none';
    });
    select.selectedIndex = 0;
  }
});

// Read the toggle status from local storage when the page loads
const storedToggleStatus = localStorage.getItem('isToggleOn');
if (storedToggleStatus === 'true') {
  toggleSwitch.checked = true;
  isToggleOn = true;

  select.disabled = !isToggleOn;

  // Display the "Play" button when the toggle switch is true
  playButtons.forEach(button => {
    button.style.display = 'block';
  });
} else {
  toggleSwitch.checked = false;
  isToggleOn = false;
  select.selectedIndex = 0;
}

// Add an event listener for the language select dropdown change event
select.addEventListener('change', function () {
  // Submit the form when a language is selected
  translationForm.submit();
});

playButtons.forEach(button => {
  button.addEventListener('click', function (e) {
    const translation = button.getAttribute('data-translation');
    const menuId = button.getAttribute('data-menu-id'); // Get the menu_id from the button
    const detailURL = `/menu/${menuId}/`; // Construct the menu detail URL
    translationContent.textContent = translation;

    // Select the "Buka menu" button inside the modal by its class
    const menuDetailLink = document.querySelector('.buka-menu-button');

    if (menuDetailLink) {
      menuDetailLink.href = detailURL; // Set the href attribute to the menu detail URL
    }
  });
});