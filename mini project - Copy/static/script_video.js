const video = document.getElementById('mediaPlayer');
const playPauseBtn = document.getElementById('playPause');
const stopBtn = document.getElementById('stop');
const fullscreenBtn = document.getElementById('fullscreen');
const seekBar = document.getElementById('seekBar');
const volumeBar = document.getElementById('volumeBar');
const select = document.getElementById('mediaSelect');

// Play / Pause
playPauseBtn.addEventListener('click', () => {
    if (video.paused) { video.play(); playPauseBtn.textContent = '⏸️ Pause'; }
    else { video.pause(); playPauseBtn.textContent = '▶️ Play'; }
});

// Stop
stopBtn.addEventListener('click', () => { video.pause(); video.currentTime = 0; playPauseBtn.textContent = '▶️ Play'; });

// Fullscreen
fullscreenBtn.addEventListener('click', () => {
    if (video.requestFullscreen) video.requestFullscreen();
});

// Progress
video.addEventListener('timeupdate', () => {
    seekBar.value = (video.currentTime / video.duration) * 100;
});
seekBar.addEventListener('input', () => {
    video.currentTime = (seekBar.value / 100) * video.duration;
});

// Volume
volumeBar.addEventListener('input', () => { video.volume = volumeBar.value; });

// Change media
select.addEventListener('change', () => { video.src = select.value; video.play(); });
