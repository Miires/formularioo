document.querySelector("#form").addEventListener("submit", async function(event) {
  event.preventDefault();

  const nome = document.getElementById("nome").value;
  const email = document.getElementById("email").value;
  const senha = document.getElementById("senha").value;
  const msg = document.getElementById("mensagem");

  if (nome.length < 3) {
    msg.textContent = "Nome deve ter ao menos 3 caracteres.";
    return;
  }

  if (!/^\S+@\S+\.\S+$/.test(email)) {
    msg.textContent = "Email inválido.";
    return;
  }

  if (!/^(?=.*[A-Z])(?=.*\d).{8,}$/.test(senha)) {
    msg.textContent = "Senha deve ter ao menos 8 caracteres, uma letra maiúscula e um número.";
    return;
  }

  const res = await fetch("/registrar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": "chave-secreta-123"
    },
    body: JSON.stringify({ nome, email, senha })
  });

  const dados = await res.json();
  msg.textContent = dados.message;
});
