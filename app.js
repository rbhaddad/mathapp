let pyodide;
let questaoAtual;

async function iniciarPy() {
  pyodide = await loadPyodide();
  const core = await fetch("core.py").then(r => r.text());
  pyodide.runPython(core);
}

async function login() {
  const nome = document.getElementById("nome").value.trim();
  if (!nome) return;

  pyodide.runPython(`estado.nome = "${nome}"; estado.carregar()`);
  document.getElementById("login").style.display = "none";
  document.getElementById("game").style.display = "block";
  novaQuestao();
}

function novaQuestao() {
  questaoAtual = pyodide.runPython(`gerar_questao()`);
  document.getElementById("questao").innerText = questaoAtual.texto;

  const div = document.getElementById("alternativas");
  div.innerHTML = "";

  questaoAtual.alternativas.forEach(a => {
    const btn = document.createElement("button");
    btn.innerText = a;
    btn.onclick = () => responder(a);
    div.appendChild(btn);
  });

  document.getElementById("feedback").innerText = "";
}

function responder(valor) {
  const certo = pyodide.runPython(
    `responder("${questaoAtual.op}", ${questaoAtual.resposta}, ${valor})`
  );

  document.getElementById("feedback").innerText =
    certo ? "✅ Correto!" : `❌ Errado! Resposta: ${questaoAtual.resposta}`;
}

iniciarPy();
