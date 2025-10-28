document.getElementById("btn3").addEventListener("click", async function() {
  const res = await fetch("/reset", { method: "POST" });
  const data = await res.json();
  const audio = document.getElementById("audioPlayer");
  audio.pause();
  audio.currentTime = 0;
  audio.hidden = true;
  document.getElementById("textInput").value = "";
  alert(data.status);
});
