const loadToggle = () => {
  const select = document.getElementById('languageSelect');

  const storedToggleStatus = localStorage.getItem('isToggleOn');
  if (storedToggleStatus === 'true') {
    select.disabled = false;
    showplay();
  } else {
    hideplay();
  }
}

const showplay = () => {
  const playButtons = document.querySelectorAll('.play');
  playButtons.forEach(button => {
    button.style.display = 'block';
  });
}

const hideplay = () => {
  const playButtons = document.querySelectorAll('.play');
  playButtons.forEach(button => {
    button.style.display = 'none';
  });
}

loadToggle();