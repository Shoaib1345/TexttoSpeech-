document.getElementById("btn2").addEventListener("click", async function() {
  const res = await fetch("/stop", { method: "POST" });
  const data = await res.json();
  const audio = document.getElementById("audioPlayer");
  audio.pause();
  alert(data.status);
});
