const toggleSwitchChange = () => {
  const toggleSwitch = document.getElementById('toggleSwitch');
  const select = document.getElementById('languageSelect');
  const translationForm = document.querySelector('form[method="get"]');
  let isToggleOn = toggleSwitch.checked;

  isToggleOn = toggleSwitch.checked;
  localStorage.setItem('isToggleOn', isToggleOn ? 'true' : 'false');

  select.disabled = !isToggleOn;

  if (isToggleOn) {
    showPlayButtons();
  } else {
    hidePlayButtons();
    select.selectedIndex = 0;
  }
}

const showPlayButtons = () => {
  const playButtons = document.querySelectorAll('.play');
  playButtons.forEach(button => {
    button.style.display = 'block';
  });
}

const hidePlayButtons = () => {
  const playButtons = document.querySelectorAll('.play');
  playButtons.forEach(button => {
    button.style.display = 'none';
  });
}

const loadToggleStatus = () => {
  const toggleSwitch = document.getElementById('toggleSwitch');
  const select = document.getElementById('languageSelect');
  const playButtons = document.querySelectorAll('.play');

  const storedToggleStatus = localStorage.getItem('isToggleOn');
  if (storedToggleStatus === 'true') {
    toggleSwitch.checked = true;
    select.disabled = false;
    showPlayButtons();
  } else {
    toggleSwitch.checked = false;
    select.selectedIndex = 0;
    hidePlayButtons();
  }
}

const languageSelectChange = () => {
  const translationForm = document.querySelector('form[method="get"]');
  translationForm.submit();
}

const playButtonClick = (e) => {
  const translation = e.target.getAttribute('data-translation');
  const menuId = e.target.getAttribute('data-menu-id');
  const detailURL = `/menu/${menuId}/`;
  const translationContent = document.getElementById('translationContent');
  translationContent.textContent = translation;

  const menuDetailLink = document.querySelector('.buka-menu-button');

  if (menuDetailLink) {
    menuDetailLink.href = detailURL;
  }
}

document.getElementById('toggleSwitch').addEventListener('change', toggleSwitchChange);
document.getElementById('languageSelect').addEventListener('change', languageSelectChange);
document.querySelectorAll('.play').forEach(button => {
  button.addEventListener('click', playButtonClick);
});

loadToggleStatus();
