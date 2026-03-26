function send() {
  fetch("http://localhost:8000/analyze", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      content: document.getElementById("log").value
    })
  })
  .then(r => r.json())
  .then(d => {
    document.getElementById("out").innerText =
      JSON.stringify(d, null, 2);
  });
}