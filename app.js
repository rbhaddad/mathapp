let pyodideReady = false;
}


initPyodide();


function startApp() {
const nameInput = document.getElementById('studentName');
aluno.nome = nameInput.value.trim();


if (!aluno.nome) {
alert('Digite seu nome');
return;
}


document.getElementById('login').classList.add('hidden');
document.getElementById('dashboard').classList.remove('hidden');
document.getElementById('welcome').innerText = `Olá, ${aluno.nome}`;


if (pyodideReady) {
aluno.nivel = pyodide.runPython(`iniciar_aluno("${aluno.nome}")`);
}


atualizarPainel();
}


function atualizarPainel() {
document.getElementById('status').innerText = `Nível atual: ${aluno.nivel}`;
}


function startActivity() {
document.getElementById('dashboard').classList.add('hidden');
document.getElementById('activity').classList.remove('hidden');


const result = pyodide.runPython(`nova_pergunta()`);
document.getElementById('question').innerText = result[0];
respostaCorreta = result[1];
}


function submitAnswer() {
const ans = parseInt(document.getElementById('answer').value);
if (isNaN(ans)) return;


const result = pyodide.runPython(`verificar(${ans})`);
const correto = result[0];
aluno.nivel = result[1];


document.getElementById('feedback').innerText = correto
? '✅ Resposta correta!'
: '❌ Resposta incorreta. Tente novamente.';
}


function backToPanel() {
document.getElementById('activity').classList.add('hidden');
document.getElementById('dashboard').classList.remove('hidden');
atualizarPainel();
}