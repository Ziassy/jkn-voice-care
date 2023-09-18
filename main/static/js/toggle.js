const loadToggle = () => {

  const storedToggleStatus = localStorage.getItem('isToggleOn');
  if (storedToggleStatus === 'true') {
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


// Function to replace spaces with underscores
const replaceSpacesWithUnderscoresDetail = (str) => {
  return str.replace(/\s+/g, ' ');
};

const playButtonDetailClick = (e) => {
  const menuName = e.target.getAttribute('data-menu-name');
  const audioPlayer = document.getElementById('audioPlayer');

  const isButtonMenu = e.target.getAttribute('data-isbuttonmenu');


  // Replace spaces with underscores in menuName
  const menuNameWithoutSpaces = replaceSpacesWithUnderscoresDetail(menuName);

  if (isButtonMenu === 'true') {
    // Construct the audio file URL based on the menuName
    const audioURL = `/media/audio-detail-${menuNameWithoutSpaces}.mp3`; // Adjust the file format as needed

    // Set the audio source and display the audio player
    audioPlayer.src = audioURL;
    audioPlayer.play();
  } else {

    // Construct the audio file URL based on the menuName
    const audioURL = `/media/audio-${menuNameWithoutSpaces}.mp3`; // Adjust the file format as needed

    // Set the audio source and display the audio player
    audioPlayer.src = audioURL;
    audioPlayer.play();
  }

};

loadToggle();
document.querySelectorAll('.play').forEach(button => {
  button.addEventListener('click', playButtonDetailClick);
});