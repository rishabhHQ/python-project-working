const audio = document.getElementById('mediaPlayer');
const playPauseBtn = document.getElementById('playPause');
const stopBtn = document.getElementById('stop');
const seekBar = document.getElementById('seekBar');
const volumeBar = document.getElementById('volumeBar');
const select = document.getElementById('mediaSelect');

// Play / Pause
playPauseBtn.addEventListener('click', () => {
    if (audio.paused) { audio.play(); playPauseBtn.textContent = '⏸️ Pause'; }
    else { audio.pause(); playPauseBtn.textContent = '▶️ Play'; }
});

// Stop
stopBtn.addEventListener('click', () => { audio.pause(); audio.currentTime = 0; playPauseBtn.textContent = '▶️ Play'; });

// Progress
audio.addEventListener('timeupdate', () => {
    seekBar.value = (audio.currentTime / audio.duration) * 100;
});
seekBar.addEventListener('input', () => {
    audio.currentTime = (seekBar.value / 100) * audio.duration;
});

// Volume
volumeBar.addEventListener('input', () => { audio.volume = volumeBar.value; });

// Change media
select.addEventListener('change', () => { audio.src = select.value; audio.play(); });
